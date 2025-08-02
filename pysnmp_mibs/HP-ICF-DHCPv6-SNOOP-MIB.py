_AM='hpicfDSnoopV6BaseGroup1'
_AL='hpicfDSnoopV6DbaseFileGroup'
_AK='hpicfDSnoopV6SourceBindingErrantReply'
_AJ='hpicfDSnoopV6SourceBindingOutOfResources'
_AI='hpicfDSnoopV6RateLimit'
_AH='hpicfDSnoopV6DatabaseValidateSFTPServer'
_AG='hpicfDSnoopV6DatabaseSFTPPassword'
_AF='hpicfDSnoopV6DatabaseSFTPUsername'
_AE='hpicfDSnoopV6DatabaseFTPort'
_AD='hpicfDSnoopV6ErrantReplyTrapCtrl'
_AC='hpicfDSnoopV6OutOfResourcesTrapCtrl'
_AB='hpicfDSnoopV6ClearStats'
_AA='hpicfDSnoopV6BindingSecVlan'
_A9='hpicfDSnoopV6BindingLLAddress'
_A8='hpicfDSnoopV6BindingVlanId'
_A7='hpicfDSnoopV6PortDynamicBinding'
_A6='hpicfDSnoopV6PortStaticBinding'
_A5='hpicfDSnoopV6MaxbindPktsDropped'
_A4='hpicfDSnoopV6AuthorizedServerStatus'
_A3='hpicfDSnoopV6StaticBindingEntry'
_A2='hpicfDSnoopV6PortMaxBindingEntry'
_A1='succeeded'
_A0='inProgress'
_z='notConfigured'
_y='not-accessible'
_x='hpicfDSnoopV6AuthorizedServerAddress'
_w='hpicfDSnoopV6AuthorizedServerAddrType'
_v='seconds'
_u='VlanIndex'
_t='hpicfDSnoopV6DbaseFileGroup1'
_s='hpicfDSnoopV6BaseGroup'
_r='hpicfDsnoopV6SourceBindingVlan'
_q='hpicfDsnoopV6SourceBindingIpAddress'
_p='hpicfDsnoopV6SourceBindingIpAddressType'
_o='hpicfDsnoopV6SourceBindingMacAddress'
_n='hpicfDsnoopV6SourceBindingPort'
_m='hpicfDSnoopV6SourceBindingErrantSrcIP'
_l='hpicfDSnoopV6SourceBindingErrantSrcIPType'
_k='hpicfDSnoopV6SourceBindingErrantSrcMAC'
_j='hpicfDSnoopV6SourceBindingNotifyCount'
_i='hpicfDSnoopV6DBFileLastWriteTime'
_h='hpicfDSnoopV6DBFileWriteStatus'
_g='hpicfDSnoopV6DBFileReadStatus'
_f='hpicfDSnoopV6DBFileWriteFailures'
_e='hpicfDSnoopV6DBFileWriteAttempts'
_d='hpicfDSnoopV6DatabaseWriteTimeout'
_c='hpicfDSnoopV6DatabaseWriteDelay'
_b='hpicfDSnoopV6DatabaseFile'
_a='hpicfDSnoopV6SCRelayReplyUntrustedPorts'
_Z='hpicfDSnoopV6SCUntrustedPorts'
_Y='hpicfDSnoopV6SCUnauthorizedServers'
_X='hpicfDSnoopV6SCForwards'
_W='hpicfDSnoopV6CSMACMismatches'
_V='hpicfDSnoopV6CSUntrustedDestPorts'
_U='hpicfDSnoopV6CSBadReleases'
_T='hpicfDSnoopV6CSForwards'
_S='hpicfDSnoopV6VlanEnable'
_R='hpicfDSnoopV6Enable'
_Q='disabled'
_P='enabled'
_O='InetAddress'
_N='hpicfDSnoopV6TrapsGroup'
_M='hpicfDSnoopV6TrapObjectsGroup'
_L='hpicfDSnoopV6ClearStatsOptionsGroup'
_K='hpicfDSnoopV6StaticBindingsGroup'
_J='hpicfDSnoopV6MaxBindingsGroup'
_I='hpicfDSnoopV6ServersGroup'
_H='deprecated'
_G='Integer32'
_F='Unsigned32'
_E='accessible-for-notify'
_D='read-write'
_C='read-only'
_B='current'
_A='HP-ICF-DHCPv6-SNOOP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
VidList,=mibBuilder.importSymbols('HP-ICF-TC','VidList')
hpicfSaviObjectsBindingEntry,hpicfSaviObjectsPortEntry=mibBuilder.importSymbols('HPICF-SAVI-MIB','hpicfSaviObjectsBindingEntry','hpicfSaviObjectsPortEntry')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_O,'InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_u)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpicfDSnoopV6=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102))
if mibBuilder.loadTexts:hpicfDSnoopV6.setRevisions(('2017-11-08 00:00','2015-01-28 00:00','2013-10-06 00:00','2013-04-30 00:00'))
_HpicfDSnoopV6Notifications_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6Notifications=_HpicfDSnoopV6Notifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,0))
_HpicfDsnoopV6SourceBindingOutOfResourcesObjects_ObjectIdentity=ObjectIdentity
hpicfDsnoopV6SourceBindingOutOfResourcesObjects=_HpicfDsnoopV6SourceBindingOutOfResourcesObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,0,2))
_HpicfDsnoopV6SourceBindingPort_Type=InterfaceIndex
_HpicfDsnoopV6SourceBindingPort_Object=MibScalar
hpicfDsnoopV6SourceBindingPort=_HpicfDsnoopV6SourceBindingPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,2,1),_HpicfDsnoopV6SourceBindingPort_Type())
hpicfDsnoopV6SourceBindingPort.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDsnoopV6SourceBindingPort.setStatus(_B)
_HpicfDsnoopV6SourceBindingMacAddress_Type=MacAddress
_HpicfDsnoopV6SourceBindingMacAddress_Object=MibScalar
hpicfDsnoopV6SourceBindingMacAddress=_HpicfDsnoopV6SourceBindingMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,2,2),_HpicfDsnoopV6SourceBindingMacAddress_Type())
hpicfDsnoopV6SourceBindingMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDsnoopV6SourceBindingMacAddress.setStatus(_B)
_HpicfDsnoopV6SourceBindingIpAddressType_Type=InetAddressType
_HpicfDsnoopV6SourceBindingIpAddressType_Object=MibScalar
hpicfDsnoopV6SourceBindingIpAddressType=_HpicfDsnoopV6SourceBindingIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,2,3),_HpicfDsnoopV6SourceBindingIpAddressType_Type())
hpicfDsnoopV6SourceBindingIpAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDsnoopV6SourceBindingIpAddressType.setStatus(_B)
_HpicfDsnoopV6SourceBindingIpAddress_Type=InetAddress
_HpicfDsnoopV6SourceBindingIpAddress_Object=MibScalar
hpicfDsnoopV6SourceBindingIpAddress=_HpicfDsnoopV6SourceBindingIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,2,4),_HpicfDsnoopV6SourceBindingIpAddress_Type())
hpicfDsnoopV6SourceBindingIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDsnoopV6SourceBindingIpAddress.setStatus(_B)
_HpicfDsnoopV6SourceBindingVlan_Type=VlanIndex
_HpicfDsnoopV6SourceBindingVlan_Object=MibScalar
hpicfDsnoopV6SourceBindingVlan=_HpicfDsnoopV6SourceBindingVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,2,5),_HpicfDsnoopV6SourceBindingVlan_Type())
hpicfDsnoopV6SourceBindingVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDsnoopV6SourceBindingVlan.setStatus(_B)
_HpicfDSnoopV6SourceBindingNotifyObjects_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6SourceBindingNotifyObjects=_HpicfDSnoopV6SourceBindingNotifyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,0,4))
_HpicfDSnoopV6SourceBindingNotifyCount_Type=Counter32
_HpicfDSnoopV6SourceBindingNotifyCount_Object=MibScalar
hpicfDSnoopV6SourceBindingNotifyCount=_HpicfDSnoopV6SourceBindingNotifyCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,4,1),_HpicfDSnoopV6SourceBindingNotifyCount_Type())
hpicfDSnoopV6SourceBindingNotifyCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDSnoopV6SourceBindingNotifyCount.setStatus(_B)
_HpicfDSnoopV6SourceBindingErrantSrcMAC_Type=MacAddress
_HpicfDSnoopV6SourceBindingErrantSrcMAC_Object=MibScalar
hpicfDSnoopV6SourceBindingErrantSrcMAC=_HpicfDSnoopV6SourceBindingErrantSrcMAC_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,4,2),_HpicfDSnoopV6SourceBindingErrantSrcMAC_Type())
hpicfDSnoopV6SourceBindingErrantSrcMAC.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDSnoopV6SourceBindingErrantSrcMAC.setStatus(_B)
_HpicfDSnoopV6SourceBindingErrantSrcIPType_Type=InetAddressType
_HpicfDSnoopV6SourceBindingErrantSrcIPType_Object=MibScalar
hpicfDSnoopV6SourceBindingErrantSrcIPType=_HpicfDSnoopV6SourceBindingErrantSrcIPType_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,4,3),_HpicfDSnoopV6SourceBindingErrantSrcIPType_Type())
hpicfDSnoopV6SourceBindingErrantSrcIPType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDSnoopV6SourceBindingErrantSrcIPType.setStatus(_B)
_HpicfDSnoopV6SourceBindingErrantSrcIP_Type=InetAddress
_HpicfDSnoopV6SourceBindingErrantSrcIP_Object=MibScalar
hpicfDSnoopV6SourceBindingErrantSrcIP=_HpicfDSnoopV6SourceBindingErrantSrcIP_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,0,4,4),_HpicfDSnoopV6SourceBindingErrantSrcIP_Type())
hpicfDSnoopV6SourceBindingErrantSrcIP.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfDSnoopV6SourceBindingErrantSrcIP.setStatus(_B)
_HpicfDSnoopV6Objects_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6Objects=_HpicfDSnoopV6Objects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,1))
_HpicfDSnoopV6Config_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6Config=_HpicfDSnoopV6Config_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1))
_HpicfDSnoopV6GlobalCfg_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6GlobalCfg=_HpicfDSnoopV6GlobalCfg_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1))
_HpicfDSnoopV6Enable_Type=TruthValue
_HpicfDSnoopV6Enable_Object=MibScalar
hpicfDSnoopV6Enable=_HpicfDSnoopV6Enable_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,1),_HpicfDSnoopV6Enable_Type())
hpicfDSnoopV6Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6Enable.setStatus(_B)
_HpicfDSnoopV6VlanEnable_Type=VidList
_HpicfDSnoopV6VlanEnable_Object=MibScalar
hpicfDSnoopV6VlanEnable=_HpicfDSnoopV6VlanEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,2),_HpicfDSnoopV6VlanEnable_Type())
hpicfDSnoopV6VlanEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6VlanEnable.setStatus(_B)
_HpicfDSnoopV6DatabaseFile_Type=SnmpAdminString
_HpicfDSnoopV6DatabaseFile_Object=MibScalar
hpicfDSnoopV6DatabaseFile=_HpicfDSnoopV6DatabaseFile_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,3),_HpicfDSnoopV6DatabaseFile_Type())
hpicfDSnoopV6DatabaseFile.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseFile.setStatus(_B)
class _HpicfDSnoopV6DatabaseWriteDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,86400))
_HpicfDSnoopV6DatabaseWriteDelay_Type.__name__=_F
_HpicfDSnoopV6DatabaseWriteDelay_Object=MibScalar
hpicfDSnoopV6DatabaseWriteDelay=_HpicfDSnoopV6DatabaseWriteDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,4),_HpicfDSnoopV6DatabaseWriteDelay_Type())
hpicfDSnoopV6DatabaseWriteDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseWriteDelay.setStatus(_B)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseWriteDelay.setUnits(_v)
class _HpicfDSnoopV6DatabaseWriteTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_HpicfDSnoopV6DatabaseWriteTimeout_Type.__name__=_F
_HpicfDSnoopV6DatabaseWriteTimeout_Object=MibScalar
hpicfDSnoopV6DatabaseWriteTimeout=_HpicfDSnoopV6DatabaseWriteTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,5),_HpicfDSnoopV6DatabaseWriteTimeout_Type())
hpicfDSnoopV6DatabaseWriteTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseWriteTimeout.setStatus(_B)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseWriteTimeout.setUnits(_v)
class _HpicfDSnoopV6OutOfResourcesTrapCtrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpicfDSnoopV6OutOfResourcesTrapCtrl_Type.__name__=_G
_HpicfDSnoopV6OutOfResourcesTrapCtrl_Object=MibScalar
hpicfDSnoopV6OutOfResourcesTrapCtrl=_HpicfDSnoopV6OutOfResourcesTrapCtrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,6),_HpicfDSnoopV6OutOfResourcesTrapCtrl_Type())
hpicfDSnoopV6OutOfResourcesTrapCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6OutOfResourcesTrapCtrl.setStatus(_B)
class _HpicfDSnoopV6ErrantReplyTrapCtrl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpicfDSnoopV6ErrantReplyTrapCtrl_Type.__name__=_G
_HpicfDSnoopV6ErrantReplyTrapCtrl_Object=MibScalar
hpicfDSnoopV6ErrantReplyTrapCtrl=_HpicfDSnoopV6ErrantReplyTrapCtrl_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,7),_HpicfDSnoopV6ErrantReplyTrapCtrl_Type())
hpicfDSnoopV6ErrantReplyTrapCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6ErrantReplyTrapCtrl.setStatus(_B)
class _HpicfDSnoopV6DatabaseFTPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpicfDSnoopV6DatabaseFTPort_Type.__name__=_F
_HpicfDSnoopV6DatabaseFTPort_Object=MibScalar
hpicfDSnoopV6DatabaseFTPort=_HpicfDSnoopV6DatabaseFTPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,8),_HpicfDSnoopV6DatabaseFTPort_Type())
hpicfDSnoopV6DatabaseFTPort.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseFTPort.setStatus(_B)
_HpicfDSnoopV6DatabaseSFTPUsername_Type=SnmpAdminString
_HpicfDSnoopV6DatabaseSFTPUsername_Object=MibScalar
hpicfDSnoopV6DatabaseSFTPUsername=_HpicfDSnoopV6DatabaseSFTPUsername_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,9),_HpicfDSnoopV6DatabaseSFTPUsername_Type())
hpicfDSnoopV6DatabaseSFTPUsername.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseSFTPUsername.setStatus(_B)
_HpicfDSnoopV6DatabaseSFTPPassword_Type=SnmpAdminString
_HpicfDSnoopV6DatabaseSFTPPassword_Object=MibScalar
hpicfDSnoopV6DatabaseSFTPPassword=_HpicfDSnoopV6DatabaseSFTPPassword_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,10),_HpicfDSnoopV6DatabaseSFTPPassword_Type())
hpicfDSnoopV6DatabaseSFTPPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseSFTPPassword.setStatus(_B)
class _HpicfDSnoopV6DatabaseValidateSFTPServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_HpicfDSnoopV6DatabaseValidateSFTPServer_Type.__name__=_G
_HpicfDSnoopV6DatabaseValidateSFTPServer_Object=MibScalar
hpicfDSnoopV6DatabaseValidateSFTPServer=_HpicfDSnoopV6DatabaseValidateSFTPServer_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,11),_HpicfDSnoopV6DatabaseValidateSFTPServer_Type())
hpicfDSnoopV6DatabaseValidateSFTPServer.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6DatabaseValidateSFTPServer.setStatus(_B)
class _HpicfDSnoopV6RateLimit_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,500))
_HpicfDSnoopV6RateLimit_Type.__name__=_F
_HpicfDSnoopV6RateLimit_Object=MibScalar
hpicfDSnoopV6RateLimit=_HpicfDSnoopV6RateLimit_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,1,12),_HpicfDSnoopV6RateLimit_Type())
hpicfDSnoopV6RateLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6RateLimit.setStatus(_B)
_HpicfDSnoopV6AuthorizedServerTable_Object=MibTable
hpicfDSnoopV6AuthorizedServerTable=_HpicfDSnoopV6AuthorizedServerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,2))
if mibBuilder.loadTexts:hpicfDSnoopV6AuthorizedServerTable.setStatus(_B)
_HpicfDSnoopV6AuthorizedServerEntry_Object=MibTableRow
hpicfDSnoopV6AuthorizedServerEntry=_HpicfDSnoopV6AuthorizedServerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,2,1))
hpicfDSnoopV6AuthorizedServerEntry.setIndexNames((0,_A,_w),(0,_A,_x))
if mibBuilder.loadTexts:hpicfDSnoopV6AuthorizedServerEntry.setStatus(_B)
_HpicfDSnoopV6AuthorizedServerAddrType_Type=InetAddressType
_HpicfDSnoopV6AuthorizedServerAddrType_Object=MibTableColumn
hpicfDSnoopV6AuthorizedServerAddrType=_HpicfDSnoopV6AuthorizedServerAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,2,1,1),_HpicfDSnoopV6AuthorizedServerAddrType_Type())
hpicfDSnoopV6AuthorizedServerAddrType.setMaxAccess(_y)
if mibBuilder.loadTexts:hpicfDSnoopV6AuthorizedServerAddrType.setStatus(_B)
class _HpicfDSnoopV6AuthorizedServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_HpicfDSnoopV6AuthorizedServerAddress_Type.__name__=_O
_HpicfDSnoopV6AuthorizedServerAddress_Object=MibTableColumn
hpicfDSnoopV6AuthorizedServerAddress=_HpicfDSnoopV6AuthorizedServerAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,2,1,2),_HpicfDSnoopV6AuthorizedServerAddress_Type())
hpicfDSnoopV6AuthorizedServerAddress.setMaxAccess(_y)
if mibBuilder.loadTexts:hpicfDSnoopV6AuthorizedServerAddress.setStatus(_B)
_HpicfDSnoopV6AuthorizedServerStatus_Type=RowStatus
_HpicfDSnoopV6AuthorizedServerStatus_Object=MibTableColumn
hpicfDSnoopV6AuthorizedServerStatus=_HpicfDSnoopV6AuthorizedServerStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,2,1,3),_HpicfDSnoopV6AuthorizedServerStatus_Type())
hpicfDSnoopV6AuthorizedServerStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpicfDSnoopV6AuthorizedServerStatus.setStatus(_B)
_HpicfDSnoopV6PortMaxBindingTable_Object=MibTable
hpicfDSnoopV6PortMaxBindingTable=_HpicfDSnoopV6PortMaxBindingTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,3))
if mibBuilder.loadTexts:hpicfDSnoopV6PortMaxBindingTable.setStatus(_B)
_HpicfDSnoopV6PortMaxBindingEntry_Object=MibTableRow
hpicfDSnoopV6PortMaxBindingEntry=_HpicfDSnoopV6PortMaxBindingEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,3,1))
if mibBuilder.loadTexts:hpicfDSnoopV6PortMaxBindingEntry.setStatus(_B)
class _HpicfDSnoopV6PortStaticBinding_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_HpicfDSnoopV6PortStaticBinding_Type.__name__=_F
_HpicfDSnoopV6PortStaticBinding_Object=MibTableColumn
hpicfDSnoopV6PortStaticBinding=_HpicfDSnoopV6PortStaticBinding_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,3,1,2),_HpicfDSnoopV6PortStaticBinding_Type())
hpicfDSnoopV6PortStaticBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6PortStaticBinding.setStatus(_B)
class _HpicfDSnoopV6PortDynamicBinding_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_HpicfDSnoopV6PortDynamicBinding_Type.__name__=_F
_HpicfDSnoopV6PortDynamicBinding_Object=MibTableColumn
hpicfDSnoopV6PortDynamicBinding=_HpicfDSnoopV6PortDynamicBinding_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,3,1,3),_HpicfDSnoopV6PortDynamicBinding_Type())
hpicfDSnoopV6PortDynamicBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6PortDynamicBinding.setStatus(_B)
_HpicfDSnoopV6StaticBindingTable_Object=MibTable
hpicfDSnoopV6StaticBindingTable=_HpicfDSnoopV6StaticBindingTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,4))
if mibBuilder.loadTexts:hpicfDSnoopV6StaticBindingTable.setStatus(_B)
_HpicfDSnoopV6StaticBindingEntry_Object=MibTableRow
hpicfDSnoopV6StaticBindingEntry=_HpicfDSnoopV6StaticBindingEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,4,1))
if mibBuilder.loadTexts:hpicfDSnoopV6StaticBindingEntry.setStatus(_B)
class _HpicfDSnoopV6BindingVlanId_Type(VlanIndex):subtypeSpec=VlanIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpicfDSnoopV6BindingVlanId_Type.__name__=_u
_HpicfDSnoopV6BindingVlanId_Object=MibTableColumn
hpicfDSnoopV6BindingVlanId=_HpicfDSnoopV6BindingVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,4,1,1),_HpicfDSnoopV6BindingVlanId_Type())
hpicfDSnoopV6BindingVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6BindingVlanId.setStatus(_B)
class _HpicfDSnoopV6BindingLLAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_HpicfDSnoopV6BindingLLAddress_Type.__name__=_O
_HpicfDSnoopV6BindingLLAddress_Object=MibTableColumn
hpicfDSnoopV6BindingLLAddress=_HpicfDSnoopV6BindingLLAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,4,1,2),_HpicfDSnoopV6BindingLLAddress_Type())
hpicfDSnoopV6BindingLLAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6BindingLLAddress.setStatus(_B)
_HpicfDSnoopV6BindingSecVlan_Type=Unsigned32
_HpicfDSnoopV6BindingSecVlan_Object=MibTableColumn
hpicfDSnoopV6BindingSecVlan=_HpicfDSnoopV6BindingSecVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,1,4,1,3),_HpicfDSnoopV6BindingSecVlan_Type())
hpicfDSnoopV6BindingSecVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6BindingSecVlan.setStatus(_B)
_HpicfDSnoopV6GlobalStats_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6GlobalStats=_HpicfDSnoopV6GlobalStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2))
_HpicfDSnoopV6CSForwards_Type=Counter32
_HpicfDSnoopV6CSForwards_Object=MibScalar
hpicfDSnoopV6CSForwards=_HpicfDSnoopV6CSForwards_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,1),_HpicfDSnoopV6CSForwards_Type())
hpicfDSnoopV6CSForwards.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6CSForwards.setStatus(_B)
_HpicfDSnoopV6CSMACMismatches_Type=Counter32
_HpicfDSnoopV6CSMACMismatches_Object=MibScalar
hpicfDSnoopV6CSMACMismatches=_HpicfDSnoopV6CSMACMismatches_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,2),_HpicfDSnoopV6CSMACMismatches_Type())
hpicfDSnoopV6CSMACMismatches.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6CSMACMismatches.setStatus(_B)
_HpicfDSnoopV6CSBadReleases_Type=Counter32
_HpicfDSnoopV6CSBadReleases_Object=MibScalar
hpicfDSnoopV6CSBadReleases=_HpicfDSnoopV6CSBadReleases_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,3),_HpicfDSnoopV6CSBadReleases_Type())
hpicfDSnoopV6CSBadReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6CSBadReleases.setStatus(_B)
_HpicfDSnoopV6CSUntrustedDestPorts_Type=Counter32
_HpicfDSnoopV6CSUntrustedDestPorts_Object=MibScalar
hpicfDSnoopV6CSUntrustedDestPorts=_HpicfDSnoopV6CSUntrustedDestPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,4),_HpicfDSnoopV6CSUntrustedDestPorts_Type())
hpicfDSnoopV6CSUntrustedDestPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6CSUntrustedDestPorts.setStatus(_B)
_HpicfDSnoopV6SCForwards_Type=Counter32
_HpicfDSnoopV6SCForwards_Object=MibScalar
hpicfDSnoopV6SCForwards=_HpicfDSnoopV6SCForwards_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,5),_HpicfDSnoopV6SCForwards_Type())
hpicfDSnoopV6SCForwards.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6SCForwards.setStatus(_B)
_HpicfDSnoopV6SCUntrustedPorts_Type=Counter32
_HpicfDSnoopV6SCUntrustedPorts_Object=MibScalar
hpicfDSnoopV6SCUntrustedPorts=_HpicfDSnoopV6SCUntrustedPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,6),_HpicfDSnoopV6SCUntrustedPorts_Type())
hpicfDSnoopV6SCUntrustedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6SCUntrustedPorts.setStatus(_B)
_HpicfDSnoopV6SCRelayReplyUntrustedPorts_Type=Counter32
_HpicfDSnoopV6SCRelayReplyUntrustedPorts_Object=MibScalar
hpicfDSnoopV6SCRelayReplyUntrustedPorts=_HpicfDSnoopV6SCRelayReplyUntrustedPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,7),_HpicfDSnoopV6SCRelayReplyUntrustedPorts_Type())
hpicfDSnoopV6SCRelayReplyUntrustedPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6SCRelayReplyUntrustedPorts.setStatus(_B)
_HpicfDSnoopV6SCUnauthorizedServers_Type=Counter32
_HpicfDSnoopV6SCUnauthorizedServers_Object=MibScalar
hpicfDSnoopV6SCUnauthorizedServers=_HpicfDSnoopV6SCUnauthorizedServers_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,8),_HpicfDSnoopV6SCUnauthorizedServers_Type())
hpicfDSnoopV6SCUnauthorizedServers.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6SCUnauthorizedServers.setStatus(_B)
_HpicfDSnoopV6DBFileWriteAttempts_Type=Counter32
_HpicfDSnoopV6DBFileWriteAttempts_Object=MibScalar
hpicfDSnoopV6DBFileWriteAttempts=_HpicfDSnoopV6DBFileWriteAttempts_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,9),_HpicfDSnoopV6DBFileWriteAttempts_Type())
hpicfDSnoopV6DBFileWriteAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6DBFileWriteAttempts.setStatus(_B)
_HpicfDSnoopV6DBFileWriteFailures_Type=Counter32
_HpicfDSnoopV6DBFileWriteFailures_Object=MibScalar
hpicfDSnoopV6DBFileWriteFailures=_HpicfDSnoopV6DBFileWriteFailures_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,10),_HpicfDSnoopV6DBFileWriteFailures_Type())
hpicfDSnoopV6DBFileWriteFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6DBFileWriteFailures.setStatus(_B)
class _HpicfDSnoopV6DBFileReadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3),('failed',4)))
_HpicfDSnoopV6DBFileReadStatus_Type.__name__=_G
_HpicfDSnoopV6DBFileReadStatus_Object=MibScalar
hpicfDSnoopV6DBFileReadStatus=_HpicfDSnoopV6DBFileReadStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,11),_HpicfDSnoopV6DBFileReadStatus_Type())
hpicfDSnoopV6DBFileReadStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6DBFileReadStatus.setStatus(_B)
class _HpicfDSnoopV6DBFileWriteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_z,1),('delaying',2),(_A0,3),(_A1,4),('failed',5)))
_HpicfDSnoopV6DBFileWriteStatus_Type.__name__=_G
_HpicfDSnoopV6DBFileWriteStatus_Object=MibScalar
hpicfDSnoopV6DBFileWriteStatus=_HpicfDSnoopV6DBFileWriteStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,12),_HpicfDSnoopV6DBFileWriteStatus_Type())
hpicfDSnoopV6DBFileWriteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6DBFileWriteStatus.setStatus(_B)
_HpicfDSnoopV6DBFileLastWriteTime_Type=DateAndTime
_HpicfDSnoopV6DBFileLastWriteTime_Object=MibScalar
hpicfDSnoopV6DBFileLastWriteTime=_HpicfDSnoopV6DBFileLastWriteTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,13),_HpicfDSnoopV6DBFileLastWriteTime_Type())
hpicfDSnoopV6DBFileLastWriteTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6DBFileLastWriteTime.setStatus(_B)
_HpicfDSnoopV6MaxbindPktsDropped_Type=Counter32
_HpicfDSnoopV6MaxbindPktsDropped_Object=MibScalar
hpicfDSnoopV6MaxbindPktsDropped=_HpicfDSnoopV6MaxbindPktsDropped_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,2,14),_HpicfDSnoopV6MaxbindPktsDropped_Type())
hpicfDSnoopV6MaxbindPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDSnoopV6MaxbindPktsDropped.setStatus(_B)
_HpicfDSnoopV6ClearStatsOptions_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6ClearStatsOptions=_HpicfDSnoopV6ClearStatsOptions_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,1,3))
_HpicfDSnoopV6ClearStats_Type=TruthValue
_HpicfDSnoopV6ClearStats_Object=MibScalar
hpicfDSnoopV6ClearStats=_HpicfDSnoopV6ClearStats_Object((1,3,6,1,4,1,11,2,14,11,5,1,102,1,3,1),_HpicfDSnoopV6ClearStats_Type())
hpicfDSnoopV6ClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDSnoopV6ClearStats.setStatus(_B)
_HpicfDSnoopV6Conformance_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6Conformance=_HpicfDSnoopV6Conformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,2))
_HpicfDSnoopV6Groups_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6Groups=_HpicfDSnoopV6Groups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1))
_HpicfDSnoopV6Compliances_ObjectIdentity=ObjectIdentity
hpicfDSnoopV6Compliances=_HpicfDSnoopV6Compliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,102,2,3))
hpicfSaviObjectsPortEntry.registerAugmentions((_A,_A2))
hpicfDSnoopV6PortMaxBindingEntry.setIndexNames(*hpicfSaviObjectsPortEntry.getIndexNames())
hpicfSaviObjectsBindingEntry.registerAugmentions((_A,_A3))
hpicfDSnoopV6StaticBindingEntry.setIndexNames(*hpicfSaviObjectsBindingEntry.getIndexNames())
hpicfDSnoopV6BaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,1))
hpicfDSnoopV6BaseGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpicfDSnoopV6BaseGroup.setStatus(_H)
hpicfDSnoopV6ServersGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,2))
hpicfDSnoopV6ServersGroup.setObjects((_A,_A4))
if mibBuilder.loadTexts:hpicfDSnoopV6ServersGroup.setStatus(_B)
hpicfDSnoopV6DbaseFileGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,3))
hpicfDSnoopV6DbaseFileGroup.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:hpicfDSnoopV6DbaseFileGroup.setStatus(_H)
hpicfDSnoopV6MaxBindingsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,4))
hpicfDSnoopV6MaxBindingsGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:hpicfDSnoopV6MaxBindingsGroup.setStatus(_B)
hpicfDSnoopV6StaticBindingsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,5))
hpicfDSnoopV6StaticBindingsGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:hpicfDSnoopV6StaticBindingsGroup.setStatus(_B)
hpicfDSnoopV6ClearStatsOptionsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,6))
hpicfDSnoopV6ClearStatsOptionsGroup.setObjects((_A,_AB))
if mibBuilder.loadTexts:hpicfDSnoopV6ClearStatsOptionsGroup.setStatus(_B)
hpicfDSnoopV6TrapObjectsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,7))
hpicfDSnoopV6TrapObjectsGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:hpicfDSnoopV6TrapObjectsGroup.setStatus(_B)
hpicfDSnoopV6DbaseFileGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,9))
hpicfDSnoopV6DbaseFileGroup1.setObjects(*((_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:hpicfDSnoopV6DbaseFileGroup1.setStatus(_B)
hpicfDSnoopV6BaseGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,10))
hpicfDSnoopV6BaseGroup1.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_AI)))
if mibBuilder.loadTexts:hpicfDSnoopV6BaseGroup1.setStatus(_B)
hpicfDSnoopV6SourceBindingOutOfResources=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,102,0,1))
hpicfDSnoopV6SourceBindingOutOfResources.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:hpicfDSnoopV6SourceBindingOutOfResources.setStatus(_B)
hpicfDSnoopV6SourceBindingErrantReply=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,102,0,3))
hpicfDSnoopV6SourceBindingErrantReply.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:hpicfDSnoopV6SourceBindingErrantReply.setStatus(_B)
hpicfDSnoopV6TrapsGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,102,2,1,8))
hpicfDSnoopV6TrapsGroup.setObjects(*((_A,_AJ),(_A,_AK)))
if mibBuilder.loadTexts:hpicfDSnoopV6TrapsGroup.setStatus(_B)
hpicfDSnoopV6Compliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,102,2,3,1))
hpicfDSnoopV6Compliance2.setObjects(*((_A,_s),(_A,_I),(_A,_AL),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfDSnoopV6Compliance2.setStatus(_H)
hpicfDSnoopV6Compliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,102,2,3,2))
hpicfDSnoopV6Compliance.setObjects(*((_A,_s),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_t)))
if mibBuilder.loadTexts:hpicfDSnoopV6Compliance.setStatus(_H)
hpicfDSnoopV6Compliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,102,2,3,3))
hpicfDSnoopV6Compliance3.setObjects(*((_A,_AM),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_t)))
if mibBuilder.loadTexts:hpicfDSnoopV6Compliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfDSnoopV6':hpicfDSnoopV6,'hpicfDSnoopV6Notifications':hpicfDSnoopV6Notifications,_AJ:hpicfDSnoopV6SourceBindingOutOfResources,'hpicfDsnoopV6SourceBindingOutOfResourcesObjects':hpicfDsnoopV6SourceBindingOutOfResourcesObjects,_n:hpicfDsnoopV6SourceBindingPort,_o:hpicfDsnoopV6SourceBindingMacAddress,_p:hpicfDsnoopV6SourceBindingIpAddressType,_q:hpicfDsnoopV6SourceBindingIpAddress,_r:hpicfDsnoopV6SourceBindingVlan,_AK:hpicfDSnoopV6SourceBindingErrantReply,'hpicfDSnoopV6SourceBindingNotifyObjects':hpicfDSnoopV6SourceBindingNotifyObjects,_j:hpicfDSnoopV6SourceBindingNotifyCount,_k:hpicfDSnoopV6SourceBindingErrantSrcMAC,_l:hpicfDSnoopV6SourceBindingErrantSrcIPType,_m:hpicfDSnoopV6SourceBindingErrantSrcIP,'hpicfDSnoopV6Objects':hpicfDSnoopV6Objects,'hpicfDSnoopV6Config':hpicfDSnoopV6Config,'hpicfDSnoopV6GlobalCfg':hpicfDSnoopV6GlobalCfg,_R:hpicfDSnoopV6Enable,_S:hpicfDSnoopV6VlanEnable,_b:hpicfDSnoopV6DatabaseFile,_c:hpicfDSnoopV6DatabaseWriteDelay,_d:hpicfDSnoopV6DatabaseWriteTimeout,_AC:hpicfDSnoopV6OutOfResourcesTrapCtrl,_AD:hpicfDSnoopV6ErrantReplyTrapCtrl,_AE:hpicfDSnoopV6DatabaseFTPort,_AF:hpicfDSnoopV6DatabaseSFTPUsername,_AG:hpicfDSnoopV6DatabaseSFTPPassword,_AH:hpicfDSnoopV6DatabaseValidateSFTPServer,_AI:hpicfDSnoopV6RateLimit,'hpicfDSnoopV6AuthorizedServerTable':hpicfDSnoopV6AuthorizedServerTable,'hpicfDSnoopV6AuthorizedServerEntry':hpicfDSnoopV6AuthorizedServerEntry,_w:hpicfDSnoopV6AuthorizedServerAddrType,_x:hpicfDSnoopV6AuthorizedServerAddress,_A4:hpicfDSnoopV6AuthorizedServerStatus,'hpicfDSnoopV6PortMaxBindingTable':hpicfDSnoopV6PortMaxBindingTable,_A2:hpicfDSnoopV6PortMaxBindingEntry,_A6:hpicfDSnoopV6PortStaticBinding,_A7:hpicfDSnoopV6PortDynamicBinding,'hpicfDSnoopV6StaticBindingTable':hpicfDSnoopV6StaticBindingTable,_A3:hpicfDSnoopV6StaticBindingEntry,_A8:hpicfDSnoopV6BindingVlanId,_A9:hpicfDSnoopV6BindingLLAddress,_AA:hpicfDSnoopV6BindingSecVlan,'hpicfDSnoopV6GlobalStats':hpicfDSnoopV6GlobalStats,_T:hpicfDSnoopV6CSForwards,_W:hpicfDSnoopV6CSMACMismatches,_U:hpicfDSnoopV6CSBadReleases,_V:hpicfDSnoopV6CSUntrustedDestPorts,_X:hpicfDSnoopV6SCForwards,_Z:hpicfDSnoopV6SCUntrustedPorts,_a:hpicfDSnoopV6SCRelayReplyUntrustedPorts,_Y:hpicfDSnoopV6SCUnauthorizedServers,_e:hpicfDSnoopV6DBFileWriteAttempts,_f:hpicfDSnoopV6DBFileWriteFailures,_g:hpicfDSnoopV6DBFileReadStatus,_h:hpicfDSnoopV6DBFileWriteStatus,_i:hpicfDSnoopV6DBFileLastWriteTime,_A5:hpicfDSnoopV6MaxbindPktsDropped,'hpicfDSnoopV6ClearStatsOptions':hpicfDSnoopV6ClearStatsOptions,_AB:hpicfDSnoopV6ClearStats,'hpicfDSnoopV6Conformance':hpicfDSnoopV6Conformance,'hpicfDSnoopV6Groups':hpicfDSnoopV6Groups,_s:hpicfDSnoopV6BaseGroup,_I:hpicfDSnoopV6ServersGroup,_AL:hpicfDSnoopV6DbaseFileGroup,_J:hpicfDSnoopV6MaxBindingsGroup,_K:hpicfDSnoopV6StaticBindingsGroup,_L:hpicfDSnoopV6ClearStatsOptionsGroup,_M:hpicfDSnoopV6TrapObjectsGroup,_N:hpicfDSnoopV6TrapsGroup,_t:hpicfDSnoopV6DbaseFileGroup1,_AM:hpicfDSnoopV6BaseGroup1,'hpicfDSnoopV6Compliances':hpicfDSnoopV6Compliances,'hpicfDSnoopV6Compliance2':hpicfDSnoopV6Compliance2,'hpicfDSnoopV6Compliance':hpicfDSnoopV6Compliance,'hpicfDSnoopV6Compliance3':hpicfDSnoopV6Compliance3})