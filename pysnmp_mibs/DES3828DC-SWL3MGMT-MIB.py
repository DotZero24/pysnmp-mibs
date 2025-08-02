_A1='swL3pimActiveRPGroupAddress'
_A0='swL3pimStaticRPAddress'
_z='swL3pimStaticRPGroupMask'
_y='swL3pimStaticRPGroupAddress'
_x='swL3pimInterface'
_w='swL3SwL3pimRegChksumIncDataRpAddr'
_v='swL3pimCbsrInterface'
_u='swL3ospfAddressLessIf'
_t='swL3ospfIfIpAddress'
_s='0000000000000000'
_r='swL3ospfVirtIfNeighbor'
_q='swL3ospfVirtIfAreaId'
_p='swL3OspfHostTOS'
_o='swL3OspfHostIpAddress'
_n='swL3RouteRedistriDstProtocol'
_m='swL3RouteRedistriSrcProtocol'
_l='swL3Md5KeyId'
_k='swL3RelayDnsCtrlIpAddr'
_j='swL3RelayDnsCtrlDomainName'
_i='swL3RelayBootpCtrlServer'
_h='swL3RelayBootpCtrlInterfaceName'
_g='swL3IpStaticRouteBkupState'
_f='swL3IpStaticRouteMask'
_e='swL3IpStaticRouteDest'
_d='static'
_c='swL3IpFdbInfoIpAddr'
_b='swL3VirtualIpCtrlInterfaceName'
_a='swL3IpCtrlIpAddr'
_Z='TruthValue'
_Y='Unsigned32'
_X='Status'
_W='DesignatedRouterPriority'
_V='AreaID'
_U='00000000'
_T='pointToPoint'
_S='valid'
_R='invalid'
_Q='IpAddress'
_P='HelloRange'
_O='OctetString'
_N='down'
_M='PositiveInteger'
_L='UpToMaxAge'
_K='DisplayString'
_J='not-accessible'
_I='enabled'
_H='disabled'
_G='other'
_F='DES3828DC-SWL3MGMT-MIB'
_E='read-only'
_D='read-write'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
AreaID,DesignatedRouterPriority,HelloRange,Metric,PositiveInteger,RouterID,Status,TOSType,UpToMaxAge=mibBuilder.importSymbols('OSPF-MIB',_V,_W,_P,'Metric',_M,'RouterID',_X,'TOSType',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_Q,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_Y,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention',_Z)
des3828DC,=mibBuilder.importSymbols('SW3800PRIMGMT-MIB','des3828DC')
swL3MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,69,2,3))
class NodeAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class NetAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_SwL3DevMgmt_ObjectIdentity=ObjectIdentity
swL3DevMgmt=_SwL3DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,1))
_SwL3DevCtrl_ObjectIdentity=ObjectIdentity
swL3DevCtrl=_SwL3DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,1,1))
class _SwL3DevCtrlRIPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3DevCtrlRIPState_Type.__name__=_B
_SwL3DevCtrlRIPState_Object=MibScalar
swL3DevCtrlRIPState=_SwL3DevCtrlRIPState_Object((1,3,6,1,4,1,171,11,69,2,3,1,1,1),_SwL3DevCtrlRIPState_Type())
swL3DevCtrlRIPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlRIPState.setStatus(_A)
class _SwL3DevCtrlOSPFState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3DevCtrlOSPFState_Type.__name__=_B
_SwL3DevCtrlOSPFState_Object=MibScalar
swL3DevCtrlOSPFState=_SwL3DevCtrlOSPFState_Object((1,3,6,1,4,1,171,11,69,2,3,1,1,2),_SwL3DevCtrlOSPFState_Type())
swL3DevCtrlOSPFState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlOSPFState.setStatus(_A)
class _SwL3DevCtrlDVMRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3DevCtrlDVMRPState_Type.__name__=_B
_SwL3DevCtrlDVMRPState_Object=MibScalar
swL3DevCtrlDVMRPState=_SwL3DevCtrlDVMRPState_Object((1,3,6,1,4,1,171,11,69,2,3,1,1,3),_SwL3DevCtrlDVMRPState_Type())
swL3DevCtrlDVMRPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlDVMRPState.setStatus(_A)
class _SwL3DevCtrlPIMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3DevCtrlPIMState_Type.__name__=_B
_SwL3DevCtrlPIMState_Object=MibScalar
swL3DevCtrlPIMState=_SwL3DevCtrlPIMState_Object((1,3,6,1,4,1,171,11,69,2,3,1,1,4),_SwL3DevCtrlPIMState_Type())
swL3DevCtrlPIMState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlPIMState.setStatus(_A)
class _SwL3DevCtrlVRRPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3DevCtrlVRRPState_Type.__name__=_B
_SwL3DevCtrlVRRPState_Object=MibScalar
swL3DevCtrlVRRPState=_SwL3DevCtrlVRRPState_Object((1,3,6,1,4,1,171,11,69,2,3,1,1,5),_SwL3DevCtrlVRRPState_Type())
swL3DevCtrlVRRPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlVRRPState.setStatus(_A)
class _SwL3DevCtrlOSPFECMPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3DevCtrlOSPFECMPState_Type.__name__=_B
_SwL3DevCtrlOSPFECMPState_Object=MibScalar
swL3DevCtrlOSPFECMPState=_SwL3DevCtrlOSPFECMPState_Object((1,3,6,1,4,1,171,11,69,2,3,1,1,8),_SwL3DevCtrlOSPFECMPState_Type())
swL3DevCtrlOSPFECMPState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3DevCtrlOSPFECMPState.setStatus(_A)
_SwL3IpMgmt_ObjectIdentity=ObjectIdentity
swL3IpMgmt=_SwL3IpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,2))
_SwL3IpCtrlMgmt_ObjectIdentity=ObjectIdentity
swL3IpCtrlMgmt=_SwL3IpCtrlMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,2,1))
_SwL3IpCtrlTable_Object=MibTable
swL3IpCtrlTable=_SwL3IpCtrlTable_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1))
if mibBuilder.loadTexts:swL3IpCtrlTable.setStatus(_A)
_SwL3IpCtrlEntry_Object=MibTableRow
swL3IpCtrlEntry=_SwL3IpCtrlEntry_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1))
swL3IpCtrlEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:swL3IpCtrlEntry.setStatus(_A)
_SwL3IpCtrlIpAddr_Type=IpAddress
_SwL3IpCtrlIpAddr_Object=MibTableColumn
swL3IpCtrlIpAddr=_SwL3IpCtrlIpAddr_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,1),_SwL3IpCtrlIpAddr_Type())
swL3IpCtrlIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3IpCtrlIpAddr.setStatus(_A)
class _SwL3IpCtrlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpCtrlIfIndex_Type.__name__=_B
_SwL3IpCtrlIfIndex_Object=MibTableColumn
swL3IpCtrlIfIndex=_SwL3IpCtrlIfIndex_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,2),_SwL3IpCtrlIfIndex_Type())
swL3IpCtrlIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlIfIndex.setStatus(_A)
class _SwL3IpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3IpCtrlInterfaceName_Type.__name__=_K
_SwL3IpCtrlInterfaceName_Object=MibTableColumn
swL3IpCtrlInterfaceName=_SwL3IpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,3),_SwL3IpCtrlInterfaceName_Type())
swL3IpCtrlInterfaceName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlInterfaceName.setStatus(_A)
_SwL3IpCtrlIpSubnetMask_Type=IpAddress
_SwL3IpCtrlIpSubnetMask_Object=MibTableColumn
swL3IpCtrlIpSubnetMask=_SwL3IpCtrlIpSubnetMask_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,4),_SwL3IpCtrlIpSubnetMask_Type())
swL3IpCtrlIpSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlIpSubnetMask.setStatus(_A)
class _SwL3IpCtrlVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL3IpCtrlVlanName_Type.__name__=_K
_SwL3IpCtrlVlanName_Object=MibTableColumn
swL3IpCtrlVlanName=_SwL3IpCtrlVlanName_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,5),_SwL3IpCtrlVlanName_Type())
swL3IpCtrlVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlVlanName.setStatus(_A)
class _SwL3IpCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('manual',2),('bootp',3),('dhcp',4)))
_SwL3IpCtrlMode_Type.__name__=_B
_SwL3IpCtrlMode_Object=MibTableColumn
swL3IpCtrlMode=_SwL3IpCtrlMode_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,6),_SwL3IpCtrlMode_Type())
swL3IpCtrlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlMode.setStatus(_A)
_SwL3IpCtrlSecondary_Type=TruthValue
_SwL3IpCtrlSecondary_Object=MibTableColumn
swL3IpCtrlSecondary=_SwL3IpCtrlSecondary_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,7),_SwL3IpCtrlSecondary_Type())
swL3IpCtrlSecondary.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlSecondary.setStatus(_A)
_SwL3IpCtrlState_Type=RowStatus
_SwL3IpCtrlState_Object=MibTableColumn
swL3IpCtrlState=_SwL3IpCtrlState_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,8),_SwL3IpCtrlState_Type())
swL3IpCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlState.setStatus(_A)
class _SwL3IpCtrlOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('up',2),(_N,3)))
_SwL3IpCtrlOperState_Type.__name__=_B
_SwL3IpCtrlOperState_Object=MibTableColumn
swL3IpCtrlOperState=_SwL3IpCtrlOperState_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,9),_SwL3IpCtrlOperState_Type())
swL3IpCtrlOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpCtrlOperState.setStatus(_A)
class _SwL3IpCtrlProxyARPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3IpCtrlProxyARPState_Type.__name__=_B
_SwL3IpCtrlProxyARPState_Object=MibTableColumn
swL3IpCtrlProxyARPState=_SwL3IpCtrlProxyARPState_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,1,1,10),_SwL3IpCtrlProxyARPState_Type())
swL3IpCtrlProxyARPState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpCtrlProxyARPState.setStatus(_A)
_SwL3VirtualIpCtrlTable_Object=MibTable
swL3VirtualIpCtrlTable=_SwL3VirtualIpCtrlTable_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2))
if mibBuilder.loadTexts:swL3VirtualIpCtrlTable.setStatus(_A)
_SwL3VirtualIpCtrlEntry_Object=MibTableRow
swL3VirtualIpCtrlEntry=_SwL3VirtualIpCtrlEntry_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2,1))
swL3VirtualIpCtrlEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:swL3VirtualIpCtrlEntry.setStatus(_A)
class _SwL3VirtualIpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_SwL3VirtualIpCtrlInterfaceName_Type.__name__=_K
_SwL3VirtualIpCtrlInterfaceName_Object=MibTableColumn
swL3VirtualIpCtrlInterfaceName=_SwL3VirtualIpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2,1,1),_SwL3VirtualIpCtrlInterfaceName_Type())
swL3VirtualIpCtrlInterfaceName.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3VirtualIpCtrlInterfaceName.setStatus(_A)
class _SwL3VirtualIpCtrlIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3VirtualIpCtrlIfIndex_Type.__name__=_B
_SwL3VirtualIpCtrlIfIndex_Object=MibTableColumn
swL3VirtualIpCtrlIfIndex=_SwL3VirtualIpCtrlIfIndex_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2,1,2),_SwL3VirtualIpCtrlIfIndex_Type())
swL3VirtualIpCtrlIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VirtualIpCtrlIfIndex.setStatus(_A)
_SwL3VirtualIpCtrlIpAddr_Type=IpAddress
_SwL3VirtualIpCtrlIpAddr_Object=MibTableColumn
swL3VirtualIpCtrlIpAddr=_SwL3VirtualIpCtrlIpAddr_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2,1,3),_SwL3VirtualIpCtrlIpAddr_Type())
swL3VirtualIpCtrlIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VirtualIpCtrlIpAddr.setStatus(_A)
_SwL3VirtualIpCtrlIpSubnetMask_Type=IpAddress
_SwL3VirtualIpCtrlIpSubnetMask_Object=MibTableColumn
swL3VirtualIpCtrlIpSubnetMask=_SwL3VirtualIpCtrlIpSubnetMask_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2,1,4),_SwL3VirtualIpCtrlIpSubnetMask_Type())
swL3VirtualIpCtrlIpSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VirtualIpCtrlIpSubnetMask.setStatus(_A)
class _SwL3VirtualIpCtrlOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('up',2),(_N,3)))
_SwL3VirtualIpCtrlOperState_Type.__name__=_B
_SwL3VirtualIpCtrlOperState_Object=MibTableColumn
swL3VirtualIpCtrlOperState=_SwL3VirtualIpCtrlOperState_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2,1,5),_SwL3VirtualIpCtrlOperState_Type())
swL3VirtualIpCtrlOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3VirtualIpCtrlOperState.setStatus(_A)
_SwL3VirtualIpCtrlState_Type=RowStatus
_SwL3VirtualIpCtrlState_Object=MibTableColumn
swL3VirtualIpCtrlState=_SwL3VirtualIpCtrlState_Object((1,3,6,1,4,1,171,11,69,2,3,2,1,2,1,9),_SwL3VirtualIpCtrlState_Type())
swL3VirtualIpCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3VirtualIpCtrlState.setStatus(_A)
_SwL3IpFdbMgmt_ObjectIdentity=ObjectIdentity
swL3IpFdbMgmt=_SwL3IpFdbMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,2,2))
_SwL3IpFdbInfoTable_Object=MibTable
swL3IpFdbInfoTable=_SwL3IpFdbInfoTable_Object((1,3,6,1,4,1,171,11,69,2,3,2,2,1))
if mibBuilder.loadTexts:swL3IpFdbInfoTable.setStatus(_A)
_SwL3IpFdbInfoEntry_Object=MibTableRow
swL3IpFdbInfoEntry=_SwL3IpFdbInfoEntry_Object((1,3,6,1,4,1,171,11,69,2,3,2,2,1,1))
swL3IpFdbInfoEntry.setIndexNames((0,_F,_c))
if mibBuilder.loadTexts:swL3IpFdbInfoEntry.setStatus(_A)
_SwL3IpFdbInfoIpAddr_Type=IpAddress
_SwL3IpFdbInfoIpAddr_Object=MibTableColumn
swL3IpFdbInfoIpAddr=_SwL3IpFdbInfoIpAddr_Object((1,3,6,1,4,1,171,11,69,2,3,2,2,1,1,1),_SwL3IpFdbInfoIpAddr_Type())
swL3IpFdbInfoIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpFdbInfoIpAddr.setStatus(_A)
_SwL3IpFdbInfoIpSubnetMask_Type=IpAddress
_SwL3IpFdbInfoIpSubnetMask_Object=MibTableColumn
swL3IpFdbInfoIpSubnetMask=_SwL3IpFdbInfoIpSubnetMask_Object((1,3,6,1,4,1,171,11,69,2,3,2,2,1,1,2),_SwL3IpFdbInfoIpSubnetMask_Type())
swL3IpFdbInfoIpSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpFdbInfoIpSubnetMask.setStatus(_A)
class _SwL3IpFdbInfoPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpFdbInfoPort_Type.__name__=_B
_SwL3IpFdbInfoPort_Object=MibTableColumn
swL3IpFdbInfoPort=_SwL3IpFdbInfoPort_Object((1,3,6,1,4,1,171,11,69,2,3,2,2,1,1,3),_SwL3IpFdbInfoPort_Type())
swL3IpFdbInfoPort.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpFdbInfoPort.setStatus(_A)
class _SwL3IpFdbInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_d,2),('dynamic',3)))
_SwL3IpFdbInfoType_Type.__name__=_B
_SwL3IpFdbInfoType_Object=MibTableColumn
swL3IpFdbInfoType=_SwL3IpFdbInfoType_Object((1,3,6,1,4,1,171,11,69,2,3,2,2,1,1,4),_SwL3IpFdbInfoType_Type())
swL3IpFdbInfoType.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpFdbInfoType.setStatus(_A)
class _SwL3IpArpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3IpArpAgingTime_Type.__name__=_B
_SwL3IpArpAgingTime_Object=MibScalar
swL3IpArpAgingTime=_SwL3IpArpAgingTime_Object((1,3,6,1,4,1,171,11,69,2,3,2,4),_SwL3IpArpAgingTime_Type())
swL3IpArpAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3IpArpAgingTime.setStatus(_A)
_SwL3IpStaticRouteTable_Object=MibTable
swL3IpStaticRouteTable=_SwL3IpStaticRouteTable_Object((1,3,6,1,4,1,171,11,69,2,3,2,5))
if mibBuilder.loadTexts:swL3IpStaticRouteTable.setStatus(_A)
_SwL3IpStaticRouteEntry_Object=MibTableRow
swL3IpStaticRouteEntry=_SwL3IpStaticRouteEntry_Object((1,3,6,1,4,1,171,11,69,2,3,2,5,1))
swL3IpStaticRouteEntry.setIndexNames((0,_F,_e),(0,_F,_f),(0,_F,_g))
if mibBuilder.loadTexts:swL3IpStaticRouteEntry.setStatus(_A)
_SwL3IpStaticRouteDest_Type=IpAddress
_SwL3IpStaticRouteDest_Object=MibTableColumn
swL3IpStaticRouteDest=_SwL3IpStaticRouteDest_Object((1,3,6,1,4,1,171,11,69,2,3,2,5,1,1),_SwL3IpStaticRouteDest_Type())
swL3IpStaticRouteDest.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteDest.setStatus(_A)
_SwL3IpStaticRouteMask_Type=IpAddress
_SwL3IpStaticRouteMask_Object=MibTableColumn
swL3IpStaticRouteMask=_SwL3IpStaticRouteMask_Object((1,3,6,1,4,1,171,11,69,2,3,2,5,1,2),_SwL3IpStaticRouteMask_Type())
swL3IpStaticRouteMask.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteMask.setStatus(_A)
class _SwL3IpStaticRouteBkupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_SwL3IpStaticRouteBkupState_Type.__name__=_B
_SwL3IpStaticRouteBkupState_Object=MibTableColumn
swL3IpStaticRouteBkupState=_SwL3IpStaticRouteBkupState_Object((1,3,6,1,4,1,171,11,69,2,3,2,5,1,3),_SwL3IpStaticRouteBkupState_Type())
swL3IpStaticRouteBkupState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3IpStaticRouteBkupState.setStatus(_A)
_SwL3IpStaticRouteNextHop_Type=IpAddress
_SwL3IpStaticRouteNextHop_Object=MibTableColumn
swL3IpStaticRouteNextHop=_SwL3IpStaticRouteNextHop_Object((1,3,6,1,4,1,171,11,69,2,3,2,5,1,4),_SwL3IpStaticRouteNextHop_Type())
swL3IpStaticRouteNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpStaticRouteNextHop.setStatus(_A)
class _SwL3IpStaticRouteMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwL3IpStaticRouteMetric_Type.__name__=_B
_SwL3IpStaticRouteMetric_Object=MibTableColumn
swL3IpStaticRouteMetric=_SwL3IpStaticRouteMetric_Object((1,3,6,1,4,1,171,11,69,2,3,2,5,1,5),_SwL3IpStaticRouteMetric_Type())
swL3IpStaticRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpStaticRouteMetric.setStatus(_A)
class _SwL3IpStaticRouteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_R,2),(_S,3)))
_SwL3IpStaticRouteStatus_Type.__name__=_B
_SwL3IpStaticRouteStatus_Object=MibTableColumn
swL3IpStaticRouteStatus=_SwL3IpStaticRouteStatus_Object((1,3,6,1,4,1,171,11,69,2,3,2,5,1,6),_SwL3IpStaticRouteStatus_Type())
swL3IpStaticRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3IpStaticRouteStatus.setStatus(_A)
_SwL3RelayMgmt_ObjectIdentity=ObjectIdentity
swL3RelayMgmt=_SwL3RelayMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,3))
_SwL3RelayBootpMgmt_ObjectIdentity=ObjectIdentity
swL3RelayBootpMgmt=_SwL3RelayBootpMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,3,1))
class _SwL3RelayBootpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3RelayBootpState_Type.__name__=_B
_SwL3RelayBootpState_Object=MibScalar
swL3RelayBootpState=_SwL3RelayBootpState_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,1),_SwL3RelayBootpState_Type())
swL3RelayBootpState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayBootpState.setStatus(_A)
class _SwL3RelayBootpHopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3RelayBootpHopCount_Type.__name__=_B
_SwL3RelayBootpHopCount_Object=MibScalar
swL3RelayBootpHopCount=_SwL3RelayBootpHopCount_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,2),_SwL3RelayBootpHopCount_Type())
swL3RelayBootpHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayBootpHopCount.setStatus(_A)
class _SwL3RelayBootpTimeThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL3RelayBootpTimeThreshold_Type.__name__=_B
_SwL3RelayBootpTimeThreshold_Object=MibScalar
swL3RelayBootpTimeThreshold=_SwL3RelayBootpTimeThreshold_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,3),_SwL3RelayBootpTimeThreshold_Type())
swL3RelayBootpTimeThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayBootpTimeThreshold.setStatus(_A)
class _SwL3RelayBootpOption82State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3RelayBootpOption82State_Type.__name__=_B
_SwL3RelayBootpOption82State_Object=MibScalar
swL3RelayBootpOption82State=_SwL3RelayBootpOption82State_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,4),_SwL3RelayBootpOption82State_Type())
swL3RelayBootpOption82State.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayBootpOption82State.setStatus(_A)
class _SwL3RelayBootpOption82Check_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3RelayBootpOption82Check_Type.__name__=_B
_SwL3RelayBootpOption82Check_Object=MibScalar
swL3RelayBootpOption82Check=_SwL3RelayBootpOption82Check_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,5),_SwL3RelayBootpOption82Check_Type())
swL3RelayBootpOption82Check.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayBootpOption82Check.setStatus(_A)
class _SwL3RelayBootpOption82Policy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('replace',1),('drop',2),('keep',3)))
_SwL3RelayBootpOption82Policy_Type.__name__=_B
_SwL3RelayBootpOption82Policy_Object=MibScalar
swL3RelayBootpOption82Policy=_SwL3RelayBootpOption82Policy_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,6),_SwL3RelayBootpOption82Policy_Type())
swL3RelayBootpOption82Policy.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayBootpOption82Policy.setStatus(_A)
_SwL3RelayBootpCtrlTable_Object=MibTable
swL3RelayBootpCtrlTable=_SwL3RelayBootpCtrlTable_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,7))
if mibBuilder.loadTexts:swL3RelayBootpCtrlTable.setStatus(_A)
_SwL3RelayBootpCtrlEntry_Object=MibTableRow
swL3RelayBootpCtrlEntry=_SwL3RelayBootpCtrlEntry_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,7,1))
swL3RelayBootpCtrlEntry.setIndexNames((0,_F,_h),(0,_F,_i))
if mibBuilder.loadTexts:swL3RelayBootpCtrlEntry.setStatus(_A)
class _SwL3RelayBootpCtrlInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SwL3RelayBootpCtrlInterfaceName_Type.__name__=_K
_SwL3RelayBootpCtrlInterfaceName_Object=MibTableColumn
swL3RelayBootpCtrlInterfaceName=_SwL3RelayBootpCtrlInterfaceName_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,7,1,1),_SwL3RelayBootpCtrlInterfaceName_Type())
swL3RelayBootpCtrlInterfaceName.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RelayBootpCtrlInterfaceName.setStatus(_A)
_SwL3RelayBootpCtrlServer_Type=IpAddress
_SwL3RelayBootpCtrlServer_Object=MibTableColumn
swL3RelayBootpCtrlServer=_SwL3RelayBootpCtrlServer_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,7,1,2),_SwL3RelayBootpCtrlServer_Type())
swL3RelayBootpCtrlServer.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RelayBootpCtrlServer.setStatus(_A)
class _SwL3RelayBootpCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_R,2),(_S,3)))
_SwL3RelayBootpCtrlState_Type.__name__=_B
_SwL3RelayBootpCtrlState_Object=MibTableColumn
swL3RelayBootpCtrlState=_SwL3RelayBootpCtrlState_Object((1,3,6,1,4,1,171,11,69,2,3,3,1,7,1,3),_SwL3RelayBootpCtrlState_Type())
swL3RelayBootpCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayBootpCtrlState.setStatus(_A)
_SwL3RelayDnsMgmt_ObjectIdentity=ObjectIdentity
swL3RelayDnsMgmt=_SwL3RelayDnsMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,3,2))
class _SwL3RelayDnsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3RelayDnsState_Type.__name__=_B
_SwL3RelayDnsState_Object=MibScalar
swL3RelayDnsState=_SwL3RelayDnsState_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,1),_SwL3RelayDnsState_Type())
swL3RelayDnsState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsState.setStatus(_A)
_SwL3RelayDnsPrimaryServer_Type=IpAddress
_SwL3RelayDnsPrimaryServer_Object=MibScalar
swL3RelayDnsPrimaryServer=_SwL3RelayDnsPrimaryServer_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,2),_SwL3RelayDnsPrimaryServer_Type())
swL3RelayDnsPrimaryServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsPrimaryServer.setStatus(_A)
_SwL3RelayDnsSecondaryServer_Type=IpAddress
_SwL3RelayDnsSecondaryServer_Object=MibScalar
swL3RelayDnsSecondaryServer=_SwL3RelayDnsSecondaryServer_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,3),_SwL3RelayDnsSecondaryServer_Type())
swL3RelayDnsSecondaryServer.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsSecondaryServer.setStatus(_A)
class _SwL3RelayDnsCacheState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3RelayDnsCacheState_Type.__name__=_B
_SwL3RelayDnsCacheState_Object=MibScalar
swL3RelayDnsCacheState=_SwL3RelayDnsCacheState_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,4),_SwL3RelayDnsCacheState_Type())
swL3RelayDnsCacheState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsCacheState.setStatus(_A)
class _SwL3RelayDnsStaticTableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3RelayDnsStaticTableState_Type.__name__=_B
_SwL3RelayDnsStaticTableState_Object=MibScalar
swL3RelayDnsStaticTableState=_SwL3RelayDnsStaticTableState_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,5),_SwL3RelayDnsStaticTableState_Type())
swL3RelayDnsStaticTableState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsStaticTableState.setStatus(_A)
_SwL3RelayDnsCtrlTable_Object=MibTable
swL3RelayDnsCtrlTable=_SwL3RelayDnsCtrlTable_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,6))
if mibBuilder.loadTexts:swL3RelayDnsCtrlTable.setStatus(_A)
_SwL3RelayDnsCtrlEntry_Object=MibTableRow
swL3RelayDnsCtrlEntry=_SwL3RelayDnsCtrlEntry_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,6,1))
swL3RelayDnsCtrlEntry.setIndexNames((0,_F,_j),(0,_F,_k))
if mibBuilder.loadTexts:swL3RelayDnsCtrlEntry.setStatus(_A)
class _SwL3RelayDnsCtrlDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwL3RelayDnsCtrlDomainName_Type.__name__=_K
_SwL3RelayDnsCtrlDomainName_Object=MibTableColumn
swL3RelayDnsCtrlDomainName=_SwL3RelayDnsCtrlDomainName_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,6,1,1),_SwL3RelayDnsCtrlDomainName_Type())
swL3RelayDnsCtrlDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RelayDnsCtrlDomainName.setStatus(_A)
_SwL3RelayDnsCtrlIpAddr_Type=IpAddress
_SwL3RelayDnsCtrlIpAddr_Object=MibTableColumn
swL3RelayDnsCtrlIpAddr=_SwL3RelayDnsCtrlIpAddr_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,6,1,2),_SwL3RelayDnsCtrlIpAddr_Type())
swL3RelayDnsCtrlIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RelayDnsCtrlIpAddr.setStatus(_A)
class _SwL3RelayDnsCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_R,2),(_S,3)))
_SwL3RelayDnsCtrlState_Type.__name__=_B
_SwL3RelayDnsCtrlState_Object=MibTableColumn
swL3RelayDnsCtrlState=_SwL3RelayDnsCtrlState_Object((1,3,6,1,4,1,171,11,69,2,3,3,2,6,1,3),_SwL3RelayDnsCtrlState_Type())
swL3RelayDnsCtrlState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RelayDnsCtrlState.setStatus(_A)
_SwL3Md5Table_Object=MibTable
swL3Md5Table=_SwL3Md5Table_Object((1,3,6,1,4,1,171,11,69,2,3,4))
if mibBuilder.loadTexts:swL3Md5Table.setStatus(_A)
_SwL3Md5Entry_Object=MibTableRow
swL3Md5Entry=_SwL3Md5Entry_Object((1,3,6,1,4,1,171,11,69,2,3,4,1))
swL3Md5Entry.setIndexNames((0,_F,_l))
if mibBuilder.loadTexts:swL3Md5Entry.setStatus(_A)
class _SwL3Md5KeyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL3Md5KeyId_Type.__name__=_B
_SwL3Md5KeyId_Object=MibTableColumn
swL3Md5KeyId=_SwL3Md5KeyId_Object((1,3,6,1,4,1,171,11,69,2,3,4,1,1),_SwL3Md5KeyId_Type())
swL3Md5KeyId.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3Md5KeyId.setStatus(_A)
class _SwL3Md5Key_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_SwL3Md5Key_Type.__name__=_K
_SwL3Md5Key_Object=MibTableColumn
swL3Md5Key=_SwL3Md5Key_Object((1,3,6,1,4,1,171,11,69,2,3,4,1,2),_SwL3Md5Key_Type())
swL3Md5Key.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Md5Key.setStatus(_A)
_SwL3Md5RowStatus_Type=RowStatus
_SwL3Md5RowStatus_Object=MibTableColumn
swL3Md5RowStatus=_SwL3Md5RowStatus_Object((1,3,6,1,4,1,171,11,69,2,3,4,1,3),_SwL3Md5RowStatus_Type())
swL3Md5RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3Md5RowStatus.setStatus(_A)
_SwL3RouteRedistriTable_Object=MibTable
swL3RouteRedistriTable=_SwL3RouteRedistriTable_Object((1,3,6,1,4,1,171,11,69,2,3,5))
if mibBuilder.loadTexts:swL3RouteRedistriTable.setStatus(_A)
_SwL3RouteRedistriEntry_Object=MibTableRow
swL3RouteRedistriEntry=_SwL3RouteRedistriEntry_Object((1,3,6,1,4,1,171,11,69,2,3,5,1))
swL3RouteRedistriEntry.setIndexNames((0,_F,_m),(0,_F,_n))
if mibBuilder.loadTexts:swL3RouteRedistriEntry.setStatus(_A)
class _SwL3RouteRedistriSrcProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('rip',2),('ospf',3),(_d,4),('local',5)))
_SwL3RouteRedistriSrcProtocol_Type.__name__=_B
_SwL3RouteRedistriSrcProtocol_Object=MibTableColumn
swL3RouteRedistriSrcProtocol=_SwL3RouteRedistriSrcProtocol_Object((1,3,6,1,4,1,171,11,69,2,3,5,1,1),_SwL3RouteRedistriSrcProtocol_Type())
swL3RouteRedistriSrcProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RouteRedistriSrcProtocol.setStatus(_A)
class _SwL3RouteRedistriDstProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('rip',2),('ospf',3)))
_SwL3RouteRedistriDstProtocol_Type.__name__=_B
_SwL3RouteRedistriDstProtocol_Object=MibTableColumn
swL3RouteRedistriDstProtocol=_SwL3RouteRedistriDstProtocol_Object((1,3,6,1,4,1,171,11,69,2,3,5,1,2),_SwL3RouteRedistriDstProtocol_Type())
swL3RouteRedistriDstProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RouteRedistriDstProtocol.setStatus(_A)
class _SwL3RouteRedistriType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_G,1),('all',2),('type-1',3),('type-2',4),('internal',5),('external',6),('inter-E1',7),('inter-E2',8),('extType1',9),('extType2',10)))
_SwL3RouteRedistriType_Type.__name__=_B
_SwL3RouteRedistriType_Object=MibTableColumn
swL3RouteRedistriType=_SwL3RouteRedistriType_Object((1,3,6,1,4,1,171,11,69,2,3,5,1,3),_SwL3RouteRedistriType_Type())
swL3RouteRedistriType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RouteRedistriType.setStatus(_A)
class _SwL3RouteRedistriMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_SwL3RouteRedistriMetric_Type.__name__=_B
_SwL3RouteRedistriMetric_Object=MibTableColumn
swL3RouteRedistriMetric=_SwL3RouteRedistriMetric_Object((1,3,6,1,4,1,171,11,69,2,3,5,1,4),_SwL3RouteRedistriMetric_Type())
swL3RouteRedistriMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RouteRedistriMetric.setStatus(_A)
_SwL3RouteRedistriRowStatus_Type=RowStatus
_SwL3RouteRedistriRowStatus_Object=MibTableColumn
swL3RouteRedistriRowStatus=_SwL3RouteRedistriRowStatus_Object((1,3,6,1,4,1,171,11,69,2,3,5,1,5),_SwL3RouteRedistriRowStatus_Type())
swL3RouteRedistriRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3RouteRedistriRowStatus.setStatus(_A)
_SwL3OspfHostTable_Object=MibTable
swL3OspfHostTable=_SwL3OspfHostTable_Object((1,3,6,1,4,1,171,11,69,2,3,6))
if mibBuilder.loadTexts:swL3OspfHostTable.setStatus(_A)
_SwL3OspfHostEntry_Object=MibTableRow
swL3OspfHostEntry=_SwL3OspfHostEntry_Object((1,3,6,1,4,1,171,11,69,2,3,6,1))
swL3OspfHostEntry.setIndexNames((0,_F,_o),(0,_F,_p))
if mibBuilder.loadTexts:swL3OspfHostEntry.setStatus(_A)
_SwL3OspfHostIpAddress_Type=IpAddress
_SwL3OspfHostIpAddress_Object=MibTableColumn
swL3OspfHostIpAddress=_SwL3OspfHostIpAddress_Object((1,3,6,1,4,1,171,11,69,2,3,6,1,1),_SwL3OspfHostIpAddress_Type())
swL3OspfHostIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3OspfHostIpAddress.setStatus(_A)
_SwL3OspfHostTOS_Type=TOSType
_SwL3OspfHostTOS_Object=MibTableColumn
swL3OspfHostTOS=_SwL3OspfHostTOS_Object((1,3,6,1,4,1,171,11,69,2,3,6,1,2),_SwL3OspfHostTOS_Type())
swL3OspfHostTOS.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3OspfHostTOS.setStatus(_A)
_SwL3OspfHostMetric_Type=Metric
_SwL3OspfHostMetric_Object=MibTableColumn
swL3OspfHostMetric=_SwL3OspfHostMetric_Object((1,3,6,1,4,1,171,11,69,2,3,6,1,3),_SwL3OspfHostMetric_Type())
swL3OspfHostMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfHostMetric.setStatus(_A)
_SwL3OspfHostAreaID_Type=AreaID
_SwL3OspfHostAreaID_Object=MibTableColumn
swL3OspfHostAreaID=_SwL3OspfHostAreaID_Object((1,3,6,1,4,1,171,11,69,2,3,6,1,4),_SwL3OspfHostAreaID_Type())
swL3OspfHostAreaID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfHostAreaID.setStatus(_A)
_SwL3OspfHostStatus_Type=RowStatus
_SwL3OspfHostStatus_Object=MibTableColumn
swL3OspfHostStatus=_SwL3OspfHostStatus_Object((1,3,6,1,4,1,171,11,69,2,3,6,1,5),_SwL3OspfHostStatus_Type())
swL3OspfHostStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3OspfHostStatus.setStatus(_A)
_SwL3ospfVirtIfTable_Object=MibTable
swL3ospfVirtIfTable=_SwL3ospfVirtIfTable_Object((1,3,6,1,4,1,171,11,69,2,3,7))
if mibBuilder.loadTexts:swL3ospfVirtIfTable.setStatus(_A)
_SwL3ospfVirtIfEntry_Object=MibTableRow
swL3ospfVirtIfEntry=_SwL3ospfVirtIfEntry_Object((1,3,6,1,4,1,171,11,69,2,3,7,1))
swL3ospfVirtIfEntry.setIndexNames((0,_F,_q),(0,_F,_r))
if mibBuilder.loadTexts:swL3ospfVirtIfEntry.setStatus(_A)
_SwL3ospfVirtIfAreaId_Type=AreaID
_SwL3ospfVirtIfAreaId_Object=MibTableColumn
swL3ospfVirtIfAreaId=_SwL3ospfVirtIfAreaId_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,1),_SwL3ospfVirtIfAreaId_Type())
swL3ospfVirtIfAreaId.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfAreaId.setStatus(_A)
_SwL3ospfVirtIfNeighbor_Type=RouterID
_SwL3ospfVirtIfNeighbor_Object=MibTableColumn
swL3ospfVirtIfNeighbor=_SwL3ospfVirtIfNeighbor_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,2),_SwL3ospfVirtIfNeighbor_Type())
swL3ospfVirtIfNeighbor.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfNeighbor.setStatus(_A)
class _SwL3ospfVirtIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_SwL3ospfVirtIfTransitDelay_Type.__name__=_L
_SwL3ospfVirtIfTransitDelay_Object=MibTableColumn
swL3ospfVirtIfTransitDelay=_SwL3ospfVirtIfTransitDelay_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,3),_SwL3ospfVirtIfTransitDelay_Type())
swL3ospfVirtIfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfTransitDelay.setStatus(_A)
class _SwL3ospfVirtIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_SwL3ospfVirtIfRetransInterval_Type.__name__=_L
_SwL3ospfVirtIfRetransInterval_Object=MibTableColumn
swL3ospfVirtIfRetransInterval=_SwL3ospfVirtIfRetransInterval_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,4),_SwL3ospfVirtIfRetransInterval_Type())
swL3ospfVirtIfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfRetransInterval.setStatus(_A)
class _SwL3ospfVirtIfHelloInterval_Type(HelloRange):defaultValue=10
_SwL3ospfVirtIfHelloInterval_Type.__name__=_P
_SwL3ospfVirtIfHelloInterval_Object=MibTableColumn
swL3ospfVirtIfHelloInterval=_SwL3ospfVirtIfHelloInterval_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,5),_SwL3ospfVirtIfHelloInterval_Type())
swL3ospfVirtIfHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfHelloInterval.setStatus(_A)
class _SwL3ospfVirtIfRtrDeadInterval_Type(PositiveInteger):defaultValue=60
_SwL3ospfVirtIfRtrDeadInterval_Type.__name__=_M
_SwL3ospfVirtIfRtrDeadInterval_Object=MibTableColumn
swL3ospfVirtIfRtrDeadInterval=_SwL3ospfVirtIfRtrDeadInterval_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,6),_SwL3ospfVirtIfRtrDeadInterval_Type())
swL3ospfVirtIfRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfRtrDeadInterval.setStatus(_A)
class _SwL3ospfVirtIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_N,1),(_T,4)))
_SwL3ospfVirtIfState_Type.__name__=_B
_SwL3ospfVirtIfState_Object=MibTableColumn
swL3ospfVirtIfState=_SwL3ospfVirtIfState_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,7),_SwL3ospfVirtIfState_Type())
swL3ospfVirtIfState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfState.setStatus(_A)
_SwL3ospfVirtIfEvents_Type=Counter32
_SwL3ospfVirtIfEvents_Object=MibTableColumn
swL3ospfVirtIfEvents=_SwL3ospfVirtIfEvents_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,8),_SwL3ospfVirtIfEvents_Type())
swL3ospfVirtIfEvents.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfVirtIfEvents.setStatus(_A)
class _SwL3ospfVirtIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfVirtIfAuthType_Type.__name__=_B
_SwL3ospfVirtIfAuthType_Object=MibTableColumn
swL3ospfVirtIfAuthType=_SwL3ospfVirtIfAuthType_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,9),_SwL3ospfVirtIfAuthType_Type())
swL3ospfVirtIfAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfAuthType.setStatus(_A)
class _SwL3ospfVirtIfAuthKey_Type(OctetString):defaultHexValue=_s;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SwL3ospfVirtIfAuthKey_Type.__name__=_O
_SwL3ospfVirtIfAuthKey_Object=MibTableColumn
swL3ospfVirtIfAuthKey=_SwL3ospfVirtIfAuthKey_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,10),_SwL3ospfVirtIfAuthKey_Type())
swL3ospfVirtIfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfAuthKey.setStatus(_A)
class _SwL3ospfVirtIfAuthKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfVirtIfAuthKeyID_Type.__name__=_B
_SwL3ospfVirtIfAuthKeyID_Object=MibTableColumn
swL3ospfVirtIfAuthKeyID=_SwL3ospfVirtIfAuthKeyID_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,11),_SwL3ospfVirtIfAuthKeyID_Type())
swL3ospfVirtIfAuthKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfAuthKeyID.setStatus(_A)
_SwL3ospfVirtIfStatus_Type=RowStatus
_SwL3ospfVirtIfStatus_Object=MibTableColumn
swL3ospfVirtIfStatus=_SwL3ospfVirtIfStatus_Object((1,3,6,1,4,1,171,11,69,2,3,7,1,12),_SwL3ospfVirtIfStatus_Type())
swL3ospfVirtIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfVirtIfStatus.setStatus(_A)
_SwL3ospfIfTable_Object=MibTable
swL3ospfIfTable=_SwL3ospfIfTable_Object((1,3,6,1,4,1,171,11,69,2,3,8))
if mibBuilder.loadTexts:swL3ospfIfTable.setStatus(_A)
_SwL3ospfIfEntry_Object=MibTableRow
swL3ospfIfEntry=_SwL3ospfIfEntry_Object((1,3,6,1,4,1,171,11,69,2,3,8,1))
swL3ospfIfEntry.setIndexNames((0,_F,_t),(0,_F,_u))
if mibBuilder.loadTexts:swL3ospfIfEntry.setStatus(_A)
_SwL3ospfIfIpAddress_Type=IpAddress
_SwL3ospfIfIpAddress_Object=MibTableColumn
swL3ospfIfIpAddress=_SwL3ospfIfIpAddress_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,1),_SwL3ospfIfIpAddress_Type())
swL3ospfIfIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfIfIpAddress.setStatus(_A)
_SwL3ospfAddressLessIf_Type=Integer32
_SwL3ospfAddressLessIf_Object=MibTableColumn
swL3ospfAddressLessIf=_SwL3ospfAddressLessIf_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,2),_SwL3ospfAddressLessIf_Type())
swL3ospfAddressLessIf.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfAddressLessIf.setStatus(_A)
class _SwL3ospfIfAreaId_Type(AreaID):defaultHexValue=_U
_SwL3ospfIfAreaId_Type.__name__=_V
_SwL3ospfIfAreaId_Object=MibTableColumn
swL3ospfIfAreaId=_SwL3ospfIfAreaId_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,3),_SwL3ospfIfAreaId_Type())
swL3ospfIfAreaId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfAreaId.setStatus(_A)
class _SwL3ospfIfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*(('broadcast',1),('nbma',2),(_T,3),('pointToMultipoint',5)))
_SwL3ospfIfType_Type.__name__=_B
_SwL3ospfIfType_Object=MibTableColumn
swL3ospfIfType=_SwL3ospfIfType_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,4),_SwL3ospfIfType_Type())
swL3ospfIfType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfType.setStatus(_A)
class _SwL3ospfIfAdminStat_Type(Status):defaultValue=1
_SwL3ospfIfAdminStat_Type.__name__=_X
_SwL3ospfIfAdminStat_Object=MibTableColumn
swL3ospfIfAdminStat=_SwL3ospfIfAdminStat_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,5),_SwL3ospfIfAdminStat_Type())
swL3ospfIfAdminStat.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfAdminStat.setStatus(_A)
class _SwL3ospfIfRtrPriority_Type(DesignatedRouterPriority):defaultValue=1
_SwL3ospfIfRtrPriority_Type.__name__=_W
_SwL3ospfIfRtrPriority_Object=MibTableColumn
swL3ospfIfRtrPriority=_SwL3ospfIfRtrPriority_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,6),_SwL3ospfIfRtrPriority_Type())
swL3ospfIfRtrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfRtrPriority.setStatus(_A)
class _SwL3ospfIfTransitDelay_Type(UpToMaxAge):defaultValue=1
_SwL3ospfIfTransitDelay_Type.__name__=_L
_SwL3ospfIfTransitDelay_Object=MibTableColumn
swL3ospfIfTransitDelay=_SwL3ospfIfTransitDelay_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,7),_SwL3ospfIfTransitDelay_Type())
swL3ospfIfTransitDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfTransitDelay.setStatus(_A)
class _SwL3ospfIfRetransInterval_Type(UpToMaxAge):defaultValue=5
_SwL3ospfIfRetransInterval_Type.__name__=_L
_SwL3ospfIfRetransInterval_Object=MibTableColumn
swL3ospfIfRetransInterval=_SwL3ospfIfRetransInterval_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,8),_SwL3ospfIfRetransInterval_Type())
swL3ospfIfRetransInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfRetransInterval.setStatus(_A)
class _SwL3ospfIfHelloInterval_Type(HelloRange):defaultValue=10
_SwL3ospfIfHelloInterval_Type.__name__=_P
_SwL3ospfIfHelloInterval_Object=MibTableColumn
swL3ospfIfHelloInterval=_SwL3ospfIfHelloInterval_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,9),_SwL3ospfIfHelloInterval_Type())
swL3ospfIfHelloInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfHelloInterval.setStatus(_A)
class _SwL3ospfIfRtrDeadInterval_Type(PositiveInteger):defaultValue=40
_SwL3ospfIfRtrDeadInterval_Type.__name__=_M
_SwL3ospfIfRtrDeadInterval_Object=MibTableColumn
swL3ospfIfRtrDeadInterval=_SwL3ospfIfRtrDeadInterval_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,10),_SwL3ospfIfRtrDeadInterval_Type())
swL3ospfIfRtrDeadInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfRtrDeadInterval.setStatus(_A)
class _SwL3ospfIfPollInterval_Type(PositiveInteger):defaultValue=120
_SwL3ospfIfPollInterval_Type.__name__=_M
_SwL3ospfIfPollInterval_Object=MibTableColumn
swL3ospfIfPollInterval=_SwL3ospfIfPollInterval_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,11),_SwL3ospfIfPollInterval_Type())
swL3ospfIfPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfPollInterval.setStatus(_A)
class _SwL3ospfIfState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,1),('loopback',2),('waiting',3),(_T,4),('designatedRouter',5),('backupDesignatedRouter',6),('otherDesignatedRouter',7)))
_SwL3ospfIfState_Type.__name__=_B
_SwL3ospfIfState_Object=MibTableColumn
swL3ospfIfState=_SwL3ospfIfState_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,12),_SwL3ospfIfState_Type())
swL3ospfIfState.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfIfState.setStatus(_A)
class _SwL3ospfIfDesignatedRouter_Type(IpAddress):defaultHexValue=_U
_SwL3ospfIfDesignatedRouter_Type.__name__=_Q
_SwL3ospfIfDesignatedRouter_Object=MibTableColumn
swL3ospfIfDesignatedRouter=_SwL3ospfIfDesignatedRouter_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,13),_SwL3ospfIfDesignatedRouter_Type())
swL3ospfIfDesignatedRouter.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfIfDesignatedRouter.setStatus(_A)
class _SwL3ospfIfBackupDesignatedRouter_Type(IpAddress):defaultHexValue=_U
_SwL3ospfIfBackupDesignatedRouter_Type.__name__=_Q
_SwL3ospfIfBackupDesignatedRouter_Object=MibTableColumn
swL3ospfIfBackupDesignatedRouter=_SwL3ospfIfBackupDesignatedRouter_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,14),_SwL3ospfIfBackupDesignatedRouter_Type())
swL3ospfIfBackupDesignatedRouter.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfIfBackupDesignatedRouter.setStatus(_A)
_SwL3ospfIfEvents_Type=Counter32
_SwL3ospfIfEvents_Object=MibTableColumn
swL3ospfIfEvents=_SwL3ospfIfEvents_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,15),_SwL3ospfIfEvents_Type())
swL3ospfIfEvents.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3ospfIfEvents.setStatus(_A)
class _SwL3ospfIfMulticastForwarding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('blocked',1),('multicast',2),('unicast',3)))
_SwL3ospfIfMulticastForwarding_Type.__name__=_B
_SwL3ospfIfMulticastForwarding_Object=MibTableColumn
swL3ospfIfMulticastForwarding=_SwL3ospfIfMulticastForwarding_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,16),_SwL3ospfIfMulticastForwarding_Type())
swL3ospfIfMulticastForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfMulticastForwarding.setStatus(_A)
class _SwL3ospfIfDemand_Type(TruthValue):defaultValue=2
_SwL3ospfIfDemand_Type.__name__=_Z
_SwL3ospfIfDemand_Object=MibTableColumn
swL3ospfIfDemand=_SwL3ospfIfDemand_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,17),_SwL3ospfIfDemand_Type())
swL3ospfIfDemand.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfDemand.setStatus(_A)
class _SwL3ospfIfAuthType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfIfAuthType_Type.__name__=_B
_SwL3ospfIfAuthType_Object=MibTableColumn
swL3ospfIfAuthType=_SwL3ospfIfAuthType_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,18),_SwL3ospfIfAuthType_Type())
swL3ospfIfAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfAuthType.setStatus(_A)
class _SwL3ospfIfAuthKey_Type(OctetString):defaultHexValue=_s;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_SwL3ospfIfAuthKey_Type.__name__=_O
_SwL3ospfIfAuthKey_Object=MibTableColumn
swL3ospfIfAuthKey=_SwL3ospfIfAuthKey_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,19),_SwL3ospfIfAuthKey_Type())
swL3ospfIfAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfAuthKey.setStatus(_A)
class _SwL3ospfIfAuthKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3ospfIfAuthKeyID_Type.__name__=_B
_SwL3ospfIfAuthKeyID_Object=MibTableColumn
swL3ospfIfAuthKeyID=_SwL3ospfIfAuthKeyID_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,20),_SwL3ospfIfAuthKeyID_Type())
swL3ospfIfAuthKeyID.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfAuthKeyID.setStatus(_A)
_SwL3ospfIfStatus_Type=RowStatus
_SwL3ospfIfStatus_Object=MibTableColumn
swL3ospfIfStatus=_SwL3ospfIfStatus_Object((1,3,6,1,4,1,171,11,69,2,3,8,1,21),_SwL3ospfIfStatus_Type())
swL3ospfIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3ospfIfStatus.setStatus(_A)
_SwL3RoutePreference_ObjectIdentity=ObjectIdentity
swL3RoutePreference=_SwL3RoutePreference_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,9))
class _SwL3RoutePreferenceRIP_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceRIP_Type.__name__=_B
_SwL3RoutePreferenceRIP_Object=MibScalar
swL3RoutePreferenceRIP=_SwL3RoutePreferenceRIP_Object((1,3,6,1,4,1,171,11,69,2,3,9,1),_SwL3RoutePreferenceRIP_Type())
swL3RoutePreferenceRIP.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceRIP.setStatus(_A)
class _SwL3RoutePreferenceOSPFIntra_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFIntra_Type.__name__=_B
_SwL3RoutePreferenceOSPFIntra_Object=MibScalar
swL3RoutePreferenceOSPFIntra=_SwL3RoutePreferenceOSPFIntra_Object((1,3,6,1,4,1,171,11,69,2,3,9,2),_SwL3RoutePreferenceOSPFIntra_Type())
swL3RoutePreferenceOSPFIntra.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFIntra.setStatus(_A)
class _SwL3RoutePreferenceStatic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceStatic_Type.__name__=_B
_SwL3RoutePreferenceStatic_Object=MibScalar
swL3RoutePreferenceStatic=_SwL3RoutePreferenceStatic_Object((1,3,6,1,4,1,171,11,69,2,3,9,3),_SwL3RoutePreferenceStatic_Type())
swL3RoutePreferenceStatic.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceStatic.setStatus(_A)
class _SwL3RoutePreferenceLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,999))
_SwL3RoutePreferenceLocal_Type.__name__=_B
_SwL3RoutePreferenceLocal_Object=MibScalar
swL3RoutePreferenceLocal=_SwL3RoutePreferenceLocal_Object((1,3,6,1,4,1,171,11,69,2,3,9,4),_SwL3RoutePreferenceLocal_Type())
swL3RoutePreferenceLocal.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3RoutePreferenceLocal.setStatus(_A)
class _SwL3RoutePreferenceOSPFInter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFInter_Type.__name__=_B
_SwL3RoutePreferenceOSPFInter_Object=MibScalar
swL3RoutePreferenceOSPFInter=_SwL3RoutePreferenceOSPFInter_Object((1,3,6,1,4,1,171,11,69,2,3,9,5),_SwL3RoutePreferenceOSPFInter_Type())
swL3RoutePreferenceOSPFInter.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFInter.setStatus(_A)
class _SwL3RoutePreferenceOSPFExtT1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFExtT1_Type.__name__=_B
_SwL3RoutePreferenceOSPFExtT1_Object=MibScalar
swL3RoutePreferenceOSPFExtT1=_SwL3RoutePreferenceOSPFExtT1_Object((1,3,6,1,4,1,171,11,69,2,3,9,6),_SwL3RoutePreferenceOSPFExtT1_Type())
swL3RoutePreferenceOSPFExtT1.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFExtT1.setStatus(_A)
class _SwL3RoutePreferenceOSPFExtT2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999))
_SwL3RoutePreferenceOSPFExtT2_Type.__name__=_B
_SwL3RoutePreferenceOSPFExtT2_Object=MibScalar
swL3RoutePreferenceOSPFExtT2=_SwL3RoutePreferenceOSPFExtT2_Object((1,3,6,1,4,1,171,11,69,2,3,9,7),_SwL3RoutePreferenceOSPFExtT2_Type())
swL3RoutePreferenceOSPFExtT2.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3RoutePreferenceOSPFExtT2.setStatus(_A)
_SwL3PimMgmt_ObjectIdentity=ObjectIdentity
swL3PimMgmt=_SwL3PimMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,11))
_SwL3PimCbsrInfoMgmt_ObjectIdentity=ObjectIdentity
swL3PimCbsrInfoMgmt=_SwL3PimCbsrInfoMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,11,1))
class _SwL3pimCbsrBootStrapPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL3pimCbsrBootStrapPeriod_Type.__name__=_B
_SwL3pimCbsrBootStrapPeriod_Object=MibScalar
swL3pimCbsrBootStrapPeriod=_SwL3pimCbsrBootStrapPeriod_Object((1,3,6,1,4,1,171,11,69,2,3,11,1,1),_SwL3pimCbsrBootStrapPeriod_Type())
swL3pimCbsrBootStrapPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimCbsrBootStrapPeriod.setStatus(_A)
class _SwL3pimCbsrHashMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3pimCbsrHashMaskLen_Type.__name__=_B
_SwL3pimCbsrHashMaskLen_Object=MibScalar
swL3pimCbsrHashMaskLen=_SwL3pimCbsrHashMaskLen_Object((1,3,6,1,4,1,171,11,69,2,3,11,1,2),_SwL3pimCbsrHashMaskLen_Type())
swL3pimCbsrHashMaskLen.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimCbsrHashMaskLen.setStatus(_A)
_SwL3pimCbsrTable_Object=MibTable
swL3pimCbsrTable=_SwL3pimCbsrTable_Object((1,3,6,1,4,1,171,11,69,2,3,11,1,3))
if mibBuilder.loadTexts:swL3pimCbsrTable.setStatus(_A)
_SwL3pimCbsrEntry_Object=MibTableRow
swL3pimCbsrEntry=_SwL3pimCbsrEntry_Object((1,3,6,1,4,1,171,11,69,2,3,11,1,3,1))
swL3pimCbsrEntry.setIndexNames((0,_F,_v))
if mibBuilder.loadTexts:swL3pimCbsrEntry.setStatus(_A)
_SwL3pimCbsrInterface_Type=InterfaceIndex
_SwL3pimCbsrInterface_Object=MibTableColumn
swL3pimCbsrInterface=_SwL3pimCbsrInterface_Object((1,3,6,1,4,1,171,11,69,2,3,11,1,3,1,1),_SwL3pimCbsrInterface_Type())
swL3pimCbsrInterface.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimCbsrInterface.setStatus(_A)
class _SwL3pimCbsrPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_SwL3pimCbsrPriority_Type.__name__=_B
_SwL3pimCbsrPriority_Object=MibTableColumn
swL3pimCbsrPriority=_SwL3pimCbsrPriority_Object((1,3,6,1,4,1,171,11,69,2,3,11,1,3,1,2),_SwL3pimCbsrPriority_Type())
swL3pimCbsrPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimCbsrPriority.setStatus(_A)
_SwL3pimCandidateRPMgmt_ObjectIdentity=ObjectIdentity
swL3pimCandidateRPMgmt=_SwL3pimCandidateRPMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,11,2))
class _SwL3pimCandidateRPHoldtime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3pimCandidateRPHoldtime_Type.__name__=_B
_SwL3pimCandidateRPHoldtime_Object=MibScalar
swL3pimCandidateRPHoldtime=_SwL3pimCandidateRPHoldtime_Object((1,3,6,1,4,1,171,11,69,2,3,11,2,1),_SwL3pimCandidateRPHoldtime_Type())
swL3pimCandidateRPHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimCandidateRPHoldtime.setStatus(_A)
class _SwL3pimCandidateRPPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL3pimCandidateRPPriority_Type.__name__=_B
_SwL3pimCandidateRPPriority_Object=MibScalar
swL3pimCandidateRPPriority=_SwL3pimCandidateRPPriority_Object((1,3,6,1,4,1,171,11,69,2,3,11,2,2),_SwL3pimCandidateRPPriority_Type())
swL3pimCandidateRPPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimCandidateRPPriority.setStatus(_A)
class _SwL3pimCandidateRPWildcardPrefixCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_SwL3pimCandidateRPWildcardPrefixCnt_Type.__name__=_B
_SwL3pimCandidateRPWildcardPrefixCnt_Object=MibScalar
swL3pimCandidateRPWildcardPrefixCnt=_SwL3pimCandidateRPWildcardPrefixCnt_Object((1,3,6,1,4,1,171,11,69,2,3,11,2,3),_SwL3pimCandidateRPWildcardPrefixCnt_Type())
swL3pimCandidateRPWildcardPrefixCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimCandidateRPWildcardPrefixCnt.setStatus(_A)
_SwL3pimSptMgmt_ObjectIdentity=ObjectIdentity
swL3pimSptMgmt=_SwL3pimSptMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,11,3))
class _SwL3pimLastHopSptThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SwL3pimLastHopSptThreshold_Type.__name__=_K
_SwL3pimLastHopSptThreshold_Object=MibScalar
swL3pimLastHopSptThreshold=_SwL3pimLastHopSptThreshold_Object((1,3,6,1,4,1,171,11,69,2,3,11,3,1),_SwL3pimLastHopSptThreshold_Type())
swL3pimLastHopSptThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimLastHopSptThreshold.setStatus(_A)
class _SwL3pimRPSptThreshold_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_SwL3pimRPSptThreshold_Type.__name__=_K
_SwL3pimRPSptThreshold_Object=MibScalar
swL3pimRPSptThreshold=_SwL3pimRPSptThreshold_Object((1,3,6,1,4,1,171,11,69,2,3,11,3,2),_SwL3pimRPSptThreshold_Type())
swL3pimRPSptThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimRPSptThreshold.setStatus(_A)
_SwL3pimRegChksumIncDataTable_Object=MibTable
swL3pimRegChksumIncDataTable=_SwL3pimRegChksumIncDataTable_Object((1,3,6,1,4,1,171,11,69,2,3,11,4))
if mibBuilder.loadTexts:swL3pimRegChksumIncDataTable.setStatus(_A)
_SwL3pimRegChksumIncDataEntry_Object=MibTableRow
swL3pimRegChksumIncDataEntry=_SwL3pimRegChksumIncDataEntry_Object((1,3,6,1,4,1,171,11,69,2,3,11,4,1))
swL3pimRegChksumIncDataEntry.setIndexNames((0,_F,_w))
if mibBuilder.loadTexts:swL3pimRegChksumIncDataEntry.setStatus(_A)
_SwL3SwL3pimRegChksumIncDataRpAddr_Type=IpAddress
_SwL3SwL3pimRegChksumIncDataRpAddr_Object=MibTableColumn
swL3SwL3pimRegChksumIncDataRpAddr=_SwL3SwL3pimRegChksumIncDataRpAddr_Object((1,3,6,1,4,1,171,11,69,2,3,11,4,1,1),_SwL3SwL3pimRegChksumIncDataRpAddr_Type())
swL3SwL3pimRegChksumIncDataRpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3SwL3pimRegChksumIncDataRpAddr.setStatus(_A)
_SwL3SwL3pimRegChksumIncDataState_Type=RowStatus
_SwL3SwL3pimRegChksumIncDataState_Object=MibTableColumn
swL3SwL3pimRegChksumIncDataState=_SwL3SwL3pimRegChksumIncDataState_Object((1,3,6,1,4,1,171,11,69,2,3,11,4,1,2),_SwL3SwL3pimRegChksumIncDataState_Type())
swL3SwL3pimRegChksumIncDataState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3SwL3pimRegChksumIncDataState.setStatus(_A)
_SwL3PimInfoMgmt_ObjectIdentity=ObjectIdentity
swL3PimInfoMgmt=_SwL3PimInfoMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,11,5))
class _SwL3pimRegisterProbeTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SwL3pimRegisterProbeTime_Type.__name__=_B
_SwL3pimRegisterProbeTime_Object=MibScalar
swL3pimRegisterProbeTime=_SwL3pimRegisterProbeTime_Object((1,3,6,1,4,1,171,11,69,2,3,11,5,1),_SwL3pimRegisterProbeTime_Type())
swL3pimRegisterProbeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimRegisterProbeTime.setStatus(_A)
class _SwL3pimRegisterSuppressionTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,255))
_SwL3pimRegisterSuppressionTime_Type.__name__=_B
_SwL3pimRegisterSuppressionTime_Object=MibScalar
swL3pimRegisterSuppressionTime=_SwL3pimRegisterSuppressionTime_Object((1,3,6,1,4,1,171,11,69,2,3,11,5,2),_SwL3pimRegisterSuppressionTime_Type())
swL3pimRegisterSuppressionTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimRegisterSuppressionTime.setStatus(_A)
_SwL3pimInfoTable_Object=MibTable
swL3pimInfoTable=_SwL3pimInfoTable_Object((1,3,6,1,4,1,171,11,69,2,3,11,5,3))
if mibBuilder.loadTexts:swL3pimInfoTable.setStatus(_A)
_SwL3pimInfoEntry_Object=MibTableRow
swL3pimInfoEntry=_SwL3pimInfoEntry_Object((1,3,6,1,4,1,171,11,69,2,3,11,5,3,1))
swL3pimInfoEntry.setIndexNames((0,_F,_x))
if mibBuilder.loadTexts:swL3pimInfoEntry.setStatus(_A)
_SwL3pimInterface_Type=InterfaceIndex
_SwL3pimInterface_Object=MibTableColumn
swL3pimInterface=_SwL3pimInterface_Object((1,3,6,1,4,1,171,11,69,2,3,11,5,3,1,1),_SwL3pimInterface_Type())
swL3pimInterface.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimInterface.setStatus(_A)
class _SwL3pimDRPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967294))
_SwL3pimDRPriority_Type.__name__=_Y
_SwL3pimDRPriority_Object=MibTableColumn
swL3pimDRPriority=_SwL3pimDRPriority_Object((1,3,6,1,4,1,171,11,69,2,3,11,5,3,1,2),_SwL3pimDRPriority_Type())
swL3pimDRPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3pimDRPriority.setStatus(_A)
_SwL3pimStaticRPTable_Object=MibTable
swL3pimStaticRPTable=_SwL3pimStaticRPTable_Object((1,3,6,1,4,1,171,11,69,2,3,11,6))
if mibBuilder.loadTexts:swL3pimStaticRPTable.setStatus(_A)
_SwL3pimStaticRPEntry_Object=MibTableRow
swL3pimStaticRPEntry=_SwL3pimStaticRPEntry_Object((1,3,6,1,4,1,171,11,69,2,3,11,6,1))
swL3pimStaticRPEntry.setIndexNames((0,_F,_y),(0,_F,_z),(0,_F,_A0))
if mibBuilder.loadTexts:swL3pimStaticRPEntry.setStatus(_A)
_SwL3pimStaticRPGroupAddress_Type=IpAddress
_SwL3pimStaticRPGroupAddress_Object=MibTableColumn
swL3pimStaticRPGroupAddress=_SwL3pimStaticRPGroupAddress_Object((1,3,6,1,4,1,171,11,69,2,3,11,6,1,1),_SwL3pimStaticRPGroupAddress_Type())
swL3pimStaticRPGroupAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimStaticRPGroupAddress.setStatus(_A)
_SwL3pimStaticRPGroupMask_Type=IpAddress
_SwL3pimStaticRPGroupMask_Object=MibTableColumn
swL3pimStaticRPGroupMask=_SwL3pimStaticRPGroupMask_Object((1,3,6,1,4,1,171,11,69,2,3,11,6,1,2),_SwL3pimStaticRPGroupMask_Type())
swL3pimStaticRPGroupMask.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimStaticRPGroupMask.setStatus(_A)
_SwL3pimStaticRPAddress_Type=IpAddress
_SwL3pimStaticRPAddress_Object=MibTableColumn
swL3pimStaticRPAddress=_SwL3pimStaticRPAddress_Object((1,3,6,1,4,1,171,11,69,2,3,11,6,1,3),_SwL3pimStaticRPAddress_Type())
swL3pimStaticRPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimStaticRPAddress.setStatus(_A)
_SwL3pimStaticRPRowStatus_Type=RowStatus
_SwL3pimStaticRPRowStatus_Object=MibTableColumn
swL3pimStaticRPRowStatus=_SwL3pimStaticRPRowStatus_Object((1,3,6,1,4,1,171,11,69,2,3,11,6,1,4),_SwL3pimStaticRPRowStatus_Type())
swL3pimStaticRPRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL3pimStaticRPRowStatus.setStatus(_A)
_SwL3pimActiveRPTable_Object=MibTable
swL3pimActiveRPTable=_SwL3pimActiveRPTable_Object((1,3,6,1,4,1,171,11,69,2,3,11,7))
if mibBuilder.loadTexts:swL3pimActiveRPTable.setStatus(_A)
_SwL3pimActiveRPEntry_Object=MibTableRow
swL3pimActiveRPEntry=_SwL3pimActiveRPEntry_Object((1,3,6,1,4,1,171,11,69,2,3,11,7,1))
swL3pimActiveRPEntry.setIndexNames((0,_F,_A1))
if mibBuilder.loadTexts:swL3pimActiveRPEntry.setStatus(_A)
_SwL3pimActiveRPGroupAddress_Type=IpAddress
_SwL3pimActiveRPGroupAddress_Object=MibTableColumn
swL3pimActiveRPGroupAddress=_SwL3pimActiveRPGroupAddress_Object((1,3,6,1,4,1,171,11,69,2,3,11,7,1,1),_SwL3pimActiveRPGroupAddress_Type())
swL3pimActiveRPGroupAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimActiveRPGroupAddress.setStatus(_A)
_SwL3pimActiveRPSourceIPAddress_Type=IpAddress
_SwL3pimActiveRPSourceIPAddress_Object=MibTableColumn
swL3pimActiveRPSourceIPAddress=_SwL3pimActiveRPSourceIPAddress_Object((1,3,6,1,4,1,171,11,69,2,3,11,7,1,2),_SwL3pimActiveRPSourceIPAddress_Type())
swL3pimActiveRPSourceIPAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimActiveRPSourceIPAddress.setStatus(_A)
_SwL3pimActiveRPSourceIPMask_Type=IpAddress
_SwL3pimActiveRPSourceIPMask_Object=MibTableColumn
swL3pimActiveRPSourceIPMask=_SwL3pimActiveRPSourceIPMask_Object((1,3,6,1,4,1,171,11,69,2,3,11,7,1,3),_SwL3pimActiveRPSourceIPMask_Type())
swL3pimActiveRPSourceIPMask.setMaxAccess(_J)
if mibBuilder.loadTexts:swL3pimActiveRPSourceIPMask.setStatus(_A)
_SwL3pimActiveRPAddress_Type=IpAddress
_SwL3pimActiveRPAddress_Object=MibTableColumn
swL3pimActiveRPAddress=_SwL3pimActiveRPAddress_Object((1,3,6,1,4,1,171,11,69,2,3,11,7,1,4),_SwL3pimActiveRPAddress_Type())
swL3pimActiveRPAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:swL3pimActiveRPAddress.setStatus(_A)
_SwL3OspfDefaultInfoOriginate_ObjectIdentity=ObjectIdentity
swL3OspfDefaultInfoOriginate=_SwL3OspfDefaultInfoOriginate_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,12))
_SwL3OspfDefaultInfoOriginateState_Type=Status
_SwL3OspfDefaultInfoOriginateState_Object=MibScalar
swL3OspfDefaultInfoOriginateState=_SwL3OspfDefaultInfoOriginateState_Object((1,3,6,1,4,1,171,11,69,2,3,12,1),_SwL3OspfDefaultInfoOriginateState_Type())
swL3OspfDefaultInfoOriginateState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfDefaultInfoOriginateState.setStatus(_A)
_SwL3OspfDefaultInfoOriginateAlways_Type=Status
_SwL3OspfDefaultInfoOriginateAlways_Object=MibScalar
swL3OspfDefaultInfoOriginateAlways=_SwL3OspfDefaultInfoOriginateAlways_Object((1,3,6,1,4,1,171,11,69,2,3,12,2),_SwL3OspfDefaultInfoOriginateAlways_Type())
swL3OspfDefaultInfoOriginateAlways.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfDefaultInfoOriginateAlways.setStatus(_A)
class _SwL3OspfDefaultInfoOriginateMettype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type1',1),('type2',2)))
_SwL3OspfDefaultInfoOriginateMettype_Type.__name__=_B
_SwL3OspfDefaultInfoOriginateMettype_Object=MibScalar
swL3OspfDefaultInfoOriginateMettype=_SwL3OspfDefaultInfoOriginateMettype_Object((1,3,6,1,4,1,171,11,69,2,3,12,3),_SwL3OspfDefaultInfoOriginateMettype_Type())
swL3OspfDefaultInfoOriginateMettype.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfDefaultInfoOriginateMettype.setStatus(_A)
class _SwL3OspfDefaultInfoOriginateMetric_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777214))
_SwL3OspfDefaultInfoOriginateMetric_Type.__name__=_B
_SwL3OspfDefaultInfoOriginateMetric_Object=MibScalar
swL3OspfDefaultInfoOriginateMetric=_SwL3OspfDefaultInfoOriginateMetric_Object((1,3,6,1,4,1,171,11,69,2,3,12,4),_SwL3OspfDefaultInfoOriginateMetric_Type())
swL3OspfDefaultInfoOriginateMetric.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3OspfDefaultInfoOriginateMetric.setStatus(_A)
_SwL3TraceRouteMgmt_ObjectIdentity=ObjectIdentity
swL3TraceRouteMgmt=_SwL3TraceRouteMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,13))
_SwL3TraceRouteCtrl_ObjectIdentity=ObjectIdentity
swL3TraceRouteCtrl=_SwL3TraceRouteCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,69,2,3,13,1))
class _SwL3TraceRoutePKTToCPUState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_SwL3TraceRoutePKTToCPUState_Type.__name__=_B
_SwL3TraceRoutePKTToCPUState_Object=MibScalar
swL3TraceRoutePKTToCPUState=_SwL3TraceRoutePKTToCPUState_Object((1,3,6,1,4,1,171,11,69,2,3,13,1,1),_SwL3TraceRoutePKTToCPUState_Type())
swL3TraceRoutePKTToCPUState.setMaxAccess(_D)
if mibBuilder.loadTexts:swL3TraceRoutePKTToCPUState.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'NodeAddress':NodeAddress,'NetAddress':NetAddress,'swL3MgmtMIB':swL3MgmtMIB,'swL3DevMgmt':swL3DevMgmt,'swL3DevCtrl':swL3DevCtrl,'swL3DevCtrlRIPState':swL3DevCtrlRIPState,'swL3DevCtrlOSPFState':swL3DevCtrlOSPFState,'swL3DevCtrlDVMRPState':swL3DevCtrlDVMRPState,'swL3DevCtrlPIMState':swL3DevCtrlPIMState,'swL3DevCtrlVRRPState':swL3DevCtrlVRRPState,'swL3DevCtrlOSPFECMPState':swL3DevCtrlOSPFECMPState,'swL3IpMgmt':swL3IpMgmt,'swL3IpCtrlMgmt':swL3IpCtrlMgmt,'swL3IpCtrlTable':swL3IpCtrlTable,'swL3IpCtrlEntry':swL3IpCtrlEntry,_a:swL3IpCtrlIpAddr,'swL3IpCtrlIfIndex':swL3IpCtrlIfIndex,'swL3IpCtrlInterfaceName':swL3IpCtrlInterfaceName,'swL3IpCtrlIpSubnetMask':swL3IpCtrlIpSubnetMask,'swL3IpCtrlVlanName':swL3IpCtrlVlanName,'swL3IpCtrlMode':swL3IpCtrlMode,'swL3IpCtrlSecondary':swL3IpCtrlSecondary,'swL3IpCtrlState':swL3IpCtrlState,'swL3IpCtrlOperState':swL3IpCtrlOperState,'swL3IpCtrlProxyARPState':swL3IpCtrlProxyARPState,'swL3VirtualIpCtrlTable':swL3VirtualIpCtrlTable,'swL3VirtualIpCtrlEntry':swL3VirtualIpCtrlEntry,_b:swL3VirtualIpCtrlInterfaceName,'swL3VirtualIpCtrlIfIndex':swL3VirtualIpCtrlIfIndex,'swL3VirtualIpCtrlIpAddr':swL3VirtualIpCtrlIpAddr,'swL3VirtualIpCtrlIpSubnetMask':swL3VirtualIpCtrlIpSubnetMask,'swL3VirtualIpCtrlOperState':swL3VirtualIpCtrlOperState,'swL3VirtualIpCtrlState':swL3VirtualIpCtrlState,'swL3IpFdbMgmt':swL3IpFdbMgmt,'swL3IpFdbInfoTable':swL3IpFdbInfoTable,'swL3IpFdbInfoEntry':swL3IpFdbInfoEntry,_c:swL3IpFdbInfoIpAddr,'swL3IpFdbInfoIpSubnetMask':swL3IpFdbInfoIpSubnetMask,'swL3IpFdbInfoPort':swL3IpFdbInfoPort,'swL3IpFdbInfoType':swL3IpFdbInfoType,'swL3IpArpAgingTime':swL3IpArpAgingTime,'swL3IpStaticRouteTable':swL3IpStaticRouteTable,'swL3IpStaticRouteEntry':swL3IpStaticRouteEntry,_e:swL3IpStaticRouteDest,_f:swL3IpStaticRouteMask,_g:swL3IpStaticRouteBkupState,'swL3IpStaticRouteNextHop':swL3IpStaticRouteNextHop,'swL3IpStaticRouteMetric':swL3IpStaticRouteMetric,'swL3IpStaticRouteStatus':swL3IpStaticRouteStatus,'swL3RelayMgmt':swL3RelayMgmt,'swL3RelayBootpMgmt':swL3RelayBootpMgmt,'swL3RelayBootpState':swL3RelayBootpState,'swL3RelayBootpHopCount':swL3RelayBootpHopCount,'swL3RelayBootpTimeThreshold':swL3RelayBootpTimeThreshold,'swL3RelayBootpOption82State':swL3RelayBootpOption82State,'swL3RelayBootpOption82Check':swL3RelayBootpOption82Check,'swL3RelayBootpOption82Policy':swL3RelayBootpOption82Policy,'swL3RelayBootpCtrlTable':swL3RelayBootpCtrlTable,'swL3RelayBootpCtrlEntry':swL3RelayBootpCtrlEntry,_h:swL3RelayBootpCtrlInterfaceName,_i:swL3RelayBootpCtrlServer,'swL3RelayBootpCtrlState':swL3RelayBootpCtrlState,'swL3RelayDnsMgmt':swL3RelayDnsMgmt,'swL3RelayDnsState':swL3RelayDnsState,'swL3RelayDnsPrimaryServer':swL3RelayDnsPrimaryServer,'swL3RelayDnsSecondaryServer':swL3RelayDnsSecondaryServer,'swL3RelayDnsCacheState':swL3RelayDnsCacheState,'swL3RelayDnsStaticTableState':swL3RelayDnsStaticTableState,'swL3RelayDnsCtrlTable':swL3RelayDnsCtrlTable,'swL3RelayDnsCtrlEntry':swL3RelayDnsCtrlEntry,_j:swL3RelayDnsCtrlDomainName,_k:swL3RelayDnsCtrlIpAddr,'swL3RelayDnsCtrlState':swL3RelayDnsCtrlState,'swL3Md5Table':swL3Md5Table,'swL3Md5Entry':swL3Md5Entry,_l:swL3Md5KeyId,'swL3Md5Key':swL3Md5Key,'swL3Md5RowStatus':swL3Md5RowStatus,'swL3RouteRedistriTable':swL3RouteRedistriTable,'swL3RouteRedistriEntry':swL3RouteRedistriEntry,_m:swL3RouteRedistriSrcProtocol,_n:swL3RouteRedistriDstProtocol,'swL3RouteRedistriType':swL3RouteRedistriType,'swL3RouteRedistriMetric':swL3RouteRedistriMetric,'swL3RouteRedistriRowStatus':swL3RouteRedistriRowStatus,'swL3OspfHostTable':swL3OspfHostTable,'swL3OspfHostEntry':swL3OspfHostEntry,_o:swL3OspfHostIpAddress,_p:swL3OspfHostTOS,'swL3OspfHostMetric':swL3OspfHostMetric,'swL3OspfHostAreaID':swL3OspfHostAreaID,'swL3OspfHostStatus':swL3OspfHostStatus,'swL3ospfVirtIfTable':swL3ospfVirtIfTable,'swL3ospfVirtIfEntry':swL3ospfVirtIfEntry,_q:swL3ospfVirtIfAreaId,_r:swL3ospfVirtIfNeighbor,'swL3ospfVirtIfTransitDelay':swL3ospfVirtIfTransitDelay,'swL3ospfVirtIfRetransInterval':swL3ospfVirtIfRetransInterval,'swL3ospfVirtIfHelloInterval':swL3ospfVirtIfHelloInterval,'swL3ospfVirtIfRtrDeadInterval':swL3ospfVirtIfRtrDeadInterval,'swL3ospfVirtIfState':swL3ospfVirtIfState,'swL3ospfVirtIfEvents':swL3ospfVirtIfEvents,'swL3ospfVirtIfAuthType':swL3ospfVirtIfAuthType,'swL3ospfVirtIfAuthKey':swL3ospfVirtIfAuthKey,'swL3ospfVirtIfAuthKeyID':swL3ospfVirtIfAuthKeyID,'swL3ospfVirtIfStatus':swL3ospfVirtIfStatus,'swL3ospfIfTable':swL3ospfIfTable,'swL3ospfIfEntry':swL3ospfIfEntry,_t:swL3ospfIfIpAddress,_u:swL3ospfAddressLessIf,'swL3ospfIfAreaId':swL3ospfIfAreaId,'swL3ospfIfType':swL3ospfIfType,'swL3ospfIfAdminStat':swL3ospfIfAdminStat,'swL3ospfIfRtrPriority':swL3ospfIfRtrPriority,'swL3ospfIfTransitDelay':swL3ospfIfTransitDelay,'swL3ospfIfRetransInterval':swL3ospfIfRetransInterval,'swL3ospfIfHelloInterval':swL3ospfIfHelloInterval,'swL3ospfIfRtrDeadInterval':swL3ospfIfRtrDeadInterval,'swL3ospfIfPollInterval':swL3ospfIfPollInterval,'swL3ospfIfState':swL3ospfIfState,'swL3ospfIfDesignatedRouter':swL3ospfIfDesignatedRouter,'swL3ospfIfBackupDesignatedRouter':swL3ospfIfBackupDesignatedRouter,'swL3ospfIfEvents':swL3ospfIfEvents,'swL3ospfIfMulticastForwarding':swL3ospfIfMulticastForwarding,'swL3ospfIfDemand':swL3ospfIfDemand,'swL3ospfIfAuthType':swL3ospfIfAuthType,'swL3ospfIfAuthKey':swL3ospfIfAuthKey,'swL3ospfIfAuthKeyID':swL3ospfIfAuthKeyID,'swL3ospfIfStatus':swL3ospfIfStatus,'swL3RoutePreference':swL3RoutePreference,'swL3RoutePreferenceRIP':swL3RoutePreferenceRIP,'swL3RoutePreferenceOSPFIntra':swL3RoutePreferenceOSPFIntra,'swL3RoutePreferenceStatic':swL3RoutePreferenceStatic,'swL3RoutePreferenceLocal':swL3RoutePreferenceLocal,'swL3RoutePreferenceOSPFInter':swL3RoutePreferenceOSPFInter,'swL3RoutePreferenceOSPFExtT1':swL3RoutePreferenceOSPFExtT1,'swL3RoutePreferenceOSPFExtT2':swL3RoutePreferenceOSPFExtT2,'swL3PimMgmt':swL3PimMgmt,'swL3PimCbsrInfoMgmt':swL3PimCbsrInfoMgmt,'swL3pimCbsrBootStrapPeriod':swL3pimCbsrBootStrapPeriod,'swL3pimCbsrHashMaskLen':swL3pimCbsrHashMaskLen,'swL3pimCbsrTable':swL3pimCbsrTable,'swL3pimCbsrEntry':swL3pimCbsrEntry,_v:swL3pimCbsrInterface,'swL3pimCbsrPriority':swL3pimCbsrPriority,'swL3pimCandidateRPMgmt':swL3pimCandidateRPMgmt,'swL3pimCandidateRPHoldtime':swL3pimCandidateRPHoldtime,'swL3pimCandidateRPPriority':swL3pimCandidateRPPriority,'swL3pimCandidateRPWildcardPrefixCnt':swL3pimCandidateRPWildcardPrefixCnt,'swL3pimSptMgmt':swL3pimSptMgmt,'swL3pimLastHopSptThreshold':swL3pimLastHopSptThreshold,'swL3pimRPSptThreshold':swL3pimRPSptThreshold,'swL3pimRegChksumIncDataTable':swL3pimRegChksumIncDataTable,'swL3pimRegChksumIncDataEntry':swL3pimRegChksumIncDataEntry,_w:swL3SwL3pimRegChksumIncDataRpAddr,'swL3SwL3pimRegChksumIncDataState':swL3SwL3pimRegChksumIncDataState,'swL3PimInfoMgmt':swL3PimInfoMgmt,'swL3pimRegisterProbeTime':swL3pimRegisterProbeTime,'swL3pimRegisterSuppressionTime':swL3pimRegisterSuppressionTime,'swL3pimInfoTable':swL3pimInfoTable,'swL3pimInfoEntry':swL3pimInfoEntry,_x:swL3pimInterface,'swL3pimDRPriority':swL3pimDRPriority,'swL3pimStaticRPTable':swL3pimStaticRPTable,'swL3pimStaticRPEntry':swL3pimStaticRPEntry,_y:swL3pimStaticRPGroupAddress,_z:swL3pimStaticRPGroupMask,_A0:swL3pimStaticRPAddress,'swL3pimStaticRPRowStatus':swL3pimStaticRPRowStatus,'swL3pimActiveRPTable':swL3pimActiveRPTable,'swL3pimActiveRPEntry':swL3pimActiveRPEntry,_A1:swL3pimActiveRPGroupAddress,'swL3pimActiveRPSourceIPAddress':swL3pimActiveRPSourceIPAddress,'swL3pimActiveRPSourceIPMask':swL3pimActiveRPSourceIPMask,'swL3pimActiveRPAddress':swL3pimActiveRPAddress,'swL3OspfDefaultInfoOriginate':swL3OspfDefaultInfoOriginate,'swL3OspfDefaultInfoOriginateState':swL3OspfDefaultInfoOriginateState,'swL3OspfDefaultInfoOriginateAlways':swL3OspfDefaultInfoOriginateAlways,'swL3OspfDefaultInfoOriginateMettype':swL3OspfDefaultInfoOriginateMettype,'swL3OspfDefaultInfoOriginateMetric':swL3OspfDefaultInfoOriginateMetric,'swL3TraceRouteMgmt':swL3TraceRouteMgmt,'swL3TraceRouteCtrl':swL3TraceRouteCtrl,'swL3TraceRoutePKTToCPUState':swL3TraceRoutePKTToCPUState})