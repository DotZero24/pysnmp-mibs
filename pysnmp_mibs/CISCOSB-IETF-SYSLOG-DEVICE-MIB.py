_l='snmpSyslogApplicationGroup'
_k='snmpSyslogCollectorDefaultsGroup'
_j='snmpSyslogCollectorGroup'
_i='snmpSyslogDeviceGroup'
_h='snmpSyslogCollectorDefaultSeverity'
_g='snmpSyslogCollectorDefaultFacility'
_f='snmpSyslogCollectorDefaultUdpPort'
_e='snmpSyslogApplicationSeverity'
_d='snmpSyslogApplicationMnemonic'
_c='snmpSyslogApplicationDescription'
_b='snmpSyslogCollectorRowStatus'
_a='snmpSyslogCollectorMessagesIgnored'
_Z='snmpSyslogCollectorSeverity'
_Y='snmpSyslogCollectorFacility'
_X='snmpSyslogCollectorUdpPort'
_W='snmpSyslogCollectorAddress'
_V='snmpSyslogCollectorAddressType'
_U='snmpSyslogCollectorDescription'
_T='snmpSyslogCollectorTableNextAvailableIndex'
_S='snmpSyslogCollectorNumEntries'
_R='snmpSyslogCollectorMaxEntries'
_Q='snmpSyslogDeviceControl'
_P='snmpSyslogDeviceLastMessageTime'
_O='snmpSyslogDeviceMessagesDropped'
_N='snmpSyslogDeviceMessages'
_M='snmpSyslogApplicationIndex'
_L='SyslogFacility'
_K='SyslogUdpPort'
_J='not-accessible'
_I='snmpSyslogCollectorIndex'
_H='SyslogSeverity'
_G='Unsigned32'
_F='SnmpAdminString'
_E='read-write'
_D='read-create'
_C='read-only'
_B='CISCOSB-IETF-SYSLOG-DEVICE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rlSyslog,=mibBuilder.importSymbols('CISCOSB-MIB','rlSyslog')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','snmpModules')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
snmpSyslogDeviceMIB=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,82,1))
if mibBuilder.loadTexts:snmpSyslogDeviceMIB.setRevisions(('2002-06-06 18:41',))
class SyslogUdpPort(TextualConvention,Unsigned32):status=_A
class SyslogFacility(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('local0',16),('local1',17),('local2',18),('local3',19),('local4',20),('local5',21),('local6',22),('local7',23),('no-map',24)))
class SyslogSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',0),('alert',1),('critical',2),('error',3),('warning',4),('notice',5),('info',6),('debug',7)))
_SnmpSyslogDevice_ObjectIdentity=ObjectIdentity
snmpSyslogDevice=_SnmpSyslogDevice_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,82,1,1))
_SnmpSyslogDeviceMessages_Type=Counter32
_SnmpSyslogDeviceMessages_Object=MibScalar
snmpSyslogDeviceMessages=_SnmpSyslogDeviceMessages_Object((1,3,6,1,4,1,9,6,1,101,82,1,1,1),_SnmpSyslogDeviceMessages_Type())
snmpSyslogDeviceMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogDeviceMessages.setStatus(_A)
_SnmpSyslogDeviceMessagesDropped_Type=Counter32
_SnmpSyslogDeviceMessagesDropped_Object=MibScalar
snmpSyslogDeviceMessagesDropped=_SnmpSyslogDeviceMessagesDropped_Object((1,3,6,1,4,1,9,6,1,101,82,1,1,2),_SnmpSyslogDeviceMessagesDropped_Type())
snmpSyslogDeviceMessagesDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogDeviceMessagesDropped.setStatus(_A)
_SnmpSyslogDeviceLastMessageTime_Type=TimeStamp
_SnmpSyslogDeviceLastMessageTime_Object=MibScalar
snmpSyslogDeviceLastMessageTime=_SnmpSyslogDeviceLastMessageTime_Object((1,3,6,1,4,1,9,6,1,101,82,1,1,3),_SnmpSyslogDeviceLastMessageTime_Type())
snmpSyslogDeviceLastMessageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogDeviceLastMessageTime.setStatus(_A)
class _SnmpSyslogDeviceControl_Type(Bits):namedValues=NamedValues(('snmpSyslogDeviceControlConsoleLogging',0))
_SnmpSyslogDeviceControl_Type.__name__='Bits'
_SnmpSyslogDeviceControl_Object=MibScalar
snmpSyslogDeviceControl=_SnmpSyslogDeviceControl_Object((1,3,6,1,4,1,9,6,1,101,82,1,1,4),_SnmpSyslogDeviceControl_Type())
snmpSyslogDeviceControl.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpSyslogDeviceControl.setStatus(_A)
_SnmpSyslogCollector_ObjectIdentity=ObjectIdentity
snmpSyslogCollector=_SnmpSyslogCollector_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,82,1,2))
class _SnmpSyslogCollectorMaxEntries_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SnmpSyslogCollectorMaxEntries_Type.__name__=_G
_SnmpSyslogCollectorMaxEntries_Object=MibScalar
snmpSyslogCollectorMaxEntries=_SnmpSyslogCollectorMaxEntries_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,1),_SnmpSyslogCollectorMaxEntries_Type())
snmpSyslogCollectorMaxEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogCollectorMaxEntries.setStatus(_A)
_SnmpSyslogCollectorNumEntries_Type=Gauge32
_SnmpSyslogCollectorNumEntries_Object=MibScalar
snmpSyslogCollectorNumEntries=_SnmpSyslogCollectorNumEntries_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,2),_SnmpSyslogCollectorNumEntries_Type())
snmpSyslogCollectorNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogCollectorNumEntries.setStatus(_A)
class _SnmpSyslogCollectorTableNextAvailableIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_SnmpSyslogCollectorTableNextAvailableIndex_Type.__name__=_G
_SnmpSyslogCollectorTableNextAvailableIndex_Object=MibScalar
snmpSyslogCollectorTableNextAvailableIndex=_SnmpSyslogCollectorTableNextAvailableIndex_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,3),_SnmpSyslogCollectorTableNextAvailableIndex_Type())
snmpSyslogCollectorTableNextAvailableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogCollectorTableNextAvailableIndex.setStatus(_A)
_SnmpSyslogCollectorTable_Object=MibTable
snmpSyslogCollectorTable=_SnmpSyslogCollectorTable_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4))
if mibBuilder.loadTexts:snmpSyslogCollectorTable.setStatus(_A)
_SnmpSyslogCollectorEntry_Object=MibTableRow
snmpSyslogCollectorEntry=_SnmpSyslogCollectorEntry_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1))
snmpSyslogCollectorEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:snmpSyslogCollectorEntry.setStatus(_A)
class _SnmpSyslogCollectorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SnmpSyslogCollectorIndex_Type.__name__=_G
_SnmpSyslogCollectorIndex_Object=MibTableColumn
snmpSyslogCollectorIndex=_SnmpSyslogCollectorIndex_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,1),_SnmpSyslogCollectorIndex_Type())
snmpSyslogCollectorIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:snmpSyslogCollectorIndex.setStatus(_A)
class _SnmpSyslogCollectorDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SnmpSyslogCollectorDescription_Type.__name__=_F
_SnmpSyslogCollectorDescription_Object=MibTableColumn
snmpSyslogCollectorDescription=_SnmpSyslogCollectorDescription_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,2),_SnmpSyslogCollectorDescription_Type())
snmpSyslogCollectorDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpSyslogCollectorDescription.setStatus(_A)
_SnmpSyslogCollectorAddressType_Type=InetAddressType
_SnmpSyslogCollectorAddressType_Object=MibTableColumn
snmpSyslogCollectorAddressType=_SnmpSyslogCollectorAddressType_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,3),_SnmpSyslogCollectorAddressType_Type())
snmpSyslogCollectorAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpSyslogCollectorAddressType.setStatus(_A)
_SnmpSyslogCollectorAddress_Type=InetAddress
_SnmpSyslogCollectorAddress_Object=MibTableColumn
snmpSyslogCollectorAddress=_SnmpSyslogCollectorAddress_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,4),_SnmpSyslogCollectorAddress_Type())
snmpSyslogCollectorAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpSyslogCollectorAddress.setStatus(_A)
_SnmpSyslogCollectorUdpPort_Type=SyslogUdpPort
_SnmpSyslogCollectorUdpPort_Object=MibTableColumn
snmpSyslogCollectorUdpPort=_SnmpSyslogCollectorUdpPort_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,5),_SnmpSyslogCollectorUdpPort_Type())
snmpSyslogCollectorUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpSyslogCollectorUdpPort.setStatus(_A)
_SnmpSyslogCollectorFacility_Type=SyslogFacility
_SnmpSyslogCollectorFacility_Object=MibTableColumn
snmpSyslogCollectorFacility=_SnmpSyslogCollectorFacility_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,6),_SnmpSyslogCollectorFacility_Type())
snmpSyslogCollectorFacility.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpSyslogCollectorFacility.setStatus(_A)
_SnmpSyslogCollectorSeverity_Type=SyslogSeverity
_SnmpSyslogCollectorSeverity_Object=MibTableColumn
snmpSyslogCollectorSeverity=_SnmpSyslogCollectorSeverity_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,7),_SnmpSyslogCollectorSeverity_Type())
snmpSyslogCollectorSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpSyslogCollectorSeverity.setStatus(_A)
_SnmpSyslogCollectorMessagesIgnored_Type=Counter32
_SnmpSyslogCollectorMessagesIgnored_Object=MibTableColumn
snmpSyslogCollectorMessagesIgnored=_SnmpSyslogCollectorMessagesIgnored_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,8),_SnmpSyslogCollectorMessagesIgnored_Type())
snmpSyslogCollectorMessagesIgnored.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogCollectorMessagesIgnored.setStatus(_A)
_SnmpSyslogCollectorRowStatus_Type=RowStatus
_SnmpSyslogCollectorRowStatus_Object=MibTableColumn
snmpSyslogCollectorRowStatus=_SnmpSyslogCollectorRowStatus_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,4,1,9),_SnmpSyslogCollectorRowStatus_Type())
snmpSyslogCollectorRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpSyslogCollectorRowStatus.setStatus(_A)
class _SnmpSyslogCollectorDefaultUdpPort_Type(SyslogUdpPort):defaultValue=514
_SnmpSyslogCollectorDefaultUdpPort_Type.__name__=_K
_SnmpSyslogCollectorDefaultUdpPort_Object=MibScalar
snmpSyslogCollectorDefaultUdpPort=_SnmpSyslogCollectorDefaultUdpPort_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,5),_SnmpSyslogCollectorDefaultUdpPort_Type())
snmpSyslogCollectorDefaultUdpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpSyslogCollectorDefaultUdpPort.setStatus(_A)
class _SnmpSyslogCollectorDefaultFacility_Type(SyslogFacility):defaultValue=23
_SnmpSyslogCollectorDefaultFacility_Type.__name__=_L
_SnmpSyslogCollectorDefaultFacility_Object=MibScalar
snmpSyslogCollectorDefaultFacility=_SnmpSyslogCollectorDefaultFacility_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,6),_SnmpSyslogCollectorDefaultFacility_Type())
snmpSyslogCollectorDefaultFacility.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpSyslogCollectorDefaultFacility.setStatus(_A)
class _SnmpSyslogCollectorDefaultSeverity_Type(SyslogSeverity):defaultValue=3
_SnmpSyslogCollectorDefaultSeverity_Type.__name__=_H
_SnmpSyslogCollectorDefaultSeverity_Object=MibScalar
snmpSyslogCollectorDefaultSeverity=_SnmpSyslogCollectorDefaultSeverity_Object((1,3,6,1,4,1,9,6,1,101,82,1,2,7),_SnmpSyslogCollectorDefaultSeverity_Type())
snmpSyslogCollectorDefaultSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpSyslogCollectorDefaultSeverity.setStatus(_A)
_SnmpSyslogApplication_ObjectIdentity=ObjectIdentity
snmpSyslogApplication=_SnmpSyslogApplication_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,82,1,3))
_SnmpSyslogApplicationTable_Object=MibTable
snmpSyslogApplicationTable=_SnmpSyslogApplicationTable_Object((1,3,6,1,4,1,9,6,1,101,82,1,3,1))
if mibBuilder.loadTexts:snmpSyslogApplicationTable.setStatus(_A)
_SnmpSyslogApplicationEntry_Object=MibTableRow
snmpSyslogApplicationEntry=_SnmpSyslogApplicationEntry_Object((1,3,6,1,4,1,9,6,1,101,82,1,3,1,1))
snmpSyslogApplicationEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:snmpSyslogApplicationEntry.setStatus(_A)
_SnmpSyslogApplicationIndex_Type=Unsigned32
_SnmpSyslogApplicationIndex_Object=MibTableColumn
snmpSyslogApplicationIndex=_SnmpSyslogApplicationIndex_Object((1,3,6,1,4,1,9,6,1,101,82,1,3,1,1,1),_SnmpSyslogApplicationIndex_Type())
snmpSyslogApplicationIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:snmpSyslogApplicationIndex.setStatus(_A)
class _SnmpSyslogApplicationDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_SnmpSyslogApplicationDescription_Type.__name__=_F
_SnmpSyslogApplicationDescription_Object=MibTableColumn
snmpSyslogApplicationDescription=_SnmpSyslogApplicationDescription_Object((1,3,6,1,4,1,9,6,1,101,82,1,3,1,1,2),_SnmpSyslogApplicationDescription_Type())
snmpSyslogApplicationDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogApplicationDescription.setStatus(_A)
class _SnmpSyslogApplicationMnemonic_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SnmpSyslogApplicationMnemonic_Type.__name__=_F
_SnmpSyslogApplicationMnemonic_Object=MibTableColumn
snmpSyslogApplicationMnemonic=_SnmpSyslogApplicationMnemonic_Object((1,3,6,1,4,1,9,6,1,101,82,1,3,1,1,3),_SnmpSyslogApplicationMnemonic_Type())
snmpSyslogApplicationMnemonic.setMaxAccess(_C)
if mibBuilder.loadTexts:snmpSyslogApplicationMnemonic.setStatus(_A)
class _SnmpSyslogApplicationSeverity_Type(SyslogSeverity):defaultValue=3
_SnmpSyslogApplicationSeverity_Type.__name__=_H
_SnmpSyslogApplicationSeverity_Object=MibTableColumn
snmpSyslogApplicationSeverity=_SnmpSyslogApplicationSeverity_Object((1,3,6,1,4,1,9,6,1,101,82,1,3,1,1,4),_SnmpSyslogApplicationSeverity_Type())
snmpSyslogApplicationSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpSyslogApplicationSeverity.setStatus(_A)
_SnmpSyslogDeviceConformance_ObjectIdentity=ObjectIdentity
snmpSyslogDeviceConformance=_SnmpSyslogDeviceConformance_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,82,1,4))
_SnmpSyslogDeviceGroups_ObjectIdentity=ObjectIdentity
snmpSyslogDeviceGroups=_SnmpSyslogDeviceGroups_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,82,1,4,1))
_SnmpSyslogDeviceCompliances_ObjectIdentity=ObjectIdentity
snmpSyslogDeviceCompliances=_SnmpSyslogDeviceCompliances_ObjectIdentity((1,3,6,1,4,1,9,6,1,101,82,1,4,2))
snmpSyslogDeviceGroup=ObjectGroup((1,3,6,1,4,1,9,6,1,101,82,1,4,1,1))
snmpSyslogDeviceGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:snmpSyslogDeviceGroup.setStatus(_A)
snmpSyslogCollectorGroup=ObjectGroup((1,3,6,1,4,1,9,6,1,101,82,1,4,1,2))
snmpSyslogCollectorGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:snmpSyslogCollectorGroup.setStatus(_A)
snmpSyslogApplicationGroup=ObjectGroup((1,3,6,1,4,1,9,6,1,101,82,1,4,1,3))
snmpSyslogApplicationGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:snmpSyslogApplicationGroup.setStatus(_A)
snmpSyslogCollectorDefaultsGroup=ObjectGroup((1,3,6,1,4,1,9,6,1,101,82,1,4,1,4))
snmpSyslogCollectorDefaultsGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:snmpSyslogCollectorDefaultsGroup.setStatus(_A)
snmpSyslogDeviceCompliance=ModuleCompliance((1,3,6,1,4,1,9,6,1,101,82,1,4,2,1))
snmpSyslogDeviceCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:snmpSyslogDeviceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_K:SyslogUdpPort,_L:SyslogFacility,_H:SyslogSeverity,'snmpSyslogDeviceMIB':snmpSyslogDeviceMIB,'snmpSyslogDevice':snmpSyslogDevice,_N:snmpSyslogDeviceMessages,_O:snmpSyslogDeviceMessagesDropped,_P:snmpSyslogDeviceLastMessageTime,_Q:snmpSyslogDeviceControl,'snmpSyslogCollector':snmpSyslogCollector,_R:snmpSyslogCollectorMaxEntries,_S:snmpSyslogCollectorNumEntries,_T:snmpSyslogCollectorTableNextAvailableIndex,'snmpSyslogCollectorTable':snmpSyslogCollectorTable,'snmpSyslogCollectorEntry':snmpSyslogCollectorEntry,_I:snmpSyslogCollectorIndex,_U:snmpSyslogCollectorDescription,_V:snmpSyslogCollectorAddressType,_W:snmpSyslogCollectorAddress,_X:snmpSyslogCollectorUdpPort,_Y:snmpSyslogCollectorFacility,_Z:snmpSyslogCollectorSeverity,_a:snmpSyslogCollectorMessagesIgnored,_b:snmpSyslogCollectorRowStatus,_f:snmpSyslogCollectorDefaultUdpPort,_g:snmpSyslogCollectorDefaultFacility,_h:snmpSyslogCollectorDefaultSeverity,'snmpSyslogApplication':snmpSyslogApplication,'snmpSyslogApplicationTable':snmpSyslogApplicationTable,'snmpSyslogApplicationEntry':snmpSyslogApplicationEntry,_M:snmpSyslogApplicationIndex,_c:snmpSyslogApplicationDescription,_d:snmpSyslogApplicationMnemonic,_e:snmpSyslogApplicationSeverity,'snmpSyslogDeviceConformance':snmpSyslogDeviceConformance,'snmpSyslogDeviceGroups':snmpSyslogDeviceGroups,_i:snmpSyslogDeviceGroup,_j:snmpSyslogCollectorGroup,_l:snmpSyslogApplicationGroup,_k:snmpSyslogCollectorDefaultsGroup,'snmpSyslogDeviceCompliances':snmpSyslogDeviceCompliances,'snmpSyslogDeviceCompliance':snmpSyslogDeviceCompliance})