_O='rcIpDhcpIpLeaseIndex'
_N='rcIpDhcpIpOptionCode'
_M='rcIpDhcpRelayIndex'
_L='rcIpDhcpIpIfIndex'
_K='EnableVar'
_J='rcIpDhcpIpIndex'
_I='OctetString'
_H='not-accessible'
_G='IPDHCP-SERVER-MIB'
_F='read-write'
_E='mandatory'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
EnableVar,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_K,'Vlanset')
rcIpDhcpServer=ModuleIdentity((1,3,6,1,4,1,8886,6,1,29))
if mibBuilder.loadTexts:rcIpDhcpServer.setRevisions(('2007-10-15 00:00','2008-06-24 00:00','2009-07-14 00:00','2009-09-02 00:00','2009-09-09 00:00'))
_RcIpDhcpServerConfig_ObjectIdentity=ObjectIdentity
rcIpDhcpServerConfig=_RcIpDhcpServerConfig_ObjectIdentity((1,3,6,1,4,1,8886,6,1,29,1))
class _RcIpDhcpPropEnable_Type(EnableVar):defaultValue=2
_RcIpDhcpPropEnable_Type.__name__=_K
_RcIpDhcpPropEnable_Object=MibScalar
rcIpDhcpPropEnable=_RcIpDhcpPropEnable_Object((1,3,6,1,4,1,8886,6,1,29,1,1),_RcIpDhcpPropEnable_Type())
rcIpDhcpPropEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpPropEnable.setStatus(_A)
_RcIpDhcpIpNextIndex_Type=Integer32
_RcIpDhcpIpNextIndex_Object=MibScalar
rcIpDhcpIpNextIndex=_RcIpDhcpIpNextIndex_Object((1,3,6,1,4,1,8886,6,1,29,1,2),_RcIpDhcpIpNextIndex_Type())
rcIpDhcpIpNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpNextIndex.setStatus(_A)
class _RcIpDhcpMaxLease_Type(Integer32):defaultValue=10080;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcIpDhcpMaxLease_Type.__name__=_D
_RcIpDhcpMaxLease_Object=MibScalar
rcIpDhcpMaxLease=_RcIpDhcpMaxLease_Object((1,3,6,1,4,1,8886,6,1,29,1,3),_RcIpDhcpMaxLease_Type())
rcIpDhcpMaxLease.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpMaxLease.setStatus(_A)
class _RcIpDhcpMinLease_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcIpDhcpMinLease_Type.__name__=_D
_RcIpDhcpMinLease_Object=MibScalar
rcIpDhcpMinLease=_RcIpDhcpMinLease_Object((1,3,6,1,4,1,8886,6,1,29,1,4),_RcIpDhcpMinLease_Type())
rcIpDhcpMinLease.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpMinLease.setStatus(_A)
class _RcIpDhcpDefLease_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcIpDhcpDefLease_Type.__name__=_D
_RcIpDhcpDefLease_Object=MibScalar
rcIpDhcpDefLease=_RcIpDhcpDefLease_Object((1,3,6,1,4,1,8886,6,1,29,1,5),_RcIpDhcpDefLease_Type())
rcIpDhcpDefLease.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpDefLease.setStatus(_A)
_RcIpDhcpVlanAuth_Type=Vlanset
_RcIpDhcpVlanAuth_Object=MibScalar
rcIpDhcpVlanAuth=_RcIpDhcpVlanAuth_Object((1,3,6,1,4,1,8886,6,1,29,1,6),_RcIpDhcpVlanAuth_Type())
rcIpDhcpVlanAuth.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpVlanAuth.setStatus(_A)
_RcIpDhcpServerStartTime_Type=TimeTicks
_RcIpDhcpServerStartTime_Object=MibScalar
rcIpDhcpServerStartTime=_RcIpDhcpServerStartTime_Object((1,3,6,1,4,1,8886,6,1,29,1,7),_RcIpDhcpServerStartTime_Type())
rcIpDhcpServerStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStartTime.setStatus(_A)
_RcIpDhcpIpIfTable_Object=MibTable
rcIpDhcpIpIfTable=_RcIpDhcpIpIfTable_Object((1,3,6,1,4,1,8886,6,1,29,1,8))
if mibBuilder.loadTexts:rcIpDhcpIpIfTable.setStatus(_A)
_RcIpDhcpIpIfEntry_Object=MibTableRow
rcIpDhcpIpIfEntry=_RcIpDhcpIpIfEntry_Object((1,3,6,1,4,1,8886,6,1,29,1,8,1))
rcIpDhcpIpIfEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:rcIpDhcpIpIfEntry.setStatus(_A)
_RcIpDhcpIpIfIndex_Type=Integer32
_RcIpDhcpIpIfIndex_Object=MibTableColumn
rcIpDhcpIpIfIndex=_RcIpDhcpIpIfIndex_Object((1,3,6,1,4,1,8886,6,1,29,1,8,1,1),_RcIpDhcpIpIfIndex_Type())
rcIpDhcpIpIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rcIpDhcpIpIfIndex.setStatus(_A)
_RcIpDhcpIpIfDhcpsEnable_Type=EnableVar
_RcIpDhcpIpIfDhcpsEnable_Object=MibTableColumn
rcIpDhcpIpIfDhcpsEnable=_RcIpDhcpIpIfDhcpsEnable_Object((1,3,6,1,4,1,8886,6,1,29,1,8,1,2),_RcIpDhcpIpIfDhcpsEnable_Type())
rcIpDhcpIpIfDhcpsEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpIpIfDhcpsEnable.setStatus(_A)
_RcIpDhcpIpTable_Object=MibTable
rcIpDhcpIpTable=_RcIpDhcpIpTable_Object((1,3,6,1,4,1,8886,6,1,29,1,9))
if mibBuilder.loadTexts:rcIpDhcpIpTable.setStatus(_A)
_RcIpDhcpIpEntry_Object=MibTableRow
rcIpDhcpIpEntry=_RcIpDhcpIpEntry_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1))
rcIpDhcpIpEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:rcIpDhcpIpEntry.setStatus(_A)
_RcIpDhcpIpIndex_Type=Integer32
_RcIpDhcpIpIndex_Object=MibTableColumn
rcIpDhcpIpIndex=_RcIpDhcpIpIndex_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,1),_RcIpDhcpIpIndex_Type())
rcIpDhcpIpIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rcIpDhcpIpIndex.setStatus(_A)
class _RcIpDhcpIpEntryName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcIpDhcpIpEntryName_Type.__name__=_I
_RcIpDhcpIpEntryName_Object=MibTableColumn
rcIpDhcpIpEntryName=_RcIpDhcpIpEntryName_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,2),_RcIpDhcpIpEntryName_Type())
rcIpDhcpIpEntryName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpEntryName.setStatus(_A)
_RcIpDhcpIpInterface_Type=Integer32
_RcIpDhcpIpInterface_Object=MibTableColumn
rcIpDhcpIpInterface=_RcIpDhcpIpInterface_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,3),_RcIpDhcpIpInterface_Type())
rcIpDhcpIpInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpInterface.setStatus(_A)
_RcIpDhcpIpStartIp_Type=IpAddress
_RcIpDhcpIpStartIp_Object=MibTableColumn
rcIpDhcpIpStartIp=_RcIpDhcpIpStartIp_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,4),_RcIpDhcpIpStartIp_Type())
rcIpDhcpIpStartIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpStartIp.setStatus(_A)
_RcIpDhcpIpEndIp_Type=IpAddress
_RcIpDhcpIpEndIp_Object=MibTableColumn
rcIpDhcpIpEndIp=_RcIpDhcpIpEndIp_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,5),_RcIpDhcpIpEndIp_Type())
rcIpDhcpIpEndIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpEndIp.setStatus(_A)
_RcIpDhcpIpNetmask_Type=IpAddress
_RcIpDhcpIpNetmask_Object=MibTableColumn
rcIpDhcpIpNetmask=_RcIpDhcpIpNetmask_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,6),_RcIpDhcpIpNetmask_Type())
rcIpDhcpIpNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpNetmask.setStatus(_A)
_RcIpDhcpIpGateway_Type=IpAddress
_RcIpDhcpIpGateway_Object=MibTableColumn
rcIpDhcpIpGateway=_RcIpDhcpIpGateway_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,7),_RcIpDhcpIpGateway_Type())
rcIpDhcpIpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpGateway.setStatus(_A)
_RcIpDhcpIpDnsServer_Type=IpAddress
_RcIpDhcpIpDnsServer_Object=MibTableColumn
rcIpDhcpIpDnsServer=_RcIpDhcpIpDnsServer_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,8),_RcIpDhcpIpDnsServer_Type())
rcIpDhcpIpDnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpDnsServer.setStatus(_A)
_RcIpDhcpIpSecondaryDnsServer_Type=IpAddress
_RcIpDhcpIpSecondaryDnsServer_Object=MibTableColumn
rcIpDhcpIpSecondaryDnsServer=_RcIpDhcpIpSecondaryDnsServer_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,9),_RcIpDhcpIpSecondaryDnsServer_Type())
rcIpDhcpIpSecondaryDnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpSecondaryDnsServer.setStatus(_A)
_RcIpDhcpIpRowStatus_Type=RowStatus
_RcIpDhcpIpRowStatus_Object=MibTableColumn
rcIpDhcpIpRowStatus=_RcIpDhcpIpRowStatus_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,10),_RcIpDhcpIpRowStatus_Type())
rcIpDhcpIpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpRowStatus.setStatus(_A)
_RcIpDhcpIpTftpSvrAddress_Type=IpAddress
_RcIpDhcpIpTftpSvrAddress_Object=MibTableColumn
rcIpDhcpIpTftpSvrAddress=_RcIpDhcpIpTftpSvrAddress_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,11),_RcIpDhcpIpTftpSvrAddress_Type())
rcIpDhcpIpTftpSvrAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpTftpSvrAddress.setStatus(_A)
class _RcIpDhcpIpBootfileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_RcIpDhcpIpBootfileName_Type.__name__=_I
_RcIpDhcpIpBootfileName_Object=MibTableColumn
rcIpDhcpIpBootfileName=_RcIpDhcpIpBootfileName_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,12),_RcIpDhcpIpBootfileName_Type())
rcIpDhcpIpBootfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpBootfileName.setStatus(_A)
class _RcIpDhcpIpMaxLease_Type(Integer32):defaultValue=10080;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcIpDhcpIpMaxLease_Type.__name__=_D
_RcIpDhcpIpMaxLease_Object=MibTableColumn
rcIpDhcpIpMaxLease=_RcIpDhcpIpMaxLease_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,13),_RcIpDhcpIpMaxLease_Type())
rcIpDhcpIpMaxLease.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpMaxLease.setStatus(_A)
class _RcIpDhcpIpMinLease_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcIpDhcpIpMinLease_Type.__name__=_D
_RcIpDhcpIpMinLease_Object=MibTableColumn
rcIpDhcpIpMinLease=_RcIpDhcpIpMinLease_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,14),_RcIpDhcpIpMinLease_Type())
rcIpDhcpIpMinLease.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpMinLease.setStatus(_A)
class _RcIpDhcpIpDefLease_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcIpDhcpIpDefLease_Type.__name__=_D
_RcIpDhcpIpDefLease_Object=MibTableColumn
rcIpDhcpIpDefLease=_RcIpDhcpIpDefLease_Object((1,3,6,1,4,1,8886,6,1,29,1,9,1,15),_RcIpDhcpIpDefLease_Type())
rcIpDhcpIpDefLease.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpDefLease.setStatus(_A)
class _RcIpDhcpRelayNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcIpDhcpRelayNextIndex_Type.__name__=_D
_RcIpDhcpRelayNextIndex_Object=MibScalar
rcIpDhcpRelayNextIndex=_RcIpDhcpRelayNextIndex_Object((1,3,6,1,4,1,8886,6,1,29,1,10),_RcIpDhcpRelayNextIndex_Type())
rcIpDhcpRelayNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpRelayNextIndex.setStatus(_A)
_RcIpDhcpRelayTable_Object=MibTable
rcIpDhcpRelayTable=_RcIpDhcpRelayTable_Object((1,3,6,1,4,1,8886,6,1,29,1,11))
if mibBuilder.loadTexts:rcIpDhcpRelayTable.setStatus(_A)
_RcIpDhcpRelayEntry_Object=MibTableRow
rcIpDhcpRelayEntry=_RcIpDhcpRelayEntry_Object((1,3,6,1,4,1,8886,6,1,29,1,11,1))
rcIpDhcpRelayEntry.setIndexNames((0,_G,_M))
if mibBuilder.loadTexts:rcIpDhcpRelayEntry.setStatus(_A)
_RcIpDhcpRelayIndex_Type=Integer32
_RcIpDhcpRelayIndex_Object=MibTableColumn
rcIpDhcpRelayIndex=_RcIpDhcpRelayIndex_Object((1,3,6,1,4,1,8886,6,1,29,1,11,1,1),_RcIpDhcpRelayIndex_Type())
rcIpDhcpRelayIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rcIpDhcpRelayIndex.setStatus(_A)
_RcIpDhcpRelayAddress_Type=IpAddress
_RcIpDhcpRelayAddress_Object=MibTableColumn
rcIpDhcpRelayAddress=_RcIpDhcpRelayAddress_Object((1,3,6,1,4,1,8886,6,1,29,1,11,1,2),_RcIpDhcpRelayAddress_Type())
rcIpDhcpRelayAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpRelayAddress.setStatus(_A)
_RcIpDhcpRelayMask_Type=IpAddress
_RcIpDhcpRelayMask_Object=MibTableColumn
rcIpDhcpRelayMask=_RcIpDhcpRelayMask_Object((1,3,6,1,4,1,8886,6,1,29,1,11,1,3),_RcIpDhcpRelayMask_Type())
rcIpDhcpRelayMask.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpRelayMask.setStatus(_A)
_RcIpDhcpRelayRowStatus_Type=RowStatus
_RcIpDhcpRelayRowStatus_Object=MibTableColumn
rcIpDhcpRelayRowStatus=_RcIpDhcpRelayRowStatus_Object((1,3,6,1,4,1,8886,6,1,29,1,11,1,4),_RcIpDhcpRelayRowStatus_Type())
rcIpDhcpRelayRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpRelayRowStatus.setStatus(_A)
_RcIpDhcpIpVendorOptTable_Object=MibTable
rcIpDhcpIpVendorOptTable=_RcIpDhcpIpVendorOptTable_Object((1,3,6,1,4,1,8886,6,1,29,1,12))
if mibBuilder.loadTexts:rcIpDhcpIpVendorOptTable.setStatus(_A)
_RcIpDhcpIpVendorOptEntry_Object=MibTableRow
rcIpDhcpIpVendorOptEntry=_RcIpDhcpIpVendorOptEntry_Object((1,3,6,1,4,1,8886,6,1,29,1,12,1))
rcIpDhcpIpVendorOptEntry.setIndexNames((0,_G,_J),(0,_G,_N))
if mibBuilder.loadTexts:rcIpDhcpIpVendorOptEntry.setStatus(_A)
class _RcIpDhcpIpOptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_RcIpDhcpIpOptionCode_Type.__name__=_D
_RcIpDhcpIpOptionCode_Object=MibTableColumn
rcIpDhcpIpOptionCode=_RcIpDhcpIpOptionCode_Object((1,3,6,1,4,1,8886,6,1,29,1,12,1,1),_RcIpDhcpIpOptionCode_Type())
rcIpDhcpIpOptionCode.setMaxAccess(_H)
if mibBuilder.loadTexts:rcIpDhcpIpOptionCode.setStatus(_A)
class _RcIpDhcpIpOptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_RcIpDhcpIpOptionType_Type.__name__=_D
_RcIpDhcpIpOptionType_Object=MibTableColumn
rcIpDhcpIpOptionType=_RcIpDhcpIpOptionType_Object((1,3,6,1,4,1,8886,6,1,29,1,12,1,2),_RcIpDhcpIpOptionType_Type())
rcIpDhcpIpOptionType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpOptionType.setStatus(_A)
class _RcIpDhcpIpOptionContents_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,192))
_RcIpDhcpIpOptionContents_Type.__name__=_I
_RcIpDhcpIpOptionContents_Object=MibTableColumn
rcIpDhcpIpOptionContents=_RcIpDhcpIpOptionContents_Object((1,3,6,1,4,1,8886,6,1,29,1,12,1,3),_RcIpDhcpIpOptionContents_Type())
rcIpDhcpIpOptionContents.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpOptionContents.setStatus(_A)
class _RcIpDhcpIpOptionLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,192))
_RcIpDhcpIpOptionLength_Type.__name__=_D
_RcIpDhcpIpOptionLength_Object=MibTableColumn
rcIpDhcpIpOptionLength=_RcIpDhcpIpOptionLength_Object((1,3,6,1,4,1,8886,6,1,29,1,12,1,4),_RcIpDhcpIpOptionLength_Type())
rcIpDhcpIpOptionLength.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpOptionLength.setStatus(_A)
_RcIpDhcpIpOptionRowStatus_Type=RowStatus
_RcIpDhcpIpOptionRowStatus_Object=MibTableColumn
rcIpDhcpIpOptionRowStatus=_RcIpDhcpIpOptionRowStatus_Object((1,3,6,1,4,1,8886,6,1,29,1,12,1,5),_RcIpDhcpIpOptionRowStatus_Type())
rcIpDhcpIpOptionRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcIpDhcpIpOptionRowStatus.setStatus(_A)
_RcIpDhcpIpRelayInformationOption_Type=EnableVar
_RcIpDhcpIpRelayInformationOption_Object=MibScalar
rcIpDhcpIpRelayInformationOption=_RcIpDhcpIpRelayInformationOption_Object((1,3,6,1,4,1,8886,6,1,29,1,13),_RcIpDhcpIpRelayInformationOption_Type())
rcIpDhcpIpRelayInformationOption.setMaxAccess(_F)
if mibBuilder.loadTexts:rcIpDhcpIpRelayInformationOption.setStatus(_A)
class _RcIpDhcpIpOptionRowNumCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_RcIpDhcpIpOptionRowNumCurrent_Type.__name__=_D
_RcIpDhcpIpOptionRowNumCurrent_Object=MibScalar
rcIpDhcpIpOptionRowNumCurrent=_RcIpDhcpIpOptionRowNumCurrent_Object((1,3,6,1,4,1,8886,6,1,29,1,14),_RcIpDhcpIpOptionRowNumCurrent_Type())
rcIpDhcpIpOptionRowNumCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpOptionRowNumCurrent.setStatus(_A)
class _RcIpDhcpIpOptionRowNumHistoryMax_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_RcIpDhcpIpOptionRowNumHistoryMax_Type.__name__=_D
_RcIpDhcpIpOptionRowNumHistoryMax_Object=MibScalar
rcIpDhcpIpOptionRowNumHistoryMax=_RcIpDhcpIpOptionRowNumHistoryMax_Object((1,3,6,1,4,1,8886,6,1,29,1,15),_RcIpDhcpIpOptionRowNumHistoryMax_Type())
rcIpDhcpIpOptionRowNumHistoryMax.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpOptionRowNumHistoryMax.setStatus(_A)
_RcIpDhcpServerStatistics_ObjectIdentity=ObjectIdentity
rcIpDhcpServerStatistics=_RcIpDhcpServerStatistics_ObjectIdentity((1,3,6,1,4,1,8886,6,1,29,2))
_RcIpDhcpServerStatsBootps_Type=Counter32
_RcIpDhcpServerStatsBootps_Object=MibScalar
rcIpDhcpServerStatsBootps=_RcIpDhcpServerStatsBootps_Object((1,3,6,1,4,1,8886,6,1,29,2,1),_RcIpDhcpServerStatsBootps_Type())
rcIpDhcpServerStatsBootps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsBootps.setStatus(_E)
_RcIpDhcpServerStatsDiscovers_Type=Counter32
_RcIpDhcpServerStatsDiscovers_Object=MibScalar
rcIpDhcpServerStatsDiscovers=_RcIpDhcpServerStatsDiscovers_Object((1,3,6,1,4,1,8886,6,1,29,2,2),_RcIpDhcpServerStatsDiscovers_Type())
rcIpDhcpServerStatsDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsDiscovers.setStatus(_E)
_RcIpDhcpServerStatsRequests_Type=Counter32
_RcIpDhcpServerStatsRequests_Object=MibScalar
rcIpDhcpServerStatsRequests=_RcIpDhcpServerStatsRequests_Object((1,3,6,1,4,1,8886,6,1,29,2,3),_RcIpDhcpServerStatsRequests_Type())
rcIpDhcpServerStatsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsRequests.setStatus(_E)
_RcIpDhcpServerStatsReleases_Type=Counter32
_RcIpDhcpServerStatsReleases_Object=MibScalar
rcIpDhcpServerStatsReleases=_RcIpDhcpServerStatsReleases_Object((1,3,6,1,4,1,8886,6,1,29,2,4),_RcIpDhcpServerStatsReleases_Type())
rcIpDhcpServerStatsReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsReleases.setStatus(_E)
_RcIpDhcpServerStatsOffers_Type=Counter32
_RcIpDhcpServerStatsOffers_Object=MibScalar
rcIpDhcpServerStatsOffers=_RcIpDhcpServerStatsOffers_Object((1,3,6,1,4,1,8886,6,1,29,2,5),_RcIpDhcpServerStatsOffers_Type())
rcIpDhcpServerStatsOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsOffers.setStatus(_E)
_RcIpDhcpServerStatsAcks_Type=Counter32
_RcIpDhcpServerStatsAcks_Object=MibScalar
rcIpDhcpServerStatsAcks=_RcIpDhcpServerStatsAcks_Object((1,3,6,1,4,1,8886,6,1,29,2,6),_RcIpDhcpServerStatsAcks_Type())
rcIpDhcpServerStatsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsAcks.setStatus(_E)
_RcIpDhcpServerStatsNacks_Type=Counter32
_RcIpDhcpServerStatsNacks_Object=MibScalar
rcIpDhcpServerStatsNacks=_RcIpDhcpServerStatsNacks_Object((1,3,6,1,4,1,8886,6,1,29,2,7),_RcIpDhcpServerStatsNacks_Type())
rcIpDhcpServerStatsNacks.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsNacks.setStatus(_E)
_RcIpDhcpServerStatsDeclines_Type=Counter32
_RcIpDhcpServerStatsDeclines_Object=MibScalar
rcIpDhcpServerStatsDeclines=_RcIpDhcpServerStatsDeclines_Object((1,3,6,1,4,1,8886,6,1,29,2,8),_RcIpDhcpServerStatsDeclines_Type())
rcIpDhcpServerStatsDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsDeclines.setStatus(_E)
_RcIpDhcpServerStatsInformations_Type=Counter32
_RcIpDhcpServerStatsInformations_Object=MibScalar
rcIpDhcpServerStatsInformations=_RcIpDhcpServerStatsInformations_Object((1,3,6,1,4,1,8886,6,1,29,2,9),_RcIpDhcpServerStatsInformations_Type())
rcIpDhcpServerStatsInformations.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsInformations.setStatus(_E)
_RcIpDhcpServerStatsUnknows_Type=Counter32
_RcIpDhcpServerStatsUnknows_Object=MibScalar
rcIpDhcpServerStatsUnknows=_RcIpDhcpServerStatsUnknows_Object((1,3,6,1,4,1,8886,6,1,29,2,10),_RcIpDhcpServerStatsUnknows_Type())
rcIpDhcpServerStatsUnknows.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsUnknows.setStatus(_E)
_RcIpDhcpServerStatsPackets_Type=Counter32
_RcIpDhcpServerStatsPackets_Object=MibScalar
rcIpDhcpServerStatsPackets=_RcIpDhcpServerStatsPackets_Object((1,3,6,1,4,1,8886,6,1,29,2,11),_RcIpDhcpServerStatsPackets_Type())
rcIpDhcpServerStatsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpServerStatsPackets.setStatus(_E)
_RcIpDhcpIpLease_ObjectIdentity=ObjectIdentity
rcIpDhcpIpLease=_RcIpDhcpIpLease_ObjectIdentity((1,3,6,1,4,1,8886,6,1,29,3))
_RcIpDhcpIpLeaseTable_Object=MibTable
rcIpDhcpIpLeaseTable=_RcIpDhcpIpLeaseTable_Object((1,3,6,1,4,1,8886,6,1,29,3,1))
if mibBuilder.loadTexts:rcIpDhcpIpLeaseTable.setStatus(_A)
_RcIpDhcpIpLeaseEntry_Object=MibTableRow
rcIpDhcpIpLeaseEntry=_RcIpDhcpIpLeaseEntry_Object((1,3,6,1,4,1,8886,6,1,29,3,1,1))
rcIpDhcpIpLeaseEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:rcIpDhcpIpLeaseEntry.setStatus(_A)
_RcIpDhcpIpLeaseIndex_Type=Integer32
_RcIpDhcpIpLeaseIndex_Object=MibTableColumn
rcIpDhcpIpLeaseIndex=_RcIpDhcpIpLeaseIndex_Object((1,3,6,1,4,1,8886,6,1,29,3,1,1,1),_RcIpDhcpIpLeaseIndex_Type())
rcIpDhcpIpLeaseIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:rcIpDhcpIpLeaseIndex.setStatus(_A)
_RcIpDhcpIpLeaseIpAddres_Type=IpAddress
_RcIpDhcpIpLeaseIpAddres_Object=MibTableColumn
rcIpDhcpIpLeaseIpAddres=_RcIpDhcpIpLeaseIpAddres_Object((1,3,6,1,4,1,8886,6,1,29,3,1,1,2),_RcIpDhcpIpLeaseIpAddres_Type())
rcIpDhcpIpLeaseIpAddres.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpLeaseIpAddres.setStatus(_A)
_RcIpDhcpIpLeaseClientMacAddress_Type=MacAddress
_RcIpDhcpIpLeaseClientMacAddress_Object=MibTableColumn
rcIpDhcpIpLeaseClientMacAddress=_RcIpDhcpIpLeaseClientMacAddress_Object((1,3,6,1,4,1,8886,6,1,29,3,1,1,3),_RcIpDhcpIpLeaseClientMacAddress_Type())
rcIpDhcpIpLeaseClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpLeaseClientMacAddress.setStatus(_A)
_RcIpDhcpIpLeaseExpiration_Type=Integer32
_RcIpDhcpIpLeaseExpiration_Object=MibTableColumn
rcIpDhcpIpLeaseExpiration=_RcIpDhcpIpLeaseExpiration_Object((1,3,6,1,4,1,8886,6,1,29,3,1,1,4),_RcIpDhcpIpLeaseExpiration_Type())
rcIpDhcpIpLeaseExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpLeaseExpiration.setStatus(_A)
_RcIpDhcpIpLeaseIpInterface_Type=Integer32
_RcIpDhcpIpLeaseIpInterface_Object=MibTableColumn
rcIpDhcpIpLeaseIpInterface=_RcIpDhcpIpLeaseIpInterface_Object((1,3,6,1,4,1,8886,6,1,29,3,1,1,5),_RcIpDhcpIpLeaseIpInterface_Type())
rcIpDhcpIpLeaseIpInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:rcIpDhcpIpLeaseIpInterface.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'rcIpDhcpServer':rcIpDhcpServer,'rcIpDhcpServerConfig':rcIpDhcpServerConfig,'rcIpDhcpPropEnable':rcIpDhcpPropEnable,'rcIpDhcpIpNextIndex':rcIpDhcpIpNextIndex,'rcIpDhcpMaxLease':rcIpDhcpMaxLease,'rcIpDhcpMinLease':rcIpDhcpMinLease,'rcIpDhcpDefLease':rcIpDhcpDefLease,'rcIpDhcpVlanAuth':rcIpDhcpVlanAuth,'rcIpDhcpServerStartTime':rcIpDhcpServerStartTime,'rcIpDhcpIpIfTable':rcIpDhcpIpIfTable,'rcIpDhcpIpIfEntry':rcIpDhcpIpIfEntry,_L:rcIpDhcpIpIfIndex,'rcIpDhcpIpIfDhcpsEnable':rcIpDhcpIpIfDhcpsEnable,'rcIpDhcpIpTable':rcIpDhcpIpTable,'rcIpDhcpIpEntry':rcIpDhcpIpEntry,_J:rcIpDhcpIpIndex,'rcIpDhcpIpEntryName':rcIpDhcpIpEntryName,'rcIpDhcpIpInterface':rcIpDhcpIpInterface,'rcIpDhcpIpStartIp':rcIpDhcpIpStartIp,'rcIpDhcpIpEndIp':rcIpDhcpIpEndIp,'rcIpDhcpIpNetmask':rcIpDhcpIpNetmask,'rcIpDhcpIpGateway':rcIpDhcpIpGateway,'rcIpDhcpIpDnsServer':rcIpDhcpIpDnsServer,'rcIpDhcpIpSecondaryDnsServer':rcIpDhcpIpSecondaryDnsServer,'rcIpDhcpIpRowStatus':rcIpDhcpIpRowStatus,'rcIpDhcpIpTftpSvrAddress':rcIpDhcpIpTftpSvrAddress,'rcIpDhcpIpBootfileName':rcIpDhcpIpBootfileName,'rcIpDhcpIpMaxLease':rcIpDhcpIpMaxLease,'rcIpDhcpIpMinLease':rcIpDhcpIpMinLease,'rcIpDhcpIpDefLease':rcIpDhcpIpDefLease,'rcIpDhcpRelayNextIndex':rcIpDhcpRelayNextIndex,'rcIpDhcpRelayTable':rcIpDhcpRelayTable,'rcIpDhcpRelayEntry':rcIpDhcpRelayEntry,_M:rcIpDhcpRelayIndex,'rcIpDhcpRelayAddress':rcIpDhcpRelayAddress,'rcIpDhcpRelayMask':rcIpDhcpRelayMask,'rcIpDhcpRelayRowStatus':rcIpDhcpRelayRowStatus,'rcIpDhcpIpVendorOptTable':rcIpDhcpIpVendorOptTable,'rcIpDhcpIpVendorOptEntry':rcIpDhcpIpVendorOptEntry,_N:rcIpDhcpIpOptionCode,'rcIpDhcpIpOptionType':rcIpDhcpIpOptionType,'rcIpDhcpIpOptionContents':rcIpDhcpIpOptionContents,'rcIpDhcpIpOptionLength':rcIpDhcpIpOptionLength,'rcIpDhcpIpOptionRowStatus':rcIpDhcpIpOptionRowStatus,'rcIpDhcpIpRelayInformationOption':rcIpDhcpIpRelayInformationOption,'rcIpDhcpIpOptionRowNumCurrent':rcIpDhcpIpOptionRowNumCurrent,'rcIpDhcpIpOptionRowNumHistoryMax':rcIpDhcpIpOptionRowNumHistoryMax,'rcIpDhcpServerStatistics':rcIpDhcpServerStatistics,'rcIpDhcpServerStatsBootps':rcIpDhcpServerStatsBootps,'rcIpDhcpServerStatsDiscovers':rcIpDhcpServerStatsDiscovers,'rcIpDhcpServerStatsRequests':rcIpDhcpServerStatsRequests,'rcIpDhcpServerStatsReleases':rcIpDhcpServerStatsReleases,'rcIpDhcpServerStatsOffers':rcIpDhcpServerStatsOffers,'rcIpDhcpServerStatsAcks':rcIpDhcpServerStatsAcks,'rcIpDhcpServerStatsNacks':rcIpDhcpServerStatsNacks,'rcIpDhcpServerStatsDeclines':rcIpDhcpServerStatsDeclines,'rcIpDhcpServerStatsInformations':rcIpDhcpServerStatsInformations,'rcIpDhcpServerStatsUnknows':rcIpDhcpServerStatsUnknows,'rcIpDhcpServerStatsPackets':rcIpDhcpServerStatsPackets,'rcIpDhcpIpLease':rcIpDhcpIpLease,'rcIpDhcpIpLeaseTable':rcIpDhcpIpLeaseTable,'rcIpDhcpIpLeaseEntry':rcIpDhcpIpLeaseEntry,_O:rcIpDhcpIpLeaseIndex,'rcIpDhcpIpLeaseIpAddres':rcIpDhcpIpLeaseIpAddres,'rcIpDhcpIpLeaseClientMacAddress':rcIpDhcpIpLeaseClientMacAddress,'rcIpDhcpIpLeaseExpiration':rcIpDhcpIpLeaseExpiration,'rcIpDhcpIpLeaseIpInterface':rcIpDhcpIpLeaseIpInterface})