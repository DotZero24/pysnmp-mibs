_e='swL2PortMirrorIndex'
_d='swL2DiffServTOSCtrlPortIndex'
_c='swL2DiffServDSCPCtrlPortIndex'
_b='swL2DiffServTypeCtrlPortIndex'
_a='swL2PortCtrlPortIndex'
_Z='swL2PortInfoPortIndex'
_Y='normal'
_X='swL2PortSecurityPortIndex'
_W='swL2CosQueueIndex'
_V='swL2EgressPortBwCtrlPort'
_U='gigabitEthernetPort'
_T='fastEthernetPort'
_S='not-accessible'
_R='swL2IngrPortBwCtrlPort'
_Q='OctetString'
_P='active'
_O='full-1Gigabps'
_N='half-1Gigabps'
_M='full-100Mbps'
_L='half-100Mbps'
_K='full-10Mbps'
_J='half-10Mbps'
_I='DisplayString'
_H='DHS3226-MIB'
_G='enabled'
_F='disabled'
_E='other'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_Q,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_Dhs3226Prod,dlink_mgmt=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-Dhs3226Prod','dlink-mgmt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
swL2MgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,36,2))
class VlanId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwL2Property_ObjectIdentity=ObjectIdentity
swL2Property=_SwL2Property_ObjectIdentity((1,3,6,1,4,1,171,10,36,1,1))
_SwL2Module_ObjectIdentity=ObjectIdentity
swL2Module=_SwL2Module_ObjectIdentity((1,3,6,1,4,1,171,10,36,1,1,1))
_SwL2BwMgmt_ObjectIdentity=ObjectIdentity
swL2BwMgmt=_SwL2BwMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,1))
class _SwL2BwMgmtFEPortUnitBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2BwMgmtFEPortUnitBandwidth_Type.__name__=_B
_SwL2BwMgmtFEPortUnitBandwidth_Object=MibScalar
swL2BwMgmtFEPortUnitBandwidth=_SwL2BwMgmtFEPortUnitBandwidth_Object((1,3,6,1,4,1,171,11,36,2,1,1),_SwL2BwMgmtFEPortUnitBandwidth_Type())
swL2BwMgmtFEPortUnitBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2BwMgmtFEPortUnitBandwidth.setStatus(_A)
class _SwL2BwMgmtGEPortUnitBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2BwMgmtGEPortUnitBandwidth_Type.__name__=_B
_SwL2BwMgmtGEPortUnitBandwidth_Object=MibScalar
swL2BwMgmtGEPortUnitBandwidth=_SwL2BwMgmtGEPortUnitBandwidth_Object((1,3,6,1,4,1,171,11,36,2,1,2),_SwL2BwMgmtGEPortUnitBandwidth_Type())
swL2BwMgmtGEPortUnitBandwidth.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2BwMgmtGEPortUnitBandwidth.setStatus(_A)
_SwL2IngrPortBwControl_ObjectIdentity=ObjectIdentity
swL2IngrPortBwControl=_SwL2IngrPortBwControl_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,1,3))
_SwL2IngrPortBwCtrlTable_Object=MibTable
swL2IngrPortBwCtrlTable=_SwL2IngrPortBwCtrlTable_Object((1,3,6,1,4,1,171,11,36,2,1,3,3))
if mibBuilder.loadTexts:swL2IngrPortBwCtrlTable.setStatus(_A)
_SwL2IngrPortBwCtrlEntry_Object=MibTableRow
swL2IngrPortBwCtrlEntry=_SwL2IngrPortBwCtrlEntry_Object((1,3,6,1,4,1,171,11,36,2,1,3,3,1))
swL2IngrPortBwCtrlEntry.setIndexNames((0,_H,_R))
if mibBuilder.loadTexts:swL2IngrPortBwCtrlEntry.setStatus(_A)
class _SwL2IngrPortBwCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2IngrPortBwCtrlPort_Type.__name__=_B
_SwL2IngrPortBwCtrlPort_Object=MibTableColumn
swL2IngrPortBwCtrlPort=_SwL2IngrPortBwCtrlPort_Object((1,3,6,1,4,1,171,11,36,2,1,3,3,1,1),_SwL2IngrPortBwCtrlPort_Type())
swL2IngrPortBwCtrlPort.setMaxAccess(_S)
if mibBuilder.loadTexts:swL2IngrPortBwCtrlPort.setStatus(_A)
class _SwL2IngrPortBwCtrlPortCountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_SwL2IngrPortBwCtrlPortCountType_Type.__name__=_B
_SwL2IngrPortBwCtrlPortCountType_Object=MibTableColumn
swL2IngrPortBwCtrlPortCountType=_SwL2IngrPortBwCtrlPortCountType_Object((1,3,6,1,4,1,171,11,36,2,1,3,3,1,2),_SwL2IngrPortBwCtrlPortCountType_Type())
swL2IngrPortBwCtrlPortCountType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IngrPortBwCtrlPortCountType.setStatus(_A)
class _SwL2IngrPortBwCtrlPortNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_SwL2IngrPortBwCtrlPortNwayStatus_Type.__name__=_B
_SwL2IngrPortBwCtrlPortNwayStatus_Object=MibTableColumn
swL2IngrPortBwCtrlPortNwayStatus=_SwL2IngrPortBwCtrlPortNwayStatus_Object((1,3,6,1,4,1,171,11,36,2,1,3,3,1,3),_SwL2IngrPortBwCtrlPortNwayStatus_Type())
swL2IngrPortBwCtrlPortNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IngrPortBwCtrlPortNwayStatus.setStatus(_A)
class _SwL2IngrPortBwCtrlUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SwL2IngrPortBwCtrlUnit_Type.__name__=_B
_SwL2IngrPortBwCtrlUnit_Object=MibTableColumn
swL2IngrPortBwCtrlUnit=_SwL2IngrPortBwCtrlUnit_Object((1,3,6,1,4,1,171,11,36,2,1,3,3,1,4),_SwL2IngrPortBwCtrlUnit_Type())
swL2IngrPortBwCtrlUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IngrPortBwCtrlUnit.setStatus(_A)
class _SwL2IngrPortBwCtrlRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2IngrPortBwCtrlRate_Type.__name__=_B
_SwL2IngrPortBwCtrlRate_Object=MibTableColumn
swL2IngrPortBwCtrlRate=_SwL2IngrPortBwCtrlRate_Object((1,3,6,1,4,1,171,11,36,2,1,3,3,1,5),_SwL2IngrPortBwCtrlRate_Type())
swL2IngrPortBwCtrlRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2IngrPortBwCtrlRate.setStatus(_A)
class _SwL2IngrPortBwCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2IngrPortBwCtrlStatus_Type.__name__=_B
_SwL2IngrPortBwCtrlStatus_Object=MibTableColumn
swL2IngrPortBwCtrlStatus=_SwL2IngrPortBwCtrlStatus_Object((1,3,6,1,4,1,171,11,36,2,1,3,3,1,6),_SwL2IngrPortBwCtrlStatus_Type())
swL2IngrPortBwCtrlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2IngrPortBwCtrlStatus.setStatus(_A)
_SwL2EgressPortBwControl_ObjectIdentity=ObjectIdentity
swL2EgressPortBwControl=_SwL2EgressPortBwControl_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,1,4))
_SwL2EgressPortBwCtrlTable_Object=MibTable
swL2EgressPortBwCtrlTable=_SwL2EgressPortBwCtrlTable_Object((1,3,6,1,4,1,171,11,36,2,1,4,3))
if mibBuilder.loadTexts:swL2EgressPortBwCtrlTable.setStatus(_A)
_SwL2EgressPortBwCtrlEntry_Object=MibTableRow
swL2EgressPortBwCtrlEntry=_SwL2EgressPortBwCtrlEntry_Object((1,3,6,1,4,1,171,11,36,2,1,4,3,1))
swL2EgressPortBwCtrlEntry.setIndexNames((0,_H,_V))
if mibBuilder.loadTexts:swL2EgressPortBwCtrlEntry.setStatus(_A)
class _SwL2EgressPortBwCtrlPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2EgressPortBwCtrlPort_Type.__name__=_B
_SwL2EgressPortBwCtrlPort_Object=MibTableColumn
swL2EgressPortBwCtrlPort=_SwL2EgressPortBwCtrlPort_Object((1,3,6,1,4,1,171,11,36,2,1,4,3,1,1),_SwL2EgressPortBwCtrlPort_Type())
swL2EgressPortBwCtrlPort.setMaxAccess(_S)
if mibBuilder.loadTexts:swL2EgressPortBwCtrlPort.setStatus(_A)
class _SwL2EgressPortBwCtrlPortCountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_SwL2EgressPortBwCtrlPortCountType_Type.__name__=_B
_SwL2EgressPortBwCtrlPortCountType_Object=MibTableColumn
swL2EgressPortBwCtrlPortCountType=_SwL2EgressPortBwCtrlPortCountType_Object((1,3,6,1,4,1,171,11,36,2,1,4,3,1,2),_SwL2EgressPortBwCtrlPortCountType_Type())
swL2EgressPortBwCtrlPortCountType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2EgressPortBwCtrlPortCountType.setStatus(_A)
class _SwL2EgressPortBwCtrlPortNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_SwL2EgressPortBwCtrlPortNwayStatus_Type.__name__=_B
_SwL2EgressPortBwCtrlPortNwayStatus_Object=MibTableColumn
swL2EgressPortBwCtrlPortNwayStatus=_SwL2EgressPortBwCtrlPortNwayStatus_Object((1,3,6,1,4,1,171,11,36,2,1,4,3,1,3),_SwL2EgressPortBwCtrlPortNwayStatus_Type())
swL2EgressPortBwCtrlPortNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2EgressPortBwCtrlPortNwayStatus.setStatus(_A)
class _SwL2EgressPortBwCtrlUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_SwL2EgressPortBwCtrlUnit_Type.__name__=_B
_SwL2EgressPortBwCtrlUnit_Object=MibTableColumn
swL2EgressPortBwCtrlUnit=_SwL2EgressPortBwCtrlUnit_Object((1,3,6,1,4,1,171,11,36,2,1,4,3,1,4),_SwL2EgressPortBwCtrlUnit_Type())
swL2EgressPortBwCtrlUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2EgressPortBwCtrlUnit.setStatus(_A)
class _SwL2EgressPortBwCtrlRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwL2EgressPortBwCtrlRate_Type.__name__=_B
_SwL2EgressPortBwCtrlRate_Object=MibTableColumn
swL2EgressPortBwCtrlRate=_SwL2EgressPortBwCtrlRate_Object((1,3,6,1,4,1,171,11,36,2,1,4,3,1,5),_SwL2EgressPortBwCtrlRate_Type())
swL2EgressPortBwCtrlRate.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2EgressPortBwCtrlRate.setStatus(_A)
class _SwL2EgressPortBwCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2EgressPortBwCtrlStatus_Type.__name__=_B
_SwL2EgressPortBwCtrlStatus_Object=MibTableColumn
swL2EgressPortBwCtrlStatus=_SwL2EgressPortBwCtrlStatus_Object((1,3,6,1,4,1,171,11,36,2,1,4,3,1,6),_SwL2EgressPortBwCtrlStatus_Type())
swL2EgressPortBwCtrlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2EgressPortBwCtrlStatus.setStatus(_A)
class _SwL2GrpAddrFltrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('forwardAllGrpAddr',2),('forwardAllUnregGrpAddr',3),('filterAllUnregGrpAddr',4)))
_SwL2GrpAddrFltrMode_Type.__name__=_B
_SwL2GrpAddrFltrMode_Object=MibScalar
swL2GrpAddrFltrMode=_SwL2GrpAddrFltrMode_Object((1,3,6,1,4,1,171,11,36,2,2),_SwL2GrpAddrFltrMode_Type())
swL2GrpAddrFltrMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2GrpAddrFltrMode.setStatus(_A)
_SwL2CosMgmt_ObjectIdentity=ObjectIdentity
swL2CosMgmt=_SwL2CosMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,3))
class _SwL2CosScheduleMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('strict',2),('roundRobin',3)))
_SwL2CosScheduleMethod_Type.__name__=_B
_SwL2CosScheduleMethod_Object=MibScalar
swL2CosScheduleMethod=_SwL2CosScheduleMethod_Object((1,3,6,1,4,1,171,11,36,2,3,1),_SwL2CosScheduleMethod_Type())
swL2CosScheduleMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosScheduleMethod.setStatus(_A)
_SwL2CosControlTable_Object=MibTable
swL2CosControlTable=_SwL2CosControlTable_Object((1,3,6,1,4,1,171,11,36,2,3,2))
if mibBuilder.loadTexts:swL2CosControlTable.setStatus(_A)
_SwL2CosControlEntry_Object=MibTableRow
swL2CosControlEntry=_SwL2CosControlEntry_Object((1,3,6,1,4,1,171,11,36,2,3,2,1))
swL2CosControlEntry.setIndexNames((0,_H,_W))
if mibBuilder.loadTexts:swL2CosControlEntry.setStatus(_A)
class _SwL2CosQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SwL2CosQueueIndex_Type.__name__=_B
_SwL2CosQueueIndex_Object=MibTableColumn
swL2CosQueueIndex=_SwL2CosQueueIndex_Object((1,3,6,1,4,1,171,11,36,2,3,2,1,1),_SwL2CosQueueIndex_Type())
swL2CosQueueIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2CosQueueIndex.setStatus(_A)
class _SwL2CosMaxPackets_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2CosMaxPackets_Type.__name__=_B
_SwL2CosMaxPackets_Object=MibTableColumn
swL2CosMaxPackets=_SwL2CosMaxPackets_Object((1,3,6,1,4,1,171,11,36,2,3,2,1,2),_SwL2CosMaxPackets_Type())
swL2CosMaxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosMaxPackets.setStatus(_A)
class _SwL2CosMaxLatency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2CosMaxLatency_Type.__name__=_B
_SwL2CosMaxLatency_Object=MibTableColumn
swL2CosMaxLatency=_SwL2CosMaxLatency_Object((1,3,6,1,4,1,171,11,36,2,3,2,1,3),_SwL2CosMaxLatency_Type())
swL2CosMaxLatency.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2CosMaxLatency.setStatus(_A)
_SwL2PortSecurityMgmt_ObjectIdentity=ObjectIdentity
swL2PortSecurityMgmt=_SwL2PortSecurityMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,4))
_SwL2PortSecurityControlTable_Object=MibTable
swL2PortSecurityControlTable=_SwL2PortSecurityControlTable_Object((1,3,6,1,4,1,171,11,36,2,4,1))
if mibBuilder.loadTexts:swL2PortSecurityControlTable.setStatus(_A)
_SwL2PortSecurityControlEntry_Object=MibTableRow
swL2PortSecurityControlEntry=_SwL2PortSecurityControlEntry_Object((1,3,6,1,4,1,171,11,36,2,4,1,1))
swL2PortSecurityControlEntry.setIndexNames((0,_H,_X))
if mibBuilder.loadTexts:swL2PortSecurityControlEntry.setStatus(_A)
class _SwL2PortSecurityPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortSecurityPortIndex_Type.__name__=_B
_SwL2PortSecurityPortIndex_Object=MibTableColumn
swL2PortSecurityPortIndex=_SwL2PortSecurityPortIndex_Object((1,3,6,1,4,1,171,11,36,2,4,1,1,1),_SwL2PortSecurityPortIndex_Type())
swL2PortSecurityPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortSecurityPortIndex.setStatus(_A)
class _SwL2PortSecurityMaxLernAddr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SwL2PortSecurityMaxLernAddr_Type.__name__=_B
_SwL2PortSecurityMaxLernAddr_Object=MibTableColumn
swL2PortSecurityMaxLernAddr=_SwL2PortSecurityMaxLernAddr_Object((1,3,6,1,4,1,171,11,36,2,4,1,1,2),_SwL2PortSecurityMaxLernAddr_Type())
swL2PortSecurityMaxLernAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMaxLernAddr.setStatus(_A)
class _SwL2PortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('deleteOnTimeout',2),('deleteOnReset',3)))
_SwL2PortSecurityMode_Type.__name__=_B
_SwL2PortSecurityMode_Object=MibTableColumn
swL2PortSecurityMode=_SwL2PortSecurityMode_Object((1,3,6,1,4,1,171,11,36,2,4,1,1,3),_SwL2PortSecurityMode_Type())
swL2PortSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityMode.setStatus(_A)
class _SwL2PortSecurityAdmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('enable',2),('disable',3)))
_SwL2PortSecurityAdmState_Type.__name__=_B
_SwL2PortSecurityAdmState_Object=MibTableColumn
swL2PortSecurityAdmState=_SwL2PortSecurityAdmState_Object((1,3,6,1,4,1,171,11,36,2,4,1,1,4),_SwL2PortSecurityAdmState_Type())
swL2PortSecurityAdmState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortSecurityAdmState.setStatus(_A)
_SwL2DevMgmt_ObjectIdentity=ObjectIdentity
swL2DevMgmt=_SwL2DevMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,5))
_SwL2DevInfo_ObjectIdentity=ObjectIdentity
swL2DevInfo=_SwL2DevInfo_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,5,1))
_SwL2DevInfoSystemUpTime_Type=TimeTicks
_SwL2DevInfoSystemUpTime_Object=MibScalar
swL2DevInfoSystemUpTime=_SwL2DevInfoSystemUpTime_Object((1,3,6,1,4,1,171,11,36,2,5,1,1),_SwL2DevInfoSystemUpTime_Type())
swL2DevInfoSystemUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoSystemUpTime.setStatus(_A)
class _SwL2DevInfoTotalNumOfPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2DevInfoTotalNumOfPort_Type.__name__=_B
_SwL2DevInfoTotalNumOfPort_Object=MibScalar
swL2DevInfoTotalNumOfPort=_SwL2DevInfoTotalNumOfPort_Object((1,3,6,1,4,1,171,11,36,2,5,1,2),_SwL2DevInfoTotalNumOfPort_Type())
swL2DevInfoTotalNumOfPort.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoTotalNumOfPort.setStatus(_A)
class _SwL2DevInfoNumOfPortInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SwL2DevInfoNumOfPortInUse_Type.__name__=_B
_SwL2DevInfoNumOfPortInUse_Object=MibScalar
swL2DevInfoNumOfPortInUse=_SwL2DevInfoNumOfPortInUse_Object((1,3,6,1,4,1,171,11,36,2,5,1,3),_SwL2DevInfoNumOfPortInUse_Type())
swL2DevInfoNumOfPortInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoNumOfPortInUse.setStatus(_A)
class _SwL2DevInfoConsoleInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('in-use',2),('not-in-use',3)))
_SwL2DevInfoConsoleInUse_Type.__name__=_B
_SwL2DevInfoConsoleInUse_Object=MibScalar
swL2DevInfoConsoleInUse=_SwL2DevInfoConsoleInUse_Object((1,3,6,1,4,1,171,11,36,2,5,1,4),_SwL2DevInfoConsoleInUse_Type())
swL2DevInfoConsoleInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoConsoleInUse.setStatus(_A)
class _SwL2DevInfoFrontPanelLedStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwL2DevInfoFrontPanelLedStatus_Type.__name__=_Q
_SwL2DevInfoFrontPanelLedStatus_Object=MibScalar
swL2DevInfoFrontPanelLedStatus=_SwL2DevInfoFrontPanelLedStatus_Object((1,3,6,1,4,1,171,11,36,2,5,1,5),_SwL2DevInfoFrontPanelLedStatus_Type())
swL2DevInfoFrontPanelLedStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoFrontPanelLedStatus.setStatus(_A)
class _SwL2DevInfoCpuUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_SwL2DevInfoCpuUtilization_Type.__name__=_B
_SwL2DevInfoCpuUtilization_Object=MibScalar
swL2DevInfoCpuUtilization=_SwL2DevInfoCpuUtilization_Object((1,3,6,1,4,1,171,11,36,2,5,1,6),_SwL2DevInfoCpuUtilization_Type())
swL2DevInfoCpuUtilization.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DevInfoCpuUtilization.setStatus(_A)
if mibBuilder.loadTexts:swL2DevInfoCpuUtilization.setUnits('%')
_SwL2DevCtrl_ObjectIdentity=ObjectIdentity
swL2DevCtrl=_SwL2DevCtrl_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,5,2))
class _SwL2DevCtrlSystemReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),('reboot',2),('save-config-and-reboot',3),('reboot-and-load-factory-default-config',4),('reboot-and-load-factory-default-config-except-ip-address',5)))
_SwL2DevCtrlSystemReboot_Type.__name__=_B
_SwL2DevCtrlSystemReboot_Object=MibScalar
swL2DevCtrlSystemReboot=_SwL2DevCtrlSystemReboot_Object((1,3,6,1,4,1,171,11,36,2,5,2,1),_SwL2DevCtrlSystemReboot_Type())
swL2DevCtrlSystemReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSystemReboot.setStatus(_A)
_SwL2DevCtrlSystemIP_Type=IpAddress
_SwL2DevCtrlSystemIP_Object=MibScalar
swL2DevCtrlSystemIP=_SwL2DevCtrlSystemIP_Object((1,3,6,1,4,1,171,11,36,2,5,2,2),_SwL2DevCtrlSystemIP_Type())
swL2DevCtrlSystemIP.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSystemIP.setStatus(_A)
_SwL2DevCtrlSubnetMask_Type=IpAddress
_SwL2DevCtrlSubnetMask_Object=MibScalar
swL2DevCtrlSubnetMask=_SwL2DevCtrlSubnetMask_Object((1,3,6,1,4,1,171,11,36,2,5,2,3),_SwL2DevCtrlSubnetMask_Type())
swL2DevCtrlSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSubnetMask.setStatus(_A)
_SwL2DevCtrlDefaultGateway_Type=IpAddress
_SwL2DevCtrlDefaultGateway_Object=MibScalar
swL2DevCtrlDefaultGateway=_SwL2DevCtrlDefaultGateway_Object((1,3,6,1,4,1,171,11,36,2,5,2,4),_SwL2DevCtrlDefaultGateway_Type())
swL2DevCtrlDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlDefaultGateway.setStatus(_A)
_SwL2DevCtrlManagementVlanId_Type=VlanId
_SwL2DevCtrlManagementVlanId_Object=MibScalar
swL2DevCtrlManagementVlanId=_SwL2DevCtrlManagementVlanId_Object((1,3,6,1,4,1,171,11,36,2,5,2,5),_SwL2DevCtrlManagementVlanId_Type())
swL2DevCtrlManagementVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlManagementVlanId.setStatus(_A)
class _SwL2DevCtrlStpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2DevCtrlStpState_Type.__name__=_B
_SwL2DevCtrlStpState_Object=MibScalar
swL2DevCtrlStpState=_SwL2DevCtrlStpState_Object((1,3,6,1,4,1,171,11,36,2,5,2,6),_SwL2DevCtrlStpState_Type())
swL2DevCtrlStpState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlStpState.setStatus(_A)
class _SwL2DevCtrlIGMPSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2DevCtrlIGMPSnooping_Type.__name__=_B
_SwL2DevCtrlIGMPSnooping_Object=MibScalar
swL2DevCtrlIGMPSnooping=_SwL2DevCtrlIGMPSnooping_Object((1,3,6,1,4,1,171,11,36,2,5,2,7),_SwL2DevCtrlIGMPSnooping_Type())
swL2DevCtrlIGMPSnooping.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlIGMPSnooping.setStatus(_A)
class _SwL2DevCtrlBcastStormCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2DevCtrlBcastStormCtrl_Type.__name__=_B
_SwL2DevCtrlBcastStormCtrl_Object=MibScalar
swL2DevCtrlBcastStormCtrl=_SwL2DevCtrlBcastStormCtrl_Object((1,3,6,1,4,1,171,11,36,2,5,2,8),_SwL2DevCtrlBcastStormCtrl_Type())
swL2DevCtrlBcastStormCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlBcastStormCtrl.setStatus(_A)
class _SwL2DevCtrlMcastStormCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2DevCtrlMcastStormCtrl_Type.__name__=_B
_SwL2DevCtrlMcastStormCtrl_Object=MibScalar
swL2DevCtrlMcastStormCtrl=_SwL2DevCtrlMcastStormCtrl_Object((1,3,6,1,4,1,171,11,36,2,5,2,9),_SwL2DevCtrlMcastStormCtrl_Type())
swL2DevCtrlMcastStormCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlMcastStormCtrl.setStatus(_A)
class _SwL2DevCtrlDestLookupFailureCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2DevCtrlDestLookupFailureCtrl_Type.__name__=_B
_SwL2DevCtrlDestLookupFailureCtrl_Object=MibScalar
swL2DevCtrlDestLookupFailureCtrl=_SwL2DevCtrlDestLookupFailureCtrl_Object((1,3,6,1,4,1,171,11,36,2,5,2,10),_SwL2DevCtrlDestLookupFailureCtrl_Type())
swL2DevCtrlDestLookupFailureCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlDestLookupFailureCtrl.setStatus(_A)
class _SwL2DevCtrlBMDStormLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262143))
_SwL2DevCtrlBMDStormLimit_Type.__name__=_B
_SwL2DevCtrlBMDStormLimit_Object=MibScalar
swL2DevCtrlBMDStormLimit=_SwL2DevCtrlBMDStormLimit_Object((1,3,6,1,4,1,171,11,36,2,5,2,11),_SwL2DevCtrlBMDStormLimit_Type())
swL2DevCtrlBMDStormLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlBMDStormLimit.setStatus(_A)
class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_P,2)))
_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__=_B
_SwL2DevCtrlCleanAllStatisticCounter_Object=MibScalar
swL2DevCtrlCleanAllStatisticCounter=_SwL2DevCtrlCleanAllStatisticCounter_Object((1,3,6,1,4,1,171,11,36,2,5,2,12),_SwL2DevCtrlCleanAllStatisticCounter_Type())
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlCleanAllStatisticCounter.setStatus(_A)
class _SwL2DevCtrlSnmpEnableAuthenTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlSnmpEnableAuthenTraps_Type.__name__=_B
_SwL2DevCtrlSnmpEnableAuthenTraps_Object=MibScalar
swL2DevCtrlSnmpEnableAuthenTraps=_SwL2DevCtrlSnmpEnableAuthenTraps_Object((1,3,6,1,4,1,171,11,36,2,5,2,13),_SwL2DevCtrlSnmpEnableAuthenTraps_Type())
swL2DevCtrlSnmpEnableAuthenTraps.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlSnmpEnableAuthenTraps.setStatus(_A)
class _SwL2DevCtrlFilterEAPOLPDU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_SwL2DevCtrlFilterEAPOLPDU_Type.__name__=_B
_SwL2DevCtrlFilterEAPOLPDU_Object=MibScalar
swL2DevCtrlFilterEAPOLPDU=_SwL2DevCtrlFilterEAPOLPDU_Object((1,3,6,1,4,1,171,11,36,2,5,2,14),_SwL2DevCtrlFilterEAPOLPDU_Type())
swL2DevCtrlFilterEAPOLPDU.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlFilterEAPOLPDU.setStatus(_A)
class _SwL2DevCtrlTrafficSegmentation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2DevCtrlTrafficSegmentation_Type.__name__=_B
_SwL2DevCtrlTrafficSegmentation_Object=MibScalar
swL2DevCtrlTrafficSegmentation=_SwL2DevCtrlTrafficSegmentation_Object((1,3,6,1,4,1,171,11,36,2,5,2,15),_SwL2DevCtrlTrafficSegmentation_Type())
swL2DevCtrlTrafficSegmentation.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlTrafficSegmentation.setStatus(_A)
_AgentPingTest_ObjectIdentity=ObjectIdentity
agentPingTest=_AgentPingTest_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,5,2,16))
_AgentPingTestIPAddress_Type=IpAddress
_AgentPingTestIPAddress_Object=MibScalar
agentPingTestIPAddress=_AgentPingTestIPAddress_Object((1,3,6,1,4,1,171,11,36,2,5,2,16,1),_AgentPingTestIPAddress_Type())
agentPingTestIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPingTestIPAddress.setStatus(_A)
class _AgentPingTestRepetition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentPingTestRepetition_Type.__name__=_B
_AgentPingTestRepetition_Object=MibScalar
agentPingTestRepetition=_AgentPingTestRepetition_Object((1,3,6,1,4,1,171,11,36,2,5,2,16,2),_AgentPingTestRepetition_Type())
agentPingTestRepetition.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPingTestRepetition.setStatus(_A)
class _AgentPingTestControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('stop',0),(_P,1)))
_AgentPingTestControl_Type.__name__=_B
_AgentPingTestControl_Object=MibScalar
agentPingTestControl=_AgentPingTestControl_Object((1,3,6,1,4,1,171,11,36,2,5,2,16,3),_AgentPingTestControl_Type())
agentPingTestControl.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPingTestControl.setStatus(_A)
class _AgentPingTestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('finish',0),('proceeding',1)))
_AgentPingTestStatus_Type.__name__=_B
_AgentPingTestStatus_Object=MibScalar
agentPingTestStatus=_AgentPingTestStatus_Object((1,3,6,1,4,1,171,11,36,2,5,2,16,4),_AgentPingTestStatus_Type())
agentPingTestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPingTestStatus.setStatus(_A)
class _AgentPingTestSuccessCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentPingTestSuccessCount_Type.__name__=_B
_AgentPingTestSuccessCount_Object=MibScalar
agentPingTestSuccessCount=_AgentPingTestSuccessCount_Object((1,3,6,1,4,1,171,11,36,2,5,2,16,5),_AgentPingTestSuccessCount_Type())
agentPingTestSuccessCount.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPingTestSuccessCount.setStatus(_A)
class _AgentPingTestFailCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_AgentPingTestFailCount_Type.__name__=_B
_AgentPingTestFailCount_Object=MibScalar
agentPingTestFailCount=_AgentPingTestFailCount_Object((1,3,6,1,4,1,171,11,36,2,5,2,16,6),_AgentPingTestFailCount_Type())
agentPingTestFailCount.setMaxAccess(_D)
if mibBuilder.loadTexts:agentPingTestFailCount.setStatus(_A)
_SwL2DevCtrlVlanIdOfFDBTbl_Type=VlanId
_SwL2DevCtrlVlanIdOfFDBTbl_Object=MibScalar
swL2DevCtrlVlanIdOfFDBTbl=_SwL2DevCtrlVlanIdOfFDBTbl_Object((1,3,6,1,4,1,171,11,36,2,5,2,17),_SwL2DevCtrlVlanIdOfFDBTbl_Type())
swL2DevCtrlVlanIdOfFDBTbl.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DevCtrlVlanIdOfFDBTbl.setStatus(_A)
_SwL2PortMgmt_ObjectIdentity=ObjectIdentity
swL2PortMgmt=_SwL2PortMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,6))
_SwL2PortInfoTable_Object=MibTable
swL2PortInfoTable=_SwL2PortInfoTable_Object((1,3,6,1,4,1,171,11,36,2,6,1))
if mibBuilder.loadTexts:swL2PortInfoTable.setStatus(_A)
_SwL2PortInfoEntry_Object=MibTableRow
swL2PortInfoEntry=_SwL2PortInfoEntry_Object((1,3,6,1,4,1,171,11,36,2,6,1,1))
swL2PortInfoEntry.setIndexNames((0,_H,_Z))
if mibBuilder.loadTexts:swL2PortInfoEntry.setStatus(_A)
class _SwL2PortInfoPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortInfoPortIndex_Type.__name__=_B
_SwL2PortInfoPortIndex_Object=MibTableColumn
swL2PortInfoPortIndex=_SwL2PortInfoPortIndex_Object((1,3,6,1,4,1,171,11,36,2,6,1,1,1),_SwL2PortInfoPortIndex_Type())
swL2PortInfoPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoPortIndex.setStatus(_A)
class _SwL2PortInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),('portType-UTP',2),('portType-AUI',3),('portType-Fiber-MTRJ',4),('portType-Fiber-SC',5),('portType-Fiber-GBIC',6),('portType-BNC',7)))
_SwL2PortInfoType_Type.__name__=_B
_SwL2PortInfoType_Object=MibTableColumn
swL2PortInfoType=_SwL2PortInfoType_Object((1,3,6,1,4,1,171,11,36,2,6,1,1,2),_SwL2PortInfoType_Type())
swL2PortInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoType.setStatus(_A)
class _SwL2PortInfoDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_SwL2PortInfoDescr_Type.__name__=_I
_SwL2PortInfoDescr_Object=MibTableColumn
swL2PortInfoDescr=_SwL2PortInfoDescr_Object((1,3,6,1,4,1,171,11,36,2,6,1,1,3),_SwL2PortInfoDescr_Type())
swL2PortInfoDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoDescr.setStatus(_A)
class _SwL2PortInfoLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),('link-pass',2),('link-fail',3)))
_SwL2PortInfoLinkStatus_Type.__name__=_B
_SwL2PortInfoLinkStatus_Object=MibTableColumn
swL2PortInfoLinkStatus=_SwL2PortInfoLinkStatus_Object((1,3,6,1,4,1,171,11,36,2,6,1,1,4),_SwL2PortInfoLinkStatus_Type())
swL2PortInfoLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoLinkStatus.setStatus(_A)
class _SwL2PortInfoNwayStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_E,1),(_J,2),(_K,3),(_L,4),(_M,5),(_N,6),(_O,7)))
_SwL2PortInfoNwayStatus_Type.__name__=_B
_SwL2PortInfoNwayStatus_Object=MibTableColumn
swL2PortInfoNwayStatus=_SwL2PortInfoNwayStatus_Object((1,3,6,1,4,1,171,11,36,2,6,1,1,5),_SwL2PortInfoNwayStatus_Type())
swL2PortInfoNwayStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortInfoNwayStatus.setStatus(_A)
_SwL2PortCtrlTable_Object=MibTable
swL2PortCtrlTable=_SwL2PortCtrlTable_Object((1,3,6,1,4,1,171,11,36,2,6,2))
if mibBuilder.loadTexts:swL2PortCtrlTable.setStatus(_A)
_SwL2PortCtrlEntry_Object=MibTableRow
swL2PortCtrlEntry=_SwL2PortCtrlEntry_Object((1,3,6,1,4,1,171,11,36,2,6,2,1))
swL2PortCtrlEntry.setIndexNames((0,_H,_a))
if mibBuilder.loadTexts:swL2PortCtrlEntry.setStatus(_A)
class _SwL2PortCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2PortCtrlPortIndex_Type.__name__=_B
_SwL2PortCtrlPortIndex_Object=MibTableColumn
swL2PortCtrlPortIndex=_SwL2PortCtrlPortIndex_Object((1,3,6,1,4,1,171,11,36,2,6,2,1,1),_SwL2PortCtrlPortIndex_Type())
swL2PortCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortCtrlPortIndex.setStatus(_A)
class _SwL2PortCtrlAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2PortCtrlAdminState_Type.__name__=_B
_SwL2PortCtrlAdminState_Object=MibTableColumn
swL2PortCtrlAdminState=_SwL2PortCtrlAdminState_Object((1,3,6,1,4,1,171,11,36,2,6,2,1,2),_SwL2PortCtrlAdminState_Type())
swL2PortCtrlAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlAdminState.setStatus(_A)
class _SwL2PortCtrlNwayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_E,1),('nway-enabled',2),('nway-disabled-10Mbps-Half',3),('nway-disabled-10Mbps-Full',4),('nway-disabled-100Mbps-Half',5),('nway-disabled-100Mbps-Full',6),('nway-disabled-1Gigabps-Half',7),('nway-disabled-1Gigabps-Full',8)))
_SwL2PortCtrlNwayState_Type.__name__=_B
_SwL2PortCtrlNwayState_Object=MibTableColumn
swL2PortCtrlNwayState=_SwL2PortCtrlNwayState_Object((1,3,6,1,4,1,171,11,36,2,6,2,1,3),_SwL2PortCtrlNwayState_Type())
swL2PortCtrlNwayState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlNwayState.setStatus(_A)
class _SwL2PortCtrlFlowCtrlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_SwL2PortCtrlFlowCtrlState_Type.__name__=_B
_SwL2PortCtrlFlowCtrlState_Object=MibTableColumn
swL2PortCtrlFlowCtrlState=_SwL2PortCtrlFlowCtrlState_Object((1,3,6,1,4,1,171,11,36,2,6,2,1,4),_SwL2PortCtrlFlowCtrlState_Type())
swL2PortCtrlFlowCtrlState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlFlowCtrlState.setStatus(_A)
class _SwL2PortCtrlCleanStatCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Y,1),(_P,2)))
_SwL2PortCtrlCleanStatCounter_Type.__name__=_B
_SwL2PortCtrlCleanStatCounter_Object=MibTableColumn
swL2PortCtrlCleanStatCounter=_SwL2PortCtrlCleanStatCounter_Object((1,3,6,1,4,1,171,11,36,2,6,2,1,5),_SwL2PortCtrlCleanStatCounter_Type())
swL2PortCtrlCleanStatCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlCleanStatCounter.setStatus(_A)
class _SwL2PortCtrlDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SwL2PortCtrlDescription_Type.__name__=_I
_SwL2PortCtrlDescription_Object=MibTableColumn
swL2PortCtrlDescription=_SwL2PortCtrlDescription_Object((1,3,6,1,4,1,171,11,36,2,6,2,1,6),_SwL2PortCtrlDescription_Type())
swL2PortCtrlDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortCtrlDescription.setStatus(_A)
_SwL2DiffServMgmt_ObjectIdentity=ObjectIdentity
swL2DiffServMgmt=_SwL2DiffServMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,7))
_SwL2DiffServTypeCtrlTable_Object=MibTable
swL2DiffServTypeCtrlTable=_SwL2DiffServTypeCtrlTable_Object((1,3,6,1,4,1,171,11,36,2,7,1))
if mibBuilder.loadTexts:swL2DiffServTypeCtrlTable.setStatus(_A)
_SwL2DiffServTypeCtrlEntry_Object=MibTableRow
swL2DiffServTypeCtrlEntry=_SwL2DiffServTypeCtrlEntry_Object((1,3,6,1,4,1,171,11,36,2,7,1,1))
swL2DiffServTypeCtrlEntry.setIndexNames((0,_H,_b))
if mibBuilder.loadTexts:swL2DiffServTypeCtrlEntry.setStatus(_A)
class _SwL2DiffServTypeCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2DiffServTypeCtrlPortIndex_Type.__name__=_B
_SwL2DiffServTypeCtrlPortIndex_Object=MibTableColumn
swL2DiffServTypeCtrlPortIndex=_SwL2DiffServTypeCtrlPortIndex_Object((1,3,6,1,4,1,171,11,36,2,7,1,1,1),_SwL2DiffServTypeCtrlPortIndex_Type())
swL2DiffServTypeCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServTypeCtrlPortIndex.setStatus(_A)
class _SwL2DiffServTypeCtrlDiffServType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),('dscp',2),('tos',3)))
_SwL2DiffServTypeCtrlDiffServType_Type.__name__=_B
_SwL2DiffServTypeCtrlDiffServType_Object=MibTableColumn
swL2DiffServTypeCtrlDiffServType=_SwL2DiffServTypeCtrlDiffServType_Object((1,3,6,1,4,1,171,11,36,2,7,1,1,2),_SwL2DiffServTypeCtrlDiffServType_Type())
swL2DiffServTypeCtrlDiffServType.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServTypeCtrlDiffServType.setStatus(_A)
_SwL2DiffServDSCPCtrlTable_Object=MibTable
swL2DiffServDSCPCtrlTable=_SwL2DiffServDSCPCtrlTable_Object((1,3,6,1,4,1,171,11,36,2,7,2))
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlTable.setStatus(_A)
_SwL2DiffServDSCPCtrlEntry_Object=MibTableRow
swL2DiffServDSCPCtrlEntry=_SwL2DiffServDSCPCtrlEntry_Object((1,3,6,1,4,1,171,11,36,2,7,2,1))
swL2DiffServDSCPCtrlEntry.setIndexNames((0,_H,_c))
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlEntry.setStatus(_A)
class _SwL2DiffServDSCPCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2DiffServDSCPCtrlPortIndex_Type.__name__=_B
_SwL2DiffServDSCPCtrlPortIndex_Object=MibTableColumn
swL2DiffServDSCPCtrlPortIndex=_SwL2DiffServDSCPCtrlPortIndex_Object((1,3,6,1,4,1,171,11,36,2,7,2,1,1),_SwL2DiffServDSCPCtrlPortIndex_Type())
swL2DiffServDSCPCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlPortIndex.setStatus(_A)
class _SwL2DiffServDSCPCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dscp-Force-Overwrite',1),('dscp-Change-If-Zero',2)))
_SwL2DiffServDSCPCtrlMode_Type.__name__=_B
_SwL2DiffServDSCPCtrlMode_Object=MibTableColumn
swL2DiffServDSCPCtrlMode=_SwL2DiffServDSCPCtrlMode_Object((1,3,6,1,4,1,171,11,36,2,7,2,1,2),_SwL2DiffServDSCPCtrlMode_Type())
swL2DiffServDSCPCtrlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlMode.setStatus(_A)
class _SwL2DiffServDSCPCtrlValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_SwL2DiffServDSCPCtrlValue_Type.__name__=_B
_SwL2DiffServDSCPCtrlValue_Object=MibTableColumn
swL2DiffServDSCPCtrlValue=_SwL2DiffServDSCPCtrlValue_Object((1,3,6,1,4,1,171,11,36,2,7,2,1,3),_SwL2DiffServDSCPCtrlValue_Type())
swL2DiffServDSCPCtrlValue.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServDSCPCtrlValue.setStatus(_A)
_SwL2DiffServTOSCtrlTable_Object=MibTable
swL2DiffServTOSCtrlTable=_SwL2DiffServTOSCtrlTable_Object((1,3,6,1,4,1,171,11,36,2,7,3))
if mibBuilder.loadTexts:swL2DiffServTOSCtrlTable.setStatus(_A)
_SwL2DiffServTOSCtrlEntry_Object=MibTableRow
swL2DiffServTOSCtrlEntry=_SwL2DiffServTOSCtrlEntry_Object((1,3,6,1,4,1,171,11,36,2,7,3,1))
swL2DiffServTOSCtrlEntry.setIndexNames((0,_H,_d))
if mibBuilder.loadTexts:swL2DiffServTOSCtrlEntry.setStatus(_A)
class _SwL2DiffServTOSCtrlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_SwL2DiffServTOSCtrlPortIndex_Type.__name__=_B
_SwL2DiffServTOSCtrlPortIndex_Object=MibTableColumn
swL2DiffServTOSCtrlPortIndex=_SwL2DiffServTOSCtrlPortIndex_Object((1,3,6,1,4,1,171,11,36,2,7,3,1,1),_SwL2DiffServTOSCtrlPortIndex_Type())
swL2DiffServTOSCtrlPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2DiffServTOSCtrlPortIndex.setStatus(_A)
class _SwL2DiffServTOSCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tos-Force-Overwrite',1),('tos-TOS-Overwrite-802dot1p',2),('tos-802dot1p-Overwrite-TOS',3)))
_SwL2DiffServTOSCtrlMode_Type.__name__=_B
_SwL2DiffServTOSCtrlMode_Object=MibTableColumn
swL2DiffServTOSCtrlMode=_SwL2DiffServTOSCtrlMode_Object((1,3,6,1,4,1,171,11,36,2,7,3,1,2),_SwL2DiffServTOSCtrlMode_Type())
swL2DiffServTOSCtrlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServTOSCtrlMode.setStatus(_A)
class _SwL2DiffServTOSCtrlValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwL2DiffServTOSCtrlValue_Type.__name__=_B
_SwL2DiffServTOSCtrlValue_Object=MibTableColumn
swL2DiffServTOSCtrlValue=_SwL2DiffServTOSCtrlValue_Object((1,3,6,1,4,1,171,11,36,2,7,3,1,3),_SwL2DiffServTOSCtrlValue_Type())
swL2DiffServTOSCtrlValue.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2DiffServTOSCtrlValue.setStatus(_A)
_SwL2PortMirrorMgmt_ObjectIdentity=ObjectIdentity
swL2PortMirrorMgmt=_SwL2PortMirrorMgmt_ObjectIdentity((1,3,6,1,4,1,171,11,36,2,8))
_SwL2PortMirrorSrcPortTable_Object=MibTable
swL2PortMirrorSrcPortTable=_SwL2PortMirrorSrcPortTable_Object((1,3,6,1,4,1,171,11,36,2,8,1))
if mibBuilder.loadTexts:swL2PortMirrorSrcPortTable.setStatus(_A)
_SwL2PortMirrorSrcPortEntry_Object=MibTableRow
swL2PortMirrorSrcPortEntry=_SwL2PortMirrorSrcPortEntry_Object((1,3,6,1,4,1,171,11,36,2,8,1,1))
swL2PortMirrorSrcPortEntry.setIndexNames((0,_H,_e))
if mibBuilder.loadTexts:swL2PortMirrorSrcPortEntry.setStatus(_A)
_SwL2PortMirrorIndex_Type=Integer32
_SwL2PortMirrorIndex_Object=MibTableColumn
swL2PortMirrorIndex=_SwL2PortMirrorIndex_Object((1,3,6,1,4,1,171,11,36,2,8,1,1,1),_SwL2PortMirrorIndex_Type())
swL2PortMirrorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swL2PortMirrorIndex.setStatus(_A)
class _SwL2PortMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('ingress',2),('egress',3),('both',4)))
_SwL2PortMirrorDirection_Type.__name__=_B
_SwL2PortMirrorDirection_Object=MibTableColumn
swL2PortMirrorDirection=_SwL2PortMirrorDirection_Object((1,3,6,1,4,1,171,11,36,2,8,1,1,2),_SwL2PortMirrorDirection_Type())
swL2PortMirrorDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortMirrorDirection.setStatus(_A)
_SwL2PortMirrorTargetPort_Type=Integer32
_SwL2PortMirrorTargetPort_Object=MibScalar
swL2PortMirrorTargetPort=_SwL2PortMirrorTargetPort_Object((1,3,6,1,4,1,171,11,36,2,8,2),_SwL2PortMirrorTargetPort_Type())
swL2PortMirrorTargetPort.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortMirrorTargetPort.setStatus(_A)
class _SwL2PortMirrorState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_SwL2PortMirrorState_Type.__name__=_B
_SwL2PortMirrorState_Object=MibScalar
swL2PortMirrorState=_SwL2PortMirrorState_Object((1,3,6,1,4,1,171,11,36,2,8,3),_SwL2PortMirrorState_Type())
swL2PortMirrorState.setMaxAccess(_C)
if mibBuilder.loadTexts:swL2PortMirrorState.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'VlanId':VlanId,'swL2Property':swL2Property,'swL2Module':swL2Module,'swL2MgmtMIB':swL2MgmtMIB,'swL2BwMgmt':swL2BwMgmt,'swL2BwMgmtFEPortUnitBandwidth':swL2BwMgmtFEPortUnitBandwidth,'swL2BwMgmtGEPortUnitBandwidth':swL2BwMgmtGEPortUnitBandwidth,'swL2IngrPortBwControl':swL2IngrPortBwControl,'swL2IngrPortBwCtrlTable':swL2IngrPortBwCtrlTable,'swL2IngrPortBwCtrlEntry':swL2IngrPortBwCtrlEntry,_R:swL2IngrPortBwCtrlPort,'swL2IngrPortBwCtrlPortCountType':swL2IngrPortBwCtrlPortCountType,'swL2IngrPortBwCtrlPortNwayStatus':swL2IngrPortBwCtrlPortNwayStatus,'swL2IngrPortBwCtrlUnit':swL2IngrPortBwCtrlUnit,'swL2IngrPortBwCtrlRate':swL2IngrPortBwCtrlRate,'swL2IngrPortBwCtrlStatus':swL2IngrPortBwCtrlStatus,'swL2EgressPortBwControl':swL2EgressPortBwControl,'swL2EgressPortBwCtrlTable':swL2EgressPortBwCtrlTable,'swL2EgressPortBwCtrlEntry':swL2EgressPortBwCtrlEntry,_V:swL2EgressPortBwCtrlPort,'swL2EgressPortBwCtrlPortCountType':swL2EgressPortBwCtrlPortCountType,'swL2EgressPortBwCtrlPortNwayStatus':swL2EgressPortBwCtrlPortNwayStatus,'swL2EgressPortBwCtrlUnit':swL2EgressPortBwCtrlUnit,'swL2EgressPortBwCtrlRate':swL2EgressPortBwCtrlRate,'swL2EgressPortBwCtrlStatus':swL2EgressPortBwCtrlStatus,'swL2GrpAddrFltrMode':swL2GrpAddrFltrMode,'swL2CosMgmt':swL2CosMgmt,'swL2CosScheduleMethod':swL2CosScheduleMethod,'swL2CosControlTable':swL2CosControlTable,'swL2CosControlEntry':swL2CosControlEntry,_W:swL2CosQueueIndex,'swL2CosMaxPackets':swL2CosMaxPackets,'swL2CosMaxLatency':swL2CosMaxLatency,'swL2PortSecurityMgmt':swL2PortSecurityMgmt,'swL2PortSecurityControlTable':swL2PortSecurityControlTable,'swL2PortSecurityControlEntry':swL2PortSecurityControlEntry,_X:swL2PortSecurityPortIndex,'swL2PortSecurityMaxLernAddr':swL2PortSecurityMaxLernAddr,'swL2PortSecurityMode':swL2PortSecurityMode,'swL2PortSecurityAdmState':swL2PortSecurityAdmState,'swL2DevMgmt':swL2DevMgmt,'swL2DevInfo':swL2DevInfo,'swL2DevInfoSystemUpTime':swL2DevInfoSystemUpTime,'swL2DevInfoTotalNumOfPort':swL2DevInfoTotalNumOfPort,'swL2DevInfoNumOfPortInUse':swL2DevInfoNumOfPortInUse,'swL2DevInfoConsoleInUse':swL2DevInfoConsoleInUse,'swL2DevInfoFrontPanelLedStatus':swL2DevInfoFrontPanelLedStatus,'swL2DevInfoCpuUtilization':swL2DevInfoCpuUtilization,'swL2DevCtrl':swL2DevCtrl,'swL2DevCtrlSystemReboot':swL2DevCtrlSystemReboot,'swL2DevCtrlSystemIP':swL2DevCtrlSystemIP,'swL2DevCtrlSubnetMask':swL2DevCtrlSubnetMask,'swL2DevCtrlDefaultGateway':swL2DevCtrlDefaultGateway,'swL2DevCtrlManagementVlanId':swL2DevCtrlManagementVlanId,'swL2DevCtrlStpState':swL2DevCtrlStpState,'swL2DevCtrlIGMPSnooping':swL2DevCtrlIGMPSnooping,'swL2DevCtrlBcastStormCtrl':swL2DevCtrlBcastStormCtrl,'swL2DevCtrlMcastStormCtrl':swL2DevCtrlMcastStormCtrl,'swL2DevCtrlDestLookupFailureCtrl':swL2DevCtrlDestLookupFailureCtrl,'swL2DevCtrlBMDStormLimit':swL2DevCtrlBMDStormLimit,'swL2DevCtrlCleanAllStatisticCounter':swL2DevCtrlCleanAllStatisticCounter,'swL2DevCtrlSnmpEnableAuthenTraps':swL2DevCtrlSnmpEnableAuthenTraps,'swL2DevCtrlFilterEAPOLPDU':swL2DevCtrlFilterEAPOLPDU,'swL2DevCtrlTrafficSegmentation':swL2DevCtrlTrafficSegmentation,'agentPingTest':agentPingTest,'agentPingTestIPAddress':agentPingTestIPAddress,'agentPingTestRepetition':agentPingTestRepetition,'agentPingTestControl':agentPingTestControl,'agentPingTestStatus':agentPingTestStatus,'agentPingTestSuccessCount':agentPingTestSuccessCount,'agentPingTestFailCount':agentPingTestFailCount,'swL2DevCtrlVlanIdOfFDBTbl':swL2DevCtrlVlanIdOfFDBTbl,'swL2PortMgmt':swL2PortMgmt,'swL2PortInfoTable':swL2PortInfoTable,'swL2PortInfoEntry':swL2PortInfoEntry,_Z:swL2PortInfoPortIndex,'swL2PortInfoType':swL2PortInfoType,'swL2PortInfoDescr':swL2PortInfoDescr,'swL2PortInfoLinkStatus':swL2PortInfoLinkStatus,'swL2PortInfoNwayStatus':swL2PortInfoNwayStatus,'swL2PortCtrlTable':swL2PortCtrlTable,'swL2PortCtrlEntry':swL2PortCtrlEntry,_a:swL2PortCtrlPortIndex,'swL2PortCtrlAdminState':swL2PortCtrlAdminState,'swL2PortCtrlNwayState':swL2PortCtrlNwayState,'swL2PortCtrlFlowCtrlState':swL2PortCtrlFlowCtrlState,'swL2PortCtrlCleanStatCounter':swL2PortCtrlCleanStatCounter,'swL2PortCtrlDescription':swL2PortCtrlDescription,'swL2DiffServMgmt':swL2DiffServMgmt,'swL2DiffServTypeCtrlTable':swL2DiffServTypeCtrlTable,'swL2DiffServTypeCtrlEntry':swL2DiffServTypeCtrlEntry,_b:swL2DiffServTypeCtrlPortIndex,'swL2DiffServTypeCtrlDiffServType':swL2DiffServTypeCtrlDiffServType,'swL2DiffServDSCPCtrlTable':swL2DiffServDSCPCtrlTable,'swL2DiffServDSCPCtrlEntry':swL2DiffServDSCPCtrlEntry,_c:swL2DiffServDSCPCtrlPortIndex,'swL2DiffServDSCPCtrlMode':swL2DiffServDSCPCtrlMode,'swL2DiffServDSCPCtrlValue':swL2DiffServDSCPCtrlValue,'swL2DiffServTOSCtrlTable':swL2DiffServTOSCtrlTable,'swL2DiffServTOSCtrlEntry':swL2DiffServTOSCtrlEntry,_d:swL2DiffServTOSCtrlPortIndex,'swL2DiffServTOSCtrlMode':swL2DiffServTOSCtrlMode,'swL2DiffServTOSCtrlValue':swL2DiffServTOSCtrlValue,'swL2PortMirrorMgmt':swL2PortMirrorMgmt,'swL2PortMirrorSrcPortTable':swL2PortMirrorSrcPortTable,'swL2PortMirrorSrcPortEntry':swL2PortMirrorSrcPortEntry,_e:swL2PortMirrorIndex,'swL2PortMirrorDirection':swL2PortMirrorDirection,'swL2PortMirrorTargetPort':swL2PortMirrorTargetPort,'swL2PortMirrorState':swL2PortMirrorState})