_S='notpresent'
_R='eltexVpcMemberStatusIfIndex'
_Q='eltexVpcMemberStatusVpcGroupIndex'
_P='eltexVpcGroupIndex'
_O='read-create'
_N='00000000'
_M='InterfaceIndexOrZero'
_L='secondary'
_K='primary'
_J='IpAddress'
_I='eltexVpcDomainIndex'
_H='enabled'
_G='disabled'
_F='ELTEX-VPC-MIB'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_J,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltexVpcMIB=ModuleIdentity((1,3,6,1,4,1,35265,125))
if mibBuilder.loadTexts:eltexVpcMIB.setRevisions(('2018-09-17 00:00',))
_EltexVpcMIBObjects_ObjectIdentity=ObjectIdentity
eltexVpcMIBObjects=_EltexVpcMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,125,1))
_EltexVpcConfigGroup_ObjectIdentity=ObjectIdentity
eltexVpcConfigGroup=_EltexVpcConfigGroup_ObjectIdentity((1,3,6,1,4,1,35265,125,1,1))
class _EltexVpcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_EltexVpcMode_Type.__name__=_D
_EltexVpcMode_Object=MibScalar
eltexVpcMode=_EltexVpcMode_Object((1,3,6,1,4,1,35265,125,1,1,1),_EltexVpcMode_Type())
eltexVpcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcMode.setStatus(_A)
_EltexVpcDomainConfigTable_Object=MibTable
eltexVpcDomainConfigTable=_EltexVpcDomainConfigTable_Object((1,3,6,1,4,1,35265,125,1,1,2))
if mibBuilder.loadTexts:eltexVpcDomainConfigTable.setStatus(_A)
_EltexVpcDomainConfigEntry_Object=MibTableRow
eltexVpcDomainConfigEntry=_EltexVpcDomainConfigEntry_Object((1,3,6,1,4,1,35265,125,1,1,2,1))
eltexVpcDomainConfigEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:eltexVpcDomainConfigEntry.setStatus(_A)
class _EltexVpcDomainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EltexVpcDomainIndex_Type.__name__=_E
_EltexVpcDomainIndex_Object=MibTableColumn
eltexVpcDomainIndex=_EltexVpcDomainIndex_Object((1,3,6,1,4,1,35265,125,1,1,2,1,1),_EltexVpcDomainIndex_Type())
eltexVpcDomainIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainIndex.setStatus(_A)
_EltexVpcDomainPeerLink_Type=InterfaceIndexOrZero
_EltexVpcDomainPeerLink_Object=MibTableColumn
eltexVpcDomainPeerLink=_EltexVpcDomainPeerLink_Object((1,3,6,1,4,1,35265,125,1,1,2,1,2),_EltexVpcDomainPeerLink_Type())
eltexVpcDomainPeerLink.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainPeerLink.setStatus(_A)
class _EltexVpcDomainKeepalivePriority_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_EltexVpcDomainKeepalivePriority_Type.__name__=_E
_EltexVpcDomainKeepalivePriority_Object=MibTableColumn
eltexVpcDomainKeepalivePriority=_EltexVpcDomainKeepalivePriority_Object((1,3,6,1,4,1,35265,125,1,1,2,1,3),_EltexVpcDomainKeepalivePriority_Type())
eltexVpcDomainKeepalivePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainKeepalivePriority.setStatus(_A)
class _EltexVpcDomainKeepaliveTimeout_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,15))
_EltexVpcDomainKeepaliveTimeout_Type.__name__=_E
_EltexVpcDomainKeepaliveTimeout_Object=MibTableColumn
eltexVpcDomainKeepaliveTimeout=_EltexVpcDomainKeepaliveTimeout_Object((1,3,6,1,4,1,35265,125,1,1,2,1,4),_EltexVpcDomainKeepaliveTimeout_Type())
eltexVpcDomainKeepaliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainKeepaliveTimeout.setStatus(_A)
class _EltexVpcDomainKeepaliveMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_EltexVpcDomainKeepaliveMode_Type.__name__=_D
_EltexVpcDomainKeepaliveMode_Object=MibTableColumn
eltexVpcDomainKeepaliveMode=_EltexVpcDomainKeepaliveMode_Object((1,3,6,1,4,1,35265,125,1,1,2,1,5),_EltexVpcDomainKeepaliveMode_Type())
eltexVpcDomainKeepaliveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainKeepaliveMode.setStatus(_A)
_EltexVpcDomainSystemMac_Type=MacAddress
_EltexVpcDomainSystemMac_Object=MibTableColumn
eltexVpcDomainSystemMac=_EltexVpcDomainSystemMac_Object((1,3,6,1,4,1,35265,125,1,1,2,1,6),_EltexVpcDomainSystemMac_Type())
eltexVpcDomainSystemMac.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainSystemMac.setStatus(_A)
class _EltexVpcDomainSystemPriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexVpcDomainSystemPriority_Type.__name__=_E
_EltexVpcDomainSystemPriority_Object=MibTableColumn
eltexVpcDomainSystemPriority=_EltexVpcDomainSystemPriority_Object((1,3,6,1,4,1,35265,125,1,1,2,1,7),_EltexVpcDomainSystemPriority_Type())
eltexVpcDomainSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainSystemPriority.setStatus(_A)
class _EltexVpcDomainPeerDetectionMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_EltexVpcDomainPeerDetectionMode_Type.__name__=_D
_EltexVpcDomainPeerDetectionMode_Object=MibTableColumn
eltexVpcDomainPeerDetectionMode=_EltexVpcDomainPeerDetectionMode_Object((1,3,6,1,4,1,35265,125,1,1,2,1,8),_EltexVpcDomainPeerDetectionMode_Type())
eltexVpcDomainPeerDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionMode.setStatus(_A)
class _EltexVpcDomainPeerDetectionInterval_Type(Unsigned32):defaultValue=700;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,4000))
_EltexVpcDomainPeerDetectionInterval_Type.__name__=_E
_EltexVpcDomainPeerDetectionInterval_Object=MibTableColumn
eltexVpcDomainPeerDetectionInterval=_EltexVpcDomainPeerDetectionInterval_Object((1,3,6,1,4,1,35265,125,1,1,2,1,9),_EltexVpcDomainPeerDetectionInterval_Type())
eltexVpcDomainPeerDetectionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionInterval.setStatus(_A)
class _EltexVpcDomainPeerDetectionTimeout_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(700,14000))
_EltexVpcDomainPeerDetectionTimeout_Type.__name__=_E
_EltexVpcDomainPeerDetectionTimeout_Object=MibTableColumn
eltexVpcDomainPeerDetectionTimeout=_EltexVpcDomainPeerDetectionTimeout_Object((1,3,6,1,4,1,35265,125,1,1,2,1,10),_EltexVpcDomainPeerDetectionTimeout_Type())
eltexVpcDomainPeerDetectionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionTimeout.setStatus(_A)
class _EltexVpcDomainPeerIpAddr_Type(IpAddress):defaultHexValue=_N
_EltexVpcDomainPeerIpAddr_Type.__name__=_J
_EltexVpcDomainPeerIpAddr_Object=MibTableColumn
eltexVpcDomainPeerIpAddr=_EltexVpcDomainPeerIpAddr_Object((1,3,6,1,4,1,35265,125,1,1,2,1,11),_EltexVpcDomainPeerIpAddr_Type())
eltexVpcDomainPeerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainPeerIpAddr.setStatus(_A)
class _EltexVpcDomainSourceIpAddr_Type(IpAddress):defaultHexValue=_N
_EltexVpcDomainSourceIpAddr_Type.__name__=_J
_EltexVpcDomainSourceIpAddr_Object=MibTableColumn
eltexVpcDomainSourceIpAddr=_EltexVpcDomainSourceIpAddr_Object((1,3,6,1,4,1,35265,125,1,1,2,1,12),_EltexVpcDomainSourceIpAddr_Type())
eltexVpcDomainSourceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainSourceIpAddr.setStatus(_A)
class _EltexVpcDomainDcpdpUdpPort_Type(Unsigned32):defaultValue=50000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexVpcDomainDcpdpUdpPort_Type.__name__=_E
_EltexVpcDomainDcpdpUdpPort_Object=MibTableColumn
eltexVpcDomainDcpdpUdpPort=_EltexVpcDomainDcpdpUdpPort_Object((1,3,6,1,4,1,35265,125,1,1,2,1,13),_EltexVpcDomainDcpdpUdpPort_Type())
eltexVpcDomainDcpdpUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcDomainDcpdpUdpPort.setStatus(_A)
_EltexVpcDomainStatus_Type=RowStatus
_EltexVpcDomainStatus_Object=MibTableColumn
eltexVpcDomainStatus=_EltexVpcDomainStatus_Object((1,3,6,1,4,1,35265,125,1,1,2,1,14),_EltexVpcDomainStatus_Type())
eltexVpcDomainStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:eltexVpcDomainStatus.setStatus(_A)
_EltexVpcGroupConfigTable_Object=MibTable
eltexVpcGroupConfigTable=_EltexVpcGroupConfigTable_Object((1,3,6,1,4,1,35265,125,1,1,3))
if mibBuilder.loadTexts:eltexVpcGroupConfigTable.setStatus(_A)
_EltexVpcGroupConfigEntry_Object=MibTableRow
eltexVpcGroupConfigEntry=_EltexVpcGroupConfigEntry_Object((1,3,6,1,4,1,35265,125,1,1,3,1))
eltexVpcGroupConfigEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:eltexVpcGroupConfigEntry.setStatus(_A)
class _EltexVpcGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_EltexVpcGroupIndex_Type.__name__=_E
_EltexVpcGroupIndex_Object=MibTableColumn
eltexVpcGroupIndex=_EltexVpcGroupIndex_Object((1,3,6,1,4,1,35265,125,1,1,3,1,1),_EltexVpcGroupIndex_Type())
eltexVpcGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcGroupIndex.setStatus(_A)
class _EltexVpcGroupDomainIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EltexVpcGroupDomainIndex_Type.__name__=_E
_EltexVpcGroupDomainIndex_Object=MibTableColumn
eltexVpcGroupDomainIndex=_EltexVpcGroupDomainIndex_Object((1,3,6,1,4,1,35265,125,1,1,3,1,2),_EltexVpcGroupDomainIndex_Type())
eltexVpcGroupDomainIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcGroupDomainIndex.setStatus(_A)
class _EltexVpcGroupPortChannelIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_EltexVpcGroupPortChannelIfIndex_Type.__name__=_M
_EltexVpcGroupPortChannelIfIndex_Object=MibTableColumn
eltexVpcGroupPortChannelIfIndex=_EltexVpcGroupPortChannelIfIndex_Object((1,3,6,1,4,1,35265,125,1,1,3,1,3),_EltexVpcGroupPortChannelIfIndex_Type())
eltexVpcGroupPortChannelIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexVpcGroupPortChannelIfIndex.setStatus(_A)
class _EltexVpcGroupOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_EltexVpcGroupOperationalStatus_Type.__name__=_D
_EltexVpcGroupOperationalStatus_Object=MibTableColumn
eltexVpcGroupOperationalStatus=_EltexVpcGroupOperationalStatus_Object((1,3,6,1,4,1,35265,125,1,1,3,1,4),_EltexVpcGroupOperationalStatus_Type())
eltexVpcGroupOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcGroupOperationalStatus.setStatus(_A)
class _EltexVpcGroupInterfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('wait',2),('error',3),('active',4),('inactive',5)))
_EltexVpcGroupInterfaceState_Type.__name__=_D
_EltexVpcGroupInterfaceState_Object=MibTableColumn
eltexVpcGroupInterfaceState=_EltexVpcGroupInterfaceState_Object((1,3,6,1,4,1,35265,125,1,1,3,1,5),_EltexVpcGroupInterfaceState_Type())
eltexVpcGroupInterfaceState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcGroupInterfaceState.setStatus(_A)
_EltexVpcGroupStatus_Type=RowStatus
_EltexVpcGroupStatus_Object=MibTableColumn
eltexVpcGroupStatus=_EltexVpcGroupStatus_Object((1,3,6,1,4,1,35265,125,1,1,3,1,6),_EltexVpcGroupStatus_Type())
eltexVpcGroupStatus.setMaxAccess(_O)
if mibBuilder.loadTexts:eltexVpcGroupStatus.setStatus(_A)
_EltexVpcStatusGroup_ObjectIdentity=ObjectIdentity
eltexVpcStatusGroup=_EltexVpcStatusGroup_ObjectIdentity((1,3,6,1,4,1,35265,125,1,2))
_EltexVpcDomainStatusTable_Object=MibTable
eltexVpcDomainStatusTable=_EltexVpcDomainStatusTable_Object((1,3,6,1,4,1,35265,125,1,2,1))
if mibBuilder.loadTexts:eltexVpcDomainStatusTable.setStatus(_A)
_EltexVpcDomainStatusEntry_Object=MibTableRow
eltexVpcDomainStatusEntry=_EltexVpcDomainStatusEntry_Object((1,3,6,1,4,1,35265,125,1,2,1,1))
eltexVpcDomainStatusEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:eltexVpcDomainStatusEntry.setStatus(_A)
_EltexVpcDomainTotalVpcConfigured_Type=Unsigned32
_EltexVpcDomainTotalVpcConfigured_Object=MibTableColumn
eltexVpcDomainTotalVpcConfigured=_EltexVpcDomainTotalVpcConfigured_Object((1,3,6,1,4,1,35265,125,1,2,1,1,1),_EltexVpcDomainTotalVpcConfigured_Type())
eltexVpcDomainTotalVpcConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainTotalVpcConfigured.setStatus(_A)
_EltexVpcDomainTotalVpcOperational_Type=Unsigned32
_EltexVpcDomainTotalVpcOperational_Object=MibTableColumn
eltexVpcDomainTotalVpcOperational=_EltexVpcDomainTotalVpcOperational_Object((1,3,6,1,4,1,35265,125,1,2,1,1,2),_EltexVpcDomainTotalVpcOperational_Type())
eltexVpcDomainTotalVpcOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainTotalVpcOperational.setStatus(_A)
class _EltexVpcDomainSelfRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_K,2),(_L,3)))
_EltexVpcDomainSelfRole_Type.__name__=_D
_EltexVpcDomainSelfRole_Object=MibTableColumn
eltexVpcDomainSelfRole=_EltexVpcDomainSelfRole_Object((1,3,6,1,4,1,35265,125,1,2,1,1,3),_EltexVpcDomainSelfRole_Type())
eltexVpcDomainSelfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainSelfRole.setStatus(_A)
class _EltexVpcDomainOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_EltexVpcDomainOperationMode_Type.__name__=_D
_EltexVpcDomainOperationMode_Object=MibTableColumn
eltexVpcDomainOperationMode=_EltexVpcDomainOperationMode_Object((1,3,6,1,4,1,35265,125,1,2,1,1,4),_EltexVpcDomainOperationMode_Type())
eltexVpcDomainOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainOperationMode.setStatus(_A)
class _EltexVpcDomainState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('listen',2),('ready',3),(_K,4),(_L,5)))
_EltexVpcDomainState_Type.__name__=_D
_EltexVpcDomainState_Object=MibTableColumn
eltexVpcDomainState=_EltexVpcDomainState_Object((1,3,6,1,4,1,35265,125,1,2,1,1,5),_EltexVpcDomainState_Type())
eltexVpcDomainState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainState.setStatus(_A)
class _EltexVpcDomainOperationalSystemPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexVpcDomainOperationalSystemPriority_Type.__name__=_E
_EltexVpcDomainOperationalSystemPriority_Object=MibTableColumn
eltexVpcDomainOperationalSystemPriority=_EltexVpcDomainOperationalSystemPriority_Object((1,3,6,1,4,1,35265,125,1,2,1,1,6),_EltexVpcDomainOperationalSystemPriority_Type())
eltexVpcDomainOperationalSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainOperationalSystemPriority.setStatus(_A)
_EltexVpcDomainOperationalMac_Type=MacAddress
_EltexVpcDomainOperationalMac_Object=MibTableColumn
eltexVpcDomainOperationalMac=_EltexVpcDomainOperationalMac_Object((1,3,6,1,4,1,35265,125,1,2,1,1,7),_EltexVpcDomainOperationalMac_Type())
eltexVpcDomainOperationalMac.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainOperationalMac.setStatus(_A)
_EltexVpcDomainLocalSystemMac_Type=MacAddress
_EltexVpcDomainLocalSystemMac_Object=MibTableColumn
eltexVpcDomainLocalSystemMac=_EltexVpcDomainLocalSystemMac_Object((1,3,6,1,4,1,35265,125,1,2,1,1,8),_EltexVpcDomainLocalSystemMac_Type())
eltexVpcDomainLocalSystemMac.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainLocalSystemMac.setStatus(_A)
class _EltexVpcDomainPeerRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_K,2),(_L,3)))
_EltexVpcDomainPeerRole_Type.__name__=_D
_EltexVpcDomainPeerRole_Object=MibTableColumn
eltexVpcDomainPeerRole=_EltexVpcDomainPeerRole_Object((1,3,6,1,4,1,35265,125,1,2,1,1,9),_EltexVpcDomainPeerRole_Type())
eltexVpcDomainPeerRole.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerRole.setStatus(_A)
_EltexVpcDomainPeerRolePriority_Type=Unsigned32
_EltexVpcDomainPeerRolePriority_Object=MibTableColumn
eltexVpcDomainPeerRolePriority=_EltexVpcDomainPeerRolePriority_Object((1,3,6,1,4,1,35265,125,1,2,1,1,10),_EltexVpcDomainPeerRolePriority_Type())
eltexVpcDomainPeerRolePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerRolePriority.setStatus(_A)
_EltexVpcDomainPeerConfSystemPriority_Type=Unsigned32
_EltexVpcDomainPeerConfSystemPriority_Object=MibTableColumn
eltexVpcDomainPeerConfSystemPriority=_EltexVpcDomainPeerConfSystemPriority_Object((1,3,6,1,4,1,35265,125,1,2,1,1,11),_EltexVpcDomainPeerConfSystemPriority_Type())
eltexVpcDomainPeerConfSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerConfSystemPriority.setStatus(_A)
_EltexVpcDomainPeerOperSystemPriority_Type=Unsigned32
_EltexVpcDomainPeerOperSystemPriority_Object=MibTableColumn
eltexVpcDomainPeerOperSystemPriority=_EltexVpcDomainPeerOperSystemPriority_Object((1,3,6,1,4,1,35265,125,1,2,1,1,12),_EltexVpcDomainPeerOperSystemPriority_Type())
eltexVpcDomainPeerOperSystemPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerOperSystemPriority.setStatus(_A)
_EltexVpcDomainPeerConfMac_Type=MacAddress
_EltexVpcDomainPeerConfMac_Object=MibTableColumn
eltexVpcDomainPeerConfMac=_EltexVpcDomainPeerConfMac_Object((1,3,6,1,4,1,35265,125,1,2,1,1,13),_EltexVpcDomainPeerConfMac_Type())
eltexVpcDomainPeerConfMac.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerConfMac.setStatus(_A)
_EltexVpcDomainPeerOperMac_Type=MacAddress
_EltexVpcDomainPeerOperMac_Object=MibTableColumn
eltexVpcDomainPeerOperMac=_EltexVpcDomainPeerOperMac_Object((1,3,6,1,4,1,35265,125,1,2,1,1,14),_EltexVpcDomainPeerOperMac_Type())
eltexVpcDomainPeerOperMac.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerOperMac.setStatus(_A)
_EltexVpcDomainPeerLocalSystemMac_Type=MacAddress
_EltexVpcDomainPeerLocalSystemMac_Object=MibTableColumn
eltexVpcDomainPeerLocalSystemMac=_EltexVpcDomainPeerLocalSystemMac_Object((1,3,6,1,4,1,35265,125,1,2,1,1,15),_EltexVpcDomainPeerLocalSystemMac_Type())
eltexVpcDomainPeerLocalSystemMac.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLocalSystemMac.setStatus(_A)
_EltexVpcDomainPeerKeepaliveDetected_Type=TruthValue
_EltexVpcDomainPeerKeepaliveDetected_Object=MibTableColumn
eltexVpcDomainPeerKeepaliveDetected=_EltexVpcDomainPeerKeepaliveDetected_Object((1,3,6,1,4,1,35265,125,1,2,1,1,16),_EltexVpcDomainPeerKeepaliveDetected_Type())
eltexVpcDomainPeerKeepaliveDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepaliveDetected.setStatus(_A)
_EltexVpcDomainPeerDetectionStatus_Type=TruthValue
_EltexVpcDomainPeerDetectionStatus_Object=MibTableColumn
eltexVpcDomainPeerDetectionStatus=_EltexVpcDomainPeerDetectionStatus_Object((1,3,6,1,4,1,35265,125,1,2,1,1,17),_EltexVpcDomainPeerDetectionStatus_Type())
eltexVpcDomainPeerDetectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionStatus.setStatus(_A)
_EltexVpcDomainPeerDetectionDetected_Type=TruthValue
_EltexVpcDomainPeerDetectionDetected_Object=MibTableColumn
eltexVpcDomainPeerDetectionDetected=_EltexVpcDomainPeerDetectionDetected_Object((1,3,6,1,4,1,35265,125,1,2,1,1,18),_EltexVpcDomainPeerDetectionDetected_Type())
eltexVpcDomainPeerDetectionDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionDetected.setStatus(_A)
_EltexVpcDomainPeerKeepAliveStatsTable_Object=MibTable
eltexVpcDomainPeerKeepAliveStatsTable=_EltexVpcDomainPeerKeepAliveStatsTable_Object((1,3,6,1,4,1,35265,125,1,2,2))
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveStatsTable.setStatus(_A)
_EltexVpcDomainPeerKeepAliveStatsEntry_Object=MibTableRow
eltexVpcDomainPeerKeepAliveStatsEntry=_EltexVpcDomainPeerKeepAliveStatsEntry_Object((1,3,6,1,4,1,35265,125,1,2,2,1))
eltexVpcDomainPeerKeepAliveStatsEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveStatsEntry.setStatus(_A)
class _EltexVpcDomainKeepaliveOperationalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_G,2)))
_EltexVpcDomainKeepaliveOperationalMode_Type.__name__=_D
_EltexVpcDomainKeepaliveOperationalMode_Object=MibTableColumn
eltexVpcDomainKeepaliveOperationalMode=_EltexVpcDomainKeepaliveOperationalMode_Object((1,3,6,1,4,1,35265,125,1,2,2,1,1),_EltexVpcDomainKeepaliveOperationalMode_Type())
eltexVpcDomainKeepaliveOperationalMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainKeepaliveOperationalMode.setStatus(_A)
_EltexVpcDomainPeerKeepAliveTotalTx_Type=Unsigned32
_EltexVpcDomainPeerKeepAliveTotalTx_Object=MibTableColumn
eltexVpcDomainPeerKeepAliveTotalTx=_EltexVpcDomainPeerKeepAliveTotalTx_Object((1,3,6,1,4,1,35265,125,1,2,2,1,2),_EltexVpcDomainPeerKeepAliveTotalTx_Type())
eltexVpcDomainPeerKeepAliveTotalTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveTotalTx.setStatus(_A)
_EltexVpcDomainPeerKeepAliveSuccessTx_Type=Unsigned32
_EltexVpcDomainPeerKeepAliveSuccessTx_Object=MibTableColumn
eltexVpcDomainPeerKeepAliveSuccessTx=_EltexVpcDomainPeerKeepAliveSuccessTx_Object((1,3,6,1,4,1,35265,125,1,2,2,1,3),_EltexVpcDomainPeerKeepAliveSuccessTx_Type())
eltexVpcDomainPeerKeepAliveSuccessTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveSuccessTx.setStatus(_A)
_EltexVpcDomainPeerKeepAliveTxErrors_Type=Unsigned32
_EltexVpcDomainPeerKeepAliveTxErrors_Object=MibTableColumn
eltexVpcDomainPeerKeepAliveTxErrors=_EltexVpcDomainPeerKeepAliveTxErrors_Object((1,3,6,1,4,1,35265,125,1,2,2,1,4),_EltexVpcDomainPeerKeepAliveTxErrors_Type())
eltexVpcDomainPeerKeepAliveTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveTxErrors.setStatus(_A)
_EltexVpcDomainPeerKeepAliveTotalRx_Type=Unsigned32
_EltexVpcDomainPeerKeepAliveTotalRx_Object=MibTableColumn
eltexVpcDomainPeerKeepAliveTotalRx=_EltexVpcDomainPeerKeepAliveTotalRx_Object((1,3,6,1,4,1,35265,125,1,2,2,1,5),_EltexVpcDomainPeerKeepAliveTotalRx_Type())
eltexVpcDomainPeerKeepAliveTotalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveTotalRx.setStatus(_A)
_EltexVpcDomainPeerKeepAliveSuccessRx_Type=Unsigned32
_EltexVpcDomainPeerKeepAliveSuccessRx_Object=MibTableColumn
eltexVpcDomainPeerKeepAliveSuccessRx=_EltexVpcDomainPeerKeepAliveSuccessRx_Object((1,3,6,1,4,1,35265,125,1,2,2,1,6),_EltexVpcDomainPeerKeepAliveSuccessRx_Type())
eltexVpcDomainPeerKeepAliveSuccessRx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveSuccessRx.setStatus(_A)
_EltexVpcDomainPeerKeepAliveRxErrors_Type=Unsigned32
_EltexVpcDomainPeerKeepAliveRxErrors_Object=MibTableColumn
eltexVpcDomainPeerKeepAliveRxErrors=_EltexVpcDomainPeerKeepAliveRxErrors_Object((1,3,6,1,4,1,35265,125,1,2,2,1,7),_EltexVpcDomainPeerKeepAliveRxErrors_Type())
eltexVpcDomainPeerKeepAliveRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveRxErrors.setStatus(_A)
_EltexVpcDomainPeerKeepAliveTimeoutCount_Type=Unsigned32
_EltexVpcDomainPeerKeepAliveTimeoutCount_Object=MibTableColumn
eltexVpcDomainPeerKeepAliveTimeoutCount=_EltexVpcDomainPeerKeepAliveTimeoutCount_Object((1,3,6,1,4,1,35265,125,1,2,2,1,8),_EltexVpcDomainPeerKeepAliveTimeoutCount_Type())
eltexVpcDomainPeerKeepAliveTimeoutCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerKeepAliveTimeoutCount.setStatus(_A)
_EltexVpcDomainPeerLinkStatsTable_Object=MibTable
eltexVpcDomainPeerLinkStatsTable=_EltexVpcDomainPeerLinkStatsTable_Object((1,3,6,1,4,1,35265,125,1,2,3))
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkStatsTable.setStatus(_A)
_EltexVpcDomainLinkStatsEntry_Object=MibTableRow
eltexVpcDomainLinkStatsEntry=_EltexVpcDomainLinkStatsEntry_Object((1,3,6,1,4,1,35265,125,1,2,3,1))
eltexVpcDomainLinkStatsEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:eltexVpcDomainLinkStatsEntry.setStatus(_A)
_EltexVpcDomainPeerLinkStatus_Type=TruthValue
_EltexVpcDomainPeerLinkStatus_Object=MibTableColumn
eltexVpcDomainPeerLinkStatus=_EltexVpcDomainPeerLinkStatus_Object((1,3,6,1,4,1,35265,125,1,2,3,1,2),_EltexVpcDomainPeerLinkStatus_Type())
eltexVpcDomainPeerLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkStatus.setStatus(_A)
_EltexVpcDomainPeerLinkControlMsgTx_Type=Unsigned32
_EltexVpcDomainPeerLinkControlMsgTx_Object=MibTableColumn
eltexVpcDomainPeerLinkControlMsgTx=_EltexVpcDomainPeerLinkControlMsgTx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,3),_EltexVpcDomainPeerLinkControlMsgTx_Type())
eltexVpcDomainPeerLinkControlMsgTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkControlMsgTx.setStatus(_A)
_EltexVpcDomainPeerLinkTxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkTxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkTxErrors=_EltexVpcDomainPeerLinkTxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,4),_EltexVpcDomainPeerLinkTxErrors_Type())
eltexVpcDomainPeerLinkTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkTxErrors.setStatus(_A)
_EltexVpcDomainPeerLinkTxTimeout_Type=Unsigned32
_EltexVpcDomainPeerLinkTxTimeout_Object=MibTableColumn
eltexVpcDomainPeerLinkTxTimeout=_EltexVpcDomainPeerLinkTxTimeout_Object((1,3,6,1,4,1,35265,125,1,2,3,1,5),_EltexVpcDomainPeerLinkTxTimeout_Type())
eltexVpcDomainPeerLinkTxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkTxTimeout.setStatus(_A)
_EltexVpcDomainPeerLinkControlMsgAckTx_Type=Unsigned32
_EltexVpcDomainPeerLinkControlMsgAckTx_Object=MibTableColumn
eltexVpcDomainPeerLinkControlMsgAckTx=_EltexVpcDomainPeerLinkControlMsgAckTx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,6),_EltexVpcDomainPeerLinkControlMsgAckTx_Type())
eltexVpcDomainPeerLinkControlMsgAckTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkControlMsgAckTx.setStatus(_A)
_EltexVpcDomainPeerLinkControlMsgAckErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkControlMsgAckErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkControlMsgAckErrors=_EltexVpcDomainPeerLinkControlMsgAckErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,7),_EltexVpcDomainPeerLinkControlMsgAckErrors_Type())
eltexVpcDomainPeerLinkControlMsgAckErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkControlMsgAckErrors.setStatus(_A)
_EltexVpcDomainPeerLinkControlMsgRx_Type=Unsigned32
_EltexVpcDomainPeerLinkControlMsgRx_Object=MibTableColumn
eltexVpcDomainPeerLinkControlMsgRx=_EltexVpcDomainPeerLinkControlMsgRx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,8),_EltexVpcDomainPeerLinkControlMsgRx_Type())
eltexVpcDomainPeerLinkControlMsgRx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkControlMsgRx.setStatus(_A)
_EltexVpcDomainPeerLinkDataMsgTx_Type=Unsigned32
_EltexVpcDomainPeerLinkDataMsgTx_Object=MibTableColumn
eltexVpcDomainPeerLinkDataMsgTx=_EltexVpcDomainPeerLinkDataMsgTx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,9),_EltexVpcDomainPeerLinkDataMsgTx_Type())
eltexVpcDomainPeerLinkDataMsgTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkDataMsgTx.setStatus(_A)
_EltexVpcDomainPeerLinkDataMsgTxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkDataMsgTxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkDataMsgTxErrors=_EltexVpcDomainPeerLinkDataMsgTxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,10),_EltexVpcDomainPeerLinkDataMsgTxErrors_Type())
eltexVpcDomainPeerLinkDataMsgTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkDataMsgTxErrors.setStatus(_A)
_EltexVpcDomainPeerLinkDataMsgTxTimeout_Type=Unsigned32
_EltexVpcDomainPeerLinkDataMsgTxTimeout_Object=MibTableColumn
eltexVpcDomainPeerLinkDataMsgTxTimeout=_EltexVpcDomainPeerLinkDataMsgTxTimeout_Object((1,3,6,1,4,1,35265,125,1,2,3,1,11),_EltexVpcDomainPeerLinkDataMsgTxTimeout_Type())
eltexVpcDomainPeerLinkDataMsgTxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkDataMsgTxTimeout.setStatus(_A)
_EltexVpcDomainPeerLinkDataMsgRx_Type=Unsigned32
_EltexVpcDomainPeerLinkDataMsgRx_Object=MibTableColumn
eltexVpcDomainPeerLinkDataMsgRx=_EltexVpcDomainPeerLinkDataMsgRx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,12),_EltexVpcDomainPeerLinkDataMsgRx_Type())
eltexVpcDomainPeerLinkDataMsgRx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkDataMsgRx.setStatus(_A)
_EltexVpcDomainPeerLinkBPDUTx_Type=Unsigned32
_EltexVpcDomainPeerLinkBPDUTx_Object=MibTableColumn
eltexVpcDomainPeerLinkBPDUTx=_EltexVpcDomainPeerLinkBPDUTx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,13),_EltexVpcDomainPeerLinkBPDUTx_Type())
eltexVpcDomainPeerLinkBPDUTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBPDUTx.setStatus(_A)
_EltexVpcDomainPeerLinkBPDUTxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkBPDUTxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkBPDUTxErrors=_EltexVpcDomainPeerLinkBPDUTxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,14),_EltexVpcDomainPeerLinkBPDUTxErrors_Type())
eltexVpcDomainPeerLinkBPDUTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBPDUTxErrors.setStatus(_A)
_EltexVpcDomainPeerLinkBPDURx_Type=Unsigned32
_EltexVpcDomainPeerLinkBPDURx_Object=MibTableColumn
eltexVpcDomainPeerLinkBPDURx=_EltexVpcDomainPeerLinkBPDURx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,15),_EltexVpcDomainPeerLinkBPDURx_Type())
eltexVpcDomainPeerLinkBPDURx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBPDURx.setStatus(_A)
_EltexVpcDomainPeerLinkBPDURxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkBPDURxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkBPDURxErrors=_EltexVpcDomainPeerLinkBPDURxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,16),_EltexVpcDomainPeerLinkBPDURxErrors_Type())
eltexVpcDomainPeerLinkBPDURxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBPDURxErrors.setStatus(_A)
_EltexVpcDomainPeerLinkLACPDUTx_Type=Unsigned32
_EltexVpcDomainPeerLinkLACPDUTx_Object=MibTableColumn
eltexVpcDomainPeerLinkLACPDUTx=_EltexVpcDomainPeerLinkLACPDUTx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,17),_EltexVpcDomainPeerLinkLACPDUTx_Type())
eltexVpcDomainPeerLinkLACPDUTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkLACPDUTx.setStatus(_A)
_EltexVpcDomainPeerLinkLACPDUTxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkLACPDUTxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkLACPDUTxErrors=_EltexVpcDomainPeerLinkLACPDUTxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,18),_EltexVpcDomainPeerLinkLACPDUTxErrors_Type())
eltexVpcDomainPeerLinkLACPDUTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkLACPDUTxErrors.setStatus(_A)
_EltexVpcDomainPeerLinkLACPDURx_Type=Unsigned32
_EltexVpcDomainPeerLinkLACPDURx_Object=MibTableColumn
eltexVpcDomainPeerLinkLACPDURx=_EltexVpcDomainPeerLinkLACPDURx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,19),_EltexVpcDomainPeerLinkLACPDURx_Type())
eltexVpcDomainPeerLinkLACPDURx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkLACPDURx.setStatus(_A)
_EltexVpcDomainPeerLinkLACPDURxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkLACPDURxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkLACPDURxErrors=_EltexVpcDomainPeerLinkLACPDURxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,20),_EltexVpcDomainPeerLinkLACPDURxErrors_Type())
eltexVpcDomainPeerLinkLACPDURxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkLACPDURxErrors.setStatus(_A)
_EltexVpcDomainPeerLinkBulkTx_Type=Unsigned32
_EltexVpcDomainPeerLinkBulkTx_Object=MibTableColumn
eltexVpcDomainPeerLinkBulkTx=_EltexVpcDomainPeerLinkBulkTx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,21),_EltexVpcDomainPeerLinkBulkTx_Type())
eltexVpcDomainPeerLinkBulkTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBulkTx.setStatus(_A)
_EltexVpcDomainPeerLinkBulkTxTimeout_Type=Unsigned32
_EltexVpcDomainPeerLinkBulkTxTimeout_Object=MibTableColumn
eltexVpcDomainPeerLinkBulkTxTimeout=_EltexVpcDomainPeerLinkBulkTxTimeout_Object((1,3,6,1,4,1,35265,125,1,2,3,1,22),_EltexVpcDomainPeerLinkBulkTxTimeout_Type())
eltexVpcDomainPeerLinkBulkTxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBulkTxTimeout.setStatus(_A)
_EltexVpcDomainPeerLinkBulkTxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkBulkTxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkBulkTxErrors=_EltexVpcDomainPeerLinkBulkTxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,23),_EltexVpcDomainPeerLinkBulkTxErrors_Type())
eltexVpcDomainPeerLinkBulkTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBulkTxErrors.setStatus(_A)
_EltexVpcDomainPeerLinkBulkRx_Type=Unsigned32
_EltexVpcDomainPeerLinkBulkRx_Object=MibTableColumn
eltexVpcDomainPeerLinkBulkRx=_EltexVpcDomainPeerLinkBulkRx_Object((1,3,6,1,4,1,35265,125,1,2,3,1,24),_EltexVpcDomainPeerLinkBulkRx_Type())
eltexVpcDomainPeerLinkBulkRx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBulkRx.setStatus(_A)
_EltexVpcDomainPeerLinkBulkRxErrors_Type=Unsigned32
_EltexVpcDomainPeerLinkBulkRxErrors_Object=MibTableColumn
eltexVpcDomainPeerLinkBulkRxErrors=_EltexVpcDomainPeerLinkBulkRxErrors_Object((1,3,6,1,4,1,35265,125,1,2,3,1,25),_EltexVpcDomainPeerLinkBulkRxErrors_Type())
eltexVpcDomainPeerLinkBulkRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerLinkBulkRxErrors.setStatus(_A)
_EltexVpcDomainPeerDetectionStatsTable_Object=MibTable
eltexVpcDomainPeerDetectionStatsTable=_EltexVpcDomainPeerDetectionStatsTable_Object((1,3,6,1,4,1,35265,125,1,2,4))
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionStatsTable.setStatus(_A)
_EltexVpcDomainPeerDetectionStatsEntry_Object=MibTableRow
eltexVpcDomainPeerDetectionStatsEntry=_EltexVpcDomainPeerDetectionStatsEntry_Object((1,3,6,1,4,1,35265,125,1,2,4,1))
eltexVpcDomainPeerDetectionStatsEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionStatsEntry.setStatus(_A)
_EltexVpcDomainPeerDetectionEnabled_Type=Unsigned32
_EltexVpcDomainPeerDetectionEnabled_Object=MibTableColumn
eltexVpcDomainPeerDetectionEnabled=_EltexVpcDomainPeerDetectionEnabled_Object((1,3,6,1,4,1,35265,125,1,2,4,1,2),_EltexVpcDomainPeerDetectionEnabled_Type())
eltexVpcDomainPeerDetectionEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionEnabled.setStatus(_A)
_EltexVpcDomainPeerDetectionEnableFailure_Type=Unsigned32
_EltexVpcDomainPeerDetectionEnableFailure_Object=MibTableColumn
eltexVpcDomainPeerDetectionEnableFailure=_EltexVpcDomainPeerDetectionEnableFailure_Object((1,3,6,1,4,1,35265,125,1,2,4,1,3),_EltexVpcDomainPeerDetectionEnableFailure_Type())
eltexVpcDomainPeerDetectionEnableFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionEnableFailure.setStatus(_A)
_EltexVpcDomainPeerDetectionDisabled_Type=Unsigned32
_EltexVpcDomainPeerDetectionDisabled_Object=MibTableColumn
eltexVpcDomainPeerDetectionDisabled=_EltexVpcDomainPeerDetectionDisabled_Object((1,3,6,1,4,1,35265,125,1,2,4,1,4),_EltexVpcDomainPeerDetectionDisabled_Type())
eltexVpcDomainPeerDetectionDisabled.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionDisabled.setStatus(_A)
_EltexVpcDomainPeerDetectionPeerTimeout_Type=Unsigned32
_EltexVpcDomainPeerDetectionPeerTimeout_Object=MibTableColumn
eltexVpcDomainPeerDetectionPeerTimeout=_EltexVpcDomainPeerDetectionPeerTimeout_Object((1,3,6,1,4,1,35265,125,1,2,4,1,5),_EltexVpcDomainPeerDetectionPeerTimeout_Type())
eltexVpcDomainPeerDetectionPeerTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionPeerTimeout.setStatus(_A)
_EltexVpcDomainPeerDetectionPeerAdminDisable_Type=Unsigned32
_EltexVpcDomainPeerDetectionPeerAdminDisable_Object=MibTableColumn
eltexVpcDomainPeerDetectionPeerAdminDisable=_EltexVpcDomainPeerDetectionPeerAdminDisable_Object((1,3,6,1,4,1,35265,125,1,2,4,1,6),_EltexVpcDomainPeerDetectionPeerAdminDisable_Type())
eltexVpcDomainPeerDetectionPeerAdminDisable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionPeerAdminDisable.setStatus(_A)
_EltexVpcDomainPeerDetectionTx_Type=Unsigned32
_EltexVpcDomainPeerDetectionTx_Object=MibTableColumn
eltexVpcDomainPeerDetectionTx=_EltexVpcDomainPeerDetectionTx_Object((1,3,6,1,4,1,35265,125,1,2,4,1,7),_EltexVpcDomainPeerDetectionTx_Type())
eltexVpcDomainPeerDetectionTx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionTx.setStatus(_A)
_EltexVpcDomainPeerDetectionTxError_Type=Unsigned32
_EltexVpcDomainPeerDetectionTxError_Object=MibTableColumn
eltexVpcDomainPeerDetectionTxError=_EltexVpcDomainPeerDetectionTxError_Object((1,3,6,1,4,1,35265,125,1,2,4,1,8),_EltexVpcDomainPeerDetectionTxError_Type())
eltexVpcDomainPeerDetectionTxError.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionTxError.setStatus(_A)
_EltexVpcDomainPeerDetectionTxFdMsg_Type=Unsigned32
_EltexVpcDomainPeerDetectionTxFdMsg_Object=MibTableColumn
eltexVpcDomainPeerDetectionTxFdMsg=_EltexVpcDomainPeerDetectionTxFdMsg_Object((1,3,6,1,4,1,35265,125,1,2,4,1,9),_EltexVpcDomainPeerDetectionTxFdMsg_Type())
eltexVpcDomainPeerDetectionTxFdMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionTxFdMsg.setStatus(_A)
_EltexVpcDomainPeerDetectionTxFdAckMsg_Type=Unsigned32
_EltexVpcDomainPeerDetectionTxFdAckMsg_Object=MibTableColumn
eltexVpcDomainPeerDetectionTxFdAckMsg=_EltexVpcDomainPeerDetectionTxFdAckMsg_Object((1,3,6,1,4,1,35265,125,1,2,4,1,10),_EltexVpcDomainPeerDetectionTxFdAckMsg_Type())
eltexVpcDomainPeerDetectionTxFdAckMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionTxFdAckMsg.setStatus(_A)
_EltexVpcDomainPeerDetectionRx_Type=Unsigned32
_EltexVpcDomainPeerDetectionRx_Object=MibTableColumn
eltexVpcDomainPeerDetectionRx=_EltexVpcDomainPeerDetectionRx_Object((1,3,6,1,4,1,35265,125,1,2,4,1,11),_EltexVpcDomainPeerDetectionRx_Type())
eltexVpcDomainPeerDetectionRx.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionRx.setStatus(_A)
_EltexVpcDomainPeerDetectionRxError_Type=Unsigned32
_EltexVpcDomainPeerDetectionRxError_Object=MibTableColumn
eltexVpcDomainPeerDetectionRxError=_EltexVpcDomainPeerDetectionRxError_Object((1,3,6,1,4,1,35265,125,1,2,4,1,12),_EltexVpcDomainPeerDetectionRxError_Type())
eltexVpcDomainPeerDetectionRxError.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionRxError.setStatus(_A)
_EltexVpcDomainPeerDetectionRxFdMsg_Type=Unsigned32
_EltexVpcDomainPeerDetectionRxFdMsg_Object=MibTableColumn
eltexVpcDomainPeerDetectionRxFdMsg=_EltexVpcDomainPeerDetectionRxFdMsg_Object((1,3,6,1,4,1,35265,125,1,2,4,1,13),_EltexVpcDomainPeerDetectionRxFdMsg_Type())
eltexVpcDomainPeerDetectionRxFdMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionRxFdMsg.setStatus(_A)
_EltexVpcDomainPeerDetectionRxFdAckMsg_Type=Unsigned32
_EltexVpcDomainPeerDetectionRxFdAckMsg_Object=MibTableColumn
eltexVpcDomainPeerDetectionRxFdAckMsg=_EltexVpcDomainPeerDetectionRxFdAckMsg_Object((1,3,6,1,4,1,35265,125,1,2,4,1,14),_EltexVpcDomainPeerDetectionRxFdAckMsg_Type())
eltexVpcDomainPeerDetectionRxFdAckMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcDomainPeerDetectionRxFdAckMsg.setStatus(_A)
_EltexVpcMemberStatusTable_Object=MibTable
eltexVpcMemberStatusTable=_EltexVpcMemberStatusTable_Object((1,3,6,1,4,1,35265,125,1,2,5))
if mibBuilder.loadTexts:eltexVpcMemberStatusTable.setStatus(_A)
_EltexVpcMemberStatusEntry_Object=MibTableRow
eltexVpcMemberStatusEntry=_EltexVpcMemberStatusEntry_Object((1,3,6,1,4,1,35265,125,1,2,5,1))
eltexVpcMemberStatusEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:eltexVpcMemberStatusEntry.setStatus(_A)
class _EltexVpcMemberStatusVpcGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_EltexVpcMemberStatusVpcGroupIndex_Type.__name__=_E
_EltexVpcMemberStatusVpcGroupIndex_Object=MibTableColumn
eltexVpcMemberStatusVpcGroupIndex=_EltexVpcMemberStatusVpcGroupIndex_Object((1,3,6,1,4,1,35265,125,1,2,5,1,1),_EltexVpcMemberStatusVpcGroupIndex_Type())
eltexVpcMemberStatusVpcGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcMemberStatusVpcGroupIndex.setStatus(_A)
_EltexVpcMemberStatusIfIndex_Type=InterfaceIndexOrZero
_EltexVpcMemberStatusIfIndex_Object=MibTableColumn
eltexVpcMemberStatusIfIndex=_EltexVpcMemberStatusIfIndex_Object((1,3,6,1,4,1,35265,125,1,2,5,1,2),_EltexVpcMemberStatusIfIndex_Type())
eltexVpcMemberStatusIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcMemberStatusIfIndex.setStatus(_A)
class _EltexVpcSelfMemberStatusIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_S,3)))
_EltexVpcSelfMemberStatusIntfState_Type.__name__=_D
_EltexVpcSelfMemberStatusIntfState_Object=MibTableColumn
eltexVpcSelfMemberStatusIntfState=_EltexVpcSelfMemberStatusIntfState_Object((1,3,6,1,4,1,35265,125,1,2,5,1,3),_EltexVpcSelfMemberStatusIntfState_Type())
eltexVpcSelfMemberStatusIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcSelfMemberStatusIntfState.setStatus(_A)
class _EltexVpcPeerMemberStatusIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_S,3)))
_EltexVpcPeerMemberStatusIntfState_Type.__name__=_D
_EltexVpcPeerMemberStatusIntfState_Object=MibTableColumn
eltexVpcPeerMemberStatusIntfState=_EltexVpcPeerMemberStatusIntfState_Object((1,3,6,1,4,1,35265,125,1,2,5,1,4),_EltexVpcPeerMemberStatusIntfState_Type())
eltexVpcPeerMemberStatusIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:eltexVpcPeerMemberStatusIntfState.setStatus(_A)
_EltexVpcMIBNotification_ObjectIdentity=ObjectIdentity
eltexVpcMIBNotification=_EltexVpcMIBNotification_ObjectIdentity((1,3,6,1,4,1,35265,125,2))
mibBuilder.exportSymbols(_F,**{'eltexVpcMIB':eltexVpcMIB,'eltexVpcMIBObjects':eltexVpcMIBObjects,'eltexVpcConfigGroup':eltexVpcConfigGroup,'eltexVpcMode':eltexVpcMode,'eltexVpcDomainConfigTable':eltexVpcDomainConfigTable,'eltexVpcDomainConfigEntry':eltexVpcDomainConfigEntry,_I:eltexVpcDomainIndex,'eltexVpcDomainPeerLink':eltexVpcDomainPeerLink,'eltexVpcDomainKeepalivePriority':eltexVpcDomainKeepalivePriority,'eltexVpcDomainKeepaliveTimeout':eltexVpcDomainKeepaliveTimeout,'eltexVpcDomainKeepaliveMode':eltexVpcDomainKeepaliveMode,'eltexVpcDomainSystemMac':eltexVpcDomainSystemMac,'eltexVpcDomainSystemPriority':eltexVpcDomainSystemPriority,'eltexVpcDomainPeerDetectionMode':eltexVpcDomainPeerDetectionMode,'eltexVpcDomainPeerDetectionInterval':eltexVpcDomainPeerDetectionInterval,'eltexVpcDomainPeerDetectionTimeout':eltexVpcDomainPeerDetectionTimeout,'eltexVpcDomainPeerIpAddr':eltexVpcDomainPeerIpAddr,'eltexVpcDomainSourceIpAddr':eltexVpcDomainSourceIpAddr,'eltexVpcDomainDcpdpUdpPort':eltexVpcDomainDcpdpUdpPort,'eltexVpcDomainStatus':eltexVpcDomainStatus,'eltexVpcGroupConfigTable':eltexVpcGroupConfigTable,'eltexVpcGroupConfigEntry':eltexVpcGroupConfigEntry,_P:eltexVpcGroupIndex,'eltexVpcGroupDomainIndex':eltexVpcGroupDomainIndex,'eltexVpcGroupPortChannelIfIndex':eltexVpcGroupPortChannelIfIndex,'eltexVpcGroupOperationalStatus':eltexVpcGroupOperationalStatus,'eltexVpcGroupInterfaceState':eltexVpcGroupInterfaceState,'eltexVpcGroupStatus':eltexVpcGroupStatus,'eltexVpcStatusGroup':eltexVpcStatusGroup,'eltexVpcDomainStatusTable':eltexVpcDomainStatusTable,'eltexVpcDomainStatusEntry':eltexVpcDomainStatusEntry,'eltexVpcDomainTotalVpcConfigured':eltexVpcDomainTotalVpcConfigured,'eltexVpcDomainTotalVpcOperational':eltexVpcDomainTotalVpcOperational,'eltexVpcDomainSelfRole':eltexVpcDomainSelfRole,'eltexVpcDomainOperationMode':eltexVpcDomainOperationMode,'eltexVpcDomainState':eltexVpcDomainState,'eltexVpcDomainOperationalSystemPriority':eltexVpcDomainOperationalSystemPriority,'eltexVpcDomainOperationalMac':eltexVpcDomainOperationalMac,'eltexVpcDomainLocalSystemMac':eltexVpcDomainLocalSystemMac,'eltexVpcDomainPeerRole':eltexVpcDomainPeerRole,'eltexVpcDomainPeerRolePriority':eltexVpcDomainPeerRolePriority,'eltexVpcDomainPeerConfSystemPriority':eltexVpcDomainPeerConfSystemPriority,'eltexVpcDomainPeerOperSystemPriority':eltexVpcDomainPeerOperSystemPriority,'eltexVpcDomainPeerConfMac':eltexVpcDomainPeerConfMac,'eltexVpcDomainPeerOperMac':eltexVpcDomainPeerOperMac,'eltexVpcDomainPeerLocalSystemMac':eltexVpcDomainPeerLocalSystemMac,'eltexVpcDomainPeerKeepaliveDetected':eltexVpcDomainPeerKeepaliveDetected,'eltexVpcDomainPeerDetectionStatus':eltexVpcDomainPeerDetectionStatus,'eltexVpcDomainPeerDetectionDetected':eltexVpcDomainPeerDetectionDetected,'eltexVpcDomainPeerKeepAliveStatsTable':eltexVpcDomainPeerKeepAliveStatsTable,'eltexVpcDomainPeerKeepAliveStatsEntry':eltexVpcDomainPeerKeepAliveStatsEntry,'eltexVpcDomainKeepaliveOperationalMode':eltexVpcDomainKeepaliveOperationalMode,'eltexVpcDomainPeerKeepAliveTotalTx':eltexVpcDomainPeerKeepAliveTotalTx,'eltexVpcDomainPeerKeepAliveSuccessTx':eltexVpcDomainPeerKeepAliveSuccessTx,'eltexVpcDomainPeerKeepAliveTxErrors':eltexVpcDomainPeerKeepAliveTxErrors,'eltexVpcDomainPeerKeepAliveTotalRx':eltexVpcDomainPeerKeepAliveTotalRx,'eltexVpcDomainPeerKeepAliveSuccessRx':eltexVpcDomainPeerKeepAliveSuccessRx,'eltexVpcDomainPeerKeepAliveRxErrors':eltexVpcDomainPeerKeepAliveRxErrors,'eltexVpcDomainPeerKeepAliveTimeoutCount':eltexVpcDomainPeerKeepAliveTimeoutCount,'eltexVpcDomainPeerLinkStatsTable':eltexVpcDomainPeerLinkStatsTable,'eltexVpcDomainLinkStatsEntry':eltexVpcDomainLinkStatsEntry,'eltexVpcDomainPeerLinkStatus':eltexVpcDomainPeerLinkStatus,'eltexVpcDomainPeerLinkControlMsgTx':eltexVpcDomainPeerLinkControlMsgTx,'eltexVpcDomainPeerLinkTxErrors':eltexVpcDomainPeerLinkTxErrors,'eltexVpcDomainPeerLinkTxTimeout':eltexVpcDomainPeerLinkTxTimeout,'eltexVpcDomainPeerLinkControlMsgAckTx':eltexVpcDomainPeerLinkControlMsgAckTx,'eltexVpcDomainPeerLinkControlMsgAckErrors':eltexVpcDomainPeerLinkControlMsgAckErrors,'eltexVpcDomainPeerLinkControlMsgRx':eltexVpcDomainPeerLinkControlMsgRx,'eltexVpcDomainPeerLinkDataMsgTx':eltexVpcDomainPeerLinkDataMsgTx,'eltexVpcDomainPeerLinkDataMsgTxErrors':eltexVpcDomainPeerLinkDataMsgTxErrors,'eltexVpcDomainPeerLinkDataMsgTxTimeout':eltexVpcDomainPeerLinkDataMsgTxTimeout,'eltexVpcDomainPeerLinkDataMsgRx':eltexVpcDomainPeerLinkDataMsgRx,'eltexVpcDomainPeerLinkBPDUTx':eltexVpcDomainPeerLinkBPDUTx,'eltexVpcDomainPeerLinkBPDUTxErrors':eltexVpcDomainPeerLinkBPDUTxErrors,'eltexVpcDomainPeerLinkBPDURx':eltexVpcDomainPeerLinkBPDURx,'eltexVpcDomainPeerLinkBPDURxErrors':eltexVpcDomainPeerLinkBPDURxErrors,'eltexVpcDomainPeerLinkLACPDUTx':eltexVpcDomainPeerLinkLACPDUTx,'eltexVpcDomainPeerLinkLACPDUTxErrors':eltexVpcDomainPeerLinkLACPDUTxErrors,'eltexVpcDomainPeerLinkLACPDURx':eltexVpcDomainPeerLinkLACPDURx,'eltexVpcDomainPeerLinkLACPDURxErrors':eltexVpcDomainPeerLinkLACPDURxErrors,'eltexVpcDomainPeerLinkBulkTx':eltexVpcDomainPeerLinkBulkTx,'eltexVpcDomainPeerLinkBulkTxTimeout':eltexVpcDomainPeerLinkBulkTxTimeout,'eltexVpcDomainPeerLinkBulkTxErrors':eltexVpcDomainPeerLinkBulkTxErrors,'eltexVpcDomainPeerLinkBulkRx':eltexVpcDomainPeerLinkBulkRx,'eltexVpcDomainPeerLinkBulkRxErrors':eltexVpcDomainPeerLinkBulkRxErrors,'eltexVpcDomainPeerDetectionStatsTable':eltexVpcDomainPeerDetectionStatsTable,'eltexVpcDomainPeerDetectionStatsEntry':eltexVpcDomainPeerDetectionStatsEntry,'eltexVpcDomainPeerDetectionEnabled':eltexVpcDomainPeerDetectionEnabled,'eltexVpcDomainPeerDetectionEnableFailure':eltexVpcDomainPeerDetectionEnableFailure,'eltexVpcDomainPeerDetectionDisabled':eltexVpcDomainPeerDetectionDisabled,'eltexVpcDomainPeerDetectionPeerTimeout':eltexVpcDomainPeerDetectionPeerTimeout,'eltexVpcDomainPeerDetectionPeerAdminDisable':eltexVpcDomainPeerDetectionPeerAdminDisable,'eltexVpcDomainPeerDetectionTx':eltexVpcDomainPeerDetectionTx,'eltexVpcDomainPeerDetectionTxError':eltexVpcDomainPeerDetectionTxError,'eltexVpcDomainPeerDetectionTxFdMsg':eltexVpcDomainPeerDetectionTxFdMsg,'eltexVpcDomainPeerDetectionTxFdAckMsg':eltexVpcDomainPeerDetectionTxFdAckMsg,'eltexVpcDomainPeerDetectionRx':eltexVpcDomainPeerDetectionRx,'eltexVpcDomainPeerDetectionRxError':eltexVpcDomainPeerDetectionRxError,'eltexVpcDomainPeerDetectionRxFdMsg':eltexVpcDomainPeerDetectionRxFdMsg,'eltexVpcDomainPeerDetectionRxFdAckMsg':eltexVpcDomainPeerDetectionRxFdAckMsg,'eltexVpcMemberStatusTable':eltexVpcMemberStatusTable,'eltexVpcMemberStatusEntry':eltexVpcMemberStatusEntry,_Q:eltexVpcMemberStatusVpcGroupIndex,_R:eltexVpcMemberStatusIfIndex,'eltexVpcSelfMemberStatusIntfState':eltexVpcSelfMemberStatusIntfState,'eltexVpcPeerMemberStatusIntfState':eltexVpcPeerMemberStatusIntfState,'eltexVpcMIBNotification':eltexVpcMIBNotification})