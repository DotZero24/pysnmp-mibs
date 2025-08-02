_A5='extremeVMDetectedCounterInstallResult'
_A4='extremeVMDetectedVPPName'
_A3='extremeVMDetectedVPPResult'
_A2='extremeVMDetectedEgrErrPolicies'
_A1='extremeVMDetectedIngErrPolicies'
_A0='extremeVMDetectedOperStatus'
_z='extremeVMDetectedResultEgress'
_y='extremeVMDetectedResultIngress'
_x='extremeVMDetectedEgressVPPName'
_w='extremeVMDetectedIngressVPPName'
_v='extremeVMVPPSynchType'
_u='extremeVMLastSynchStatus'
_t='extremeVMFTPAddrType'
_s='extremeVMFTPServer'
_r='policyNotMapped'
_q='policyNotFound'
_p='policyInvalid'
_o='policyNotApplied'
_n='policyApplied'
_m='authenticating'
_l='extremeVMVPPDetailPolicyName'
_k='extremeVMVPPDetailOrder'
_j='extremeVMVPPDetailType'
_i='extremeVMVPPDetailDirection'
_h='extremeVMVPPDetailVPPName'
_g='dynamicACL'
_f='policyFile'
_e='extremeVMVPP2PolicyType'
_d='extremeVMVPP2PolicyPolicyName'
_c='extremeVMVPP2PolicyVPPName'
_b='vppNotMapped'
_a='vppInvalid'
_Z='vppMissing'
_Y='extremeVMMappingType'
_X='network'
_W='extremeVMPortConfigIfIndex'
_V='synchronizeNow'
_U='extremeVMDetectedIfIndex'
_T='extremeVMMappingVPPName'
_S='extremeVMMappingEgressVPPName'
_R='extremeVMMappingIngressVPPName'
_Q='extremeVMVPPType'
_P='idle'
_O='extremeVMFTPServerType'
_N='OctetString'
_M='extremeVMDetectedMAC'
_L='extremeVMMappingMAC'
_K='extremeVMVPPName'
_J='not-accessible'
_I='accessible-for-notify'
_H='read-write'
_G='obsolete'
_F='DisplayString'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='EXTREME-VM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
extremeVM=ModuleIdentity((1,3,6,1,4,1,1916,1,39))
if mibBuilder.loadTexts:extremeVM.setRevisions(('2015-04-07 00:00','2014-03-14 00:00','2011-04-18 00:00','2010-02-03 00:00'))
class VMVPPSynchType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('global',1),('specific',2)))
class CounterDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('ingress-only',1),('egress-only',2),('both',3)))
_ExtremeVMGeneral_ObjectIdentity=ObjectIdentity
extremeVMGeneral=_ExtremeVMGeneral_ObjectIdentity((1,3,6,1,4,1,1916,1,39,1))
_ExtremeVMFTPServerTable_Object=MibTable
extremeVMFTPServerTable=_ExtremeVMFTPServerTable_Object((1,3,6,1,4,1,1916,1,39,1,1))
if mibBuilder.loadTexts:extremeVMFTPServerTable.setStatus(_A)
_ExtremeVMFTPServerEntry_Object=MibTableRow
extremeVMFTPServerEntry=_ExtremeVMFTPServerEntry_Object((1,3,6,1,4,1,1916,1,39,1,1,1))
extremeVMFTPServerEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:extremeVMFTPServerEntry.setStatus(_A)
class _ExtremeVMFTPServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('backup',2)))
_ExtremeVMFTPServerType_Type.__name__=_C
_ExtremeVMFTPServerType_Object=MibTableColumn
extremeVMFTPServerType=_ExtremeVMFTPServerType_Object((1,3,6,1,4,1,1916,1,39,1,1,1,1),_ExtremeVMFTPServerType_Type())
extremeVMFTPServerType.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMFTPServerType.setStatus(_A)
_ExtremeVMFTPAddrType_Type=InetAddressType
_ExtremeVMFTPAddrType_Object=MibTableColumn
extremeVMFTPAddrType=_ExtremeVMFTPAddrType_Object((1,3,6,1,4,1,1916,1,39,1,1,1,2),_ExtremeVMFTPAddrType_Type())
extremeVMFTPAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMFTPAddrType.setStatus(_A)
_ExtremeVMFTPServer_Type=InetAddress
_ExtremeVMFTPServer_Object=MibTableColumn
extremeVMFTPServer=_ExtremeVMFTPServer_Object((1,3,6,1,4,1,1916,1,39,1,1,1,3),_ExtremeVMFTPServer_Type())
extremeVMFTPServer.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMFTPServer.setStatus(_A)
class _ExtremeVMFTPSynchInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_ExtremeVMFTPSynchInterval_Type.__name__=_C
_ExtremeVMFTPSynchInterval_Object=MibTableColumn
extremeVMFTPSynchInterval=_ExtremeVMFTPSynchInterval_Object((1,3,6,1,4,1,1916,1,39,1,1,1,4),_ExtremeVMFTPSynchInterval_Type())
extremeVMFTPSynchInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMFTPSynchInterval.setStatus(_A)
if mibBuilder.loadTexts:extremeVMFTPSynchInterval.setUnits('seconds')
_ExtremeVMFTPRowStatus_Type=RowStatus
_ExtremeVMFTPRowStatus_Object=MibTableColumn
extremeVMFTPRowStatus=_ExtremeVMFTPRowStatus_Object((1,3,6,1,4,1,1916,1,39,1,1,1,5),_ExtremeVMFTPRowStatus_Type())
extremeVMFTPRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMFTPRowStatus.setStatus(_A)
class _ExtremeVMFTPPathName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeVMFTPPathName_Type.__name__=_F
_ExtremeVMFTPPathName_Object=MibTableColumn
extremeVMFTPPathName=_ExtremeVMFTPPathName_Object((1,3,6,1,4,1,1916,1,39,1,1,1,6),_ExtremeVMFTPPathName_Type())
extremeVMFTPPathName.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMFTPPathName.setStatus(_A)
class _ExtremeVMFTPUsername_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMFTPUsername_Type.__name__=_F
_ExtremeVMFTPUsername_Object=MibTableColumn
extremeVMFTPUsername=_ExtremeVMFTPUsername_Object((1,3,6,1,4,1,1916,1,39,1,1,1,7),_ExtremeVMFTPUsername_Type())
extremeVMFTPUsername.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMFTPUsername.setStatus(_A)
class _ExtremeVMFTPPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMFTPPassword_Type.__name__=_F
_ExtremeVMFTPPassword_Object=MibTableColumn
extremeVMFTPPassword=_ExtremeVMFTPPassword_Object((1,3,6,1,4,1,1916,1,39,1,1,1,8),_ExtremeVMFTPPassword_Type())
extremeVMFTPPassword.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMFTPPassword.setStatus(_A)
class _ExtremeVMFTPPolicyDir_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeVMFTPPolicyDir_Type.__name__=_F
_ExtremeVMFTPPolicyDir_Object=MibScalar
extremeVMFTPPolicyDir=_ExtremeVMFTPPolicyDir_Object((1,3,6,1,4,1,1916,1,39,1,2),_ExtremeVMFTPPolicyDir_Type())
extremeVMFTPPolicyDir.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMFTPPolicyDir.setStatus(_G)
_ExtremeVMLastSynch_Type=TimeStamp
_ExtremeVMLastSynch_Object=MibScalar
extremeVMLastSynch=_ExtremeVMLastSynch_Object((1,3,6,1,4,1,1916,1,39,1,3),_ExtremeVMLastSynch_Type())
extremeVMLastSynch.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMLastSynch.setStatus(_A)
class _ExtremeVMLastSynchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('success',1),('accessDenied',2),('serverTimeout',3),('serverNotConfigured',4)))
_ExtremeVMLastSynchStatus_Type.__name__=_C
_ExtremeVMLastSynchStatus_Object=MibScalar
extremeVMLastSynchStatus=_ExtremeVMLastSynchStatus_Object((1,3,6,1,4,1,1916,1,39,1,4),_ExtremeVMLastSynchStatus_Type())
extremeVMLastSynchStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMLastSynchStatus.setStatus(_A)
class _ExtremeVMSynchAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_V,2)))
_ExtremeVMSynchAdminState_Type.__name__=_C
_ExtremeVMSynchAdminState_Object=MibScalar
extremeVMSynchAdminState=_ExtremeVMSynchAdminState_Object((1,3,6,1,4,1,1916,1,39,1,5),_ExtremeVMSynchAdminState_Type())
extremeVMSynchAdminState.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMSynchAdminState.setStatus(_A)
class _ExtremeVMSynchOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),('synchronizing',2)))
_ExtremeVMSynchOperState_Type.__name__=_C
_ExtremeVMSynchOperState_Object=MibScalar
extremeVMSynchOperState=_ExtremeVMSynchOperState_Object((1,3,6,1,4,1,1916,1,39,1,6),_ExtremeVMSynchOperState_Type())
extremeVMSynchOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMSynchOperState.setStatus(_A)
_ExtremeVMTrackingEnabled_Type=TruthValue
_ExtremeVMTrackingEnabled_Object=MibScalar
extremeVMTrackingEnabled=_ExtremeVMTrackingEnabled_Object((1,3,6,1,4,1,1916,1,39,1,7),_ExtremeVMTrackingEnabled_Type())
extremeVMTrackingEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMTrackingEnabled.setStatus(_A)
_ExtremeVMPortConfigTable_Object=MibTable
extremeVMPortConfigTable=_ExtremeVMPortConfigTable_Object((1,3,6,1,4,1,1916,1,39,1,8))
if mibBuilder.loadTexts:extremeVMPortConfigTable.setStatus(_A)
_ExtremeVMPortConfigEntry_Object=MibTableRow
extremeVMPortConfigEntry=_ExtremeVMPortConfigEntry_Object((1,3,6,1,4,1,1916,1,39,1,8,1))
extremeVMPortConfigEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:extremeVMPortConfigEntry.setStatus(_A)
_ExtremeVMPortConfigIfIndex_Type=Integer32
_ExtremeVMPortConfigIfIndex_Object=MibTableColumn
extremeVMPortConfigIfIndex=_ExtremeVMPortConfigIfIndex_Object((1,3,6,1,4,1,1916,1,39,1,8,1,1),_ExtremeVMPortConfigIfIndex_Type())
extremeVMPortConfigIfIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMPortConfigIfIndex.setStatus(_A)
_ExtremeVMPortConfigVMTrackingEnabled_Type=TruthValue
_ExtremeVMPortConfigVMTrackingEnabled_Object=MibTableColumn
extremeVMPortConfigVMTrackingEnabled=_ExtremeVMPortConfigVMTrackingEnabled_Object((1,3,6,1,4,1,1916,1,39,1,8,1,2),_ExtremeVMPortConfigVMTrackingEnabled_Type())
extremeVMPortConfigVMTrackingEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMPortConfigVMTrackingEnabled.setStatus(_A)
_ExtremeVMPortConfigVMTrackingDynVlanEnabled_Type=TruthValue
_ExtremeVMPortConfigVMTrackingDynVlanEnabled_Object=MibTableColumn
extremeVMPortConfigVMTrackingDynVlanEnabled=_ExtremeVMPortConfigVMTrackingDynVlanEnabled_Object((1,3,6,1,4,1,1916,1,39,1,8,1,3),_ExtremeVMPortConfigVMTrackingDynVlanEnabled_Type())
extremeVMPortConfigVMTrackingDynVlanEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMPortConfigVMTrackingDynVlanEnabled.setStatus(_A)
_ExtremeVMVPP_ObjectIdentity=ObjectIdentity
extremeVMVPP=_ExtremeVMVPP_ObjectIdentity((1,3,6,1,4,1,1916,1,39,2))
_ExtremeVMVPPTable_Object=MibTable
extremeVMVPPTable=_ExtremeVMVPPTable_Object((1,3,6,1,4,1,1916,1,39,2,1))
if mibBuilder.loadTexts:extremeVMVPPTable.setStatus(_A)
_ExtremeVMVPPEntry_Object=MibTableRow
extremeVMVPPEntry=_ExtremeVMVPPEntry_Object((1,3,6,1,4,1,1916,1,39,2,1,1))
extremeVMVPPEntry.setIndexNames((0,_B,_Q),(0,_B,_K))
if mibBuilder.loadTexts:extremeVMVPPEntry.setStatus(_A)
class _ExtremeVMVPPType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('local',2)))
_ExtremeVMVPPType_Type.__name__=_C
_ExtremeVMVPPType_Object=MibTableColumn
extremeVMVPPType=_ExtremeVMVPPType_Object((1,3,6,1,4,1,1916,1,39,2,1,1,1),_ExtremeVMVPPType_Type())
extremeVMVPPType.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMVPPType.setStatus(_A)
class _ExtremeVMVPPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeVMVPPName_Type.__name__=_F
_ExtremeVMVPPName_Object=MibTableColumn
extremeVMVPPName=_ExtremeVMVPPName_Object((1,3,6,1,4,1,1916,1,39,2,1,1,2),_ExtremeVMVPPName_Type())
extremeVMVPPName.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMVPPName.setStatus(_A)
class _ExtremeVMVPPControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),('noOperation',2)))
_ExtremeVMVPPControl_Type.__name__=_C
_ExtremeVMVPPControl_Object=MibTableColumn
extremeVMVPPControl=_ExtremeVMVPPControl_Object((1,3,6,1,4,1,1916,1,39,2,1,1,3),_ExtremeVMVPPControl_Type())
extremeVMVPPControl.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMVPPControl.setStatus(_A)
_ExtremeVMVPPRowStatus_Type=RowStatus
_ExtremeVMVPPRowStatus_Object=MibTableColumn
extremeVMVPPRowStatus=_ExtremeVMVPPRowStatus_Object((1,3,6,1,4,1,1916,1,39,2,1,1,4),_ExtremeVMVPPRowStatus_Type())
extremeVMVPPRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMVPPRowStatus.setStatus(_A)
_ExtremeVMVPPCounter_Type=CounterDirection
_ExtremeVMVPPCounter_Object=MibTableColumn
extremeVMVPPCounter=_ExtremeVMVPPCounter_Object((1,3,6,1,4,1,1916,1,39,2,1,1,5),_ExtremeVMVPPCounter_Type())
extremeVMVPPCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMVPPCounter.setStatus(_A)
class _ExtremeVMVPPVLANTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ExtremeVMVPPVLANTag_Type.__name__=_C
_ExtremeVMVPPVLANTag_Object=MibTableColumn
extremeVMVPPVLANTag=_ExtremeVMVPPVLANTag_Object((1,3,6,1,4,1,1916,1,39,2,1,1,6),_ExtremeVMVPPVLANTag_Type())
extremeVMVPPVLANTag.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMVPPVLANTag.setStatus(_A)
class _ExtremeVMVPPVLANVRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMVPPVLANVRName_Type.__name__=_F
_ExtremeVMVPPVLANVRName_Object=MibTableColumn
extremeVMVPPVLANVRName=_ExtremeVMVPPVLANVRName_Object((1,3,6,1,4,1,1916,1,39,2,1,1,7),_ExtremeVMVPPVLANVRName_Type())
extremeVMVPPVLANVRName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMVPPVLANVRName.setStatus(_A)
_ExtremeVMMappingTable_Object=MibTable
extremeVMMappingTable=_ExtremeVMMappingTable_Object((1,3,6,1,4,1,1916,1,39,2,2))
if mibBuilder.loadTexts:extremeVMMappingTable.setStatus(_A)
_ExtremeVMMappingEntry_Object=MibTableRow
extremeVMMappingEntry=_ExtremeVMMappingEntry_Object((1,3,6,1,4,1,1916,1,39,2,2,1))
extremeVMMappingEntry.setIndexNames((0,_B,_Y),(0,_B,_L))
if mibBuilder.loadTexts:extremeVMMappingEntry.setStatus(_A)
class _ExtremeVMMappingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_X,1),('local',2)))
_ExtremeVMMappingType_Type.__name__=_C
_ExtremeVMMappingType_Object=MibTableColumn
extremeVMMappingType=_ExtremeVMMappingType_Object((1,3,6,1,4,1,1916,1,39,2,2,1,1),_ExtremeVMMappingType_Type())
extremeVMMappingType.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMMappingType.setStatus(_A)
_ExtremeVMMappingMAC_Type=MacAddress
_ExtremeVMMappingMAC_Object=MibTableColumn
extremeVMMappingMAC=_ExtremeVMMappingMAC_Object((1,3,6,1,4,1,1916,1,39,2,2,1,2),_ExtremeVMMappingMAC_Type())
extremeVMMappingMAC.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMMappingMAC.setStatus(_A)
_ExtremeVMMappingIngressVPPName_Type=DisplayString
_ExtremeVMMappingIngressVPPName_Object=MibTableColumn
extremeVMMappingIngressVPPName=_ExtremeVMMappingIngressVPPName_Object((1,3,6,1,4,1,1916,1,39,2,2,1,3),_ExtremeVMMappingIngressVPPName_Type())
extremeVMMappingIngressVPPName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMMappingIngressVPPName.setStatus(_G)
_ExtremeVMMappingEgressVPPName_Type=DisplayString
_ExtremeVMMappingEgressVPPName_Object=MibTableColumn
extremeVMMappingEgressVPPName=_ExtremeVMMappingEgressVPPName_Object((1,3,6,1,4,1,1916,1,39,2,2,1,4),_ExtremeVMMappingEgressVPPName_Type())
extremeVMMappingEgressVPPName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMMappingEgressVPPName.setStatus(_G)
class _ExtremeVMMappingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vppValid',1),(_Z,2),(_a,3),(_b,4)))
_ExtremeVMMappingStatus_Type.__name__=_C
_ExtremeVMMappingStatus_Object=MibTableColumn
extremeVMMappingStatus=_ExtremeVMMappingStatus_Object((1,3,6,1,4,1,1916,1,39,2,2,1,5),_ExtremeVMMappingStatus_Type())
extremeVMMappingStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMMappingStatus.setStatus(_A)
_ExtremeVMMappingRowStatus_Type=RowStatus
_ExtremeVMMappingRowStatus_Object=MibTableColumn
extremeVMMappingRowStatus=_ExtremeVMMappingRowStatus_Object((1,3,6,1,4,1,1916,1,39,2,2,1,6),_ExtremeVMMappingRowStatus_Type())
extremeVMMappingRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMMappingRowStatus.setStatus(_A)
class _ExtremeVMMappingVPPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMMappingVPPName_Type.__name__=_F
_ExtremeVMMappingVPPName_Object=MibTableColumn
extremeVMMappingVPPName=_ExtremeVMMappingVPPName_Object((1,3,6,1,4,1,1916,1,39,2,2,1,7),_ExtremeVMMappingVPPName_Type())
extremeVMMappingVPPName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMMappingVPPName.setStatus(_A)
class _ExtremeVMMappingVLANTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ExtremeVMMappingVLANTag_Type.__name__=_C
_ExtremeVMMappingVLANTag_Object=MibTableColumn
extremeVMMappingVLANTag=_ExtremeVMMappingVLANTag_Object((1,3,6,1,4,1,1916,1,39,2,2,1,8),_ExtremeVMMappingVLANTag_Type())
extremeVMMappingVLANTag.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMMappingVLANTag.setStatus(_A)
class _ExtremeVMMappingVLANVRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMMappingVLANVRName_Type.__name__=_F
_ExtremeVMMappingVLANVRName_Object=MibTableColumn
extremeVMMappingVLANVRName=_ExtremeVMMappingVLANVRName_Object((1,3,6,1,4,1,1916,1,39,2,2,1,9),_ExtremeVMMappingVLANVRName_Type())
extremeVMMappingVLANVRName.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMMappingVLANVRName.setStatus(_A)
_ExtremeVMVPP2PolicyTable_Object=MibTable
extremeVMVPP2PolicyTable=_ExtremeVMVPP2PolicyTable_Object((1,3,6,1,4,1,1916,1,39,2,3))
if mibBuilder.loadTexts:extremeVMVPP2PolicyTable.setStatus(_G)
_ExtremeVMVPP2PolicyEntry_Object=MibTableRow
extremeVMVPP2PolicyEntry=_ExtremeVMVPP2PolicyEntry_Object((1,3,6,1,4,1,1916,1,39,2,3,1))
extremeVMVPP2PolicyEntry.setIndexNames((0,_B,_c),(0,_B,_d),(0,_B,_e))
if mibBuilder.loadTexts:extremeVMVPP2PolicyEntry.setStatus(_G)
class _ExtremeVMVPP2PolicyVPPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeVMVPP2PolicyVPPName_Type.__name__=_F
_ExtremeVMVPP2PolicyVPPName_Object=MibTableColumn
extremeVMVPP2PolicyVPPName=_ExtremeVMVPP2PolicyVPPName_Object((1,3,6,1,4,1,1916,1,39,2,3,1,1),_ExtremeVMVPP2PolicyVPPName_Type())
extremeVMVPP2PolicyVPPName.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPP2PolicyVPPName.setStatus(_G)
class _ExtremeVMVPP2PolicyPolicyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeVMVPP2PolicyPolicyName_Type.__name__=_F
_ExtremeVMVPP2PolicyPolicyName_Object=MibTableColumn
extremeVMVPP2PolicyPolicyName=_ExtremeVMVPP2PolicyPolicyName_Object((1,3,6,1,4,1,1916,1,39,2,3,1,2),_ExtremeVMVPP2PolicyPolicyName_Type())
extremeVMVPP2PolicyPolicyName.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPP2PolicyPolicyName.setStatus(_G)
class _ExtremeVMVPP2PolicyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_ExtremeVMVPP2PolicyType_Type.__name__=_C
_ExtremeVMVPP2PolicyType_Object=MibTableColumn
extremeVMVPP2PolicyType=_ExtremeVMVPP2PolicyType_Object((1,3,6,1,4,1,1916,1,39,2,3,1,3),_ExtremeVMVPP2PolicyType_Type())
extremeVMVPP2PolicyType.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPP2PolicyType.setStatus(_G)
_ExtremeVMVPP2PolicyOrder_Type=Integer32
_ExtremeVMVPP2PolicyOrder_Object=MibTableColumn
extremeVMVPP2PolicyOrder=_ExtremeVMVPP2PolicyOrder_Object((1,3,6,1,4,1,1916,1,39,2,3,1,4),_ExtremeVMVPP2PolicyOrder_Type())
extremeVMVPP2PolicyOrder.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMVPP2PolicyOrder.setStatus(_G)
_ExtremeVMVPP2PolicyRowStatus_Type=RowStatus
_ExtremeVMVPP2PolicyRowStatus_Object=MibTableColumn
extremeVMVPP2PolicyRowStatus=_ExtremeVMVPP2PolicyRowStatus_Object((1,3,6,1,4,1,1916,1,39,2,3,1,5),_ExtremeVMVPP2PolicyRowStatus_Type())
extremeVMVPP2PolicyRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMVPP2PolicyRowStatus.setStatus(_G)
_ExtremeVMVPPDetailTable_Object=MibTable
extremeVMVPPDetailTable=_ExtremeVMVPPDetailTable_Object((1,3,6,1,4,1,1916,1,39,2,4))
if mibBuilder.loadTexts:extremeVMVPPDetailTable.setStatus(_A)
_ExtremeVMVPPDetailEntry_Object=MibTableRow
extremeVMVPPDetailEntry=_ExtremeVMVPPDetailEntry_Object((1,3,6,1,4,1,1916,1,39,2,4,1))
extremeVMVPPDetailEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:extremeVMVPPDetailEntry.setStatus(_A)
_ExtremeVMVPPDetailVPPName_Type=DisplayString
_ExtremeVMVPPDetailVPPName_Object=MibTableColumn
extremeVMVPPDetailVPPName=_ExtremeVMVPPDetailVPPName_Object((1,3,6,1,4,1,1916,1,39,2,4,1,1),_ExtremeVMVPPDetailVPPName_Type())
extremeVMVPPDetailVPPName.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPPDetailVPPName.setStatus(_A)
class _ExtremeVMVPPDetailDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_ExtremeVMVPPDetailDirection_Type.__name__=_C
_ExtremeVMVPPDetailDirection_Object=MibTableColumn
extremeVMVPPDetailDirection=_ExtremeVMVPPDetailDirection_Object((1,3,6,1,4,1,1916,1,39,2,4,1,2),_ExtremeVMVPPDetailDirection_Type())
extremeVMVPPDetailDirection.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPPDetailDirection.setStatus(_A)
class _ExtremeVMVPPDetailType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_f,1),(_g,2)))
_ExtremeVMVPPDetailType_Type.__name__=_C
_ExtremeVMVPPDetailType_Object=MibTableColumn
extremeVMVPPDetailType=_ExtremeVMVPPDetailType_Object((1,3,6,1,4,1,1916,1,39,2,4,1,3),_ExtremeVMVPPDetailType_Type())
extremeVMVPPDetailType.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPPDetailType.setStatus(_A)
_ExtremeVMVPPDetailOrder_Type=Integer32
_ExtremeVMVPPDetailOrder_Object=MibTableColumn
extremeVMVPPDetailOrder=_ExtremeVMVPPDetailOrder_Object((1,3,6,1,4,1,1916,1,39,2,4,1,4),_ExtremeVMVPPDetailOrder_Type())
extremeVMVPPDetailOrder.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPPDetailOrder.setStatus(_A)
_ExtremeVMVPPDetailPolicyName_Type=DisplayString
_ExtremeVMVPPDetailPolicyName_Object=MibTableColumn
extremeVMVPPDetailPolicyName=_ExtremeVMVPPDetailPolicyName_Object((1,3,6,1,4,1,1916,1,39,2,4,1,5),_ExtremeVMVPPDetailPolicyName_Type())
extremeVMVPPDetailPolicyName.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeVMVPPDetailPolicyName.setStatus(_A)
_ExtremeVMVPPDetailRowStatus_Type=RowStatus
_ExtremeVMVPPDetailRowStatus_Object=MibTableColumn
extremeVMVPPDetailRowStatus=_ExtremeVMVPPDetailRowStatus_Object((1,3,6,1,4,1,1916,1,39,2,4,1,6),_ExtremeVMVPPDetailRowStatus_Type())
extremeVMVPPDetailRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:extremeVMVPPDetailRowStatus.setStatus(_A)
_ExtremeVMDetected_ObjectIdentity=ObjectIdentity
extremeVMDetected=_ExtremeVMDetected_ObjectIdentity((1,3,6,1,4,1,1916,1,39,3))
_ExtremeVMDetectedNumber_Type=Gauge32
_ExtremeVMDetectedNumber_Object=MibScalar
extremeVMDetectedNumber=_ExtremeVMDetectedNumber_Object((1,3,6,1,4,1,1916,1,39,3,1),_ExtremeVMDetectedNumber_Type())
extremeVMDetectedNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedNumber.setStatus(_A)
_ExtremeVMDetectedTable_Object=MibTable
extremeVMDetectedTable=_ExtremeVMDetectedTable_Object((1,3,6,1,4,1,1916,1,39,3,2))
if mibBuilder.loadTexts:extremeVMDetectedTable.setStatus(_A)
_ExtremeVMDetectedEntry_Object=MibTableRow
extremeVMDetectedEntry=_ExtremeVMDetectedEntry_Object((1,3,6,1,4,1,1916,1,39,3,2,1))
extremeVMDetectedEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:extremeVMDetectedEntry.setStatus(_A)
_ExtremeVMDetectedMAC_Type=MacAddress
_ExtremeVMDetectedMAC_Object=MibTableColumn
extremeVMDetectedMAC=_ExtremeVMDetectedMAC_Object((1,3,6,1,4,1,1916,1,39,3,2,1,1),_ExtremeVMDetectedMAC_Type())
extremeVMDetectedMAC.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMDetectedMAC.setStatus(_A)
class _ExtremeVMDetectedVMName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMDetectedVMName_Type.__name__=_F
_ExtremeVMDetectedVMName_Object=MibTableColumn
extremeVMDetectedVMName=_ExtremeVMDetectedVMName_Object((1,3,6,1,4,1,1916,1,39,3,2,1,2),_ExtremeVMDetectedVMName_Type())
extremeVMDetectedVMName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedVMName.setStatus(_A)
_ExtremeVMDetectedIngressVPPName_Type=DisplayString
_ExtremeVMDetectedIngressVPPName_Object=MibTableColumn
extremeVMDetectedIngressVPPName=_ExtremeVMDetectedIngressVPPName_Object((1,3,6,1,4,1,1916,1,39,3,2,1,3),_ExtremeVMDetectedIngressVPPName_Type())
extremeVMDetectedIngressVPPName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedIngressVPPName.setStatus(_G)
_ExtremeVMDetectedEgressVPPName_Type=DisplayString
_ExtremeVMDetectedEgressVPPName_Object=MibTableColumn
extremeVMDetectedEgressVPPName=_ExtremeVMDetectedEgressVPPName_Object((1,3,6,1,4,1,1916,1,39,3,2,1,4),_ExtremeVMDetectedEgressVPPName_Type())
extremeVMDetectedEgressVPPName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedEgressVPPName.setStatus(_G)
_ExtremeVMDetectedIfIndex_Type=Integer32
_ExtremeVMDetectedIfIndex_Object=MibTableColumn
extremeVMDetectedIfIndex=_ExtremeVMDetectedIfIndex_Object((1,3,6,1,4,1,1916,1,39,3,2,1,5),_ExtremeVMDetectedIfIndex_Type())
extremeVMDetectedIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedIfIndex.setStatus(_A)
class _ExtremeVMDetectedAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_m,1),(_P,2)))
_ExtremeVMDetectedAdminStatus_Type.__name__=_C
_ExtremeVMDetectedAdminStatus_Object=MibTableColumn
extremeVMDetectedAdminStatus=_ExtremeVMDetectedAdminStatus_Object((1,3,6,1,4,1,1916,1,39,3,2,1,6),_ExtremeVMDetectedAdminStatus_Type())
extremeVMDetectedAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeVMDetectedAdminStatus.setStatus(_A)
class _ExtremeVMDetectedOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_m,1),('authenticatedNetwork',2),('authenticatedLocally',3),('authenticationDenied',4),('notAuthenticated',5)))
_ExtremeVMDetectedOperStatus_Type.__name__=_C
_ExtremeVMDetectedOperStatus_Object=MibTableColumn
extremeVMDetectedOperStatus=_ExtremeVMDetectedOperStatus_Object((1,3,6,1,4,1,1916,1,39,3,2,1,7),_ExtremeVMDetectedOperStatus_Type())
extremeVMDetectedOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedOperStatus.setStatus(_A)
class _ExtremeVMDetectedResultIngress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_n,1),(_o,2),(_p,3),(_q,4),(_r,5)))
_ExtremeVMDetectedResultIngress_Type.__name__=_C
_ExtremeVMDetectedResultIngress_Object=MibTableColumn
extremeVMDetectedResultIngress=_ExtremeVMDetectedResultIngress_Object((1,3,6,1,4,1,1916,1,39,3,2,1,8),_ExtremeVMDetectedResultIngress_Type())
extremeVMDetectedResultIngress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedResultIngress.setStatus(_A)
class _ExtremeVMDetectedResultEgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_n,1),(_o,2),(_p,3),(_q,4),(_r,5)))
_ExtremeVMDetectedResultEgress_Type.__name__=_C
_ExtremeVMDetectedResultEgress_Object=MibTableColumn
extremeVMDetectedResultEgress=_ExtremeVMDetectedResultEgress_Object((1,3,6,1,4,1,1916,1,39,3,2,1,9),_ExtremeVMDetectedResultEgress_Type())
extremeVMDetectedResultEgress.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedResultEgress.setStatus(_A)
class _ExtremeVMDetectedIngErrPolicies_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_ExtremeVMDetectedIngErrPolicies_Type.__name__=_N
_ExtremeVMDetectedIngErrPolicies_Object=MibTableColumn
extremeVMDetectedIngErrPolicies=_ExtremeVMDetectedIngErrPolicies_Object((1,3,6,1,4,1,1916,1,39,3,2,1,10),_ExtremeVMDetectedIngErrPolicies_Type())
extremeVMDetectedIngErrPolicies.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedIngErrPolicies.setStatus(_A)
class _ExtremeVMDetectedEgrErrPolicies_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_ExtremeVMDetectedEgrErrPolicies_Type.__name__=_N
_ExtremeVMDetectedEgrErrPolicies_Object=MibTableColumn
extremeVMDetectedEgrErrPolicies=_ExtremeVMDetectedEgrErrPolicies_Object((1,3,6,1,4,1,1916,1,39,3,2,1,11),_ExtremeVMDetectedEgrErrPolicies_Type())
extremeVMDetectedEgrErrPolicies.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedEgrErrPolicies.setStatus(_A)
class _ExtremeVMDetectedVPPName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMDetectedVPPName_Type.__name__=_F
_ExtremeVMDetectedVPPName_Object=MibTableColumn
extremeVMDetectedVPPName=_ExtremeVMDetectedVPPName_Object((1,3,6,1,4,1,1916,1,39,3,2,1,12),_ExtremeVMDetectedVPPName_Type())
extremeVMDetectedVPPName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedVPPName.setStatus(_A)
class _ExtremeVMDetectedVPPResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('vppMapped',1),(_b,2),(_a,3),(_Z,4)))
_ExtremeVMDetectedVPPResult_Type.__name__=_C
_ExtremeVMDetectedVPPResult_Object=MibTableColumn
extremeVMDetectedVPPResult=_ExtremeVMDetectedVPPResult_Object((1,3,6,1,4,1,1916,1,39,3,2,1,13),_ExtremeVMDetectedVPPResult_Type())
extremeVMDetectedVPPResult.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedVPPResult.setStatus(_A)
_ExtremeVMDetectedCounterInstallResult_Type=CounterDirection
_ExtremeVMDetectedCounterInstallResult_Object=MibTableColumn
extremeVMDetectedCounterInstallResult=_ExtremeVMDetectedCounterInstallResult_Object((1,3,6,1,4,1,1916,1,39,3,2,1,14),_ExtremeVMDetectedCounterInstallResult_Type())
extremeVMDetectedCounterInstallResult.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedCounterInstallResult.setStatus(_A)
class _ExtremeVMDetectedVMVLANTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_ExtremeVMDetectedVMVLANTag_Type.__name__=_C
_ExtremeVMDetectedVMVLANTag_Object=MibTableColumn
extremeVMDetectedVMVLANTag=_ExtremeVMDetectedVMVLANTag_Object((1,3,6,1,4,1,1916,1,39,3,2,1,15),_ExtremeVMDetectedVMVLANTag_Type())
extremeVMDetectedVMVLANTag.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedVMVLANTag.setStatus(_A)
class _ExtremeVMDetectedVMVLANVRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ExtremeVMDetectedVMVLANVRName_Type.__name__=_F
_ExtremeVMDetectedVMVLANVRName_Object=MibTableColumn
extremeVMDetectedVMVLANVRName=_ExtremeVMDetectedVMVLANVRName_Object((1,3,6,1,4,1,1916,1,39,3,2,1,16),_ExtremeVMDetectedVMVLANVRName_Type())
extremeVMDetectedVMVLANVRName.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeVMDetectedVMVLANVRName.setStatus(_A)
_ExtremeVMNotificationObjects_ObjectIdentity=ObjectIdentity
extremeVMNotificationObjects=_ExtremeVMNotificationObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,39,4))
_ExtremeVMVPPSynchType_Type=VMVPPSynchType
_ExtremeVMVPPSynchType_Object=MibScalar
extremeVMVPPSynchType=_ExtremeVMVPPSynchType_Object((1,3,6,1,4,1,1916,1,39,4,1),_ExtremeVMVPPSynchType_Type())
extremeVMVPPSynchType.setMaxAccess(_I)
if mibBuilder.loadTexts:extremeVMVPPSynchType.setStatus(_A)
_ExtremeVMNotifications_ObjectIdentity=ObjectIdentity
extremeVMNotifications=_ExtremeVMNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,39,5))
_ExtremeVMNotificationPrefix_ObjectIdentity=ObjectIdentity
extremeVMNotificationPrefix=_ExtremeVMNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,39,5,0))
extremeVMVPPSyncFailed=NotificationType((1,3,6,1,4,1,1916,1,39,5,0,1))
extremeVMVPPSyncFailed.setObjects(*((_B,_s),(_B,_t),(_B,_O),(_B,_u),(_B,_K),(_B,_v)))
if mibBuilder.loadTexts:extremeVMVPPSyncFailed.setStatus(_A)
extremeVMVPPInvalid=NotificationType((1,3,6,1,4,1,1916,1,39,5,0,2))
extremeVMVPPInvalid.setObjects(*((_B,_Q),(_B,_K)))
if mibBuilder.loadTexts:extremeVMVPPInvalid.setStatus(_A)
extremeVMMapped=NotificationType((1,3,6,1,4,1,1916,1,39,5,0,3))
extremeVMMapped.setObjects(*((_B,_L),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:extremeVMMapped.setStatus(_A)
extremeVMUnMapped=NotificationType((1,3,6,1,4,1,1916,1,39,5,0,4))
extremeVMUnMapped.setObjects(*((_B,_L),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:extremeVMUnMapped.setStatus(_A)
extremeVMDetectResult=NotificationType((1,3,6,1,4,1,1916,1,39,5,0,5))
extremeVMDetectResult.setObjects(*((_B,_M),(_B,_U),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:extremeVMDetectResult.setStatus(_A)
extremeVMUnDetectResult=NotificationType((1,3,6,1,4,1,1916,1,39,5,0,6))
extremeVMUnDetectResult.setObjects(*((_B,_M),(_B,_U)))
if mibBuilder.loadTexts:extremeVMUnDetectResult.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VMVPPSynchType':VMVPPSynchType,'CounterDirection':CounterDirection,'extremeVM':extremeVM,'extremeVMGeneral':extremeVMGeneral,'extremeVMFTPServerTable':extremeVMFTPServerTable,'extremeVMFTPServerEntry':extremeVMFTPServerEntry,_O:extremeVMFTPServerType,_t:extremeVMFTPAddrType,_s:extremeVMFTPServer,'extremeVMFTPSynchInterval':extremeVMFTPSynchInterval,'extremeVMFTPRowStatus':extremeVMFTPRowStatus,'extremeVMFTPPathName':extremeVMFTPPathName,'extremeVMFTPUsername':extremeVMFTPUsername,'extremeVMFTPPassword':extremeVMFTPPassword,'extremeVMFTPPolicyDir':extremeVMFTPPolicyDir,'extremeVMLastSynch':extremeVMLastSynch,_u:extremeVMLastSynchStatus,'extremeVMSynchAdminState':extremeVMSynchAdminState,'extremeVMSynchOperState':extremeVMSynchOperState,'extremeVMTrackingEnabled':extremeVMTrackingEnabled,'extremeVMPortConfigTable':extremeVMPortConfigTable,'extremeVMPortConfigEntry':extremeVMPortConfigEntry,_W:extremeVMPortConfigIfIndex,'extremeVMPortConfigVMTrackingEnabled':extremeVMPortConfigVMTrackingEnabled,'extremeVMPortConfigVMTrackingDynVlanEnabled':extremeVMPortConfigVMTrackingDynVlanEnabled,'extremeVMVPP':extremeVMVPP,'extremeVMVPPTable':extremeVMVPPTable,'extremeVMVPPEntry':extremeVMVPPEntry,_Q:extremeVMVPPType,_K:extremeVMVPPName,'extremeVMVPPControl':extremeVMVPPControl,'extremeVMVPPRowStatus':extremeVMVPPRowStatus,'extremeVMVPPCounter':extremeVMVPPCounter,'extremeVMVPPVLANTag':extremeVMVPPVLANTag,'extremeVMVPPVLANVRName':extremeVMVPPVLANVRName,'extremeVMMappingTable':extremeVMMappingTable,'extremeVMMappingEntry':extremeVMMappingEntry,_Y:extremeVMMappingType,_L:extremeVMMappingMAC,_R:extremeVMMappingIngressVPPName,_S:extremeVMMappingEgressVPPName,'extremeVMMappingStatus':extremeVMMappingStatus,'extremeVMMappingRowStatus':extremeVMMappingRowStatus,_T:extremeVMMappingVPPName,'extremeVMMappingVLANTag':extremeVMMappingVLANTag,'extremeVMMappingVLANVRName':extremeVMMappingVLANVRName,'extremeVMVPP2PolicyTable':extremeVMVPP2PolicyTable,'extremeVMVPP2PolicyEntry':extremeVMVPP2PolicyEntry,_c:extremeVMVPP2PolicyVPPName,_d:extremeVMVPP2PolicyPolicyName,_e:extremeVMVPP2PolicyType,'extremeVMVPP2PolicyOrder':extremeVMVPP2PolicyOrder,'extremeVMVPP2PolicyRowStatus':extremeVMVPP2PolicyRowStatus,'extremeVMVPPDetailTable':extremeVMVPPDetailTable,'extremeVMVPPDetailEntry':extremeVMVPPDetailEntry,_h:extremeVMVPPDetailVPPName,_i:extremeVMVPPDetailDirection,_j:extremeVMVPPDetailType,_k:extremeVMVPPDetailOrder,_l:extremeVMVPPDetailPolicyName,'extremeVMVPPDetailRowStatus':extremeVMVPPDetailRowStatus,'extremeVMDetected':extremeVMDetected,'extremeVMDetectedNumber':extremeVMDetectedNumber,'extremeVMDetectedTable':extremeVMDetectedTable,'extremeVMDetectedEntry':extremeVMDetectedEntry,_M:extremeVMDetectedMAC,'extremeVMDetectedVMName':extremeVMDetectedVMName,_w:extremeVMDetectedIngressVPPName,_x:extremeVMDetectedEgressVPPName,_U:extremeVMDetectedIfIndex,'extremeVMDetectedAdminStatus':extremeVMDetectedAdminStatus,_A0:extremeVMDetectedOperStatus,_y:extremeVMDetectedResultIngress,_z:extremeVMDetectedResultEgress,_A1:extremeVMDetectedIngErrPolicies,_A2:extremeVMDetectedEgrErrPolicies,_A4:extremeVMDetectedVPPName,_A3:extremeVMDetectedVPPResult,_A5:extremeVMDetectedCounterInstallResult,'extremeVMDetectedVMVLANTag':extremeVMDetectedVMVLANTag,'extremeVMDetectedVMVLANVRName':extremeVMDetectedVMVLANVRName,'extremeVMNotificationObjects':extremeVMNotificationObjects,_v:extremeVMVPPSynchType,'extremeVMNotifications':extremeVMNotifications,'extremeVMNotificationPrefix':extremeVMNotificationPrefix,'extremeVMVPPSyncFailed':extremeVMVPPSyncFailed,'extremeVMVPPInvalid':extremeVMVPPInvalid,'extremeVMMapped':extremeVMMapped,'extremeVMUnMapped':extremeVMUnMapped,'extremeVMDetectResult':extremeVMDetectResult,'extremeVMUnDetectResult':extremeVMUnDetectResult})