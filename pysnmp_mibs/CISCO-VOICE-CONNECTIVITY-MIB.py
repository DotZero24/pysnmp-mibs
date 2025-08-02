_j='cvcNotificationsGroup'
_i='cvcNotifGroup'
_h='cvcCallAgentConnectionGroup'
_g='cvcPortGroup'
_f='cvcCallAgentGroup'
_e='cvcPortRegistrationStatusChange'
_d='cvcNotifEnable'
_c='cvcVirtualInterfaceDN'
_b='cvcProtocol'
_a='cvcProductCategory'
_Z='cvcPortType'
_Y='cvcPortMACAddress'
_X='cvcPortInetAddress'
_W='cvcPortInetAddressType'
_V='cvcPortAssociation'
_U='cvcCallAgentType'
_T='cvcCallAgentInetAddressType'
_S='cvcCallAgentName'
_R='unknown'
_Q='not-accessible'
_P='TruthValue'
_O='SnmpAdminString'
_N='cvcLastRegisteredTime'
_M='cvcLastStatusChangeTime'
_L='cvcStatusReason'
_K='cvcRegistrationStatus'
_J='cvcCallAgentPriority'
_I='cvcPortDeviceName'
_H='cvcCallAgentInetAddress'
_G='cvcPortIndex'
_F='cvcCallAgentIndex'
_E='Unsigned32'
_D='Integer32'
_C='read-only'
_B='current'
_A='CISCO-VOICE-CONNECTIVITY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
IANAifType,=mibBuilder.importSymbols('IANAifType-MIB','IANAifType')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
AutonomousType,DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention',_P)
ciscoVoiceConnectivityMIB=ModuleIdentity((1,3,6,1,4,1,9,9,393))
if mibBuilder.loadTexts:ciscoVoiceConnectivityMIB.setRevisions(('2005-09-13 00:00',))
_CiscoVoiceConnectivityMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVoiceConnectivityMIBNotifs=_CiscoVoiceConnectivityMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,393,0))
_CiscoVoiceConnectivityMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVoiceConnectivityMIBObjects=_CiscoVoiceConnectivityMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,393,1))
_CvcCallAgent_ObjectIdentity=ObjectIdentity
cvcCallAgent=_CvcCallAgent_ObjectIdentity((1,3,6,1,4,1,9,9,393,1,1))
_CvcCallAgentTable_Object=MibTable
cvcCallAgentTable=_CvcCallAgentTable_Object((1,3,6,1,4,1,9,9,393,1,1,1))
if mibBuilder.loadTexts:cvcCallAgentTable.setStatus(_B)
_CvcCallAgentEntry_Object=MibTableRow
cvcCallAgentEntry=_CvcCallAgentEntry_Object((1,3,6,1,4,1,9,9,393,1,1,1,1))
cvcCallAgentEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:cvcCallAgentEntry.setStatus(_B)
class _CvcCallAgentIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CvcCallAgentIndex_Type.__name__=_E
_CvcCallAgentIndex_Object=MibTableColumn
cvcCallAgentIndex=_CvcCallAgentIndex_Object((1,3,6,1,4,1,9,9,393,1,1,1,1,1),_CvcCallAgentIndex_Type())
cvcCallAgentIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:cvcCallAgentIndex.setStatus(_B)
class _CvcCallAgentName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CvcCallAgentName_Type.__name__=_O
_CvcCallAgentName_Object=MibTableColumn
cvcCallAgentName=_CvcCallAgentName_Object((1,3,6,1,4,1,9,9,393,1,1,1,1,2),_CvcCallAgentName_Type())
cvcCallAgentName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcCallAgentName.setStatus(_B)
_CvcCallAgentInetAddressType_Type=InetAddressType
_CvcCallAgentInetAddressType_Object=MibTableColumn
cvcCallAgentInetAddressType=_CvcCallAgentInetAddressType_Object((1,3,6,1,4,1,9,9,393,1,1,1,1,3),_CvcCallAgentInetAddressType_Type())
cvcCallAgentInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcCallAgentInetAddressType.setStatus(_B)
_CvcCallAgentInetAddress_Type=InetAddress
_CvcCallAgentInetAddress_Object=MibTableColumn
cvcCallAgentInetAddress=_CvcCallAgentInetAddress_Object((1,3,6,1,4,1,9,9,393,1,1,1,1,4),_CvcCallAgentInetAddress_Type())
cvcCallAgentInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcCallAgentInetAddress.setStatus(_B)
_CvcCallAgentType_Type=AutonomousType
_CvcCallAgentType_Object=MibTableColumn
cvcCallAgentType=_CvcCallAgentType_Object((1,3,6,1,4,1,9,9,393,1,1,1,1,5),_CvcCallAgentType_Type())
cvcCallAgentType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcCallAgentType.setStatus(_B)
_CvcPort_ObjectIdentity=ObjectIdentity
cvcPort=_CvcPort_ObjectIdentity((1,3,6,1,4,1,9,9,393,1,2))
_CvcPortTable_Object=MibTable
cvcPortTable=_CvcPortTable_Object((1,3,6,1,4,1,9,9,393,1,2,1))
if mibBuilder.loadTexts:cvcPortTable.setStatus(_B)
_CvcPortEntry_Object=MibTableRow
cvcPortEntry=_CvcPortEntry_Object((1,3,6,1,4,1,9,9,393,1,2,1,1))
cvcPortEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:cvcPortEntry.setStatus(_B)
class _CvcPortIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CvcPortIndex_Type.__name__=_E
_CvcPortIndex_Object=MibTableColumn
cvcPortIndex=_CvcPortIndex_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,1),_CvcPortIndex_Type())
cvcPortIndex.setMaxAccess(_Q)
if mibBuilder.loadTexts:cvcPortIndex.setStatus(_B)
_CvcPortAssociation_Type=RowPointer
_CvcPortAssociation_Object=MibTableColumn
cvcPortAssociation=_CvcPortAssociation_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,2),_CvcPortAssociation_Type())
cvcPortAssociation.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcPortAssociation.setStatus(_B)
_CvcPortDeviceName_Type=SnmpAdminString
_CvcPortDeviceName_Object=MibTableColumn
cvcPortDeviceName=_CvcPortDeviceName_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,3),_CvcPortDeviceName_Type())
cvcPortDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcPortDeviceName.setStatus(_B)
_CvcPortInetAddressType_Type=InetAddressType
_CvcPortInetAddressType_Object=MibTableColumn
cvcPortInetAddressType=_CvcPortInetAddressType_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,4),_CvcPortInetAddressType_Type())
cvcPortInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcPortInetAddressType.setStatus(_B)
_CvcPortInetAddress_Type=InetAddress
_CvcPortInetAddress_Object=MibTableColumn
cvcPortInetAddress=_CvcPortInetAddress_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,5),_CvcPortInetAddress_Type())
cvcPortInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcPortInetAddress.setStatus(_B)
_CvcPortMACAddress_Type=MacAddress
_CvcPortMACAddress_Object=MibTableColumn
cvcPortMACAddress=_CvcPortMACAddress_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,6),_CvcPortMACAddress_Type())
cvcPortMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcPortMACAddress.setStatus(_B)
_CvcPortType_Type=IANAifType
_CvcPortType_Object=MibTableColumn
cvcPortType=_CvcPortType_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,7),_CvcPortType_Type())
cvcPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcPortType.setStatus(_B)
class _CvcProductCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('phone',1),('gateway',2),('h323Device',3),('ctiDevice',4),('voiceMailDevice',5),('mediaResourceDevice',6),('huntListDevice',7),('sipDevice',8)))
_CvcProductCategory_Type.__name__=_D
_CvcProductCategory_Object=MibTableColumn
cvcProductCategory=_CvcProductCategory_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,8),_CvcProductCategory_Type())
cvcProductCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcProductCategory.setStatus(_B)
class _CvcProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('sccp',1),('sgcp',2),('mgcp',3),('h323',4),('sip',5)))
_CvcProtocol_Type.__name__=_D
_CvcProtocol_Object=MibTableColumn
cvcProtocol=_CvcProtocol_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,9),_CvcProtocol_Type())
cvcProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcProtocol.setStatus(_B)
_CvcVirtualInterfaceDN_Type=SnmpAdminString
_CvcVirtualInterfaceDN_Object=MibTableColumn
cvcVirtualInterfaceDN=_CvcVirtualInterfaceDN_Object((1,3,6,1,4,1,9,9,393,1,2,1,1,10),_CvcVirtualInterfaceDN_Type())
cvcVirtualInterfaceDN.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcVirtualInterfaceDN.setStatus(_B)
_CvcCallAgentConnection_ObjectIdentity=ObjectIdentity
cvcCallAgentConnection=_CvcCallAgentConnection_ObjectIdentity((1,3,6,1,4,1,9,9,393,1,3))
_CvcCallAgentConnectionTable_Object=MibTable
cvcCallAgentConnectionTable=_CvcCallAgentConnectionTable_Object((1,3,6,1,4,1,9,9,393,1,3,1))
if mibBuilder.loadTexts:cvcCallAgentConnectionTable.setStatus(_B)
_CvcCallAgentConnectionEntry_Object=MibTableRow
cvcCallAgentConnectionEntry=_CvcCallAgentConnectionEntry_Object((1,3,6,1,4,1,9,9,393,1,3,1,1))
cvcCallAgentConnectionEntry.setIndexNames((0,_A,_G),(0,_A,_F))
if mibBuilder.loadTexts:cvcCallAgentConnectionEntry.setStatus(_B)
_CvcCallAgentPriority_Type=Unsigned32
_CvcCallAgentPriority_Object=MibTableColumn
cvcCallAgentPriority=_CvcCallAgentPriority_Object((1,3,6,1,4,1,9,9,393,1,3,1,1,1),_CvcCallAgentPriority_Type())
cvcCallAgentPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcCallAgentPriority.setStatus(_B)
class _CvcRegistrationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_R,1),('notapplicable',2),('registered',3),('unregistered',4),('rejected',5)))
_CvcRegistrationStatus_Type.__name__=_D
_CvcRegistrationStatus_Object=MibTableColumn
cvcRegistrationStatus=_CvcRegistrationStatus_Object((1,3,6,1,4,1,9,9,393,1,3,1,1,2),_CvcRegistrationStatus_Type())
cvcRegistrationStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcRegistrationStatus.setStatus(_B)
class _CvcStatusReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noError',1),(_R,2),('configurationError',3),('deviceNameUnresolveable',4),('maxDevRegReached',5),('connectivityError',6),('initializationError',7),('deviceReset',8)))
_CvcStatusReason_Type.__name__=_D
_CvcStatusReason_Object=MibTableColumn
cvcStatusReason=_CvcStatusReason_Object((1,3,6,1,4,1,9,9,393,1,3,1,1,3),_CvcStatusReason_Type())
cvcStatusReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcStatusReason.setStatus(_B)
_CvcLastStatusChangeTime_Type=DateAndTime
_CvcLastStatusChangeTime_Object=MibTableColumn
cvcLastStatusChangeTime=_CvcLastStatusChangeTime_Object((1,3,6,1,4,1,9,9,393,1,3,1,1,4),_CvcLastStatusChangeTime_Type())
cvcLastStatusChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcLastStatusChangeTime.setStatus(_B)
_CvcLastRegisteredTime_Type=DateAndTime
_CvcLastRegisteredTime_Object=MibTableColumn
cvcLastRegisteredTime=_CvcLastRegisteredTime_Object((1,3,6,1,4,1,9,9,393,1,3,1,1,5),_CvcLastRegisteredTime_Type())
cvcLastRegisteredTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvcLastRegisteredTime.setStatus(_B)
_CvcNotif_ObjectIdentity=ObjectIdentity
cvcNotif=_CvcNotif_ObjectIdentity((1,3,6,1,4,1,9,9,393,1,4))
class _CvcNotifEnable_Type(TruthValue):defaultValue=2
_CvcNotifEnable_Type.__name__=_P
_CvcNotifEnable_Object=MibScalar
cvcNotifEnable=_CvcNotifEnable_Object((1,3,6,1,4,1,9,9,393,1,4,1),_CvcNotifEnable_Type())
cvcNotifEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cvcNotifEnable.setStatus(_B)
_CiscoVoiceConnectivityMIBConform_ObjectIdentity=ObjectIdentity
ciscoVoiceConnectivityMIBConform=_CiscoVoiceConnectivityMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,393,2))
_CvcMIBCompliances_ObjectIdentity=ObjectIdentity
cvcMIBCompliances=_CvcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,393,2,1))
_CvcMIBGroups_ObjectIdentity=ObjectIdentity
cvcMIBGroups=_CvcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,393,2,2))
cvcCallAgentGroup=ObjectGroup((1,3,6,1,4,1,9,9,393,2,2,1))
cvcCallAgentGroup.setObjects(*((_A,_S),(_A,_T),(_A,_H),(_A,_U)))
if mibBuilder.loadTexts:cvcCallAgentGroup.setStatus(_B)
cvcPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,393,2,2,2))
cvcPortGroup.setObjects(*((_A,_V),(_A,_I),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c)))
if mibBuilder.loadTexts:cvcPortGroup.setStatus(_B)
cvcCallAgentConnectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,393,2,2,3))
cvcCallAgentConnectionGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cvcCallAgentConnectionGroup.setStatus(_B)
cvcNotifGroup=ObjectGroup((1,3,6,1,4,1,9,9,393,2,2,4))
cvcNotifGroup.setObjects((_A,_d))
if mibBuilder.loadTexts:cvcNotifGroup.setStatus(_B)
cvcPortRegistrationStatusChange=NotificationType((1,3,6,1,4,1,9,9,393,0,1))
cvcPortRegistrationStatusChange.setObjects(*((_A,_I),(_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:cvcPortRegistrationStatusChange.setStatus(_B)
cvcNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,393,2,2,5))
cvcNotificationsGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:cvcNotificationsGroup.setStatus(_B)
cvcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,393,2,1,1))
cvcMIBCompliance.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:cvcMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoVoiceConnectivityMIB':ciscoVoiceConnectivityMIB,'ciscoVoiceConnectivityMIBNotifs':ciscoVoiceConnectivityMIBNotifs,_e:cvcPortRegistrationStatusChange,'ciscoVoiceConnectivityMIBObjects':ciscoVoiceConnectivityMIBObjects,'cvcCallAgent':cvcCallAgent,'cvcCallAgentTable':cvcCallAgentTable,'cvcCallAgentEntry':cvcCallAgentEntry,_F:cvcCallAgentIndex,_S:cvcCallAgentName,_T:cvcCallAgentInetAddressType,_H:cvcCallAgentInetAddress,_U:cvcCallAgentType,'cvcPort':cvcPort,'cvcPortTable':cvcPortTable,'cvcPortEntry':cvcPortEntry,_G:cvcPortIndex,_V:cvcPortAssociation,_I:cvcPortDeviceName,_W:cvcPortInetAddressType,_X:cvcPortInetAddress,_Y:cvcPortMACAddress,_Z:cvcPortType,_a:cvcProductCategory,_b:cvcProtocol,_c:cvcVirtualInterfaceDN,'cvcCallAgentConnection':cvcCallAgentConnection,'cvcCallAgentConnectionTable':cvcCallAgentConnectionTable,'cvcCallAgentConnectionEntry':cvcCallAgentConnectionEntry,_J:cvcCallAgentPriority,_K:cvcRegistrationStatus,_L:cvcStatusReason,_M:cvcLastStatusChangeTime,_N:cvcLastRegisteredTime,'cvcNotif':cvcNotif,_d:cvcNotifEnable,'ciscoVoiceConnectivityMIBConform':ciscoVoiceConnectivityMIBConform,'cvcMIBCompliances':cvcMIBCompliances,'cvcMIBCompliance':cvcMIBCompliance,'cvcMIBGroups':cvcMIBGroups,_f:cvcCallAgentGroup,_g:cvcPortGroup,_h:cvcCallAgentConnectionGroup,_i:cvcNotifGroup,_j:cvcNotificationsGroup})