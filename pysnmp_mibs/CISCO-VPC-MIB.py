_AB='cVpcMIBHostLinkStatusGroup'
_AA='cVpcMIBPeerLinkStatusGroup'
_A9='cVpcMIBStatisticsGroup'
_A8='cVpcMIBRoleGroup'
_A7='cVpcPeerKeepAliveStatusInfoGroup'
_A6='cVpcPeerKeepAliveConfigInfoGroup'
_A5='cVpcStatusHostLinkConsistencyDetail'
_A4='cVpcStatusHostLinkConsistencyStatus'
_A3='cVpcStatusHostLinkStatus'
_A2='cVpcStatusHostLinkIfIndex'
_A1='cVpcStatusPeerLinkIfIndex'
_A0='cVpcStatsPeerStatusChangeCount'
_z='cVpcStatsPeerKeepAliveAvgInterval'
_y='cVpcStatsPeerKeepAliveMsgsRcved'
_x='cVpcStatsPeerKeepAliveMsgsSent'
_w='cVpcLocalRoleOperPriority'
_v='cVpcLocalRoleAdminPriority'
_u='cVpcSystemOperPriority'
_t='cVpcSystemAdminPriority'
_s='cVpcLocalOperMacAddress'
_r='cVpcSystemOperMacAddress'
_q='cVpcSystemAdminMacAddress'
_p='cVpcDualActiveDetectionStatus'
_o='cVpcRoleStatus'
_n='cVpcPeerKeepAliveMsgReceiveInterface'
_m='cVpcPeerKeepAliveMsgLastReceiveTime'
_l='cVpcPeerKeepAliveMsgRcvrStatus'
_k='cVpcPeerKeepAliveMsgSendInterface'
_j='cVpcPeerKeepAliveMsgLastSendTime'
_i='cVpcPeerKeepAliveMsgSendStatus'
_h='cVpcPeerKeepAliveTime'
_g='cVpcPeerKeepAliveStatus'
_f='cVpcPeerKeepAliveVrfName'
_e='cVpcPeerKeepAliveTosByte'
_d='cVpcPeerKeepAlivePrecedence'
_c='cVpcPeerKeepAliveTos'
_b='cVpcPeerKeepAliveHoldTimeout'
_a='cVpcPeerKeepAliveTimeout'
_Z='cVpcPeerKeepAliveInterval'
_Y='cVpcPeerKeepAliveUdpPort'
_X='cVpcPeerKeepAliveSourceAddr'
_W='cVpcPeerKeepAliveSourceAddrType'
_V='cVpcPeerKeepAliveDestAddr'
_U='cVpcPeerKeepAliveDestAddrType'
_T='cVpcStatusHostLinkVpcID'
_S='cVpcStatusHostLinkDomainID'
_R='cVpcStatusPeerLinkDomainID'
_Q='cVpcStatsPeerKeepAliveDomainID'
_P='cVpcRoleDomainID'
_O='failure'
_N='cVpcPeerKeepAliveDomainID'
_M='milli-seconds'
_L='cVpcPeerKeepAliveConfigDomainID'
_K='SnmpAdminString'
_J='InetPortNumber'
_I='success'
_H='seconds'
_G='not-accessible'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='CISCO-VPC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
ciscoVpcMIB=ModuleIdentity((1,3,6,1,4,1,9,9,807))
if mibBuilder.loadTexts:ciscoVpcMIB.setRevisions(('2013-05-09 00:00',))
_CiscoVpcMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVpcMIBNotifs=_CiscoVpcMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,807,0))
_CiscoVpcMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVpcMIBObjects=_CiscoVpcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,807,1))
_CVpcPeerKeepAlive_ObjectIdentity=ObjectIdentity
cVpcPeerKeepAlive=_CVpcPeerKeepAlive_ObjectIdentity((1,3,6,1,4,1,9,9,807,1,1))
_CVpcPeerKeepAliveConfigTable_Object=MibTable
cVpcPeerKeepAliveConfigTable=_CVpcPeerKeepAliveConfigTable_Object((1,3,6,1,4,1,9,9,807,1,1,1))
if mibBuilder.loadTexts:cVpcPeerKeepAliveConfigTable.setStatus(_A)
_CVpcPeerKeepAliveConfigEntry_Object=MibTableRow
cVpcPeerKeepAliveConfigEntry=_CVpcPeerKeepAliveConfigEntry_Object((1,3,6,1,4,1,9,9,807,1,1,1,1))
cVpcPeerKeepAliveConfigEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:cVpcPeerKeepAliveConfigEntry.setStatus(_A)
_CVpcPeerKeepAliveConfigDomainID_Type=Unsigned32
_CVpcPeerKeepAliveConfigDomainID_Object=MibTableColumn
cVpcPeerKeepAliveConfigDomainID=_CVpcPeerKeepAliveConfigDomainID_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,1),_CVpcPeerKeepAliveConfigDomainID_Type())
cVpcPeerKeepAliveConfigDomainID.setMaxAccess(_G)
if mibBuilder.loadTexts:cVpcPeerKeepAliveConfigDomainID.setStatus(_A)
_CVpcPeerKeepAliveDestAddrType_Type=InetAddressType
_CVpcPeerKeepAliveDestAddrType_Object=MibTableColumn
cVpcPeerKeepAliveDestAddrType=_CVpcPeerKeepAliveDestAddrType_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,2),_CVpcPeerKeepAliveDestAddrType_Type())
cVpcPeerKeepAliveDestAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveDestAddrType.setStatus(_A)
_CVpcPeerKeepAliveDestAddr_Type=InetAddress
_CVpcPeerKeepAliveDestAddr_Object=MibTableColumn
cVpcPeerKeepAliveDestAddr=_CVpcPeerKeepAliveDestAddr_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,3),_CVpcPeerKeepAliveDestAddr_Type())
cVpcPeerKeepAliveDestAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveDestAddr.setStatus(_A)
_CVpcPeerKeepAliveSourceAddrType_Type=InetAddressType
_CVpcPeerKeepAliveSourceAddrType_Object=MibTableColumn
cVpcPeerKeepAliveSourceAddrType=_CVpcPeerKeepAliveSourceAddrType_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,4),_CVpcPeerKeepAliveSourceAddrType_Type())
cVpcPeerKeepAliveSourceAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveSourceAddrType.setStatus(_A)
_CVpcPeerKeepAliveSourceAddr_Type=InetAddress
_CVpcPeerKeepAliveSourceAddr_Object=MibTableColumn
cVpcPeerKeepAliveSourceAddr=_CVpcPeerKeepAliveSourceAddr_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,5),_CVpcPeerKeepAliveSourceAddr_Type())
cVpcPeerKeepAliveSourceAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveSourceAddr.setStatus(_A)
class _CVpcPeerKeepAliveUdpPort_Type(InetPortNumber):defaultValue=3200
_CVpcPeerKeepAliveUdpPort_Type.__name__=_J
_CVpcPeerKeepAliveUdpPort_Object=MibTableColumn
cVpcPeerKeepAliveUdpPort=_CVpcPeerKeepAliveUdpPort_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,6),_CVpcPeerKeepAliveUdpPort_Type())
cVpcPeerKeepAliveUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveUdpPort.setStatus(_A)
class _CVpcPeerKeepAliveInterval_Type(Unsigned32):defaultValue=1000
_CVpcPeerKeepAliveInterval_Type.__name__=_F
_CVpcPeerKeepAliveInterval_Object=MibTableColumn
cVpcPeerKeepAliveInterval=_CVpcPeerKeepAliveInterval_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,7),_CVpcPeerKeepAliveInterval_Type())
cVpcPeerKeepAliveInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveInterval.setStatus(_A)
if mibBuilder.loadTexts:cVpcPeerKeepAliveInterval.setUnits(_M)
class _CVpcPeerKeepAliveTimeout_Type(Unsigned32):defaultValue=5
_CVpcPeerKeepAliveTimeout_Type.__name__=_F
_CVpcPeerKeepAliveTimeout_Object=MibTableColumn
cVpcPeerKeepAliveTimeout=_CVpcPeerKeepAliveTimeout_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,8),_CVpcPeerKeepAliveTimeout_Type())
cVpcPeerKeepAliveTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveTimeout.setStatus(_A)
if mibBuilder.loadTexts:cVpcPeerKeepAliveTimeout.setUnits(_H)
class _CVpcPeerKeepAliveHoldTimeout_Type(Unsigned32):defaultValue=3
_CVpcPeerKeepAliveHoldTimeout_Type.__name__=_F
_CVpcPeerKeepAliveHoldTimeout_Object=MibTableColumn
cVpcPeerKeepAliveHoldTimeout=_CVpcPeerKeepAliveHoldTimeout_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,9),_CVpcPeerKeepAliveHoldTimeout_Type())
cVpcPeerKeepAliveHoldTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveHoldTimeout.setStatus(_A)
if mibBuilder.loadTexts:cVpcPeerKeepAliveHoldTimeout.setUnits(_H)
class _CVpcPeerKeepAliveTos_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CVpcPeerKeepAliveTos_Type.__name__=_F
_CVpcPeerKeepAliveTos_Object=MibTableColumn
cVpcPeerKeepAliveTos=_CVpcPeerKeepAliveTos_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,10),_CVpcPeerKeepAliveTos_Type())
cVpcPeerKeepAliveTos.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveTos.setStatus(_A)
class _CVpcPeerKeepAlivePrecedence_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CVpcPeerKeepAlivePrecedence_Type.__name__=_F
_CVpcPeerKeepAlivePrecedence_Object=MibTableColumn
cVpcPeerKeepAlivePrecedence=_CVpcPeerKeepAlivePrecedence_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,11),_CVpcPeerKeepAlivePrecedence_Type())
cVpcPeerKeepAlivePrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAlivePrecedence.setStatus(_A)
class _CVpcPeerKeepAliveTosByte_Type(Unsigned32):defaultValue=192;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CVpcPeerKeepAliveTosByte_Type.__name__=_F
_CVpcPeerKeepAliveTosByte_Object=MibTableColumn
cVpcPeerKeepAliveTosByte=_CVpcPeerKeepAliveTosByte_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,12),_CVpcPeerKeepAliveTosByte_Type())
cVpcPeerKeepAliveTosByte.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveTosByte.setStatus(_A)
class _CVpcPeerKeepAliveVrfName_Type(SnmpAdminString):defaultValue=OctetString('management')
_CVpcPeerKeepAliveVrfName_Type.__name__=_K
_CVpcPeerKeepAliveVrfName_Object=MibTableColumn
cVpcPeerKeepAliveVrfName=_CVpcPeerKeepAliveVrfName_Object((1,3,6,1,4,1,9,9,807,1,1,1,1,13),_CVpcPeerKeepAliveVrfName_Type())
cVpcPeerKeepAliveVrfName.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcPeerKeepAliveVrfName.setStatus(_A)
_CVpcPeerKeepAliveTable_Object=MibTable
cVpcPeerKeepAliveTable=_CVpcPeerKeepAliveTable_Object((1,3,6,1,4,1,9,9,807,1,1,2))
if mibBuilder.loadTexts:cVpcPeerKeepAliveTable.setStatus(_A)
_CVpcPeerKeepAliveEntry_Object=MibTableRow
cVpcPeerKeepAliveEntry=_CVpcPeerKeepAliveEntry_Object((1,3,6,1,4,1,9,9,807,1,1,2,1))
cVpcPeerKeepAliveEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:cVpcPeerKeepAliveEntry.setStatus(_A)
_CVpcPeerKeepAliveDomainID_Type=Unsigned32
_CVpcPeerKeepAliveDomainID_Object=MibTableColumn
cVpcPeerKeepAliveDomainID=_CVpcPeerKeepAliveDomainID_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,1),_CVpcPeerKeepAliveDomainID_Type())
cVpcPeerKeepAliveDomainID.setMaxAccess(_G)
if mibBuilder.loadTexts:cVpcPeerKeepAliveDomainID.setStatus(_A)
class _CVpcPeerKeepAliveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('disabled',1),('alive',2),('peerUnreachable',3),('aliveButDomainIdDismatch',4),('suspendedAsISSU',5),('suspendedAsDestIPUnreachable',6),('suspendedAsVRFUnusable',7),('misconfigured',8)))
_CVpcPeerKeepAliveStatus_Type.__name__=_E
_CVpcPeerKeepAliveStatus_Object=MibTableColumn
cVpcPeerKeepAliveStatus=_CVpcPeerKeepAliveStatus_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,2),_CVpcPeerKeepAliveStatus_Type())
cVpcPeerKeepAliveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveStatus.setStatus(_A)
_CVpcPeerKeepAliveTime_Type=CounterBasedGauge64
_CVpcPeerKeepAliveTime_Object=MibTableColumn
cVpcPeerKeepAliveTime=_CVpcPeerKeepAliveTime_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,3),_CVpcPeerKeepAliveTime_Type())
cVpcPeerKeepAliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveTime.setStatus(_A)
if mibBuilder.loadTexts:cVpcPeerKeepAliveTime.setUnits(_M)
class _CVpcPeerKeepAliveMsgSendStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_O,2)))
_CVpcPeerKeepAliveMsgSendStatus_Type.__name__=_E
_CVpcPeerKeepAliveMsgSendStatus_Object=MibTableColumn
cVpcPeerKeepAliveMsgSendStatus=_CVpcPeerKeepAliveMsgSendStatus_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,4),_CVpcPeerKeepAliveMsgSendStatus_Type())
cVpcPeerKeepAliveMsgSendStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveMsgSendStatus.setStatus(_A)
_CVpcPeerKeepAliveMsgLastSendTime_Type=DateAndTime
_CVpcPeerKeepAliveMsgLastSendTime_Object=MibTableColumn
cVpcPeerKeepAliveMsgLastSendTime=_CVpcPeerKeepAliveMsgLastSendTime_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,5),_CVpcPeerKeepAliveMsgLastSendTime_Type())
cVpcPeerKeepAliveMsgLastSendTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveMsgLastSendTime.setStatus(_A)
_CVpcPeerKeepAliveMsgSendInterface_Type=InterfaceIndexOrZero
_CVpcPeerKeepAliveMsgSendInterface_Object=MibTableColumn
cVpcPeerKeepAliveMsgSendInterface=_CVpcPeerKeepAliveMsgSendInterface_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,6),_CVpcPeerKeepAliveMsgSendInterface_Type())
cVpcPeerKeepAliveMsgSendInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveMsgSendInterface.setStatus(_A)
class _CVpcPeerKeepAliveMsgRcvrStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_O,2)))
_CVpcPeerKeepAliveMsgRcvrStatus_Type.__name__=_E
_CVpcPeerKeepAliveMsgRcvrStatus_Object=MibTableColumn
cVpcPeerKeepAliveMsgRcvrStatus=_CVpcPeerKeepAliveMsgRcvrStatus_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,7),_CVpcPeerKeepAliveMsgRcvrStatus_Type())
cVpcPeerKeepAliveMsgRcvrStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveMsgRcvrStatus.setStatus(_A)
_CVpcPeerKeepAliveMsgLastReceiveTime_Type=DateAndTime
_CVpcPeerKeepAliveMsgLastReceiveTime_Object=MibTableColumn
cVpcPeerKeepAliveMsgLastReceiveTime=_CVpcPeerKeepAliveMsgLastReceiveTime_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,8),_CVpcPeerKeepAliveMsgLastReceiveTime_Type())
cVpcPeerKeepAliveMsgLastReceiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveMsgLastReceiveTime.setStatus(_A)
_CVpcPeerKeepAliveMsgReceiveInterface_Type=InterfaceIndexOrZero
_CVpcPeerKeepAliveMsgReceiveInterface_Object=MibTableColumn
cVpcPeerKeepAliveMsgReceiveInterface=_CVpcPeerKeepAliveMsgReceiveInterface_Object((1,3,6,1,4,1,9,9,807,1,1,2,1,9),_CVpcPeerKeepAliveMsgReceiveInterface_Type())
cVpcPeerKeepAliveMsgReceiveInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcPeerKeepAliveMsgReceiveInterface.setStatus(_A)
_CVpcRole_ObjectIdentity=ObjectIdentity
cVpcRole=_CVpcRole_ObjectIdentity((1,3,6,1,4,1,9,9,807,1,2))
_CVpcRoleTable_Object=MibTable
cVpcRoleTable=_CVpcRoleTable_Object((1,3,6,1,4,1,9,9,807,1,2,1))
if mibBuilder.loadTexts:cVpcRoleTable.setStatus(_A)
_CVpcRoleEntry_Object=MibTableRow
cVpcRoleEntry=_CVpcRoleEntry_Object((1,3,6,1,4,1,9,9,807,1,2,1,1))
cVpcRoleEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:cVpcRoleEntry.setStatus(_A)
_CVpcRoleDomainID_Type=Unsigned32
_CVpcRoleDomainID_Object=MibTableColumn
cVpcRoleDomainID=_CVpcRoleDomainID_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,1),_CVpcRoleDomainID_Type())
cVpcRoleDomainID.setMaxAccess(_G)
if mibBuilder.loadTexts:cVpcRoleDomainID.setStatus(_A)
class _CVpcRoleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('primarySecondary',1),('primary',2),('secondaryPrimary',3),('secondary',4),('noneEstablished',5)))
_CVpcRoleStatus_Type.__name__=_E
_CVpcRoleStatus_Object=MibTableColumn
cVpcRoleStatus=_CVpcRoleStatus_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,2),_CVpcRoleStatus_Type())
cVpcRoleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcRoleStatus.setStatus(_A)
_CVpcDualActiveDetectionStatus_Type=TruthValue
_CVpcDualActiveDetectionStatus_Object=MibTableColumn
cVpcDualActiveDetectionStatus=_CVpcDualActiveDetectionStatus_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,3),_CVpcDualActiveDetectionStatus_Type())
cVpcDualActiveDetectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcDualActiveDetectionStatus.setStatus(_A)
_CVpcSystemAdminMacAddress_Type=MacAddress
_CVpcSystemAdminMacAddress_Object=MibTableColumn
cVpcSystemAdminMacAddress=_CVpcSystemAdminMacAddress_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,4),_CVpcSystemAdminMacAddress_Type())
cVpcSystemAdminMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcSystemAdminMacAddress.setStatus(_A)
_CVpcSystemOperMacAddress_Type=MacAddress
_CVpcSystemOperMacAddress_Object=MibTableColumn
cVpcSystemOperMacAddress=_CVpcSystemOperMacAddress_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,5),_CVpcSystemOperMacAddress_Type())
cVpcSystemOperMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcSystemOperMacAddress.setStatus(_A)
_CVpcLocalOperMacAddress_Type=MacAddress
_CVpcLocalOperMacAddress_Object=MibTableColumn
cVpcLocalOperMacAddress=_CVpcLocalOperMacAddress_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,6),_CVpcLocalOperMacAddress_Type())
cVpcLocalOperMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcLocalOperMacAddress.setStatus(_A)
_CVpcSystemAdminPriority_Type=Unsigned32
_CVpcSystemAdminPriority_Object=MibTableColumn
cVpcSystemAdminPriority=_CVpcSystemAdminPriority_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,7),_CVpcSystemAdminPriority_Type())
cVpcSystemAdminPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcSystemAdminPriority.setStatus(_A)
_CVpcSystemOperPriority_Type=Unsigned32
_CVpcSystemOperPriority_Object=MibTableColumn
cVpcSystemOperPriority=_CVpcSystemOperPriority_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,8),_CVpcSystemOperPriority_Type())
cVpcSystemOperPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcSystemOperPriority.setStatus(_A)
_CVpcLocalRoleAdminPriority_Type=Unsigned32
_CVpcLocalRoleAdminPriority_Object=MibTableColumn
cVpcLocalRoleAdminPriority=_CVpcLocalRoleAdminPriority_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,9),_CVpcLocalRoleAdminPriority_Type())
cVpcLocalRoleAdminPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cVpcLocalRoleAdminPriority.setStatus(_A)
_CVpcLocalRoleOperPriority_Type=Unsigned32
_CVpcLocalRoleOperPriority_Object=MibTableColumn
cVpcLocalRoleOperPriority=_CVpcLocalRoleOperPriority_Object((1,3,6,1,4,1,9,9,807,1,2,1,1,10),_CVpcLocalRoleOperPriority_Type())
cVpcLocalRoleOperPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcLocalRoleOperPriority.setStatus(_A)
_CVpcStatistics_ObjectIdentity=ObjectIdentity
cVpcStatistics=_CVpcStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,807,1,3))
_CVpcStatsPeerKeepAliveTable_Object=MibTable
cVpcStatsPeerKeepAliveTable=_CVpcStatsPeerKeepAliveTable_Object((1,3,6,1,4,1,9,9,807,1,3,1))
if mibBuilder.loadTexts:cVpcStatsPeerKeepAliveTable.setStatus(_A)
_CVpcStatsPeerKeepAliveEntry_Object=MibTableRow
cVpcStatsPeerKeepAliveEntry=_CVpcStatsPeerKeepAliveEntry_Object((1,3,6,1,4,1,9,9,807,1,3,1,1))
cVpcStatsPeerKeepAliveEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cVpcStatsPeerKeepAliveEntry.setStatus(_A)
_CVpcStatsPeerKeepAliveDomainID_Type=Unsigned32
_CVpcStatsPeerKeepAliveDomainID_Object=MibTableColumn
cVpcStatsPeerKeepAliveDomainID=_CVpcStatsPeerKeepAliveDomainID_Object((1,3,6,1,4,1,9,9,807,1,3,1,1,1),_CVpcStatsPeerKeepAliveDomainID_Type())
cVpcStatsPeerKeepAliveDomainID.setMaxAccess(_G)
if mibBuilder.loadTexts:cVpcStatsPeerKeepAliveDomainID.setStatus(_A)
_CVpcStatsPeerKeepAliveMsgsSent_Type=Counter32
_CVpcStatsPeerKeepAliveMsgsSent_Object=MibTableColumn
cVpcStatsPeerKeepAliveMsgsSent=_CVpcStatsPeerKeepAliveMsgsSent_Object((1,3,6,1,4,1,9,9,807,1,3,1,1,2),_CVpcStatsPeerKeepAliveMsgsSent_Type())
cVpcStatsPeerKeepAliveMsgsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatsPeerKeepAliveMsgsSent.setStatus(_A)
_CVpcStatsPeerKeepAliveMsgsRcved_Type=Counter32
_CVpcStatsPeerKeepAliveMsgsRcved_Object=MibTableColumn
cVpcStatsPeerKeepAliveMsgsRcved=_CVpcStatsPeerKeepAliveMsgsRcved_Object((1,3,6,1,4,1,9,9,807,1,3,1,1,3),_CVpcStatsPeerKeepAliveMsgsRcved_Type())
cVpcStatsPeerKeepAliveMsgsRcved.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatsPeerKeepAliveMsgsRcved.setStatus(_A)
_CVpcStatsPeerKeepAliveAvgInterval_Type=Unsigned32
_CVpcStatsPeerKeepAliveAvgInterval_Object=MibTableColumn
cVpcStatsPeerKeepAliveAvgInterval=_CVpcStatsPeerKeepAliveAvgInterval_Object((1,3,6,1,4,1,9,9,807,1,3,1,1,4),_CVpcStatsPeerKeepAliveAvgInterval_Type())
cVpcStatsPeerKeepAliveAvgInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatsPeerKeepAliveAvgInterval.setStatus(_A)
if mibBuilder.loadTexts:cVpcStatsPeerKeepAliveAvgInterval.setUnits(_H)
_CVpcStatsPeerStatusChangeCount_Type=Counter32
_CVpcStatsPeerStatusChangeCount_Object=MibTableColumn
cVpcStatsPeerStatusChangeCount=_CVpcStatsPeerStatusChangeCount_Object((1,3,6,1,4,1,9,9,807,1,3,1,1,5),_CVpcStatsPeerStatusChangeCount_Type())
cVpcStatsPeerStatusChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatsPeerStatusChangeCount.setStatus(_A)
_CVpcStatus_ObjectIdentity=ObjectIdentity
cVpcStatus=_CVpcStatus_ObjectIdentity((1,3,6,1,4,1,9,9,807,1,4))
_CVpcStatusPeerLinkTable_Object=MibTable
cVpcStatusPeerLinkTable=_CVpcStatusPeerLinkTable_Object((1,3,6,1,4,1,9,9,807,1,4,1))
if mibBuilder.loadTexts:cVpcStatusPeerLinkTable.setStatus(_A)
_CVpcStatusPeerLinkEntry_Object=MibTableRow
cVpcStatusPeerLinkEntry=_CVpcStatusPeerLinkEntry_Object((1,3,6,1,4,1,9,9,807,1,4,1,1))
cVpcStatusPeerLinkEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:cVpcStatusPeerLinkEntry.setStatus(_A)
_CVpcStatusPeerLinkDomainID_Type=Unsigned32
_CVpcStatusPeerLinkDomainID_Object=MibTableColumn
cVpcStatusPeerLinkDomainID=_CVpcStatusPeerLinkDomainID_Object((1,3,6,1,4,1,9,9,807,1,4,1,1,1),_CVpcStatusPeerLinkDomainID_Type())
cVpcStatusPeerLinkDomainID.setMaxAccess(_G)
if mibBuilder.loadTexts:cVpcStatusPeerLinkDomainID.setStatus(_A)
_CVpcStatusPeerLinkIfIndex_Type=InterfaceIndex
_CVpcStatusPeerLinkIfIndex_Object=MibTableColumn
cVpcStatusPeerLinkIfIndex=_CVpcStatusPeerLinkIfIndex_Object((1,3,6,1,4,1,9,9,807,1,4,1,1,2),_CVpcStatusPeerLinkIfIndex_Type())
cVpcStatusPeerLinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatusPeerLinkIfIndex.setStatus(_A)
_CVpcStatusHostLinkTable_Object=MibTable
cVpcStatusHostLinkTable=_CVpcStatusHostLinkTable_Object((1,3,6,1,4,1,9,9,807,1,4,2))
if mibBuilder.loadTexts:cVpcStatusHostLinkTable.setStatus(_A)
_CVpcStatusHostLinkEntry_Object=MibTableRow
cVpcStatusHostLinkEntry=_CVpcStatusHostLinkEntry_Object((1,3,6,1,4,1,9,9,807,1,4,2,1))
cVpcStatusHostLinkEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cVpcStatusHostLinkEntry.setStatus(_A)
_CVpcStatusHostLinkDomainID_Type=Unsigned32
_CVpcStatusHostLinkDomainID_Object=MibTableColumn
cVpcStatusHostLinkDomainID=_CVpcStatusHostLinkDomainID_Object((1,3,6,1,4,1,9,9,807,1,4,2,1,1),_CVpcStatusHostLinkDomainID_Type())
cVpcStatusHostLinkDomainID.setMaxAccess(_G)
if mibBuilder.loadTexts:cVpcStatusHostLinkDomainID.setStatus(_A)
_CVpcStatusHostLinkVpcID_Type=Unsigned32
_CVpcStatusHostLinkVpcID_Object=MibTableColumn
cVpcStatusHostLinkVpcID=_CVpcStatusHostLinkVpcID_Object((1,3,6,1,4,1,9,9,807,1,4,2,1,2),_CVpcStatusHostLinkVpcID_Type())
cVpcStatusHostLinkVpcID.setMaxAccess(_G)
if mibBuilder.loadTexts:cVpcStatusHostLinkVpcID.setStatus(_A)
_CVpcStatusHostLinkIfIndex_Type=InterfaceIndexOrZero
_CVpcStatusHostLinkIfIndex_Object=MibTableColumn
cVpcStatusHostLinkIfIndex=_CVpcStatusHostLinkIfIndex_Object((1,3,6,1,4,1,9,9,807,1,4,2,1,3),_CVpcStatusHostLinkIfIndex_Type())
cVpcStatusHostLinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatusHostLinkIfIndex.setStatus(_A)
class _CVpcStatusHostLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('down',1),('downStar',2),('up',3)))
_CVpcStatusHostLinkStatus_Type.__name__=_E
_CVpcStatusHostLinkStatus_Object=MibTableColumn
cVpcStatusHostLinkStatus=_CVpcStatusHostLinkStatus_Object((1,3,6,1,4,1,9,9,807,1,4,2,1,4),_CVpcStatusHostLinkStatus_Type())
cVpcStatusHostLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatusHostLinkStatus.setStatus(_A)
class _CVpcStatusHostLinkConsistencyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('failed',2),('notApplicable',3)))
_CVpcStatusHostLinkConsistencyStatus_Type.__name__=_E
_CVpcStatusHostLinkConsistencyStatus_Object=MibTableColumn
cVpcStatusHostLinkConsistencyStatus=_CVpcStatusHostLinkConsistencyStatus_Object((1,3,6,1,4,1,9,9,807,1,4,2,1,5),_CVpcStatusHostLinkConsistencyStatus_Type())
cVpcStatusHostLinkConsistencyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatusHostLinkConsistencyStatus.setStatus(_A)
_CVpcStatusHostLinkConsistencyDetail_Type=SnmpAdminString
_CVpcStatusHostLinkConsistencyDetail_Object=MibTableColumn
cVpcStatusHostLinkConsistencyDetail=_CVpcStatusHostLinkConsistencyDetail_Object((1,3,6,1,4,1,9,9,807,1,4,2,1,6),_CVpcStatusHostLinkConsistencyDetail_Type())
cVpcStatusHostLinkConsistencyDetail.setMaxAccess(_C)
if mibBuilder.loadTexts:cVpcStatusHostLinkConsistencyDetail.setStatus(_A)
_CiscoVpcMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVpcMIBConformance=_CiscoVpcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,807,2))
_CiscoVpcMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVpcMIBCompliances=_CiscoVpcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,807,2,1))
_CiscoVpcMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVpcMIBGroups=_CiscoVpcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,807,2,2))
cVpcPeerKeepAliveConfigInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,807,2,2,1))
cVpcPeerKeepAliveConfigInfoGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cVpcPeerKeepAliveConfigInfoGroup.setStatus(_A)
cVpcPeerKeepAliveStatusInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,807,2,2,2))
cVpcPeerKeepAliveStatusInfoGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cVpcPeerKeepAliveStatusInfoGroup.setStatus(_A)
cVpcMIBRoleGroup=ObjectGroup((1,3,6,1,4,1,9,9,807,2,2,3))
cVpcMIBRoleGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cVpcMIBRoleGroup.setStatus(_A)
cVpcMIBStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,807,2,2,4))
cVpcMIBStatisticsGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cVpcMIBStatisticsGroup.setStatus(_A)
cVpcMIBPeerLinkStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,807,2,2,5))
cVpcMIBPeerLinkStatusGroup.setObjects((_B,_A1))
if mibBuilder.loadTexts:cVpcMIBPeerLinkStatusGroup.setStatus(_A)
cVpcMIBHostLinkStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,807,2,2,6))
cVpcMIBHostLinkStatusGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:cVpcMIBHostLinkStatusGroup.setStatus(_A)
ciscoVpcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,807,2,1,1))
ciscoVpcMIBCompliance.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:ciscoVpcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoVpcMIB':ciscoVpcMIB,'ciscoVpcMIBNotifs':ciscoVpcMIBNotifs,'ciscoVpcMIBObjects':ciscoVpcMIBObjects,'cVpcPeerKeepAlive':cVpcPeerKeepAlive,'cVpcPeerKeepAliveConfigTable':cVpcPeerKeepAliveConfigTable,'cVpcPeerKeepAliveConfigEntry':cVpcPeerKeepAliveConfigEntry,_L:cVpcPeerKeepAliveConfigDomainID,_U:cVpcPeerKeepAliveDestAddrType,_V:cVpcPeerKeepAliveDestAddr,_W:cVpcPeerKeepAliveSourceAddrType,_X:cVpcPeerKeepAliveSourceAddr,_Y:cVpcPeerKeepAliveUdpPort,_Z:cVpcPeerKeepAliveInterval,_a:cVpcPeerKeepAliveTimeout,_b:cVpcPeerKeepAliveHoldTimeout,_c:cVpcPeerKeepAliveTos,_d:cVpcPeerKeepAlivePrecedence,_e:cVpcPeerKeepAliveTosByte,_f:cVpcPeerKeepAliveVrfName,'cVpcPeerKeepAliveTable':cVpcPeerKeepAliveTable,'cVpcPeerKeepAliveEntry':cVpcPeerKeepAliveEntry,_N:cVpcPeerKeepAliveDomainID,_g:cVpcPeerKeepAliveStatus,_h:cVpcPeerKeepAliveTime,_i:cVpcPeerKeepAliveMsgSendStatus,_j:cVpcPeerKeepAliveMsgLastSendTime,_k:cVpcPeerKeepAliveMsgSendInterface,_l:cVpcPeerKeepAliveMsgRcvrStatus,_m:cVpcPeerKeepAliveMsgLastReceiveTime,_n:cVpcPeerKeepAliveMsgReceiveInterface,'cVpcRole':cVpcRole,'cVpcRoleTable':cVpcRoleTable,'cVpcRoleEntry':cVpcRoleEntry,_P:cVpcRoleDomainID,_o:cVpcRoleStatus,_p:cVpcDualActiveDetectionStatus,_q:cVpcSystemAdminMacAddress,_r:cVpcSystemOperMacAddress,_s:cVpcLocalOperMacAddress,_t:cVpcSystemAdminPriority,_u:cVpcSystemOperPriority,_v:cVpcLocalRoleAdminPriority,_w:cVpcLocalRoleOperPriority,'cVpcStatistics':cVpcStatistics,'cVpcStatsPeerKeepAliveTable':cVpcStatsPeerKeepAliveTable,'cVpcStatsPeerKeepAliveEntry':cVpcStatsPeerKeepAliveEntry,_Q:cVpcStatsPeerKeepAliveDomainID,_x:cVpcStatsPeerKeepAliveMsgsSent,_y:cVpcStatsPeerKeepAliveMsgsRcved,_z:cVpcStatsPeerKeepAliveAvgInterval,_A0:cVpcStatsPeerStatusChangeCount,'cVpcStatus':cVpcStatus,'cVpcStatusPeerLinkTable':cVpcStatusPeerLinkTable,'cVpcStatusPeerLinkEntry':cVpcStatusPeerLinkEntry,_R:cVpcStatusPeerLinkDomainID,_A1:cVpcStatusPeerLinkIfIndex,'cVpcStatusHostLinkTable':cVpcStatusHostLinkTable,'cVpcStatusHostLinkEntry':cVpcStatusHostLinkEntry,_S:cVpcStatusHostLinkDomainID,_T:cVpcStatusHostLinkVpcID,_A2:cVpcStatusHostLinkIfIndex,_A3:cVpcStatusHostLinkStatus,_A4:cVpcStatusHostLinkConsistencyStatus,_A5:cVpcStatusHostLinkConsistencyDetail,'ciscoVpcMIBConformance':ciscoVpcMIBConformance,'ciscoVpcMIBCompliances':ciscoVpcMIBCompliances,'ciscoVpcMIBCompliance':ciscoVpcMIBCompliance,'ciscoVpcMIBGroups':ciscoVpcMIBGroups,_A6:cVpcPeerKeepAliveConfigInfoGroup,_A7:cVpcPeerKeepAliveStatusInfoGroup,_A8:cVpcMIBRoleGroup,_A9:cVpcMIBStatisticsGroup,_AA:cVpcMIBPeerLinkStatusGroup,_AB:cVpcMIBHostLinkStatusGroup})