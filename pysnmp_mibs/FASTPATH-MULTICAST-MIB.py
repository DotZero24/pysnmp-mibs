_R='agentIpStaticMRouteSrcNetMask'
_Q='agentIpStaticMRouteSrcIpAddr'
_P='agentIpStaticMRouteSrcAddressType'
_O='agentMulticastPIMSMInterfaceIndex'
_N='agentMulticastPIMSMStaticRPGroupIpMask'
_M='agentMulticastPIMSMStaticRPGroupIpAddr'
_L='agentMulticastPIMSMStaticRPIpAddr'
_K='agentMulticastIGMPInterfaceIfIndex'
_J='Unsigned32'
_I='read-create'
_H='not-accessible'
_G='disable'
_F='enable'
_E='FASTPATH-MULTICAST-MIB'
_D='read-write'
_C='obsolete'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fastPathMulticast=ModuleIdentity((1,3,6,1,4,1,4413,1,1,4))
if mibBuilder.loadTexts:fastPathMulticast.setRevisions(('2009-01-03 00:00','2007-05-23 00:00','2003-11-21 00:00','2002-05-08 14:18'))
_AgentMulticastIGMPConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastIGMPConfigGroup=_AgentMulticastIGMPConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,4,1))
class _AgentMulticastIGMPAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMulticastIGMPAdminMode_Type.__name__=_B
_AgentMulticastIGMPAdminMode_Object=MibScalar
agentMulticastIGMPAdminMode=_AgentMulticastIGMPAdminMode_Object((1,3,6,1,4,1,4413,1,1,4,1,1),_AgentMulticastIGMPAdminMode_Type())
agentMulticastIGMPAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastIGMPAdminMode.setStatus(_A)
_AgentMulticastIGMPInterfaceTable_Object=MibTable
agentMulticastIGMPInterfaceTable=_AgentMulticastIGMPInterfaceTable_Object((1,3,6,1,4,1,4413,1,1,4,1,2))
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceTable.setStatus(_C)
_AgentMulticastIGMPInterfaceEntry_Object=MibTableRow
agentMulticastIGMPInterfaceEntry=_AgentMulticastIGMPInterfaceEntry_Object((1,3,6,1,4,1,4413,1,1,4,1,2,1))
agentMulticastIGMPInterfaceEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceEntry.setStatus(_C)
class _AgentMulticastIGMPInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AgentMulticastIGMPInterfaceIfIndex_Type.__name__=_B
_AgentMulticastIGMPInterfaceIfIndex_Object=MibTableColumn
agentMulticastIGMPInterfaceIfIndex=_AgentMulticastIGMPInterfaceIfIndex_Object((1,3,6,1,4,1,4413,1,1,4,1,2,1,1),_AgentMulticastIGMPInterfaceIfIndex_Type())
agentMulticastIGMPInterfaceIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceIfIndex.setStatus(_C)
class _AgentMulticastIGMPInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMulticastIGMPInterfaceAdminMode_Type.__name__=_B
_AgentMulticastIGMPInterfaceAdminMode_Object=MibTableColumn
agentMulticastIGMPInterfaceAdminMode=_AgentMulticastIGMPInterfaceAdminMode_Object((1,3,6,1,4,1,4413,1,1,4,1,2,1,2),_AgentMulticastIGMPInterfaceAdminMode_Type())
agentMulticastIGMPInterfaceAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastIGMPInterfaceAdminMode.setStatus(_C)
_AgentMulticastPIMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastPIMConfigGroup=_AgentMulticastPIMConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,4,2))
class _AgentMulticastPIMConfigMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sparse',1),('dense',2)))
_AgentMulticastPIMConfigMode_Type.__name__=_B
_AgentMulticastPIMConfigMode_Object=MibScalar
agentMulticastPIMConfigMode=_AgentMulticastPIMConfigMode_Object((1,3,6,1,4,1,4413,1,1,4,2,1),_AgentMulticastPIMConfigMode_Type())
agentMulticastPIMConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastPIMConfigMode.setStatus(_C)
_AgentMulticastPIMSMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastPIMSMConfigGroup=_AgentMulticastPIMSMConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,4,3))
class _AgentMulticastPIMSMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMulticastPIMSMAdminMode_Type.__name__=_B
_AgentMulticastPIMSMAdminMode_Object=MibScalar
agentMulticastPIMSMAdminMode=_AgentMulticastPIMSMAdminMode_Object((1,3,6,1,4,1,4413,1,1,4,3,1),_AgentMulticastPIMSMAdminMode_Type())
agentMulticastPIMSMAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastPIMSMAdminMode.setStatus(_A)
class _AgentMulticastPIMSMDataThresholdRate_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentMulticastPIMSMDataThresholdRate_Type.__name__=_B
_AgentMulticastPIMSMDataThresholdRate_Object=MibScalar
agentMulticastPIMSMDataThresholdRate=_AgentMulticastPIMSMDataThresholdRate_Object((1,3,6,1,4,1,4413,1,1,4,3,2),_AgentMulticastPIMSMDataThresholdRate_Type())
agentMulticastPIMSMDataThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastPIMSMDataThresholdRate.setStatus(_A)
class _AgentMulticastPIMSMRegThresholdRate_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_AgentMulticastPIMSMRegThresholdRate_Type.__name__=_B
_AgentMulticastPIMSMRegThresholdRate_Object=MibScalar
agentMulticastPIMSMRegThresholdRate=_AgentMulticastPIMSMRegThresholdRate_Object((1,3,6,1,4,1,4413,1,1,4,3,3),_AgentMulticastPIMSMRegThresholdRate_Type())
agentMulticastPIMSMRegThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastPIMSMRegThresholdRate.setStatus(_A)
_AgentMulticastPIMSMStaticRPTable_Object=MibTable
agentMulticastPIMSMStaticRPTable=_AgentMulticastPIMSMStaticRPTable_Object((1,3,6,1,4,1,4413,1,1,4,3,4))
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPTable.setStatus(_C)
_AgentMulticastPIMSMStaticRPEntry_Object=MibTableRow
agentMulticastPIMSMStaticRPEntry=_AgentMulticastPIMSMStaticRPEntry_Object((1,3,6,1,4,1,4413,1,1,4,3,4,1))
agentMulticastPIMSMStaticRPEntry.setIndexNames((0,_E,_L),(0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPEntry.setStatus(_C)
_AgentMulticastPIMSMStaticRPIpAddr_Type=IpAddress
_AgentMulticastPIMSMStaticRPIpAddr_Object=MibTableColumn
agentMulticastPIMSMStaticRPIpAddr=_AgentMulticastPIMSMStaticRPIpAddr_Object((1,3,6,1,4,1,4413,1,1,4,3,4,1,1),_AgentMulticastPIMSMStaticRPIpAddr_Type())
agentMulticastPIMSMStaticRPIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPIpAddr.setStatus(_C)
_AgentMulticastPIMSMStaticRPGroupIpAddr_Type=IpAddress
_AgentMulticastPIMSMStaticRPGroupIpAddr_Object=MibTableColumn
agentMulticastPIMSMStaticRPGroupIpAddr=_AgentMulticastPIMSMStaticRPGroupIpAddr_Object((1,3,6,1,4,1,4413,1,1,4,3,4,1,2),_AgentMulticastPIMSMStaticRPGroupIpAddr_Type())
agentMulticastPIMSMStaticRPGroupIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPGroupIpAddr.setStatus(_C)
_AgentMulticastPIMSMStaticRPGroupIpMask_Type=IpAddress
_AgentMulticastPIMSMStaticRPGroupIpMask_Object=MibTableColumn
agentMulticastPIMSMStaticRPGroupIpMask=_AgentMulticastPIMSMStaticRPGroupIpMask_Object((1,3,6,1,4,1,4413,1,1,4,3,4,1,3),_AgentMulticastPIMSMStaticRPGroupIpMask_Type())
agentMulticastPIMSMStaticRPGroupIpMask.setMaxAccess(_H)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPGroupIpMask.setStatus(_C)
_AgentMulticastPIMSMStaticRPStatus_Type=RowStatus
_AgentMulticastPIMSMStaticRPStatus_Object=MibTableColumn
agentMulticastPIMSMStaticRPStatus=_AgentMulticastPIMSMStaticRPStatus_Object((1,3,6,1,4,1,4413,1,1,4,3,4,1,4),_AgentMulticastPIMSMStaticRPStatus_Type())
agentMulticastPIMSMStaticRPStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentMulticastPIMSMStaticRPStatus.setStatus(_C)
_AgentMulticastPIMSMInterfaceTable_Object=MibTable
agentMulticastPIMSMInterfaceTable=_AgentMulticastPIMSMInterfaceTable_Object((1,3,6,1,4,1,4413,1,1,4,3,5))
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceTable.setStatus(_C)
_AgentMulticastPIMSMInterfaceEntry_Object=MibTableRow
agentMulticastPIMSMInterfaceEntry=_AgentMulticastPIMSMInterfaceEntry_Object((1,3,6,1,4,1,4413,1,1,4,3,5,1))
agentMulticastPIMSMInterfaceEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceEntry.setStatus(_C)
_AgentMulticastPIMSMInterfaceIndex_Type=Unsigned32
_AgentMulticastPIMSMInterfaceIndex_Object=MibTableColumn
agentMulticastPIMSMInterfaceIndex=_AgentMulticastPIMSMInterfaceIndex_Object((1,3,6,1,4,1,4413,1,1,4,3,5,1,1),_AgentMulticastPIMSMInterfaceIndex_Type())
agentMulticastPIMSMInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceIndex.setStatus(_C)
class _AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type.__name__=_J
_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object=MibTableColumn
agentMulticastPIMSMInterfaceCBSRHashMaskLength=_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object((1,3,6,1,4,1,4413,1,1,4,3,5,1,2),_AgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type())
agentMulticastPIMSMInterfaceCBSRHashMaskLength.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus(_C)
class _AgentMulticastPIMSMInterfaceCRPPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_AgentMulticastPIMSMInterfaceCRPPreference_Type.__name__=_B
_AgentMulticastPIMSMInterfaceCRPPreference_Object=MibTableColumn
agentMulticastPIMSMInterfaceCRPPreference=_AgentMulticastPIMSMInterfaceCRPPreference_Object((1,3,6,1,4,1,4413,1,1,4,3,5,1,3),_AgentMulticastPIMSMInterfaceCRPPreference_Type())
agentMulticastPIMSMInterfaceCRPPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastPIMSMInterfaceCRPPreference.setStatus(_C)
_AgentMulticastPIMDMConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastPIMDMConfigGroup=_AgentMulticastPIMDMConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,4,4))
class _AgentMulticastPIMDMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMulticastPIMDMAdminMode_Type.__name__=_B
_AgentMulticastPIMDMAdminMode_Object=MibScalar
agentMulticastPIMDMAdminMode=_AgentMulticastPIMDMAdminMode_Object((1,3,6,1,4,1,4413,1,1,4,4,1),_AgentMulticastPIMDMAdminMode_Type())
agentMulticastPIMDMAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastPIMDMAdminMode.setStatus(_A)
_AgentMulticastRoutingConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastRoutingConfigGroup=_AgentMulticastRoutingConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,4,5))
class _AgentMulticastRoutingAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMulticastRoutingAdminMode_Type.__name__=_B
_AgentMulticastRoutingAdminMode_Object=MibScalar
agentMulticastRoutingAdminMode=_AgentMulticastRoutingAdminMode_Object((1,3,6,1,4,1,4413,1,1,4,5,1),_AgentMulticastRoutingAdminMode_Type())
agentMulticastRoutingAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastRoutingAdminMode.setStatus(_A)
_AgentMulticastDVMRPConfigGroup_ObjectIdentity=ObjectIdentity
agentMulticastDVMRPConfigGroup=_AgentMulticastDVMRPConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,4,6))
class _AgentMulticastDVMRPAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentMulticastDVMRPAdminMode_Type.__name__=_B
_AgentMulticastDVMRPAdminMode_Object=MibScalar
agentMulticastDVMRPAdminMode=_AgentMulticastDVMRPAdminMode_Object((1,3,6,1,4,1,4413,1,1,4,6,1),_AgentMulticastDVMRPAdminMode_Type())
agentMulticastDVMRPAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:agentMulticastDVMRPAdminMode.setStatus(_A)
_AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity=ObjectIdentity
agentSnmpTrapFlagsConfigGroupMulticast=_AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity((1,3,6,1,4,1,4413,1,1,4,7))
class _AgentSnmpDVMRPTrapFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSnmpDVMRPTrapFlag_Type.__name__=_B
_AgentSnmpDVMRPTrapFlag_Object=MibScalar
agentSnmpDVMRPTrapFlag=_AgentSnmpDVMRPTrapFlag_Object((1,3,6,1,4,1,4413,1,1,4,7,1),_AgentSnmpDVMRPTrapFlag_Type())
agentSnmpDVMRPTrapFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSnmpDVMRPTrapFlag.setStatus(_A)
class _AgentSnmpPIMTrapFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_AgentSnmpPIMTrapFlag_Type.__name__=_B
_AgentSnmpPIMTrapFlag_Object=MibScalar
agentSnmpPIMTrapFlag=_AgentSnmpPIMTrapFlag_Object((1,3,6,1,4,1,4413,1,1,4,7,2),_AgentSnmpPIMTrapFlag_Type())
agentSnmpPIMTrapFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:agentSnmpPIMTrapFlag.setStatus(_A)
_AgentIpStaticMRouteTable_Object=MibTable
agentIpStaticMRouteTable=_AgentIpStaticMRouteTable_Object((1,3,6,1,4,1,4413,1,1,4,8))
if mibBuilder.loadTexts:agentIpStaticMRouteTable.setStatus(_A)
_AgentIpStaticMRouteEntry_Object=MibTableRow
agentIpStaticMRouteEntry=_AgentIpStaticMRouteEntry_Object((1,3,6,1,4,1,4413,1,1,4,8,1))
agentIpStaticMRouteEntry.setIndexNames((0,_E,_P),(0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:agentIpStaticMRouteEntry.setStatus(_A)
_AgentIpStaticMRouteSrcAddressType_Type=InetAddressType
_AgentIpStaticMRouteSrcAddressType_Object=MibTableColumn
agentIpStaticMRouteSrcAddressType=_AgentIpStaticMRouteSrcAddressType_Object((1,3,6,1,4,1,4413,1,1,4,8,1,1),_AgentIpStaticMRouteSrcAddressType_Type())
agentIpStaticMRouteSrcAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpStaticMRouteSrcAddressType.setStatus(_A)
_AgentIpStaticMRouteSrcIpAddr_Type=InetAddress
_AgentIpStaticMRouteSrcIpAddr_Object=MibTableColumn
agentIpStaticMRouteSrcIpAddr=_AgentIpStaticMRouteSrcIpAddr_Object((1,3,6,1,4,1,4413,1,1,4,8,1,2),_AgentIpStaticMRouteSrcIpAddr_Type())
agentIpStaticMRouteSrcIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpStaticMRouteSrcIpAddr.setStatus(_A)
class _AgentIpStaticMRouteSrcNetMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AgentIpStaticMRouteSrcNetMask_Type.__name__=_B
_AgentIpStaticMRouteSrcNetMask_Object=MibTableColumn
agentIpStaticMRouteSrcNetMask=_AgentIpStaticMRouteSrcNetMask_Object((1,3,6,1,4,1,4413,1,1,4,8,1,3),_AgentIpStaticMRouteSrcNetMask_Type())
agentIpStaticMRouteSrcNetMask.setMaxAccess(_H)
if mibBuilder.loadTexts:agentIpStaticMRouteSrcNetMask.setStatus(_A)
_AgentIpStaticMRouteRpfIpAddr_Type=InetAddress
_AgentIpStaticMRouteRpfIpAddr_Object=MibTableColumn
agentIpStaticMRouteRpfIpAddr=_AgentIpStaticMRouteRpfIpAddr_Object((1,3,6,1,4,1,4413,1,1,4,8,1,4),_AgentIpStaticMRouteRpfIpAddr_Type())
agentIpStaticMRouteRpfIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpStaticMRouteRpfIpAddr.setStatus(_A)
_AgentIpStaticMRouteIfIndex_Type=InterfaceIndex
_AgentIpStaticMRouteIfIndex_Object=MibTableColumn
agentIpStaticMRouteIfIndex=_AgentIpStaticMRouteIfIndex_Object((1,3,6,1,4,1,4413,1,1,4,8,1,5),_AgentIpStaticMRouteIfIndex_Type())
agentIpStaticMRouteIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpStaticMRouteIfIndex.setStatus(_A)
class _AgentIpStaticMRoutePreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentIpStaticMRoutePreference_Type.__name__=_B
_AgentIpStaticMRoutePreference_Object=MibTableColumn
agentIpStaticMRoutePreference=_AgentIpStaticMRoutePreference_Object((1,3,6,1,4,1,4413,1,1,4,8,1,6),_AgentIpStaticMRoutePreference_Type())
agentIpStaticMRoutePreference.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpStaticMRoutePreference.setStatus(_A)
_AgentIpStaticMRouteStatus_Type=RowStatus
_AgentIpStaticMRouteStatus_Object=MibTableColumn
agentIpStaticMRouteStatus=_AgentIpStaticMRouteStatus_Object((1,3,6,1,4,1,4413,1,1,4,8,1,7),_AgentIpStaticMRouteStatus_Type())
agentIpStaticMRouteStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:agentIpStaticMRouteStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fastPathMulticast':fastPathMulticast,'agentMulticastIGMPConfigGroup':agentMulticastIGMPConfigGroup,'agentMulticastIGMPAdminMode':agentMulticastIGMPAdminMode,'agentMulticastIGMPInterfaceTable':agentMulticastIGMPInterfaceTable,'agentMulticastIGMPInterfaceEntry':agentMulticastIGMPInterfaceEntry,_K:agentMulticastIGMPInterfaceIfIndex,'agentMulticastIGMPInterfaceAdminMode':agentMulticastIGMPInterfaceAdminMode,'agentMulticastPIMConfigGroup':agentMulticastPIMConfigGroup,'agentMulticastPIMConfigMode':agentMulticastPIMConfigMode,'agentMulticastPIMSMConfigGroup':agentMulticastPIMSMConfigGroup,'agentMulticastPIMSMAdminMode':agentMulticastPIMSMAdminMode,'agentMulticastPIMSMDataThresholdRate':agentMulticastPIMSMDataThresholdRate,'agentMulticastPIMSMRegThresholdRate':agentMulticastPIMSMRegThresholdRate,'agentMulticastPIMSMStaticRPTable':agentMulticastPIMSMStaticRPTable,'agentMulticastPIMSMStaticRPEntry':agentMulticastPIMSMStaticRPEntry,_L:agentMulticastPIMSMStaticRPIpAddr,_M:agentMulticastPIMSMStaticRPGroupIpAddr,_N:agentMulticastPIMSMStaticRPGroupIpMask,'agentMulticastPIMSMStaticRPStatus':agentMulticastPIMSMStaticRPStatus,'agentMulticastPIMSMInterfaceTable':agentMulticastPIMSMInterfaceTable,'agentMulticastPIMSMInterfaceEntry':agentMulticastPIMSMInterfaceEntry,_O:agentMulticastPIMSMInterfaceIndex,'agentMulticastPIMSMInterfaceCBSRHashMaskLength':agentMulticastPIMSMInterfaceCBSRHashMaskLength,'agentMulticastPIMSMInterfaceCRPPreference':agentMulticastPIMSMInterfaceCRPPreference,'agentMulticastPIMDMConfigGroup':agentMulticastPIMDMConfigGroup,'agentMulticastPIMDMAdminMode':agentMulticastPIMDMAdminMode,'agentMulticastRoutingConfigGroup':agentMulticastRoutingConfigGroup,'agentMulticastRoutingAdminMode':agentMulticastRoutingAdminMode,'agentMulticastDVMRPConfigGroup':agentMulticastDVMRPConfigGroup,'agentMulticastDVMRPAdminMode':agentMulticastDVMRPAdminMode,'agentSnmpTrapFlagsConfigGroupMulticast':agentSnmpTrapFlagsConfigGroupMulticast,'agentSnmpDVMRPTrapFlag':agentSnmpDVMRPTrapFlag,'agentSnmpPIMTrapFlag':agentSnmpPIMTrapFlag,'agentIpStaticMRouteTable':agentIpStaticMRouteTable,'agentIpStaticMRouteEntry':agentIpStaticMRouteEntry,_P:agentIpStaticMRouteSrcAddressType,_Q:agentIpStaticMRouteSrcIpAddr,_R:agentIpStaticMRouteSrcNetMask,'agentIpStaticMRouteRpfIpAddr':agentIpStaticMRouteRpfIpAddr,'agentIpStaticMRouteIfIndex':agentIpStaticMRouteIfIndex,'agentIpStaticMRoutePreference':agentIpStaticMRoutePreference,'agentIpStaticMRouteStatus':agentIpStaticMRouteStatus})