_An='hpicfDhcpSnoopBaseGroup1'
_Am='hpicfDhcpSnoopClearBindingsOptionsGroup'
_Al='hpicfDhcpSnoopAllowOverwriteBindingGroup'
_Ak='hpicfDhcpSnoopPktsGroup1'
_Aj='hpicfDhcpSnoopClearStatsOptionsGroup'
_Ai='hpicfDhcpSnoopPktsGroup'
_Ah='hpicfDhcpSnoopNotificationGroup'
_Ag='hpicfDhcpSnoopNotifyObjsGroup'
_Af='hpicfDhcpSnoopErrantReply'
_Ae='hpicfDhcpSnoopRateLimit'
_Ad='hpicfDhcpSnoopClearBindingsVlan'
_Ac='hpicfDhcpSnoopClearBindingsPort'
_Ab='hpicfDhcpSnoopClearBindingsIpAddr'
_Aa='hpicfDhcpSnoopClearBindingsIpType'
_AZ='hpicfDhcpSnoopClearBindings'
_AY='hpicfDhcpSnoopAllowOverwriteBinding'
_AX='hpicfDhcpSnoopDatabaseValidateSFTPServer'
_AW='hpicfDhcpSnoopDatabaseSFTPPassword'
_AV='hpicfDhcpSnoopDatabaseSFTPUsername'
_AU='hpicfDhcpSnoopDatabaseFTPort'
_AT='hpicfDhcpSnoopMaxbindPktsDropped'
_AS='hpicfDhcpSnoopPortDynamicBinding'
_AR='hpicfDhcpSnoopPortStaticBinding'
_AQ='hpicfDhcpSnoopPortMaxbind'
_AP='hpicfDhcpSnoopClearStats'
_AO='hpicfDhcpSnoopErrantReplyEnable'
_AN='hpicfIpStaticBindingsStatus'
_AM='hpicfIpStaticBindingsInterface'
_AL='hpicfIpStaticBindingsMacAddress'
_AK='hpicfDhcpSnoopBindingsSecVlan'
_AJ='hpicfDhcpSnoopBindingsLeaseTime'
_AI='hpicfDhcpSnoopBindingsInterface'
_AH='hpicfDhcpSnoopSCUntrustedServers'
_AG='hpicfDhcpSnoopServerStatus'
_AF='hpicfDhcpSnoopSCOpt82Failures'
_AE='hpicfDhcpSnoopCSUntrustedOpt82s'
_AD='hpicfDhcpSnoopOpt82RemoteId'
_AC='hpicfDhcpSnoopOpt82Policy'
_AB='hpicfDhcpSnoopOpt82Insert'
_AA='hpicfDhcpSnoopBindingsAddress'
_A9='hpicfDhcpSnoopBindingsAddrType'
_A8='hpicfDhcpSnoopBindingsMacAddress'
_A7='hpicfDhcpSnoopBindingsVlan'
_A6='succeeded'
_A5='inProgress'
_A4='notConfigured'
_A3='hpicfIpStaticBindingsAddress'
_A2='hpicfIpStaticBindingsAddrType'
_A1='hpicfIpStaticBindingsVlan'
_A0='hpicfDhcpSnoopServerAddress'
_z='hpicfDhcpSnoopServerAddrType'
_y='disabled'
_x='enabled'
_w='TruthValue'
_v='ifIndex'
_u='IF-MIB'
_t='OctetString'
_s='hpicfDhcpSnoopDbaseFileGroup'
_r='hpicfDhcpSnoopPktsDropped'
_q='hpicfDhcpSnoopPktsReceived'
_p='hpicfDhcpSnoopPktsSent'
_o='hpicfDhcpSnoopErrantSrcIP'
_n='hpicfDhcpSnoopErrantSrcIPType'
_m='hpicfDhcpSnoopErrantSrcMAC'
_l='hpicfDhcpSnoopNotifyCount'
_k='hpicfDhcpSnoopBindingsType'
_j='hpicfDhcpSnoopDBFileLastWriteTime'
_i='hpicfDhcpSnoopDBFileWriteStatus'
_h='hpicfDhcpSnoopDBFileReadStatus'
_g='hpicfDhcpSnoopDBFileWriteFailures'
_f='hpicfDhcpSnoopDBFileWriteAttempts'
_e='hpicfDhcpSnoopDatabaseWriteTimeout'
_d='hpicfDhcpSnoopDatabaseWriteDelay'
_c='hpicfDhcpSnoopDatabaseFile'
_b='hpicfDhcpSnoopSCUntrustedPorts'
_a='hpicfDhcpSnoopSCForwards'
_Z='hpicfDhcpSnoopCSUntrustedDestPorts'
_Y='hpicfDhcpSnoopCSBadReleases'
_X='hpicfDhcpSnoopCSMACMismatches'
_W='hpicfDhcpSnoopCSForwards'
_V='hpicfDhcpSnoopPortTrust'
_U='hpicfDhcpSnoopVerifyMac'
_T='hpicfDhcpSnoopVlanEnable'
_S='hpicfDhcpSnoopEnable'
_R='VlanIndex'
_Q='hpicfDhcpSnoopMaxbindingGroup'
_P='hpicfDhcpSnoopDbaseFileGroup1'
_O='accessible-for-notify'
_N='read-create'
_M='hpicfDhcpSnoopStaticBindingsGroup'
_L='hpicfDhcpSnoopBaseGroup'
_K='deprecated'
_J='hpicfDhcpSnoopBindingsGroup'
_I='hpicfDhcpSnoopServersGroup'
_H='hpicfDhcpSnoopOpt82Group'
_G='Unsigned32'
_F='not-accessible'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='current'
_A='HP-ICF-DHCP-SNOOP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_t,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_u,'InterfaceIndex','InterfaceIndexOrZero',_v)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_R)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_w)
hpicfIpDhcpSnoop=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34))
if mibBuilder.loadTexts:hpicfIpDhcpSnoop.setRevisions(('2019-01-17 00:00','2018-12-07 00:00','2016-06-01 00:00','2016-01-29 00:00','2015-06-12 00:00','2013-06-12 00:00','2013-05-02 00:00','2013-02-10 00:00','2007-08-24 00:00','2006-07-06 00:38','2006-03-18 00:38'))
_HpicfDhcpSnoopNotifications_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopNotifications=_HpicfDhcpSnoopNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,0))
_HpicfIpDhcpSnoopObjects_ObjectIdentity=ObjectIdentity
hpicfIpDhcpSnoopObjects=_HpicfIpDhcpSnoopObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1))
_HpicfIpDhcpSnoopConfig_ObjectIdentity=ObjectIdentity
hpicfIpDhcpSnoopConfig=_HpicfIpDhcpSnoopConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1))
_HpicfDhcpSnoopGlobalCfg_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopGlobalCfg=_HpicfDhcpSnoopGlobalCfg_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1))
_HpicfDhcpSnoopEnable_Type=TruthValue
_HpicfDhcpSnoopEnable_Object=MibScalar
hpicfDhcpSnoopEnable=_HpicfDhcpSnoopEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,1),_HpicfDhcpSnoopEnable_Type())
hpicfDhcpSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopEnable.setStatus(_B)
class _HpicfDhcpSnoopVlanEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_HpicfDhcpSnoopVlanEnable_Type.__name__=_t
_HpicfDhcpSnoopVlanEnable_Object=MibScalar
hpicfDhcpSnoopVlanEnable=_HpicfDhcpSnoopVlanEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,2),_HpicfDhcpSnoopVlanEnable_Type())
hpicfDhcpSnoopVlanEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopVlanEnable.setStatus(_B)
_HpicfDhcpSnoopVerifyMac_Type=TruthValue
_HpicfDhcpSnoopVerifyMac_Object=MibScalar
hpicfDhcpSnoopVerifyMac=_HpicfDhcpSnoopVerifyMac_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,3),_HpicfDhcpSnoopVerifyMac_Type())
hpicfDhcpSnoopVerifyMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopVerifyMac.setStatus(_B)
_HpicfDhcpSnoopDatabaseFile_Type=SnmpAdminString
_HpicfDhcpSnoopDatabaseFile_Object=MibScalar
hpicfDhcpSnoopDatabaseFile=_HpicfDhcpSnoopDatabaseFile_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,4),_HpicfDhcpSnoopDatabaseFile_Type())
hpicfDhcpSnoopDatabaseFile.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopDatabaseFile.setStatus(_B)
class _HpicfDhcpSnoopDatabaseWriteDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,86400))
_HpicfDhcpSnoopDatabaseWriteDelay_Type.__name__=_G
_HpicfDhcpSnoopDatabaseWriteDelay_Object=MibScalar
hpicfDhcpSnoopDatabaseWriteDelay=_HpicfDhcpSnoopDatabaseWriteDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,5),_HpicfDhcpSnoopDatabaseWriteDelay_Type())
hpicfDhcpSnoopDatabaseWriteDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopDatabaseWriteDelay.setStatus(_B)
class _HpicfDhcpSnoopDatabaseWriteTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_HpicfDhcpSnoopDatabaseWriteTimeout_Type.__name__=_G
_HpicfDhcpSnoopDatabaseWriteTimeout_Object=MibScalar
hpicfDhcpSnoopDatabaseWriteTimeout=_HpicfDhcpSnoopDatabaseWriteTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,6),_HpicfDhcpSnoopDatabaseWriteTimeout_Type())
hpicfDhcpSnoopDatabaseWriteTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopDatabaseWriteTimeout.setStatus(_B)
_HpicfDhcpSnoopOpt82Insert_Type=TruthValue
_HpicfDhcpSnoopOpt82Insert_Object=MibScalar
hpicfDhcpSnoopOpt82Insert=_HpicfDhcpSnoopOpt82Insert_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,7),_HpicfDhcpSnoopOpt82Insert_Type())
hpicfDhcpSnoopOpt82Insert.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopOpt82Insert.setStatus(_B)
class _HpicfDhcpSnoopOpt82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('keep',1),('replace',2),('drop',3)))
_HpicfDhcpSnoopOpt82Policy_Type.__name__=_E
_HpicfDhcpSnoopOpt82Policy_Object=MibScalar
hpicfDhcpSnoopOpt82Policy=_HpicfDhcpSnoopOpt82Policy_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,8),_HpicfDhcpSnoopOpt82Policy_Type())
hpicfDhcpSnoopOpt82Policy.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopOpt82Policy.setStatus(_B)
class _HpicfDhcpSnoopOpt82RemoteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mac',1),('subnetIP',2),('mgmtIP',3)))
_HpicfDhcpSnoopOpt82RemoteId_Type.__name__=_E
_HpicfDhcpSnoopOpt82RemoteId_Object=MibScalar
hpicfDhcpSnoopOpt82RemoteId=_HpicfDhcpSnoopOpt82RemoteId_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,9),_HpicfDhcpSnoopOpt82RemoteId_Type())
hpicfDhcpSnoopOpt82RemoteId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopOpt82RemoteId.setStatus(_B)
class _HpicfDhcpSnoopErrantReplyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_HpicfDhcpSnoopErrantReplyEnable_Type.__name__=_E
_HpicfDhcpSnoopErrantReplyEnable_Object=MibScalar
hpicfDhcpSnoopErrantReplyEnable=_HpicfDhcpSnoopErrantReplyEnable_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,10),_HpicfDhcpSnoopErrantReplyEnable_Type())
hpicfDhcpSnoopErrantReplyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopErrantReplyEnable.setStatus(_B)
class _HpicfDhcpSnoopDatabaseFTPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpicfDhcpSnoopDatabaseFTPort_Type.__name__=_G
_HpicfDhcpSnoopDatabaseFTPort_Object=MibScalar
hpicfDhcpSnoopDatabaseFTPort=_HpicfDhcpSnoopDatabaseFTPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,11),_HpicfDhcpSnoopDatabaseFTPort_Type())
hpicfDhcpSnoopDatabaseFTPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopDatabaseFTPort.setStatus(_B)
_HpicfDhcpSnoopDatabaseSFTPUsername_Type=SnmpAdminString
_HpicfDhcpSnoopDatabaseSFTPUsername_Object=MibScalar
hpicfDhcpSnoopDatabaseSFTPUsername=_HpicfDhcpSnoopDatabaseSFTPUsername_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,12),_HpicfDhcpSnoopDatabaseSFTPUsername_Type())
hpicfDhcpSnoopDatabaseSFTPUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopDatabaseSFTPUsername.setStatus(_B)
_HpicfDhcpSnoopDatabaseSFTPPassword_Type=SnmpAdminString
_HpicfDhcpSnoopDatabaseSFTPPassword_Object=MibScalar
hpicfDhcpSnoopDatabaseSFTPPassword=_HpicfDhcpSnoopDatabaseSFTPPassword_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,13),_HpicfDhcpSnoopDatabaseSFTPPassword_Type())
hpicfDhcpSnoopDatabaseSFTPPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopDatabaseSFTPPassword.setStatus(_B)
class _HpicfDhcpSnoopDatabaseValidateSFTPServer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_x,1),(_y,2)))
_HpicfDhcpSnoopDatabaseValidateSFTPServer_Type.__name__=_E
_HpicfDhcpSnoopDatabaseValidateSFTPServer_Object=MibScalar
hpicfDhcpSnoopDatabaseValidateSFTPServer=_HpicfDhcpSnoopDatabaseValidateSFTPServer_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,14),_HpicfDhcpSnoopDatabaseValidateSFTPServer_Type())
hpicfDhcpSnoopDatabaseValidateSFTPServer.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopDatabaseValidateSFTPServer.setStatus(_B)
class _HpicfDhcpSnoopAllowOverwriteBinding_Type(TruthValue):defaultValue=2
_HpicfDhcpSnoopAllowOverwriteBinding_Type.__name__=_w
_HpicfDhcpSnoopAllowOverwriteBinding_Object=MibScalar
hpicfDhcpSnoopAllowOverwriteBinding=_HpicfDhcpSnoopAllowOverwriteBinding_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,15),_HpicfDhcpSnoopAllowOverwriteBinding_Type())
hpicfDhcpSnoopAllowOverwriteBinding.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopAllowOverwriteBinding.setStatus(_B)
class _HpicfDhcpSnoopRateLimit_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,500))
_HpicfDhcpSnoopRateLimit_Type.__name__=_E
_HpicfDhcpSnoopRateLimit_Object=MibScalar
hpicfDhcpSnoopRateLimit=_HpicfDhcpSnoopRateLimit_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,1,16),_HpicfDhcpSnoopRateLimit_Type())
hpicfDhcpSnoopRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopRateLimit.setStatus(_B)
_HpicfDhcpSnoopPortTable_Object=MibTable
hpicfDhcpSnoopPortTable=_HpicfDhcpSnoopPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,2))
if mibBuilder.loadTexts:hpicfDhcpSnoopPortTable.setStatus(_B)
_HpicfDhcpSnoopPortEntry_Object=MibTableRow
hpicfDhcpSnoopPortEntry=_HpicfDhcpSnoopPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,2,1))
hpicfDhcpSnoopPortEntry.setIndexNames((0,_u,_v))
if mibBuilder.loadTexts:hpicfDhcpSnoopPortEntry.setStatus(_B)
_HpicfDhcpSnoopPortTrust_Type=TruthValue
_HpicfDhcpSnoopPortTrust_Object=MibTableColumn
hpicfDhcpSnoopPortTrust=_HpicfDhcpSnoopPortTrust_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,2,1,1),_HpicfDhcpSnoopPortTrust_Type())
hpicfDhcpSnoopPortTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopPortTrust.setStatus(_B)
class _HpicfDhcpSnoopPortMaxbind_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8192))
_HpicfDhcpSnoopPortMaxbind_Type.__name__=_G
_HpicfDhcpSnoopPortMaxbind_Object=MibTableColumn
hpicfDhcpSnoopPortMaxbind=_HpicfDhcpSnoopPortMaxbind_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,2,1,2),_HpicfDhcpSnoopPortMaxbind_Type())
hpicfDhcpSnoopPortMaxbind.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopPortMaxbind.setStatus(_B)
class _HpicfDhcpSnoopPortStaticBinding_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_HpicfDhcpSnoopPortStaticBinding_Type.__name__=_G
_HpicfDhcpSnoopPortStaticBinding_Object=MibTableColumn
hpicfDhcpSnoopPortStaticBinding=_HpicfDhcpSnoopPortStaticBinding_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,2,1,3),_HpicfDhcpSnoopPortStaticBinding_Type())
hpicfDhcpSnoopPortStaticBinding.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopPortStaticBinding.setStatus(_B)
class _HpicfDhcpSnoopPortDynamicBinding_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_HpicfDhcpSnoopPortDynamicBinding_Type.__name__=_G
_HpicfDhcpSnoopPortDynamicBinding_Object=MibTableColumn
hpicfDhcpSnoopPortDynamicBinding=_HpicfDhcpSnoopPortDynamicBinding_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,2,1,4),_HpicfDhcpSnoopPortDynamicBinding_Type())
hpicfDhcpSnoopPortDynamicBinding.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopPortDynamicBinding.setStatus(_B)
_HpicfDhcpSnoopServerTable_Object=MibTable
hpicfDhcpSnoopServerTable=_HpicfDhcpSnoopServerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,3))
if mibBuilder.loadTexts:hpicfDhcpSnoopServerTable.setStatus(_B)
_HpicfDhcpSnoopServerEntry_Object=MibTableRow
hpicfDhcpSnoopServerEntry=_HpicfDhcpSnoopServerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,3,1))
hpicfDhcpSnoopServerEntry.setIndexNames((0,_A,_z),(0,_A,_A0))
if mibBuilder.loadTexts:hpicfDhcpSnoopServerEntry.setStatus(_B)
_HpicfDhcpSnoopServerAddrType_Type=InetAddressType
_HpicfDhcpSnoopServerAddrType_Object=MibTableColumn
hpicfDhcpSnoopServerAddrType=_HpicfDhcpSnoopServerAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,3,1,1),_HpicfDhcpSnoopServerAddrType_Type())
hpicfDhcpSnoopServerAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDhcpSnoopServerAddrType.setStatus(_B)
_HpicfDhcpSnoopServerAddress_Type=InetAddress
_HpicfDhcpSnoopServerAddress_Object=MibTableColumn
hpicfDhcpSnoopServerAddress=_HpicfDhcpSnoopServerAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,3,1,2),_HpicfDhcpSnoopServerAddress_Type())
hpicfDhcpSnoopServerAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDhcpSnoopServerAddress.setStatus(_B)
_HpicfDhcpSnoopServerStatus_Type=RowStatus
_HpicfDhcpSnoopServerStatus_Object=MibTableColumn
hpicfDhcpSnoopServerStatus=_HpicfDhcpSnoopServerStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,3,1,3),_HpicfDhcpSnoopServerStatus_Type())
hpicfDhcpSnoopServerStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:hpicfDhcpSnoopServerStatus.setStatus(_B)
_HpicfIpStaticBindingsTable_Object=MibTable
hpicfIpStaticBindingsTable=_HpicfIpStaticBindingsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4))
if mibBuilder.loadTexts:hpicfIpStaticBindingsTable.setStatus(_B)
_HpicfIpStaticBindingsEntry_Object=MibTableRow
hpicfIpStaticBindingsEntry=_HpicfIpStaticBindingsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4,1))
hpicfIpStaticBindingsEntry.setIndexNames((0,_A,_A1),(0,_A,_A2),(0,_A,_A3))
if mibBuilder.loadTexts:hpicfIpStaticBindingsEntry.setStatus(_B)
class _HpicfIpStaticBindingsVlan_Type(VlanIndex):subtypeSpec=VlanIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_HpicfIpStaticBindingsVlan_Type.__name__=_R
_HpicfIpStaticBindingsVlan_Object=MibTableColumn
hpicfIpStaticBindingsVlan=_HpicfIpStaticBindingsVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4,1,1),_HpicfIpStaticBindingsVlan_Type())
hpicfIpStaticBindingsVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfIpStaticBindingsVlan.setStatus(_B)
_HpicfIpStaticBindingsAddrType_Type=InetAddressType
_HpicfIpStaticBindingsAddrType_Object=MibTableColumn
hpicfIpStaticBindingsAddrType=_HpicfIpStaticBindingsAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4,1,2),_HpicfIpStaticBindingsAddrType_Type())
hpicfIpStaticBindingsAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfIpStaticBindingsAddrType.setStatus(_B)
_HpicfIpStaticBindingsAddress_Type=InetAddress
_HpicfIpStaticBindingsAddress_Object=MibTableColumn
hpicfIpStaticBindingsAddress=_HpicfIpStaticBindingsAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4,1,3),_HpicfIpStaticBindingsAddress_Type())
hpicfIpStaticBindingsAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfIpStaticBindingsAddress.setStatus(_B)
_HpicfIpStaticBindingsMacAddress_Type=MacAddress
_HpicfIpStaticBindingsMacAddress_Object=MibTableColumn
hpicfIpStaticBindingsMacAddress=_HpicfIpStaticBindingsMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4,1,4),_HpicfIpStaticBindingsMacAddress_Type())
hpicfIpStaticBindingsMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:hpicfIpStaticBindingsMacAddress.setStatus(_B)
_HpicfIpStaticBindingsInterface_Type=InterfaceIndex
_HpicfIpStaticBindingsInterface_Object=MibTableColumn
hpicfIpStaticBindingsInterface=_HpicfIpStaticBindingsInterface_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4,1,5),_HpicfIpStaticBindingsInterface_Type())
hpicfIpStaticBindingsInterface.setMaxAccess(_N)
if mibBuilder.loadTexts:hpicfIpStaticBindingsInterface.setStatus(_B)
_HpicfIpStaticBindingsStatus_Type=RowStatus
_HpicfIpStaticBindingsStatus_Object=MibTableColumn
hpicfIpStaticBindingsStatus=_HpicfIpStaticBindingsStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,1,4,1,6),_HpicfIpStaticBindingsStatus_Type())
hpicfIpStaticBindingsStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:hpicfIpStaticBindingsStatus.setStatus(_B)
_HpicfIpDhcpSnoopStatus_ObjectIdentity=ObjectIdentity
hpicfIpDhcpSnoopStatus=_HpicfIpDhcpSnoopStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2))
_HpicfDhcpSnoopGlobalStats_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopGlobalStats=_HpicfDhcpSnoopGlobalStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1))
_HpicfDhcpSnoopCSForwards_Type=Counter32
_HpicfDhcpSnoopCSForwards_Object=MibScalar
hpicfDhcpSnoopCSForwards=_HpicfDhcpSnoopCSForwards_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,1),_HpicfDhcpSnoopCSForwards_Type())
hpicfDhcpSnoopCSForwards.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopCSForwards.setStatus(_B)
_HpicfDhcpSnoopCSMACMismatches_Type=Counter32
_HpicfDhcpSnoopCSMACMismatches_Object=MibScalar
hpicfDhcpSnoopCSMACMismatches=_HpicfDhcpSnoopCSMACMismatches_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,2),_HpicfDhcpSnoopCSMACMismatches_Type())
hpicfDhcpSnoopCSMACMismatches.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopCSMACMismatches.setStatus(_B)
_HpicfDhcpSnoopCSUntrustedOpt82s_Type=Counter32
_HpicfDhcpSnoopCSUntrustedOpt82s_Object=MibScalar
hpicfDhcpSnoopCSUntrustedOpt82s=_HpicfDhcpSnoopCSUntrustedOpt82s_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,3),_HpicfDhcpSnoopCSUntrustedOpt82s_Type())
hpicfDhcpSnoopCSUntrustedOpt82s.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopCSUntrustedOpt82s.setStatus(_B)
_HpicfDhcpSnoopCSBadReleases_Type=Counter32
_HpicfDhcpSnoopCSBadReleases_Object=MibScalar
hpicfDhcpSnoopCSBadReleases=_HpicfDhcpSnoopCSBadReleases_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,4),_HpicfDhcpSnoopCSBadReleases_Type())
hpicfDhcpSnoopCSBadReleases.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopCSBadReleases.setStatus(_B)
_HpicfDhcpSnoopCSUntrustedDestPorts_Type=Counter32
_HpicfDhcpSnoopCSUntrustedDestPorts_Object=MibScalar
hpicfDhcpSnoopCSUntrustedDestPorts=_HpicfDhcpSnoopCSUntrustedDestPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,5),_HpicfDhcpSnoopCSUntrustedDestPorts_Type())
hpicfDhcpSnoopCSUntrustedDestPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopCSUntrustedDestPorts.setStatus(_B)
_HpicfDhcpSnoopSCForwards_Type=Counter32
_HpicfDhcpSnoopSCForwards_Object=MibScalar
hpicfDhcpSnoopSCForwards=_HpicfDhcpSnoopSCForwards_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,6),_HpicfDhcpSnoopSCForwards_Type())
hpicfDhcpSnoopSCForwards.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopSCForwards.setStatus(_B)
_HpicfDhcpSnoopSCUntrustedPorts_Type=Counter32
_HpicfDhcpSnoopSCUntrustedPorts_Object=MibScalar
hpicfDhcpSnoopSCUntrustedPorts=_HpicfDhcpSnoopSCUntrustedPorts_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,7),_HpicfDhcpSnoopSCUntrustedPorts_Type())
hpicfDhcpSnoopSCUntrustedPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopSCUntrustedPorts.setStatus(_B)
_HpicfDhcpSnoopSCUntrustedServers_Type=Counter32
_HpicfDhcpSnoopSCUntrustedServers_Object=MibScalar
hpicfDhcpSnoopSCUntrustedServers=_HpicfDhcpSnoopSCUntrustedServers_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,8),_HpicfDhcpSnoopSCUntrustedServers_Type())
hpicfDhcpSnoopSCUntrustedServers.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopSCUntrustedServers.setStatus(_B)
_HpicfDhcpSnoopSCOpt82Failures_Type=Counter32
_HpicfDhcpSnoopSCOpt82Failures_Object=MibScalar
hpicfDhcpSnoopSCOpt82Failures=_HpicfDhcpSnoopSCOpt82Failures_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,9),_HpicfDhcpSnoopSCOpt82Failures_Type())
hpicfDhcpSnoopSCOpt82Failures.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopSCOpt82Failures.setStatus(_B)
_HpicfDhcpSnoopDBFileWriteAttempts_Type=Counter32
_HpicfDhcpSnoopDBFileWriteAttempts_Object=MibScalar
hpicfDhcpSnoopDBFileWriteAttempts=_HpicfDhcpSnoopDBFileWriteAttempts_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,10),_HpicfDhcpSnoopDBFileWriteAttempts_Type())
hpicfDhcpSnoopDBFileWriteAttempts.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopDBFileWriteAttempts.setStatus(_B)
_HpicfDhcpSnoopDBFileWriteFailures_Type=Counter32
_HpicfDhcpSnoopDBFileWriteFailures_Object=MibScalar
hpicfDhcpSnoopDBFileWriteFailures=_HpicfDhcpSnoopDBFileWriteFailures_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,11),_HpicfDhcpSnoopDBFileWriteFailures_Type())
hpicfDhcpSnoopDBFileWriteFailures.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopDBFileWriteFailures.setStatus(_B)
class _HpicfDhcpSnoopDBFileReadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_A4,1),(_A5,2),(_A6,3),('failed',4)))
_HpicfDhcpSnoopDBFileReadStatus_Type.__name__=_E
_HpicfDhcpSnoopDBFileReadStatus_Object=MibScalar
hpicfDhcpSnoopDBFileReadStatus=_HpicfDhcpSnoopDBFileReadStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,12),_HpicfDhcpSnoopDBFileReadStatus_Type())
hpicfDhcpSnoopDBFileReadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopDBFileReadStatus.setStatus(_B)
class _HpicfDhcpSnoopDBFileWriteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_A4,1),('delaying',2),(_A5,3),(_A6,4),('failed',5)))
_HpicfDhcpSnoopDBFileWriteStatus_Type.__name__=_E
_HpicfDhcpSnoopDBFileWriteStatus_Object=MibScalar
hpicfDhcpSnoopDBFileWriteStatus=_HpicfDhcpSnoopDBFileWriteStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,13),_HpicfDhcpSnoopDBFileWriteStatus_Type())
hpicfDhcpSnoopDBFileWriteStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopDBFileWriteStatus.setStatus(_B)
_HpicfDhcpSnoopDBFileLastWriteTime_Type=DateAndTime
_HpicfDhcpSnoopDBFileLastWriteTime_Object=MibScalar
hpicfDhcpSnoopDBFileLastWriteTime=_HpicfDhcpSnoopDBFileLastWriteTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,14),_HpicfDhcpSnoopDBFileLastWriteTime_Type())
hpicfDhcpSnoopDBFileLastWriteTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopDBFileLastWriteTime.setStatus(_B)
_HpicfDhcpSnoopPktsSent_Type=Counter32
_HpicfDhcpSnoopPktsSent_Object=MibScalar
hpicfDhcpSnoopPktsSent=_HpicfDhcpSnoopPktsSent_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,15),_HpicfDhcpSnoopPktsSent_Type())
hpicfDhcpSnoopPktsSent.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopPktsSent.setStatus(_B)
_HpicfDhcpSnoopPktsReceived_Type=Counter32
_HpicfDhcpSnoopPktsReceived_Object=MibScalar
hpicfDhcpSnoopPktsReceived=_HpicfDhcpSnoopPktsReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,16),_HpicfDhcpSnoopPktsReceived_Type())
hpicfDhcpSnoopPktsReceived.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopPktsReceived.setStatus(_B)
_HpicfDhcpSnoopPktsDropped_Type=Counter32
_HpicfDhcpSnoopPktsDropped_Object=MibScalar
hpicfDhcpSnoopPktsDropped=_HpicfDhcpSnoopPktsDropped_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,17),_HpicfDhcpSnoopPktsDropped_Type())
hpicfDhcpSnoopPktsDropped.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopPktsDropped.setStatus(_B)
_HpicfDhcpSnoopMaxbindPktsDropped_Type=Counter32
_HpicfDhcpSnoopMaxbindPktsDropped_Object=MibScalar
hpicfDhcpSnoopMaxbindPktsDropped=_HpicfDhcpSnoopMaxbindPktsDropped_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,1,18),_HpicfDhcpSnoopMaxbindPktsDropped_Type())
hpicfDhcpSnoopMaxbindPktsDropped.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopMaxbindPktsDropped.setStatus(_B)
_HpicfDhcpSnoopBindingsTable_Object=MibTable
hpicfDhcpSnoopBindingsTable=_HpicfDhcpSnoopBindingsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2))
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsTable.setStatus(_B)
_HpicfDhcpSnoopBindingsEntry_Object=MibTableRow
hpicfDhcpSnoopBindingsEntry=_HpicfDhcpSnoopBindingsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1))
hpicfDhcpSnoopBindingsEntry.setIndexNames((0,_A,_A7),(0,_A,_A8),(0,_A,_A9),(0,_A,_AA))
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsEntry.setStatus(_B)
class _HpicfDhcpSnoopBindingsVlan_Type(VlanIndex):subtypeSpec=VlanIndex.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_HpicfDhcpSnoopBindingsVlan_Type.__name__=_R
_HpicfDhcpSnoopBindingsVlan_Object=MibTableColumn
hpicfDhcpSnoopBindingsVlan=_HpicfDhcpSnoopBindingsVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,1),_HpicfDhcpSnoopBindingsVlan_Type())
hpicfDhcpSnoopBindingsVlan.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsVlan.setStatus(_B)
_HpicfDhcpSnoopBindingsMacAddress_Type=MacAddress
_HpicfDhcpSnoopBindingsMacAddress_Object=MibTableColumn
hpicfDhcpSnoopBindingsMacAddress=_HpicfDhcpSnoopBindingsMacAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,2),_HpicfDhcpSnoopBindingsMacAddress_Type())
hpicfDhcpSnoopBindingsMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsMacAddress.setStatus(_B)
_HpicfDhcpSnoopBindingsAddrType_Type=InetAddressType
_HpicfDhcpSnoopBindingsAddrType_Object=MibTableColumn
hpicfDhcpSnoopBindingsAddrType=_HpicfDhcpSnoopBindingsAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,3),_HpicfDhcpSnoopBindingsAddrType_Type())
hpicfDhcpSnoopBindingsAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsAddrType.setStatus(_B)
_HpicfDhcpSnoopBindingsAddress_Type=InetAddress
_HpicfDhcpSnoopBindingsAddress_Object=MibTableColumn
hpicfDhcpSnoopBindingsAddress=_HpicfDhcpSnoopBindingsAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,4),_HpicfDhcpSnoopBindingsAddress_Type())
hpicfDhcpSnoopBindingsAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsAddress.setStatus(_B)
_HpicfDhcpSnoopBindingsInterface_Type=InterfaceIndex
_HpicfDhcpSnoopBindingsInterface_Object=MibTableColumn
hpicfDhcpSnoopBindingsInterface=_HpicfDhcpSnoopBindingsInterface_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,5),_HpicfDhcpSnoopBindingsInterface_Type())
hpicfDhcpSnoopBindingsInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsInterface.setStatus(_B)
_HpicfDhcpSnoopBindingsLeaseTime_Type=Unsigned32
_HpicfDhcpSnoopBindingsLeaseTime_Object=MibTableColumn
hpicfDhcpSnoopBindingsLeaseTime=_HpicfDhcpSnoopBindingsLeaseTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,6),_HpicfDhcpSnoopBindingsLeaseTime_Type())
hpicfDhcpSnoopBindingsLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsLeaseTime.setStatus(_B)
class _HpicfDhcpSnoopBindingsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dhcp',1),('static',2)))
_HpicfDhcpSnoopBindingsType_Type.__name__=_E
_HpicfDhcpSnoopBindingsType_Object=MibTableColumn
hpicfDhcpSnoopBindingsType=_HpicfDhcpSnoopBindingsType_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,7),_HpicfDhcpSnoopBindingsType_Type())
hpicfDhcpSnoopBindingsType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsType.setStatus(_B)
_HpicfDhcpSnoopBindingsSecVlan_Type=Unsigned32
_HpicfDhcpSnoopBindingsSecVlan_Object=MibTableColumn
hpicfDhcpSnoopBindingsSecVlan=_HpicfDhcpSnoopBindingsSecVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,2,2,1,8),_HpicfDhcpSnoopBindingsSecVlan_Type())
hpicfDhcpSnoopBindingsSecVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsSecVlan.setStatus(_B)
_HpicfDhcpSnoopNotifyObjects_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopNotifyObjects=_HpicfDhcpSnoopNotifyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1,3))
_HpicfDhcpSnoopNotifyCount_Type=Counter32
_HpicfDhcpSnoopNotifyCount_Object=MibScalar
hpicfDhcpSnoopNotifyCount=_HpicfDhcpSnoopNotifyCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,3,1),_HpicfDhcpSnoopNotifyCount_Type())
hpicfDhcpSnoopNotifyCount.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfDhcpSnoopNotifyCount.setStatus(_B)
_HpicfDhcpSnoopErrantSrcMAC_Type=MacAddress
_HpicfDhcpSnoopErrantSrcMAC_Object=MibScalar
hpicfDhcpSnoopErrantSrcMAC=_HpicfDhcpSnoopErrantSrcMAC_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,3,2),_HpicfDhcpSnoopErrantSrcMAC_Type())
hpicfDhcpSnoopErrantSrcMAC.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfDhcpSnoopErrantSrcMAC.setStatus(_B)
_HpicfDhcpSnoopErrantSrcIPType_Type=InetAddressType
_HpicfDhcpSnoopErrantSrcIPType_Object=MibScalar
hpicfDhcpSnoopErrantSrcIPType=_HpicfDhcpSnoopErrantSrcIPType_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,3,3),_HpicfDhcpSnoopErrantSrcIPType_Type())
hpicfDhcpSnoopErrantSrcIPType.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfDhcpSnoopErrantSrcIPType.setStatus(_B)
_HpicfDhcpSnoopErrantSrcIP_Type=InetAddress
_HpicfDhcpSnoopErrantSrcIP_Object=MibScalar
hpicfDhcpSnoopErrantSrcIP=_HpicfDhcpSnoopErrantSrcIP_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,3,4),_HpicfDhcpSnoopErrantSrcIP_Type())
hpicfDhcpSnoopErrantSrcIP.setMaxAccess(_O)
if mibBuilder.loadTexts:hpicfDhcpSnoopErrantSrcIP.setStatus(_B)
_HpicfDhcpSnoopClearStatsOptions_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopClearStatsOptions=_HpicfDhcpSnoopClearStatsOptions_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1,4))
_HpicfDhcpSnoopClearStats_Type=TruthValue
_HpicfDhcpSnoopClearStats_Object=MibScalar
hpicfDhcpSnoopClearStats=_HpicfDhcpSnoopClearStats_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,4,1),_HpicfDhcpSnoopClearStats_Type())
hpicfDhcpSnoopClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopClearStats.setStatus(_B)
_HpicfDhcpSnoopClearBindingsOptions_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopClearBindingsOptions=_HpicfDhcpSnoopClearBindingsOptions_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,1,5))
_HpicfDhcpSnoopClearBindings_Type=TruthValue
_HpicfDhcpSnoopClearBindings_Object=MibScalar
hpicfDhcpSnoopClearBindings=_HpicfDhcpSnoopClearBindings_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,5,1),_HpicfDhcpSnoopClearBindings_Type())
hpicfDhcpSnoopClearBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopClearBindings.setStatus(_B)
_HpicfDhcpSnoopClearBindingsIpType_Type=InetAddressType
_HpicfDhcpSnoopClearBindingsIpType_Object=MibScalar
hpicfDhcpSnoopClearBindingsIpType=_HpicfDhcpSnoopClearBindingsIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,5,2),_HpicfDhcpSnoopClearBindingsIpType_Type())
hpicfDhcpSnoopClearBindingsIpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopClearBindingsIpType.setStatus(_B)
_HpicfDhcpSnoopClearBindingsIpAddr_Type=InetAddress
_HpicfDhcpSnoopClearBindingsIpAddr_Object=MibScalar
hpicfDhcpSnoopClearBindingsIpAddr=_HpicfDhcpSnoopClearBindingsIpAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,5,3),_HpicfDhcpSnoopClearBindingsIpAddr_Type())
hpicfDhcpSnoopClearBindingsIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopClearBindingsIpAddr.setStatus(_B)
_HpicfDhcpSnoopClearBindingsPort_Type=InterfaceIndexOrZero
_HpicfDhcpSnoopClearBindingsPort_Object=MibScalar
hpicfDhcpSnoopClearBindingsPort=_HpicfDhcpSnoopClearBindingsPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,5,4),_HpicfDhcpSnoopClearBindingsPort_Type())
hpicfDhcpSnoopClearBindingsPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopClearBindingsPort.setStatus(_B)
_HpicfDhcpSnoopClearBindingsVlan_Type=InterfaceIndexOrZero
_HpicfDhcpSnoopClearBindingsVlan_Object=MibScalar
hpicfDhcpSnoopClearBindingsVlan=_HpicfDhcpSnoopClearBindingsVlan_Object((1,3,6,1,4,1,11,2,14,11,5,1,34,1,5,5),_HpicfDhcpSnoopClearBindingsVlan_Type())
hpicfDhcpSnoopClearBindingsVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDhcpSnoopClearBindingsVlan.setStatus(_B)
_HpicfDhcpSnoopConformance_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopConformance=_HpicfDhcpSnoopConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,2))
_HpicfIpDhcpSnoopGroups_ObjectIdentity=ObjectIdentity
hpicfIpDhcpSnoopGroups=_HpicfIpDhcpSnoopGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1))
_HpicfDhcpSnoopCompliances_ObjectIdentity=ObjectIdentity
hpicfDhcpSnoopCompliances=_HpicfDhcpSnoopCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2))
hpicfDhcpSnoopBaseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,1))
hpicfDhcpSnoopBaseGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hpicfDhcpSnoopBaseGroup.setStatus(_K)
hpicfDhcpSnoopOpt82Group=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,2))
hpicfDhcpSnoopOpt82Group.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:hpicfDhcpSnoopOpt82Group.setStatus(_B)
hpicfDhcpSnoopServersGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,3))
hpicfDhcpSnoopServersGroup.setObjects(*((_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:hpicfDhcpSnoopServersGroup.setStatus(_B)
hpicfDhcpSnoopDbaseFileGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,4))
hpicfDhcpSnoopDbaseFileGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:hpicfDhcpSnoopDbaseFileGroup.setStatus(_K)
hpicfDhcpSnoopBindingsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,5))
hpicfDhcpSnoopBindingsGroup.setObjects(*((_A,_AI),(_A,_AJ),(_A,_k),(_A,_AK)))
if mibBuilder.loadTexts:hpicfDhcpSnoopBindingsGroup.setStatus(_B)
hpicfDhcpSnoopStaticBindingsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,6))
hpicfDhcpSnoopStaticBindingsGroup.setObjects(*((_A,_AL),(_A,_AM),(_A,_AN),(_A,_k)))
if mibBuilder.loadTexts:hpicfDhcpSnoopStaticBindingsGroup.setStatus(_B)
hpicfDhcpSnoopNotifyObjsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,7))
hpicfDhcpSnoopNotifyObjsGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_AO)))
if mibBuilder.loadTexts:hpicfDhcpSnoopNotifyObjsGroup.setStatus(_B)
hpicfDhcpSnoopPktsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,9))
hpicfDhcpSnoopPktsGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:hpicfDhcpSnoopPktsGroup.setStatus(_B)
hpicfDhcpSnoopClearStatsOptionsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,10))
hpicfDhcpSnoopClearStatsOptionsGroup.setObjects((_A,_AP))
if mibBuilder.loadTexts:hpicfDhcpSnoopClearStatsOptionsGroup.setStatus(_B)
hpicfDhcpSnoopMaxbindingGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,11))
hpicfDhcpSnoopMaxbindingGroup.setObjects(*((_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:hpicfDhcpSnoopMaxbindingGroup.setStatus(_B)
hpicfDhcpSnoopPktsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,12))
hpicfDhcpSnoopPktsGroup1.setObjects(*((_A,_p),(_A,_q),(_A,_r),(_A,_AT)))
if mibBuilder.loadTexts:hpicfDhcpSnoopPktsGroup1.setStatus(_B)
hpicfDhcpSnoopDbaseFileGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,13))
hpicfDhcpSnoopDbaseFileGroup1.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:hpicfDhcpSnoopDbaseFileGroup1.setStatus(_B)
hpicfDhcpSnoopAllowOverwriteBindingGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,14))
hpicfDhcpSnoopAllowOverwriteBindingGroup.setObjects((_A,_AY))
if mibBuilder.loadTexts:hpicfDhcpSnoopAllowOverwriteBindingGroup.setStatus(_B)
hpicfDhcpSnoopClearBindingsOptionsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,15))
hpicfDhcpSnoopClearBindingsOptionsGroup.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:hpicfDhcpSnoopClearBindingsOptionsGroup.setStatus(_B)
hpicfDhcpSnoopBaseGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,16))
hpicfDhcpSnoopBaseGroup1.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_Ae)))
if mibBuilder.loadTexts:hpicfDhcpSnoopBaseGroup1.setStatus(_B)
hpicfDhcpSnoopErrantReply=NotificationType((1,3,6,1,4,1,11,2,14,11,5,1,34,0,1))
hpicfDhcpSnoopErrantReply.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:hpicfDhcpSnoopErrantReply.setStatus(_B)
hpicfDhcpSnoopNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,5,1,34,2,1,8))
hpicfDhcpSnoopNotificationGroup.setObjects((_A,_Af))
if mibBuilder.loadTexts:hpicfDhcpSnoopNotificationGroup.setStatus(_B)
hpicfDhcpSnoopCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,1))
hpicfDhcpSnoopCompliance.setObjects(*((_A,_L),(_A,_H),(_A,_I),(_A,_s),(_A,_J)))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance.setStatus(_K)
hpicfDhcpSnoopCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,2))
hpicfDhcpSnoopCompliance2.setObjects(*((_A,_L),(_A,_H),(_A,_I),(_A,_P),(_A,_J),(_A,_M)))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance2.setStatus(_B)
hpicfDhcpSnoopCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,3))
hpicfDhcpSnoopCompliance3.setObjects(*((_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance3.setStatus(_B)
hpicfDhcpSnoopCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,4))
hpicfDhcpSnoopCompliance4.setObjects((_A,_Ai))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance4.setStatus(_B)
hpicfDhcpSnoopClearStatsCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,5))
hpicfDhcpSnoopClearStatsCompliance.setObjects((_A,_Aj))
if mibBuilder.loadTexts:hpicfDhcpSnoopClearStatsCompliance.setStatus(_B)
hpicfDhcpSnoopCompliance6=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,6))
hpicfDhcpSnoopCompliance6.setObjects(*((_A,_L),(_A,_H),(_A,_I),(_A,_s),(_A,_J),(_A,_M),(_A,_Q)))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance6.setStatus(_K)
hpicfDhcpSnoopCompliance7=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,7))
hpicfDhcpSnoopCompliance7.setObjects((_A,_Ak))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance7.setStatus(_B)
hpicfDhcpSnoopCompliance8=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,8))
hpicfDhcpSnoopCompliance8.setObjects(*((_A,_L),(_A,_H),(_A,_I),(_A,_P),(_A,_J),(_A,_M),(_A,_Q)))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance8.setStatus(_K)
hpicfDhcpSnoopCompliance9=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,9))
hpicfDhcpSnoopCompliance9.setObjects((_A,_Al))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance9.setStatus(_B)
hpicfDhcpSnoopCompliance10=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,10))
hpicfDhcpSnoopCompliance10.setObjects((_A,_Am))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance10.setStatus(_B)
hpicfDhcpSnoopCompliance11=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,34,2,2,11))
hpicfDhcpSnoopCompliance11.setObjects(*((_A,_An),(_A,_H),(_A,_I),(_A,_P),(_A,_J),(_A,_M),(_A,_Q)))
if mibBuilder.loadTexts:hpicfDhcpSnoopCompliance11.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfIpDhcpSnoop':hpicfIpDhcpSnoop,'hpicfDhcpSnoopNotifications':hpicfDhcpSnoopNotifications,_Af:hpicfDhcpSnoopErrantReply,'hpicfIpDhcpSnoopObjects':hpicfIpDhcpSnoopObjects,'hpicfIpDhcpSnoopConfig':hpicfIpDhcpSnoopConfig,'hpicfDhcpSnoopGlobalCfg':hpicfDhcpSnoopGlobalCfg,_S:hpicfDhcpSnoopEnable,_T:hpicfDhcpSnoopVlanEnable,_U:hpicfDhcpSnoopVerifyMac,_c:hpicfDhcpSnoopDatabaseFile,_d:hpicfDhcpSnoopDatabaseWriteDelay,_e:hpicfDhcpSnoopDatabaseWriteTimeout,_AB:hpicfDhcpSnoopOpt82Insert,_AC:hpicfDhcpSnoopOpt82Policy,_AD:hpicfDhcpSnoopOpt82RemoteId,_AO:hpicfDhcpSnoopErrantReplyEnable,_AU:hpicfDhcpSnoopDatabaseFTPort,_AV:hpicfDhcpSnoopDatabaseSFTPUsername,_AW:hpicfDhcpSnoopDatabaseSFTPPassword,_AX:hpicfDhcpSnoopDatabaseValidateSFTPServer,_AY:hpicfDhcpSnoopAllowOverwriteBinding,_Ae:hpicfDhcpSnoopRateLimit,'hpicfDhcpSnoopPortTable':hpicfDhcpSnoopPortTable,'hpicfDhcpSnoopPortEntry':hpicfDhcpSnoopPortEntry,_V:hpicfDhcpSnoopPortTrust,_AQ:hpicfDhcpSnoopPortMaxbind,_AR:hpicfDhcpSnoopPortStaticBinding,_AS:hpicfDhcpSnoopPortDynamicBinding,'hpicfDhcpSnoopServerTable':hpicfDhcpSnoopServerTable,'hpicfDhcpSnoopServerEntry':hpicfDhcpSnoopServerEntry,_z:hpicfDhcpSnoopServerAddrType,_A0:hpicfDhcpSnoopServerAddress,_AG:hpicfDhcpSnoopServerStatus,'hpicfIpStaticBindingsTable':hpicfIpStaticBindingsTable,'hpicfIpStaticBindingsEntry':hpicfIpStaticBindingsEntry,_A1:hpicfIpStaticBindingsVlan,_A2:hpicfIpStaticBindingsAddrType,_A3:hpicfIpStaticBindingsAddress,_AL:hpicfIpStaticBindingsMacAddress,_AM:hpicfIpStaticBindingsInterface,_AN:hpicfIpStaticBindingsStatus,'hpicfIpDhcpSnoopStatus':hpicfIpDhcpSnoopStatus,'hpicfDhcpSnoopGlobalStats':hpicfDhcpSnoopGlobalStats,_W:hpicfDhcpSnoopCSForwards,_X:hpicfDhcpSnoopCSMACMismatches,_AE:hpicfDhcpSnoopCSUntrustedOpt82s,_Y:hpicfDhcpSnoopCSBadReleases,_Z:hpicfDhcpSnoopCSUntrustedDestPorts,_a:hpicfDhcpSnoopSCForwards,_b:hpicfDhcpSnoopSCUntrustedPorts,_AH:hpicfDhcpSnoopSCUntrustedServers,_AF:hpicfDhcpSnoopSCOpt82Failures,_f:hpicfDhcpSnoopDBFileWriteAttempts,_g:hpicfDhcpSnoopDBFileWriteFailures,_h:hpicfDhcpSnoopDBFileReadStatus,_i:hpicfDhcpSnoopDBFileWriteStatus,_j:hpicfDhcpSnoopDBFileLastWriteTime,_p:hpicfDhcpSnoopPktsSent,_q:hpicfDhcpSnoopPktsReceived,_r:hpicfDhcpSnoopPktsDropped,_AT:hpicfDhcpSnoopMaxbindPktsDropped,'hpicfDhcpSnoopBindingsTable':hpicfDhcpSnoopBindingsTable,'hpicfDhcpSnoopBindingsEntry':hpicfDhcpSnoopBindingsEntry,_A7:hpicfDhcpSnoopBindingsVlan,_A8:hpicfDhcpSnoopBindingsMacAddress,_A9:hpicfDhcpSnoopBindingsAddrType,_AA:hpicfDhcpSnoopBindingsAddress,_AI:hpicfDhcpSnoopBindingsInterface,_AJ:hpicfDhcpSnoopBindingsLeaseTime,_k:hpicfDhcpSnoopBindingsType,_AK:hpicfDhcpSnoopBindingsSecVlan,'hpicfDhcpSnoopNotifyObjects':hpicfDhcpSnoopNotifyObjects,_l:hpicfDhcpSnoopNotifyCount,_m:hpicfDhcpSnoopErrantSrcMAC,_n:hpicfDhcpSnoopErrantSrcIPType,_o:hpicfDhcpSnoopErrantSrcIP,'hpicfDhcpSnoopClearStatsOptions':hpicfDhcpSnoopClearStatsOptions,_AP:hpicfDhcpSnoopClearStats,'hpicfDhcpSnoopClearBindingsOptions':hpicfDhcpSnoopClearBindingsOptions,_AZ:hpicfDhcpSnoopClearBindings,_Aa:hpicfDhcpSnoopClearBindingsIpType,_Ab:hpicfDhcpSnoopClearBindingsIpAddr,_Ac:hpicfDhcpSnoopClearBindingsPort,_Ad:hpicfDhcpSnoopClearBindingsVlan,'hpicfDhcpSnoopConformance':hpicfDhcpSnoopConformance,'hpicfIpDhcpSnoopGroups':hpicfIpDhcpSnoopGroups,_L:hpicfDhcpSnoopBaseGroup,_H:hpicfDhcpSnoopOpt82Group,_I:hpicfDhcpSnoopServersGroup,_s:hpicfDhcpSnoopDbaseFileGroup,_J:hpicfDhcpSnoopBindingsGroup,_M:hpicfDhcpSnoopStaticBindingsGroup,_Ag:hpicfDhcpSnoopNotifyObjsGroup,_Ah:hpicfDhcpSnoopNotificationGroup,_Ai:hpicfDhcpSnoopPktsGroup,_Aj:hpicfDhcpSnoopClearStatsOptionsGroup,_Q:hpicfDhcpSnoopMaxbindingGroup,_Ak:hpicfDhcpSnoopPktsGroup1,_P:hpicfDhcpSnoopDbaseFileGroup1,_Al:hpicfDhcpSnoopAllowOverwriteBindingGroup,_Am:hpicfDhcpSnoopClearBindingsOptionsGroup,_An:hpicfDhcpSnoopBaseGroup1,'hpicfDhcpSnoopCompliances':hpicfDhcpSnoopCompliances,'hpicfDhcpSnoopCompliance':hpicfDhcpSnoopCompliance,'hpicfDhcpSnoopCompliance2':hpicfDhcpSnoopCompliance2,'hpicfDhcpSnoopCompliance3':hpicfDhcpSnoopCompliance3,'hpicfDhcpSnoopCompliance4':hpicfDhcpSnoopCompliance4,'hpicfDhcpSnoopClearStatsCompliance':hpicfDhcpSnoopClearStatsCompliance,'hpicfDhcpSnoopCompliance6':hpicfDhcpSnoopCompliance6,'hpicfDhcpSnoopCompliance7':hpicfDhcpSnoopCompliance7,'hpicfDhcpSnoopCompliance8':hpicfDhcpSnoopCompliance8,'hpicfDhcpSnoopCompliance9':hpicfDhcpSnoopCompliance9,'hpicfDhcpSnoopCompliance10':hpicfDhcpSnoopCompliance10,'hpicfDhcpSnoopCompliance11':hpicfDhcpSnoopCompliance11})