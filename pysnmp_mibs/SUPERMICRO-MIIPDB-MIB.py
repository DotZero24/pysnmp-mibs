_R='fsMIIpDbSrcGuardIndex'
_Q='fsMIIpDbIntfVlanId'
_P='fsMIIpDbIntfContextId'
_O='fsMIIpDbGatewayIp'
_N='fsMIIpDbGatewayNetMask'
_M='fsMIIpDbGatewayNetwork'
_L='fsMIIpDbStaticHostMac'
_K='fsMIIpDbStaticHostVlanId'
_J='fsMIIpDbContextId'
_I='fsMIIpDbHostMac'
_H='fsMIIpDbHostVlanId'
_G='fsMIIpDbHostContextId'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='SUPERMICRO-MIIPDB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsMIIpdb=ModuleIdentity((1,3,6,1,4,1,10876,101,2,48))
if mibBuilder.loadTexts:fsMIIpdb.setRevisions(('2012-09-05 00:00',))
_FsMIIpDbScalars_ObjectIdentity=ObjectIdentity
fsMIIpDbScalars=_FsMIIpDbScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,2,48,1))
_FsMIIpDbNoOfBindings_Type=Counter32
_FsMIIpDbNoOfBindings_Object=MibScalar
fsMIIpDbNoOfBindings=_FsMIIpDbNoOfBindings_Object((1,3,6,1,4,1,10876,101,2,48,1,1),_FsMIIpDbNoOfBindings_Type())
fsMIIpDbNoOfBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbNoOfBindings.setStatus(_A)
_FsMIIpDbNoOfStaticBindings_Type=Counter32
_FsMIIpDbNoOfStaticBindings_Object=MibScalar
fsMIIpDbNoOfStaticBindings=_FsMIIpDbNoOfStaticBindings_Object((1,3,6,1,4,1,10876,101,2,48,1,2),_FsMIIpDbNoOfStaticBindings_Type())
fsMIIpDbNoOfStaticBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbNoOfStaticBindings.setStatus(_A)
_FsMIIpDbNoOfDHCPBindings_Type=Counter32
_FsMIIpDbNoOfDHCPBindings_Object=MibScalar
fsMIIpDbNoOfDHCPBindings=_FsMIIpDbNoOfDHCPBindings_Object((1,3,6,1,4,1,10876,101,2,48,1,3),_FsMIIpDbNoOfDHCPBindings_Type())
fsMIIpDbNoOfDHCPBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbNoOfDHCPBindings.setStatus(_A)
_FsMIIpDbNoOfPPPBindings_Type=Counter32
_FsMIIpDbNoOfPPPBindings_Object=MibScalar
fsMIIpDbNoOfPPPBindings=_FsMIIpDbNoOfPPPBindings_Object((1,3,6,1,4,1,10876,101,2,48,1,4),_FsMIIpDbNoOfPPPBindings_Type())
fsMIIpDbNoOfPPPBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbNoOfPPPBindings.setStatus(_A)
_FsMIIpDbTraceLevel_Type=Integer32
_FsMIIpDbTraceLevel_Object=MibScalar
fsMIIpDbTraceLevel=_FsMIIpDbTraceLevel_Object((1,3,6,1,4,1,10876,101,2,48,1,5),_FsMIIpDbTraceLevel_Type())
fsMIIpDbTraceLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbTraceLevel.setStatus(_A)
_FsMIIpDbStatic_ObjectIdentity=ObjectIdentity
fsMIIpDbStatic=_FsMIIpDbStatic_ObjectIdentity((1,3,6,1,4,1,10876,101,2,48,2))
_FsMIIpDbStaticBindingTable_Object=MibTable
fsMIIpDbStaticBindingTable=_FsMIIpDbStaticBindingTable_Object((1,3,6,1,4,1,10876,101,2,48,2,1))
if mibBuilder.loadTexts:fsMIIpDbStaticBindingTable.setStatus(_A)
_FsMIIpDbStaticBindingEntry_Object=MibTableRow
fsMIIpDbStaticBindingEntry=_FsMIIpDbStaticBindingEntry_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1))
fsMIIpDbStaticBindingEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:fsMIIpDbStaticBindingEntry.setStatus(_A)
class _FsMIIpDbContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbContextId_Type.__name__=_E
_FsMIIpDbContextId_Object=MibTableColumn
fsMIIpDbContextId=_FsMIIpDbContextId_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1,1),_FsMIIpDbContextId_Type())
fsMIIpDbContextId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbContextId.setStatus(_A)
class _FsMIIpDbStaticHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbStaticHostVlanId_Type.__name__=_E
_FsMIIpDbStaticHostVlanId_Object=MibTableColumn
fsMIIpDbStaticHostVlanId=_FsMIIpDbStaticHostVlanId_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1,2),_FsMIIpDbStaticHostVlanId_Type())
fsMIIpDbStaticHostVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbStaticHostVlanId.setStatus(_A)
_FsMIIpDbStaticHostMac_Type=MacAddress
_FsMIIpDbStaticHostMac_Object=MibTableColumn
fsMIIpDbStaticHostMac=_FsMIIpDbStaticHostMac_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1,3),_FsMIIpDbStaticHostMac_Type())
fsMIIpDbStaticHostMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbStaticHostMac.setStatus(_A)
_FsMIIpDbStaticHostIp_Type=IpAddress
_FsMIIpDbStaticHostIp_Object=MibTableColumn
fsMIIpDbStaticHostIp=_FsMIIpDbStaticHostIp_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1,4),_FsMIIpDbStaticHostIp_Type())
fsMIIpDbStaticHostIp.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbStaticHostIp.setStatus(_A)
_FsMIIpDbStaticInIfIndex_Type=Integer32
_FsMIIpDbStaticInIfIndex_Object=MibTableColumn
fsMIIpDbStaticInIfIndex=_FsMIIpDbStaticInIfIndex_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1,5),_FsMIIpDbStaticInIfIndex_Type())
fsMIIpDbStaticInIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbStaticInIfIndex.setStatus(_A)
_FsMIIpDbStaticGateway_Type=IpAddress
_FsMIIpDbStaticGateway_Object=MibTableColumn
fsMIIpDbStaticGateway=_FsMIIpDbStaticGateway_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1,6),_FsMIIpDbStaticGateway_Type())
fsMIIpDbStaticGateway.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbStaticGateway.setStatus(_A)
_FsMIIpDbStaticBindingStatus_Type=RowStatus
_FsMIIpDbStaticBindingStatus_Object=MibTableColumn
fsMIIpDbStaticBindingStatus=_FsMIIpDbStaticBindingStatus_Object((1,3,6,1,4,1,10876,101,2,48,2,1,1,7),_FsMIIpDbStaticBindingStatus_Type())
fsMIIpDbStaticBindingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbStaticBindingStatus.setStatus(_A)
_FsMIIpDbBindings_ObjectIdentity=ObjectIdentity
fsMIIpDbBindings=_FsMIIpDbBindings_ObjectIdentity((1,3,6,1,4,1,10876,101,2,48,3))
_FsMIIpDbBindingTable_Object=MibTable
fsMIIpDbBindingTable=_FsMIIpDbBindingTable_Object((1,3,6,1,4,1,10876,101,2,48,3,1))
if mibBuilder.loadTexts:fsMIIpDbBindingTable.setStatus(_A)
_FsMIIpDbBindingEntry_Object=MibTableRow
fsMIIpDbBindingEntry=_FsMIIpDbBindingEntry_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1))
fsMIIpDbBindingEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsMIIpDbBindingEntry.setStatus(_A)
class _FsMIIpDbHostContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbHostContextId_Type.__name__=_E
_FsMIIpDbHostContextId_Object=MibTableColumn
fsMIIpDbHostContextId=_FsMIIpDbHostContextId_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,1),_FsMIIpDbHostContextId_Type())
fsMIIpDbHostContextId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbHostContextId.setStatus(_A)
class _FsMIIpDbHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbHostVlanId_Type.__name__=_E
_FsMIIpDbHostVlanId_Object=MibTableColumn
fsMIIpDbHostVlanId=_FsMIIpDbHostVlanId_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,2),_FsMIIpDbHostVlanId_Type())
fsMIIpDbHostVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbHostVlanId.setStatus(_A)
_FsMIIpDbHostMac_Type=MacAddress
_FsMIIpDbHostMac_Object=MibTableColumn
fsMIIpDbHostMac=_FsMIIpDbHostMac_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,3),_FsMIIpDbHostMac_Type())
fsMIIpDbHostMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbHostMac.setStatus(_A)
class _FsMIIpDbHostBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dhcp',2),('ppp',3)))
_FsMIIpDbHostBindingType_Type.__name__=_E
_FsMIIpDbHostBindingType_Object=MibTableColumn
fsMIIpDbHostBindingType=_FsMIIpDbHostBindingType_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,4),_FsMIIpDbHostBindingType_Type())
fsMIIpDbHostBindingType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbHostBindingType.setStatus(_A)
_FsMIIpDbHostIp_Type=IpAddress
_FsMIIpDbHostIp_Object=MibTableColumn
fsMIIpDbHostIp=_FsMIIpDbHostIp_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,5),_FsMIIpDbHostIp_Type())
fsMIIpDbHostIp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbHostIp.setStatus(_A)
_FsMIIpDbHostInIfIndex_Type=Integer32
_FsMIIpDbHostInIfIndex_Object=MibTableColumn
fsMIIpDbHostInIfIndex=_FsMIIpDbHostInIfIndex_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,6),_FsMIIpDbHostInIfIndex_Type())
fsMIIpDbHostInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbHostInIfIndex.setStatus(_A)
_FsMIIpDbHostRemLeaseTime_Type=Integer32
_FsMIIpDbHostRemLeaseTime_Object=MibTableColumn
fsMIIpDbHostRemLeaseTime=_FsMIIpDbHostRemLeaseTime_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,7),_FsMIIpDbHostRemLeaseTime_Type())
fsMIIpDbHostRemLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbHostRemLeaseTime.setStatus(_A)
_FsMIIpDbHostBindingID_Type=Unsigned32
_FsMIIpDbHostBindingID_Object=MibTableColumn
fsMIIpDbHostBindingID=_FsMIIpDbHostBindingID_Object((1,3,6,1,4,1,10876,101,2,48,3,1,1,8),_FsMIIpDbHostBindingID_Type())
fsMIIpDbHostBindingID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbHostBindingID.setStatus(_A)
_FsMIIpDbGatewayIpTable_Object=MibTable
fsMIIpDbGatewayIpTable=_FsMIIpDbGatewayIpTable_Object((1,3,6,1,4,1,10876,101,2,48,3,2))
if mibBuilder.loadTexts:fsMIIpDbGatewayIpTable.setStatus(_A)
_FsMIIpDbGatewayIpEntry_Object=MibTableRow
fsMIIpDbGatewayIpEntry=_FsMIIpDbGatewayIpEntry_Object((1,3,6,1,4,1,10876,101,2,48,3,2,1))
fsMIIpDbGatewayIpEntry.setIndexNames((0,_B,_G),(0,_B,_I),(0,_B,_H),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:fsMIIpDbGatewayIpEntry.setStatus(_A)
_FsMIIpDbGatewayNetwork_Type=IpAddress
_FsMIIpDbGatewayNetwork_Object=MibTableColumn
fsMIIpDbGatewayNetwork=_FsMIIpDbGatewayNetwork_Object((1,3,6,1,4,1,10876,101,2,48,3,2,1,1),_FsMIIpDbGatewayNetwork_Type())
fsMIIpDbGatewayNetwork.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbGatewayNetwork.setStatus(_A)
_FsMIIpDbGatewayNetMask_Type=IpAddress
_FsMIIpDbGatewayNetMask_Object=MibTableColumn
fsMIIpDbGatewayNetMask=_FsMIIpDbGatewayNetMask_Object((1,3,6,1,4,1,10876,101,2,48,3,2,1,2),_FsMIIpDbGatewayNetMask_Type())
fsMIIpDbGatewayNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbGatewayNetMask.setStatus(_A)
_FsMIIpDbGatewayIp_Type=IpAddress
_FsMIIpDbGatewayIp_Object=MibTableColumn
fsMIIpDbGatewayIp=_FsMIIpDbGatewayIp_Object((1,3,6,1,4,1,10876,101,2,48,3,2,1,3),_FsMIIpDbGatewayIp_Type())
fsMIIpDbGatewayIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbGatewayIp.setStatus(_A)
class _FsMIIpDbGatewayIpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('active',0))
_FsMIIpDbGatewayIpMode_Type.__name__=_E
_FsMIIpDbGatewayIpMode_Object=MibTableColumn
fsMIIpDbGatewayIpMode=_FsMIIpDbGatewayIpMode_Object((1,3,6,1,4,1,10876,101,2,48,3,2,1,4),_FsMIIpDbGatewayIpMode_Type())
fsMIIpDbGatewayIpMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbGatewayIpMode.setStatus(_A)
_FsMIIpDbInterface_ObjectIdentity=ObjectIdentity
fsMIIpDbInterface=_FsMIIpDbInterface_ObjectIdentity((1,3,6,1,4,1,10876,101,2,48,4))
_FsMIIpDbInterfaceTable_Object=MibTable
fsMIIpDbInterfaceTable=_FsMIIpDbInterfaceTable_Object((1,3,6,1,4,1,10876,101,2,48,4,1))
if mibBuilder.loadTexts:fsMIIpDbInterfaceTable.setStatus(_A)
_FsMIIpDbInterfaceEntry_Object=MibTableRow
fsMIIpDbInterfaceEntry=_FsMIIpDbInterfaceEntry_Object((1,3,6,1,4,1,10876,101,2,48,4,1,1))
fsMIIpDbInterfaceEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:fsMIIpDbInterfaceEntry.setStatus(_A)
class _FsMIIpDbIntfContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIIpDbIntfContextId_Type.__name__=_E
_FsMIIpDbIntfContextId_Object=MibTableColumn
fsMIIpDbIntfContextId=_FsMIIpDbIntfContextId_Object((1,3,6,1,4,1,10876,101,2,48,4,1,1,1),_FsMIIpDbIntfContextId_Type())
fsMIIpDbIntfContextId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbIntfContextId.setStatus(_A)
class _FsMIIpDbIntfVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIIpDbIntfVlanId_Type.__name__=_E
_FsMIIpDbIntfVlanId_Object=MibTableColumn
fsMIIpDbIntfVlanId=_FsMIIpDbIntfVlanId_Object((1,3,6,1,4,1,10876,101,2,48,4,1,1,2),_FsMIIpDbIntfVlanId_Type())
fsMIIpDbIntfVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbIntfVlanId.setStatus(_A)
_FsMIIpDbIntfNoOfVlanBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanBindings=_FsMIIpDbIntfNoOfVlanBindings_Object((1,3,6,1,4,1,10876,101,2,48,4,1,1,3),_FsMIIpDbIntfNoOfVlanBindings_Type())
fsMIIpDbIntfNoOfVlanBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanBindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanStaticBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanStaticBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanStaticBindings=_FsMIIpDbIntfNoOfVlanStaticBindings_Object((1,3,6,1,4,1,10876,101,2,48,4,1,1,4),_FsMIIpDbIntfNoOfVlanStaticBindings_Type())
fsMIIpDbIntfNoOfVlanStaticBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanStaticBindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanDHCPBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanDHCPBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanDHCPBindings=_FsMIIpDbIntfNoOfVlanDHCPBindings_Object((1,3,6,1,4,1,10876,101,2,48,4,1,1,5),_FsMIIpDbIntfNoOfVlanDHCPBindings_Type())
fsMIIpDbIntfNoOfVlanDHCPBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanDHCPBindings.setStatus(_A)
_FsMIIpDbIntfNoOfVlanPPPBindings_Type=Counter32
_FsMIIpDbIntfNoOfVlanPPPBindings_Object=MibTableColumn
fsMIIpDbIntfNoOfVlanPPPBindings=_FsMIIpDbIntfNoOfVlanPPPBindings_Object((1,3,6,1,4,1,10876,101,2,48,4,1,1,6),_FsMIIpDbIntfNoOfVlanPPPBindings_Type())
fsMIIpDbIntfNoOfVlanPPPBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIIpDbIntfNoOfVlanPPPBindings.setStatus(_A)
_FsMIIpDbSrcGuard_ObjectIdentity=ObjectIdentity
fsMIIpDbSrcGuard=_FsMIIpDbSrcGuard_ObjectIdentity((1,3,6,1,4,1,10876,101,2,48,5))
_FsMIIpDbSrcGuardConfigTable_Object=MibTable
fsMIIpDbSrcGuardConfigTable=_FsMIIpDbSrcGuardConfigTable_Object((1,3,6,1,4,1,10876,101,2,48,5,1))
if mibBuilder.loadTexts:fsMIIpDbSrcGuardConfigTable.setStatus(_A)
_FsMIIpDbSrcGuardConfigEntry_Object=MibTableRow
fsMIIpDbSrcGuardConfigEntry=_FsMIIpDbSrcGuardConfigEntry_Object((1,3,6,1,4,1,10876,101,2,48,5,1,1))
fsMIIpDbSrcGuardConfigEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:fsMIIpDbSrcGuardConfigEntry.setStatus(_A)
_FsMIIpDbSrcGuardIndex_Type=InterfaceIndex
_FsMIIpDbSrcGuardIndex_Object=MibTableColumn
fsMIIpDbSrcGuardIndex=_FsMIIpDbSrcGuardIndex_Object((1,3,6,1,4,1,10876,101,2,48,5,1,1,1),_FsMIIpDbSrcGuardIndex_Type())
fsMIIpDbSrcGuardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIIpDbSrcGuardIndex.setStatus(_A)
class _FsMIIpDbSrcGuardStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('ip',2),('ipMac',3)))
_FsMIIpDbSrcGuardStatus_Type.__name__=_E
_FsMIIpDbSrcGuardStatus_Object=MibTableColumn
fsMIIpDbSrcGuardStatus=_FsMIIpDbSrcGuardStatus_Object((1,3,6,1,4,1,10876,101,2,48,5,1,1,2),_FsMIIpDbSrcGuardStatus_Type())
fsMIIpDbSrcGuardStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIIpDbSrcGuardStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsMIIpdb':fsMIIpdb,'fsMIIpDbScalars':fsMIIpDbScalars,'fsMIIpDbNoOfBindings':fsMIIpDbNoOfBindings,'fsMIIpDbNoOfStaticBindings':fsMIIpDbNoOfStaticBindings,'fsMIIpDbNoOfDHCPBindings':fsMIIpDbNoOfDHCPBindings,'fsMIIpDbNoOfPPPBindings':fsMIIpDbNoOfPPPBindings,'fsMIIpDbTraceLevel':fsMIIpDbTraceLevel,'fsMIIpDbStatic':fsMIIpDbStatic,'fsMIIpDbStaticBindingTable':fsMIIpDbStaticBindingTable,'fsMIIpDbStaticBindingEntry':fsMIIpDbStaticBindingEntry,_J:fsMIIpDbContextId,_K:fsMIIpDbStaticHostVlanId,_L:fsMIIpDbStaticHostMac,'fsMIIpDbStaticHostIp':fsMIIpDbStaticHostIp,'fsMIIpDbStaticInIfIndex':fsMIIpDbStaticInIfIndex,'fsMIIpDbStaticGateway':fsMIIpDbStaticGateway,'fsMIIpDbStaticBindingStatus':fsMIIpDbStaticBindingStatus,'fsMIIpDbBindings':fsMIIpDbBindings,'fsMIIpDbBindingTable':fsMIIpDbBindingTable,'fsMIIpDbBindingEntry':fsMIIpDbBindingEntry,_G:fsMIIpDbHostContextId,_H:fsMIIpDbHostVlanId,_I:fsMIIpDbHostMac,'fsMIIpDbHostBindingType':fsMIIpDbHostBindingType,'fsMIIpDbHostIp':fsMIIpDbHostIp,'fsMIIpDbHostInIfIndex':fsMIIpDbHostInIfIndex,'fsMIIpDbHostRemLeaseTime':fsMIIpDbHostRemLeaseTime,'fsMIIpDbHostBindingID':fsMIIpDbHostBindingID,'fsMIIpDbGatewayIpTable':fsMIIpDbGatewayIpTable,'fsMIIpDbGatewayIpEntry':fsMIIpDbGatewayIpEntry,_M:fsMIIpDbGatewayNetwork,_N:fsMIIpDbGatewayNetMask,_O:fsMIIpDbGatewayIp,'fsMIIpDbGatewayIpMode':fsMIIpDbGatewayIpMode,'fsMIIpDbInterface':fsMIIpDbInterface,'fsMIIpDbInterfaceTable':fsMIIpDbInterfaceTable,'fsMIIpDbInterfaceEntry':fsMIIpDbInterfaceEntry,_P:fsMIIpDbIntfContextId,_Q:fsMIIpDbIntfVlanId,'fsMIIpDbIntfNoOfVlanBindings':fsMIIpDbIntfNoOfVlanBindings,'fsMIIpDbIntfNoOfVlanStaticBindings':fsMIIpDbIntfNoOfVlanStaticBindings,'fsMIIpDbIntfNoOfVlanDHCPBindings':fsMIIpDbIntfNoOfVlanDHCPBindings,'fsMIIpDbIntfNoOfVlanPPPBindings':fsMIIpDbIntfNoOfVlanPPPBindings,'fsMIIpDbSrcGuard':fsMIIpDbSrcGuard,'fsMIIpDbSrcGuardConfigTable':fsMIIpDbSrcGuardConfigTable,'fsMIIpDbSrcGuardConfigEntry':fsMIIpDbSrcGuardConfigEntry,_R:fsMIIpDbSrcGuardIndex,'fsMIIpDbSrcGuardStatus':fsMIIpDbSrcGuardStatus})