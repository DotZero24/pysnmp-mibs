_R='hmAgentIpStaticMRouteSrcNetMask'
_Q='hmAgentIpStaticMRouteSrcIpAddr'
_P='hmAgentIpStaticMRouteSrcAddressType'
_O='hmAgentMulticastPIMSMInterfaceIndex'
_N='hmAgentMulticastPIMSMStaticRPGroupIpMask'
_M='hmAgentMulticastPIMSMStaticRPGroupIpAddr'
_L='hmAgentMulticastPIMSMStaticRPIpAddr'
_K='hmAgentMulticastIGMPInterfaceIfIndex'
_J='Unsigned32'
_I='read-create'
_H='not-accessible'
_G='disable'
_F='enable'
_E='HIRSCHMANN-MULTICAST-MIB'
_D='read-write'
_C='obsolete'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmPlatform4,=mibBuilder.importSymbols('HIRSCHMANN-MMP4-BASICL2-MIB','hmPlatform4')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hmPlatform4Multicast=ModuleIdentity((1,3,6,1,4,1,248,15,4))
if mibBuilder.loadTexts:hmPlatform4Multicast.setRevisions(('2006-02-03 12:00','2002-05-08 14:18'))
_HmAgentMulticastIGMPConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentMulticastIGMPConfigGroup=_HmAgentMulticastIGMPConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,4,1))
class _HmAgentMulticastIGMPAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentMulticastIGMPAdminMode_Type.__name__=_B
_HmAgentMulticastIGMPAdminMode_Object=MibScalar
hmAgentMulticastIGMPAdminMode=_HmAgentMulticastIGMPAdminMode_Object((1,3,6,1,4,1,248,15,4,1,1),_HmAgentMulticastIGMPAdminMode_Type())
hmAgentMulticastIGMPAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastIGMPAdminMode.setStatus(_A)
_HmAgentMulticastIGMPInterfaceTable_Object=MibTable
hmAgentMulticastIGMPInterfaceTable=_HmAgentMulticastIGMPInterfaceTable_Object((1,3,6,1,4,1,248,15,4,1,2))
if mibBuilder.loadTexts:hmAgentMulticastIGMPInterfaceTable.setStatus(_C)
_HmAgentMulticastIGMPInterfaceEntry_Object=MibTableRow
hmAgentMulticastIGMPInterfaceEntry=_HmAgentMulticastIGMPInterfaceEntry_Object((1,3,6,1,4,1,248,15,4,1,2,1))
hmAgentMulticastIGMPInterfaceEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:hmAgentMulticastIGMPInterfaceEntry.setStatus(_C)
_HmAgentMulticastIGMPInterfaceIfIndex_Type=Integer32
_HmAgentMulticastIGMPInterfaceIfIndex_Object=MibTableColumn
hmAgentMulticastIGMPInterfaceIfIndex=_HmAgentMulticastIGMPInterfaceIfIndex_Object((1,3,6,1,4,1,248,15,4,1,2,1,1),_HmAgentMulticastIGMPInterfaceIfIndex_Type())
hmAgentMulticastIGMPInterfaceIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:hmAgentMulticastIGMPInterfaceIfIndex.setStatus(_C)
class _HmAgentMulticastIGMPInterfaceAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentMulticastIGMPInterfaceAdminMode_Type.__name__=_B
_HmAgentMulticastIGMPInterfaceAdminMode_Object=MibTableColumn
hmAgentMulticastIGMPInterfaceAdminMode=_HmAgentMulticastIGMPInterfaceAdminMode_Object((1,3,6,1,4,1,248,15,4,1,2,1,2),_HmAgentMulticastIGMPInterfaceAdminMode_Type())
hmAgentMulticastIGMPInterfaceAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastIGMPInterfaceAdminMode.setStatus(_C)
class _HmAgentMulticastIGMPSoftwareDSCP_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_HmAgentMulticastIGMPSoftwareDSCP_Type.__name__=_B
_HmAgentMulticastIGMPSoftwareDSCP_Object=MibScalar
hmAgentMulticastIGMPSoftwareDSCP=_HmAgentMulticastIGMPSoftwareDSCP_Object((1,3,6,1,4,1,248,15,4,1,210),_HmAgentMulticastIGMPSoftwareDSCP_Type())
hmAgentMulticastIGMPSoftwareDSCP.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastIGMPSoftwareDSCP.setStatus(_A)
_HmAgentMulticastPIMConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentMulticastPIMConfigGroup=_HmAgentMulticastPIMConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,4,2))
class _HmAgentMulticastPIMConfigMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('sparse',1),('dense',2)))
_HmAgentMulticastPIMConfigMode_Type.__name__=_B
_HmAgentMulticastPIMConfigMode_Object=MibScalar
hmAgentMulticastPIMConfigMode=_HmAgentMulticastPIMConfigMode_Object((1,3,6,1,4,1,248,15,4,2,1),_HmAgentMulticastPIMConfigMode_Type())
hmAgentMulticastPIMConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMConfigMode.setStatus(_C)
class _HmAgentMulticastPIMPruneHoldtime_Type(Integer32):defaultValue=210;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,64800))
_HmAgentMulticastPIMPruneHoldtime_Type.__name__=_B
_HmAgentMulticastPIMPruneHoldtime_Object=MibScalar
hmAgentMulticastPIMPruneHoldtime=_HmAgentMulticastPIMPruneHoldtime_Object((1,3,6,1,4,1,248,15,4,2,2),_HmAgentMulticastPIMPruneHoldtime_Type())
hmAgentMulticastPIMPruneHoldtime.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMPruneHoldtime.setStatus(_C)
_HmAgentMulticastPIMSMConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentMulticastPIMSMConfigGroup=_HmAgentMulticastPIMSMConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,4,3))
class _HmAgentMulticastPIMSMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentMulticastPIMSMAdminMode_Type.__name__=_B
_HmAgentMulticastPIMSMAdminMode_Object=MibScalar
hmAgentMulticastPIMSMAdminMode=_HmAgentMulticastPIMSMAdminMode_Object((1,3,6,1,4,1,248,15,4,3,1),_HmAgentMulticastPIMSMAdminMode_Type())
hmAgentMulticastPIMSMAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMAdminMode.setStatus(_A)
class _HmAgentMulticastPIMSMDataThresholdRate_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_HmAgentMulticastPIMSMDataThresholdRate_Type.__name__=_B
_HmAgentMulticastPIMSMDataThresholdRate_Object=MibScalar
hmAgentMulticastPIMSMDataThresholdRate=_HmAgentMulticastPIMSMDataThresholdRate_Object((1,3,6,1,4,1,248,15,4,3,2),_HmAgentMulticastPIMSMDataThresholdRate_Type())
hmAgentMulticastPIMSMDataThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMDataThresholdRate.setStatus(_A)
class _HmAgentMulticastPIMSMRegThresholdRate_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_HmAgentMulticastPIMSMRegThresholdRate_Type.__name__=_B
_HmAgentMulticastPIMSMRegThresholdRate_Object=MibScalar
hmAgentMulticastPIMSMRegThresholdRate=_HmAgentMulticastPIMSMRegThresholdRate_Object((1,3,6,1,4,1,248,15,4,3,3),_HmAgentMulticastPIMSMRegThresholdRate_Type())
hmAgentMulticastPIMSMRegThresholdRate.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMRegThresholdRate.setStatus(_A)
_HmAgentMulticastPIMSMStaticRPTable_Object=MibTable
hmAgentMulticastPIMSMStaticRPTable=_HmAgentMulticastPIMSMStaticRPTable_Object((1,3,6,1,4,1,248,15,4,3,4))
if mibBuilder.loadTexts:hmAgentMulticastPIMSMStaticRPTable.setStatus(_C)
_HmAgentMulticastPIMSMStaticRPEntry_Object=MibTableRow
hmAgentMulticastPIMSMStaticRPEntry=_HmAgentMulticastPIMSMStaticRPEntry_Object((1,3,6,1,4,1,248,15,4,3,4,1))
hmAgentMulticastPIMSMStaticRPEntry.setIndexNames((0,_E,_L),(0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:hmAgentMulticastPIMSMStaticRPEntry.setStatus(_C)
_HmAgentMulticastPIMSMStaticRPIpAddr_Type=IpAddress
_HmAgentMulticastPIMSMStaticRPIpAddr_Object=MibTableColumn
hmAgentMulticastPIMSMStaticRPIpAddr=_HmAgentMulticastPIMSMStaticRPIpAddr_Object((1,3,6,1,4,1,248,15,4,3,4,1,1),_HmAgentMulticastPIMSMStaticRPIpAddr_Type())
hmAgentMulticastPIMSMStaticRPIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMStaticRPIpAddr.setStatus(_C)
_HmAgentMulticastPIMSMStaticRPGroupIpAddr_Type=IpAddress
_HmAgentMulticastPIMSMStaticRPGroupIpAddr_Object=MibTableColumn
hmAgentMulticastPIMSMStaticRPGroupIpAddr=_HmAgentMulticastPIMSMStaticRPGroupIpAddr_Object((1,3,6,1,4,1,248,15,4,3,4,1,2),_HmAgentMulticastPIMSMStaticRPGroupIpAddr_Type())
hmAgentMulticastPIMSMStaticRPGroupIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMStaticRPGroupIpAddr.setStatus(_C)
_HmAgentMulticastPIMSMStaticRPGroupIpMask_Type=IpAddress
_HmAgentMulticastPIMSMStaticRPGroupIpMask_Object=MibTableColumn
hmAgentMulticastPIMSMStaticRPGroupIpMask=_HmAgentMulticastPIMSMStaticRPGroupIpMask_Object((1,3,6,1,4,1,248,15,4,3,4,1,3),_HmAgentMulticastPIMSMStaticRPGroupIpMask_Type())
hmAgentMulticastPIMSMStaticRPGroupIpMask.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMStaticRPGroupIpMask.setStatus(_C)
_HmAgentMulticastPIMSMStaticRPStatus_Type=RowStatus
_HmAgentMulticastPIMSMStaticRPStatus_Object=MibTableColumn
hmAgentMulticastPIMSMStaticRPStatus=_HmAgentMulticastPIMSMStaticRPStatus_Object((1,3,6,1,4,1,248,15,4,3,4,1,4),_HmAgentMulticastPIMSMStaticRPStatus_Type())
hmAgentMulticastPIMSMStaticRPStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMStaticRPStatus.setStatus(_C)
_HmAgentMulticastPIMSMInterfaceTable_Object=MibTable
hmAgentMulticastPIMSMInterfaceTable=_HmAgentMulticastPIMSMInterfaceTable_Object((1,3,6,1,4,1,248,15,4,3,5))
if mibBuilder.loadTexts:hmAgentMulticastPIMSMInterfaceTable.setStatus(_C)
_HmAgentMulticastPIMSMInterfaceEntry_Object=MibTableRow
hmAgentMulticastPIMSMInterfaceEntry=_HmAgentMulticastPIMSMInterfaceEntry_Object((1,3,6,1,4,1,248,15,4,3,5,1))
hmAgentMulticastPIMSMInterfaceEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hmAgentMulticastPIMSMInterfaceEntry.setStatus(_C)
_HmAgentMulticastPIMSMInterfaceIndex_Type=Unsigned32
_HmAgentMulticastPIMSMInterfaceIndex_Object=MibTableColumn
hmAgentMulticastPIMSMInterfaceIndex=_HmAgentMulticastPIMSMInterfaceIndex_Object((1,3,6,1,4,1,248,15,4,3,5,1,1),_HmAgentMulticastPIMSMInterfaceIndex_Type())
hmAgentMulticastPIMSMInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMInterfaceIndex.setStatus(_C)
class _HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type.__name__=_J
_HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object=MibTableColumn
hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength=_HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Object((1,3,6,1,4,1,248,15,4,3,5,1,2),_HmAgentMulticastPIMSMInterfaceCBSRHashMaskLength_Type())
hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength.setStatus(_C)
class _HmAgentMulticastPIMSMInterfaceCRPPreference_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,255))
_HmAgentMulticastPIMSMInterfaceCRPPreference_Type.__name__=_B
_HmAgentMulticastPIMSMInterfaceCRPPreference_Object=MibTableColumn
hmAgentMulticastPIMSMInterfaceCRPPreference=_HmAgentMulticastPIMSMInterfaceCRPPreference_Object((1,3,6,1,4,1,248,15,4,3,5,1,3),_HmAgentMulticastPIMSMInterfaceCRPPreference_Type())
hmAgentMulticastPIMSMInterfaceCRPPreference.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMSMInterfaceCRPPreference.setStatus(_C)
_HmAgentMulticastPIMDMConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentMulticastPIMDMConfigGroup=_HmAgentMulticastPIMDMConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,4,4))
class _HmAgentMulticastPIMDMAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentMulticastPIMDMAdminMode_Type.__name__=_B
_HmAgentMulticastPIMDMAdminMode_Object=MibScalar
hmAgentMulticastPIMDMAdminMode=_HmAgentMulticastPIMDMAdminMode_Object((1,3,6,1,4,1,248,15,4,4,1),_HmAgentMulticastPIMDMAdminMode_Type())
hmAgentMulticastPIMDMAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastPIMDMAdminMode.setStatus(_A)
_HmAgentMulticastRoutingConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentMulticastRoutingConfigGroup=_HmAgentMulticastRoutingConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,4,5))
class _HmAgentMulticastRoutingAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentMulticastRoutingAdminMode_Type.__name__=_B
_HmAgentMulticastRoutingAdminMode_Object=MibScalar
hmAgentMulticastRoutingAdminMode=_HmAgentMulticastRoutingAdminMode_Object((1,3,6,1,4,1,248,15,4,5,1),_HmAgentMulticastRoutingAdminMode_Type())
hmAgentMulticastRoutingAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastRoutingAdminMode.setStatus(_A)
_HmAgentMulticastDVMRPConfigGroup_ObjectIdentity=ObjectIdentity
hmAgentMulticastDVMRPConfigGroup=_HmAgentMulticastDVMRPConfigGroup_ObjectIdentity((1,3,6,1,4,1,248,15,4,6))
class _HmAgentMulticastDVMRPAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentMulticastDVMRPAdminMode_Type.__name__=_B
_HmAgentMulticastDVMRPAdminMode_Object=MibScalar
hmAgentMulticastDVMRPAdminMode=_HmAgentMulticastDVMRPAdminMode_Object((1,3,6,1,4,1,248,15,4,6,1),_HmAgentMulticastDVMRPAdminMode_Type())
hmAgentMulticastDVMRPAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentMulticastDVMRPAdminMode.setStatus(_A)
_HmAgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity=ObjectIdentity
hmAgentSnmpTrapFlagsConfigGroupMulticast=_HmAgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity((1,3,6,1,4,1,248,15,4,7))
class _HmAgentSnmpDVMRPTrapFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSnmpDVMRPTrapFlag_Type.__name__=_B
_HmAgentSnmpDVMRPTrapFlag_Object=MibScalar
hmAgentSnmpDVMRPTrapFlag=_HmAgentSnmpDVMRPTrapFlag_Object((1,3,6,1,4,1,248,15,4,7,1),_HmAgentSnmpDVMRPTrapFlag_Type())
hmAgentSnmpDVMRPTrapFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSnmpDVMRPTrapFlag.setStatus(_A)
class _HmAgentSnmpPIMTrapFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_HmAgentSnmpPIMTrapFlag_Type.__name__=_B
_HmAgentSnmpPIMTrapFlag_Object=MibScalar
hmAgentSnmpPIMTrapFlag=_HmAgentSnmpPIMTrapFlag_Object((1,3,6,1,4,1,248,15,4,7,2),_HmAgentSnmpPIMTrapFlag_Type())
hmAgentSnmpPIMTrapFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:hmAgentSnmpPIMTrapFlag.setStatus(_A)
_HmAgentIpStaticMRouteTable_Object=MibTable
hmAgentIpStaticMRouteTable=_HmAgentIpStaticMRouteTable_Object((1,3,6,1,4,1,248,15,4,8))
if mibBuilder.loadTexts:hmAgentIpStaticMRouteTable.setStatus(_A)
_HmAgentIpStaticMRouteEntry_Object=MibTableRow
hmAgentIpStaticMRouteEntry=_HmAgentIpStaticMRouteEntry_Object((1,3,6,1,4,1,248,15,4,8,1))
hmAgentIpStaticMRouteEntry.setIndexNames((0,_E,_P),(0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:hmAgentIpStaticMRouteEntry.setStatus(_A)
_HmAgentIpStaticMRouteSrcAddressType_Type=InetAddressType
_HmAgentIpStaticMRouteSrcAddressType_Object=MibTableColumn
hmAgentIpStaticMRouteSrcAddressType=_HmAgentIpStaticMRouteSrcAddressType_Object((1,3,6,1,4,1,248,15,4,8,1,1),_HmAgentIpStaticMRouteSrcAddressType_Type())
hmAgentIpStaticMRouteSrcAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentIpStaticMRouteSrcAddressType.setStatus(_A)
_HmAgentIpStaticMRouteSrcIpAddr_Type=InetAddress
_HmAgentIpStaticMRouteSrcIpAddr_Object=MibTableColumn
hmAgentIpStaticMRouteSrcIpAddr=_HmAgentIpStaticMRouteSrcIpAddr_Object((1,3,6,1,4,1,248,15,4,8,1,2),_HmAgentIpStaticMRouteSrcIpAddr_Type())
hmAgentIpStaticMRouteSrcIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentIpStaticMRouteSrcIpAddr.setStatus(_A)
class _HmAgentIpStaticMRouteSrcNetMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_HmAgentIpStaticMRouteSrcNetMask_Type.__name__=_B
_HmAgentIpStaticMRouteSrcNetMask_Object=MibTableColumn
hmAgentIpStaticMRouteSrcNetMask=_HmAgentIpStaticMRouteSrcNetMask_Object((1,3,6,1,4,1,248,15,4,8,1,3),_HmAgentIpStaticMRouteSrcNetMask_Type())
hmAgentIpStaticMRouteSrcNetMask.setMaxAccess(_H)
if mibBuilder.loadTexts:hmAgentIpStaticMRouteSrcNetMask.setStatus(_A)
_HmAgentIpStaticMRouteRpfIpAddr_Type=InetAddress
_HmAgentIpStaticMRouteRpfIpAddr_Object=MibTableColumn
hmAgentIpStaticMRouteRpfIpAddr=_HmAgentIpStaticMRouteRpfIpAddr_Object((1,3,6,1,4,1,248,15,4,8,1,4),_HmAgentIpStaticMRouteRpfIpAddr_Type())
hmAgentIpStaticMRouteRpfIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentIpStaticMRouteRpfIpAddr.setStatus(_A)
_HmAgentIpStaticMRouteIfIndex_Type=InterfaceIndex
_HmAgentIpStaticMRouteIfIndex_Object=MibTableColumn
hmAgentIpStaticMRouteIfIndex=_HmAgentIpStaticMRouteIfIndex_Object((1,3,6,1,4,1,248,15,4,8,1,5),_HmAgentIpStaticMRouteIfIndex_Type())
hmAgentIpStaticMRouteIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentIpStaticMRouteIfIndex.setStatus(_A)
class _HmAgentIpStaticMRoutePreference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmAgentIpStaticMRoutePreference_Type.__name__=_B
_HmAgentIpStaticMRoutePreference_Object=MibTableColumn
hmAgentIpStaticMRoutePreference=_HmAgentIpStaticMRoutePreference_Object((1,3,6,1,4,1,248,15,4,8,1,6),_HmAgentIpStaticMRoutePreference_Type())
hmAgentIpStaticMRoutePreference.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentIpStaticMRoutePreference.setStatus(_A)
_HmAgentIpStaticMRouteStatus_Type=RowStatus
_HmAgentIpStaticMRouteStatus_Object=MibTableColumn
hmAgentIpStaticMRouteStatus=_HmAgentIpStaticMRouteStatus_Object((1,3,6,1,4,1,248,15,4,8,1,7),_HmAgentIpStaticMRouteStatus_Type())
hmAgentIpStaticMRouteStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hmAgentIpStaticMRouteStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hmPlatform4Multicast':hmPlatform4Multicast,'hmAgentMulticastIGMPConfigGroup':hmAgentMulticastIGMPConfigGroup,'hmAgentMulticastIGMPAdminMode':hmAgentMulticastIGMPAdminMode,'hmAgentMulticastIGMPInterfaceTable':hmAgentMulticastIGMPInterfaceTable,'hmAgentMulticastIGMPInterfaceEntry':hmAgentMulticastIGMPInterfaceEntry,_K:hmAgentMulticastIGMPInterfaceIfIndex,'hmAgentMulticastIGMPInterfaceAdminMode':hmAgentMulticastIGMPInterfaceAdminMode,'hmAgentMulticastIGMPSoftwareDSCP':hmAgentMulticastIGMPSoftwareDSCP,'hmAgentMulticastPIMConfigGroup':hmAgentMulticastPIMConfigGroup,'hmAgentMulticastPIMConfigMode':hmAgentMulticastPIMConfigMode,'hmAgentMulticastPIMPruneHoldtime':hmAgentMulticastPIMPruneHoldtime,'hmAgentMulticastPIMSMConfigGroup':hmAgentMulticastPIMSMConfigGroup,'hmAgentMulticastPIMSMAdminMode':hmAgentMulticastPIMSMAdminMode,'hmAgentMulticastPIMSMDataThresholdRate':hmAgentMulticastPIMSMDataThresholdRate,'hmAgentMulticastPIMSMRegThresholdRate':hmAgentMulticastPIMSMRegThresholdRate,'hmAgentMulticastPIMSMStaticRPTable':hmAgentMulticastPIMSMStaticRPTable,'hmAgentMulticastPIMSMStaticRPEntry':hmAgentMulticastPIMSMStaticRPEntry,_L:hmAgentMulticastPIMSMStaticRPIpAddr,_M:hmAgentMulticastPIMSMStaticRPGroupIpAddr,_N:hmAgentMulticastPIMSMStaticRPGroupIpMask,'hmAgentMulticastPIMSMStaticRPStatus':hmAgentMulticastPIMSMStaticRPStatus,'hmAgentMulticastPIMSMInterfaceTable':hmAgentMulticastPIMSMInterfaceTable,'hmAgentMulticastPIMSMInterfaceEntry':hmAgentMulticastPIMSMInterfaceEntry,_O:hmAgentMulticastPIMSMInterfaceIndex,'hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength':hmAgentMulticastPIMSMInterfaceCBSRHashMaskLength,'hmAgentMulticastPIMSMInterfaceCRPPreference':hmAgentMulticastPIMSMInterfaceCRPPreference,'hmAgentMulticastPIMDMConfigGroup':hmAgentMulticastPIMDMConfigGroup,'hmAgentMulticastPIMDMAdminMode':hmAgentMulticastPIMDMAdminMode,'hmAgentMulticastRoutingConfigGroup':hmAgentMulticastRoutingConfigGroup,'hmAgentMulticastRoutingAdminMode':hmAgentMulticastRoutingAdminMode,'hmAgentMulticastDVMRPConfigGroup':hmAgentMulticastDVMRPConfigGroup,'hmAgentMulticastDVMRPAdminMode':hmAgentMulticastDVMRPAdminMode,'hmAgentSnmpTrapFlagsConfigGroupMulticast':hmAgentSnmpTrapFlagsConfigGroupMulticast,'hmAgentSnmpDVMRPTrapFlag':hmAgentSnmpDVMRPTrapFlag,'hmAgentSnmpPIMTrapFlag':hmAgentSnmpPIMTrapFlag,'hmAgentIpStaticMRouteTable':hmAgentIpStaticMRouteTable,'hmAgentIpStaticMRouteEntry':hmAgentIpStaticMRouteEntry,_P:hmAgentIpStaticMRouteSrcAddressType,_Q:hmAgentIpStaticMRouteSrcIpAddr,_R:hmAgentIpStaticMRouteSrcNetMask,'hmAgentIpStaticMRouteRpfIpAddr':hmAgentIpStaticMRouteRpfIpAddr,'hmAgentIpStaticMRouteIfIndex':hmAgentIpStaticMRouteIfIndex,'hmAgentIpStaticMRoutePreference':hmAgentIpStaticMRoutePreference,'hmAgentIpStaticMRouteStatus':hmAgentIpStaticMRouteStatus})