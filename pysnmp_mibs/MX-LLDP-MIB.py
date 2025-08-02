_K='disable'
_J='unknown'
_I='remoteMediaPolicyStateAppType'
_H='MX-LLDP-MIB'
_G='MxEnableState'
_F='OctetString'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixServices,=mibBuilder.importSymbols('MX-SMI2','mediatrixServices')
MxActivationState,MxAdvancedIpPort,MxDigitMap,MxEnableState,MxIpAddress,MxIpHostName,MxIpPort,MxIpSubnetMask=mibBuilder.importSymbols('MX-TC','MxActivationState','MxAdvancedIpPort','MxDigitMap',_G,'MxIpAddress','MxIpHostName','MxIpPort','MxIpSubnetMask')
MxFloat32,MxIpAddr,MxIpAddrMask,MxIpAddrPort,MxIpHostNamePort,MxUInt64,MxUri,MxUrl=mibBuilder.importSymbols('MX-TC2','MxFloat32','MxIpAddr','MxIpAddrMask','MxIpAddrPort','MxIpHostNamePort','MxUInt64','MxUri','MxUrl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lldpMIB=ModuleIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4100))
_LldpMIBObjects_ObjectIdentity=ObjectIdentity
lldpMIBObjects=_LldpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4100,1))
_StatusGroup_ObjectIdentity=ObjectIdentity
statusGroup=_StatusGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100))
_RemoteMediaPolicyStateTable_Object=MibTable
remoteMediaPolicyStateTable=_RemoteMediaPolicyStateTable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100))
if mibBuilder.loadTexts:remoteMediaPolicyStateTable.setStatus(_A)
_RemoteMediaPolicyStateEntry_Object=MibTableRow
remoteMediaPolicyStateEntry=_RemoteMediaPolicyStateEntry_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100,1))
remoteMediaPolicyStateEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:remoteMediaPolicyStateEntry.setStatus(_A)
class _RemoteMediaPolicyStateAppType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,0),('voice',1),('voiceSignaling',2),('guestVoice',3),('guestVoiceSignaling',4),('softPhoneVoice',5),('videoConferencing',6),('streamingVideo',7),('videoSignaling',8)))
_RemoteMediaPolicyStateAppType_Type.__name__=_B
_RemoteMediaPolicyStateAppType_Object=MibTableColumn
remoteMediaPolicyStateAppType=_RemoteMediaPolicyStateAppType_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100,1,100),_RemoteMediaPolicyStateAppType_Type())
remoteMediaPolicyStateAppType.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteMediaPolicyStateAppType.setStatus(_A)
class _RemoteMediaPolicyStateVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_RemoteMediaPolicyStateVlanId_Type.__name__=_E
_RemoteMediaPolicyStateVlanId_Object=MibTableColumn
remoteMediaPolicyStateVlanId=_RemoteMediaPolicyStateVlanId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100,1,200),_RemoteMediaPolicyStateVlanId_Type())
remoteMediaPolicyStateVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteMediaPolicyStateVlanId.setStatus(_A)
class _RemoteMediaPolicyStatePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RemoteMediaPolicyStatePriority_Type.__name__=_E
_RemoteMediaPolicyStatePriority_Object=MibTableColumn
remoteMediaPolicyStatePriority=_RemoteMediaPolicyStatePriority_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100,1,300),_RemoteMediaPolicyStatePriority_Type())
remoteMediaPolicyStatePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteMediaPolicyStatePriority.setStatus(_A)
class _RemoteMediaPolicyStateDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RemoteMediaPolicyStateDscp_Type.__name__=_E
_RemoteMediaPolicyStateDscp_Object=MibTableColumn
remoteMediaPolicyStateDscp=_RemoteMediaPolicyStateDscp_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100,1,400),_RemoteMediaPolicyStateDscp_Type())
remoteMediaPolicyStateDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteMediaPolicyStateDscp.setStatus(_A)
class _RemoteMediaPolicyStatePolicyFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('defined',100),(_J,200)))
_RemoteMediaPolicyStatePolicyFlag_Type.__name__=_B
_RemoteMediaPolicyStatePolicyFlag_Object=MibTableColumn
remoteMediaPolicyStatePolicyFlag=_RemoteMediaPolicyStatePolicyFlag_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100,1,500),_RemoteMediaPolicyStatePolicyFlag_Type())
remoteMediaPolicyStatePolicyFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteMediaPolicyStatePolicyFlag.setStatus(_A)
class _RemoteMediaPolicyStateTaggedFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('untagged',100),('tagged',200)))
_RemoteMediaPolicyStateTaggedFlag_Type.__name__=_B
_RemoteMediaPolicyStateTaggedFlag_Object=MibTableColumn
remoteMediaPolicyStateTaggedFlag=_RemoteMediaPolicyStateTaggedFlag_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,100,100,1,600),_RemoteMediaPolicyStateTaggedFlag_Type())
remoteMediaPolicyStateTaggedFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:remoteMediaPolicyStateTaggedFlag.setStatus(_A)
class _NetworkInterface_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NetworkInterface_Type.__name__=_F
_NetworkInterface_Object=MibScalar
networkInterface=_NetworkInterface_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,200),_NetworkInterface_Type())
networkInterface.setMaxAccess(_D)
if mibBuilder.loadTexts:networkInterface.setStatus(_A)
class _ChassisId_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*(('macAddress',100),('networkAddress',200)))
_ChassisId_Type.__name__=_B
_ChassisId_Object=MibScalar
chassisId=_ChassisId_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,300),_ChassisId_Type())
chassisId.setMaxAccess(_D)
if mibBuilder.loadTexts:chassisId.setStatus(_A)
class _OverrideNetworkPolicyEnable_Type(MxEnableState):defaultValue=0
_OverrideNetworkPolicyEnable_Type.__name__=_G
_OverrideNetworkPolicyEnable_Object=MibScalar
overrideNetworkPolicyEnable=_OverrideNetworkPolicyEnable_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,400),_OverrideNetworkPolicyEnable_Type())
overrideNetworkPolicyEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:overrideNetworkPolicyEnable.setStatus(_A)
class _OverrideNetworkPolicyRefresh_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(100,200)));namedValues=NamedValues(*((_K,100),('onNetworkPolicyChanges',200)))
_OverrideNetworkPolicyRefresh_Type.__name__=_B
_OverrideNetworkPolicyRefresh_Object=MibScalar
overrideNetworkPolicyRefresh=_OverrideNetworkPolicyRefresh_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,410),_OverrideNetworkPolicyRefresh_Type())
overrideNetworkPolicyRefresh.setMaxAccess(_D)
if mibBuilder.loadTexts:overrideNetworkPolicyRefresh.setStatus(_A)
_NotificationsGroup_ObjectIdentity=ObjectIdentity
notificationsGroup=_NotificationsGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,60010))
class _MinSeverity_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100,200,300,400,500)));namedValues=NamedValues(*((_K,0),('debug',100),('info',200),('warning',300),('error',400),('critical',500)))
_MinSeverity_Type.__name__=_B
_MinSeverity_Object=MibScalar
minSeverity=_MinSeverity_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,60010,100),_MinSeverity_Type())
minSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:minSeverity.setStatus(_A)
_ConfigurationGroup_ObjectIdentity=ObjectIdentity
configurationGroup=_ConfigurationGroup_ObjectIdentity((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,60020))
class _NeedRestartInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,100)));namedValues=NamedValues(*(('no',0),('yes',100)))
_NeedRestartInfo_Type.__name__=_B
_NeedRestartInfo_Object=MibScalar
needRestartInfo=_NeedRestartInfo_Object((1,3,6,1,4,1,4935,1000,100,200,100,4100,1,60020,100),_NeedRestartInfo_Type())
needRestartInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:needRestartInfo.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'lldpMIB':lldpMIB,'lldpMIBObjects':lldpMIBObjects,'statusGroup':statusGroup,'remoteMediaPolicyStateTable':remoteMediaPolicyStateTable,'remoteMediaPolicyStateEntry':remoteMediaPolicyStateEntry,_I:remoteMediaPolicyStateAppType,'remoteMediaPolicyStateVlanId':remoteMediaPolicyStateVlanId,'remoteMediaPolicyStatePriority':remoteMediaPolicyStatePriority,'remoteMediaPolicyStateDscp':remoteMediaPolicyStateDscp,'remoteMediaPolicyStatePolicyFlag':remoteMediaPolicyStatePolicyFlag,'remoteMediaPolicyStateTaggedFlag':remoteMediaPolicyStateTaggedFlag,'networkInterface':networkInterface,'chassisId':chassisId,'overrideNetworkPolicyEnable':overrideNetworkPolicyEnable,'overrideNetworkPolicyRefresh':overrideNetworkPolicyRefresh,'notificationsGroup':notificationsGroup,'minSeverity':minSeverity,'configurationGroup':configurationGroup,'needRestartInfo':needRestartInfo})