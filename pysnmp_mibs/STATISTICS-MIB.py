_w='hpGarpStatsPortIndex'
_v='hpSwitchEgressQueueStatsQueueIndex'
_u='hpSwitchEgressQueueStatsPortIndex'
_t='hpSwitchEgressQueueDropStatsQueueIndex'
_s='hpSwitchEgressQueueDropStatsPortIndex'
_r='hpSwitchQueueWatchStatsQueueIndex'
_q='hpSwitchQueueWatchStatsPortIndex'
_p='hpSwitchPortStatIndex'
_o='hpSwitchPhysicalPortIndex'
_n='hpSshStatsSesIndex'
_m='hpGvrpVlanPortIndex'
_l='hpGvrpStatsPortIndex'
_k='hpGvrpStatsVlanIndex'
_j='hpFECStatsPortIndex'
_i='initialized'
_h='failed'
_g='successful'
_f='hpFECStatsTrunkIndex'
_e='hpSwitchFlowControlStatusPortIndex'
_d='disabled'
_c='hpLdbalStatsPortIndex'
_b='hpIgmpStatsPortIndex2'
_a='host-router'
_Z='router'
_Y='hpIgmpStatsPortIndex'
_X='notforwarding'
_W='hpABCStatsPortIndex'
_V='hpABCStatsVlanIndex'
_U='hpSwitchFddiSystemStatIndex'
_T='hpSwitchFddiIpFragStatIndex'
_S='hpSwitchPortFdbAddress'
_R='hpSwitchPortFdbId'
_Q='hpSwitchVlanFdbAddress'
_P='hpSwitchVlanFdbId'
_O='hpSwitchIpStatIndex'
_N='hpSwitchIpxStatIndex'
_M='hpIgmpStatsVlanIndex'
_L='forwarding'
_K='hpIgmpStatsActiveGroupAddr'
_J='enable'
_I='DisplayString'
_H='OctetString'
_G='disable'
_F='deprecated'
_E='obsolete'
_D='STATISTICS-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
HpSwitchPortType,VidList=mibBuilder.importSymbols('HP-ICF-TC','HpSwitchPortType','VidList')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
class MacAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class VlanID(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchStatistics_ObjectIdentity=ObjectIdentity
hpSwitchStatistics=_HpSwitchStatistics_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9))
_HpSwitchIpxStat_ObjectIdentity=ObjectIdentity
hpSwitchIpxStat=_HpSwitchIpxStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,1))
_HpSwitchIpxStatTable_Object=MibTable
hpSwitchIpxStatTable=_HpSwitchIpxStatTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,1,1))
if mibBuilder.loadTexts:hpSwitchIpxStatTable.setStatus(_A)
_HpSwitchIpxStatEntry_Object=MibTableRow
hpSwitchIpxStatEntry=_HpSwitchIpxStatEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,1,1,1))
hpSwitchIpxStatEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:hpSwitchIpxStatEntry.setStatus(_A)
_HpSwitchIpxStatIndex_Type=VlanID
_HpSwitchIpxStatIndex_Object=MibTableColumn
hpSwitchIpxStatIndex=_HpSwitchIpxStatIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,1,1,1,1),_HpSwitchIpxStatIndex_Type())
hpSwitchIpxStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpxStatIndex.setStatus(_A)
_HpSwitchIpxStatNodeAddr_Type=MacAddress
_HpSwitchIpxStatNodeAddr_Object=MibTableColumn
hpSwitchIpxStatNodeAddr=_HpSwitchIpxStatNodeAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,1,1,1,2),_HpSwitchIpxStatNodeAddr_Type())
hpSwitchIpxStatNodeAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpxStatNodeAddr.setStatus(_A)
_HpSwitchIpxStatGatewayAddr_Type=MacAddress
_HpSwitchIpxStatGatewayAddr_Object=MibTableColumn
hpSwitchIpxStatGatewayAddr=_HpSwitchIpxStatGatewayAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,1,1,1,3),_HpSwitchIpxStatGatewayAddr_Type())
hpSwitchIpxStatGatewayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpxStatGatewayAddr.setStatus(_A)
class _HpSwitchIpxStatGatewayEncap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ethernetII',1),('ieee8022',2),('snap',3),('ieee8023Raw',4),('noGateway',5)))
_HpSwitchIpxStatGatewayEncap_Type.__name__=_C
_HpSwitchIpxStatGatewayEncap_Object=MibTableColumn
hpSwitchIpxStatGatewayEncap=_HpSwitchIpxStatGatewayEncap_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,1,1,1,4),_HpSwitchIpxStatGatewayEncap_Type())
hpSwitchIpxStatGatewayEncap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpxStatGatewayEncap.setStatus(_A)
class _HpSwitchIpxStatAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_HpSwitchIpxStatAdminStatus_Type.__name__=_C
_HpSwitchIpxStatAdminStatus_Object=MibTableColumn
hpSwitchIpxStatAdminStatus=_HpSwitchIpxStatAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,1,1,1,5),_HpSwitchIpxStatAdminStatus_Type())
hpSwitchIpxStatAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpxStatAdminStatus.setStatus(_A)
_HpSwitchIpStat_ObjectIdentity=ObjectIdentity
hpSwitchIpStat=_HpSwitchIpStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,2))
class _HpSwitchIpStatTimepAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_HpSwitchIpStatTimepAdminStatus_Type.__name__=_C
_HpSwitchIpStatTimepAdminStatus_Object=MibScalar
hpSwitchIpStatTimepAdminStatus=_HpSwitchIpStatTimepAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,1),_HpSwitchIpStatTimepAdminStatus_Type())
hpSwitchIpStatTimepAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatTimepAdminStatus.setStatus(_E)
_HpSwitchIpStatTimepServerAddr_Type=IpAddress
_HpSwitchIpStatTimepServerAddr_Object=MibScalar
hpSwitchIpStatTimepServerAddr=_HpSwitchIpStatTimepServerAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,2),_HpSwitchIpStatTimepServerAddr_Type())
hpSwitchIpStatTimepServerAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatTimepServerAddr.setStatus(_E)
class _HpSwitchIpStatTimepPollInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchIpStatTimepPollInterval_Type.__name__=_C
_HpSwitchIpStatTimepPollInterval_Object=MibScalar
hpSwitchIpStatTimepPollInterval=_HpSwitchIpStatTimepPollInterval_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,3),_HpSwitchIpStatTimepPollInterval_Type())
hpSwitchIpStatTimepPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatTimepPollInterval.setStatus(_E)
_HpSwitchIpStatTable_Object=MibTable
hpSwitchIpStatTable=_HpSwitchIpStatTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,4))
if mibBuilder.loadTexts:hpSwitchIpStatTable.setStatus(_E)
_HpSwitchIpStatEntry_Object=MibTableRow
hpSwitchIpStatEntry=_HpSwitchIpStatEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,4,1))
hpSwitchIpStatEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:hpSwitchIpStatEntry.setStatus(_E)
_HpSwitchIpStatIndex_Type=VlanID
_HpSwitchIpStatIndex_Object=MibTableColumn
hpSwitchIpStatIndex=_HpSwitchIpStatIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,4,1,1),_HpSwitchIpStatIndex_Type())
hpSwitchIpStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatIndex.setStatus(_E)
_HpSwitchIpStatAddr_Type=IpAddress
_HpSwitchIpStatAddr_Object=MibTableColumn
hpSwitchIpStatAddr=_HpSwitchIpStatAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,4,1,2),_HpSwitchIpStatAddr_Type())
hpSwitchIpStatAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatAddr.setStatus(_E)
_HpSwitchIpStatMask_Type=IpAddress
_HpSwitchIpStatMask_Object=MibTableColumn
hpSwitchIpStatMask=_HpSwitchIpStatMask_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,4,1,3),_HpSwitchIpStatMask_Type())
hpSwitchIpStatMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatMask.setStatus(_E)
_HpSwitchIpStatGatewayAddr_Type=IpAddress
_HpSwitchIpStatGatewayAddr_Object=MibTableColumn
hpSwitchIpStatGatewayAddr=_HpSwitchIpStatGatewayAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,4,1,4),_HpSwitchIpStatGatewayAddr_Type())
hpSwitchIpStatGatewayAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatGatewayAddr.setStatus(_E)
class _HpSwitchIpStatAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_G,2),('bootp',3)))
_HpSwitchIpStatAdminStatus_Type.__name__=_C
_HpSwitchIpStatAdminStatus_Object=MibTableColumn
hpSwitchIpStatAdminStatus=_HpSwitchIpStatAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,2,4,1,5),_HpSwitchIpStatAdminStatus_Type())
hpSwitchIpStatAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchIpStatAdminStatus.setStatus(_E)
_HpSwitchFdbInfo_ObjectIdentity=ObjectIdentity
hpSwitchFdbInfo=_HpSwitchFdbInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,4))
_HpSwitchVlanFdbAddrTable_Object=MibTable
hpSwitchVlanFdbAddrTable=_HpSwitchVlanFdbAddrTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,1))
if mibBuilder.loadTexts:hpSwitchVlanFdbAddrTable.setStatus(_A)
_HpSwitchVlanFdbAddrEntry_Object=MibTableRow
hpSwitchVlanFdbAddrEntry=_HpSwitchVlanFdbAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,1,1))
hpSwitchVlanFdbAddrEntry.setIndexNames((0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:hpSwitchVlanFdbAddrEntry.setStatus(_A)
_HpSwitchVlanFdbId_Type=VlanID
_HpSwitchVlanFdbId_Object=MibTableColumn
hpSwitchVlanFdbId=_HpSwitchVlanFdbId_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,1,1,1),_HpSwitchVlanFdbId_Type())
hpSwitchVlanFdbId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchVlanFdbId.setStatus(_A)
_HpSwitchVlanFdbAddress_Type=MacAddress
_HpSwitchVlanFdbAddress_Object=MibTableColumn
hpSwitchVlanFdbAddress=_HpSwitchVlanFdbAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,1,1,2),_HpSwitchVlanFdbAddress_Type())
hpSwitchVlanFdbAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchVlanFdbAddress.setStatus(_A)
_HpSwitchVlanFdbPort_Type=Integer32
_HpSwitchVlanFdbPort_Object=MibTableColumn
hpSwitchVlanFdbPort=_HpSwitchVlanFdbPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,1,1,3),_HpSwitchVlanFdbPort_Type())
hpSwitchVlanFdbPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchVlanFdbPort.setStatus(_A)
_HpSwitchPortFdbAddrTable_Object=MibTable
hpSwitchPortFdbAddrTable=_HpSwitchPortFdbAddrTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,2))
if mibBuilder.loadTexts:hpSwitchPortFdbAddrTable.setStatus(_A)
_HpSwitchPortFdbAddrEntry_Object=MibTableRow
hpSwitchPortFdbAddrEntry=_HpSwitchPortFdbAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,2,1))
hpSwitchPortFdbAddrEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:hpSwitchPortFdbAddrEntry.setStatus(_A)
_HpSwitchPortFdbId_Type=Integer32
_HpSwitchPortFdbId_Object=MibTableColumn
hpSwitchPortFdbId=_HpSwitchPortFdbId_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,2,1,1),_HpSwitchPortFdbId_Type())
hpSwitchPortFdbId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortFdbId.setStatus(_A)
_HpSwitchPortFdbAddress_Type=MacAddress
_HpSwitchPortFdbAddress_Object=MibTableColumn
hpSwitchPortFdbAddress=_HpSwitchPortFdbAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,2,1,2),_HpSwitchPortFdbAddress_Type())
hpSwitchPortFdbAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortFdbAddress.setStatus(_A)
_HpSwitchPortFdbVlanId_Type=VlanID
_HpSwitchPortFdbVlanId_Object=MibTableColumn
hpSwitchPortFdbVlanId=_HpSwitchPortFdbVlanId_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,2,1,3),_HpSwitchPortFdbVlanId_Type())
hpSwitchPortFdbVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortFdbVlanId.setStatus(_F)
_HpSwitchPortFdbVidList_Type=VidList
_HpSwitchPortFdbVidList_Object=MibTableColumn
hpSwitchPortFdbVidList=_HpSwitchPortFdbVidList_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,4,2,1,4),_HpSwitchPortFdbVidList_Type())
hpSwitchPortFdbVidList.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortFdbVidList.setStatus(_A)
_HpSwitchStpStat_ObjectIdentity=ObjectIdentity
hpSwitchStpStat=_HpSwitchStpStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,5))
class _HpSwitchStpStatAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_HpSwitchStpStatAdminStatus_Type.__name__=_C
_HpSwitchStpStatAdminStatus_Object=MibScalar
hpSwitchStpStatAdminStatus=_HpSwitchStpStatAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,5,1),_HpSwitchStpStatAdminStatus_Type())
hpSwitchStpStatAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchStpStatAdminStatus.setStatus(_A)
_HpSwitchMiscStat_ObjectIdentity=ObjectIdentity
hpSwitchMiscStat=_HpSwitchMiscStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,6))
class _HpSwitchCpuStat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchCpuStat_Type.__name__=_C
_HpSwitchCpuStat_Object=MibScalar
hpSwitchCpuStat=_HpSwitchCpuStat_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,6,1),_HpSwitchCpuStat_Type())
hpSwitchCpuStat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchCpuStat.setStatus(_A)
_HpSwitchFddiIpFragStat_ObjectIdentity=ObjectIdentity
hpSwitchFddiIpFragStat=_HpSwitchFddiIpFragStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,7))
_HpSwitchFddiIpFragStatTable_Object=MibTable
hpSwitchFddiIpFragStatTable=_HpSwitchFddiIpFragStatTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,7,1))
if mibBuilder.loadTexts:hpSwitchFddiIpFragStatTable.setStatus(_A)
_HpSwitchFddiIpFragStatEntry_Object=MibTableRow
hpSwitchFddiIpFragStatEntry=_HpSwitchFddiIpFragStatEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,7,1,1))
hpSwitchFddiIpFragStatEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:hpSwitchFddiIpFragStatEntry.setStatus(_A)
class _HpSwitchFddiIpFragStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchFddiIpFragStatIndex_Type.__name__=_C
_HpSwitchFddiIpFragStatIndex_Object=MibTableColumn
hpSwitchFddiIpFragStatIndex=_HpSwitchFddiIpFragStatIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,7,1,1,1),_HpSwitchFddiIpFragStatIndex_Type())
hpSwitchFddiIpFragStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiIpFragStatIndex.setStatus(_A)
_HpSwitchFddiIpFragFramesFragmented_Type=Counter32
_HpSwitchFddiIpFragFramesFragmented_Object=MibTableColumn
hpSwitchFddiIpFragFramesFragmented=_HpSwitchFddiIpFragFramesFragmented_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,7,1,1,2),_HpSwitchFddiIpFragFramesFragmented_Type())
hpSwitchFddiIpFragFramesFragmented.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiIpFragFramesFragmented.setStatus(_A)
_HpSwitchFddiIpFragFramesCreated_Type=Counter32
_HpSwitchFddiIpFragFramesCreated_Object=MibTableColumn
hpSwitchFddiIpFragFramesCreated=_HpSwitchFddiIpFragFramesCreated_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,7,1,1,3),_HpSwitchFddiIpFragFramesCreated_Type())
hpSwitchFddiIpFragFramesCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiIpFragFramesCreated.setStatus(_A)
_HpSwitchFddiIpFragFrameErrors_Type=Counter32
_HpSwitchFddiIpFragFrameErrors_Object=MibTableColumn
hpSwitchFddiIpFragFrameErrors=_HpSwitchFddiIpFragFrameErrors_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,7,1,1,4),_HpSwitchFddiIpFragFrameErrors_Type())
hpSwitchFddiIpFragFrameErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiIpFragFrameErrors.setStatus(_A)
_HpSwitchFddiSystemStat_ObjectIdentity=ObjectIdentity
hpSwitchFddiSystemStat=_HpSwitchFddiSystemStat_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,8))
_HpSwitchFddiSystemStatTable_Object=MibTable
hpSwitchFddiSystemStatTable=_HpSwitchFddiSystemStatTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1))
if mibBuilder.loadTexts:hpSwitchFddiSystemStatTable.setStatus(_A)
_HpSwitchFddiSystemStatEntry_Object=MibTableRow
hpSwitchFddiSystemStatEntry=_HpSwitchFddiSystemStatEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1))
hpSwitchFddiSystemStatEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:hpSwitchFddiSystemStatEntry.setStatus(_A)
class _HpSwitchFddiSystemStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchFddiSystemStatIndex_Type.__name__=_C
_HpSwitchFddiSystemStatIndex_Object=MibTableColumn
hpSwitchFddiSystemStatIndex=_HpSwitchFddiSystemStatIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,1),_HpSwitchFddiSystemStatIndex_Type())
hpSwitchFddiSystemStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemStatIndex.setStatus(_A)
class _HpSwitchFddiSystemOsVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpSwitchFddiSystemOsVersion_Type.__name__=_I
_HpSwitchFddiSystemOsVersion_Object=MibTableColumn
hpSwitchFddiSystemOsVersion=_HpSwitchFddiSystemOsVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,2),_HpSwitchFddiSystemOsVersion_Type())
hpSwitchFddiSystemOsVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemOsVersion.setStatus(_A)
class _HpSwitchFddiSystemRomVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_HpSwitchFddiSystemRomVersion_Type.__name__=_I
_HpSwitchFddiSystemRomVersion_Object=MibTableColumn
hpSwitchFddiSystemRomVersion=_HpSwitchFddiSystemRomVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,3),_HpSwitchFddiSystemRomVersion_Type())
hpSwitchFddiSystemRomVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemRomVersion.setStatus(_A)
_HpSwitchFddiSystemMemoryTotal_Type=Integer32
_HpSwitchFddiSystemMemoryTotal_Object=MibTableColumn
hpSwitchFddiSystemMemoryTotal=_HpSwitchFddiSystemMemoryTotal_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,4),_HpSwitchFddiSystemMemoryTotal_Type())
hpSwitchFddiSystemMemoryTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemMemoryTotal.setStatus(_A)
_HpSwitchFddiSystemMemoryFree_Type=Integer32
_HpSwitchFddiSystemMemoryFree_Object=MibTableColumn
hpSwitchFddiSystemMemoryFree=_HpSwitchFddiSystemMemoryFree_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,5),_HpSwitchFddiSystemMemoryFree_Type())
hpSwitchFddiSystemMemoryFree.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemMemoryFree.setStatus(_A)
class _HpSwitchFddiSystemCpuUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchFddiSystemCpuUtil_Type.__name__=_C
_HpSwitchFddiSystemCpuUtil_Object=MibTableColumn
hpSwitchFddiSystemCpuUtil=_HpSwitchFddiSystemCpuUtil_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,6),_HpSwitchFddiSystemCpuUtil_Type())
hpSwitchFddiSystemCpuUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemCpuUtil.setStatus(_A)
class _HpSwitchFddiSystemBuildDirectory_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(80,80));fixedLength=80
_HpSwitchFddiSystemBuildDirectory_Type.__name__=_H
_HpSwitchFddiSystemBuildDirectory_Object=MibTableColumn
hpSwitchFddiSystemBuildDirectory=_HpSwitchFddiSystemBuildDirectory_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,7),_HpSwitchFddiSystemBuildDirectory_Type())
hpSwitchFddiSystemBuildDirectory.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemBuildDirectory.setStatus(_A)
class _HpSwitchFddiSystemBuildDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(40,40));fixedLength=40
_HpSwitchFddiSystemBuildDate_Type.__name__=_H
_HpSwitchFddiSystemBuildDate_Object=MibTableColumn
hpSwitchFddiSystemBuildDate=_HpSwitchFddiSystemBuildDate_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,8),_HpSwitchFddiSystemBuildDate_Type())
hpSwitchFddiSystemBuildDate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemBuildDate.setStatus(_A)
class _HpSwitchFddiSystemBuildNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_HpSwitchFddiSystemBuildNumber_Type.__name__=_H
_HpSwitchFddiSystemBuildNumber_Object=MibTableColumn
hpSwitchFddiSystemBuildNumber=_HpSwitchFddiSystemBuildNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,8,1,1,9),_HpSwitchFddiSystemBuildNumber_Type())
hpSwitchFddiSystemBuildNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFddiSystemBuildNumber.setStatus(_A)
_HpABCStats_ObjectIdentity=ObjectIdentity
hpABCStats=_HpABCStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,9))
_HpABCStatsTable_Object=MibTable
hpABCStatsTable=_HpABCStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1))
if mibBuilder.loadTexts:hpABCStatsTable.setStatus(_A)
_HpABCStatsEntry_Object=MibTableRow
hpABCStatsEntry=_HpABCStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1))
hpABCStatsEntry.setIndexNames((0,_D,_V),(0,_D,_W))
if mibBuilder.loadTexts:hpABCStatsEntry.setStatus(_A)
_HpABCStatsVlanIndex_Type=VlanID
_HpABCStatsVlanIndex_Object=MibTableColumn
hpABCStatsVlanIndex=_HpABCStatsVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1,1),_HpABCStatsVlanIndex_Type())
hpABCStatsVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpABCStatsVlanIndex.setStatus(_A)
class _HpABCStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpABCStatsPortIndex_Type.__name__=_C
_HpABCStatsPortIndex_Object=MibTableColumn
hpABCStatsPortIndex=_HpABCStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1,2),_HpABCStatsPortIndex_Type())
hpABCStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpABCStatsPortIndex.setStatus(_A)
_HpABCStatsPortType_Type=HpSwitchPortType
_HpABCStatsPortType_Object=MibTableColumn
hpABCStatsPortType=_HpABCStatsPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1,3),_HpABCStatsPortType_Type())
hpABCStatsPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpABCStatsPortType.setStatus(_A)
_HpABCStatsArpReplies_Type=Counter32
_HpABCStatsArpReplies_Object=MibTableColumn
hpABCStatsArpReplies=_HpABCStatsArpReplies_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1,4),_HpABCStatsArpReplies_Type())
hpABCStatsArpReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:hpABCStatsArpReplies.setStatus(_A)
_HpABCStatsIpxReplies_Type=Counter32
_HpABCStatsIpxReplies_Object=MibTableColumn
hpABCStatsIpxReplies=_HpABCStatsIpxReplies_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1,5),_HpABCStatsIpxReplies_Type())
hpABCStatsIpxReplies.setMaxAccess(_B)
if mibBuilder.loadTexts:hpABCStatsIpxReplies.setStatus(_A)
class _HpABCStatsIpRipControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_X,2)))
_HpABCStatsIpRipControl_Type.__name__=_C
_HpABCStatsIpRipControl_Object=MibTableColumn
hpABCStatsIpRipControl=_HpABCStatsIpRipControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1,6),_HpABCStatsIpRipControl_Type())
hpABCStatsIpRipControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpABCStatsIpRipControl.setStatus(_A)
class _HpABCStatsIpxRipSapControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_X,2)))
_HpABCStatsIpxRipSapControl_Type.__name__=_C
_HpABCStatsIpxRipSapControl_Object=MibTableColumn
hpABCStatsIpxRipSapControl=_HpABCStatsIpxRipSapControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,9,1,1,7),_HpABCStatsIpxRipSapControl_Type())
hpABCStatsIpxRipSapControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpABCStatsIpxRipSapControl.setStatus(_A)
_HpIgmpStats_ObjectIdentity=ObjectIdentity
hpIgmpStats=_HpIgmpStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,10))
_HpIgmpStatsTable_Object=MibTable
hpIgmpStatsTable=_HpIgmpStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,1))
if mibBuilder.loadTexts:hpIgmpStatsTable.setStatus(_A)
_HpIgmpStatsEntry_Object=MibTableRow
hpIgmpStatsEntry=_HpIgmpStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,1,1))
hpIgmpStatsEntry.setIndexNames((0,_D,_M),(0,_D,_K))
if mibBuilder.loadTexts:hpIgmpStatsEntry.setStatus(_A)
_HpIgmpStatsVlanIndex_Type=VlanID
_HpIgmpStatsVlanIndex_Object=MibTableColumn
hpIgmpStatsVlanIndex=_HpIgmpStatsVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,1,1,1),_HpIgmpStatsVlanIndex_Type())
hpIgmpStatsVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsVlanIndex.setStatus(_A)
_HpIgmpStatsActiveGroupAddr_Type=IpAddress
_HpIgmpStatsActiveGroupAddr_Object=MibTableColumn
hpIgmpStatsActiveGroupAddr=_HpIgmpStatsActiveGroupAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,1,1,2),_HpIgmpStatsActiveGroupAddr_Type())
hpIgmpStatsActiveGroupAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsActiveGroupAddr.setStatus(_A)
_HpIgmpStatsReports_Type=Counter32
_HpIgmpStatsReports_Object=MibTableColumn
hpIgmpStatsReports=_HpIgmpStatsReports_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,1,1,3),_HpIgmpStatsReports_Type())
hpIgmpStatsReports.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsReports.setStatus(_A)
_HpIgmpStatsQueries_Type=Counter32
_HpIgmpStatsQueries_Object=MibTableColumn
hpIgmpStatsQueries=_HpIgmpStatsQueries_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,1,1,4),_HpIgmpStatsQueries_Type())
hpIgmpStatsQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsQueries.setStatus(_A)
_HpIgmpStatsQuerierAccessPort_Type=Integer32
_HpIgmpStatsQuerierAccessPort_Object=MibTableColumn
hpIgmpStatsQuerierAccessPort=_HpIgmpStatsQuerierAccessPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,1,1,5),_HpIgmpStatsQuerierAccessPort_Type())
hpIgmpStatsQuerierAccessPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsQuerierAccessPort.setStatus(_A)
_HpIgmpStatsPortTable_Object=MibTable
hpIgmpStatsPortTable=_HpIgmpStatsPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,2))
if mibBuilder.loadTexts:hpIgmpStatsPortTable.setStatus(_F)
_HpIgmpStatsPortEntry_Object=MibTableRow
hpIgmpStatsPortEntry=_HpIgmpStatsPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,2,1))
hpIgmpStatsPortEntry.setIndexNames((0,_D,_K),(0,_D,_Y))
if mibBuilder.loadTexts:hpIgmpStatsPortEntry.setStatus(_F)
class _HpIgmpStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpIgmpStatsPortIndex_Type.__name__=_C
_HpIgmpStatsPortIndex_Object=MibTableColumn
hpIgmpStatsPortIndex=_HpIgmpStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,2,1,1),_HpIgmpStatsPortIndex_Type())
hpIgmpStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortIndex.setStatus(_F)
_HpIgmpStatsPortType_Type=HpSwitchPortType
_HpIgmpStatsPortType_Object=MibTableColumn
hpIgmpStatsPortType=_HpIgmpStatsPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,2,1,2),_HpIgmpStatsPortType_Type())
hpIgmpStatsPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortType.setStatus(_F)
class _HpIgmpStatsPortAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('host',1),(_Z,2),(_a,3)))
_HpIgmpStatsPortAccess_Type.__name__=_C
_HpIgmpStatsPortAccess_Object=MibTableColumn
hpIgmpStatsPortAccess=_HpIgmpStatsPortAccess_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,2,1,3),_HpIgmpStatsPortAccess_Type())
hpIgmpStatsPortAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortAccess.setStatus(_F)
_HpIgmpStatsPortTable2_Object=MibTable
hpIgmpStatsPortTable2=_HpIgmpStatsPortTable2_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,3))
if mibBuilder.loadTexts:hpIgmpStatsPortTable2.setStatus(_A)
_HpIgmpStatsPortEntry2_Object=MibTableRow
hpIgmpStatsPortEntry2=_HpIgmpStatsPortEntry2_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,3,1))
hpIgmpStatsPortEntry2.setIndexNames((0,_D,_M),(0,_D,_K),(0,_D,_b))
if mibBuilder.loadTexts:hpIgmpStatsPortEntry2.setStatus(_A)
class _HpIgmpStatsPortIndex2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpIgmpStatsPortIndex2_Type.__name__=_C
_HpIgmpStatsPortIndex2_Object=MibTableColumn
hpIgmpStatsPortIndex2=_HpIgmpStatsPortIndex2_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,3,1,1),_HpIgmpStatsPortIndex2_Type())
hpIgmpStatsPortIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortIndex2.setStatus(_A)
_HpIgmpStatsPortType2_Type=HpSwitchPortType
_HpIgmpStatsPortType2_Object=MibTableColumn
hpIgmpStatsPortType2=_HpIgmpStatsPortType2_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,3,1,2),_HpIgmpStatsPortType2_Type())
hpIgmpStatsPortType2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortType2.setStatus(_A)
class _HpIgmpStatsPortAccess2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('host',1),(_Z,2),(_a,3)))
_HpIgmpStatsPortAccess2_Type.__name__=_C
_HpIgmpStatsPortAccess2_Object=MibTableColumn
hpIgmpStatsPortAccess2=_HpIgmpStatsPortAccess2_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,3,1,3),_HpIgmpStatsPortAccess2_Type())
hpIgmpStatsPortAccess2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortAccess2.setStatus(_A)
_HpIgmpStatsPortAgeTimer2_Type=Integer32
_HpIgmpStatsPortAgeTimer2_Object=MibTableColumn
hpIgmpStatsPortAgeTimer2=_HpIgmpStatsPortAgeTimer2_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,3,1,4),_HpIgmpStatsPortAgeTimer2_Type())
hpIgmpStatsPortAgeTimer2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortAgeTimer2.setStatus(_A)
_HpIgmpStatsPortLeaveTimer2_Type=Integer32
_HpIgmpStatsPortLeaveTimer2_Object=MibTableColumn
hpIgmpStatsPortLeaveTimer2=_HpIgmpStatsPortLeaveTimer2_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,10,3,1,5),_HpIgmpStatsPortLeaveTimer2_Type())
hpIgmpStatsPortLeaveTimer2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpIgmpStatsPortLeaveTimer2.setStatus(_A)
_HpLdbalStats_ObjectIdentity=ObjectIdentity
hpLdbalStats=_HpLdbalStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,11))
_HpLdbalStatsPortTable_Object=MibTable
hpLdbalStatsPortTable=_HpLdbalStatsPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1))
if mibBuilder.loadTexts:hpLdbalStatsPortTable.setStatus(_A)
_HpLdbalStatsPortEntry_Object=MibTableRow
hpLdbalStatsPortEntry=_HpLdbalStatsPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1,1))
hpLdbalStatsPortEntry.setIndexNames((0,_D,_c))
if mibBuilder.loadTexts:hpLdbalStatsPortEntry.setStatus(_A)
class _HpLdbalStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpLdbalStatsPortIndex_Type.__name__=_C
_HpLdbalStatsPortIndex_Object=MibTableColumn
hpLdbalStatsPortIndex=_HpLdbalStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1,1,1),_HpLdbalStatsPortIndex_Type())
hpLdbalStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLdbalStatsPortIndex.setStatus(_A)
class _HpLdbalStatsPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_d,1),('error',2),('initial',3),('notEstablished',4),('established',5),('topologyError',6)))
_HpLdbalStatsPortState_Type.__name__=_C
_HpLdbalStatsPortState_Object=MibTableColumn
hpLdbalStatsPortState=_HpLdbalStatsPortState_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1,1,2),_HpLdbalStatsPortState_Type())
hpLdbalStatsPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLdbalStatsPortState.setStatus(_A)
_HpLdbalStatsAdjacentSwitch_Type=MacAddress
_HpLdbalStatsAdjacentSwitch_Object=MibTableColumn
hpLdbalStatsAdjacentSwitch=_HpLdbalStatsAdjacentSwitch_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1,1,3),_HpLdbalStatsAdjacentSwitch_Type())
hpLdbalStatsAdjacentSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLdbalStatsAdjacentSwitch.setStatus(_A)
_HpLdbalStatsPeerPort_Type=MacAddress
_HpLdbalStatsPeerPort_Object=MibTableColumn
hpLdbalStatsPeerPort=_HpLdbalStatsPeerPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1,1,4),_HpLdbalStatsPeerPort_Type())
hpLdbalStatsPeerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLdbalStatsPeerPort.setStatus(_A)
_HpLdbalStatsAdjacentHost_Type=DisplayString
_HpLdbalStatsAdjacentHost_Object=MibTableColumn
hpLdbalStatsAdjacentHost=_HpLdbalStatsAdjacentHost_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1,1,5),_HpLdbalStatsAdjacentHost_Type())
hpLdbalStatsAdjacentHost.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLdbalStatsAdjacentHost.setStatus(_A)
class _HpLdbalStatsMeshWarningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_d,2)))
_HpLdbalStatsMeshWarningStatus_Type.__name__=_C
_HpLdbalStatsMeshWarningStatus_Object=MibTableColumn
hpLdbalStatsMeshWarningStatus=_HpLdbalStatsMeshWarningStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,11,1,1,6),_HpLdbalStatsMeshWarningStatus_Type())
hpLdbalStatsMeshWarningStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpLdbalStatsMeshWarningStatus.setStatus(_A)
_HpSwitchMacStats_ObjectIdentity=ObjectIdentity
hpSwitchMacStats=_HpSwitchMacStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,12))
class _HpSwitchFdbAddressCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_HpSwitchFdbAddressCount_Type.__name__=_C
_HpSwitchFdbAddressCount_Object=MibScalar
hpSwitchFdbAddressCount=_HpSwitchFdbAddressCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,12,1),_HpSwitchFdbAddressCount_Type())
hpSwitchFdbAddressCount.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFdbAddressCount.setStatus(_A)
_HpSwitchFlowControlStatus_ObjectIdentity=ObjectIdentity
hpSwitchFlowControlStatus=_HpSwitchFlowControlStatus_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,13))
_HpSwitchFlowControlStatusTable_Object=MibTable
hpSwitchFlowControlStatusTable=_HpSwitchFlowControlStatusTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,13,1))
if mibBuilder.loadTexts:hpSwitchFlowControlStatusTable.setStatus(_A)
_HpSwitchFlowControlStatusEntry_Object=MibTableRow
hpSwitchFlowControlStatusEntry=_HpSwitchFlowControlStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,13,1,1))
hpSwitchFlowControlStatusEntry.setIndexNames((0,_D,_e))
if mibBuilder.loadTexts:hpSwitchFlowControlStatusEntry.setStatus(_A)
class _HpSwitchFlowControlStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchFlowControlStatusPortIndex_Type.__name__=_C
_HpSwitchFlowControlStatusPortIndex_Object=MibTableColumn
hpSwitchFlowControlStatusPortIndex=_HpSwitchFlowControlStatusPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,13,1,1,1),_HpSwitchFlowControlStatusPortIndex_Type())
hpSwitchFlowControlStatusPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFlowControlStatusPortIndex.setStatus(_A)
class _HpSwitchFlowControlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('on',2),('on-rx',3),('on-tx',4)))
_HpSwitchFlowControlState_Type.__name__=_C
_HpSwitchFlowControlState_Object=MibTableColumn
hpSwitchFlowControlState=_HpSwitchFlowControlState_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,13,1,1,2),_HpSwitchFlowControlState_Type())
hpSwitchFlowControlState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchFlowControlState.setStatus(_A)
_HpFECStatsTrunk_ObjectIdentity=ObjectIdentity
hpFECStatsTrunk=_HpFECStatsTrunk_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,14))
_HpFECStatsTrunkTable_Object=MibTable
hpFECStatsTrunkTable=_HpFECStatsTrunkTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,14,1))
if mibBuilder.loadTexts:hpFECStatsTrunkTable.setStatus(_A)
_HpFECStatsTrunkEntry_Object=MibTableRow
hpFECStatsTrunkEntry=_HpFECStatsTrunkEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,14,1,1))
hpFECStatsTrunkEntry.setIndexNames((0,_D,_f))
if mibBuilder.loadTexts:hpFECStatsTrunkEntry.setStatus(_A)
class _HpFECStatsTrunkIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpFECStatsTrunkIndex_Type.__name__=_C
_HpFECStatsTrunkIndex_Object=MibTableColumn
hpFECStatsTrunkIndex=_HpFECStatsTrunkIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,14,1,1,1),_HpFECStatsTrunkIndex_Type())
hpFECStatsTrunkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsTrunkIndex.setStatus(_A)
_HpFECStatsTrunkName_Type=DisplayString
_HpFECStatsTrunkName_Object=MibTableColumn
hpFECStatsTrunkName=_HpFECStatsTrunkName_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,14,1,1,2),_HpFECStatsTrunkName_Type())
hpFECStatsTrunkName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsTrunkName.setStatus(_A)
class _HpFECStatsTrunkNegotiationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3)))
_HpFECStatsTrunkNegotiationStatus_Type.__name__=_C
_HpFECStatsTrunkNegotiationStatus_Object=MibTableColumn
hpFECStatsTrunkNegotiationStatus=_HpFECStatsTrunkNegotiationStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,14,1,1,3),_HpFECStatsTrunkNegotiationStatus_Type())
hpFECStatsTrunkNegotiationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsTrunkNegotiationStatus.setStatus(_A)
class _HpFECStatsTrunkForwardingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sa-only',1),('sa-da',2),('none',3)))
_HpFECStatsTrunkForwardingMode_Type.__name__=_C
_HpFECStatsTrunkForwardingMode_Object=MibTableColumn
hpFECStatsTrunkForwardingMode=_HpFECStatsTrunkForwardingMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,14,1,1,4),_HpFECStatsTrunkForwardingMode_Type())
hpFECStatsTrunkForwardingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsTrunkForwardingMode.setStatus(_A)
_HpFECStatsTrunkFlushPktsEchoed_Type=Counter32
_HpFECStatsTrunkFlushPktsEchoed_Object=MibTableColumn
hpFECStatsTrunkFlushPktsEchoed=_HpFECStatsTrunkFlushPktsEchoed_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,14,1,1,5),_HpFECStatsTrunkFlushPktsEchoed_Type())
hpFECStatsTrunkFlushPktsEchoed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsTrunkFlushPktsEchoed.setStatus(_A)
_HpFECStatsPort_ObjectIdentity=ObjectIdentity
hpFECStatsPort=_HpFECStatsPort_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,15))
_HpFECStatsPortTable_Object=MibTable
hpFECStatsPortTable=_HpFECStatsPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1))
if mibBuilder.loadTexts:hpFECStatsPortTable.setStatus(_A)
_HpFECStatsPortEntry_Object=MibTableRow
hpFECStatsPortEntry=_HpFECStatsPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1))
hpFECStatsPortEntry.setIndexNames((0,_D,_j))
if mibBuilder.loadTexts:hpFECStatsPortEntry.setStatus(_A)
class _HpFECStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpFECStatsPortIndex_Type.__name__=_C
_HpFECStatsPortIndex_Object=MibTableColumn
hpFECStatsPortIndex=_HpFECStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,1),_HpFECStatsPortIndex_Type())
hpFECStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortIndex.setStatus(_A)
class _HpFECStatsPortTrunkNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpFECStatsPortTrunkNumber_Type.__name__=_C
_HpFECStatsPortTrunkNumber_Object=MibTableColumn
hpFECStatsPortTrunkNumber=_HpFECStatsPortTrunkNumber_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,2),_HpFECStatsPortTrunkNumber_Type())
hpFECStatsPortTrunkNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortTrunkNumber.setStatus(_A)
_HpFECStatsPortTrunkName_Type=DisplayString
_HpFECStatsPortTrunkName_Object=MibTableColumn
hpFECStatsPortTrunkName=_HpFECStatsPortTrunkName_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,3),_HpFECStatsPortTrunkName_Type())
hpFECStatsPortTrunkName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortTrunkName.setStatus(_A)
class _HpFECStatsPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),(_L,2),('blocking',3),('up',4)))
_HpFECStatsPortMode_Type.__name__=_C
_HpFECStatsPortMode_Object=MibTableColumn
hpFECStatsPortMode=_HpFECStatsPortMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,4),_HpFECStatsPortMode_Type())
hpFECStatsPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortMode.setStatus(_A)
class _HpFECStatsPortNegotiationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_g,1),(_h,2),(_i,3)))
_HpFECStatsPortNegotiationStatus_Type.__name__=_C
_HpFECStatsPortNegotiationStatus_Object=MibTableColumn
hpFECStatsPortNegotiationStatus=_HpFECStatsPortNegotiationStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,5),_HpFECStatsPortNegotiationStatus_Type())
hpFECStatsPortNegotiationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortNegotiationStatus.setStatus(_A)
_HpFECStatsPortHellosSent_Type=Counter32
_HpFECStatsPortHellosSent_Object=MibTableColumn
hpFECStatsPortHellosSent=_HpFECStatsPortHellosSent_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,6),_HpFECStatsPortHellosSent_Type())
hpFECStatsPortHellosSent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortHellosSent.setStatus(_A)
_HpFECStatsPortHellosReceived_Type=Counter32
_HpFECStatsPortHellosReceived_Object=MibTableColumn
hpFECStatsPortHellosReceived=_HpFECStatsPortHellosReceived_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,7),_HpFECStatsPortHellosReceived_Type())
hpFECStatsPortHellosReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortHellosReceived.setStatus(_A)
class _HpFECStatsPortMySlowHello_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fast',1),('slow',2)))
_HpFECStatsPortMySlowHello_Type.__name__=_C
_HpFECStatsPortMySlowHello_Object=MibTableColumn
hpFECStatsPortMySlowHello=_HpFECStatsPortMySlowHello_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,8),_HpFECStatsPortMySlowHello_Type())
hpFECStatsPortMySlowHello.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortMySlowHello.setStatus(_A)
class _HpFECStatsPortMyAutoMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('desirable',1),('auto',2)))
_HpFECStatsPortMyAutoMode_Type.__name__=_C
_HpFECStatsPortMyAutoMode_Object=MibTableColumn
hpFECStatsPortMyAutoMode=_HpFECStatsPortMyAutoMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,9),_HpFECStatsPortMyAutoMode_Type())
hpFECStatsPortMyAutoMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortMyAutoMode.setStatus(_A)
_HpFECStatsPortPartner_Type=MacAddress
_HpFECStatsPortPartner_Object=MibTableColumn
hpFECStatsPortPartner=_HpFECStatsPortPartner_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,10),_HpFECStatsPortPartner_Type())
hpFECStatsPortPartner.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortPartner.setStatus(_A)
_HpFECStatsPortFlushPktsEchoed_Type=Counter32
_HpFECStatsPortFlushPktsEchoed_Object=MibTableColumn
hpFECStatsPortFlushPktsEchoed=_HpFECStatsPortFlushPktsEchoed_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,15,1,1,11),_HpFECStatsPortFlushPktsEchoed_Type())
hpFECStatsPortFlushPktsEchoed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpFECStatsPortFlushPktsEchoed.setStatus(_A)
_HpGvrpStats_ObjectIdentity=ObjectIdentity
hpGvrpStats=_HpGvrpStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,16))
_HpGvrpStatsTable_Object=MibTable
hpGvrpStatsTable=_HpGvrpStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,1))
if mibBuilder.loadTexts:hpGvrpStatsTable.setStatus(_A)
_HpGvrpStatsEntry_Object=MibTableRow
hpGvrpStatsEntry=_HpGvrpStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,1,1))
hpGvrpStatsEntry.setIndexNames((0,_D,_k),(0,_D,_l))
if mibBuilder.loadTexts:hpGvrpStatsEntry.setStatus(_A)
_HpGvrpStatsVlanIndex_Type=VlanID
_HpGvrpStatsVlanIndex_Object=MibTableColumn
hpGvrpStatsVlanIndex=_HpGvrpStatsVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,1,1,1),_HpGvrpStatsVlanIndex_Type())
hpGvrpStatsVlanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpStatsVlanIndex.setStatus(_A)
class _HpGvrpStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpGvrpStatsPortIndex_Type.__name__=_C
_HpGvrpStatsPortIndex_Object=MibTableColumn
hpGvrpStatsPortIndex=_HpGvrpStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,1,1,2),_HpGvrpStatsPortIndex_Type())
hpGvrpStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpStatsPortIndex.setStatus(_A)
class _HpGvrpStatsPortVlanMember_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pending',1),('yes',2),('no',3)))
_HpGvrpStatsPortVlanMember_Type.__name__=_C
_HpGvrpStatsPortVlanMember_Object=MibTableColumn
hpGvrpStatsPortVlanMember=_HpGvrpStatsPortVlanMember_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,1,1,3),_HpGvrpStatsPortVlanMember_Type())
hpGvrpStatsPortVlanMember.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpStatsPortVlanMember.setStatus(_A)
class _HpGvrpPortIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HpGvrpPortIfOperStatus_Type.__name__=_C
_HpGvrpPortIfOperStatus_Object=MibTableColumn
hpGvrpPortIfOperStatus=_HpGvrpPortIfOperStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,1,1,4),_HpGvrpPortIfOperStatus_Type())
hpGvrpPortIfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpPortIfOperStatus.setStatus(_A)
class _HpPortGvrpCtrlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('learn',1),('block',2),(_G,3)))
_HpPortGvrpCtrlStatus_Type.__name__=_C
_HpPortGvrpCtrlStatus_Object=MibTableColumn
hpPortGvrpCtrlStatus=_HpPortGvrpCtrlStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,1,1,5),_HpPortGvrpCtrlStatus_Type())
hpPortGvrpCtrlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpPortGvrpCtrlStatus.setStatus(_A)
_HpGvrpVlanTable_Object=MibTable
hpGvrpVlanTable=_HpGvrpVlanTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,2))
if mibBuilder.loadTexts:hpGvrpVlanTable.setStatus(_A)
_HpGvrpVlanEntry_Object=MibTableRow
hpGvrpVlanEntry=_HpGvrpVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,2,1))
hpGvrpVlanEntry.setIndexNames((0,_D,_m))
if mibBuilder.loadTexts:hpGvrpVlanEntry.setStatus(_A)
class _HpGvrpVlanPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpGvrpVlanPortIndex_Type.__name__=_C
_HpGvrpVlanPortIndex_Object=MibTableColumn
hpGvrpVlanPortIndex=_HpGvrpVlanPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,2,1,1),_HpGvrpVlanPortIndex_Type())
hpGvrpVlanPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpVlanPortIndex.setStatus(_A)
_HpGvrpVlanCreationMap_Type=VidList
_HpGvrpVlanCreationMap_Object=MibTableColumn
hpGvrpVlanCreationMap=_HpGvrpVlanCreationMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,2,1,2),_HpGvrpVlanCreationMap_Type())
hpGvrpVlanCreationMap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpVlanCreationMap.setStatus(_A)
_HpGvrpVlanDeletionMap_Type=VidList
_HpGvrpVlanDeletionMap_Object=MibTableColumn
hpGvrpVlanDeletionMap=_HpGvrpVlanDeletionMap_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,2,1,3),_HpGvrpVlanDeletionMap_Type())
hpGvrpVlanDeletionMap.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpVlanDeletionMap.setStatus(_A)
_HpGvrpVlanLearningOnPort_Type=VidList
_HpGvrpVlanLearningOnPort_Object=MibTableColumn
hpGvrpVlanLearningOnPort=_HpGvrpVlanLearningOnPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,2,1,4),_HpGvrpVlanLearningOnPort_Type())
hpGvrpVlanLearningOnPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpVlanLearningOnPort.setStatus(_A)
_HpGvrpVlanLeavingPort_Type=VidList
_HpGvrpVlanLeavingPort_Object=MibTableColumn
hpGvrpVlanLeavingPort=_HpGvrpVlanLeavingPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,16,2,1,5),_HpGvrpVlanLeavingPort_Type())
hpGvrpVlanLeavingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpVlanLeavingPort.setStatus(_A)
_HpSshStats_ObjectIdentity=ObjectIdentity
hpSshStats=_HpSshStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,17))
_HpSshStatsTable_Object=MibTable
hpSshStatsTable=_HpSshStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1))
if mibBuilder.loadTexts:hpSshStatsTable.setStatus(_A)
_HpSshStatsEntry_Object=MibTableRow
hpSshStatsEntry=_HpSshStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1))
hpSshStatsEntry.setIndexNames((0,_D,_n))
if mibBuilder.loadTexts:hpSshStatsEntry.setStatus(_A)
class _HpSshStatsSesIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSshStatsSesIndex_Type.__name__=_C
_HpSshStatsSesIndex_Object=MibTableColumn
hpSshStatsSesIndex=_HpSshStatsSesIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1,1),_HpSshStatsSesIndex_Type())
hpSshStatsSesIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSshStatsSesIndex.setStatus(_A)
class _HpSshStatsSesType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('console',1),('telnet',2),('ssh',3),('inactive',4)))
_HpSshStatsSesType_Type.__name__=_C
_HpSshStatsSesType_Object=MibTableColumn
hpSshStatsSesType=_HpSshStatsSesType_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1,2),_HpSshStatsSesType_Type())
hpSshStatsSesType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSshStatsSesType.setStatus(_A)
class _HpSshStatsSourceIpPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,21))
_HpSshStatsSourceIpPort_Type.__name__=_I
_HpSshStatsSourceIpPort_Object=MibTableColumn
hpSshStatsSourceIpPort=_HpSshStatsSourceIpPort_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1,3),_HpSshStatsSourceIpPort_Type())
hpSshStatsSourceIpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSshStatsSourceIpPort.setStatus(_F)
class _HpSshStatsSesVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('version1',1),('version2',2),('noConnect',255)))
_HpSshStatsSesVersion_Type.__name__=_C
_HpSshStatsSesVersion_Object=MibTableColumn
hpSshStatsSesVersion=_HpSshStatsSesVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1,4),_HpSshStatsSesVersion_Type())
hpSshStatsSesVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSshStatsSesVersion.setStatus(_A)
_HpSshStatsSourceIpType_Type=InetAddressType
_HpSshStatsSourceIpType_Object=MibTableColumn
hpSshStatsSourceIpType=_HpSshStatsSourceIpType_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1,5),_HpSshStatsSourceIpType_Type())
hpSshStatsSourceIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSshStatsSourceIpType.setStatus(_A)
_HpSshStatsSourceIpAddress_Type=InetAddress
_HpSshStatsSourceIpAddress_Object=MibTableColumn
hpSshStatsSourceIpAddress=_HpSshStatsSourceIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1,6),_HpSshStatsSourceIpAddress_Type())
hpSshStatsSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSshStatsSourceIpAddress.setStatus(_A)
_HpSshStatsSourceIpPortNum_Type=InetPortNumber
_HpSshStatsSourceIpPortNum_Object=MibTableColumn
hpSshStatsSourceIpPortNum=_HpSshStatsSourceIpPortNum_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,17,1,1,7),_HpSshStatsSourceIpPortNum_Type())
hpSshStatsSourceIpPortNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSshStatsSourceIpPortNum.setStatus(_A)
_HpSwitchPhysicalPort_ObjectIdentity=ObjectIdentity
hpSwitchPhysicalPort=_HpSwitchPhysicalPort_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,18))
_HpSwitchPhysicalPortTable_Object=MibTable
hpSwitchPhysicalPortTable=_HpSwitchPhysicalPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,1))
if mibBuilder.loadTexts:hpSwitchPhysicalPortTable.setStatus(_A)
_HpSwitchPhysicalPortEntry_Object=MibTableRow
hpSwitchPhysicalPortEntry=_HpSwitchPhysicalPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,1,1))
hpSwitchPhysicalPortEntry.setIndexNames((0,_D,_o))
if mibBuilder.loadTexts:hpSwitchPhysicalPortEntry.setStatus(_A)
class _HpSwitchPhysicalPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchPhysicalPortIndex_Type.__name__=_C
_HpSwitchPhysicalPortIndex_Object=MibTableColumn
hpSwitchPhysicalPortIndex=_HpSwitchPhysicalPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,1,1,1),_HpSwitchPhysicalPortIndex_Type())
hpSwitchPhysicalPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPhysicalPortIndex.setStatus(_A)
_HpSwitchPhysicalPortType_Type=HpSwitchPortType
_HpSwitchPhysicalPortType_Object=MibTableColumn
hpSwitchPhysicalPortType=_HpSwitchPhysicalPortType_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,1,1,2),_HpSwitchPhysicalPortType_Type())
hpSwitchPhysicalPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPhysicalPortType.setStatus(_A)
_HpSwitchPortStatTable_Object=MibTable
hpSwitchPortStatTable=_HpSwitchPortStatTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2))
if mibBuilder.loadTexts:hpSwitchPortStatTable.setStatus(_A)
_HpSwitchPortStatEntry_Object=MibTableRow
hpSwitchPortStatEntry=_HpSwitchPortStatEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1))
hpSwitchPortStatEntry.setIndexNames((0,_D,_p))
if mibBuilder.loadTexts:hpSwitchPortStatEntry.setStatus(_A)
class _HpSwitchPortStatIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchPortStatIndex_Type.__name__=_C
_HpSwitchPortStatIndex_Object=MibTableColumn
hpSwitchPortStatIndex=_HpSwitchPortStatIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,1),_HpSwitchPortStatIndex_Type())
hpSwitchPortStatIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatIndex.setStatus(_A)
_HpSwitchPortStatAvgInBcastPkts_Type=Counter32
_HpSwitchPortStatAvgInBcastPkts_Object=MibTableColumn
hpSwitchPortStatAvgInBcastPkts=_HpSwitchPortStatAvgInBcastPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,2),_HpSwitchPortStatAvgInBcastPkts_Type())
hpSwitchPortStatAvgInBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgInBcastPkts.setStatus(_A)
_HpSwitchPortStatAvgInMcastPkts_Type=Counter32
_HpSwitchPortStatAvgInMcastPkts_Object=MibTableColumn
hpSwitchPortStatAvgInMcastPkts=_HpSwitchPortStatAvgInMcastPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,3),_HpSwitchPortStatAvgInMcastPkts_Type())
hpSwitchPortStatAvgInMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgInMcastPkts.setStatus(_A)
_HpSwitchPortStatAvgInTotalPkts_Type=Counter32
_HpSwitchPortStatAvgInTotalPkts_Object=MibTableColumn
hpSwitchPortStatAvgInTotalPkts=_HpSwitchPortStatAvgInTotalPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,4),_HpSwitchPortStatAvgInTotalPkts_Type())
hpSwitchPortStatAvgInTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgInTotalPkts.setStatus(_A)
_HpSwitchPortStatAvgOutBcastPkts_Type=Counter32
_HpSwitchPortStatAvgOutBcastPkts_Object=MibTableColumn
hpSwitchPortStatAvgOutBcastPkts=_HpSwitchPortStatAvgOutBcastPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,5),_HpSwitchPortStatAvgOutBcastPkts_Type())
hpSwitchPortStatAvgOutBcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgOutBcastPkts.setStatus(_A)
_HpSwitchPortStatAvgOutMcastPkts_Type=Counter32
_HpSwitchPortStatAvgOutMcastPkts_Object=MibTableColumn
hpSwitchPortStatAvgOutMcastPkts=_HpSwitchPortStatAvgOutMcastPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,6),_HpSwitchPortStatAvgOutMcastPkts_Type())
hpSwitchPortStatAvgOutMcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgOutMcastPkts.setStatus(_A)
_HpSwitchPortStatAvgOutTotalPkts_Type=Counter32
_HpSwitchPortStatAvgOutTotalPkts_Object=MibTableColumn
hpSwitchPortStatAvgOutTotalPkts=_HpSwitchPortStatAvgOutTotalPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,7),_HpSwitchPortStatAvgOutTotalPkts_Type())
hpSwitchPortStatAvgOutTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgOutTotalPkts.setStatus(_A)
_HpSwitchPortStatAvgInBytes_Type=Counter32
_HpSwitchPortStatAvgInBytes_Object=MibTableColumn
hpSwitchPortStatAvgInBytes=_HpSwitchPortStatAvgInBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,8),_HpSwitchPortStatAvgInBytes_Type())
hpSwitchPortStatAvgInBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgInBytes.setStatus(_A)
_HpSwitchPortStatAvgOutBytes_Type=Counter32
_HpSwitchPortStatAvgOutBytes_Object=MibTableColumn
hpSwitchPortStatAvgOutBytes=_HpSwitchPortStatAvgOutBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,9),_HpSwitchPortStatAvgOutBytes_Type())
hpSwitchPortStatAvgOutBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgOutBytes.setStatus(_A)
class _HpSwitchPortStatAvgInPortUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchPortStatAvgInPortUtil_Type.__name__=_C
_HpSwitchPortStatAvgInPortUtil_Object=MibTableColumn
hpSwitchPortStatAvgInPortUtil=_HpSwitchPortStatAvgInPortUtil_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,10),_HpSwitchPortStatAvgInPortUtil_Type())
hpSwitchPortStatAvgInPortUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgInPortUtil.setStatus(_A)
class _HpSwitchPortStatAvgOutPortUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpSwitchPortStatAvgOutPortUtil_Type.__name__=_C
_HpSwitchPortStatAvgOutPortUtil_Object=MibTableColumn
hpSwitchPortStatAvgOutPortUtil=_HpSwitchPortStatAvgOutPortUtil_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,18,2,1,11),_HpSwitchPortStatAvgOutPortUtil_Type())
hpSwitchPortStatAvgOutPortUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchPortStatAvgOutPortUtil.setStatus(_A)
_HpSwitchCosStats_ObjectIdentity=ObjectIdentity
hpSwitchCosStats=_HpSwitchCosStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,19))
_HpSwitchQueueWatchStatsTable_Object=MibTable
hpSwitchQueueWatchStatsTable=_HpSwitchQueueWatchStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,1))
if mibBuilder.loadTexts:hpSwitchQueueWatchStatsTable.setStatus(_A)
_HpSwitchQueueWatchStatsEntry_Object=MibTableRow
hpSwitchQueueWatchStatsEntry=_HpSwitchQueueWatchStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,1,1))
hpSwitchQueueWatchStatsEntry.setIndexNames((0,_D,_q),(0,_D,_r))
if mibBuilder.loadTexts:hpSwitchQueueWatchStatsEntry.setStatus(_A)
class _HpSwitchQueueWatchStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchQueueWatchStatsPortIndex_Type.__name__=_C
_HpSwitchQueueWatchStatsPortIndex_Object=MibTableColumn
hpSwitchQueueWatchStatsPortIndex=_HpSwitchQueueWatchStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,1,1,1),_HpSwitchQueueWatchStatsPortIndex_Type())
hpSwitchQueueWatchStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchQueueWatchStatsPortIndex.setStatus(_A)
class _HpSwitchQueueWatchStatsQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchQueueWatchStatsQueueIndex_Type.__name__=_C
_HpSwitchQueueWatchStatsQueueIndex_Object=MibTableColumn
hpSwitchQueueWatchStatsQueueIndex=_HpSwitchQueueWatchStatsQueueIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,1,1,2),_HpSwitchQueueWatchStatsQueueIndex_Type())
hpSwitchQueueWatchStatsQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchQueueWatchStatsQueueIndex.setStatus(_A)
_HpSwitchQueueWatchStatsQueueDrops_Type=Counter32
_HpSwitchQueueWatchStatsQueueDrops_Object=MibTableColumn
hpSwitchQueueWatchStatsQueueDrops=_HpSwitchQueueWatchStatsQueueDrops_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,1,1,3),_HpSwitchQueueWatchStatsQueueDrops_Type())
hpSwitchQueueWatchStatsQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchQueueWatchStatsQueueDrops.setStatus(_A)
_HpSwitchEgressQueueDropStatsTable_Object=MibTable
hpSwitchEgressQueueDropStatsTable=_HpSwitchEgressQueueDropStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,2))
if mibBuilder.loadTexts:hpSwitchEgressQueueDropStatsTable.setStatus(_A)
_HpSwitchEgressQueueDropStatsEntry_Object=MibTableRow
hpSwitchEgressQueueDropStatsEntry=_HpSwitchEgressQueueDropStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,2,1))
hpSwitchEgressQueueDropStatsEntry.setIndexNames((0,_D,_s),(0,_D,_t))
if mibBuilder.loadTexts:hpSwitchEgressQueueDropStatsEntry.setStatus(_A)
class _HpSwitchEgressQueueDropStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchEgressQueueDropStatsPortIndex_Type.__name__=_C
_HpSwitchEgressQueueDropStatsPortIndex_Object=MibTableColumn
hpSwitchEgressQueueDropStatsPortIndex=_HpSwitchEgressQueueDropStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,2,1,1),_HpSwitchEgressQueueDropStatsPortIndex_Type())
hpSwitchEgressQueueDropStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueDropStatsPortIndex.setStatus(_A)
class _HpSwitchEgressQueueDropStatsQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchEgressQueueDropStatsQueueIndex_Type.__name__=_C
_HpSwitchEgressQueueDropStatsQueueIndex_Object=MibTableColumn
hpSwitchEgressQueueDropStatsQueueIndex=_HpSwitchEgressQueueDropStatsQueueIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,2,1,2),_HpSwitchEgressQueueDropStatsQueueIndex_Type())
hpSwitchEgressQueueDropStatsQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueDropStatsQueueIndex.setStatus(_A)
_HpSwitchEgressQueueDropStatsQueueDrops_Type=Counter32
_HpSwitchEgressQueueDropStatsQueueDrops_Object=MibTableColumn
hpSwitchEgressQueueDropStatsQueueDrops=_HpSwitchEgressQueueDropStatsQueueDrops_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,2,1,3),_HpSwitchEgressQueueDropStatsQueueDrops_Type())
hpSwitchEgressQueueDropStatsQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueDropStatsQueueDrops.setStatus(_A)
_HpSwitchEgressQueueStatsTable_Object=MibTable
hpSwitchEgressQueueStatsTable=_HpSwitchEgressQueueStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3))
if mibBuilder.loadTexts:hpSwitchEgressQueueStatsTable.setStatus(_A)
_HpSwitchEgressQueueStatsEntry_Object=MibTableRow
hpSwitchEgressQueueStatsEntry=_HpSwitchEgressQueueStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3,1))
hpSwitchEgressQueueStatsEntry.setIndexNames((0,_D,_u),(0,_D,_v))
if mibBuilder.loadTexts:hpSwitchEgressQueueStatsEntry.setStatus(_A)
class _HpSwitchEgressQueueStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchEgressQueueStatsPortIndex_Type.__name__=_C
_HpSwitchEgressQueueStatsPortIndex_Object=MibTableColumn
hpSwitchEgressQueueStatsPortIndex=_HpSwitchEgressQueueStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3,1,1),_HpSwitchEgressQueueStatsPortIndex_Type())
hpSwitchEgressQueueStatsPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueStatsPortIndex.setStatus(_A)
class _HpSwitchEgressQueueStatsQueueIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpSwitchEgressQueueStatsQueueIndex_Type.__name__=_C
_HpSwitchEgressQueueStatsQueueIndex_Object=MibTableColumn
hpSwitchEgressQueueStatsQueueIndex=_HpSwitchEgressQueueStatsQueueIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3,1,2),_HpSwitchEgressQueueStatsQueueIndex_Type())
hpSwitchEgressQueueStatsQueueIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueStatsQueueIndex.setStatus(_A)
_HpSwitchEgressQueueTxPkts_Type=Counter64
_HpSwitchEgressQueueTxPkts_Object=MibTableColumn
hpSwitchEgressQueueTxPkts=_HpSwitchEgressQueueTxPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3,1,3),_HpSwitchEgressQueueTxPkts_Type())
hpSwitchEgressQueueTxPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueTxPkts.setStatus(_A)
_HpSwitchEgressQueueTxDropPkts_Type=Counter64
_HpSwitchEgressQueueTxDropPkts_Object=MibTableColumn
hpSwitchEgressQueueTxDropPkts=_HpSwitchEgressQueueTxDropPkts_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3,1,4),_HpSwitchEgressQueueTxDropPkts_Type())
hpSwitchEgressQueueTxDropPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueTxDropPkts.setStatus(_A)
_HpSwitchEgressQueueTxBytes_Type=Counter64
_HpSwitchEgressQueueTxBytes_Object=MibTableColumn
hpSwitchEgressQueueTxBytes=_HpSwitchEgressQueueTxBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3,1,5),_HpSwitchEgressQueueTxBytes_Type())
hpSwitchEgressQueueTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueTxBytes.setStatus(_A)
_HpSwitchEgressQueueTxDropBytes_Type=Counter64
_HpSwitchEgressQueueTxDropBytes_Object=MibTableColumn
hpSwitchEgressQueueTxDropBytes=_HpSwitchEgressQueueTxDropBytes_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,19,3,1,6),_HpSwitchEgressQueueTxDropBytes_Type())
hpSwitchEgressQueueTxDropBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:hpSwitchEgressQueueTxDropBytes.setStatus(_A)
_HpGarpStats_ObjectIdentity=ObjectIdentity
hpGarpStats=_HpGarpStats_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,9,21))
_HpGarpStatsTable_Object=MibTable
hpGarpStatsTable=_HpGarpStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,21,1))
if mibBuilder.loadTexts:hpGarpStatsTable.setStatus(_A)
_HpGarpStatsEntry_Object=MibTableRow
hpGarpStatsEntry=_HpGarpStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,21,1,1))
hpGarpStatsEntry.setIndexNames((0,_D,_w))
if mibBuilder.loadTexts:hpGarpStatsEntry.setStatus(_A)
class _HpGarpStatsPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpGarpStatsPortIndex_Type.__name__=_C
_HpGarpStatsPortIndex_Object=MibTableColumn
hpGarpStatsPortIndex=_HpGarpStatsPortIndex_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,21,1,1,1),_HpGarpStatsPortIndex_Type())
hpGarpStatsPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpGarpStatsPortIndex.setStatus(_A)
_HpGvrpFramesRecieved_Type=Counter32
_HpGvrpFramesRecieved_Object=MibTableColumn
hpGvrpFramesRecieved=_HpGvrpFramesRecieved_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,21,1,1,2),_HpGvrpFramesRecieved_Type())
hpGvrpFramesRecieved.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpFramesRecieved.setStatus(_A)
_HpGvrpFramesTransmitted_Type=Counter32
_HpGvrpFramesTransmitted_Object=MibTableColumn
hpGvrpFramesTransmitted=_HpGvrpFramesTransmitted_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,21,1,1,3),_HpGvrpFramesTransmitted_Type())
hpGvrpFramesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpFramesTransmitted.setStatus(_A)
_HpGvrpFramesDiscarded_Type=Counter32
_HpGvrpFramesDiscarded_Object=MibTableColumn
hpGvrpFramesDiscarded=_HpGvrpFramesDiscarded_Object((1,3,6,1,4,1,11,2,14,11,5,1,9,21,1,1,4),_HpGvrpFramesDiscarded_Type())
hpGvrpFramesDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:hpGvrpFramesDiscarded.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MacAddress':MacAddress,'VlanID':VlanID,'hpSwitchStatistics':hpSwitchStatistics,'hpSwitchIpxStat':hpSwitchIpxStat,'hpSwitchIpxStatTable':hpSwitchIpxStatTable,'hpSwitchIpxStatEntry':hpSwitchIpxStatEntry,_N:hpSwitchIpxStatIndex,'hpSwitchIpxStatNodeAddr':hpSwitchIpxStatNodeAddr,'hpSwitchIpxStatGatewayAddr':hpSwitchIpxStatGatewayAddr,'hpSwitchIpxStatGatewayEncap':hpSwitchIpxStatGatewayEncap,'hpSwitchIpxStatAdminStatus':hpSwitchIpxStatAdminStatus,'hpSwitchIpStat':hpSwitchIpStat,'hpSwitchIpStatTimepAdminStatus':hpSwitchIpStatTimepAdminStatus,'hpSwitchIpStatTimepServerAddr':hpSwitchIpStatTimepServerAddr,'hpSwitchIpStatTimepPollInterval':hpSwitchIpStatTimepPollInterval,'hpSwitchIpStatTable':hpSwitchIpStatTable,'hpSwitchIpStatEntry':hpSwitchIpStatEntry,_O:hpSwitchIpStatIndex,'hpSwitchIpStatAddr':hpSwitchIpStatAddr,'hpSwitchIpStatMask':hpSwitchIpStatMask,'hpSwitchIpStatGatewayAddr':hpSwitchIpStatGatewayAddr,'hpSwitchIpStatAdminStatus':hpSwitchIpStatAdminStatus,'hpSwitchFdbInfo':hpSwitchFdbInfo,'hpSwitchVlanFdbAddrTable':hpSwitchVlanFdbAddrTable,'hpSwitchVlanFdbAddrEntry':hpSwitchVlanFdbAddrEntry,_P:hpSwitchVlanFdbId,_Q:hpSwitchVlanFdbAddress,'hpSwitchVlanFdbPort':hpSwitchVlanFdbPort,'hpSwitchPortFdbAddrTable':hpSwitchPortFdbAddrTable,'hpSwitchPortFdbAddrEntry':hpSwitchPortFdbAddrEntry,_R:hpSwitchPortFdbId,_S:hpSwitchPortFdbAddress,'hpSwitchPortFdbVlanId':hpSwitchPortFdbVlanId,'hpSwitchPortFdbVidList':hpSwitchPortFdbVidList,'hpSwitchStpStat':hpSwitchStpStat,'hpSwitchStpStatAdminStatus':hpSwitchStpStatAdminStatus,'hpSwitchMiscStat':hpSwitchMiscStat,'hpSwitchCpuStat':hpSwitchCpuStat,'hpSwitchFddiIpFragStat':hpSwitchFddiIpFragStat,'hpSwitchFddiIpFragStatTable':hpSwitchFddiIpFragStatTable,'hpSwitchFddiIpFragStatEntry':hpSwitchFddiIpFragStatEntry,_T:hpSwitchFddiIpFragStatIndex,'hpSwitchFddiIpFragFramesFragmented':hpSwitchFddiIpFragFramesFragmented,'hpSwitchFddiIpFragFramesCreated':hpSwitchFddiIpFragFramesCreated,'hpSwitchFddiIpFragFrameErrors':hpSwitchFddiIpFragFrameErrors,'hpSwitchFddiSystemStat':hpSwitchFddiSystemStat,'hpSwitchFddiSystemStatTable':hpSwitchFddiSystemStatTable,'hpSwitchFddiSystemStatEntry':hpSwitchFddiSystemStatEntry,_U:hpSwitchFddiSystemStatIndex,'hpSwitchFddiSystemOsVersion':hpSwitchFddiSystemOsVersion,'hpSwitchFddiSystemRomVersion':hpSwitchFddiSystemRomVersion,'hpSwitchFddiSystemMemoryTotal':hpSwitchFddiSystemMemoryTotal,'hpSwitchFddiSystemMemoryFree':hpSwitchFddiSystemMemoryFree,'hpSwitchFddiSystemCpuUtil':hpSwitchFddiSystemCpuUtil,'hpSwitchFddiSystemBuildDirectory':hpSwitchFddiSystemBuildDirectory,'hpSwitchFddiSystemBuildDate':hpSwitchFddiSystemBuildDate,'hpSwitchFddiSystemBuildNumber':hpSwitchFddiSystemBuildNumber,'hpABCStats':hpABCStats,'hpABCStatsTable':hpABCStatsTable,'hpABCStatsEntry':hpABCStatsEntry,_V:hpABCStatsVlanIndex,_W:hpABCStatsPortIndex,'hpABCStatsPortType':hpABCStatsPortType,'hpABCStatsArpReplies':hpABCStatsArpReplies,'hpABCStatsIpxReplies':hpABCStatsIpxReplies,'hpABCStatsIpRipControl':hpABCStatsIpRipControl,'hpABCStatsIpxRipSapControl':hpABCStatsIpxRipSapControl,'hpIgmpStats':hpIgmpStats,'hpIgmpStatsTable':hpIgmpStatsTable,'hpIgmpStatsEntry':hpIgmpStatsEntry,_M:hpIgmpStatsVlanIndex,_K:hpIgmpStatsActiveGroupAddr,'hpIgmpStatsReports':hpIgmpStatsReports,'hpIgmpStatsQueries':hpIgmpStatsQueries,'hpIgmpStatsQuerierAccessPort':hpIgmpStatsQuerierAccessPort,'hpIgmpStatsPortTable':hpIgmpStatsPortTable,'hpIgmpStatsPortEntry':hpIgmpStatsPortEntry,_Y:hpIgmpStatsPortIndex,'hpIgmpStatsPortType':hpIgmpStatsPortType,'hpIgmpStatsPortAccess':hpIgmpStatsPortAccess,'hpIgmpStatsPortTable2':hpIgmpStatsPortTable2,'hpIgmpStatsPortEntry2':hpIgmpStatsPortEntry2,_b:hpIgmpStatsPortIndex2,'hpIgmpStatsPortType2':hpIgmpStatsPortType2,'hpIgmpStatsPortAccess2':hpIgmpStatsPortAccess2,'hpIgmpStatsPortAgeTimer2':hpIgmpStatsPortAgeTimer2,'hpIgmpStatsPortLeaveTimer2':hpIgmpStatsPortLeaveTimer2,'hpLdbalStats':hpLdbalStats,'hpLdbalStatsPortTable':hpLdbalStatsPortTable,'hpLdbalStatsPortEntry':hpLdbalStatsPortEntry,_c:hpLdbalStatsPortIndex,'hpLdbalStatsPortState':hpLdbalStatsPortState,'hpLdbalStatsAdjacentSwitch':hpLdbalStatsAdjacentSwitch,'hpLdbalStatsPeerPort':hpLdbalStatsPeerPort,'hpLdbalStatsAdjacentHost':hpLdbalStatsAdjacentHost,'hpLdbalStatsMeshWarningStatus':hpLdbalStatsMeshWarningStatus,'hpSwitchMacStats':hpSwitchMacStats,'hpSwitchFdbAddressCount':hpSwitchFdbAddressCount,'hpSwitchFlowControlStatus':hpSwitchFlowControlStatus,'hpSwitchFlowControlStatusTable':hpSwitchFlowControlStatusTable,'hpSwitchFlowControlStatusEntry':hpSwitchFlowControlStatusEntry,_e:hpSwitchFlowControlStatusPortIndex,'hpSwitchFlowControlState':hpSwitchFlowControlState,'hpFECStatsTrunk':hpFECStatsTrunk,'hpFECStatsTrunkTable':hpFECStatsTrunkTable,'hpFECStatsTrunkEntry':hpFECStatsTrunkEntry,_f:hpFECStatsTrunkIndex,'hpFECStatsTrunkName':hpFECStatsTrunkName,'hpFECStatsTrunkNegotiationStatus':hpFECStatsTrunkNegotiationStatus,'hpFECStatsTrunkForwardingMode':hpFECStatsTrunkForwardingMode,'hpFECStatsTrunkFlushPktsEchoed':hpFECStatsTrunkFlushPktsEchoed,'hpFECStatsPort':hpFECStatsPort,'hpFECStatsPortTable':hpFECStatsPortTable,'hpFECStatsPortEntry':hpFECStatsPortEntry,_j:hpFECStatsPortIndex,'hpFECStatsPortTrunkNumber':hpFECStatsPortTrunkNumber,'hpFECStatsPortTrunkName':hpFECStatsPortTrunkName,'hpFECStatsPortMode':hpFECStatsPortMode,'hpFECStatsPortNegotiationStatus':hpFECStatsPortNegotiationStatus,'hpFECStatsPortHellosSent':hpFECStatsPortHellosSent,'hpFECStatsPortHellosReceived':hpFECStatsPortHellosReceived,'hpFECStatsPortMySlowHello':hpFECStatsPortMySlowHello,'hpFECStatsPortMyAutoMode':hpFECStatsPortMyAutoMode,'hpFECStatsPortPartner':hpFECStatsPortPartner,'hpFECStatsPortFlushPktsEchoed':hpFECStatsPortFlushPktsEchoed,'hpGvrpStats':hpGvrpStats,'hpGvrpStatsTable':hpGvrpStatsTable,'hpGvrpStatsEntry':hpGvrpStatsEntry,_k:hpGvrpStatsVlanIndex,_l:hpGvrpStatsPortIndex,'hpGvrpStatsPortVlanMember':hpGvrpStatsPortVlanMember,'hpGvrpPortIfOperStatus':hpGvrpPortIfOperStatus,'hpPortGvrpCtrlStatus':hpPortGvrpCtrlStatus,'hpGvrpVlanTable':hpGvrpVlanTable,'hpGvrpVlanEntry':hpGvrpVlanEntry,_m:hpGvrpVlanPortIndex,'hpGvrpVlanCreationMap':hpGvrpVlanCreationMap,'hpGvrpVlanDeletionMap':hpGvrpVlanDeletionMap,'hpGvrpVlanLearningOnPort':hpGvrpVlanLearningOnPort,'hpGvrpVlanLeavingPort':hpGvrpVlanLeavingPort,'hpSshStats':hpSshStats,'hpSshStatsTable':hpSshStatsTable,'hpSshStatsEntry':hpSshStatsEntry,_n:hpSshStatsSesIndex,'hpSshStatsSesType':hpSshStatsSesType,'hpSshStatsSourceIpPort':hpSshStatsSourceIpPort,'hpSshStatsSesVersion':hpSshStatsSesVersion,'hpSshStatsSourceIpType':hpSshStatsSourceIpType,'hpSshStatsSourceIpAddress':hpSshStatsSourceIpAddress,'hpSshStatsSourceIpPortNum':hpSshStatsSourceIpPortNum,'hpSwitchPhysicalPort':hpSwitchPhysicalPort,'hpSwitchPhysicalPortTable':hpSwitchPhysicalPortTable,'hpSwitchPhysicalPortEntry':hpSwitchPhysicalPortEntry,_o:hpSwitchPhysicalPortIndex,'hpSwitchPhysicalPortType':hpSwitchPhysicalPortType,'hpSwitchPortStatTable':hpSwitchPortStatTable,'hpSwitchPortStatEntry':hpSwitchPortStatEntry,_p:hpSwitchPortStatIndex,'hpSwitchPortStatAvgInBcastPkts':hpSwitchPortStatAvgInBcastPkts,'hpSwitchPortStatAvgInMcastPkts':hpSwitchPortStatAvgInMcastPkts,'hpSwitchPortStatAvgInTotalPkts':hpSwitchPortStatAvgInTotalPkts,'hpSwitchPortStatAvgOutBcastPkts':hpSwitchPortStatAvgOutBcastPkts,'hpSwitchPortStatAvgOutMcastPkts':hpSwitchPortStatAvgOutMcastPkts,'hpSwitchPortStatAvgOutTotalPkts':hpSwitchPortStatAvgOutTotalPkts,'hpSwitchPortStatAvgInBytes':hpSwitchPortStatAvgInBytes,'hpSwitchPortStatAvgOutBytes':hpSwitchPortStatAvgOutBytes,'hpSwitchPortStatAvgInPortUtil':hpSwitchPortStatAvgInPortUtil,'hpSwitchPortStatAvgOutPortUtil':hpSwitchPortStatAvgOutPortUtil,'hpSwitchCosStats':hpSwitchCosStats,'hpSwitchQueueWatchStatsTable':hpSwitchQueueWatchStatsTable,'hpSwitchQueueWatchStatsEntry':hpSwitchQueueWatchStatsEntry,_q:hpSwitchQueueWatchStatsPortIndex,_r:hpSwitchQueueWatchStatsQueueIndex,'hpSwitchQueueWatchStatsQueueDrops':hpSwitchQueueWatchStatsQueueDrops,'hpSwitchEgressQueueDropStatsTable':hpSwitchEgressQueueDropStatsTable,'hpSwitchEgressQueueDropStatsEntry':hpSwitchEgressQueueDropStatsEntry,_s:hpSwitchEgressQueueDropStatsPortIndex,_t:hpSwitchEgressQueueDropStatsQueueIndex,'hpSwitchEgressQueueDropStatsQueueDrops':hpSwitchEgressQueueDropStatsQueueDrops,'hpSwitchEgressQueueStatsTable':hpSwitchEgressQueueStatsTable,'hpSwitchEgressQueueStatsEntry':hpSwitchEgressQueueStatsEntry,_u:hpSwitchEgressQueueStatsPortIndex,_v:hpSwitchEgressQueueStatsQueueIndex,'hpSwitchEgressQueueTxPkts':hpSwitchEgressQueueTxPkts,'hpSwitchEgressQueueTxDropPkts':hpSwitchEgressQueueTxDropPkts,'hpSwitchEgressQueueTxBytes':hpSwitchEgressQueueTxBytes,'hpSwitchEgressQueueTxDropBytes':hpSwitchEgressQueueTxDropBytes,'hpGarpStats':hpGarpStats,'hpGarpStatsTable':hpGarpStatsTable,'hpGarpStatsEntry':hpGarpStatsEntry,_w:hpGarpStatsPortIndex,'hpGvrpFramesRecieved':hpGvrpFramesRecieved,'hpGvrpFramesTransmitted':hpGvrpFramesTransmitted,'hpGvrpFramesDiscarded':hpGvrpFramesDiscarded})