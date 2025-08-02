_p='extremeVplsNotifStatusOperStatus'
_o='extremeVplsNotifConfigAdminStatus'
_n='extremeVplsNotifConfigVpnId'
_m='extremeVplsNotifConfigIndex'
_l='extremeMplsNotifLdpSessionDiscontinuityTime'
_k='extremeMplsNotifLdpSessionState'
_j='extremeMplsNotifLdpPeerLdpId'
_i='extremeMplsNotifLdpEntityIndex'
_h='extremeMplsNotifLdpEntityLdpId'
_g='extremeMplsNotifTunnelOperStatus'
_f='extremeMplsNotifTunnelAdminStatus'
_e='extremeMplsNotifTunnelEgressLSRId'
_d='extremeMplsNotifTunnelIngressLSRId'
_c='extremeMplsNotifTunnelInstance'
_b='extremeMplsNotifTunnelIndex'
_a='extremePwNotificationPeerAddr'
_Z='extremePwNotificationPeerAddrType'
_Y='extremePwNotificationPwOperStatus'
_X='disabled'
_W='enabled'
_V='extremeVplsPwBindIndex'
_U='extremeVplsIndex'
_T='extremeVplsStatusIndex'
_S='extremeVplsConfigIndex'
_R='degraded'
_Q='testing'
_P='extremePwNotificationLspIndex'
_O='lspIndex'
_N='TruthValue'
_M='pwIndex'
_L='PW-STD-MIB'
_K='extremePwNotificationPwIndex'
_J='not-accessible'
_I='down'
_H='up'
_G='read-write'
_F='Unsigned32'
_E='Integer32'
_D='accessible-for-notify'
_C='read-only'
_B='EXTREME-MPLS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
MplsIndexType,=mibBuilder.importSymbols('MPLS-LSR-STD-MIB','MplsIndexType')
MplsExtendedTunnelId,MplsLdpIdentifier,MplsLsrIdentifier,MplsTunnelIndex,MplsTunnelInstanceIndex=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsExtendedTunnelId','MplsLdpIdentifier','MplsLsrIdentifier','MplsTunnelIndex','MplsTunnelInstanceIndex')
pwIndex,=mibBuilder.importSymbols(_L,_M)
PwIndexType,PwOperStatusTC,PwStatus=mibBuilder.importSymbols('PW-TC-STD-MIB','PwIndexType','PwOperStatusTC','PwStatus')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_N)
VPNIdOrZero,=mibBuilder.importSymbols('VPN-TC-STD-MIB','VPNIdOrZero')
extremeMplsMIB=ModuleIdentity((1,3,6,1,4,1,1916,1,37))
class IndexInteger(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ExtremeMplsNotifications_ObjectIdentity=ObjectIdentity
extremeMplsNotifications=_ExtremeMplsNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,37,0))
_ExtremeMplsScalars_ObjectIdentity=ObjectIdentity
extremeMplsScalars=_ExtremeMplsScalars_ObjectIdentity((1,3,6,1,4,1,1916,1,37,1))
class _ExtremePwUpDownNotificationEnable_Type(TruthValue):defaultValue=1
_ExtremePwUpDownNotificationEnable_Type.__name__=_N
_ExtremePwUpDownNotificationEnable_Object=MibScalar
extremePwUpDownNotificationEnable=_ExtremePwUpDownNotificationEnable_Object((1,3,6,1,4,1,1916,1,37,1,5),_ExtremePwUpDownNotificationEnable_Type())
extremePwUpDownNotificationEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:extremePwUpDownNotificationEnable.setStatus(_A)
class _ExtremePwDeletedNotificationEnable_Type(TruthValue):defaultValue=1
_ExtremePwDeletedNotificationEnable_Type.__name__=_N
_ExtremePwDeletedNotificationEnable_Object=MibScalar
extremePwDeletedNotificationEnable=_ExtremePwDeletedNotificationEnable_Object((1,3,6,1,4,1,1916,1,37,1,6),_ExtremePwDeletedNotificationEnable_Type())
extremePwDeletedNotificationEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:extremePwDeletedNotificationEnable.setStatus(_A)
class _ExtremePwNotificationMaxRate_Type(Unsigned32):defaultValue=0
_ExtremePwNotificationMaxRate_Type.__name__=_F
_ExtremePwNotificationMaxRate_Object=MibScalar
extremePwNotificationMaxRate=_ExtremePwNotificationMaxRate_Object((1,3,6,1,4,1,1916,1,37,1,7),_ExtremePwNotificationMaxRate_Type())
extremePwNotificationMaxRate.setMaxAccess(_G)
if mibBuilder.loadTexts:extremePwNotificationMaxRate.setStatus(_A)
_ExtremePwNotificationPwIndex_Type=PwIndexType
_ExtremePwNotificationPwIndex_Object=MibScalar
extremePwNotificationPwIndex=_ExtremePwNotificationPwIndex_Object((1,3,6,1,4,1,1916,1,37,1,8),_ExtremePwNotificationPwIndex_Type())
extremePwNotificationPwIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePwNotificationPwIndex.setStatus(_A)
_ExtremePwNotificationPwOperStatus_Type=PwOperStatusTC
_ExtremePwNotificationPwOperStatus_Object=MibScalar
extremePwNotificationPwOperStatus=_ExtremePwNotificationPwOperStatus_Object((1,3,6,1,4,1,1916,1,37,1,9),_ExtremePwNotificationPwOperStatus_Type())
extremePwNotificationPwOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePwNotificationPwOperStatus.setStatus(_A)
_ExtremePwNotificationPeerAddrType_Type=InetAddressType
_ExtremePwNotificationPeerAddrType_Object=MibScalar
extremePwNotificationPeerAddrType=_ExtremePwNotificationPeerAddrType_Object((1,3,6,1,4,1,1916,1,37,1,10),_ExtremePwNotificationPeerAddrType_Type())
extremePwNotificationPeerAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePwNotificationPeerAddrType.setStatus(_A)
_ExtremePwNotificationPeerAddr_Type=InetAddress
_ExtremePwNotificationPeerAddr_Object=MibScalar
extremePwNotificationPeerAddr=_ExtremePwNotificationPeerAddr_Object((1,3,6,1,4,1,1916,1,37,1,11),_ExtremePwNotificationPeerAddr_Type())
extremePwNotificationPeerAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePwNotificationPeerAddr.setStatus(_A)
_ExtremeMplsNotifTunnelIndex_Type=MplsTunnelIndex
_ExtremeMplsNotifTunnelIndex_Object=MibScalar
extremeMplsNotifTunnelIndex=_ExtremeMplsNotifTunnelIndex_Object((1,3,6,1,4,1,1916,1,37,1,12),_ExtremeMplsNotifTunnelIndex_Type())
extremeMplsNotifTunnelIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifTunnelIndex.setStatus(_A)
_ExtremeMplsNotifTunnelInstance_Type=MplsTunnelInstanceIndex
_ExtremeMplsNotifTunnelInstance_Object=MibScalar
extremeMplsNotifTunnelInstance=_ExtremeMplsNotifTunnelInstance_Object((1,3,6,1,4,1,1916,1,37,1,13),_ExtremeMplsNotifTunnelInstance_Type())
extremeMplsNotifTunnelInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifTunnelInstance.setStatus(_A)
_ExtremeMplsNotifTunnelIngressLSRId_Type=MplsExtendedTunnelId
_ExtremeMplsNotifTunnelIngressLSRId_Object=MibScalar
extremeMplsNotifTunnelIngressLSRId=_ExtremeMplsNotifTunnelIngressLSRId_Object((1,3,6,1,4,1,1916,1,37,1,14),_ExtremeMplsNotifTunnelIngressLSRId_Type())
extremeMplsNotifTunnelIngressLSRId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifTunnelIngressLSRId.setStatus(_A)
_ExtremeMplsNotifTunnelEgressLSRId_Type=MplsExtendedTunnelId
_ExtremeMplsNotifTunnelEgressLSRId_Object=MibScalar
extremeMplsNotifTunnelEgressLSRId=_ExtremeMplsNotifTunnelEgressLSRId_Object((1,3,6,1,4,1,1916,1,37,1,15),_ExtremeMplsNotifTunnelEgressLSRId_Type())
extremeMplsNotifTunnelEgressLSRId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifTunnelEgressLSRId.setStatus(_A)
class _ExtremeMplsNotifTunnelAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_ExtremeMplsNotifTunnelAdminStatus_Type.__name__=_E
_ExtremeMplsNotifTunnelAdminStatus_Object=MibScalar
extremeMplsNotifTunnelAdminStatus=_ExtremeMplsNotifTunnelAdminStatus_Object((1,3,6,1,4,1,1916,1,37,1,16),_ExtremeMplsNotifTunnelAdminStatus_Type())
extremeMplsNotifTunnelAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifTunnelAdminStatus.setStatus(_A)
class _ExtremeMplsNotifTunnelOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),(_I,2),(_Q,3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_ExtremeMplsNotifTunnelOperStatus_Type.__name__=_E
_ExtremeMplsNotifTunnelOperStatus_Object=MibScalar
extremeMplsNotifTunnelOperStatus=_ExtremeMplsNotifTunnelOperStatus_Object((1,3,6,1,4,1,1916,1,37,1,17),_ExtremeMplsNotifTunnelOperStatus_Type())
extremeMplsNotifTunnelOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifTunnelOperStatus.setStatus(_A)
_ExtremeMplsNotifLdpEntityLdpId_Type=MplsLdpIdentifier
_ExtremeMplsNotifLdpEntityLdpId_Object=MibScalar
extremeMplsNotifLdpEntityLdpId=_ExtremeMplsNotifLdpEntityLdpId_Object((1,3,6,1,4,1,1916,1,37,1,18),_ExtremeMplsNotifLdpEntityLdpId_Type())
extremeMplsNotifLdpEntityLdpId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifLdpEntityLdpId.setStatus(_A)
_ExtremeMplsNotifLdpEntityIndex_Type=IndexInteger
_ExtremeMplsNotifLdpEntityIndex_Object=MibScalar
extremeMplsNotifLdpEntityIndex=_ExtremeMplsNotifLdpEntityIndex_Object((1,3,6,1,4,1,1916,1,37,1,19),_ExtremeMplsNotifLdpEntityIndex_Type())
extremeMplsNotifLdpEntityIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifLdpEntityIndex.setStatus(_A)
_ExtremeMplsNotifLdpPeerLdpId_Type=MplsLdpIdentifier
_ExtremeMplsNotifLdpPeerLdpId_Object=MibScalar
extremeMplsNotifLdpPeerLdpId=_ExtremeMplsNotifLdpPeerLdpId_Object((1,3,6,1,4,1,1916,1,37,1,20),_ExtremeMplsNotifLdpPeerLdpId_Type())
extremeMplsNotifLdpPeerLdpId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifLdpPeerLdpId.setStatus(_A)
class _ExtremeMplsNotifLdpSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nonexistent',1),('initialized',2),('openrec',3),('opensent',4),('operational',5)))
_ExtremeMplsNotifLdpSessionState_Type.__name__=_E
_ExtremeMplsNotifLdpSessionState_Object=MibScalar
extremeMplsNotifLdpSessionState=_ExtremeMplsNotifLdpSessionState_Object((1,3,6,1,4,1,1916,1,37,1,21),_ExtremeMplsNotifLdpSessionState_Type())
extremeMplsNotifLdpSessionState.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifLdpSessionState.setStatus(_A)
_ExtremeMplsNotifLdpSessionDiscontinuityTime_Type=TimeStamp
_ExtremeMplsNotifLdpSessionDiscontinuityTime_Object=MibScalar
extremeMplsNotifLdpSessionDiscontinuityTime=_ExtremeMplsNotifLdpSessionDiscontinuityTime_Object((1,3,6,1,4,1,1916,1,37,1,22),_ExtremeMplsNotifLdpSessionDiscontinuityTime_Type())
extremeMplsNotifLdpSessionDiscontinuityTime.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeMplsNotifLdpSessionDiscontinuityTime.setStatus(_A)
class _ExtremeVplsNotifConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ExtremeVplsNotifConfigIndex_Type.__name__=_F
_ExtremeVplsNotifConfigIndex_Object=MibScalar
extremeVplsNotifConfigIndex=_ExtremeVplsNotifConfigIndex_Object((1,3,6,1,4,1,1916,1,37,1,23),_ExtremeVplsNotifConfigIndex_Type())
extremeVplsNotifConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVplsNotifConfigIndex.setStatus(_A)
_ExtremeVplsNotifConfigVpnId_Type=VPNIdOrZero
_ExtremeVplsNotifConfigVpnId_Object=MibScalar
extremeVplsNotifConfigVpnId=_ExtremeVplsNotifConfigVpnId_Object((1,3,6,1,4,1,1916,1,37,1,24),_ExtremeVplsNotifConfigVpnId_Type())
extremeVplsNotifConfigVpnId.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVplsNotifConfigVpnId.setStatus(_A)
class _ExtremeVplsNotifConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_Q,3)))
_ExtremeVplsNotifConfigAdminStatus_Type.__name__=_E
_ExtremeVplsNotifConfigAdminStatus_Object=MibScalar
extremeVplsNotifConfigAdminStatus=_ExtremeVplsNotifConfigAdminStatus_Object((1,3,6,1,4,1,1916,1,37,1,25),_ExtremeVplsNotifConfigAdminStatus_Type())
extremeVplsNotifConfigAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVplsNotifConfigAdminStatus.setStatus(_A)
class _ExtremeVplsNotifStatusOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_R,2),(_I,3)))
_ExtremeVplsNotifStatusOperStatus_Type.__name__=_E
_ExtremeVplsNotifStatusOperStatus_Object=MibScalar
extremeVplsNotifStatusOperStatus=_ExtremeVplsNotifStatusOperStatus_Object((1,3,6,1,4,1,1916,1,37,1,26),_ExtremeVplsNotifStatusOperStatus_Type())
extremeVplsNotifStatusOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVplsNotifStatusOperStatus.setStatus(_A)
_ExtremePwNotificationLspIndex_Type=Unsigned32
_ExtremePwNotificationLspIndex_Object=MibScalar
extremePwNotificationLspIndex=_ExtremePwNotificationLspIndex_Object((1,3,6,1,4,1,1916,1,37,1,27),_ExtremePwNotificationLspIndex_Type())
extremePwNotificationLspIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePwNotificationLspIndex.setStatus(_A)
_ExtremeVplsObjects_ObjectIdentity=ObjectIdentity
extremeVplsObjects=_ExtremeVplsObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,37,3))
_ExtremeVplsConfigTable_Object=MibTable
extremeVplsConfigTable=_ExtremeVplsConfigTable_Object((1,3,6,1,4,1,1916,1,37,3,1))
if mibBuilder.loadTexts:extremeVplsConfigTable.setStatus(_A)
_ExtremeVplsConfigEntry_Object=MibTableRow
extremeVplsConfigEntry=_ExtremeVplsConfigEntry_Object((1,3,6,1,4,1,1916,1,37,3,1,1))
extremeVplsConfigEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:extremeVplsConfigEntry.setStatus(_A)
class _ExtremeVplsConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ExtremeVplsConfigIndex_Type.__name__=_F
_ExtremeVplsConfigIndex_Object=MibTableColumn
extremeVplsConfigIndex=_ExtremeVplsConfigIndex_Object((1,3,6,1,4,1,1916,1,37,3,1,1,1),_ExtremeVplsConfigIndex_Type())
extremeVplsConfigIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVplsConfigIndex.setStatus(_A)
class _ExtremeVplsConfigRedunType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('esrp',1),('eaps',2),('stp',3)))
_ExtremeVplsConfigRedunType_Type.__name__=_E
_ExtremeVplsConfigRedunType_Object=MibTableColumn
extremeVplsConfigRedunType=_ExtremeVplsConfigRedunType_Object((1,3,6,1,4,1,1916,1,37,3,1,1,2),_ExtremeVplsConfigRedunType_Type())
extremeVplsConfigRedunType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVplsConfigRedunType.setStatus(_A)
_ExtremeVplsConfigEAPSStatus_Type=SnmpAdminString
_ExtremeVplsConfigEAPSStatus_Object=MibTableColumn
extremeVplsConfigEAPSStatus=_ExtremeVplsConfigEAPSStatus_Object((1,3,6,1,4,1,1916,1,37,3,1,1,3),_ExtremeVplsConfigEAPSStatus_Type())
extremeVplsConfigEAPSStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVplsConfigEAPSStatus.setStatus(_A)
_ExtremeVplsConfigESRPState_Type=SnmpAdminString
_ExtremeVplsConfigESRPState_Object=MibTableColumn
extremeVplsConfigESRPState=_ExtremeVplsConfigESRPState_Object((1,3,6,1,4,1,1916,1,37,3,1,1,4),_ExtremeVplsConfigESRPState_Type())
extremeVplsConfigESRPState.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVplsConfigESRPState.setStatus(_A)
_ExtremeVplsStatusTable_Object=MibTable
extremeVplsStatusTable=_ExtremeVplsStatusTable_Object((1,3,6,1,4,1,1916,1,37,3,2))
if mibBuilder.loadTexts:extremeVplsStatusTable.setStatus(_A)
_ExtremeVplsStatusEntry_Object=MibTableRow
extremeVplsStatusEntry=_ExtremeVplsStatusEntry_Object((1,3,6,1,4,1,1916,1,37,3,2,1))
extremeVplsStatusEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:extremeVplsStatusEntry.setStatus(_A)
class _ExtremeVplsStatusIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ExtremeVplsStatusIndex_Type.__name__=_F
_ExtremeVplsStatusIndex_Object=MibTableColumn
extremeVplsStatusIndex=_ExtremeVplsStatusIndex_Object((1,3,6,1,4,1,1916,1,37,3,2,1,1),_ExtremeVplsStatusIndex_Type())
extremeVplsStatusIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVplsStatusIndex.setStatus(_A)
class _ExtremeVplsOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_R,2),(_I,3)))
_ExtremeVplsOperStatus_Type.__name__=_E
_ExtremeVplsOperStatus_Object=MibTableColumn
extremeVplsOperStatus=_ExtremeVplsOperStatus_Object((1,3,6,1,4,1,1916,1,37,3,2,1,2),_ExtremeVplsOperStatus_Type())
extremeVplsOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeVplsOperStatus.setStatus(_A)
_ExtremeVplsPeerTable_Object=MibTable
extremeVplsPeerTable=_ExtremeVplsPeerTable_Object((1,3,6,1,4,1,1916,1,37,3,3))
if mibBuilder.loadTexts:extremeVplsPeerTable.setStatus(_A)
_ExtremeVplsPeerEntry_Object=MibTableRow
extremeVplsPeerEntry=_ExtremeVplsPeerEntry_Object((1,3,6,1,4,1,1916,1,37,3,3,1))
extremeVplsPeerEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:extremeVplsPeerEntry.setStatus(_A)
class _ExtremeVplsIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ExtremeVplsIndex_Type.__name__=_F
_ExtremeVplsIndex_Object=MibTableColumn
extremeVplsIndex=_ExtremeVplsIndex_Object((1,3,6,1,4,1,1916,1,37,3,3,1,1),_ExtremeVplsIndex_Type())
extremeVplsIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVplsIndex.setStatus(_A)
_ExtremeVplsPwBindIndex_Type=PwIndexType
_ExtremeVplsPwBindIndex_Object=MibTableColumn
extremeVplsPwBindIndex=_ExtremeVplsPwBindIndex_Object((1,3,6,1,4,1,1916,1,37,3,3,1,2),_ExtremeVplsPwBindIndex_Type())
extremeVplsPwBindIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVplsPwBindIndex.setStatus(_A)
class _ExtremePwInstalled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_ExtremePwInstalled_Type.__name__=_E
_ExtremePwInstalled_Object=MibTableColumn
extremePwInstalled=_ExtremePwInstalled_Object((1,3,6,1,4,1,1916,1,37,3,3,1,3),_ExtremePwInstalled_Type())
extremePwInstalled.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePwInstalled.setStatus(_A)
class _ExtremePwMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('coretocore',1),('coretospoke',2),('spoketocore',3)))
_ExtremePwMode_Type.__name__=_E
_ExtremePwMode_Object=MibTableColumn
extremePwMode=_ExtremePwMode_Object((1,3,6,1,4,1,1916,1,37,3,3,1,4),_ExtremePwMode_Type())
extremePwMode.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePwMode.setStatus(_A)
class _ExtremePwConfiguredRole_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('notApplicable',3)))
_ExtremePwConfiguredRole_Type.__name__=_E
_ExtremePwConfiguredRole_Object=MibTableColumn
extremePwConfiguredRole=_ExtremePwConfiguredRole_Object((1,3,6,1,4,1,1916,1,37,3,3,1,5),_ExtremePwConfiguredRole_Type())
extremePwConfiguredRole.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePwConfiguredRole.setStatus(_A)
_ExtremeL2VpnMplsNotificationHandler_ObjectIdentity=ObjectIdentity
extremeL2VpnMplsNotificationHandler=_ExtremeL2VpnMplsNotificationHandler_ObjectIdentity((1,3,6,1,4,1,1916,1,37,4))
class _ExtremeMPLSTrapsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ExtremeMPLSTrapsEnable_Type.__name__=_E
_ExtremeMPLSTrapsEnable_Object=MibScalar
extremeMPLSTrapsEnable=_ExtremeMPLSTrapsEnable_Object((1,3,6,1,4,1,1916,1,37,4,1),_ExtremeMPLSTrapsEnable_Type())
extremeMPLSTrapsEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeMPLSTrapsEnable.setStatus(_A)
class _ExtremeL2VpnTrapsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_X,2)))
_ExtremeL2VpnTrapsEnable_Type.__name__=_E
_ExtremeL2VpnTrapsEnable_Object=MibScalar
extremeL2VpnTrapsEnable=_ExtremeL2VpnTrapsEnable_Object((1,3,6,1,4,1,1916,1,37,4,2),_ExtremeL2VpnTrapsEnable_Type())
extremeL2VpnTrapsEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:extremeL2VpnTrapsEnable.setStatus(_A)
_ExtremePwObjects_ObjectIdentity=ObjectIdentity
extremePwObjects=_ExtremePwObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,37,5))
_ExtremePwPerfTable_Object=MibTable
extremePwPerfTable=_ExtremePwPerfTable_Object((1,3,6,1,4,1,1916,1,37,5,1))
if mibBuilder.loadTexts:extremePwPerfTable.setStatus(_A)
_ExtremePwPerfEntry_Object=MibTableRow
extremePwPerfEntry=_ExtremePwPerfEntry_Object((1,3,6,1,4,1,1916,1,37,5,1,1))
extremePwPerfEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:extremePwPerfEntry.setStatus(_A)
_PwPerfInPackets_Type=Counter32
_PwPerfInPackets_Object=MibTableColumn
pwPerfInPackets=_PwPerfInPackets_Object((1,3,6,1,4,1,1916,1,37,5,1,1,1),_PwPerfInPackets_Type())
pwPerfInPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfInPackets.setStatus(_A)
_PwPerfInBytes_Type=Counter32
_PwPerfInBytes_Object=MibTableColumn
pwPerfInBytes=_PwPerfInBytes_Object((1,3,6,1,4,1,1916,1,37,5,1,1,2),_PwPerfInBytes_Type())
pwPerfInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfInBytes.setStatus(_A)
_PwPerfOutPackets_Type=Counter32
_PwPerfOutPackets_Object=MibTableColumn
pwPerfOutPackets=_PwPerfOutPackets_Object((1,3,6,1,4,1,1916,1,37,5,1,1,3),_PwPerfOutPackets_Type())
pwPerfOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfOutPackets.setStatus(_A)
_PwPerfOutBytes_Type=Counter32
_PwPerfOutBytes_Object=MibTableColumn
pwPerfOutBytes=_PwPerfOutBytes_Object((1,3,6,1,4,1,1916,1,37,5,1,1,4),_PwPerfOutBytes_Type())
pwPerfOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfOutBytes.setStatus(_A)
_PwPerfInHCPackets_Type=Counter64
_PwPerfInHCPackets_Object=MibTableColumn
pwPerfInHCPackets=_PwPerfInHCPackets_Object((1,3,6,1,4,1,1916,1,37,5,1,1,5),_PwPerfInHCPackets_Type())
pwPerfInHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfInHCPackets.setStatus(_A)
_PwPerfInHCBytes_Type=Counter64
_PwPerfInHCBytes_Object=MibTableColumn
pwPerfInHCBytes=_PwPerfInHCBytes_Object((1,3,6,1,4,1,1916,1,37,5,1,1,6),_PwPerfInHCBytes_Type())
pwPerfInHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfInHCBytes.setStatus(_A)
_PwPerfOutHCPackets_Type=Counter64
_PwPerfOutHCPackets_Object=MibTableColumn
pwPerfOutHCPackets=_PwPerfOutHCPackets_Object((1,3,6,1,4,1,1916,1,37,5,1,1,7),_PwPerfOutHCPackets_Type())
pwPerfOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfOutHCPackets.setStatus(_A)
_PwPerfOutHCBytes_Type=Counter64
_PwPerfOutHCBytes_Object=MibTableColumn
pwPerfOutHCBytes=_PwPerfOutHCBytes_Object((1,3,6,1,4,1,1916,1,37,5,1,1,8),_PwPerfOutHCBytes_Type())
pwPerfOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwPerfOutHCBytes.setStatus(_A)
_ExtremePwLspOutboundMappingTable_Object=MibTable
extremePwLspOutboundMappingTable=_ExtremePwLspOutboundMappingTable_Object((1,3,6,1,4,1,1916,1,37,5,2))
if mibBuilder.loadTexts:extremePwLspOutboundMappingTable.setStatus(_A)
_ExtremePwLspOutboundMappingEntry_Object=MibTableRow
extremePwLspOutboundMappingEntry=_ExtremePwLspOutboundMappingEntry_Object((1,3,6,1,4,1,1916,1,37,5,2,1))
extremePwLspOutboundMappingEntry.setIndexNames((0,_L,_M),(0,_B,_O))
if mibBuilder.loadTexts:extremePwLspOutboundMappingEntry.setStatus(_A)
_LspIndex_Type=Unsigned32
_LspIndex_Object=MibTableColumn
lspIndex=_LspIndex_Object((1,3,6,1,4,1,1916,1,37,5,2,1,1),_LspIndex_Type())
lspIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:lspIndex.setStatus(_A)
_PwLspOutboundLsrXcIndex_Type=MplsIndexType
_PwLspOutboundLsrXcIndex_Object=MibTableColumn
pwLspOutboundLsrXcIndex=_PwLspOutboundLsrXcIndex_Object((1,3,6,1,4,1,1916,1,37,5,2,1,2),_PwLspOutboundLsrXcIndex_Type())
pwLspOutboundLsrXcIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspOutboundLsrXcIndex.setStatus(_A)
_PwLspOutboundTunnelIndex_Type=MplsTunnelIndex
_PwLspOutboundTunnelIndex_Object=MibTableColumn
pwLspOutboundTunnelIndex=_PwLspOutboundTunnelIndex_Object((1,3,6,1,4,1,1916,1,37,5,2,1,3),_PwLspOutboundTunnelIndex_Type())
pwLspOutboundTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspOutboundTunnelIndex.setStatus(_A)
_PwLspOutboundTunnelInstance_Type=MplsTunnelInstanceIndex
_PwLspOutboundTunnelInstance_Object=MibTableColumn
pwLspOutboundTunnelInstance=_PwLspOutboundTunnelInstance_Object((1,3,6,1,4,1,1916,1,37,5,2,1,4),_PwLspOutboundTunnelInstance_Type())
pwLspOutboundTunnelInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspOutboundTunnelInstance.setStatus(_A)
_PwLspOutboundTunnelLclLSR_Type=MplsLsrIdentifier
_PwLspOutboundTunnelLclLSR_Object=MibTableColumn
pwLspOutboundTunnelLclLSR=_PwLspOutboundTunnelLclLSR_Object((1,3,6,1,4,1,1916,1,37,5,2,1,5),_PwLspOutboundTunnelLclLSR_Type())
pwLspOutboundTunnelLclLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspOutboundTunnelLclLSR.setStatus(_A)
_PwLspOutboundTunnelPeerLSR_Type=MplsLsrIdentifier
_PwLspOutboundTunnelPeerLSR_Object=MibTableColumn
pwLspOutboundTunnelPeerLSR=_PwLspOutboundTunnelPeerLSR_Object((1,3,6,1,4,1,1916,1,37,5,2,1,6),_PwLspOutboundTunnelPeerLSR_Type())
pwLspOutboundTunnelPeerLSR.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspOutboundTunnelPeerLSR.setStatus(_A)
class _PwLspOutboundTunnelTypeInUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mplsTe',1),('mplsNonTe',2)))
_PwLspOutboundTunnelTypeInUse_Type.__name__=_E
_PwLspOutboundTunnelTypeInUse_Object=MibTableColumn
pwLspOutboundTunnelTypeInUse=_PwLspOutboundTunnelTypeInUse_Object((1,3,6,1,4,1,1916,1,37,5,2,1,7),_PwLspOutboundTunnelTypeInUse_Type())
pwLspOutboundTunnelTypeInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspOutboundTunnelTypeInUse.setStatus(_A)
_ExtremePwLspPerfTable_Object=MibTable
extremePwLspPerfTable=_ExtremePwLspPerfTable_Object((1,3,6,1,4,1,1916,1,37,5,3))
if mibBuilder.loadTexts:extremePwLspPerfTable.setStatus(_A)
_ExtremePwLspPerfEntry_Object=MibTableRow
extremePwLspPerfEntry=_ExtremePwLspPerfEntry_Object((1,3,6,1,4,1,1916,1,37,5,3,1))
extremePwLspPerfEntry.setIndexNames((0,_L,_M),(0,_B,_O))
if mibBuilder.loadTexts:extremePwLspPerfEntry.setStatus(_A)
_PwLspPerfOutPackets_Type=Counter32
_PwLspPerfOutPackets_Object=MibTableColumn
pwLspPerfOutPackets=_PwLspPerfOutPackets_Object((1,3,6,1,4,1,1916,1,37,5,3,1,1),_PwLspPerfOutPackets_Type())
pwLspPerfOutPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspPerfOutPackets.setStatus(_A)
_PwLspPerfOutBytes_Type=Counter32
_PwLspPerfOutBytes_Object=MibTableColumn
pwLspPerfOutBytes=_PwLspPerfOutBytes_Object((1,3,6,1,4,1,1916,1,37,5,3,1,2),_PwLspPerfOutBytes_Type())
pwLspPerfOutBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspPerfOutBytes.setStatus(_A)
_PwLspPerfOutHCPackets_Type=Counter64
_PwLspPerfOutHCPackets_Object=MibTableColumn
pwLspPerfOutHCPackets=_PwLspPerfOutHCPackets_Object((1,3,6,1,4,1,1916,1,37,5,3,1,3),_PwLspPerfOutHCPackets_Type())
pwLspPerfOutHCPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspPerfOutHCPackets.setStatus(_A)
_PwLspPerfOutHCBytes_Type=Counter64
_PwLspPerfOutHCBytes_Object=MibTableColumn
pwLspPerfOutHCBytes=_PwLspPerfOutHCBytes_Object((1,3,6,1,4,1,1916,1,37,5,3,1,4),_PwLspPerfOutHCBytes_Type())
pwLspPerfOutHCBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:pwLspPerfOutHCBytes.setStatus(_A)
extremePwStatusChange=NotificationType((1,3,6,1,4,1,1916,1,37,0,1))
extremePwStatusChange.setObjects(*((_B,_K),(_B,_Y)))
if mibBuilder.loadTexts:extremePwStatusChange.setStatus(_A)
extremePwDeleted=NotificationType((1,3,6,1,4,1,1916,1,37,0,2))
extremePwDeleted.setObjects(*((_B,_K),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:extremePwDeleted.setStatus(_A)
extremeMplsTunnelStatusChange=NotificationType((1,3,6,1,4,1,1916,1,37,0,3))
extremeMplsTunnelStatusChange.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:extremeMplsTunnelStatusChange.setStatus(_A)
extremeMplsLdpSessionStatusChange=NotificationType((1,3,6,1,4,1,1916,1,37,0,4))
extremeMplsLdpSessionStatusChange.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:extremeMplsLdpSessionStatusChange.setStatus(_A)
extremeVplsStatusChange=NotificationType((1,3,6,1,4,1,1916,1,37,0,5))
extremeVplsStatusChange.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:extremeVplsStatusChange.setStatus(_A)
extremePwLspAdded=NotificationType((1,3,6,1,4,1,1916,1,37,0,6))
extremePwLspAdded.setObjects(*((_B,_K),(_B,_P)))
if mibBuilder.loadTexts:extremePwLspAdded.setStatus(_A)
extremePwLspDeleted=NotificationType((1,3,6,1,4,1,1916,1,37,0,7))
extremePwLspDeleted.setObjects(*((_B,_K),(_B,_P)))
if mibBuilder.loadTexts:extremePwLspDeleted.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IndexInteger':IndexInteger,'extremeMplsMIB':extremeMplsMIB,'extremeMplsNotifications':extremeMplsNotifications,'extremePwStatusChange':extremePwStatusChange,'extremePwDeleted':extremePwDeleted,'extremeMplsTunnelStatusChange':extremeMplsTunnelStatusChange,'extremeMplsLdpSessionStatusChange':extremeMplsLdpSessionStatusChange,'extremeVplsStatusChange':extremeVplsStatusChange,'extremePwLspAdded':extremePwLspAdded,'extremePwLspDeleted':extremePwLspDeleted,'extremeMplsScalars':extremeMplsScalars,'extremePwUpDownNotificationEnable':extremePwUpDownNotificationEnable,'extremePwDeletedNotificationEnable':extremePwDeletedNotificationEnable,'extremePwNotificationMaxRate':extremePwNotificationMaxRate,_K:extremePwNotificationPwIndex,_Y:extremePwNotificationPwOperStatus,_Z:extremePwNotificationPeerAddrType,_a:extremePwNotificationPeerAddr,_b:extremeMplsNotifTunnelIndex,_c:extremeMplsNotifTunnelInstance,_d:extremeMplsNotifTunnelIngressLSRId,_e:extremeMplsNotifTunnelEgressLSRId,_f:extremeMplsNotifTunnelAdminStatus,_g:extremeMplsNotifTunnelOperStatus,_h:extremeMplsNotifLdpEntityLdpId,_i:extremeMplsNotifLdpEntityIndex,_j:extremeMplsNotifLdpPeerLdpId,_k:extremeMplsNotifLdpSessionState,_l:extremeMplsNotifLdpSessionDiscontinuityTime,_m:extremeVplsNotifConfigIndex,_n:extremeVplsNotifConfigVpnId,_o:extremeVplsNotifConfigAdminStatus,_p:extremeVplsNotifStatusOperStatus,_P:extremePwNotificationLspIndex,'extremeVplsObjects':extremeVplsObjects,'extremeVplsConfigTable':extremeVplsConfigTable,'extremeVplsConfigEntry':extremeVplsConfigEntry,_S:extremeVplsConfigIndex,'extremeVplsConfigRedunType':extremeVplsConfigRedunType,'extremeVplsConfigEAPSStatus':extremeVplsConfigEAPSStatus,'extremeVplsConfigESRPState':extremeVplsConfigESRPState,'extremeVplsStatusTable':extremeVplsStatusTable,'extremeVplsStatusEntry':extremeVplsStatusEntry,_T:extremeVplsStatusIndex,'extremeVplsOperStatus':extremeVplsOperStatus,'extremeVplsPeerTable':extremeVplsPeerTable,'extremeVplsPeerEntry':extremeVplsPeerEntry,_U:extremeVplsIndex,_V:extremeVplsPwBindIndex,'extremePwInstalled':extremePwInstalled,'extremePwMode':extremePwMode,'extremePwConfiguredRole':extremePwConfiguredRole,'extremeL2VpnMplsNotificationHandler':extremeL2VpnMplsNotificationHandler,'extremeMPLSTrapsEnable':extremeMPLSTrapsEnable,'extremeL2VpnTrapsEnable':extremeL2VpnTrapsEnable,'extremePwObjects':extremePwObjects,'extremePwPerfTable':extremePwPerfTable,'extremePwPerfEntry':extremePwPerfEntry,'pwPerfInPackets':pwPerfInPackets,'pwPerfInBytes':pwPerfInBytes,'pwPerfOutPackets':pwPerfOutPackets,'pwPerfOutBytes':pwPerfOutBytes,'pwPerfInHCPackets':pwPerfInHCPackets,'pwPerfInHCBytes':pwPerfInHCBytes,'pwPerfOutHCPackets':pwPerfOutHCPackets,'pwPerfOutHCBytes':pwPerfOutHCBytes,'extremePwLspOutboundMappingTable':extremePwLspOutboundMappingTable,'extremePwLspOutboundMappingEntry':extremePwLspOutboundMappingEntry,_O:lspIndex,'pwLspOutboundLsrXcIndex':pwLspOutboundLsrXcIndex,'pwLspOutboundTunnelIndex':pwLspOutboundTunnelIndex,'pwLspOutboundTunnelInstance':pwLspOutboundTunnelInstance,'pwLspOutboundTunnelLclLSR':pwLspOutboundTunnelLclLSR,'pwLspOutboundTunnelPeerLSR':pwLspOutboundTunnelPeerLSR,'pwLspOutboundTunnelTypeInUse':pwLspOutboundTunnelTypeInUse,'extremePwLspPerfTable':extremePwLspPerfTable,'extremePwLspPerfEntry':extremePwLspPerfEntry,'pwLspPerfOutPackets':pwLspPerfOutPackets,'pwLspPerfOutBytes':pwLspPerfOutBytes,'pwLspPerfOutHCPackets':pwLspPerfOutHCPackets,'pwLspPerfOutHCBytes':pwLspPerfOutHCBytes})