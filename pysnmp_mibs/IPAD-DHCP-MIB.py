_N='ipadDhcpPortIndex'
_M='ipadDhcpAddressStatusIndex'
_L='ipadDhcpAddressListIndex'
_K='ipadDhcpStaticEntryIndex'
_J='ipadDhcpServerHostIndex'
_I='enable'
_H='disable'
_G='addnew'
_F='IPAD-DHCP-MIB'
_E='other'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ipad,=mibBuilder.importSymbols('IPADv2-MIB','ipad')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipadDhcp=ModuleIdentity((1,3,6,1,4,1,321,100,1,27))
_IpadDhcpParms_ObjectIdentity=ObjectIdentity
ipadDhcpParms=_IpadDhcpParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,27,1))
class _IpadDhcpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_IpadDhcpEnable_Type.__name__=_D
_IpadDhcpEnable_Object=MibScalar
ipadDhcpEnable=_IpadDhcpEnable_Object((1,3,6,1,4,1,321,100,1,27,1,1),_IpadDhcpEnable_Type())
ipadDhcpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpEnable.setStatus(_A)
_IpadDhcpNumberPorts_Type=Integer32
_IpadDhcpNumberPorts_Object=MibScalar
ipadDhcpNumberPorts=_IpadDhcpNumberPorts_Object((1,3,6,1,4,1,321,100,1,27,1,2),_IpadDhcpNumberPorts_Type())
ipadDhcpNumberPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpNumberPorts.setStatus(_A)
_IpadDhcpTTL_Type=Integer32
_IpadDhcpTTL_Object=MibScalar
ipadDhcpTTL=_IpadDhcpTTL_Object((1,3,6,1,4,1,321,100,1,27,1,3),_IpadDhcpTTL_Type())
ipadDhcpTTL.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpTTL.setStatus(_A)
_IpadDhcpServiceType_Type=Integer32
_IpadDhcpServiceType_Object=MibScalar
ipadDhcpServiceType=_IpadDhcpServiceType_Object((1,3,6,1,4,1,321,100,1,27,1,4),_IpadDhcpServiceType_Type())
ipadDhcpServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServiceType.setStatus(_A)
_IpadDhcpLeaseTime_Type=Integer32
_IpadDhcpLeaseTime_Object=MibScalar
ipadDhcpLeaseTime=_IpadDhcpLeaseTime_Object((1,3,6,1,4,1,321,100,1,27,1,5),_IpadDhcpLeaseTime_Type())
ipadDhcpLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpLeaseTime.setStatus(_A)
_IpadDhcpServerDatabasePrimaryDnsIpAddress_Type=IpAddress
_IpadDhcpServerDatabasePrimaryDnsIpAddress_Object=MibScalar
ipadDhcpServerDatabasePrimaryDnsIpAddress=_IpadDhcpServerDatabasePrimaryDnsIpAddress_Object((1,3,6,1,4,1,321,100,1,27,1,6),_IpadDhcpServerDatabasePrimaryDnsIpAddress_Type())
ipadDhcpServerDatabasePrimaryDnsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerDatabasePrimaryDnsIpAddress.setStatus(_A)
_IpadDhcpServerDatabaseSecondaryDnsIpAddress_Type=IpAddress
_IpadDhcpServerDatabaseSecondaryDnsIpAddress_Object=MibScalar
ipadDhcpServerDatabaseSecondaryDnsIpAddress=_IpadDhcpServerDatabaseSecondaryDnsIpAddress_Object((1,3,6,1,4,1,321,100,1,27,1,7),_IpadDhcpServerDatabaseSecondaryDnsIpAddress_Type())
ipadDhcpServerDatabaseSecondaryDnsIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerDatabaseSecondaryDnsIpAddress.setStatus(_A)
_IpadDhcpServerDatabaseDomainName_Type=DisplayString
_IpadDhcpServerDatabaseDomainName_Object=MibScalar
ipadDhcpServerDatabaseDomainName=_IpadDhcpServerDatabaseDomainName_Object((1,3,6,1,4,1,321,100,1,27,1,8),_IpadDhcpServerDatabaseDomainName_Type())
ipadDhcpServerDatabaseDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerDatabaseDomainName.setStatus(_A)
_IpadDhcpServerDatabaseRouterIpAddress_Type=IpAddress
_IpadDhcpServerDatabaseRouterIpAddress_Object=MibScalar
ipadDhcpServerDatabaseRouterIpAddress=_IpadDhcpServerDatabaseRouterIpAddress_Object((1,3,6,1,4,1,321,100,1,27,1,9),_IpadDhcpServerDatabaseRouterIpAddress_Type())
ipadDhcpServerDatabaseRouterIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerDatabaseRouterIpAddress.setStatus(_A)
_IpadDhcpServerHostNameTable_Object=MibTable
ipadDhcpServerHostNameTable=_IpadDhcpServerHostNameTable_Object((1,3,6,1,4,1,321,100,1,27,1,10))
if mibBuilder.loadTexts:ipadDhcpServerHostNameTable.setStatus(_A)
_IpadDhcpServerHostNameTableEntry_Object=MibTableRow
ipadDhcpServerHostNameTableEntry=_IpadDhcpServerHostNameTableEntry_Object((1,3,6,1,4,1,321,100,1,27,1,10,1))
ipadDhcpServerHostNameTableEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:ipadDhcpServerHostNameTableEntry.setStatus(_A)
_IpadDhcpServerHostIndex_Type=Integer32
_IpadDhcpServerHostIndex_Object=MibTableColumn
ipadDhcpServerHostIndex=_IpadDhcpServerHostIndex_Object((1,3,6,1,4,1,321,100,1,27,1,10,1,1),_IpadDhcpServerHostIndex_Type())
ipadDhcpServerHostIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpServerHostIndex.setStatus(_A)
_IpadDhcpServerHostName_Type=DisplayString
_IpadDhcpServerHostName_Object=MibTableColumn
ipadDhcpServerHostName=_IpadDhcpServerHostName_Object((1,3,6,1,4,1,321,100,1,27,1,10,1,2),_IpadDhcpServerHostName_Type())
ipadDhcpServerHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerHostName.setStatus(_A)
class _IpadDhcpServerHostAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_IpadDhcpServerHostAdd_Type.__name__=_D
_IpadDhcpServerHostAdd_Object=MibScalar
ipadDhcpServerHostAdd=_IpadDhcpServerHostAdd_Object((1,3,6,1,4,1,321,100,1,27,1,11),_IpadDhcpServerHostAdd_Type())
ipadDhcpServerHostAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerHostAdd.setStatus(_A)
_IpadDhcpServerHostDelete_Type=Integer32
_IpadDhcpServerHostDelete_Object=MibScalar
ipadDhcpServerHostDelete=_IpadDhcpServerHostDelete_Object((1,3,6,1,4,1,321,100,1,27,1,12),_IpadDhcpServerHostDelete_Type())
ipadDhcpServerHostDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerHostDelete.setStatus(_A)
_IpadDhcpStaticEntryTable_Object=MibTable
ipadDhcpStaticEntryTable=_IpadDhcpStaticEntryTable_Object((1,3,6,1,4,1,321,100,1,27,1,13))
if mibBuilder.loadTexts:ipadDhcpStaticEntryTable.setStatus(_A)
_IpadDhcpStaticEntryTableEntry_Object=MibTableRow
ipadDhcpStaticEntryTableEntry=_IpadDhcpStaticEntryTableEntry_Object((1,3,6,1,4,1,321,100,1,27,1,13,1))
ipadDhcpStaticEntryTableEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:ipadDhcpStaticEntryTableEntry.setStatus(_A)
_IpadDhcpStaticEntryIndex_Type=Integer32
_IpadDhcpStaticEntryIndex_Object=MibTableColumn
ipadDhcpStaticEntryIndex=_IpadDhcpStaticEntryIndex_Object((1,3,6,1,4,1,321,100,1,27,1,13,1,1),_IpadDhcpStaticEntryIndex_Type())
ipadDhcpStaticEntryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpStaticEntryIndex.setStatus(_A)
_IpadDhcpStaticEntryMacAddress_Type=OctetString
_IpadDhcpStaticEntryMacAddress_Object=MibTableColumn
ipadDhcpStaticEntryMacAddress=_IpadDhcpStaticEntryMacAddress_Object((1,3,6,1,4,1,321,100,1,27,1,13,1,2),_IpadDhcpStaticEntryMacAddress_Type())
ipadDhcpStaticEntryMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpStaticEntryMacAddress.setStatus(_A)
_IpadDhcpStaticEntryIpAddress_Type=IpAddress
_IpadDhcpStaticEntryIpAddress_Object=MibTableColumn
ipadDhcpStaticEntryIpAddress=_IpadDhcpStaticEntryIpAddress_Object((1,3,6,1,4,1,321,100,1,27,1,13,1,3),_IpadDhcpStaticEntryIpAddress_Type())
ipadDhcpStaticEntryIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpStaticEntryIpAddress.setStatus(_A)
_IpadDhcpStaticEntryMaskAddress_Type=IpAddress
_IpadDhcpStaticEntryMaskAddress_Object=MibTableColumn
ipadDhcpStaticEntryMaskAddress=_IpadDhcpStaticEntryMaskAddress_Object((1,3,6,1,4,1,321,100,1,27,1,13,1,4),_IpadDhcpStaticEntryMaskAddress_Type())
ipadDhcpStaticEntryMaskAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpStaticEntryMaskAddress.setStatus(_A)
_IpadDhcpStaticEntryHostName_Type=DisplayString
_IpadDhcpStaticEntryHostName_Object=MibTableColumn
ipadDhcpStaticEntryHostName=_IpadDhcpStaticEntryHostName_Object((1,3,6,1,4,1,321,100,1,27,1,13,1,5),_IpadDhcpStaticEntryHostName_Type())
ipadDhcpStaticEntryHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpStaticEntryHostName.setStatus(_A)
class _IpadDhcpStaticEntryAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_IpadDhcpStaticEntryAdd_Type.__name__=_D
_IpadDhcpStaticEntryAdd_Object=MibScalar
ipadDhcpStaticEntryAdd=_IpadDhcpStaticEntryAdd_Object((1,3,6,1,4,1,321,100,1,27,1,14),_IpadDhcpStaticEntryAdd_Type())
ipadDhcpStaticEntryAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpStaticEntryAdd.setStatus(_A)
_IpadDhcpStaticEntryDelete_Type=Integer32
_IpadDhcpStaticEntryDelete_Object=MibScalar
ipadDhcpStaticEntryDelete=_IpadDhcpStaticEntryDelete_Object((1,3,6,1,4,1,321,100,1,27,1,15),_IpadDhcpStaticEntryDelete_Type())
ipadDhcpStaticEntryDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpStaticEntryDelete.setStatus(_A)
_IpadDhcpAddressListTable_Object=MibTable
ipadDhcpAddressListTable=_IpadDhcpAddressListTable_Object((1,3,6,1,4,1,321,100,1,27,1,16))
if mibBuilder.loadTexts:ipadDhcpAddressListTable.setStatus(_A)
_IpadDhcpAddressListTableEntry_Object=MibTableRow
ipadDhcpAddressListTableEntry=_IpadDhcpAddressListTableEntry_Object((1,3,6,1,4,1,321,100,1,27,1,16,1))
ipadDhcpAddressListTableEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:ipadDhcpAddressListTableEntry.setStatus(_A)
_IpadDhcpAddressListIndex_Type=Integer32
_IpadDhcpAddressListIndex_Object=MibTableColumn
ipadDhcpAddressListIndex=_IpadDhcpAddressListIndex_Object((1,3,6,1,4,1,321,100,1,27,1,16,1,1),_IpadDhcpAddressListIndex_Type())
ipadDhcpAddressListIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpAddressListIndex.setStatus(_A)
_IpadDhcpAddressListIpStart_Type=IpAddress
_IpadDhcpAddressListIpStart_Object=MibTableColumn
ipadDhcpAddressListIpStart=_IpadDhcpAddressListIpStart_Object((1,3,6,1,4,1,321,100,1,27,1,16,1,2),_IpadDhcpAddressListIpStart_Type())
ipadDhcpAddressListIpStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpAddressListIpStart.setStatus(_A)
_IpadDhcpAddressListIpEnd_Type=IpAddress
_IpadDhcpAddressListIpEnd_Object=MibTableColumn
ipadDhcpAddressListIpEnd=_IpadDhcpAddressListIpEnd_Object((1,3,6,1,4,1,321,100,1,27,1,16,1,3),_IpadDhcpAddressListIpEnd_Type())
ipadDhcpAddressListIpEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpAddressListIpEnd.setStatus(_A)
_IpadDhcpAddressListSubnetMask_Type=IpAddress
_IpadDhcpAddressListSubnetMask_Object=MibTableColumn
ipadDhcpAddressListSubnetMask=_IpadDhcpAddressListSubnetMask_Object((1,3,6,1,4,1,321,100,1,27,1,16,1,4),_IpadDhcpAddressListSubnetMask_Type())
ipadDhcpAddressListSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpAddressListSubnetMask.setStatus(_A)
_IpadDhcpAddressListIpExcludeStart_Type=IpAddress
_IpadDhcpAddressListIpExcludeStart_Object=MibTableColumn
ipadDhcpAddressListIpExcludeStart=_IpadDhcpAddressListIpExcludeStart_Object((1,3,6,1,4,1,321,100,1,27,1,16,1,5),_IpadDhcpAddressListIpExcludeStart_Type())
ipadDhcpAddressListIpExcludeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpAddressListIpExcludeStart.setStatus(_A)
_IpadDhcpAddressListIpExcludeEnd_Type=IpAddress
_IpadDhcpAddressListIpExcludeEnd_Object=MibTableColumn
ipadDhcpAddressListIpExcludeEnd=_IpadDhcpAddressListIpExcludeEnd_Object((1,3,6,1,4,1,321,100,1,27,1,16,1,6),_IpadDhcpAddressListIpExcludeEnd_Type())
ipadDhcpAddressListIpExcludeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpAddressListIpExcludeEnd.setStatus(_A)
class _IpadDhcpAddressListAdd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_G,2)))
_IpadDhcpAddressListAdd_Type.__name__=_D
_IpadDhcpAddressListAdd_Object=MibScalar
ipadDhcpAddressListAdd=_IpadDhcpAddressListAdd_Object((1,3,6,1,4,1,321,100,1,27,1,17),_IpadDhcpAddressListAdd_Type())
ipadDhcpAddressListAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpAddressListAdd.setStatus(_A)
_IpadDhcpAddressListDelete_Type=Integer32
_IpadDhcpAddressListDelete_Object=MibScalar
ipadDhcpAddressListDelete=_IpadDhcpAddressListDelete_Object((1,3,6,1,4,1,321,100,1,27,1,18),_IpadDhcpAddressListDelete_Type())
ipadDhcpAddressListDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpAddressListDelete.setStatus(_A)
_IpadDhcpAddressStatusTable_Object=MibTable
ipadDhcpAddressStatusTable=_IpadDhcpAddressStatusTable_Object((1,3,6,1,4,1,321,100,1,27,1,19))
if mibBuilder.loadTexts:ipadDhcpAddressStatusTable.setStatus(_A)
_IpadDhcpAddressStatusTableEntry_Object=MibTableRow
ipadDhcpAddressStatusTableEntry=_IpadDhcpAddressStatusTableEntry_Object((1,3,6,1,4,1,321,100,1,27,1,19,1))
ipadDhcpAddressStatusTableEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:ipadDhcpAddressStatusTableEntry.setStatus(_A)
_IpadDhcpAddressStatusIndex_Type=Integer32
_IpadDhcpAddressStatusIndex_Object=MibTableColumn
ipadDhcpAddressStatusIndex=_IpadDhcpAddressStatusIndex_Object((1,3,6,1,4,1,321,100,1,27,1,19,1,1),_IpadDhcpAddressStatusIndex_Type())
ipadDhcpAddressStatusIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpAddressStatusIndex.setStatus(_A)
_IpadDhcpAddressStatusMacAddress_Type=OctetString
_IpadDhcpAddressStatusMacAddress_Object=MibTableColumn
ipadDhcpAddressStatusMacAddress=_IpadDhcpAddressStatusMacAddress_Object((1,3,6,1,4,1,321,100,1,27,1,19,1,2),_IpadDhcpAddressStatusMacAddress_Type())
ipadDhcpAddressStatusMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpAddressStatusMacAddress.setStatus(_A)
_IpadDhcpAddressStatusIpAddress_Type=IpAddress
_IpadDhcpAddressStatusIpAddress_Object=MibTableColumn
ipadDhcpAddressStatusIpAddress=_IpadDhcpAddressStatusIpAddress_Object((1,3,6,1,4,1,321,100,1,27,1,19,1,3),_IpadDhcpAddressStatusIpAddress_Type())
ipadDhcpAddressStatusIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpAddressStatusIpAddress.setStatus(_A)
class _IpadDhcpAddressStatusStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('available',2),('assigned',3)))
_IpadDhcpAddressStatusStatus_Type.__name__=_D
_IpadDhcpAddressStatusStatus_Object=MibTableColumn
ipadDhcpAddressStatusStatus=_IpadDhcpAddressStatusStatus_Object((1,3,6,1,4,1,321,100,1,27,1,19,1,4),_IpadDhcpAddressStatusStatus_Type())
ipadDhcpAddressStatusStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpAddressStatusStatus.setStatus(_A)
_IpadDhcpServerDatabaseWinsPrimary_Type=IpAddress
_IpadDhcpServerDatabaseWinsPrimary_Object=MibScalar
ipadDhcpServerDatabaseWinsPrimary=_IpadDhcpServerDatabaseWinsPrimary_Object((1,3,6,1,4,1,321,100,1,27,1,20),_IpadDhcpServerDatabaseWinsPrimary_Type())
ipadDhcpServerDatabaseWinsPrimary.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerDatabaseWinsPrimary.setStatus(_A)
_IpadDhcpServerDatabaseWinsSecondary_Type=IpAddress
_IpadDhcpServerDatabaseWinsSecondary_Object=MibScalar
ipadDhcpServerDatabaseWinsSecondary=_IpadDhcpServerDatabaseWinsSecondary_Object((1,3,6,1,4,1,321,100,1,27,1,21),_IpadDhcpServerDatabaseWinsSecondary_Type())
ipadDhcpServerDatabaseWinsSecondary.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpServerDatabaseWinsSecondary.setStatus(_A)
_IpadDhcpPortParms_ObjectIdentity=ObjectIdentity
ipadDhcpPortParms=_IpadDhcpPortParms_ObjectIdentity((1,3,6,1,4,1,321,100,1,27,2))
_IpadDhcpPortTable_Object=MibTable
ipadDhcpPortTable=_IpadDhcpPortTable_Object((1,3,6,1,4,1,321,100,1,27,2,1))
if mibBuilder.loadTexts:ipadDhcpPortTable.setStatus(_A)
_IpadDhcpPortTableEntry_Object=MibTableRow
ipadDhcpPortTableEntry=_IpadDhcpPortTableEntry_Object((1,3,6,1,4,1,321,100,1,27,2,1,1))
ipadDhcpPortTableEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:ipadDhcpPortTableEntry.setStatus(_A)
_IpadDhcpPortIndex_Type=Integer32
_IpadDhcpPortIndex_Object=MibTableColumn
ipadDhcpPortIndex=_IpadDhcpPortIndex_Object((1,3,6,1,4,1,321,100,1,27,2,1,1,1),_IpadDhcpPortIndex_Type())
ipadDhcpPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipadDhcpPortIndex.setStatus(_A)
_IpadDhcpPortIpAddress_Type=IpAddress
_IpadDhcpPortIpAddress_Object=MibTableColumn
ipadDhcpPortIpAddress=_IpadDhcpPortIpAddress_Object((1,3,6,1,4,1,321,100,1,27,2,1,1,2),_IpadDhcpPortIpAddress_Type())
ipadDhcpPortIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpPortIpAddress.setStatus(_A)
class _IpadDhcpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3)))
_IpadDhcpPortEnable_Type.__name__=_D
_IpadDhcpPortEnable_Object=MibTableColumn
ipadDhcpPortEnable=_IpadDhcpPortEnable_Object((1,3,6,1,4,1,321,100,1,27,2,1,1,3),_IpadDhcpPortEnable_Type())
ipadDhcpPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpPortEnable.setStatus(_A)
_IpadDhcpPortAdd_Type=Integer32
_IpadDhcpPortAdd_Object=MibScalar
ipadDhcpPortAdd=_IpadDhcpPortAdd_Object((1,3,6,1,4,1,321,100,1,27,2,2),_IpadDhcpPortAdd_Type())
ipadDhcpPortAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpPortAdd.setStatus(_A)
_IpadDhcpPortDelete_Type=Integer32
_IpadDhcpPortDelete_Object=MibScalar
ipadDhcpPortDelete=_IpadDhcpPortDelete_Object((1,3,6,1,4,1,321,100,1,27,2,3),_IpadDhcpPortDelete_Type())
ipadDhcpPortDelete.setMaxAccess(_B)
if mibBuilder.loadTexts:ipadDhcpPortDelete.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ipadDhcp':ipadDhcp,'ipadDhcpParms':ipadDhcpParms,'ipadDhcpEnable':ipadDhcpEnable,'ipadDhcpNumberPorts':ipadDhcpNumberPorts,'ipadDhcpTTL':ipadDhcpTTL,'ipadDhcpServiceType':ipadDhcpServiceType,'ipadDhcpLeaseTime':ipadDhcpLeaseTime,'ipadDhcpServerDatabasePrimaryDnsIpAddress':ipadDhcpServerDatabasePrimaryDnsIpAddress,'ipadDhcpServerDatabaseSecondaryDnsIpAddress':ipadDhcpServerDatabaseSecondaryDnsIpAddress,'ipadDhcpServerDatabaseDomainName':ipadDhcpServerDatabaseDomainName,'ipadDhcpServerDatabaseRouterIpAddress':ipadDhcpServerDatabaseRouterIpAddress,'ipadDhcpServerHostNameTable':ipadDhcpServerHostNameTable,'ipadDhcpServerHostNameTableEntry':ipadDhcpServerHostNameTableEntry,_J:ipadDhcpServerHostIndex,'ipadDhcpServerHostName':ipadDhcpServerHostName,'ipadDhcpServerHostAdd':ipadDhcpServerHostAdd,'ipadDhcpServerHostDelete':ipadDhcpServerHostDelete,'ipadDhcpStaticEntryTable':ipadDhcpStaticEntryTable,'ipadDhcpStaticEntryTableEntry':ipadDhcpStaticEntryTableEntry,_K:ipadDhcpStaticEntryIndex,'ipadDhcpStaticEntryMacAddress':ipadDhcpStaticEntryMacAddress,'ipadDhcpStaticEntryIpAddress':ipadDhcpStaticEntryIpAddress,'ipadDhcpStaticEntryMaskAddress':ipadDhcpStaticEntryMaskAddress,'ipadDhcpStaticEntryHostName':ipadDhcpStaticEntryHostName,'ipadDhcpStaticEntryAdd':ipadDhcpStaticEntryAdd,'ipadDhcpStaticEntryDelete':ipadDhcpStaticEntryDelete,'ipadDhcpAddressListTable':ipadDhcpAddressListTable,'ipadDhcpAddressListTableEntry':ipadDhcpAddressListTableEntry,_L:ipadDhcpAddressListIndex,'ipadDhcpAddressListIpStart':ipadDhcpAddressListIpStart,'ipadDhcpAddressListIpEnd':ipadDhcpAddressListIpEnd,'ipadDhcpAddressListSubnetMask':ipadDhcpAddressListSubnetMask,'ipadDhcpAddressListIpExcludeStart':ipadDhcpAddressListIpExcludeStart,'ipadDhcpAddressListIpExcludeEnd':ipadDhcpAddressListIpExcludeEnd,'ipadDhcpAddressListAdd':ipadDhcpAddressListAdd,'ipadDhcpAddressListDelete':ipadDhcpAddressListDelete,'ipadDhcpAddressStatusTable':ipadDhcpAddressStatusTable,'ipadDhcpAddressStatusTableEntry':ipadDhcpAddressStatusTableEntry,_M:ipadDhcpAddressStatusIndex,'ipadDhcpAddressStatusMacAddress':ipadDhcpAddressStatusMacAddress,'ipadDhcpAddressStatusIpAddress':ipadDhcpAddressStatusIpAddress,'ipadDhcpAddressStatusStatus':ipadDhcpAddressStatusStatus,'ipadDhcpServerDatabaseWinsPrimary':ipadDhcpServerDatabaseWinsPrimary,'ipadDhcpServerDatabaseWinsSecondary':ipadDhcpServerDatabaseWinsSecondary,'ipadDhcpPortParms':ipadDhcpPortParms,'ipadDhcpPortTable':ipadDhcpPortTable,'ipadDhcpPortTableEntry':ipadDhcpPortTableEntry,_N:ipadDhcpPortIndex,'ipadDhcpPortIpAddress':ipadDhcpPortIpAddress,'ipadDhcpPortEnable':ipadDhcpPortEnable,'ipadDhcpPortAdd':ipadDhcpPortAdd,'ipadDhcpPortDelete':ipadDhcpPortDelete})