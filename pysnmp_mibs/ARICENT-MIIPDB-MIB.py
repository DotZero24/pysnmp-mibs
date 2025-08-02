_f='fsMIIpDbv6HostMac'
_e='fsMIIpDbv6HostVlanId'
_d='fsMIIpDbv6HostContextId'
_c='fsMIIpDbv6StaticHostMac'
_b='fsMIIpDbv6StaticHostVlanId'
_a='fsMIIpDbv6ContextId'
_Z='fsMIIpArpInsVlanId'
_Y='fsMIIpArpInsVlanContextId'
_X='disabled'
_W='enabled'
_V='fsMIIpDbSrcGuardIndex'
_U='fsMIIpDbIntfVlanId'
_T='fsMIIpDbIntfContextId'
_S='fsMIIpDbGatewayIp'
_R='fsMIIpDbGatewayNetMask'
_Q='fsMIIpDbGatewayNetwork'
_P='static'
_O='fsMIIpDbStaticHostMac'
_N='fsMIIpDbStaticHostVlanId'
_M='fsMIIpDbContextId'
_L='enable'
_K='fsMIIpDbHostMac'
_J='fsMIIpDbHostVlanId'
_I='fsMIIpDbHostContextId'
_H='disable'
_G='TruthValue'
_F='not-accessible'
_E='Integer32'
_D='read-write'
_C='ARICENT-MIIPDB-MIB'
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
fsMIIpdb=ModuleIdentity((1,3,6,1,4,1,29601,2,48))
if mibBuilder.loadTexts:fsMIIpdb.setRevisions(('2012-09-05 00:00',))
class Ipv6Address(TextualConvention,OctetString):status=_A;displayHint='2x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_FsMIIpDbScalars_ObjectIdentity=ObjectIdentity
fsMIIpDbScalars=_FsMIIpDbScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,48,1))
_FsMIIpDbNoOfBindings_Type=Counter32
_FsMIIpDbNoOfBindings_Object=MibScalar
fsMIIpDbNoOfBindings=_FsMIIpDbNoOfBindings_Object((1,3,6,1,4,1,29601,2,48,1,1),_FsMIIpDbNoOfBindings_Type())
fsMIIpDbNoOfBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbNoOfBindings.setStatus(_A)
_FsMIIpDbNoOfStaticBindings_Type=Counter32
_FsMIIpDbNoOfStaticBindings_Object=MibScalar
fsMIIpDbNoOfStaticBindings=_FsMIIpDbNoOfStaticBindings_Object((1,3,6,1,4,1,29601,2,48,1,2),_FsMIIpDbNoOfStaticBindings_Type())
fsMIIpDbNoOfStaticBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbNoOfStaticBindings.setStatus(_A)
_FsMIIpDbNoOfDHCPBindings_Type=Counter32
_FsMIIpDbNoOfDHCPBindings_Object=MibScalar
fsMIIpDbNoOfDHCPBindings=_FsMIIpDbNoOfDHCPBindings_Object((1,3,6,1,4,1,29601,2,48,1,3),_FsMIIpDbNoOfDHCPBindings_Type())
fsMIIpDbNoOfDHCPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbNoOfDHCPBindings.setStatus(_A)
_FsMIIpDbNoOfPPPBindings_Type=Counter32
_FsMIIpDbNoOfPPPBindings_Object=MibScalar
fsMIIpDbNoOfPPPBindings=_FsMIIpDbNoOfPPPBindings_Object((1,3,6,1,4,1,29601,2,48,1,4),_FsMIIpDbNoOfPPPBindings_Type())
fsMIIpDbNoOfPPPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbNoOfPPPBindings.setStatus(_A)
_FsMIIpDbTraceLevel_Type=Integer32
_FsMIIpDbTraceLevel_Object=MibScalar
fsMIIpDbTraceLevel=_FsMIIpDbTraceLevel_Object((1,3,6,1,4,1,29601,2,48,1,5),_FsMIIpDbTraceLevel_Type())
fsMIIpDbTraceLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbTraceLevel.setStatus(_A)
class _FsMIIpDbv6DynamicDbSaveStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_H,2)))
_FsMIIpDbv6DynamicDbSaveStatus_Type.__name__=_E
_FsMIIpDbv6DynamicDbSaveStatus_Object=MibScalar
fsMIIpDbv6DynamicDbSaveStatus=_FsMIIpDbv6DynamicDbSaveStatus_Object((1,3,6,1,4,1,29601,2,48,1,6),_FsMIIpDbv6DynamicDbSaveStatus_Type())
fsMIIpDbv6DynamicDbSaveStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6DynamicDbSaveStatus.setStatus(_A)
class _FsMIIpDbClearBindingStatus_Type(TruthValue):defaultValue=2
_FsMIIpDbClearBindingStatus_Type.__name__=_G
_FsMIIpDbClearBindingStatus_Object=MibScalar
fsMIIpDbClearBindingStatus=_FsMIIpDbClearBindingStatus_Object((1,3,6,1,4,1,29601,2,48,1,7),_FsMIIpDbClearBindingStatus_Type())
fsMIIpDbClearBindingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbClearBindingStatus.setStatus(_A)
class _FsMIIpDbv6ClearBindingStatus_Type(TruthValue):defaultValue=2
_FsMIIpDbv6ClearBindingStatus_Type.__name__=_G
_FsMIIpDbv6ClearBindingStatus_Object=MibScalar
fsMIIpDbv6ClearBindingStatus=_FsMIIpDbv6ClearBindingStatus_Object((1,3,6,1,4,1,29601,2,48,1,8),_FsMIIpDbv6ClearBindingStatus_Type())
fsMIIpDbv6ClearBindingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6ClearBindingStatus.setStatus(_A)
_FsMIIpDbStatic_ObjectIdentity=ObjectIdentity
fsMIIpDbStatic=_FsMIIpDbStatic_ObjectIdentity((1,3,6,1,4,1,29601,2,48,2))
_FsMIIpDbStaticBindingTable_Object=MibTable
fsMIIpDbStaticBindingTable=_FsMIIpDbStaticBindingTable_Object((1,3,6,1,4,1,29601,2,48,2,1))
if mibBuilder.loadTexts:fsMIIpDbStaticBindingTable.setStatus(_A)
_FsMIIpDbStaticBindingEntry_Object=MibTableRow
fsMIIpDbStaticBindingEntry=_FsMIIpDbStaticBindingEntry_Object((1,3,6,1,4,1,29601,2,48,2,1,1))
fsMIIpDbStaticBindingEntry.setIndexNames((0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:fsMIIpDbStaticBindingEntry.setStatus(_A)
class _FsMIIpDbContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbContextId_Type.__name__=_E
_FsMIIpDbContextId_Object=MibTableColumn
fsMIIpDbContextId=_FsMIIpDbContextId_Object((1,3,6,1,4,1,29601,2,48,2,1,1,1),_FsMIIpDbContextId_Type())
fsMIIpDbContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbContextId.setStatus(_A)
class _FsMIIpDbStaticHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbStaticHostVlanId_Type.__name__=_E
_FsMIIpDbStaticHostVlanId_Object=MibTableColumn
fsMIIpDbStaticHostVlanId=_FsMIIpDbStaticHostVlanId_Object((1,3,6,1,4,1,29601,2,48,2,1,1,2),_FsMIIpDbStaticHostVlanId_Type())
fsMIIpDbStaticHostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbStaticHostVlanId.setStatus(_A)
_FsMIIpDbStaticHostMac_Type=MacAddress
_FsMIIpDbStaticHostMac_Object=MibTableColumn
fsMIIpDbStaticHostMac=_FsMIIpDbStaticHostMac_Object((1,3,6,1,4,1,29601,2,48,2,1,1,3),_FsMIIpDbStaticHostMac_Type())
fsMIIpDbStaticHostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbStaticHostMac.setStatus(_A)
_FsMIIpDbStaticHostIp_Type=IpAddress
_FsMIIpDbStaticHostIp_Object=MibTableColumn
fsMIIpDbStaticHostIp=_FsMIIpDbStaticHostIp_Object((1,3,6,1,4,1,29601,2,48,2,1,1,4),_FsMIIpDbStaticHostIp_Type())
fsMIIpDbStaticHostIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbStaticHostIp.setStatus(_A)
_FsMIIpDbStaticInIfIndex_Type=Integer32
_FsMIIpDbStaticInIfIndex_Object=MibTableColumn
fsMIIpDbStaticInIfIndex=_FsMIIpDbStaticInIfIndex_Object((1,3,6,1,4,1,29601,2,48,2,1,1,5),_FsMIIpDbStaticInIfIndex_Type())
fsMIIpDbStaticInIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbStaticInIfIndex.setStatus(_A)
_FsMIIpDbStaticGateway_Type=IpAddress
_FsMIIpDbStaticGateway_Object=MibTableColumn
fsMIIpDbStaticGateway=_FsMIIpDbStaticGateway_Object((1,3,6,1,4,1,29601,2,48,2,1,1,6),_FsMIIpDbStaticGateway_Type())
fsMIIpDbStaticGateway.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbStaticGateway.setStatus(_A)
_FsMIIpDbStaticBindingStatus_Type=RowStatus
_FsMIIpDbStaticBindingStatus_Object=MibTableColumn
fsMIIpDbStaticBindingStatus=_FsMIIpDbStaticBindingStatus_Object((1,3,6,1,4,1,29601,2,48,2,1,1,7),_FsMIIpDbStaticBindingStatus_Type())
fsMIIpDbStaticBindingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbStaticBindingStatus.setStatus(_A)
_FsMIIpDbBindings_ObjectIdentity=ObjectIdentity
fsMIIpDbBindings=_FsMIIpDbBindings_ObjectIdentity((1,3,6,1,4,1,29601,2,48,3))
_FsMIIpDbBindingTable_Object=MibTable
fsMIIpDbBindingTable=_FsMIIpDbBindingTable_Object((1,3,6,1,4,1,29601,2,48,3,1))
if mibBuilder.loadTexts:fsMIIpDbBindingTable.setStatus(_A)
_FsMIIpDbBindingEntry_Object=MibTableRow
fsMIIpDbBindingEntry=_FsMIIpDbBindingEntry_Object((1,3,6,1,4,1,29601,2,48,3,1,1))
fsMIIpDbBindingEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:fsMIIpDbBindingEntry.setStatus(_A)
class _FsMIIpDbHostContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbHostContextId_Type.__name__=_E
_FsMIIpDbHostContextId_Object=MibTableColumn
fsMIIpDbHostContextId=_FsMIIpDbHostContextId_Object((1,3,6,1,4,1,29601,2,48,3,1,1,1),_FsMIIpDbHostContextId_Type())
fsMIIpDbHostContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbHostContextId.setStatus(_A)
class _FsMIIpDbHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbHostVlanId_Type.__name__=_E
_FsMIIpDbHostVlanId_Object=MibTableColumn
fsMIIpDbHostVlanId=_FsMIIpDbHostVlanId_Object((1,3,6,1,4,1,29601,2,48,3,1,1,2),_FsMIIpDbHostVlanId_Type())
fsMIIpDbHostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbHostVlanId.setStatus(_A)
_FsMIIpDbHostMac_Type=MacAddress
_FsMIIpDbHostMac_Object=MibTableColumn
fsMIIpDbHostMac=_FsMIIpDbHostMac_Object((1,3,6,1,4,1,29601,2,48,3,1,1,3),_FsMIIpDbHostMac_Type())
fsMIIpDbHostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbHostMac.setStatus(_A)
class _FsMIIpDbHostBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('dhcp',2),('ppp',3)))
_FsMIIpDbHostBindingType_Type.__name__=_E
_FsMIIpDbHostBindingType_Object=MibTableColumn
fsMIIpDbHostBindingType=_FsMIIpDbHostBindingType_Object((1,3,6,1,4,1,29601,2,48,3,1,1,4),_FsMIIpDbHostBindingType_Type())
fsMIIpDbHostBindingType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbHostBindingType.setStatus(_A)
_FsMIIpDbHostIp_Type=IpAddress
_FsMIIpDbHostIp_Object=MibTableColumn
fsMIIpDbHostIp=_FsMIIpDbHostIp_Object((1,3,6,1,4,1,29601,2,48,3,1,1,5),_FsMIIpDbHostIp_Type())
fsMIIpDbHostIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbHostIp.setStatus(_A)
_FsMIIpDbHostInIfIndex_Type=Integer32
_FsMIIpDbHostInIfIndex_Object=MibTableColumn
fsMIIpDbHostInIfIndex=_FsMIIpDbHostInIfIndex_Object((1,3,6,1,4,1,29601,2,48,3,1,1,6),_FsMIIpDbHostInIfIndex_Type())
fsMIIpDbHostInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbHostInIfIndex.setStatus(_A)
_FsMIIpDbHostRemLeaseTime_Type=Integer32
_FsMIIpDbHostRemLeaseTime_Object=MibTableColumn
fsMIIpDbHostRemLeaseTime=_FsMIIpDbHostRemLeaseTime_Object((1,3,6,1,4,1,29601,2,48,3,1,1,7),_FsMIIpDbHostRemLeaseTime_Type())
fsMIIpDbHostRemLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbHostRemLeaseTime.setStatus(_A)
_FsMIIpDbHostBindingID_Type=Unsigned32
_FsMIIpDbHostBindingID_Object=MibTableColumn
fsMIIpDbHostBindingID=_FsMIIpDbHostBindingID_Object((1,3,6,1,4,1,29601,2,48,3,1,1,8),_FsMIIpDbHostBindingID_Type())
fsMIIpDbHostBindingID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbHostBindingID.setStatus(_A)
_FsMIIpDbGatewayIpTable_Object=MibTable
fsMIIpDbGatewayIpTable=_FsMIIpDbGatewayIpTable_Object((1,3,6,1,4,1,29601,2,48,3,2))
if mibBuilder.loadTexts:fsMIIpDbGatewayIpTable.setStatus(_A)
_FsMIIpDbGatewayIpEntry_Object=MibTableRow
fsMIIpDbGatewayIpEntry=_FsMIIpDbGatewayIpEntry_Object((1,3,6,1,4,1,29601,2,48,3,2,1))
fsMIIpDbGatewayIpEntry.setIndexNames((0,_C,_I),(0,_C,_K),(0,_C,_J),(0,_C,_Q),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:fsMIIpDbGatewayIpEntry.setStatus(_A)
_FsMIIpDbGatewayNetwork_Type=IpAddress
_FsMIIpDbGatewayNetwork_Object=MibTableColumn
fsMIIpDbGatewayNetwork=_FsMIIpDbGatewayNetwork_Object((1,3,6,1,4,1,29601,2,48,3,2,1,1),_FsMIIpDbGatewayNetwork_Type())
fsMIIpDbGatewayNetwork.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbGatewayNetwork.setStatus(_A)
_FsMIIpDbGatewayNetMask_Type=IpAddress
_FsMIIpDbGatewayNetMask_Object=MibTableColumn
fsMIIpDbGatewayNetMask=_FsMIIpDbGatewayNetMask_Object((1,3,6,1,4,1,29601,2,48,3,2,1,2),_FsMIIpDbGatewayNetMask_Type())
fsMIIpDbGatewayNetMask.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbGatewayNetMask.setStatus(_A)
_FsMIIpDbGatewayIp_Type=IpAddress
_FsMIIpDbGatewayIp_Object=MibTableColumn
fsMIIpDbGatewayIp=_FsMIIpDbGatewayIp_Object((1,3,6,1,4,1,29601,2,48,3,2,1,3),_FsMIIpDbGatewayIp_Type())
fsMIIpDbGatewayIp.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbGatewayIp.setStatus(_A)
class _FsMIIpDbGatewayIpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('active',0))
_FsMIIpDbGatewayIpMode_Type.__name__=_E
_FsMIIpDbGatewayIpMode_Object=MibTableColumn
fsMIIpDbGatewayIpMode=_FsMIIpDbGatewayIpMode_Object((1,3,6,1,4,1,29601,2,48,3,2,1,4),_FsMIIpDbGatewayIpMode_Type())
fsMIIpDbGatewayIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbGatewayIpMode.setStatus(_A)
_FsMIIpDbInterface_ObjectIdentity=ObjectIdentity
fsMIIpDbInterface=_FsMIIpDbInterface_ObjectIdentity((1,3,6,1,4,1,29601,2,48,4))
_FsMIIpDbInterfaceTable_Object=MibTable
fsMIIpDbInterfaceTable=_FsMIIpDbInterfaceTable_Object((1,3,6,1,4,1,29601,2,48,4,1))
if mibBuilder.loadTexts:fsMIIpDbInterfaceTable.setStatus(_A)
_FsMIIpDbInterfaceEntry_Object=MibTableRow
fsMIIpDbInterfaceEntry=_FsMIIpDbInterfaceEntry_Object((1,3,6,1,4,1,29601,2,48,4,1,1))
fsMIIpDbInterfaceEntry.setIndexNames((0,_C,_T),(0,_C,_U))
if mibBuilder.loadTexts:fsMIIpDbInterfaceEntry.setStatus(_A)
class _FsMIIpDbIntfContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbIntfContextId_Type.__name__=_E
_FsMIIpDbIntfContextId_Object=MibTableColumn
fsMIIpDbIntfContextId=_FsMIIpDbIntfContextId_Object((1,3,6,1,4,1,29601,2,48,4,1,1,1),_FsMIIpDbIntfContextId_Type())
fsMIIpDbIntfContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbIntfContextId.setStatus(_A)
class _FsMIIpDbIntfVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbIntfVlanId_Type.__name__=_E
_FsMIIpDbIntfVlanId_Object=MibTableColumn
fsMIIpDbIntfVlanId=_FsMIIpDbIntfVlanId_Object((1,3,6,1,4,1,29601,2,48,4,1,1,2),_FsMIIpDbIntfVlanId_Type())
fsMIIpDbIntfVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbIntfVlanId.setStatus(_A)
_FsMIIpDbIntfNoOfVlanBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanBindings=_FsMIIpDbIntfNoOfVlanBindings_Object((1,3,6,1,4,1,29601,2,48,4,1,1,3),_FsMIIpDbIntfNoOfVlanBindings_Type())
fsMIIpDbIntfNoOfVlanBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanBindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanStaticBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanStaticBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanStaticBindings=_FsMIIpDbIntfNoOfVlanStaticBindings_Object((1,3,6,1,4,1,29601,2,48,4,1,1,4),_FsMIIpDbIntfNoOfVlanStaticBindings_Type())
fsMIIpDbIntfNoOfVlanStaticBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanStaticBindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanDHCPBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanDHCPBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanDHCPBindings=_FsMIIpDbIntfNoOfVlanDHCPBindings_Object((1,3,6,1,4,1,29601,2,48,4,1,1,5),_FsMIIpDbIntfNoOfVlanDHCPBindings_Type())
fsMIIpDbIntfNoOfVlanDHCPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanDHCPBindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanPPPBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanPPPBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanPPPBindings=_FsMIIpDbIntfNoOfVlanPPPBindings_Object((1,3,6,1,4,1,29601,2,48,4,1,1,6),_FsMIIpDbIntfNoOfVlanPPPBindings_Type())
fsMIIpDbIntfNoOfVlanPPPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanPPPBindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanDHCPv6Bindings=_FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Object((1,3,6,1,4,1,29601,2,48,4,1,1,7),_FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Type())
fsMIIpDbIntfNoOfVlanDHCPv6Bindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanDHCPv6Bindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanStaticv6Bindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanStaticv6Bindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanStaticv6Bindings=_FsMIIpDbIntfNoOfVlanStaticv6Bindings_Object((1,3,6,1,4,1,29601,2,48,4,1,1,8),_FsMIIpDbIntfNoOfVlanStaticv6Bindings_Type())
fsMIIpDbIntfNoOfVlanStaticv6Bindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanStaticv6Bindings.setStatus(_A)
_FsMIIpDbSrcGuard_ObjectIdentity=ObjectIdentity
fsMIIpDbSrcGuard=_FsMIIpDbSrcGuard_ObjectIdentity((1,3,6,1,4,1,29601,2,48,5))
_FsMIIpDbSrcGuardConfigTable_Object=MibTable
fsMIIpDbSrcGuardConfigTable=_FsMIIpDbSrcGuardConfigTable_Object((1,3,6,1,4,1,29601,2,48,5,1))
if mibBuilder.loadTexts:fsMIIpDbSrcGuardConfigTable.setStatus(_A)
_FsMIIpDbSrcGuardConfigEntry_Object=MibTableRow
fsMIIpDbSrcGuardConfigEntry=_FsMIIpDbSrcGuardConfigEntry_Object((1,3,6,1,4,1,29601,2,48,5,1,1))
fsMIIpDbSrcGuardConfigEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:fsMIIpDbSrcGuardConfigEntry.setStatus(_A)
_FsMIIpDbSrcGuardIndex_Type=InterfaceIndex
_FsMIIpDbSrcGuardIndex_Object=MibTableColumn
fsMIIpDbSrcGuardIndex=_FsMIIpDbSrcGuardIndex_Object((1,3,6,1,4,1,29601,2,48,5,1,1,1),_FsMIIpDbSrcGuardIndex_Type())
fsMIIpDbSrcGuardIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbSrcGuardIndex.setStatus(_A)
class _FsMIIpDbSrcGuardStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('ip',2),('ipMac',3)))
_FsMIIpDbSrcGuardStatus_Type.__name__=_E
_FsMIIpDbSrcGuardStatus_Object=MibTableColumn
fsMIIpDbSrcGuardStatus=_FsMIIpDbSrcGuardStatus_Object((1,3,6,1,4,1,29601,2,48,5,1,1,2),_FsMIIpDbSrcGuardStatus_Type())
fsMIIpDbSrcGuardStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbSrcGuardStatus.setStatus(_A)
class _FsMIIpDbv6SrcGuardStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_H,2)))
_FsMIIpDbv6SrcGuardStatus_Type.__name__=_E
_FsMIIpDbv6SrcGuardStatus_Object=MibTableColumn
fsMIIpDbv6SrcGuardStatus=_FsMIIpDbv6SrcGuardStatus_Object((1,3,6,1,4,1,29601,2,48,5,1,1,3),_FsMIIpDbv6SrcGuardStatus_Type())
fsMIIpDbv6SrcGuardStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6SrcGuardStatus.setStatus(_A)
_FsMIIpArpInspect_ObjectIdentity=ObjectIdentity
fsMIIpArpInspect=_FsMIIpArpInspect_ObjectIdentity((1,3,6,1,4,1,29601,2,48,6))
class _FsMIIpArpInspectionStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsMIIpArpInspectionStatus_Type.__name__=_E
_FsMIIpArpInspectionStatus_Object=MibScalar
fsMIIpArpInspectionStatus=_FsMIIpArpInspectionStatus_Object((1,3,6,1,4,1,29601,2,48,6,1),_FsMIIpArpInspectionStatus_Type())
fsMIIpArpInspectionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpArpInspectionStatus.setStatus(_A)
class _FsMIIpArpInsValidateOption_Type(Bits):defaultHexValue='';namedValues=NamedValues(*(('srcmac',1),('dstmac',2),('ip',3)))
_FsMIIpArpInsValidateOption_Type.__name__='Bits'
_FsMIIpArpInsValidateOption_Object=MibScalar
fsMIIpArpInsValidateOption=_FsMIIpArpInsValidateOption_Object((1,3,6,1,4,1,29601,2,48,6,2),_FsMIIpArpInsValidateOption_Type())
fsMIIpArpInsValidateOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpArpInsValidateOption.setStatus(_A)
_FsMIIpArpInsArpPktsForwarded_Type=Counter32
_FsMIIpArpInsArpPktsForwarded_Object=MibScalar
fsMIIpArpInsArpPktsForwarded=_FsMIIpArpInsArpPktsForwarded_Object((1,3,6,1,4,1,29601,2,48,6,3),_FsMIIpArpInsArpPktsForwarded_Type())
fsMIIpArpInsArpPktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsArpPktsForwarded.setStatus(_A)
_FsMIIpArpInsArpPktsDropped_Type=Counter32
_FsMIIpArpInsArpPktsDropped_Object=MibScalar
fsMIIpArpInsArpPktsDropped=_FsMIIpArpInsArpPktsDropped_Object((1,3,6,1,4,1,29601,2,48,6,4),_FsMIIpArpInsArpPktsDropped_Type())
fsMIIpArpInsArpPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsArpPktsDropped.setStatus(_A)
_FsMIIpArpInsIPValidFailures_Type=Counter32
_FsMIIpArpInsIPValidFailures_Object=MibScalar
fsMIIpArpInsIPValidFailures=_FsMIIpArpInsIPValidFailures_Object((1,3,6,1,4,1,29601,2,48,6,5),_FsMIIpArpInsIPValidFailures_Type())
fsMIIpArpInsIPValidFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsIPValidFailures.setStatus(_A)
_FsMIIpArpInsDestMACFailures_Type=Counter32
_FsMIIpArpInsDestMACFailures_Object=MibScalar
fsMIIpArpInsDestMACFailures=_FsMIIpArpInsDestMACFailures_Object((1,3,6,1,4,1,29601,2,48,6,6),_FsMIIpArpInsDestMACFailures_Type())
fsMIIpArpInsDestMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsDestMACFailures.setStatus(_A)
_FsMIIpArpInsSrcMACFailures_Type=Counter32
_FsMIIpArpInsSrcMACFailures_Object=MibScalar
fsMIIpArpInsSrcMACFailures=_FsMIIpArpInsSrcMACFailures_Object((1,3,6,1,4,1,29601,2,48,6,7),_FsMIIpArpInsSrcMACFailures_Type())
fsMIIpArpInsSrcMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsSrcMACFailures.setStatus(_A)
class _FsMIIpArpInsGlobalStatsClear_Type(TruthValue):defaultValue=2
_FsMIIpArpInsGlobalStatsClear_Type.__name__=_G
_FsMIIpArpInsGlobalStatsClear_Object=MibScalar
fsMIIpArpInsGlobalStatsClear=_FsMIIpArpInsGlobalStatsClear_Object((1,3,6,1,4,1,29601,2,48,6,8),_FsMIIpArpInsGlobalStatsClear_Type())
fsMIIpArpInsGlobalStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpArpInsGlobalStatsClear.setStatus(_A)
_FsMIIpArpInsVlanTable_Object=MibTable
fsMIIpArpInsVlanTable=_FsMIIpArpInsVlanTable_Object((1,3,6,1,4,1,29601,2,48,6,9))
if mibBuilder.loadTexts:fsMIIpArpInsVlanTable.setStatus(_A)
_FsMIIpArpInsVlanEntry_Object=MibTableRow
fsMIIpArpInsVlanEntry=_FsMIIpArpInsVlanEntry_Object((1,3,6,1,4,1,29601,2,48,6,9,1))
fsMIIpArpInsVlanEntry.setIndexNames((0,_C,_Y),(0,_C,_Z))
if mibBuilder.loadTexts:fsMIIpArpInsVlanEntry.setStatus(_A)
class _FsMIIpArpInsVlanContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIIpArpInsVlanContextId_Type.__name__=_E
_FsMIIpArpInsVlanContextId_Object=MibTableColumn
fsMIIpArpInsVlanContextId=_FsMIIpArpInsVlanContextId_Object((1,3,6,1,4,1,29601,2,48,6,9,1,1),_FsMIIpArpInsVlanContextId_Type())
fsMIIpArpInsVlanContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpArpInsVlanContextId.setStatus(_A)
class _FsMIIpArpInsVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpArpInsVlanId_Type.__name__=_E
_FsMIIpArpInsVlanId_Object=MibTableColumn
fsMIIpArpInsVlanId=_FsMIIpArpInsVlanId_Object((1,3,6,1,4,1,29601,2,48,6,9,1,2),_FsMIIpArpInsVlanId_Type())
fsMIIpArpInsVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpArpInsVlanId.setStatus(_A)
class _FsMIIpArpInsVlanStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_FsMIIpArpInsVlanStatus_Type.__name__=_E
_FsMIIpArpInsVlanStatus_Object=MibTableColumn
fsMIIpArpInsVlanStatus=_FsMIIpArpInsVlanStatus_Object((1,3,6,1,4,1,29601,2,48,6,9,1,3),_FsMIIpArpInsVlanStatus_Type())
fsMIIpArpInsVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpArpInsVlanStatus.setStatus(_A)
_FsMIIpArpInsVlanArpPktsForwarded_Type=Integer32
_FsMIIpArpInsVlanArpPktsForwarded_Object=MibTableColumn
fsMIIpArpInsVlanArpPktsForwarded=_FsMIIpArpInsVlanArpPktsForwarded_Object((1,3,6,1,4,1,29601,2,48,6,9,1,4),_FsMIIpArpInsVlanArpPktsForwarded_Type())
fsMIIpArpInsVlanArpPktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsVlanArpPktsForwarded.setStatus(_A)
_FsMIIpArpInsVlanArpPktsDropped_Type=Integer32
_FsMIIpArpInsVlanArpPktsDropped_Object=MibTableColumn
fsMIIpArpInsVlanArpPktsDropped=_FsMIIpArpInsVlanArpPktsDropped_Object((1,3,6,1,4,1,29601,2,48,6,9,1,5),_FsMIIpArpInsVlanArpPktsDropped_Type())
fsMIIpArpInsVlanArpPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsVlanArpPktsDropped.setStatus(_A)
_FsMIIpArpInsVlanIPValidFailures_Type=Integer32
_FsMIIpArpInsVlanIPValidFailures_Object=MibTableColumn
fsMIIpArpInsVlanIPValidFailures=_FsMIIpArpInsVlanIPValidFailures_Object((1,3,6,1,4,1,29601,2,48,6,9,1,6),_FsMIIpArpInsVlanIPValidFailures_Type())
fsMIIpArpInsVlanIPValidFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsVlanIPValidFailures.setStatus(_A)
_FsMIIpArpInsVlanDestMACFailures_Type=Integer32
_FsMIIpArpInsVlanDestMACFailures_Object=MibTableColumn
fsMIIpArpInsVlanDestMACFailures=_FsMIIpArpInsVlanDestMACFailures_Object((1,3,6,1,4,1,29601,2,48,6,9,1,7),_FsMIIpArpInsVlanDestMACFailures_Type())
fsMIIpArpInsVlanDestMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsVlanDestMACFailures.setStatus(_A)
_FsMIIpArpInsVlanSrcMACFailures_Type=Integer32
_FsMIIpArpInsVlanSrcMACFailures_Object=MibTableColumn
fsMIIpArpInsVlanSrcMACFailures=_FsMIIpArpInsVlanSrcMACFailures_Object((1,3,6,1,4,1,29601,2,48,6,9,1,8),_FsMIIpArpInsVlanSrcMACFailures_Type())
fsMIIpArpInsVlanSrcMACFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIIpArpInsVlanSrcMACFailures.setStatus(_A)
class _FsMIIpArpInsVlanClearStats_Type(TruthValue):defaultValue=2
_FsMIIpArpInsVlanClearStats_Type.__name__=_G
_FsMIIpArpInsVlanClearStats_Object=MibTableColumn
fsMIIpArpInsVlanClearStats=_FsMIIpArpInsVlanClearStats_Object((1,3,6,1,4,1,29601,2,48,6,9,1,9),_FsMIIpArpInsVlanClearStats_Type())
fsMIIpArpInsVlanClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpArpInsVlanClearStats.setStatus(_A)
_FsMIIpArpInsVlanRowStatus_Type=RowStatus
_FsMIIpArpInsVlanRowStatus_Object=MibTableColumn
fsMIIpArpInsVlanRowStatus=_FsMIIpArpInsVlanRowStatus_Object((1,3,6,1,4,1,29601,2,48,6,9,1,10),_FsMIIpArpInsVlanRowStatus_Type())
fsMIIpArpInsVlanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpArpInsVlanRowStatus.setStatus(_A)
_FsMIIpDbv6Static_ObjectIdentity=ObjectIdentity
fsMIIpDbv6Static=_FsMIIpDbv6Static_ObjectIdentity((1,3,6,1,4,1,29601,2,48,7))
_FsMIIpDbv6StaticBindingTable_Object=MibTable
fsMIIpDbv6StaticBindingTable=_FsMIIpDbv6StaticBindingTable_Object((1,3,6,1,4,1,29601,2,48,7,1))
if mibBuilder.loadTexts:fsMIIpDbv6StaticBindingTable.setStatus(_A)
_FsMIIpDbv6StaticBindingEntry_Object=MibTableRow
fsMIIpDbv6StaticBindingEntry=_FsMIIpDbv6StaticBindingEntry_Object((1,3,6,1,4,1,29601,2,48,7,1,1))
fsMIIpDbv6StaticBindingEntry.setIndexNames((0,_C,_a),(0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:fsMIIpDbv6StaticBindingEntry.setStatus(_A)
class _FsMIIpDbv6ContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbv6ContextId_Type.__name__=_E
_FsMIIpDbv6ContextId_Object=MibTableColumn
fsMIIpDbv6ContextId=_FsMIIpDbv6ContextId_Object((1,3,6,1,4,1,29601,2,48,7,1,1,1),_FsMIIpDbv6ContextId_Type())
fsMIIpDbv6ContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbv6ContextId.setStatus(_A)
class _FsMIIpDbv6StaticHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbv6StaticHostVlanId_Type.__name__=_E
_FsMIIpDbv6StaticHostVlanId_Object=MibTableColumn
fsMIIpDbv6StaticHostVlanId=_FsMIIpDbv6StaticHostVlanId_Object((1,3,6,1,4,1,29601,2,48,7,1,1,2),_FsMIIpDbv6StaticHostVlanId_Type())
fsMIIpDbv6StaticHostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbv6StaticHostVlanId.setStatus(_A)
_FsMIIpDbv6StaticHostMac_Type=MacAddress
_FsMIIpDbv6StaticHostMac_Object=MibTableColumn
fsMIIpDbv6StaticHostMac=_FsMIIpDbv6StaticHostMac_Object((1,3,6,1,4,1,29601,2,48,7,1,1,3),_FsMIIpDbv6StaticHostMac_Type())
fsMIIpDbv6StaticHostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbv6StaticHostMac.setStatus(_A)
_FsMIIpDbv6StaticHostIp_Type=Ipv6Address
_FsMIIpDbv6StaticHostIp_Object=MibTableColumn
fsMIIpDbv6StaticHostIp=_FsMIIpDbv6StaticHostIp_Object((1,3,6,1,4,1,29601,2,48,7,1,1,4),_FsMIIpDbv6StaticHostIp_Type())
fsMIIpDbv6StaticHostIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6StaticHostIp.setStatus(_A)
_FsMIIpDbv6StaticInIfIndex_Type=Integer32
_FsMIIpDbv6StaticInIfIndex_Object=MibTableColumn
fsMIIpDbv6StaticInIfIndex=_FsMIIpDbv6StaticInIfIndex_Object((1,3,6,1,4,1,29601,2,48,7,1,1,5),_FsMIIpDbv6StaticInIfIndex_Type())
fsMIIpDbv6StaticInIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6StaticInIfIndex.setStatus(_A)
_FsMIIpDbv6StaticBindingStatus_Type=RowStatus
_FsMIIpDbv6StaticBindingStatus_Object=MibTableColumn
fsMIIpDbv6StaticBindingStatus=_FsMIIpDbv6StaticBindingStatus_Object((1,3,6,1,4,1,29601,2,48,7,1,1,6),_FsMIIpDbv6StaticBindingStatus_Type())
fsMIIpDbv6StaticBindingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6StaticBindingStatus.setStatus(_A)
_FsMIIpDbv6Bindings_ObjectIdentity=ObjectIdentity
fsMIIpDbv6Bindings=_FsMIIpDbv6Bindings_ObjectIdentity((1,3,6,1,4,1,29601,2,48,8))
_FsMIIpDbv6BindingTable_Object=MibTable
fsMIIpDbv6BindingTable=_FsMIIpDbv6BindingTable_Object((1,3,6,1,4,1,29601,2,48,8,1))
if mibBuilder.loadTexts:fsMIIpDbv6BindingTable.setStatus(_A)
_FsMIIpDbv6BindingEntry_Object=MibTableRow
fsMIIpDbv6BindingEntry=_FsMIIpDbv6BindingEntry_Object((1,3,6,1,4,1,29601,2,48,8,1,1))
fsMIIpDbv6BindingEntry.setIndexNames((0,_C,_d),(0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:fsMIIpDbv6BindingEntry.setStatus(_A)
class _FsMIIpDbv6HostContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbv6HostContextId_Type.__name__=_E
_FsMIIpDbv6HostContextId_Object=MibTableColumn
fsMIIpDbv6HostContextId=_FsMIIpDbv6HostContextId_Object((1,3,6,1,4,1,29601,2,48,8,1,1,1),_FsMIIpDbv6HostContextId_Type())
fsMIIpDbv6HostContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbv6HostContextId.setStatus(_A)
class _FsMIIpDbv6HostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbv6HostVlanId_Type.__name__=_E
_FsMIIpDbv6HostVlanId_Object=MibTableColumn
fsMIIpDbv6HostVlanId=_FsMIIpDbv6HostVlanId_Object((1,3,6,1,4,1,29601,2,48,8,1,1,2),_FsMIIpDbv6HostVlanId_Type())
fsMIIpDbv6HostVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbv6HostVlanId.setStatus(_A)
_FsMIIpDbv6HostMac_Type=MacAddress
_FsMIIpDbv6HostMac_Object=MibTableColumn
fsMIIpDbv6HostMac=_FsMIIpDbv6HostMac_Object((1,3,6,1,4,1,29601,2,48,8,1,1,3),_FsMIIpDbv6HostMac_Type())
fsMIIpDbv6HostMac.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbv6HostMac.setStatus(_A)
class _FsMIIpDbv6HostBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('dhcp',2)))
_FsMIIpDbv6HostBindingType_Type.__name__=_E
_FsMIIpDbv6HostBindingType_Object=MibTableColumn
fsMIIpDbv6HostBindingType=_FsMIIpDbv6HostBindingType_Object((1,3,6,1,4,1,29601,2,48,8,1,1,4),_FsMIIpDbv6HostBindingType_Type())
fsMIIpDbv6HostBindingType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6HostBindingType.setStatus(_A)
_FsMIIpDbv6HostIp_Type=Ipv6Address
_FsMIIpDbv6HostIp_Object=MibTableColumn
fsMIIpDbv6HostIp=_FsMIIpDbv6HostIp_Object((1,3,6,1,4,1,29601,2,48,8,1,1,5),_FsMIIpDbv6HostIp_Type())
fsMIIpDbv6HostIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6HostIp.setStatus(_A)
_FsMIIpDbv6HostInIfIndex_Type=Integer32
_FsMIIpDbv6HostInIfIndex_Object=MibTableColumn
fsMIIpDbv6HostInIfIndex=_FsMIIpDbv6HostInIfIndex_Object((1,3,6,1,4,1,29601,2,48,8,1,1,6),_FsMIIpDbv6HostInIfIndex_Type())
fsMIIpDbv6HostInIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6HostInIfIndex.setStatus(_A)
_FsMIIpDbv6HostRemLeaseTime_Type=Integer32
_FsMIIpDbv6HostRemLeaseTime_Object=MibTableColumn
fsMIIpDbv6HostRemLeaseTime=_FsMIIpDbv6HostRemLeaseTime_Object((1,3,6,1,4,1,29601,2,48,8,1,1,7),_FsMIIpDbv6HostRemLeaseTime_Type())
fsMIIpDbv6HostRemLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbv6HostRemLeaseTime.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'Ipv6Address':Ipv6Address,'fsMIIpdb':fsMIIpdb,'fsMIIpDbScalars':fsMIIpDbScalars,'fsMIIpDbNoOfBindings':fsMIIpDbNoOfBindings,'fsMIIpDbNoOfStaticBindings':fsMIIpDbNoOfStaticBindings,'fsMIIpDbNoOfDHCPBindings':fsMIIpDbNoOfDHCPBindings,'fsMIIpDbNoOfPPPBindings':fsMIIpDbNoOfPPPBindings,'fsMIIpDbTraceLevel':fsMIIpDbTraceLevel,'fsMIIpDbv6DynamicDbSaveStatus':fsMIIpDbv6DynamicDbSaveStatus,'fsMIIpDbClearBindingStatus':fsMIIpDbClearBindingStatus,'fsMIIpDbv6ClearBindingStatus':fsMIIpDbv6ClearBindingStatus,'fsMIIpDbStatic':fsMIIpDbStatic,'fsMIIpDbStaticBindingTable':fsMIIpDbStaticBindingTable,'fsMIIpDbStaticBindingEntry':fsMIIpDbStaticBindingEntry,_M:fsMIIpDbContextId,_N:fsMIIpDbStaticHostVlanId,_O:fsMIIpDbStaticHostMac,'fsMIIpDbStaticHostIp':fsMIIpDbStaticHostIp,'fsMIIpDbStaticInIfIndex':fsMIIpDbStaticInIfIndex,'fsMIIpDbStaticGateway':fsMIIpDbStaticGateway,'fsMIIpDbStaticBindingStatus':fsMIIpDbStaticBindingStatus,'fsMIIpDbBindings':fsMIIpDbBindings,'fsMIIpDbBindingTable':fsMIIpDbBindingTable,'fsMIIpDbBindingEntry':fsMIIpDbBindingEntry,_I:fsMIIpDbHostContextId,_J:fsMIIpDbHostVlanId,_K:fsMIIpDbHostMac,'fsMIIpDbHostBindingType':fsMIIpDbHostBindingType,'fsMIIpDbHostIp':fsMIIpDbHostIp,'fsMIIpDbHostInIfIndex':fsMIIpDbHostInIfIndex,'fsMIIpDbHostRemLeaseTime':fsMIIpDbHostRemLeaseTime,'fsMIIpDbHostBindingID':fsMIIpDbHostBindingID,'fsMIIpDbGatewayIpTable':fsMIIpDbGatewayIpTable,'fsMIIpDbGatewayIpEntry':fsMIIpDbGatewayIpEntry,_Q:fsMIIpDbGatewayNetwork,_R:fsMIIpDbGatewayNetMask,_S:fsMIIpDbGatewayIp,'fsMIIpDbGatewayIpMode':fsMIIpDbGatewayIpMode,'fsMIIpDbInterface':fsMIIpDbInterface,'fsMIIpDbInterfaceTable':fsMIIpDbInterfaceTable,'fsMIIpDbInterfaceEntry':fsMIIpDbInterfaceEntry,_T:fsMIIpDbIntfContextId,_U:fsMIIpDbIntfVlanId,'fsMIIpDbIntfNoOfVlanBindings':fsMIIpDbIntfNoOfVlanBindings,'fsMIIpDbIntfNoOfVlanStaticBindings':fsMIIpDbIntfNoOfVlanStaticBindings,'fsMIIpDbIntfNoOfVlanDHCPBindings':fsMIIpDbIntfNoOfVlanDHCPBindings,'fsMIIpDbIntfNoOfVlanPPPBindings':fsMIIpDbIntfNoOfVlanPPPBindings,'fsMIIpDbIntfNoOfVlanDHCPv6Bindings':fsMIIpDbIntfNoOfVlanDHCPv6Bindings,'fsMIIpDbIntfNoOfVlanStaticv6Bindings':fsMIIpDbIntfNoOfVlanStaticv6Bindings,'fsMIIpDbSrcGuard':fsMIIpDbSrcGuard,'fsMIIpDbSrcGuardConfigTable':fsMIIpDbSrcGuardConfigTable,'fsMIIpDbSrcGuardConfigEntry':fsMIIpDbSrcGuardConfigEntry,_V:fsMIIpDbSrcGuardIndex,'fsMIIpDbSrcGuardStatus':fsMIIpDbSrcGuardStatus,'fsMIIpDbv6SrcGuardStatus':fsMIIpDbv6SrcGuardStatus,'fsMIIpArpInspect':fsMIIpArpInspect,'fsMIIpArpInspectionStatus':fsMIIpArpInspectionStatus,'fsMIIpArpInsValidateOption':fsMIIpArpInsValidateOption,'fsMIIpArpInsArpPktsForwarded':fsMIIpArpInsArpPktsForwarded,'fsMIIpArpInsArpPktsDropped':fsMIIpArpInsArpPktsDropped,'fsMIIpArpInsIPValidFailures':fsMIIpArpInsIPValidFailures,'fsMIIpArpInsDestMACFailures':fsMIIpArpInsDestMACFailures,'fsMIIpArpInsSrcMACFailures':fsMIIpArpInsSrcMACFailures,'fsMIIpArpInsGlobalStatsClear':fsMIIpArpInsGlobalStatsClear,'fsMIIpArpInsVlanTable':fsMIIpArpInsVlanTable,'fsMIIpArpInsVlanEntry':fsMIIpArpInsVlanEntry,_Y:fsMIIpArpInsVlanContextId,_Z:fsMIIpArpInsVlanId,'fsMIIpArpInsVlanStatus':fsMIIpArpInsVlanStatus,'fsMIIpArpInsVlanArpPktsForwarded':fsMIIpArpInsVlanArpPktsForwarded,'fsMIIpArpInsVlanArpPktsDropped':fsMIIpArpInsVlanArpPktsDropped,'fsMIIpArpInsVlanIPValidFailures':fsMIIpArpInsVlanIPValidFailures,'fsMIIpArpInsVlanDestMACFailures':fsMIIpArpInsVlanDestMACFailures,'fsMIIpArpInsVlanSrcMACFailures':fsMIIpArpInsVlanSrcMACFailures,'fsMIIpArpInsVlanClearStats':fsMIIpArpInsVlanClearStats,'fsMIIpArpInsVlanRowStatus':fsMIIpArpInsVlanRowStatus,'fsMIIpDbv6Static':fsMIIpDbv6Static,'fsMIIpDbv6StaticBindingTable':fsMIIpDbv6StaticBindingTable,'fsMIIpDbv6StaticBindingEntry':fsMIIpDbv6StaticBindingEntry,_a:fsMIIpDbv6ContextId,_b:fsMIIpDbv6StaticHostVlanId,_c:fsMIIpDbv6StaticHostMac,'fsMIIpDbv6StaticHostIp':fsMIIpDbv6StaticHostIp,'fsMIIpDbv6StaticInIfIndex':fsMIIpDbv6StaticInIfIndex,'fsMIIpDbv6StaticBindingStatus':fsMIIpDbv6StaticBindingStatus,'fsMIIpDbv6Bindings':fsMIIpDbv6Bindings,'fsMIIpDbv6BindingTable':fsMIIpDbv6BindingTable,'fsMIIpDbv6BindingEntry':fsMIIpDbv6BindingEntry,_d:fsMIIpDbv6HostContextId,_e:fsMIIpDbv6HostVlanId,_f:fsMIIpDbv6HostMac,'fsMIIpDbv6HostBindingType':fsMIIpDbv6HostBindingType,'fsMIIpDbv6HostIp':fsMIIpDbv6HostIp,'fsMIIpDbv6HostInIfIndex':fsMIIpDbv6HostInIfIndex,'fsMIIpDbv6HostRemLeaseTime':fsMIIpDbv6HostRemLeaseTime})