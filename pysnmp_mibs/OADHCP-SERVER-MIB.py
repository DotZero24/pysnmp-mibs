_S='oaDhcpRelayIfName'
_R='oaDhcpRelayServerIp'
_Q='oaDhcpDefaultGWIp'
_P='oaDhcpDefaultGWSubnetMask'
_O='oaDhcpDefaultGWSubnetIp'
_N='oaDhcpIpRangeStart'
_M='oaDhcpIpRangeSubnetMask'
_L='oaDhcpIpRangeSubnetIp'
_K='oaDhcpSubnetMask'
_J='oaDhcpSubnetIp'
_I='oaDhcpInterfaceName'
_H='oaDhcpNetbiosServerNum'
_G='oaDhcpDNSNum'
_F='NotificationType'
_E='Integer32'
_D='read-only'
_C='OADHCP-SERVER-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HostName(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
class EntryStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('valid',1),('invalid',2),('insert',3)))
class ObjectStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),('disable',2),('other',3)))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaDhcp_ObjectIdentity=ObjectIdentity
oaDhcp=_OaDhcp_ObjectIdentity((1,3,6,1,4,1,6926,1,11))
_OaDhcpServer_ObjectIdentity=ObjectIdentity
oaDhcpServer=_OaDhcpServer_ObjectIdentity((1,3,6,1,4,1,6926,1,11,1))
_OaDhcpServerGeneral_ObjectIdentity=ObjectIdentity
oaDhcpServerGeneral=_OaDhcpServerGeneral_ObjectIdentity((1,3,6,1,4,1,6926,1,11,1,1))
_OaDhcpServerStatus_Type=ObjectStatus
_OaDhcpServerStatus_Object=MibScalar
oaDhcpServerStatus=_OaDhcpServerStatus_Object((1,3,6,1,4,1,6926,1,11,1,1,1),_OaDhcpServerStatus_Type())
oaDhcpServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpServerStatus.setStatus(_A)
class _OaDhcpNetbiosNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('B-node',2),('P-node',3),('M-node',4),('H-node',5)))
_OaDhcpNetbiosNodeType_Type.__name__=_E
_OaDhcpNetbiosNodeType_Object=MibScalar
oaDhcpNetbiosNodeType=_OaDhcpNetbiosNodeType_Object((1,3,6,1,4,1,6926,1,11,1,1,2),_OaDhcpNetbiosNodeType_Type())
oaDhcpNetbiosNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpNetbiosNodeType.setStatus(_A)
_OaDhcpDomainName_Type=HostName
_OaDhcpDomainName_Object=MibScalar
oaDhcpDomainName=_OaDhcpDomainName_Object((1,3,6,1,4,1,6926,1,11,1,1,3),_OaDhcpDomainName_Type())
oaDhcpDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpDomainName.setStatus(_A)
_OaDhcpDefaultLeaseTime_Type=Integer32
_OaDhcpDefaultLeaseTime_Object=MibScalar
oaDhcpDefaultLeaseTime=_OaDhcpDefaultLeaseTime_Object((1,3,6,1,4,1,6926,1,11,1,1,4),_OaDhcpDefaultLeaseTime_Type())
oaDhcpDefaultLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpDefaultLeaseTime.setStatus(_A)
_OaDhcpMaxLeaseTime_Type=Integer32
_OaDhcpMaxLeaseTime_Object=MibScalar
oaDhcpMaxLeaseTime=_OaDhcpMaxLeaseTime_Object((1,3,6,1,4,1,6926,1,11,1,1,5),_OaDhcpMaxLeaseTime_Type())
oaDhcpMaxLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpMaxLeaseTime.setStatus(_A)
_OaDhcpDNSTable_Object=MibTable
oaDhcpDNSTable=_OaDhcpDNSTable_Object((1,3,6,1,4,1,6926,1,11,1,2))
if mibBuilder.loadTexts:oaDhcpDNSTable.setStatus(_A)
_OaDhcpDNSEntry_Object=MibTableRow
oaDhcpDNSEntry=_OaDhcpDNSEntry_Object((1,3,6,1,4,1,6926,1,11,1,2,1))
oaDhcpDNSEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:oaDhcpDNSEntry.setStatus(_A)
_OaDhcpDNSNum_Type=Integer32
_OaDhcpDNSNum_Object=MibTableColumn
oaDhcpDNSNum=_OaDhcpDNSNum_Object((1,3,6,1,4,1,6926,1,11,1,2,1,1),_OaDhcpDNSNum_Type())
oaDhcpDNSNum.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpDNSNum.setStatus(_A)
_OaDhcpDNSIp_Type=IpAddress
_OaDhcpDNSIp_Object=MibTableColumn
oaDhcpDNSIp=_OaDhcpDNSIp_Object((1,3,6,1,4,1,6926,1,11,1,2,1,2),_OaDhcpDNSIp_Type())
oaDhcpDNSIp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpDNSIp.setStatus(_A)
_OaDhcpDNSStatus_Type=EntryStatus
_OaDhcpDNSStatus_Object=MibTableColumn
oaDhcpDNSStatus=_OaDhcpDNSStatus_Object((1,3,6,1,4,1,6926,1,11,1,2,1,3),_OaDhcpDNSStatus_Type())
oaDhcpDNSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpDNSStatus.setStatus(_A)
_OaDhcpNetbiosServersTable_Object=MibTable
oaDhcpNetbiosServersTable=_OaDhcpNetbiosServersTable_Object((1,3,6,1,4,1,6926,1,11,1,3))
if mibBuilder.loadTexts:oaDhcpNetbiosServersTable.setStatus(_A)
_OaDhcpNetbiosServersEntry_Object=MibTableRow
oaDhcpNetbiosServersEntry=_OaDhcpNetbiosServersEntry_Object((1,3,6,1,4,1,6926,1,11,1,3,1))
oaDhcpNetbiosServersEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:oaDhcpNetbiosServersEntry.setStatus(_A)
_OaDhcpNetbiosServerNum_Type=Integer32
_OaDhcpNetbiosServerNum_Object=MibTableColumn
oaDhcpNetbiosServerNum=_OaDhcpNetbiosServerNum_Object((1,3,6,1,4,1,6926,1,11,1,3,1,1),_OaDhcpNetbiosServerNum_Type())
oaDhcpNetbiosServerNum.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpNetbiosServerNum.setStatus(_A)
_OaDhcpNetbiosServerIp_Type=IpAddress
_OaDhcpNetbiosServerIp_Object=MibTableColumn
oaDhcpNetbiosServerIp=_OaDhcpNetbiosServerIp_Object((1,3,6,1,4,1,6926,1,11,1,3,1,2),_OaDhcpNetbiosServerIp_Type())
oaDhcpNetbiosServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpNetbiosServerIp.setStatus(_A)
_OaDhcpNetbiosServerStatus_Type=EntryStatus
_OaDhcpNetbiosServerStatus_Object=MibTableColumn
oaDhcpNetbiosServerStatus=_OaDhcpNetbiosServerStatus_Object((1,3,6,1,4,1,6926,1,11,1,3,1,3),_OaDhcpNetbiosServerStatus_Type())
oaDhcpNetbiosServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpNetbiosServerStatus.setStatus(_A)
_OaDhcpSubnetConfigTable_Object=MibTable
oaDhcpSubnetConfigTable=_OaDhcpSubnetConfigTable_Object((1,3,6,1,4,1,6926,1,11,1,4))
if mibBuilder.loadTexts:oaDhcpSubnetConfigTable.setStatus(_A)
_OaDhcpSubnetConfigEntry_Object=MibTableRow
oaDhcpSubnetConfigEntry=_OaDhcpSubnetConfigEntry_Object((1,3,6,1,4,1,6926,1,11,1,4,1))
oaDhcpSubnetConfigEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:oaDhcpSubnetConfigEntry.setStatus(_A)
_OaDhcpInterfaceName_Type=DisplayString
_OaDhcpInterfaceName_Object=MibTableColumn
oaDhcpInterfaceName=_OaDhcpInterfaceName_Object((1,3,6,1,4,1,6926,1,11,1,4,1,1),_OaDhcpInterfaceName_Type())
oaDhcpInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpInterfaceName.setStatus(_A)
_OaDhcpSubnetIp_Type=IpAddress
_OaDhcpSubnetIp_Object=MibTableColumn
oaDhcpSubnetIp=_OaDhcpSubnetIp_Object((1,3,6,1,4,1,6926,1,11,1,4,1,2),_OaDhcpSubnetIp_Type())
oaDhcpSubnetIp.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpSubnetIp.setStatus(_A)
_OaDhcpSubnetMask_Type=IpAddress
_OaDhcpSubnetMask_Object=MibTableColumn
oaDhcpSubnetMask=_OaDhcpSubnetMask_Object((1,3,6,1,4,1,6926,1,11,1,4,1,3),_OaDhcpSubnetMask_Type())
oaDhcpSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpSubnetMask.setStatus(_A)
_OaDhcpOptionSubnetMask_Type=IpAddress
_OaDhcpOptionSubnetMask_Object=MibTableColumn
oaDhcpOptionSubnetMask=_OaDhcpOptionSubnetMask_Object((1,3,6,1,4,1,6926,1,11,1,4,1,4),_OaDhcpOptionSubnetMask_Type())
oaDhcpOptionSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpOptionSubnetMask.setStatus(_A)
_OaDhcpIsOptionMask_Type=ObjectStatus
_OaDhcpIsOptionMask_Object=MibTableColumn
oaDhcpIsOptionMask=_OaDhcpIsOptionMask_Object((1,3,6,1,4,1,6926,1,11,1,4,1,5),_OaDhcpIsOptionMask_Type())
oaDhcpIsOptionMask.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpIsOptionMask.setStatus(_A)
_OaDhcpSubnetConfigStatus_Type=EntryStatus
_OaDhcpSubnetConfigStatus_Object=MibTableColumn
oaDhcpSubnetConfigStatus=_OaDhcpSubnetConfigStatus_Object((1,3,6,1,4,1,6926,1,11,1,4,1,6),_OaDhcpSubnetConfigStatus_Type())
oaDhcpSubnetConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpSubnetConfigStatus.setStatus(_A)
_OaDhcpIpRangeTable_Object=MibTable
oaDhcpIpRangeTable=_OaDhcpIpRangeTable_Object((1,3,6,1,4,1,6926,1,11,1,5))
if mibBuilder.loadTexts:oaDhcpIpRangeTable.setStatus(_A)
_OaDhcpIpRangeEntry_Object=MibTableRow
oaDhcpIpRangeEntry=_OaDhcpIpRangeEntry_Object((1,3,6,1,4,1,6926,1,11,1,5,1))
oaDhcpIpRangeEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:oaDhcpIpRangeEntry.setStatus(_A)
_OaDhcpIpRangeSubnetIp_Type=IpAddress
_OaDhcpIpRangeSubnetIp_Object=MibTableColumn
oaDhcpIpRangeSubnetIp=_OaDhcpIpRangeSubnetIp_Object((1,3,6,1,4,1,6926,1,11,1,5,1,1),_OaDhcpIpRangeSubnetIp_Type())
oaDhcpIpRangeSubnetIp.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpIpRangeSubnetIp.setStatus(_A)
_OaDhcpIpRangeSubnetMask_Type=IpAddress
_OaDhcpIpRangeSubnetMask_Object=MibTableColumn
oaDhcpIpRangeSubnetMask=_OaDhcpIpRangeSubnetMask_Object((1,3,6,1,4,1,6926,1,11,1,5,1,2),_OaDhcpIpRangeSubnetMask_Type())
oaDhcpIpRangeSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpIpRangeSubnetMask.setStatus(_A)
_OaDhcpIpRangeStart_Type=IpAddress
_OaDhcpIpRangeStart_Object=MibTableColumn
oaDhcpIpRangeStart=_OaDhcpIpRangeStart_Object((1,3,6,1,4,1,6926,1,11,1,5,1,3),_OaDhcpIpRangeStart_Type())
oaDhcpIpRangeStart.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpIpRangeStart.setStatus(_A)
_OaDhcpIpRangeEnd_Type=IpAddress
_OaDhcpIpRangeEnd_Object=MibTableColumn
oaDhcpIpRangeEnd=_OaDhcpIpRangeEnd_Object((1,3,6,1,4,1,6926,1,11,1,5,1,4),_OaDhcpIpRangeEnd_Type())
oaDhcpIpRangeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpIpRangeEnd.setStatus(_A)
_OaDhcpIpRangeStatus_Type=EntryStatus
_OaDhcpIpRangeStatus_Object=MibTableColumn
oaDhcpIpRangeStatus=_OaDhcpIpRangeStatus_Object((1,3,6,1,4,1,6926,1,11,1,5,1,5),_OaDhcpIpRangeStatus_Type())
oaDhcpIpRangeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpIpRangeStatus.setStatus(_A)
_OaDhcpDefaultGWTable_Object=MibTable
oaDhcpDefaultGWTable=_OaDhcpDefaultGWTable_Object((1,3,6,1,4,1,6926,1,11,1,6))
if mibBuilder.loadTexts:oaDhcpDefaultGWTable.setStatus(_A)
_OaDhcpDefaultGWEntry_Object=MibTableRow
oaDhcpDefaultGWEntry=_OaDhcpDefaultGWEntry_Object((1,3,6,1,4,1,6926,1,11,1,6,1))
oaDhcpDefaultGWEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:oaDhcpDefaultGWEntry.setStatus(_A)
_OaDhcpDefaultGWSubnetIp_Type=IpAddress
_OaDhcpDefaultGWSubnetIp_Object=MibTableColumn
oaDhcpDefaultGWSubnetIp=_OaDhcpDefaultGWSubnetIp_Object((1,3,6,1,4,1,6926,1,11,1,6,1,1),_OaDhcpDefaultGWSubnetIp_Type())
oaDhcpDefaultGWSubnetIp.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpDefaultGWSubnetIp.setStatus(_A)
_OaDhcpDefaultGWSubnetMask_Type=IpAddress
_OaDhcpDefaultGWSubnetMask_Object=MibTableColumn
oaDhcpDefaultGWSubnetMask=_OaDhcpDefaultGWSubnetMask_Object((1,3,6,1,4,1,6926,1,11,1,6,1,2),_OaDhcpDefaultGWSubnetMask_Type())
oaDhcpDefaultGWSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpDefaultGWSubnetMask.setStatus(_A)
_OaDhcpDefaultGWIp_Type=IpAddress
_OaDhcpDefaultGWIp_Object=MibTableColumn
oaDhcpDefaultGWIp=_OaDhcpDefaultGWIp_Object((1,3,6,1,4,1,6926,1,11,1,6,1,3),_OaDhcpDefaultGWIp_Type())
oaDhcpDefaultGWIp.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpDefaultGWIp.setStatus(_A)
_OaDhcpDefaultGWStatus_Type=EntryStatus
_OaDhcpDefaultGWStatus_Object=MibTableColumn
oaDhcpDefaultGWStatus=_OaDhcpDefaultGWStatus_Object((1,3,6,1,4,1,6926,1,11,1,6,1,4),_OaDhcpDefaultGWStatus_Type())
oaDhcpDefaultGWStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpDefaultGWStatus.setStatus(_A)
_OaDhcpRelay_ObjectIdentity=ObjectIdentity
oaDhcpRelay=_OaDhcpRelay_ObjectIdentity((1,3,6,1,4,1,6926,1,11,2))
_OaDhcpRelayGeneral_ObjectIdentity=ObjectIdentity
oaDhcpRelayGeneral=_OaDhcpRelayGeneral_ObjectIdentity((1,3,6,1,4,1,6926,1,11,2,1))
_OaDhcpRelayStatus_Type=ObjectStatus
_OaDhcpRelayStatus_Object=MibScalar
oaDhcpRelayStatus=_OaDhcpRelayStatus_Object((1,3,6,1,4,1,6926,1,11,2,1,1),_OaDhcpRelayStatus_Type())
oaDhcpRelayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpRelayStatus.setStatus(_A)
class _OaDhcpRelayClearConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('None',1),('ResetConfig',2)))
_OaDhcpRelayClearConfig_Type.__name__=_E
_OaDhcpRelayClearConfig_Object=MibScalar
oaDhcpRelayClearConfig=_OaDhcpRelayClearConfig_Object((1,3,6,1,4,1,6926,1,11,2,1,2),_OaDhcpRelayClearConfig_Type())
oaDhcpRelayClearConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpRelayClearConfig.setStatus(_A)
_OaDhcpRelayServerTable_Object=MibTable
oaDhcpRelayServerTable=_OaDhcpRelayServerTable_Object((1,3,6,1,4,1,6926,1,11,2,2))
if mibBuilder.loadTexts:oaDhcpRelayServerTable.setStatus(_A)
_OaDhcpRelayServerEntry_Object=MibTableRow
oaDhcpRelayServerEntry=_OaDhcpRelayServerEntry_Object((1,3,6,1,4,1,6926,1,11,2,2,1))
oaDhcpRelayServerEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:oaDhcpRelayServerEntry.setStatus(_A)
_OaDhcpRelayServerIp_Type=IpAddress
_OaDhcpRelayServerIp_Object=MibTableColumn
oaDhcpRelayServerIp=_OaDhcpRelayServerIp_Object((1,3,6,1,4,1,6926,1,11,2,2,1,1),_OaDhcpRelayServerIp_Type())
oaDhcpRelayServerIp.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpRelayServerIp.setStatus(_A)
_OaDhcpRelayServerStatus_Type=EntryStatus
_OaDhcpRelayServerStatus_Object=MibTableColumn
oaDhcpRelayServerStatus=_OaDhcpRelayServerStatus_Object((1,3,6,1,4,1,6926,1,11,2,2,1,2),_OaDhcpRelayServerStatus_Type())
oaDhcpRelayServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpRelayServerStatus.setStatus(_A)
_OaDhcpRelayInterfaceTable_Object=MibTable
oaDhcpRelayInterfaceTable=_OaDhcpRelayInterfaceTable_Object((1,3,6,1,4,1,6926,1,11,2,3))
if mibBuilder.loadTexts:oaDhcpRelayInterfaceTable.setStatus(_A)
_OaDhcpRelayInterfaceEntry_Object=MibTableRow
oaDhcpRelayInterfaceEntry=_OaDhcpRelayInterfaceEntry_Object((1,3,6,1,4,1,6926,1,11,2,3,1))
oaDhcpRelayInterfaceEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:oaDhcpRelayInterfaceEntry.setStatus(_A)
_OaDhcpRelayIfName_Type=DisplayString
_OaDhcpRelayIfName_Object=MibTableColumn
oaDhcpRelayIfName=_OaDhcpRelayIfName_Object((1,3,6,1,4,1,6926,1,11,2,3,1,1),_OaDhcpRelayIfName_Type())
oaDhcpRelayIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:oaDhcpRelayIfName.setStatus(_A)
_OaDhcpRelayIfStatus_Type=EntryStatus
_OaDhcpRelayIfStatus_Object=MibTableColumn
oaDhcpRelayIfStatus=_OaDhcpRelayIfStatus_Object((1,3,6,1,4,1,6926,1,11,2,3,1,2),_OaDhcpRelayIfStatus_Type())
oaDhcpRelayIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oaDhcpRelayIfStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HostName':HostName,'EntryStatus':EntryStatus,'ObjectStatus':ObjectStatus,'oaccess':oaccess,'oaManagement':oaManagement,'oaDhcp':oaDhcp,'oaDhcpServer':oaDhcpServer,'oaDhcpServerGeneral':oaDhcpServerGeneral,'oaDhcpServerStatus':oaDhcpServerStatus,'oaDhcpNetbiosNodeType':oaDhcpNetbiosNodeType,'oaDhcpDomainName':oaDhcpDomainName,'oaDhcpDefaultLeaseTime':oaDhcpDefaultLeaseTime,'oaDhcpMaxLeaseTime':oaDhcpMaxLeaseTime,'oaDhcpDNSTable':oaDhcpDNSTable,'oaDhcpDNSEntry':oaDhcpDNSEntry,_G:oaDhcpDNSNum,'oaDhcpDNSIp':oaDhcpDNSIp,'oaDhcpDNSStatus':oaDhcpDNSStatus,'oaDhcpNetbiosServersTable':oaDhcpNetbiosServersTable,'oaDhcpNetbiosServersEntry':oaDhcpNetbiosServersEntry,_H:oaDhcpNetbiosServerNum,'oaDhcpNetbiosServerIp':oaDhcpNetbiosServerIp,'oaDhcpNetbiosServerStatus':oaDhcpNetbiosServerStatus,'oaDhcpSubnetConfigTable':oaDhcpSubnetConfigTable,'oaDhcpSubnetConfigEntry':oaDhcpSubnetConfigEntry,_I:oaDhcpInterfaceName,_J:oaDhcpSubnetIp,_K:oaDhcpSubnetMask,'oaDhcpOptionSubnetMask':oaDhcpOptionSubnetMask,'oaDhcpIsOptionMask':oaDhcpIsOptionMask,'oaDhcpSubnetConfigStatus':oaDhcpSubnetConfigStatus,'oaDhcpIpRangeTable':oaDhcpIpRangeTable,'oaDhcpIpRangeEntry':oaDhcpIpRangeEntry,_L:oaDhcpIpRangeSubnetIp,_M:oaDhcpIpRangeSubnetMask,_N:oaDhcpIpRangeStart,'oaDhcpIpRangeEnd':oaDhcpIpRangeEnd,'oaDhcpIpRangeStatus':oaDhcpIpRangeStatus,'oaDhcpDefaultGWTable':oaDhcpDefaultGWTable,'oaDhcpDefaultGWEntry':oaDhcpDefaultGWEntry,_O:oaDhcpDefaultGWSubnetIp,_P:oaDhcpDefaultGWSubnetMask,_Q:oaDhcpDefaultGWIp,'oaDhcpDefaultGWStatus':oaDhcpDefaultGWStatus,'oaDhcpRelay':oaDhcpRelay,'oaDhcpRelayGeneral':oaDhcpRelayGeneral,'oaDhcpRelayStatus':oaDhcpRelayStatus,'oaDhcpRelayClearConfig':oaDhcpRelayClearConfig,'oaDhcpRelayServerTable':oaDhcpRelayServerTable,'oaDhcpRelayServerEntry':oaDhcpRelayServerEntry,_R:oaDhcpRelayServerIp,'oaDhcpRelayServerStatus':oaDhcpRelayServerStatus,'oaDhcpRelayInterfaceTable':oaDhcpRelayInterfaceTable,'oaDhcpRelayInterfaceEntry':oaDhcpRelayInterfaceEntry,_S:oaDhcpRelayIfName,'oaDhcpRelayIfStatus':oaDhcpRelayIfStatus})