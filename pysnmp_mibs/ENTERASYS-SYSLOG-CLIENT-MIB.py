_z='etsysSyslogServerGroup3'
_y='etsysSyslogServerGroup2'
_x='etsysSyslogSecureGroup'
_w='etsysSyslogNotificationGroup'
_v='etsysSyslogServerGroup'
_u='etsysSyslogSecureLogDroppedMsgNotification'
_t='etsysSyslogSecureLogArchiveNotification'
_s='etsysSyslogServerVirtualRouterName'
_r='etsysSyslogServerDefaultSeverity'
_q='etsysSyslogServerDefaultFacility'
_p='etsysSyslogServerDefaultUdpPort'
_o='etsysSyslogApplicationAllowedServers'
_n='etsysSyslogApplicationSeverity'
_m='etsysSyslogApplicationMnemonic'
_l='etsysSyslogApplicationDescription'
_k='etsysSyslogClientControl'
_j='etsysSyslogClientLastMessageTime'
_i='etsysSyslogClientMessagesDropped'
_h='etsysSyslogClientMessages'
_g='etsysSyslogApplicationIndex'
_f='SyslogFacility'
_e='SyslogUdpPort'
_d='not-accessible'
_c='etsysSyslogServerIndex'
_b='Integer32'
_a='OctetString'
_Z='etsysSyslogServerHostname'
_Y='etsysSyslogClientSecureMessagesDropped'
_X='SyslogSeverity'
_W='Bits'
_V='etsysSyslogApplicationGroup'
_U='etsysSyslogServerDefaultsGroup'
_T='etsysSyslogClientGroup'
_S='deprecated'
_R='etsysSyslogServerRowStatus'
_Q='etsysSyslogServerMessagesIgnored'
_P='etsysSyslogServerSeverity'
_O='etsysSyslogServerFacility'
_N='etsysSyslogServerUdpPort'
_M='etsysSyslogServerAddress'
_L='etsysSyslogServerAddressType'
_K='etsysSyslogServerDescription'
_J='etsysSyslogServerTableNextAvailableIndex'
_I='etsysSyslogServerNumEntries'
_H='etsysSyslogServerMaxEntries'
_G='Unsigned32'
_F='SnmpAdminString'
_E='read-write'
_D='read-create'
_C='read-only'
_B='current'
_A='ENTERASYS-SYSLOG-CLIENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_a,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_W,'Counter32','Counter64','Gauge32',_b,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
etsysSyslogClientMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,14))
if mibBuilder.loadTexts:etsysSyslogClientMIB.setRevisions(('2017-08-31 11:12','2017-05-30 18:23','2013-02-26 20:13','2011-03-08 20:15','2009-07-17 14:38','2009-02-17 20:53','2009-01-16 18:59','2003-11-06 15:15','2003-07-31 14:19','2001-12-03 19:55','2001-08-08 00:00'))
class SyslogUdpPort(TextualConvention,Unsigned32):status=_B;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class SyslogFacility(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,17,18,19,20,21,22,23)));namedValues=NamedValues(*(('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23)))
class SyslogSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('info',7),('debug',8)))
_EtsysSyslogClient_ObjectIdentity=ObjectIdentity
etsysSyslogClient=_EtsysSyslogClient_ObjectIdentity((1,3,6,1,4,1,5624,1,2,14,1))
_EtsysSyslogClientMessages_Type=Counter32
_EtsysSyslogClientMessages_Object=MibScalar
etsysSyslogClientMessages=_EtsysSyslogClientMessages_Object((1,3,6,1,4,1,5624,1,2,14,1,1),_EtsysSyslogClientMessages_Type())
etsysSyslogClientMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogClientMessages.setStatus(_B)
_EtsysSyslogClientMessagesDropped_Type=Counter32
_EtsysSyslogClientMessagesDropped_Object=MibScalar
etsysSyslogClientMessagesDropped=_EtsysSyslogClientMessagesDropped_Object((1,3,6,1,4,1,5624,1,2,14,1,2),_EtsysSyslogClientMessagesDropped_Type())
etsysSyslogClientMessagesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogClientMessagesDropped.setStatus(_B)
_EtsysSyslogClientLastMessageTime_Type=TimeStamp
_EtsysSyslogClientLastMessageTime_Object=MibScalar
etsysSyslogClientLastMessageTime=_EtsysSyslogClientLastMessageTime_Object((1,3,6,1,4,1,5624,1,2,14,1,3),_EtsysSyslogClientLastMessageTime_Type())
etsysSyslogClientLastMessageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogClientLastMessageTime.setStatus(_B)
class _EtsysSyslogClientControl_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*(('etsysSyslogClientControlConsoleLogging',0),('etsysSyslogClientControlPersistentLogging',1),('etsysSyslogClientControlSecurePersistentLogging',2)))
_EtsysSyslogClientControl_Type.__name__=_W
_EtsysSyslogClientControl_Object=MibScalar
etsysSyslogClientControl=_EtsysSyslogClientControl_Object((1,3,6,1,4,1,5624,1,2,14,1,4),_EtsysSyslogClientControl_Type())
etsysSyslogClientControl.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSyslogClientControl.setStatus(_B)
_EtsysSyslogClientSecureMessagesDropped_Type=Counter32
_EtsysSyslogClientSecureMessagesDropped_Object=MibScalar
etsysSyslogClientSecureMessagesDropped=_EtsysSyslogClientSecureMessagesDropped_Object((1,3,6,1,4,1,5624,1,2,14,1,5),_EtsysSyslogClientSecureMessagesDropped_Type())
etsysSyslogClientSecureMessagesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogClientSecureMessagesDropped.setStatus(_B)
_EtsysSyslogServer_ObjectIdentity=ObjectIdentity
etsysSyslogServer=_EtsysSyslogServer_ObjectIdentity((1,3,6,1,4,1,5624,1,2,14,2))
class _EtsysSyslogServerMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_EtsysSyslogServerMaxEntries_Type.__name__=_G
_EtsysSyslogServerMaxEntries_Object=MibScalar
etsysSyslogServerMaxEntries=_EtsysSyslogServerMaxEntries_Object((1,3,6,1,4,1,5624,1,2,14,2,1),_EtsysSyslogServerMaxEntries_Type())
etsysSyslogServerMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogServerMaxEntries.setStatus(_B)
_EtsysSyslogServerNumEntries_Type=Gauge32
_EtsysSyslogServerNumEntries_Object=MibScalar
etsysSyslogServerNumEntries=_EtsysSyslogServerNumEntries_Object((1,3,6,1,4,1,5624,1,2,14,2,2),_EtsysSyslogServerNumEntries_Type())
etsysSyslogServerNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogServerNumEntries.setStatus(_B)
class _EtsysSyslogServerTableNextAvailableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_EtsysSyslogServerTableNextAvailableIndex_Type.__name__=_G
_EtsysSyslogServerTableNextAvailableIndex_Object=MibScalar
etsysSyslogServerTableNextAvailableIndex=_EtsysSyslogServerTableNextAvailableIndex_Object((1,3,6,1,4,1,5624,1,2,14,2,3),_EtsysSyslogServerTableNextAvailableIndex_Type())
etsysSyslogServerTableNextAvailableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogServerTableNextAvailableIndex.setStatus(_B)
_EtsysSyslogServerTable_Object=MibTable
etsysSyslogServerTable=_EtsysSyslogServerTable_Object((1,3,6,1,4,1,5624,1,2,14,2,4))
if mibBuilder.loadTexts:etsysSyslogServerTable.setStatus(_B)
_EtsysSyslogServerEntry_Object=MibTableRow
etsysSyslogServerEntry=_EtsysSyslogServerEntry_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1))
etsysSyslogServerEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:etsysSyslogServerEntry.setStatus(_B)
class _EtsysSyslogServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_EtsysSyslogServerIndex_Type.__name__=_G
_EtsysSyslogServerIndex_Object=MibTableColumn
etsysSyslogServerIndex=_EtsysSyslogServerIndex_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,1),_EtsysSyslogServerIndex_Type())
etsysSyslogServerIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:etsysSyslogServerIndex.setStatus(_B)
class _EtsysSyslogServerDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysSyslogServerDescription_Type.__name__=_F
_EtsysSyslogServerDescription_Object=MibTableColumn
etsysSyslogServerDescription=_EtsysSyslogServerDescription_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,2),_EtsysSyslogServerDescription_Type())
etsysSyslogServerDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerDescription.setStatus(_B)
_EtsysSyslogServerAddressType_Type=InetAddressType
_EtsysSyslogServerAddressType_Object=MibTableColumn
etsysSyslogServerAddressType=_EtsysSyslogServerAddressType_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,3),_EtsysSyslogServerAddressType_Type())
etsysSyslogServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerAddressType.setStatus(_B)
_EtsysSyslogServerAddress_Type=InetAddress
_EtsysSyslogServerAddress_Object=MibTableColumn
etsysSyslogServerAddress=_EtsysSyslogServerAddress_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,4),_EtsysSyslogServerAddress_Type())
etsysSyslogServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerAddress.setStatus(_B)
_EtsysSyslogServerUdpPort_Type=SyslogUdpPort
_EtsysSyslogServerUdpPort_Object=MibTableColumn
etsysSyslogServerUdpPort=_EtsysSyslogServerUdpPort_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,5),_EtsysSyslogServerUdpPort_Type())
etsysSyslogServerUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerUdpPort.setStatus(_B)
_EtsysSyslogServerFacility_Type=SyslogFacility
_EtsysSyslogServerFacility_Object=MibTableColumn
etsysSyslogServerFacility=_EtsysSyslogServerFacility_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,6),_EtsysSyslogServerFacility_Type())
etsysSyslogServerFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerFacility.setStatus(_B)
_EtsysSyslogServerSeverity_Type=SyslogSeverity
_EtsysSyslogServerSeverity_Object=MibTableColumn
etsysSyslogServerSeverity=_EtsysSyslogServerSeverity_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,7),_EtsysSyslogServerSeverity_Type())
etsysSyslogServerSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerSeverity.setStatus(_B)
_EtsysSyslogServerMessagesIgnored_Type=Counter32
_EtsysSyslogServerMessagesIgnored_Object=MibTableColumn
etsysSyslogServerMessagesIgnored=_EtsysSyslogServerMessagesIgnored_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,8),_EtsysSyslogServerMessagesIgnored_Type())
etsysSyslogServerMessagesIgnored.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogServerMessagesIgnored.setStatus(_B)
_EtsysSyslogServerRowStatus_Type=RowStatus
_EtsysSyslogServerRowStatus_Object=MibTableColumn
etsysSyslogServerRowStatus=_EtsysSyslogServerRowStatus_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,9),_EtsysSyslogServerRowStatus_Type())
etsysSyslogServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerRowStatus.setStatus(_B)
class _EtsysSyslogServerVirtualRouterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysSyslogServerVirtualRouterName_Type.__name__=_a
_EtsysSyslogServerVirtualRouterName_Object=MibTableColumn
etsysSyslogServerVirtualRouterName=_EtsysSyslogServerVirtualRouterName_Object((1,3,6,1,4,1,5624,1,2,14,2,4,1,10),_EtsysSyslogServerVirtualRouterName_Type())
etsysSyslogServerVirtualRouterName.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysSyslogServerVirtualRouterName.setStatus(_B)
class _EtsysSyslogServerDefaultUdpPort_Type(SyslogUdpPort):defaultValue=514
_EtsysSyslogServerDefaultUdpPort_Type.__name__=_e
_EtsysSyslogServerDefaultUdpPort_Object=MibScalar
etsysSyslogServerDefaultUdpPort=_EtsysSyslogServerDefaultUdpPort_Object((1,3,6,1,4,1,5624,1,2,14,2,5),_EtsysSyslogServerDefaultUdpPort_Type())
etsysSyslogServerDefaultUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSyslogServerDefaultUdpPort.setStatus(_B)
class _EtsysSyslogServerDefaultFacility_Type(SyslogFacility):defaultValue=23
_EtsysSyslogServerDefaultFacility_Type.__name__=_f
_EtsysSyslogServerDefaultFacility_Object=MibScalar
etsysSyslogServerDefaultFacility=_EtsysSyslogServerDefaultFacility_Object((1,3,6,1,4,1,5624,1,2,14,2,6),_EtsysSyslogServerDefaultFacility_Type())
etsysSyslogServerDefaultFacility.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSyslogServerDefaultFacility.setStatus(_B)
class _EtsysSyslogServerDefaultSeverity_Type(SyslogSeverity):defaultValue=4
_EtsysSyslogServerDefaultSeverity_Type.__name__=_X
_EtsysSyslogServerDefaultSeverity_Object=MibScalar
etsysSyslogServerDefaultSeverity=_EtsysSyslogServerDefaultSeverity_Object((1,3,6,1,4,1,5624,1,2,14,2,7),_EtsysSyslogServerDefaultSeverity_Type())
etsysSyslogServerDefaultSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSyslogServerDefaultSeverity.setStatus(_B)
class _EtsysSyslogServerHostname_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('default',1),('ipv4',2),('ipv6',3),('sysName',4)))
_EtsysSyslogServerHostname_Type.__name__=_b
_EtsysSyslogServerHostname_Object=MibScalar
etsysSyslogServerHostname=_EtsysSyslogServerHostname_Object((1,3,6,1,4,1,5624,1,2,14,2,8),_EtsysSyslogServerHostname_Type())
etsysSyslogServerHostname.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSyslogServerHostname.setStatus(_B)
_EtsysSyslogApplication_ObjectIdentity=ObjectIdentity
etsysSyslogApplication=_EtsysSyslogApplication_ObjectIdentity((1,3,6,1,4,1,5624,1,2,14,3))
_EtsysSyslogApplicationTable_Object=MibTable
etsysSyslogApplicationTable=_EtsysSyslogApplicationTable_Object((1,3,6,1,4,1,5624,1,2,14,3,1))
if mibBuilder.loadTexts:etsysSyslogApplicationTable.setStatus(_B)
_EtsysSyslogApplicationEntry_Object=MibTableRow
etsysSyslogApplicationEntry=_EtsysSyslogApplicationEntry_Object((1,3,6,1,4,1,5624,1,2,14,3,1,1))
etsysSyslogApplicationEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:etsysSyslogApplicationEntry.setStatus(_B)
_EtsysSyslogApplicationIndex_Type=Unsigned32
_EtsysSyslogApplicationIndex_Object=MibTableColumn
etsysSyslogApplicationIndex=_EtsysSyslogApplicationIndex_Object((1,3,6,1,4,1,5624,1,2,14,3,1,1,1),_EtsysSyslogApplicationIndex_Type())
etsysSyslogApplicationIndex.setMaxAccess(_d)
if mibBuilder.loadTexts:etsysSyslogApplicationIndex.setStatus(_B)
class _EtsysSyslogApplicationDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_EtsysSyslogApplicationDescription_Type.__name__=_F
_EtsysSyslogApplicationDescription_Object=MibTableColumn
etsysSyslogApplicationDescription=_EtsysSyslogApplicationDescription_Object((1,3,6,1,4,1,5624,1,2,14,3,1,1,2),_EtsysSyslogApplicationDescription_Type())
etsysSyslogApplicationDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogApplicationDescription.setStatus(_B)
class _EtsysSyslogApplicationMnemonic_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_EtsysSyslogApplicationMnemonic_Type.__name__=_F
_EtsysSyslogApplicationMnemonic_Object=MibTableColumn
etsysSyslogApplicationMnemonic=_EtsysSyslogApplicationMnemonic_Object((1,3,6,1,4,1,5624,1,2,14,3,1,1,3),_EtsysSyslogApplicationMnemonic_Type())
etsysSyslogApplicationMnemonic.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysSyslogApplicationMnemonic.setStatus(_B)
class _EtsysSyslogApplicationSeverity_Type(SyslogSeverity):defaultValue=4
_EtsysSyslogApplicationSeverity_Type.__name__=_X
_EtsysSyslogApplicationSeverity_Object=MibTableColumn
etsysSyslogApplicationSeverity=_EtsysSyslogApplicationSeverity_Object((1,3,6,1,4,1,5624,1,2,14,3,1,1,4),_EtsysSyslogApplicationSeverity_Type())
etsysSyslogApplicationSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSyslogApplicationSeverity.setStatus(_B)
class _EtsysSyslogApplicationAllowedServers_Type(Bits):defaultBinValue='1111111111011111111';namedValues=NamedValues(*(('etsysSyslogServerIndex1',0),('etsysSyslogServerIndex2',1),('etsysSyslogServerIndex3',2),('etsysSyslogServerIndex4',3),('etsysSyslogServerIndex5',4),('etsysSyslogServerIndex6',5),('etsysSyslogServerIndex7',6),('etsysSyslogServerIndex8',7),('etsysSyslogServerConsole',8),('etsysSyslogServerFile',9),('etsysSyslogServerSecureFile',10),('etsysSyslogServerIndex9',11),('etsysSyslogServerIndex10',12),('etsysSyslogServerIndex11',13),('etsysSyslogServerIndex12',14),('etsysSyslogServerIndex13',15),('etsysSyslogServerIndex14',16),('etsysSyslogServerIndex15',17),('etsysSyslogServerIndex16',18)))
_EtsysSyslogApplicationAllowedServers_Type.__name__=_W
_EtsysSyslogApplicationAllowedServers_Object=MibTableColumn
etsysSyslogApplicationAllowedServers=_EtsysSyslogApplicationAllowedServers_Object((1,3,6,1,4,1,5624,1,2,14,3,1,1,5),_EtsysSyslogApplicationAllowedServers_Type())
etsysSyslogApplicationAllowedServers.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysSyslogApplicationAllowedServers.setStatus(_B)
_EtsysSyslogClientConformance_ObjectIdentity=ObjectIdentity
etsysSyslogClientConformance=_EtsysSyslogClientConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,14,4))
_EtsysSyslogClientGroups_ObjectIdentity=ObjectIdentity
etsysSyslogClientGroups=_EtsysSyslogClientGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,14,4,1))
_EtsysSyslogClientCompliances_ObjectIdentity=ObjectIdentity
etsysSyslogClientCompliances=_EtsysSyslogClientCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,14,4,2))
_EtsysSyslogNotification_ObjectIdentity=ObjectIdentity
etsysSyslogNotification=_EtsysSyslogNotification_ObjectIdentity((1,3,6,1,4,1,5624,1,2,14,5))
etsysSyslogClientGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,14,4,1,1))
etsysSyslogClientGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:etsysSyslogClientGroup.setStatus(_B)
etsysSyslogServerGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,14,4,1,2))
etsysSyslogServerGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsysSyslogServerGroup.setStatus(_S)
etsysSyslogApplicationGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,14,4,1,3))
etsysSyslogApplicationGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:etsysSyslogApplicationGroup.setStatus(_B)
etsysSyslogServerDefaultsGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,14,4,1,4))
etsysSyslogServerDefaultsGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:etsysSyslogServerDefaultsGroup.setStatus(_B)
etsysSyslogSecureGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,14,4,1,6))
etsysSyslogSecureGroup.setObjects((_A,_Y))
if mibBuilder.loadTexts:etsysSyslogSecureGroup.setStatus(_B)
etsysSyslogServerGroup2=ObjectGroup((1,3,6,1,4,1,5624,1,2,14,4,1,7))
etsysSyslogServerGroup2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_Z)))
if mibBuilder.loadTexts:etsysSyslogServerGroup2.setStatus(_S)
etsysSyslogServerGroup3=ObjectGroup((1,3,6,1,4,1,5624,1,2,14,4,1,8))
etsysSyslogServerGroup3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_s),(_A,_Z)))
if mibBuilder.loadTexts:etsysSyslogServerGroup3.setStatus(_B)
etsysSyslogSecureLogArchiveNotification=NotificationType((1,3,6,1,4,1,5624,1,2,14,5,1))
if mibBuilder.loadTexts:etsysSyslogSecureLogArchiveNotification.setStatus(_B)
etsysSyslogSecureLogDroppedMsgNotification=NotificationType((1,3,6,1,4,1,5624,1,2,14,5,2))
etsysSyslogSecureLogDroppedMsgNotification.setObjects((_A,_Y))
if mibBuilder.loadTexts:etsysSyslogSecureLogDroppedMsgNotification.setStatus(_B)
etsysSyslogNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,14,4,1,5))
etsysSyslogNotificationGroup.setObjects(*((_A,_t),(_A,_u)))
if mibBuilder.loadTexts:etsysSyslogNotificationGroup.setStatus(_B)
etsysSyslogClientCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,14,4,2,1))
etsysSyslogClientCompliance.setObjects(*((_A,_T),(_A,_v),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:etsysSyslogClientCompliance.setStatus(_S)
etsysSyslogNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,14,4,2,2))
etsysSyslogNotificationCompliance.setObjects((_A,_w))
if mibBuilder.loadTexts:etsysSyslogNotificationCompliance.setStatus(_B)
etsysSyslogSecureCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,14,4,2,3))
etsysSyslogSecureCompliance.setObjects((_A,_x))
if mibBuilder.loadTexts:etsysSyslogSecureCompliance.setStatus(_B)
etsysSyslogClientCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,14,4,2,4))
etsysSyslogClientCompliance2.setObjects(*((_A,_T),(_A,_y),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:etsysSyslogClientCompliance2.setStatus(_S)
etsysSyslogClientCompliance3=ModuleCompliance((1,3,6,1,4,1,5624,1,2,14,4,2,5))
etsysSyslogClientCompliance3.setObjects(*((_A,_T),(_A,_z),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:etsysSyslogClientCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_e:SyslogUdpPort,_f:SyslogFacility,_X:SyslogSeverity,'etsysSyslogClientMIB':etsysSyslogClientMIB,'etsysSyslogClient':etsysSyslogClient,_h:etsysSyslogClientMessages,_i:etsysSyslogClientMessagesDropped,_j:etsysSyslogClientLastMessageTime,_k:etsysSyslogClientControl,_Y:etsysSyslogClientSecureMessagesDropped,'etsysSyslogServer':etsysSyslogServer,_H:etsysSyslogServerMaxEntries,_I:etsysSyslogServerNumEntries,_J:etsysSyslogServerTableNextAvailableIndex,'etsysSyslogServerTable':etsysSyslogServerTable,'etsysSyslogServerEntry':etsysSyslogServerEntry,_c:etsysSyslogServerIndex,_K:etsysSyslogServerDescription,_L:etsysSyslogServerAddressType,_M:etsysSyslogServerAddress,_N:etsysSyslogServerUdpPort,_O:etsysSyslogServerFacility,_P:etsysSyslogServerSeverity,_Q:etsysSyslogServerMessagesIgnored,_R:etsysSyslogServerRowStatus,_s:etsysSyslogServerVirtualRouterName,_p:etsysSyslogServerDefaultUdpPort,_q:etsysSyslogServerDefaultFacility,_r:etsysSyslogServerDefaultSeverity,_Z:etsysSyslogServerHostname,'etsysSyslogApplication':etsysSyslogApplication,'etsysSyslogApplicationTable':etsysSyslogApplicationTable,'etsysSyslogApplicationEntry':etsysSyslogApplicationEntry,_g:etsysSyslogApplicationIndex,_l:etsysSyslogApplicationDescription,_m:etsysSyslogApplicationMnemonic,_n:etsysSyslogApplicationSeverity,_o:etsysSyslogApplicationAllowedServers,'etsysSyslogClientConformance':etsysSyslogClientConformance,'etsysSyslogClientGroups':etsysSyslogClientGroups,_T:etsysSyslogClientGroup,_v:etsysSyslogServerGroup,_V:etsysSyslogApplicationGroup,_U:etsysSyslogServerDefaultsGroup,_w:etsysSyslogNotificationGroup,_x:etsysSyslogSecureGroup,_y:etsysSyslogServerGroup2,_z:etsysSyslogServerGroup3,'etsysSyslogClientCompliances':etsysSyslogClientCompliances,'etsysSyslogClientCompliance':etsysSyslogClientCompliance,'etsysSyslogNotificationCompliance':etsysSyslogNotificationCompliance,'etsysSyslogSecureCompliance':etsysSyslogSecureCompliance,'etsysSyslogClientCompliance2':etsysSyslogClientCompliance2,'etsysSyslogClientCompliance3':etsysSyslogClientCompliance3,'etsysSyslogNotification':etsysSyslogNotification,_t:etsysSyslogSecureLogArchiveNotification,_u:etsysSyslogSecureLogDroppedMsgNotification})