_Z='fsIpDbv6HostMac'
_Y='fsIpDbv6HostVlanId'
_X='fsIpDbv6StaticHostMac'
_W='fsIpDbv6StaticHostVlanId'
_V='fsIpArpInsVlanId'
_U='disabled'
_T='enabled'
_S='fsIpDbSrcGuardIndex'
_R='fsIpDbIntfVlanId'
_Q='fsIpDbGatewayIp'
_P='fsIpDbGatewayNetMask'
_O='fsIpDbGatewayNetwork'
_N='static'
_M='fsIpDbStaticHostMac'
_L='fsIpDbStaticHostVlanId'
_K='enable'
_J='fsIpDbHostMac'
_I='fsIpDbHostVlanId'
_H='disable'
_G='TruthValue'
_F='not-accessible'
_E='Integer32'
_D='ARICENT-IPDB-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
fsipdb=ModuleIdentity((1,3,6,1,4,1,29601,2,2))
if mibBuilder.loadTexts:fsipdb.setRevisions(('2012-09-05 00:00','2010-05-24 00:00','2010-05-17 00:00'))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsIpDbScalars_ObjectIdentity=ObjectIdentity
fsIpDbScalars=_FsIpDbScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,2,1))
_FsIpDbNoOfBindings_Type=Counter32
_FsIpDbNoOfBindings_Object=MibScalar
fsIpDbNoOfBindings=_FsIpDbNoOfBindings_Object((1,3,6,1,4,1,29601,2,2,1,1),_FsIpDbNoOfBindings_Type())
fsIpDbNoOfBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfBindings.setStatus(_A)
_FsIpDbNoOfStaticBindings_Type=Counter32
_FsIpDbNoOfStaticBindings_Object=MibScalar
fsIpDbNoOfStaticBindings=_FsIpDbNoOfStaticBindings_Object((1,3,6,1,4,1,29601,2,2,1,2),_FsIpDbNoOfStaticBindings_Type())
fsIpDbNoOfStaticBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfStaticBindings.setStatus(_A)
_FsIpDbNoOfDHCPBindings_Type=Counter32
_FsIpDbNoOfDHCPBindings_Object=MibScalar
fsIpDbNoOfDHCPBindings=_FsIpDbNoOfDHCPBindings_Object((1,3,6,1,4,1,29601,2,2,1,3),_FsIpDbNoOfDHCPBindings_Type())
fsIpDbNoOfDHCPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfDHCPBindings.setStatus(_A)
_FsIpDbNoOfPPPBindings_Type=Counter32
_FsIpDbNoOfPPPBindings_Object=MibScalar
fsIpDbNoOfPPPBindings=_FsIpDbNoOfPPPBindings_Object((1,3,6,1,4,1,29601,2,2,1,4),_FsIpDbNoOfPPPBindings_Type())
fsIpDbNoOfPPPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfPPPBindings.setStatus(_A)
_FsIpDbTraceLevel_Type=Integer32
_FsIpDbTraceLevel_Object=MibScalar
fsIpDbTraceLevel=_FsIpDbTraceLevel_Object((1,3,6,1,4,1,29601,2,2,1,5),_FsIpDbTraceLevel_Type())
fsIpDbTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbTraceLevel.setStatus(_A)
class _FsIpDbv6DynamicDbSaveStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_H,2)))
_FsIpDbv6DynamicDbSaveStatus_Type.__name__=_E
_FsIpDbv6DynamicDbSaveStatus_Object=MibScalar
fsIpDbv6DynamicDbSaveStatus=_FsIpDbv6DynamicDbSaveStatus_Object((1,3,6,1,4,1,29601,2,2,1,6),_FsIpDbv6DynamicDbSaveStatus_Type())
fsIpDbv6DynamicDbSaveStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6DynamicDbSaveStatus.setStatus(_A)
class _FsIpDbClearBindingStatus_Type(TruthValue):defaultValue=2
_FsIpDbClearBindingStatus_Type.__name__=_G
_FsIpDbClearBindingStatus_Object=MibScalar
fsIpDbClearBindingStatus=_FsIpDbClearBindingStatus_Object((1,3,6,1,4,1,29601,2,2,1,7),_FsIpDbClearBindingStatus_Type())
fsIpDbClearBindingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbClearBindingStatus.setStatus(_A)
class _FsIpDbv6ClearBindingStatus_Type(TruthValue):defaultValue=2
_FsIpDbv6ClearBindingStatus_Type.__name__=_G
_FsIpDbv6ClearBindingStatus_Object=MibScalar
fsIpDbv6ClearBindingStatus=_FsIpDbv6ClearBindingStatus_Object((1,3,6,1,4,1,29601,2,2,1,8),_FsIpDbv6ClearBindingStatus_Type())
fsIpDbv6ClearBindingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6ClearBindingStatus.setStatus(_A)
_FsIpDbStatic_ObjectIdentity=ObjectIdentity
fsIpDbStatic=_FsIpDbStatic_ObjectIdentity((1,3,6,1,4,1,29601,2,2,2))
_FsIpDbStaticBindingTable_Object=MibTable
fsIpDbStaticBindingTable=_FsIpDbStaticBindingTable_Object((1,3,6,1,4,1,29601,2,2,2,1))
if mibBuilder.loadTexts:fsIpDbStaticBindingTable.setStatus(_A)
_FsIpDbStaticBindingEntry_Object=MibTableRow
fsIpDbStaticBindingEntry=_FsIpDbStaticBindingEntry_Object((1,3,6,1,4,1,29601,2,2,2,1,1))
fsIpDbStaticBindingEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:fsIpDbStaticBindingEntry.setStatus(_A)
class _FsIpDbStaticHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbStaticHostVlanId_Type.__name__=_E
_FsIpDbStaticHostVlanId_Object=MibTableColumn
fsIpDbStaticHostVlanId=_FsIpDbStaticHostVlanId_Object((1,3,6,1,4,1,29601,2,2,2,1,1,1),_FsIpDbStaticHostVlanId_Type())
fsIpDbStaticHostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbStaticHostVlanId.setStatus(_A)
_FsIpDbStaticHostMac_Type=MacAddress
_FsIpDbStaticHostMac_Object=MibTableColumn
fsIpDbStaticHostMac=_FsIpDbStaticHostMac_Object((1,3,6,1,4,1,29601,2,2,2,1,1,2),_FsIpDbStaticHostMac_Type())
fsIpDbStaticHostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbStaticHostMac.setStatus(_A)
_FsIpDbStaticHostIp_Type=IpAddress
_FsIpDbStaticHostIp_Object=MibTableColumn
fsIpDbStaticHostIp=_FsIpDbStaticHostIp_Object((1,3,6,1,4,1,29601,2,2,2,1,1,3),_FsIpDbStaticHostIp_Type())
fsIpDbStaticHostIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbStaticHostIp.setStatus(_A)
_FsIpDbStaticInIfIndex_Type=Integer32
_FsIpDbStaticInIfIndex_Object=MibTableColumn
fsIpDbStaticInIfIndex=_FsIpDbStaticInIfIndex_Object((1,3,6,1,4,1,29601,2,2,2,1,1,4),_FsIpDbStaticInIfIndex_Type())
fsIpDbStaticInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbStaticInIfIndex.setStatus(_A)
_FsIpDbStaticGateway_Type=IpAddress
_FsIpDbStaticGateway_Object=MibTableColumn
fsIpDbStaticGateway=_FsIpDbStaticGateway_Object((1,3,6,1,4,1,29601,2,2,2,1,1,5),_FsIpDbStaticGateway_Type())
fsIpDbStaticGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbStaticGateway.setStatus(_A)
_FsIpDbStaticBindingStatus_Type=RowStatus
_FsIpDbStaticBindingStatus_Object=MibTableColumn
fsIpDbStaticBindingStatus=_FsIpDbStaticBindingStatus_Object((1,3,6,1,4,1,29601,2,2,2,1,1,6),_FsIpDbStaticBindingStatus_Type())
fsIpDbStaticBindingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbStaticBindingStatus.setStatus(_A)
_FsIpDbBindings_ObjectIdentity=ObjectIdentity
fsIpDbBindings=_FsIpDbBindings_ObjectIdentity((1,3,6,1,4,1,29601,2,2,3))
_FsIpDbBindingTable_Object=MibTable
fsIpDbBindingTable=_FsIpDbBindingTable_Object((1,3,6,1,4,1,29601,2,2,3,1))
if mibBuilder.loadTexts:fsIpDbBindingTable.setStatus(_A)
_FsIpDbBindingEntry_Object=MibTableRow
fsIpDbBindingEntry=_FsIpDbBindingEntry_Object((1,3,6,1,4,1,29601,2,2,3,1,1))
fsIpDbBindingEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:fsIpDbBindingEntry.setStatus(_A)
class _FsIpDbHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbHostVlanId_Type.__name__=_E
_FsIpDbHostVlanId_Object=MibTableColumn
fsIpDbHostVlanId=_FsIpDbHostVlanId_Object((1,3,6,1,4,1,29601,2,2,3,1,1,1),_FsIpDbHostVlanId_Type())
fsIpDbHostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbHostVlanId.setStatus(_A)
_FsIpDbHostMac_Type=MacAddress
_FsIpDbHostMac_Object=MibTableColumn
fsIpDbHostMac=_FsIpDbHostMac_Object((1,3,6,1,4,1,29601,2,2,3,1,1,2),_FsIpDbHostMac_Type())
fsIpDbHostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbHostMac.setStatus(_A)
class _FsIpDbHostBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('dhcp',2),('ppp',3)))
_FsIpDbHostBindingType_Type.__name__=_E
_FsIpDbHostBindingType_Object=MibTableColumn
fsIpDbHostBindingType=_FsIpDbHostBindingType_Object((1,3,6,1,4,1,29601,2,2,3,1,1,3),_FsIpDbHostBindingType_Type())
fsIpDbHostBindingType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostBindingType.setStatus(_A)
_FsIpDbHostIp_Type=IpAddress
_FsIpDbHostIp_Object=MibTableColumn
fsIpDbHostIp=_FsIpDbHostIp_Object((1,3,6,1,4,1,29601,2,2,3,1,1,4),_FsIpDbHostIp_Type())
fsIpDbHostIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostIp.setStatus(_A)
_FsIpDbHostInIfIndex_Type=Integer32
_FsIpDbHostInIfIndex_Object=MibTableColumn
fsIpDbHostInIfIndex=_FsIpDbHostInIfIndex_Object((1,3,6,1,4,1,29601,2,2,3,1,1,5),_FsIpDbHostInIfIndex_Type())
fsIpDbHostInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostInIfIndex.setStatus(_A)
_FsIpDbHostRemLeaseTime_Type=Integer32
_FsIpDbHostRemLeaseTime_Object=MibTableColumn
fsIpDbHostRemLeaseTime=_FsIpDbHostRemLeaseTime_Object((1,3,6,1,4,1,29601,2,2,3,1,1,6),_FsIpDbHostRemLeaseTime_Type())
fsIpDbHostRemLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostRemLeaseTime.setStatus(_A)
_FsIpDbHostBindingID_Type=Unsigned32
_FsIpDbHostBindingID_Object=MibTableColumn
fsIpDbHostBindingID=_FsIpDbHostBindingID_Object((1,3,6,1,4,1,29601,2,2,3,1,1,7),_FsIpDbHostBindingID_Type())
fsIpDbHostBindingID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostBindingID.setStatus(_A)
_FsIpDbGatewayIpTable_Object=MibTable
fsIpDbGatewayIpTable=_FsIpDbGatewayIpTable_Object((1,3,6,1,4,1,29601,2,2,3,2))
if mibBuilder.loadTexts:fsIpDbGatewayIpTable.setStatus(_A)
_FsIpDbGatewayIpEntry_Object=MibTableRow
fsIpDbGatewayIpEntry=_FsIpDbGatewayIpEntry_Object((1,3,6,1,4,1,29601,2,2,3,2,1))
fsIpDbGatewayIpEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:fsIpDbGatewayIpEntry.setStatus(_A)
_FsIpDbGatewayNetwork_Type=IpAddress
_FsIpDbGatewayNetwork_Object=MibTableColumn
fsIpDbGatewayNetwork=_FsIpDbGatewayNetwork_Object((1,3,6,1,4,1,29601,2,2,3,2,1,1),_FsIpDbGatewayNetwork_Type())
fsIpDbGatewayNetwork.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbGatewayNetwork.setStatus(_A)
_FsIpDbGatewayNetMask_Type=IpAddress
_FsIpDbGatewayNetMask_Object=MibTableColumn
fsIpDbGatewayNetMask=_FsIpDbGatewayNetMask_Object((1,3,6,1,4,1,29601,2,2,3,2,1,2),_FsIpDbGatewayNetMask_Type())
fsIpDbGatewayNetMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbGatewayNetMask.setStatus(_A)
_FsIpDbGatewayIp_Type=IpAddress
_FsIpDbGatewayIp_Object=MibTableColumn
fsIpDbGatewayIp=_FsIpDbGatewayIp_Object((1,3,6,1,4,1,29601,2,2,3,2,1,3),_FsIpDbGatewayIp_Type())
fsIpDbGatewayIp.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbGatewayIp.setStatus(_A)
class _FsIpDbGatewayIpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('active',0))
_FsIpDbGatewayIpMode_Type.__name__=_E
_FsIpDbGatewayIpMode_Object=MibTableColumn
fsIpDbGatewayIpMode=_FsIpDbGatewayIpMode_Object((1,3,6,1,4,1,29601,2,2,3,2,1,4),_FsIpDbGatewayIpMode_Type())
fsIpDbGatewayIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbGatewayIpMode.setStatus(_A)
_FsIpDbInterface_ObjectIdentity=ObjectIdentity
fsIpDbInterface=_FsIpDbInterface_ObjectIdentity((1,3,6,1,4,1,29601,2,2,4))
_FsIpDbInterfaceTable_Object=MibTable
fsIpDbInterfaceTable=_FsIpDbInterfaceTable_Object((1,3,6,1,4,1,29601,2,2,4,1))
if mibBuilder.loadTexts:fsIpDbInterfaceTable.setStatus(_A)
_FsIpDbInterfaceEntry_Object=MibTableRow
fsIpDbInterfaceEntry=_FsIpDbInterfaceEntry_Object((1,3,6,1,4,1,29601,2,2,4,1,1))
fsIpDbInterfaceEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:fsIpDbInterfaceEntry.setStatus(_A)
class _FsIpDbIntfVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbIntfVlanId_Type.__name__=_E
_FsIpDbIntfVlanId_Object=MibTableColumn
fsIpDbIntfVlanId=_FsIpDbIntfVlanId_Object((1,3,6,1,4,1,29601,2,2,4,1,1,1),_FsIpDbIntfVlanId_Type())
fsIpDbIntfVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbIntfVlanId.setStatus(_A)
_FsIpDbIntfNoOfVlanBindings_Type=Counter32
_FsIpDbIntfNoOfVlanBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanBindings=_FsIpDbIntfNoOfVlanBindings_Object((1,3,6,1,4,1,29601,2,2,4,1,1,2),_FsIpDbIntfNoOfVlanBindings_Type())
fsIpDbIntfNoOfVlanBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanBindings.setStatus(_A)
_FsIpDbIntfNoOfVlanStaticBindings_Type=Counter32
_FsIpDbIntfNoOfVlanStaticBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanStaticBindings=_FsIpDbIntfNoOfVlanStaticBindings_Object((1,3,6,1,4,1,29601,2,2,4,1,1,3),_FsIpDbIntfNoOfVlanStaticBindings_Type())
fsIpDbIntfNoOfVlanStaticBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanStaticBindings.setStatus(_A)
_FsIpDbIntfNoOfVlanDHCPBindings_Type=Counter32
_FsIpDbIntfNoOfVlanDHCPBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanDHCPBindings=_FsIpDbIntfNoOfVlanDHCPBindings_Object((1,3,6,1,4,1,29601,2,2,4,1,1,4),_FsIpDbIntfNoOfVlanDHCPBindings_Type())
fsIpDbIntfNoOfVlanDHCPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanDHCPBindings.setStatus(_A)
_FsIpDbIntfNoOfVlanPPPBindings_Type=Counter32
_FsIpDbIntfNoOfVlanPPPBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanPPPBindings=_FsIpDbIntfNoOfVlanPPPBindings_Object((1,3,6,1,4,1,29601,2,2,4,1,1,5),_FsIpDbIntfNoOfVlanPPPBindings_Type())
fsIpDbIntfNoOfVlanPPPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanPPPBindings.setStatus(_A)
_FsIpDbIntfNoOfVlanDHCPv6Bindings_Type=Counter32
_FsIpDbIntfNoOfVlanDHCPv6Bindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanDHCPv6Bindings=_FsIpDbIntfNoOfVlanDHCPv6Bindings_Object((1,3,6,1,4,1,29601,2,2,4,1,1,6),_FsIpDbIntfNoOfVlanDHCPv6Bindings_Type())
fsIpDbIntfNoOfVlanDHCPv6Bindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanDHCPv6Bindings.setStatus(_A)
_FsIpDbIntfNoOfVlanStaticv6Bindings_Type=Counter32
_FsIpDbIntfNoOfVlanStaticv6Bindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanStaticv6Bindings=_FsIpDbIntfNoOfVlanStaticv6Bindings_Object((1,3,6,1,4,1,29601,2,2,4,1,1,7),_FsIpDbIntfNoOfVlanStaticv6Bindings_Type())
fsIpDbIntfNoOfVlanStaticv6Bindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanStaticv6Bindings.setStatus(_A)
_FsIpDbSrcGuard_ObjectIdentity=ObjectIdentity
fsIpDbSrcGuard=_FsIpDbSrcGuard_ObjectIdentity((1,3,6,1,4,1,29601,2,2,5))
_FsIpDbSrcGuardConfigTable_Object=MibTable
fsIpDbSrcGuardConfigTable=_FsIpDbSrcGuardConfigTable_Object((1,3,6,1,4,1,29601,2,2,5,1))
if mibBuilder.loadTexts:fsIpDbSrcGuardConfigTable.setStatus(_A)
_FsIpDbSrcGuardConfigEntry_Object=MibTableRow
fsIpDbSrcGuardConfigEntry=_FsIpDbSrcGuardConfigEntry_Object((1,3,6,1,4,1,29601,2,2,5,1,1))
fsIpDbSrcGuardConfigEntry.setIndexNames((0,_D,_S))
if mibBuilder.loadTexts:fsIpDbSrcGuardConfigEntry.setStatus(_A)
_FsIpDbSrcGuardIndex_Type=InterfaceIndex
_FsIpDbSrcGuardIndex_Object=MibTableColumn
fsIpDbSrcGuardIndex=_FsIpDbSrcGuardIndex_Object((1,3,6,1,4,1,29601,2,2,5,1,1,1),_FsIpDbSrcGuardIndex_Type())
fsIpDbSrcGuardIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbSrcGuardIndex.setStatus(_A)
class _FsIpDbSrcGuardStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('ip',2),('ipMac',3)))
_FsIpDbSrcGuardStatus_Type.__name__=_E
_FsIpDbSrcGuardStatus_Object=MibTableColumn
fsIpDbSrcGuardStatus=_FsIpDbSrcGuardStatus_Object((1,3,6,1,4,1,29601,2,2,5,1,1,2),_FsIpDbSrcGuardStatus_Type())
fsIpDbSrcGuardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbSrcGuardStatus.setStatus(_A)
class _FsIpDbv6SrcGuardStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_H,2)))
_FsIpDbv6SrcGuardStatus_Type.__name__=_E
_FsIpDbv6SrcGuardStatus_Object=MibTableColumn
fsIpDbv6SrcGuardStatus=_FsIpDbv6SrcGuardStatus_Object((1,3,6,1,4,1,29601,2,2,5,1,1,3),_FsIpDbv6SrcGuardStatus_Type())
fsIpDbv6SrcGuardStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6SrcGuardStatus.setStatus(_A)
_FsIpArpInspect_ObjectIdentity=ObjectIdentity
fsIpArpInspect=_FsIpArpInspect_ObjectIdentity((1,3,6,1,4,1,29601,2,2,6))
class _FsIpArpInspectionStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FsIpArpInspectionStatus_Type.__name__=_E
_FsIpArpInspectionStatus_Object=MibScalar
fsIpArpInspectionStatus=_FsIpArpInspectionStatus_Object((1,3,6,1,4,1,29601,2,2,6,1),_FsIpArpInspectionStatus_Type())
fsIpArpInspectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpArpInspectionStatus.setStatus(_A)
class _FsIpArpInsValidateOption_Type(Bits):defaultHexValue='';namedValues=NamedValues(*(('srcmac',1),('dstmac',2),('ip',3)))
_FsIpArpInsValidateOption_Type.__name__='Bits'
_FsIpArpInsValidateOption_Object=MibScalar
fsIpArpInsValidateOption=_FsIpArpInsValidateOption_Object((1,3,6,1,4,1,29601,2,2,6,2),_FsIpArpInsValidateOption_Type())
fsIpArpInsValidateOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpArpInsValidateOption.setStatus(_A)
_FsIpArpInsArpPktsForwarded_Type=Counter32
_FsIpArpInsArpPktsForwarded_Object=MibScalar
fsIpArpInsArpPktsForwarded=_FsIpArpInsArpPktsForwarded_Object((1,3,6,1,4,1,29601,2,2,6,3),_FsIpArpInsArpPktsForwarded_Type())
fsIpArpInsArpPktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsArpPktsForwarded.setStatus(_A)
_FsIpArpInsArpPktsDropped_Type=Counter32
_FsIpArpInsArpPktsDropped_Object=MibScalar
fsIpArpInsArpPktsDropped=_FsIpArpInsArpPktsDropped_Object((1,3,6,1,4,1,29601,2,2,6,4),_FsIpArpInsArpPktsDropped_Type())
fsIpArpInsArpPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsArpPktsDropped.setStatus(_A)
_FsIpArpInsIPValidFailures_Type=Counter32
_FsIpArpInsIPValidFailures_Object=MibScalar
fsIpArpInsIPValidFailures=_FsIpArpInsIPValidFailures_Object((1,3,6,1,4,1,29601,2,2,6,5),_FsIpArpInsIPValidFailures_Type())
fsIpArpInsIPValidFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsIPValidFailures.setStatus(_A)
_FsIpArpInsDestMACFailures_Type=Counter32
_FsIpArpInsDestMACFailures_Object=MibScalar
fsIpArpInsDestMACFailures=_FsIpArpInsDestMACFailures_Object((1,3,6,1,4,1,29601,2,2,6,6),_FsIpArpInsDestMACFailures_Type())
fsIpArpInsDestMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsDestMACFailures.setStatus(_A)
_FsIpArpInsSrcMACFailures_Type=Counter32
_FsIpArpInsSrcMACFailures_Object=MibScalar
fsIpArpInsSrcMACFailures=_FsIpArpInsSrcMACFailures_Object((1,3,6,1,4,1,29601,2,2,6,7),_FsIpArpInsSrcMACFailures_Type())
fsIpArpInsSrcMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsSrcMACFailures.setStatus(_A)
class _FsIpArpInsGlobalStatsClear_Type(TruthValue):defaultValue=2
_FsIpArpInsGlobalStatsClear_Type.__name__=_G
_FsIpArpInsGlobalStatsClear_Object=MibScalar
fsIpArpInsGlobalStatsClear=_FsIpArpInsGlobalStatsClear_Object((1,3,6,1,4,1,29601,2,2,6,8),_FsIpArpInsGlobalStatsClear_Type())
fsIpArpInsGlobalStatsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpArpInsGlobalStatsClear.setStatus(_A)
_FsIpArpInsVlanTable_Object=MibTable
fsIpArpInsVlanTable=_FsIpArpInsVlanTable_Object((1,3,6,1,4,1,29601,2,2,6,9))
if mibBuilder.loadTexts:fsIpArpInsVlanTable.setStatus(_A)
_FsIpArpInsVlanEntry_Object=MibTableRow
fsIpArpInsVlanEntry=_FsIpArpInsVlanEntry_Object((1,3,6,1,4,1,29601,2,2,6,9,1))
fsIpArpInsVlanEntry.setIndexNames((0,_D,_V))
if mibBuilder.loadTexts:fsIpArpInsVlanEntry.setStatus(_A)
class _FsIpArpInsVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpArpInsVlanId_Type.__name__=_E
_FsIpArpInsVlanId_Object=MibTableColumn
fsIpArpInsVlanId=_FsIpArpInsVlanId_Object((1,3,6,1,4,1,29601,2,2,6,9,1,1),_FsIpArpInsVlanId_Type())
fsIpArpInsVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpArpInsVlanId.setStatus(_A)
class _FsIpArpInsVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_T,1),(_U,2)))
_FsIpArpInsVlanStatus_Type.__name__=_E
_FsIpArpInsVlanStatus_Object=MibTableColumn
fsIpArpInsVlanStatus=_FsIpArpInsVlanStatus_Object((1,3,6,1,4,1,29601,2,2,6,9,1,2),_FsIpArpInsVlanStatus_Type())
fsIpArpInsVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpArpInsVlanStatus.setStatus(_A)
_FsIpArpInsVlanArpPktsForwarded_Type=Integer32
_FsIpArpInsVlanArpPktsForwarded_Object=MibTableColumn
fsIpArpInsVlanArpPktsForwarded=_FsIpArpInsVlanArpPktsForwarded_Object((1,3,6,1,4,1,29601,2,2,6,9,1,3),_FsIpArpInsVlanArpPktsForwarded_Type())
fsIpArpInsVlanArpPktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsVlanArpPktsForwarded.setStatus(_A)
_FsIpArpInsVlanArpPktsDropped_Type=Integer32
_FsIpArpInsVlanArpPktsDropped_Object=MibTableColumn
fsIpArpInsVlanArpPktsDropped=_FsIpArpInsVlanArpPktsDropped_Object((1,3,6,1,4,1,29601,2,2,6,9,1,4),_FsIpArpInsVlanArpPktsDropped_Type())
fsIpArpInsVlanArpPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsVlanArpPktsDropped.setStatus(_A)
_FsIpArpInsVlanIPValidFailures_Type=Integer32
_FsIpArpInsVlanIPValidFailures_Object=MibTableColumn
fsIpArpInsVlanIPValidFailures=_FsIpArpInsVlanIPValidFailures_Object((1,3,6,1,4,1,29601,2,2,6,9,1,5),_FsIpArpInsVlanIPValidFailures_Type())
fsIpArpInsVlanIPValidFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsVlanIPValidFailures.setStatus(_A)
_FsIpArpInsVlanDestMACFailures_Type=Integer32
_FsIpArpInsVlanDestMACFailures_Object=MibTableColumn
fsIpArpInsVlanDestMACFailures=_FsIpArpInsVlanDestMACFailures_Object((1,3,6,1,4,1,29601,2,2,6,9,1,6),_FsIpArpInsVlanDestMACFailures_Type())
fsIpArpInsVlanDestMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsVlanDestMACFailures.setStatus(_A)
_FsIpArpInsVlanSrcMACFailures_Type=Integer32
_FsIpArpInsVlanSrcMACFailures_Object=MibTableColumn
fsIpArpInsVlanSrcMACFailures=_FsIpArpInsVlanSrcMACFailures_Object((1,3,6,1,4,1,29601,2,2,6,9,1,7),_FsIpArpInsVlanSrcMACFailures_Type())
fsIpArpInsVlanSrcMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpArpInsVlanSrcMACFailures.setStatus(_A)
class _FsIpArpInsVlanClearStats_Type(TruthValue):defaultValue=2
_FsIpArpInsVlanClearStats_Type.__name__=_G
_FsIpArpInsVlanClearStats_Object=MibTableColumn
fsIpArpInsVlanClearStats=_FsIpArpInsVlanClearStats_Object((1,3,6,1,4,1,29601,2,2,6,9,1,8),_FsIpArpInsVlanClearStats_Type())
fsIpArpInsVlanClearStats.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpArpInsVlanClearStats.setStatus(_A)
_FsIpArpInsVlanRowStatus_Type=RowStatus
_FsIpArpInsVlanRowStatus_Object=MibTableColumn
fsIpArpInsVlanRowStatus=_FsIpArpInsVlanRowStatus_Object((1,3,6,1,4,1,29601,2,2,6,9,1,9),_FsIpArpInsVlanRowStatus_Type())
fsIpArpInsVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpArpInsVlanRowStatus.setStatus(_A)
_FsIpDbv6Static_ObjectIdentity=ObjectIdentity
fsIpDbv6Static=_FsIpDbv6Static_ObjectIdentity((1,3,6,1,4,1,29601,2,2,7))
_FsIpDbv6StaticBindingTable_Object=MibTable
fsIpDbv6StaticBindingTable=_FsIpDbv6StaticBindingTable_Object((1,3,6,1,4,1,29601,2,2,7,1))
if mibBuilder.loadTexts:fsIpDbv6StaticBindingTable.setStatus(_A)
_FsIpDbv6StaticBindingEntry_Object=MibTableRow
fsIpDbv6StaticBindingEntry=_FsIpDbv6StaticBindingEntry_Object((1,3,6,1,4,1,29601,2,2,7,1,1))
fsIpDbv6StaticBindingEntry.setIndexNames((0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:fsIpDbv6StaticBindingEntry.setStatus(_A)
class _FsIpDbv6StaticHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbv6StaticHostVlanId_Type.__name__=_E
_FsIpDbv6StaticHostVlanId_Object=MibTableColumn
fsIpDbv6StaticHostVlanId=_FsIpDbv6StaticHostVlanId_Object((1,3,6,1,4,1,29601,2,2,7,1,1,1),_FsIpDbv6StaticHostVlanId_Type())
fsIpDbv6StaticHostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbv6StaticHostVlanId.setStatus(_A)
_FsIpDbv6StaticHostMac_Type=MacAddress
_FsIpDbv6StaticHostMac_Object=MibTableColumn
fsIpDbv6StaticHostMac=_FsIpDbv6StaticHostMac_Object((1,3,6,1,4,1,29601,2,2,7,1,1,2),_FsIpDbv6StaticHostMac_Type())
fsIpDbv6StaticHostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbv6StaticHostMac.setStatus(_A)
_FsIpDbv6StaticHostIp_Type=Ipv6Address
_FsIpDbv6StaticHostIp_Object=MibTableColumn
fsIpDbv6StaticHostIp=_FsIpDbv6StaticHostIp_Object((1,3,6,1,4,1,29601,2,2,7,1,1,3),_FsIpDbv6StaticHostIp_Type())
fsIpDbv6StaticHostIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6StaticHostIp.setStatus(_A)
_FsIpDbv6StaticInIfIndex_Type=Integer32
_FsIpDbv6StaticInIfIndex_Object=MibTableColumn
fsIpDbv6StaticInIfIndex=_FsIpDbv6StaticInIfIndex_Object((1,3,6,1,4,1,29601,2,2,7,1,1,4),_FsIpDbv6StaticInIfIndex_Type())
fsIpDbv6StaticInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6StaticInIfIndex.setStatus(_A)
_FsIpDbv6StaticBindingStatus_Type=RowStatus
_FsIpDbv6StaticBindingStatus_Object=MibTableColumn
fsIpDbv6StaticBindingStatus=_FsIpDbv6StaticBindingStatus_Object((1,3,6,1,4,1,29601,2,2,7,1,1,6),_FsIpDbv6StaticBindingStatus_Type())
fsIpDbv6StaticBindingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6StaticBindingStatus.setStatus(_A)
_FsIpDbv6Bindings_ObjectIdentity=ObjectIdentity
fsIpDbv6Bindings=_FsIpDbv6Bindings_ObjectIdentity((1,3,6,1,4,1,29601,2,2,8))
_FsIpDbv6BindingTable_Object=MibTable
fsIpDbv6BindingTable=_FsIpDbv6BindingTable_Object((1,3,6,1,4,1,29601,2,2,8,1))
if mibBuilder.loadTexts:fsIpDbv6BindingTable.setStatus(_A)
_FsIpDbv6BindingEntry_Object=MibTableRow
fsIpDbv6BindingEntry=_FsIpDbv6BindingEntry_Object((1,3,6,1,4,1,29601,2,2,8,1,1))
fsIpDbv6BindingEntry.setIndexNames((0,_D,_Y),(0,_D,_Z))
if mibBuilder.loadTexts:fsIpDbv6BindingEntry.setStatus(_A)
class _FsIpDbv6HostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbv6HostVlanId_Type.__name__=_E
_FsIpDbv6HostVlanId_Object=MibTableColumn
fsIpDbv6HostVlanId=_FsIpDbv6HostVlanId_Object((1,3,6,1,4,1,29601,2,2,8,1,1,1),_FsIpDbv6HostVlanId_Type())
fsIpDbv6HostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbv6HostVlanId.setStatus(_A)
_FsIpDbv6HostMac_Type=MacAddress
_FsIpDbv6HostMac_Object=MibTableColumn
fsIpDbv6HostMac=_FsIpDbv6HostMac_Object((1,3,6,1,4,1,29601,2,2,8,1,1,2),_FsIpDbv6HostMac_Type())
fsIpDbv6HostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbv6HostMac.setStatus(_A)
class _FsIpDbv6HostBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('dhcp',2)))
_FsIpDbv6HostBindingType_Type.__name__=_E
_FsIpDbv6HostBindingType_Object=MibTableColumn
fsIpDbv6HostBindingType=_FsIpDbv6HostBindingType_Object((1,3,6,1,4,1,29601,2,2,8,1,1,3),_FsIpDbv6HostBindingType_Type())
fsIpDbv6HostBindingType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6HostBindingType.setStatus(_A)
_FsIpDbv6HostIp_Type=Ipv6Address
_FsIpDbv6HostIp_Object=MibTableColumn
fsIpDbv6HostIp=_FsIpDbv6HostIp_Object((1,3,6,1,4,1,29601,2,2,8,1,1,4),_FsIpDbv6HostIp_Type())
fsIpDbv6HostIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6HostIp.setStatus(_A)
_FsIpDbv6HostInIfIndex_Type=Integer32
_FsIpDbv6HostInIfIndex_Object=MibTableColumn
fsIpDbv6HostInIfIndex=_FsIpDbv6HostInIfIndex_Object((1,3,6,1,4,1,29601,2,2,8,1,1,5),_FsIpDbv6HostInIfIndex_Type())
fsIpDbv6HostInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6HostInIfIndex.setStatus(_A)
_FsIpDbv6HostRemLeaseTime_Type=Integer32
_FsIpDbv6HostRemLeaseTime_Object=MibTableColumn
fsIpDbv6HostRemLeaseTime=_FsIpDbv6HostRemLeaseTime_Object((1,3,6,1,4,1,29601,2,2,8,1,1,6),_FsIpDbv6HostRemLeaseTime_Type())
fsIpDbv6HostRemLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIpDbv6HostRemLeaseTime.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'Ipv6Address':Ipv6Address,'fsipdb':fsipdb,'fsIpDbScalars':fsIpDbScalars,'fsIpDbNoOfBindings':fsIpDbNoOfBindings,'fsIpDbNoOfStaticBindings':fsIpDbNoOfStaticBindings,'fsIpDbNoOfDHCPBindings':fsIpDbNoOfDHCPBindings,'fsIpDbNoOfPPPBindings':fsIpDbNoOfPPPBindings,'fsIpDbTraceLevel':fsIpDbTraceLevel,'fsIpDbv6DynamicDbSaveStatus':fsIpDbv6DynamicDbSaveStatus,'fsIpDbClearBindingStatus':fsIpDbClearBindingStatus,'fsIpDbv6ClearBindingStatus':fsIpDbv6ClearBindingStatus,'fsIpDbStatic':fsIpDbStatic,'fsIpDbStaticBindingTable':fsIpDbStaticBindingTable,'fsIpDbStaticBindingEntry':fsIpDbStaticBindingEntry,_L:fsIpDbStaticHostVlanId,_M:fsIpDbStaticHostMac,'fsIpDbStaticHostIp':fsIpDbStaticHostIp,'fsIpDbStaticInIfIndex':fsIpDbStaticInIfIndex,'fsIpDbStaticGateway':fsIpDbStaticGateway,'fsIpDbStaticBindingStatus':fsIpDbStaticBindingStatus,'fsIpDbBindings':fsIpDbBindings,'fsIpDbBindingTable':fsIpDbBindingTable,'fsIpDbBindingEntry':fsIpDbBindingEntry,_I:fsIpDbHostVlanId,_J:fsIpDbHostMac,'fsIpDbHostBindingType':fsIpDbHostBindingType,'fsIpDbHostIp':fsIpDbHostIp,'fsIpDbHostInIfIndex':fsIpDbHostInIfIndex,'fsIpDbHostRemLeaseTime':fsIpDbHostRemLeaseTime,'fsIpDbHostBindingID':fsIpDbHostBindingID,'fsIpDbGatewayIpTable':fsIpDbGatewayIpTable,'fsIpDbGatewayIpEntry':fsIpDbGatewayIpEntry,_O:fsIpDbGatewayNetwork,_P:fsIpDbGatewayNetMask,_Q:fsIpDbGatewayIp,'fsIpDbGatewayIpMode':fsIpDbGatewayIpMode,'fsIpDbInterface':fsIpDbInterface,'fsIpDbInterfaceTable':fsIpDbInterfaceTable,'fsIpDbInterfaceEntry':fsIpDbInterfaceEntry,_R:fsIpDbIntfVlanId,'fsIpDbIntfNoOfVlanBindings':fsIpDbIntfNoOfVlanBindings,'fsIpDbIntfNoOfVlanStaticBindings':fsIpDbIntfNoOfVlanStaticBindings,'fsIpDbIntfNoOfVlanDHCPBindings':fsIpDbIntfNoOfVlanDHCPBindings,'fsIpDbIntfNoOfVlanPPPBindings':fsIpDbIntfNoOfVlanPPPBindings,'fsIpDbIntfNoOfVlanDHCPv6Bindings':fsIpDbIntfNoOfVlanDHCPv6Bindings,'fsIpDbIntfNoOfVlanStaticv6Bindings':fsIpDbIntfNoOfVlanStaticv6Bindings,'fsIpDbSrcGuard':fsIpDbSrcGuard,'fsIpDbSrcGuardConfigTable':fsIpDbSrcGuardConfigTable,'fsIpDbSrcGuardConfigEntry':fsIpDbSrcGuardConfigEntry,_S:fsIpDbSrcGuardIndex,'fsIpDbSrcGuardStatus':fsIpDbSrcGuardStatus,'fsIpDbv6SrcGuardStatus':fsIpDbv6SrcGuardStatus,'fsIpArpInspect':fsIpArpInspect,'fsIpArpInspectionStatus':fsIpArpInspectionStatus,'fsIpArpInsValidateOption':fsIpArpInsValidateOption,'fsIpArpInsArpPktsForwarded':fsIpArpInsArpPktsForwarded,'fsIpArpInsArpPktsDropped':fsIpArpInsArpPktsDropped,'fsIpArpInsIPValidFailures':fsIpArpInsIPValidFailures,'fsIpArpInsDestMACFailures':fsIpArpInsDestMACFailures,'fsIpArpInsSrcMACFailures':fsIpArpInsSrcMACFailures,'fsIpArpInsGlobalStatsClear':fsIpArpInsGlobalStatsClear,'fsIpArpInsVlanTable':fsIpArpInsVlanTable,'fsIpArpInsVlanEntry':fsIpArpInsVlanEntry,_V:fsIpArpInsVlanId,'fsIpArpInsVlanStatus':fsIpArpInsVlanStatus,'fsIpArpInsVlanArpPktsForwarded':fsIpArpInsVlanArpPktsForwarded,'fsIpArpInsVlanArpPktsDropped':fsIpArpInsVlanArpPktsDropped,'fsIpArpInsVlanIPValidFailures':fsIpArpInsVlanIPValidFailures,'fsIpArpInsVlanDestMACFailures':fsIpArpInsVlanDestMACFailures,'fsIpArpInsVlanSrcMACFailures':fsIpArpInsVlanSrcMACFailures,'fsIpArpInsVlanClearStats':fsIpArpInsVlanClearStats,'fsIpArpInsVlanRowStatus':fsIpArpInsVlanRowStatus,'fsIpDbv6Static':fsIpDbv6Static,'fsIpDbv6StaticBindingTable':fsIpDbv6StaticBindingTable,'fsIpDbv6StaticBindingEntry':fsIpDbv6StaticBindingEntry,_W:fsIpDbv6StaticHostVlanId,_X:fsIpDbv6StaticHostMac,'fsIpDbv6StaticHostIp':fsIpDbv6StaticHostIp,'fsIpDbv6StaticInIfIndex':fsIpDbv6StaticInIfIndex,'fsIpDbv6StaticBindingStatus':fsIpDbv6StaticBindingStatus,'fsIpDbv6Bindings':fsIpDbv6Bindings,'fsIpDbv6BindingTable':fsIpDbv6BindingTable,'fsIpDbv6BindingEntry':fsIpDbv6BindingEntry,_Y:fsIpDbv6HostVlanId,_Z:fsIpDbv6HostMac,'fsIpDbv6HostBindingType':fsIpDbv6HostBindingType,'fsIpDbv6HostIp':fsIpDbv6HostIp,'fsIpDbv6HostInIfIndex':fsIpDbv6HostInIfIndex,'fsIpDbv6HostRemLeaseTime':fsIpDbv6HostRemLeaseTime})