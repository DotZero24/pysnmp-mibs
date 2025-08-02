_Q='zxAnLdpPeerIpAddr'
_P='zxAnLdpPeerIpAddrType'
_O='zxAnLdpTargetIpAddr'
_N='zxAnLdpTargetIpAddrType'
_M='zxAnL3IfIndex'
_L='ZTE-AN-L3-IF-MIB'
_K='DisplayString'
_J='read-only'
_I='not-accessible'
_H='ZTE-AN-LDP-MIB'
_G='disable'
_F='enable'
_E='seconds'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','RowStatus','TextualConvention')
zxAnL3IfIndex,=mibBuilder.importSymbols(_L,_M)
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnLdpMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,55))
_ZxAnLdpGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnLdpGlobalObjects=_ZxAnLdpGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,55,1))
class _ZxAnLdpMplsEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxAnLdpMplsEnable_Type.__name__=_B
_ZxAnLdpMplsEnable_Object=MibScalar
zxAnLdpMplsEnable=_ZxAnLdpMplsEnable_Object((1,3,6,1,4,1,3902,1015,55,1,1),_ZxAnLdpMplsEnable_Type())
zxAnLdpMplsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsEnable.setStatus(_A)
class _ZxAnLdpMplsMinLabel_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnLdpMplsMinLabel_Type.__name__=_B
_ZxAnLdpMplsMinLabel_Object=MibScalar
zxAnLdpMplsMinLabel=_ZxAnLdpMplsMinLabel_Object((1,3,6,1,4,1,3902,1015,55,1,2),_ZxAnLdpMplsMinLabel_Type())
zxAnLdpMplsMinLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsMinLabel.setStatus(_A)
class _ZxAnLdpMplsMaxLabel_Type(Integer32):defaultValue=100000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnLdpMplsMaxLabel_Type.__name__=_B
_ZxAnLdpMplsMaxLabel_Object=MibScalar
zxAnLdpMplsMaxLabel=_ZxAnLdpMplsMaxLabel_Object((1,3,6,1,4,1,3902,1015,55,1,3),_ZxAnLdpMplsMaxLabel_Type())
zxAnLdpMplsMaxLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsMaxLabel.setStatus(_A)
class _ZxAnLdpMplsLdpRouterId_Type(Integer32):defaultValue=0
_ZxAnLdpMplsLdpRouterId_Type.__name__=_B
_ZxAnLdpMplsLdpRouterId_Object=MibScalar
zxAnLdpMplsLdpRouterId=_ZxAnLdpMplsLdpRouterId_Object((1,3,6,1,4,1,3902,1015,55,1,4),_ZxAnLdpMplsLdpRouterId_Type())
zxAnLdpMplsLdpRouterId.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsLdpRouterId.setStatus(_A)
class _ZxAnLdpMplsLdpRouterIdForce_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('force',1),('noForce',2)))
_ZxAnLdpMplsLdpRouterIdForce_Type.__name__=_B
_ZxAnLdpMplsLdpRouterIdForce_Object=MibScalar
zxAnLdpMplsLdpRouterIdForce=_ZxAnLdpMplsLdpRouterIdForce_Object((1,3,6,1,4,1,3902,1015,55,1,5),_ZxAnLdpMplsLdpRouterIdForce_Type())
zxAnLdpMplsLdpRouterIdForce.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsLdpRouterIdForce.setStatus(_A)
class _ZxAnLdpMplsExplicitNullEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxAnLdpMplsExplicitNullEnable_Type.__name__=_B
_ZxAnLdpMplsExplicitNullEnable_Object=MibScalar
zxAnLdpMplsExplicitNullEnable=_ZxAnLdpMplsExplicitNullEnable_Object((1,3,6,1,4,1,3902,1015,55,1,6),_ZxAnLdpMplsExplicitNullEnable_Type())
zxAnLdpMplsExplicitNullEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsExplicitNullEnable.setStatus(_A)
class _ZxAnLdpMplsMinInUseLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnLdpMplsMinInUseLabel_Type.__name__=_B
_ZxAnLdpMplsMinInUseLabel_Object=MibScalar
zxAnLdpMplsMinInUseLabel=_ZxAnLdpMplsMinInUseLabel_Object((1,3,6,1,4,1,3902,1015,55,1,7),_ZxAnLdpMplsMinInUseLabel_Type())
zxAnLdpMplsMinInUseLabel.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnLdpMplsMinInUseLabel.setStatus(_A)
class _ZxAnLdpMplsMaxInUseLabel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1048575))
_ZxAnLdpMplsMaxInUseLabel_Type.__name__=_B
_ZxAnLdpMplsMaxInUseLabel_Object=MibScalar
zxAnLdpMplsMaxInUseLabel=_ZxAnLdpMplsMaxInUseLabel_Object((1,3,6,1,4,1,3902,1015,55,1,8),_ZxAnLdpMplsMaxInUseLabel_Type())
zxAnLdpMplsMaxInUseLabel.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnLdpMplsMaxInUseLabel.setStatus(_A)
class _ZxAnLdpMplsSessInitBackoffTime_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_ZxAnLdpMplsSessInitBackoffTime_Type.__name__=_B
_ZxAnLdpMplsSessInitBackoffTime_Object=MibScalar
zxAnLdpMplsSessInitBackoffTime=_ZxAnLdpMplsSessInitBackoffTime_Object((1,3,6,1,4,1,3902,1015,55,1,9),_ZxAnLdpMplsSessInitBackoffTime_Type())
zxAnLdpMplsSessInitBackoffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsSessInitBackoffTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsSessInitBackoffTime.setUnits(_E)
class _ZxAnLdpMplsSessMaxBackoffTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_ZxAnLdpMplsSessMaxBackoffTime_Type.__name__=_B
_ZxAnLdpMplsSessMaxBackoffTime_Object=MibScalar
zxAnLdpMplsSessMaxBackoffTime=_ZxAnLdpMplsSessMaxBackoffTime_Object((1,3,6,1,4,1,3902,1015,55,1,10),_ZxAnLdpMplsSessMaxBackoffTime_Type())
zxAnLdpMplsSessMaxBackoffTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsSessMaxBackoffTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsSessMaxBackoffTime.setUnits(_E)
class _ZxAnLdpMplsSessKeepAliveTime_Type(Integer32):defaultValue=180;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,65535))
_ZxAnLdpMplsSessKeepAliveTime_Type.__name__=_B
_ZxAnLdpMplsSessKeepAliveTime_Object=MibScalar
zxAnLdpMplsSessKeepAliveTime=_ZxAnLdpMplsSessKeepAliveTime_Object((1,3,6,1,4,1,3902,1015,55,1,11),_ZxAnLdpMplsSessKeepAliveTime_Type())
zxAnLdpMplsSessKeepAliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsSessKeepAliveTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsSessKeepAliveTime.setUnits(_E)
class _ZxAnLdpMplsGrEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxAnLdpMplsGrEnable_Type.__name__=_B
_ZxAnLdpMplsGrEnable_Object=MibScalar
zxAnLdpMplsGrEnable=_ZxAnLdpMplsGrEnable_Object((1,3,6,1,4,1,3902,1015,55,1,12),_ZxAnLdpMplsGrEnable_Type())
zxAnLdpMplsGrEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsGrEnable.setStatus(_A)
class _ZxAnLdpMplsGrRecoveryTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,600))
_ZxAnLdpMplsGrRecoveryTime_Type.__name__=_B
_ZxAnLdpMplsGrRecoveryTime_Object=MibScalar
zxAnLdpMplsGrRecoveryTime=_ZxAnLdpMplsGrRecoveryTime_Object((1,3,6,1,4,1,3902,1015,55,1,13),_ZxAnLdpMplsGrRecoveryTime_Type())
zxAnLdpMplsGrRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsGrRecoveryTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsGrRecoveryTime.setUnits(_E)
class _ZxAnLdpMplsGrNeighKeepAliveTime_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,300))
_ZxAnLdpMplsGrNeighKeepAliveTime_Type.__name__=_B
_ZxAnLdpMplsGrNeighKeepAliveTime_Object=MibScalar
zxAnLdpMplsGrNeighKeepAliveTime=_ZxAnLdpMplsGrNeighKeepAliveTime_Object((1,3,6,1,4,1,3902,1015,55,1,14),_ZxAnLdpMplsGrNeighKeepAliveTime_Type())
zxAnLdpMplsGrNeighKeepAliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsGrNeighKeepAliveTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsGrNeighKeepAliveTime.setUnits(_E)
class _ZxAnLdpMplsVpnGrEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxAnLdpMplsVpnGrEnable_Type.__name__=_B
_ZxAnLdpMplsVpnGrEnable_Object=MibScalar
zxAnLdpMplsVpnGrEnable=_ZxAnLdpMplsVpnGrEnable_Object((1,3,6,1,4,1,3902,1015,55,1,15),_ZxAnLdpMplsVpnGrEnable_Type())
zxAnLdpMplsVpnGrEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsVpnGrEnable.setStatus(_A)
class _ZxAnLdpMplsHelloHoldTime_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65535))
_ZxAnLdpMplsHelloHoldTime_Type.__name__=_B
_ZxAnLdpMplsHelloHoldTime_Object=MibScalar
zxAnLdpMplsHelloHoldTime=_ZxAnLdpMplsHelloHoldTime_Object((1,3,6,1,4,1,3902,1015,55,1,16),_ZxAnLdpMplsHelloHoldTime_Type())
zxAnLdpMplsHelloHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsHelloHoldTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsHelloHoldTime.setUnits(_E)
class _ZxAnLdpMplsHelloSendInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnLdpMplsHelloSendInterval_Type.__name__=_B
_ZxAnLdpMplsHelloSendInterval_Object=MibScalar
zxAnLdpMplsHelloSendInterval=_ZxAnLdpMplsHelloSendInterval_Object((1,3,6,1,4,1,3902,1015,55,1,17),_ZxAnLdpMplsHelloSendInterval_Type())
zxAnLdpMplsHelloSendInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsHelloSendInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsHelloSendInterval.setUnits(_E)
class _ZxAnLdpMplsTgtHelloHoldTime_Type(Integer32):defaultValue=45;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65535))
_ZxAnLdpMplsTgtHelloHoldTime_Type.__name__=_B
_ZxAnLdpMplsTgtHelloHoldTime_Object=MibScalar
zxAnLdpMplsTgtHelloHoldTime=_ZxAnLdpMplsTgtHelloHoldTime_Object((1,3,6,1,4,1,3902,1015,55,1,18),_ZxAnLdpMplsTgtHelloHoldTime_Type())
zxAnLdpMplsTgtHelloHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsTgtHelloHoldTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsTgtHelloHoldTime.setUnits(_E)
class _ZxAnLdpMplsTgtHelloSendInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnLdpMplsTgtHelloSendInterval_Type.__name__=_B
_ZxAnLdpMplsTgtHelloSendInterval_Object=MibScalar
zxAnLdpMplsTgtHelloSendInterval=_ZxAnLdpMplsTgtHelloSendInterval_Object((1,3,6,1,4,1,3902,1015,55,1,19),_ZxAnLdpMplsTgtHelloSendInterval_Type())
zxAnLdpMplsTgtHelloSendInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsTgtHelloSendInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnLdpMplsTgtHelloSendInterval.setUnits(_E)
class _ZxAnLdpMplsKeepSessWithHelloMsg_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxAnLdpMplsKeepSessWithHelloMsg_Type.__name__=_B
_ZxAnLdpMplsKeepSessWithHelloMsg_Object=MibScalar
zxAnLdpMplsKeepSessWithHelloMsg=_ZxAnLdpMplsKeepSessWithHelloMsg_Object((1,3,6,1,4,1,3902,1015,55,1,20),_ZxAnLdpMplsKeepSessWithHelloMsg_Type())
zxAnLdpMplsKeepSessWithHelloMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsKeepSessWithHelloMsg.setStatus(_A)
class _ZxAnLdpMplsGrHelperEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxAnLdpMplsGrHelperEnable_Type.__name__=_B
_ZxAnLdpMplsGrHelperEnable_Object=MibScalar
zxAnLdpMplsGrHelperEnable=_ZxAnLdpMplsGrHelperEnable_Object((1,3,6,1,4,1,3902,1015,55,1,21),_ZxAnLdpMplsGrHelperEnable_Type())
zxAnLdpMplsGrHelperEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsGrHelperEnable.setStatus(_A)
class _ZxAnLdpMplsLabelControlMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ordered',1),('independent',2)))
_ZxAnLdpMplsLabelControlMode_Type.__name__=_B
_ZxAnLdpMplsLabelControlMode_Object=MibScalar
zxAnLdpMplsLabelControlMode=_ZxAnLdpMplsLabelControlMode_Object((1,3,6,1,4,1,3902,1015,55,1,22),_ZxAnLdpMplsLabelControlMode_Type())
zxAnLdpMplsLabelControlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsLabelControlMode.setStatus(_A)
class _ZxAnLdpMplsLabelRetentionMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('conservative',1),('liberal',2)))
_ZxAnLdpMplsLabelRetentionMode_Type.__name__=_B
_ZxAnLdpMplsLabelRetentionMode_Object=MibScalar
zxAnLdpMplsLabelRetentionMode=_ZxAnLdpMplsLabelRetentionMode_Object((1,3,6,1,4,1,3902,1015,55,1,23),_ZxAnLdpMplsLabelRetentionMode_Type())
zxAnLdpMplsLabelRetentionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsLabelRetentionMode.setStatus(_A)
class _ZxAnLdpMplsPktWithLabelEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_ZxAnLdpMplsPktWithLabelEnable_Type.__name__=_B
_ZxAnLdpMplsPktWithLabelEnable_Object=MibScalar
zxAnLdpMplsPktWithLabelEnable=_ZxAnLdpMplsPktWithLabelEnable_Object((1,3,6,1,4,1,3902,1015,55,1,24),_ZxAnLdpMplsPktWithLabelEnable_Type())
zxAnLdpMplsPktWithLabelEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpMplsPktWithLabelEnable.setStatus(_A)
_ZxAnLdpObjects_ObjectIdentity=ObjectIdentity
zxAnLdpObjects=_ZxAnLdpObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,55,2))
_ZxAnLdpTargetSessionTable_Object=MibTable
zxAnLdpTargetSessionTable=_ZxAnLdpTargetSessionTable_Object((1,3,6,1,4,1,3902,1015,55,2,3))
if mibBuilder.loadTexts:zxAnLdpTargetSessionTable.setStatus(_A)
_ZxAnLdpTargetSessionEntry_Object=MibTableRow
zxAnLdpTargetSessionEntry=_ZxAnLdpTargetSessionEntry_Object((1,3,6,1,4,1,3902,1015,55,2,3,1))
zxAnLdpTargetSessionEntry.setIndexNames((0,_H,_N),(0,_H,_O))
if mibBuilder.loadTexts:zxAnLdpTargetSessionEntry.setStatus(_A)
_ZxAnLdpTargetIpAddrType_Type=InetAddressType
_ZxAnLdpTargetIpAddrType_Object=MibTableColumn
zxAnLdpTargetIpAddrType=_ZxAnLdpTargetIpAddrType_Object((1,3,6,1,4,1,3902,1015,55,2,3,1,1),_ZxAnLdpTargetIpAddrType_Type())
zxAnLdpTargetIpAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnLdpTargetIpAddrType.setStatus(_A)
_ZxAnLdpTargetIpAddr_Type=InetAddress
_ZxAnLdpTargetIpAddr_Object=MibTableColumn
zxAnLdpTargetIpAddr=_ZxAnLdpTargetIpAddr_Object((1,3,6,1,4,1,3902,1015,55,2,3,1,2),_ZxAnLdpTargetIpAddr_Type())
zxAnLdpTargetIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnLdpTargetIpAddr.setStatus(_A)
class _ZxAnLdpTargetDistributionMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dod',1),('du',2)))
_ZxAnLdpTargetDistributionMode_Type.__name__=_B
_ZxAnLdpTargetDistributionMode_Object=MibTableColumn
zxAnLdpTargetDistributionMode=_ZxAnLdpTargetDistributionMode_Object((1,3,6,1,4,1,3902,1015,55,2,3,1,3),_ZxAnLdpTargetDistributionMode_Type())
zxAnLdpTargetDistributionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpTargetDistributionMode.setStatus(_A)
_ZxAnLdpTargetSessionRowStatus_Type=RowStatus
_ZxAnLdpTargetSessionRowStatus_Object=MibTableColumn
zxAnLdpTargetSessionRowStatus=_ZxAnLdpTargetSessionRowStatus_Object((1,3,6,1,4,1,3902,1015,55,2,3,1,20),_ZxAnLdpTargetSessionRowStatus_Type())
zxAnLdpTargetSessionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpTargetSessionRowStatus.setStatus(_A)
_ZxAnLdpSessionTable_Object=MibTable
zxAnLdpSessionTable=_ZxAnLdpSessionTable_Object((1,3,6,1,4,1,3902,1015,55,2,4))
if mibBuilder.loadTexts:zxAnLdpSessionTable.setStatus(_A)
_ZxAnLdpSessionEntry_Object=MibTableRow
zxAnLdpSessionEntry=_ZxAnLdpSessionEntry_Object((1,3,6,1,4,1,3902,1015,55,2,4,1))
zxAnLdpSessionEntry.setIndexNames((0,_H,_P),(0,_H,_Q))
if mibBuilder.loadTexts:zxAnLdpSessionEntry.setStatus(_A)
_ZxAnLdpPeerIpAddrType_Type=InetAddressType
_ZxAnLdpPeerIpAddrType_Object=MibTableColumn
zxAnLdpPeerIpAddrType=_ZxAnLdpPeerIpAddrType_Object((1,3,6,1,4,1,3902,1015,55,2,4,1,1),_ZxAnLdpPeerIpAddrType_Type())
zxAnLdpPeerIpAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnLdpPeerIpAddrType.setStatus(_A)
_ZxAnLdpPeerIpAddr_Type=InetAddress
_ZxAnLdpPeerIpAddr_Object=MibTableColumn
zxAnLdpPeerIpAddr=_ZxAnLdpPeerIpAddr_Object((1,3,6,1,4,1,3902,1015,55,2,4,1,2),_ZxAnLdpPeerIpAddr_Type())
zxAnLdpPeerIpAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:zxAnLdpPeerIpAddr.setStatus(_A)
class _ZxAnLdpMd5Pwd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,80))
_ZxAnLdpMd5Pwd_Type.__name__=_K
_ZxAnLdpMd5Pwd_Object=MibTableColumn
zxAnLdpMd5Pwd=_ZxAnLdpMd5Pwd_Object((1,3,6,1,4,1,3902,1015,55,2,4,1,3),_ZxAnLdpMd5Pwd_Type())
zxAnLdpMd5Pwd.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpMd5Pwd.setStatus(_A)
class _ZxAnLdpMd5PwdConfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noPwd',1),('withPwd',2)))
_ZxAnLdpMd5PwdConfStatus_Type.__name__=_B
_ZxAnLdpMd5PwdConfStatus_Object=MibTableColumn
zxAnLdpMd5PwdConfStatus=_ZxAnLdpMd5PwdConfStatus_Object((1,3,6,1,4,1,3902,1015,55,2,4,1,4),_ZxAnLdpMd5PwdConfStatus_Type())
zxAnLdpMd5PwdConfStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zxAnLdpMd5PwdConfStatus.setStatus(_A)
class _ZxAnLdpMd5PwdEncrypt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noEncrypt',1),('encrypt',2)))
_ZxAnLdpMd5PwdEncrypt_Type.__name__=_B
_ZxAnLdpMd5PwdEncrypt_Object=MibTableColumn
zxAnLdpMd5PwdEncrypt=_ZxAnLdpMd5PwdEncrypt_Object((1,3,6,1,4,1,3902,1015,55,2,4,1,5),_ZxAnLdpMd5PwdEncrypt_Type())
zxAnLdpMd5PwdEncrypt.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpMd5PwdEncrypt.setStatus(_A)
class _ZxAnLdpSessionReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noReset',1),('reset',2)))
_ZxAnLdpSessionReset_Type.__name__=_B
_ZxAnLdpSessionReset_Object=MibTableColumn
zxAnLdpSessionReset=_ZxAnLdpSessionReset_Object((1,3,6,1,4,1,3902,1015,55,2,4,1,6),_ZxAnLdpSessionReset_Type())
zxAnLdpSessionReset.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnLdpSessionReset.setStatus(_A)
_ZxAnLdpSessionRowStatus_Type=RowStatus
_ZxAnLdpSessionRowStatus_Object=MibTableColumn
zxAnLdpSessionRowStatus=_ZxAnLdpSessionRowStatus_Object((1,3,6,1,4,1,3902,1015,55,2,4,1,20),_ZxAnLdpSessionRowStatus_Type())
zxAnLdpSessionRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpSessionRowStatus.setStatus(_A)
_ZxAnLdpL3IfEntityTable_Object=MibTable
zxAnLdpL3IfEntityTable=_ZxAnLdpL3IfEntityTable_Object((1,3,6,1,4,1,3902,1015,55,2,5))
if mibBuilder.loadTexts:zxAnLdpL3IfEntityTable.setStatus(_A)
_ZxAnLdpL3IfEntityEntry_Object=MibTableRow
zxAnLdpL3IfEntityEntry=_ZxAnLdpL3IfEntityEntry_Object((1,3,6,1,4,1,3902,1015,55,2,5,1))
zxAnLdpL3IfEntityEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:zxAnLdpL3IfEntityEntry.setStatus(_A)
class _ZxAnLdpL3IfTransAddrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unconfigured',0),('ifIp',1),('specifyIp',2)))
_ZxAnLdpL3IfTransAddrMode_Type.__name__=_B
_ZxAnLdpL3IfTransAddrMode_Object=MibTableColumn
zxAnLdpL3IfTransAddrMode=_ZxAnLdpL3IfTransAddrMode_Object((1,3,6,1,4,1,3902,1015,55,2,5,1,1),_ZxAnLdpL3IfTransAddrMode_Type())
zxAnLdpL3IfTransAddrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpL3IfTransAddrMode.setStatus(_A)
_ZxAnLdpL3IfTransAddrType_Type=InetAddressType
_ZxAnLdpL3IfTransAddrType_Object=MibTableColumn
zxAnLdpL3IfTransAddrType=_ZxAnLdpL3IfTransAddrType_Object((1,3,6,1,4,1,3902,1015,55,2,5,1,2),_ZxAnLdpL3IfTransAddrType_Type())
zxAnLdpL3IfTransAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpL3IfTransAddrType.setStatus(_A)
_ZxAnLdpL3IfTransAddr_Type=InetAddress
_ZxAnLdpL3IfTransAddr_Object=MibTableColumn
zxAnLdpL3IfTransAddr=_ZxAnLdpL3IfTransAddr_Object((1,3,6,1,4,1,3902,1015,55,2,5,1,3),_ZxAnLdpL3IfTransAddr_Type())
zxAnLdpL3IfTransAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpL3IfTransAddr.setStatus(_A)
class _ZxAnLdpL3IfDistributionMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('dod',1),('du',2)))
_ZxAnLdpL3IfDistributionMode_Type.__name__=_B
_ZxAnLdpL3IfDistributionMode_Object=MibTableColumn
zxAnLdpL3IfDistributionMode=_ZxAnLdpL3IfDistributionMode_Object((1,3,6,1,4,1,3902,1015,55,2,5,1,4),_ZxAnLdpL3IfDistributionMode_Type())
zxAnLdpL3IfDistributionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpL3IfDistributionMode.setStatus(_A)
_ZxAnLdpL3IfEntityRowStatus_Type=RowStatus
_ZxAnLdpL3IfEntityRowStatus_Object=MibTableColumn
zxAnLdpL3IfEntityRowStatus=_ZxAnLdpL3IfEntityRowStatus_Object((1,3,6,1,4,1,3902,1015,55,2,5,1,20),_ZxAnLdpL3IfEntityRowStatus_Type())
zxAnLdpL3IfEntityRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnLdpL3IfEntityRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'zxAnLdpMib':zxAnLdpMib,'zxAnLdpGlobalObjects':zxAnLdpGlobalObjects,'zxAnLdpMplsEnable':zxAnLdpMplsEnable,'zxAnLdpMplsMinLabel':zxAnLdpMplsMinLabel,'zxAnLdpMplsMaxLabel':zxAnLdpMplsMaxLabel,'zxAnLdpMplsLdpRouterId':zxAnLdpMplsLdpRouterId,'zxAnLdpMplsLdpRouterIdForce':zxAnLdpMplsLdpRouterIdForce,'zxAnLdpMplsExplicitNullEnable':zxAnLdpMplsExplicitNullEnable,'zxAnLdpMplsMinInUseLabel':zxAnLdpMplsMinInUseLabel,'zxAnLdpMplsMaxInUseLabel':zxAnLdpMplsMaxInUseLabel,'zxAnLdpMplsSessInitBackoffTime':zxAnLdpMplsSessInitBackoffTime,'zxAnLdpMplsSessMaxBackoffTime':zxAnLdpMplsSessMaxBackoffTime,'zxAnLdpMplsSessKeepAliveTime':zxAnLdpMplsSessKeepAliveTime,'zxAnLdpMplsGrEnable':zxAnLdpMplsGrEnable,'zxAnLdpMplsGrRecoveryTime':zxAnLdpMplsGrRecoveryTime,'zxAnLdpMplsGrNeighKeepAliveTime':zxAnLdpMplsGrNeighKeepAliveTime,'zxAnLdpMplsVpnGrEnable':zxAnLdpMplsVpnGrEnable,'zxAnLdpMplsHelloHoldTime':zxAnLdpMplsHelloHoldTime,'zxAnLdpMplsHelloSendInterval':zxAnLdpMplsHelloSendInterval,'zxAnLdpMplsTgtHelloHoldTime':zxAnLdpMplsTgtHelloHoldTime,'zxAnLdpMplsTgtHelloSendInterval':zxAnLdpMplsTgtHelloSendInterval,'zxAnLdpMplsKeepSessWithHelloMsg':zxAnLdpMplsKeepSessWithHelloMsg,'zxAnLdpMplsGrHelperEnable':zxAnLdpMplsGrHelperEnable,'zxAnLdpMplsLabelControlMode':zxAnLdpMplsLabelControlMode,'zxAnLdpMplsLabelRetentionMode':zxAnLdpMplsLabelRetentionMode,'zxAnLdpMplsPktWithLabelEnable':zxAnLdpMplsPktWithLabelEnable,'zxAnLdpObjects':zxAnLdpObjects,'zxAnLdpTargetSessionTable':zxAnLdpTargetSessionTable,'zxAnLdpTargetSessionEntry':zxAnLdpTargetSessionEntry,_N:zxAnLdpTargetIpAddrType,_O:zxAnLdpTargetIpAddr,'zxAnLdpTargetDistributionMode':zxAnLdpTargetDistributionMode,'zxAnLdpTargetSessionRowStatus':zxAnLdpTargetSessionRowStatus,'zxAnLdpSessionTable':zxAnLdpSessionTable,'zxAnLdpSessionEntry':zxAnLdpSessionEntry,_P:zxAnLdpPeerIpAddrType,_Q:zxAnLdpPeerIpAddr,'zxAnLdpMd5Pwd':zxAnLdpMd5Pwd,'zxAnLdpMd5PwdConfStatus':zxAnLdpMd5PwdConfStatus,'zxAnLdpMd5PwdEncrypt':zxAnLdpMd5PwdEncrypt,'zxAnLdpSessionReset':zxAnLdpSessionReset,'zxAnLdpSessionRowStatus':zxAnLdpSessionRowStatus,'zxAnLdpL3IfEntityTable':zxAnLdpL3IfEntityTable,'zxAnLdpL3IfEntityEntry':zxAnLdpL3IfEntityEntry,'zxAnLdpL3IfTransAddrMode':zxAnLdpL3IfTransAddrMode,'zxAnLdpL3IfTransAddrType':zxAnLdpL3IfTransAddrType,'zxAnLdpL3IfTransAddr':zxAnLdpL3IfTransAddr,'zxAnLdpL3IfDistributionMode':zxAnLdpL3IfDistributionMode,'zxAnLdpL3IfEntityRowStatus':zxAnLdpL3IfEntityRowStatus})