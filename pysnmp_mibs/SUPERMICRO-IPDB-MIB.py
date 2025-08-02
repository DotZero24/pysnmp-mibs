_O='fsIpDbSrcGuardIndex'
_N='fsIpDbIntfVlanId'
_M='fsIpDbGatewayIp'
_L='fsIpDbGatewayNetMask'
_K='fsIpDbGatewayNetwork'
_J='fsIpDbStaticHostMac'
_I='fsIpDbStaticHostVlanId'
_H='fsIpDbHostMac'
_G='fsIpDbHostVlanId'
_F='read-write'
_E='Integer32'
_D='not-accessible'
_C='SUPERMICRO-IPDB-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fsipdb=ModuleIdentity((1,3,6,1,4,1,10876,101,2,2))
if mibBuilder.loadTexts:fsipdb.setRevisions(('2012-09-05 00:00','2010-05-24 00:00','2010-05-17 00:00'))
_FsIpDbScalars_ObjectIdentity=ObjectIdentity
fsIpDbScalars=_FsIpDbScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,2,2,1))
_FsIpDbNoOfBindings_Type=Counter32
_FsIpDbNoOfBindings_Object=MibScalar
fsIpDbNoOfBindings=_FsIpDbNoOfBindings_Object((1,3,6,1,4,1,10876,101,2,2,1,1),_FsIpDbNoOfBindings_Type())
fsIpDbNoOfBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfBindings.setStatus(_A)
_FsIpDbNoOfStaticBindings_Type=Counter32
_FsIpDbNoOfStaticBindings_Object=MibScalar
fsIpDbNoOfStaticBindings=_FsIpDbNoOfStaticBindings_Object((1,3,6,1,4,1,10876,101,2,2,1,2),_FsIpDbNoOfStaticBindings_Type())
fsIpDbNoOfStaticBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfStaticBindings.setStatus(_A)
_FsIpDbNoOfDHCPBindings_Type=Counter32
_FsIpDbNoOfDHCPBindings_Object=MibScalar
fsIpDbNoOfDHCPBindings=_FsIpDbNoOfDHCPBindings_Object((1,3,6,1,4,1,10876,101,2,2,1,3),_FsIpDbNoOfDHCPBindings_Type())
fsIpDbNoOfDHCPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfDHCPBindings.setStatus(_A)
_FsIpDbNoOfPPPBindings_Type=Counter32
_FsIpDbNoOfPPPBindings_Object=MibScalar
fsIpDbNoOfPPPBindings=_FsIpDbNoOfPPPBindings_Object((1,3,6,1,4,1,10876,101,2,2,1,4),_FsIpDbNoOfPPPBindings_Type())
fsIpDbNoOfPPPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbNoOfPPPBindings.setStatus(_A)
_FsIpDbTraceLevel_Type=Integer32
_FsIpDbTraceLevel_Object=MibScalar
fsIpDbTraceLevel=_FsIpDbTraceLevel_Object((1,3,6,1,4,1,10876,101,2,2,1,5),_FsIpDbTraceLevel_Type())
fsIpDbTraceLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbTraceLevel.setStatus(_A)
_FsIpDbStatic_ObjectIdentity=ObjectIdentity
fsIpDbStatic=_FsIpDbStatic_ObjectIdentity((1,3,6,1,4,1,10876,101,2,2,2))
_FsIpDbStaticBindingTable_Object=MibTable
fsIpDbStaticBindingTable=_FsIpDbStaticBindingTable_Object((1,3,6,1,4,1,10876,101,2,2,2,1))
if mibBuilder.loadTexts:fsIpDbStaticBindingTable.setStatus(_A)
_FsIpDbStaticBindingEntry_Object=MibTableRow
fsIpDbStaticBindingEntry=_FsIpDbStaticBindingEntry_Object((1,3,6,1,4,1,10876,101,2,2,2,1,1))
fsIpDbStaticBindingEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:fsIpDbStaticBindingEntry.setStatus(_A)
class _FsIpDbStaticHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbStaticHostVlanId_Type.__name__=_E
_FsIpDbStaticHostVlanId_Object=MibTableColumn
fsIpDbStaticHostVlanId=_FsIpDbStaticHostVlanId_Object((1,3,6,1,4,1,10876,101,2,2,2,1,1,1),_FsIpDbStaticHostVlanId_Type())
fsIpDbStaticHostVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbStaticHostVlanId.setStatus(_A)
_FsIpDbStaticHostMac_Type=MacAddress
_FsIpDbStaticHostMac_Object=MibTableColumn
fsIpDbStaticHostMac=_FsIpDbStaticHostMac_Object((1,3,6,1,4,1,10876,101,2,2,2,1,1,2),_FsIpDbStaticHostMac_Type())
fsIpDbStaticHostMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbStaticHostMac.setStatus(_A)
_FsIpDbStaticHostIp_Type=IpAddress
_FsIpDbStaticHostIp_Object=MibTableColumn
fsIpDbStaticHostIp=_FsIpDbStaticHostIp_Object((1,3,6,1,4,1,10876,101,2,2,2,1,1,3),_FsIpDbStaticHostIp_Type())
fsIpDbStaticHostIp.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbStaticHostIp.setStatus(_A)
_FsIpDbStaticInIfIndex_Type=Integer32
_FsIpDbStaticInIfIndex_Object=MibTableColumn
fsIpDbStaticInIfIndex=_FsIpDbStaticInIfIndex_Object((1,3,6,1,4,1,10876,101,2,2,2,1,1,4),_FsIpDbStaticInIfIndex_Type())
fsIpDbStaticInIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbStaticInIfIndex.setStatus(_A)
_FsIpDbStaticGateway_Type=IpAddress
_FsIpDbStaticGateway_Object=MibTableColumn
fsIpDbStaticGateway=_FsIpDbStaticGateway_Object((1,3,6,1,4,1,10876,101,2,2,2,1,1,5),_FsIpDbStaticGateway_Type())
fsIpDbStaticGateway.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbStaticGateway.setStatus(_A)
_FsIpDbStaticBindingStatus_Type=RowStatus
_FsIpDbStaticBindingStatus_Object=MibTableColumn
fsIpDbStaticBindingStatus=_FsIpDbStaticBindingStatus_Object((1,3,6,1,4,1,10876,101,2,2,2,1,1,6),_FsIpDbStaticBindingStatus_Type())
fsIpDbStaticBindingStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbStaticBindingStatus.setStatus(_A)
_FsIpDbBindings_ObjectIdentity=ObjectIdentity
fsIpDbBindings=_FsIpDbBindings_ObjectIdentity((1,3,6,1,4,1,10876,101,2,2,3))
_FsIpDbBindingTable_Object=MibTable
fsIpDbBindingTable=_FsIpDbBindingTable_Object((1,3,6,1,4,1,10876,101,2,2,3,1))
if mibBuilder.loadTexts:fsIpDbBindingTable.setStatus(_A)
_FsIpDbBindingEntry_Object=MibTableRow
fsIpDbBindingEntry=_FsIpDbBindingEntry_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1))
fsIpDbBindingEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:fsIpDbBindingEntry.setStatus(_A)
class _FsIpDbHostVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbHostVlanId_Type.__name__=_E
_FsIpDbHostVlanId_Object=MibTableColumn
fsIpDbHostVlanId=_FsIpDbHostVlanId_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1,1),_FsIpDbHostVlanId_Type())
fsIpDbHostVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbHostVlanId.setStatus(_A)
_FsIpDbHostMac_Type=MacAddress
_FsIpDbHostMac_Object=MibTableColumn
fsIpDbHostMac=_FsIpDbHostMac_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1,2),_FsIpDbHostMac_Type())
fsIpDbHostMac.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbHostMac.setStatus(_A)
class _FsIpDbHostBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dhcp',2),('ppp',3)))
_FsIpDbHostBindingType_Type.__name__=_E
_FsIpDbHostBindingType_Object=MibTableColumn
fsIpDbHostBindingType=_FsIpDbHostBindingType_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1,3),_FsIpDbHostBindingType_Type())
fsIpDbHostBindingType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostBindingType.setStatus(_A)
_FsIpDbHostIp_Type=IpAddress
_FsIpDbHostIp_Object=MibTableColumn
fsIpDbHostIp=_FsIpDbHostIp_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1,4),_FsIpDbHostIp_Type())
fsIpDbHostIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostIp.setStatus(_A)
_FsIpDbHostInIfIndex_Type=Integer32
_FsIpDbHostInIfIndex_Object=MibTableColumn
fsIpDbHostInIfIndex=_FsIpDbHostInIfIndex_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1,5),_FsIpDbHostInIfIndex_Type())
fsIpDbHostInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostInIfIndex.setStatus(_A)
_FsIpDbHostRemLeaseTime_Type=Integer32
_FsIpDbHostRemLeaseTime_Object=MibTableColumn
fsIpDbHostRemLeaseTime=_FsIpDbHostRemLeaseTime_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1,6),_FsIpDbHostRemLeaseTime_Type())
fsIpDbHostRemLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostRemLeaseTime.setStatus(_A)
_FsIpDbHostBindingID_Type=Unsigned32
_FsIpDbHostBindingID_Object=MibTableColumn
fsIpDbHostBindingID=_FsIpDbHostBindingID_Object((1,3,6,1,4,1,10876,101,2,2,3,1,1,7),_FsIpDbHostBindingID_Type())
fsIpDbHostBindingID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbHostBindingID.setStatus(_A)
_FsIpDbGatewayIpTable_Object=MibTable
fsIpDbGatewayIpTable=_FsIpDbGatewayIpTable_Object((1,3,6,1,4,1,10876,101,2,2,3,2))
if mibBuilder.loadTexts:fsIpDbGatewayIpTable.setStatus(_A)
_FsIpDbGatewayIpEntry_Object=MibTableRow
fsIpDbGatewayIpEntry=_FsIpDbGatewayIpEntry_Object((1,3,6,1,4,1,10876,101,2,2,3,2,1))
fsIpDbGatewayIpEntry.setIndexNames((0,_C,_H),(0,_C,_G),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:fsIpDbGatewayIpEntry.setStatus(_A)
_FsIpDbGatewayNetwork_Type=IpAddress
_FsIpDbGatewayNetwork_Object=MibTableColumn
fsIpDbGatewayNetwork=_FsIpDbGatewayNetwork_Object((1,3,6,1,4,1,10876,101,2,2,3,2,1,1),_FsIpDbGatewayNetwork_Type())
fsIpDbGatewayNetwork.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbGatewayNetwork.setStatus(_A)
_FsIpDbGatewayNetMask_Type=IpAddress
_FsIpDbGatewayNetMask_Object=MibTableColumn
fsIpDbGatewayNetMask=_FsIpDbGatewayNetMask_Object((1,3,6,1,4,1,10876,101,2,2,3,2,1,2),_FsIpDbGatewayNetMask_Type())
fsIpDbGatewayNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbGatewayNetMask.setStatus(_A)
_FsIpDbGatewayIp_Type=IpAddress
_FsIpDbGatewayIp_Object=MibTableColumn
fsIpDbGatewayIp=_FsIpDbGatewayIp_Object((1,3,6,1,4,1,10876,101,2,2,3,2,1,3),_FsIpDbGatewayIp_Type())
fsIpDbGatewayIp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbGatewayIp.setStatus(_A)
class _FsIpDbGatewayIpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('active',0))
_FsIpDbGatewayIpMode_Type.__name__=_E
_FsIpDbGatewayIpMode_Object=MibTableColumn
fsIpDbGatewayIpMode=_FsIpDbGatewayIpMode_Object((1,3,6,1,4,1,10876,101,2,2,3,2,1,4),_FsIpDbGatewayIpMode_Type())
fsIpDbGatewayIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbGatewayIpMode.setStatus(_A)
_FsIpDbInterface_ObjectIdentity=ObjectIdentity
fsIpDbInterface=_FsIpDbInterface_ObjectIdentity((1,3,6,1,4,1,10876,101,2,2,4))
_FsIpDbInterfaceTable_Object=MibTable
fsIpDbInterfaceTable=_FsIpDbInterfaceTable_Object((1,3,6,1,4,1,10876,101,2,2,4,1))
if mibBuilder.loadTexts:fsIpDbInterfaceTable.setStatus(_A)
_FsIpDbInterfaceEntry_Object=MibTableRow
fsIpDbInterfaceEntry=_FsIpDbInterfaceEntry_Object((1,3,6,1,4,1,10876,101,2,2,4,1,1))
fsIpDbInterfaceEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:fsIpDbInterfaceEntry.setStatus(_A)
class _FsIpDbIntfVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsIpDbIntfVlanId_Type.__name__=_E
_FsIpDbIntfVlanId_Object=MibTableColumn
fsIpDbIntfVlanId=_FsIpDbIntfVlanId_Object((1,3,6,1,4,1,10876,101,2,2,4,1,1,1),_FsIpDbIntfVlanId_Type())
fsIpDbIntfVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbIntfVlanId.setStatus(_A)
_FsIpDbIntfNoOfVlanBindings_Type=Counter32
_FsIpDbIntfNoOfVlanBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanBindings=_FsIpDbIntfNoOfVlanBindings_Object((1,3,6,1,4,1,10876,101,2,2,4,1,1,2),_FsIpDbIntfNoOfVlanBindings_Type())
fsIpDbIntfNoOfVlanBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanBindings.setStatus(_A)
_FsIpDbIntfNoOfVlanStaticBindings_Type=Counter32
_FsIpDbIntfNoOfVlanStaticBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanStaticBindings=_FsIpDbIntfNoOfVlanStaticBindings_Object((1,3,6,1,4,1,10876,101,2,2,4,1,1,3),_FsIpDbIntfNoOfVlanStaticBindings_Type())
fsIpDbIntfNoOfVlanStaticBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanStaticBindings.setStatus(_A)
_FsIpDbIntfNoOfVlanDHCPBindings_Type=Counter32
_FsIpDbIntfNoOfVlanDHCPBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanDHCPBindings=_FsIpDbIntfNoOfVlanDHCPBindings_Object((1,3,6,1,4,1,10876,101,2,2,4,1,1,4),_FsIpDbIntfNoOfVlanDHCPBindings_Type())
fsIpDbIntfNoOfVlanDHCPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanDHCPBindings.setStatus(_A)
_FsIpDbIntfNoOfVlanPPPBindings_Type=Counter32
_FsIpDbIntfNoOfVlanPPPBindings_Object=MibTableColumn
fsIpDbIntfNoOfVlanPPPBindings=_FsIpDbIntfNoOfVlanPPPBindings_Object((1,3,6,1,4,1,10876,101,2,2,4,1,1,5),_FsIpDbIntfNoOfVlanPPPBindings_Type())
fsIpDbIntfNoOfVlanPPPBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:fsIpDbIntfNoOfVlanPPPBindings.setStatus(_A)
_FsIpDbSrcGuard_ObjectIdentity=ObjectIdentity
fsIpDbSrcGuard=_FsIpDbSrcGuard_ObjectIdentity((1,3,6,1,4,1,10876,101,2,2,5))
_FsIpDbSrcGuardConfigTable_Object=MibTable
fsIpDbSrcGuardConfigTable=_FsIpDbSrcGuardConfigTable_Object((1,3,6,1,4,1,10876,101,2,2,5,1))
if mibBuilder.loadTexts:fsIpDbSrcGuardConfigTable.setStatus(_A)
_FsIpDbSrcGuardConfigEntry_Object=MibTableRow
fsIpDbSrcGuardConfigEntry=_FsIpDbSrcGuardConfigEntry_Object((1,3,6,1,4,1,10876,101,2,2,5,1,1))
fsIpDbSrcGuardConfigEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:fsIpDbSrcGuardConfigEntry.setStatus(_A)
_FsIpDbSrcGuardIndex_Type=InterfaceIndex
_FsIpDbSrcGuardIndex_Object=MibTableColumn
fsIpDbSrcGuardIndex=_FsIpDbSrcGuardIndex_Object((1,3,6,1,4,1,10876,101,2,2,5,1,1,1),_FsIpDbSrcGuardIndex_Type())
fsIpDbSrcGuardIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIpDbSrcGuardIndex.setStatus(_A)
class _FsIpDbSrcGuardStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disable',1),('ip',2),('ipMac',3)))
_FsIpDbSrcGuardStatus_Type.__name__=_E
_FsIpDbSrcGuardStatus_Object=MibTableColumn
fsIpDbSrcGuardStatus=_FsIpDbSrcGuardStatus_Object((1,3,6,1,4,1,10876,101,2,2,5,1,1,2),_FsIpDbSrcGuardStatus_Type())
fsIpDbSrcGuardStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIpDbSrcGuardStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsipdb':fsipdb,'fsIpDbScalars':fsIpDbScalars,'fsIpDbNoOfBindings':fsIpDbNoOfBindings,'fsIpDbNoOfStaticBindings':fsIpDbNoOfStaticBindings,'fsIpDbNoOfDHCPBindings':fsIpDbNoOfDHCPBindings,'fsIpDbNoOfPPPBindings':fsIpDbNoOfPPPBindings,'fsIpDbTraceLevel':fsIpDbTraceLevel,'fsIpDbStatic':fsIpDbStatic,'fsIpDbStaticBindingTable':fsIpDbStaticBindingTable,'fsIpDbStaticBindingEntry':fsIpDbStaticBindingEntry,_I:fsIpDbStaticHostVlanId,_J:fsIpDbStaticHostMac,'fsIpDbStaticHostIp':fsIpDbStaticHostIp,'fsIpDbStaticInIfIndex':fsIpDbStaticInIfIndex,'fsIpDbStaticGateway':fsIpDbStaticGateway,'fsIpDbStaticBindingStatus':fsIpDbStaticBindingStatus,'fsIpDbBindings':fsIpDbBindings,'fsIpDbBindingTable':fsIpDbBindingTable,'fsIpDbBindingEntry':fsIpDbBindingEntry,_G:fsIpDbHostVlanId,_H:fsIpDbHostMac,'fsIpDbHostBindingType':fsIpDbHostBindingType,'fsIpDbHostIp':fsIpDbHostIp,'fsIpDbHostInIfIndex':fsIpDbHostInIfIndex,'fsIpDbHostRemLeaseTime':fsIpDbHostRemLeaseTime,'fsIpDbHostBindingID':fsIpDbHostBindingID,'fsIpDbGatewayIpTable':fsIpDbGatewayIpTable,'fsIpDbGatewayIpEntry':fsIpDbGatewayIpEntry,_K:fsIpDbGatewayNetwork,_L:fsIpDbGatewayNetMask,_M:fsIpDbGatewayIp,'fsIpDbGatewayIpMode':fsIpDbGatewayIpMode,'fsIpDbInterface':fsIpDbInterface,'fsIpDbInterfaceTable':fsIpDbInterfaceTable,'fsIpDbInterfaceEntry':fsIpDbInterfaceEntry,_N:fsIpDbIntfVlanId,'fsIpDbIntfNoOfVlanBindings':fsIpDbIntfNoOfVlanBindings,'fsIpDbIntfNoOfVlanStaticBindings':fsIpDbIntfNoOfVlanStaticBindings,'fsIpDbIntfNoOfVlanDHCPBindings':fsIpDbIntfNoOfVlanDHCPBindings,'fsIpDbIntfNoOfVlanPPPBindings':fsIpDbIntfNoOfVlanPPPBindings,'fsIpDbSrcGuard':fsIpDbSrcGuard,'fsIpDbSrcGuardConfigTable':fsIpDbSrcGuardConfigTable,'fsIpDbSrcGuardConfigEntry':fsIpDbSrcGuardConfigEntry,_O:fsIpDbSrcGuardIndex,'fsIpDbSrcGuardStatus':fsIpDbSrcGuardStatus})