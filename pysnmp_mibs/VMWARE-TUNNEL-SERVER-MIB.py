_AD='vmwTunnelServerStatGroup4'
_AC='vmwTunnelServerStatGroup3'
_AB='vmwTunnelServerStatGroup2'
_AA='vmwTunnelServerStatGroup'
_A9='vmwTunnelServerInfoGroup3'
_A8='vmwTunnelServerInfoGroup2'
_A7='vmwTunnelServerInfoGroup'
_A6='vmwTunnelNumConnBlockedByZTNA'
_A5='vmwTunnelNumDevicesBlockedByAdm'
_A4='vmwTunnelNumDevicesBlockedByZTNA'
_A3='vmwTunnelGeneveMetadata'
_A2='vmwTunnelIsContainer'
_A1='vmwTunnelIsAppliance'
_A0='vmwTunnelNumZTNAPDTR'
_z='vmwTunnelNumZTNADTR'
_y='vmwTunnelZTNAPDTR'
_x='vmwTunnelZTNADTR'
_w='vmwTunnelTLSPortSharing'
_v='vmwTunnelMemoryShared'
_u='vmwTunnelMemoryResident'
_t='vmwTunnelMemoryVirtual'
_s='vmwTunnelNumBackEndsDown'
_r='vmwTunnelNumBackEnds'
_q='vmwTunnelNumConnFailed'
_p='vmwTunnelNumConnSuccessful'
_o='vmwTunnelNumDDoSRejected'
_n='vmwTunnelServerStatus'
_m='vmwTunnelProcessUpTime'
_l='vmwTunnelLogLevel'
_k='vmwTunnelNumNonManaged'
_j='vmwTunnelNumNonCompliant'
_i='vmwTunnelNumNotInAllowlist'
_h='vmwTunnelNSXEnabled'
_g='vmwTunnelFIPSEnabled'
_f='vmwTunnelTrafficRulesEnabled'
_e='vmwTunnelDeploymentMode'
_d='vmwTunnelCascadeMode'
_c='vmwTunnelProcessStartTime'
_b='vmwTunnelAWCMLastSyncTime'
_a='vmwTunnelAPILastSyncTime'
_Z='vmwTunnelAWCMLastResponse'
_Y='vmwTunnelAPILastResponse'
_X='vmwTunnelAWCMConnectivity'
_W='vmwTunnelAPIConnectivity'
_V='vmwTunnelOperatingSystem'
_U='vmwTunnelConsoleVersion'
_T='vmwTunnelServerVersion'
_S='vmwTunnelNumDevicesSinceStart'
_R='vmwTunnelNumFailedHandshakes'
_Q='vmwTunnelNumClosedHandshakes'
_P='vmwTunnelNumAllowListedDevices'
_O='vmwTunnelNumTrafficRules'
_N='vmwTunnelNumProxiesDown'
_M='vmwTunnelNumProxies'
_L='vmwTunnelUpstreamBitRate'
_K='vmwTunnelDownstreamBitRate'
_J='vmwTunnelNumConnectionsPeak'
_I='vmwTunnelNumConnections'
_H='vmwTunnelNumDevicesPeak'
_G='vmwTunnelNumDevices'
_F='Gauge32'
_E='Counter64'
_D='Unsigned32'
_C='read-only'
_B='VMWARE-TUNNEL-SERVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32',_E,_F,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
vmwPerAppTunnel,=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwPerAppTunnel')
VmwLongDisplayString,=mibBuilder.importSymbols('VMWARE-TC-MIB','VmwLongDisplayString')
vmwTunnelServerMIB=ModuleIdentity((1,3,6,1,4,1,6876,130,1))
if mibBuilder.loadTexts:vmwTunnelServerMIB.setRevisions(('2022-10-28 00:00','2020-08-21 00:00','2020-07-21 00:00','2019-10-30 00:00','2018-08-30 00:00'))
class VmwTunnelUpDownState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class VmwTunnelCascadeModeState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('frontend',2),('backend',3)))
class VmwTunnelLogState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('off',0),('error',1),('warning',2),('info',3),('debug',4)))
_VmwTunnelServerStat_ObjectIdentity=ObjectIdentity
vmwTunnelServerStat=_VmwTunnelServerStat_ObjectIdentity((1,3,6,1,4,1,6876,130,1,1))
class _VmwTunnelNumDevices_Type(Gauge32):defaultValue=0
_VmwTunnelNumDevices_Type.__name__=_F
_VmwTunnelNumDevices_Object=MibScalar
vmwTunnelNumDevices=_VmwTunnelNumDevices_Object((1,3,6,1,4,1,6876,130,1,1,1),_VmwTunnelNumDevices_Type())
vmwTunnelNumDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumDevices.setStatus(_A)
class _VmwTunnelNumDevicesPeak_Type(Unsigned32):defaultValue=0
_VmwTunnelNumDevicesPeak_Type.__name__=_D
_VmwTunnelNumDevicesPeak_Object=MibScalar
vmwTunnelNumDevicesPeak=_VmwTunnelNumDevicesPeak_Object((1,3,6,1,4,1,6876,130,1,1,2),_VmwTunnelNumDevicesPeak_Type())
vmwTunnelNumDevicesPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumDevicesPeak.setStatus(_A)
class _VmwTunnelNumConnections_Type(Gauge32):defaultValue=0
_VmwTunnelNumConnections_Type.__name__=_F
_VmwTunnelNumConnections_Object=MibScalar
vmwTunnelNumConnections=_VmwTunnelNumConnections_Object((1,3,6,1,4,1,6876,130,1,1,3),_VmwTunnelNumConnections_Type())
vmwTunnelNumConnections.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumConnections.setStatus(_A)
class _VmwTunnelNumConnectionsPeak_Type(Unsigned32):defaultValue=0
_VmwTunnelNumConnectionsPeak_Type.__name__=_D
_VmwTunnelNumConnectionsPeak_Object=MibScalar
vmwTunnelNumConnectionsPeak=_VmwTunnelNumConnectionsPeak_Object((1,3,6,1,4,1,6876,130,1,1,4),_VmwTunnelNumConnectionsPeak_Type())
vmwTunnelNumConnectionsPeak.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumConnectionsPeak.setStatus(_A)
_VmwTunnelDownstreamBitRate_Type=Unsigned32
_VmwTunnelDownstreamBitRate_Object=MibScalar
vmwTunnelDownstreamBitRate=_VmwTunnelDownstreamBitRate_Object((1,3,6,1,4,1,6876,130,1,1,20),_VmwTunnelDownstreamBitRate_Type())
vmwTunnelDownstreamBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelDownstreamBitRate.setStatus(_A)
if mibBuilder.loadTexts:vmwTunnelDownstreamBitRate.setUnits('kB/s')
_VmwTunnelUpstreamBitRate_Type=Unsigned32
_VmwTunnelUpstreamBitRate_Object=MibScalar
vmwTunnelUpstreamBitRate=_VmwTunnelUpstreamBitRate_Object((1,3,6,1,4,1,6876,130,1,1,21),_VmwTunnelUpstreamBitRate_Type())
vmwTunnelUpstreamBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelUpstreamBitRate.setStatus(_A)
if mibBuilder.loadTexts:vmwTunnelUpstreamBitRate.setUnits('kB/s')
class _VmwTunnelNumProxies_Type(Unsigned32):defaultValue=0
_VmwTunnelNumProxies_Type.__name__=_D
_VmwTunnelNumProxies_Object=MibScalar
vmwTunnelNumProxies=_VmwTunnelNumProxies_Object((1,3,6,1,4,1,6876,130,1,1,40),_VmwTunnelNumProxies_Type())
vmwTunnelNumProxies.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumProxies.setStatus(_A)
class _VmwTunnelNumProxiesDown_Type(Unsigned32):defaultValue=0
_VmwTunnelNumProxiesDown_Type.__name__=_D
_VmwTunnelNumProxiesDown_Object=MibScalar
vmwTunnelNumProxiesDown=_VmwTunnelNumProxiesDown_Object((1,3,6,1,4,1,6876,130,1,1,41),_VmwTunnelNumProxiesDown_Type())
vmwTunnelNumProxiesDown.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumProxiesDown.setStatus(_A)
class _VmwTunnelNumTrafficRules_Type(Unsigned32):defaultValue=0
_VmwTunnelNumTrafficRules_Type.__name__=_D
_VmwTunnelNumTrafficRules_Object=MibScalar
vmwTunnelNumTrafficRules=_VmwTunnelNumTrafficRules_Object((1,3,6,1,4,1,6876,130,1,1,50),_VmwTunnelNumTrafficRules_Type())
vmwTunnelNumTrafficRules.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumTrafficRules.setStatus(_A)
class _VmwTunnelNumAllowListedDevices_Type(Unsigned32):defaultValue=0
_VmwTunnelNumAllowListedDevices_Type.__name__=_D
_VmwTunnelNumAllowListedDevices_Object=MibScalar
vmwTunnelNumAllowListedDevices=_VmwTunnelNumAllowListedDevices_Object((1,3,6,1,4,1,6876,130,1,1,60),_VmwTunnelNumAllowListedDevices_Type())
vmwTunnelNumAllowListedDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumAllowListedDevices.setStatus(_A)
_VmwTunnelNumClosedHandshakes_Type=Counter64
_VmwTunnelNumClosedHandshakes_Object=MibScalar
vmwTunnelNumClosedHandshakes=_VmwTunnelNumClosedHandshakes_Object((1,3,6,1,4,1,6876,130,1,1,70),_VmwTunnelNumClosedHandshakes_Type())
vmwTunnelNumClosedHandshakes.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumClosedHandshakes.setStatus(_A)
_VmwTunnelNumFailedHandshakes_Type=Counter64
_VmwTunnelNumFailedHandshakes_Object=MibScalar
vmwTunnelNumFailedHandshakes=_VmwTunnelNumFailedHandshakes_Object((1,3,6,1,4,1,6876,130,1,1,71),_VmwTunnelNumFailedHandshakes_Type())
vmwTunnelNumFailedHandshakes.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumFailedHandshakes.setStatus(_A)
_VmwTunnelNumNotInAllowlist_Type=Counter64
_VmwTunnelNumNotInAllowlist_Object=MibScalar
vmwTunnelNumNotInAllowlist=_VmwTunnelNumNotInAllowlist_Object((1,3,6,1,4,1,6876,130,1,1,72),_VmwTunnelNumNotInAllowlist_Type())
vmwTunnelNumNotInAllowlist.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumNotInAllowlist.setStatus(_A)
_VmwTunnelNumNonCompliant_Type=Counter64
_VmwTunnelNumNonCompliant_Object=MibScalar
vmwTunnelNumNonCompliant=_VmwTunnelNumNonCompliant_Object((1,3,6,1,4,1,6876,130,1,1,73),_VmwTunnelNumNonCompliant_Type())
vmwTunnelNumNonCompliant.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumNonCompliant.setStatus(_A)
_VmwTunnelNumNonManaged_Type=Counter64
_VmwTunnelNumNonManaged_Object=MibScalar
vmwTunnelNumNonManaged=_VmwTunnelNumNonManaged_Object((1,3,6,1,4,1,6876,130,1,1,74),_VmwTunnelNumNonManaged_Type())
vmwTunnelNumNonManaged.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumNonManaged.setStatus(_A)
_VmwTunnelNumDDoSRejected_Type=Counter64
_VmwTunnelNumDDoSRejected_Object=MibScalar
vmwTunnelNumDDoSRejected=_VmwTunnelNumDDoSRejected_Object((1,3,6,1,4,1,6876,130,1,1,75),_VmwTunnelNumDDoSRejected_Type())
vmwTunnelNumDDoSRejected.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumDDoSRejected.setStatus(_A)
_VmwTunnelNumDevicesBlockedByZTNA_Type=Counter64
_VmwTunnelNumDevicesBlockedByZTNA_Object=MibScalar
vmwTunnelNumDevicesBlockedByZTNA=_VmwTunnelNumDevicesBlockedByZTNA_Object((1,3,6,1,4,1,6876,130,1,1,76),_VmwTunnelNumDevicesBlockedByZTNA_Type())
vmwTunnelNumDevicesBlockedByZTNA.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumDevicesBlockedByZTNA.setStatus(_A)
_VmwTunnelNumDevicesBlockedByAdm_Type=Counter64
_VmwTunnelNumDevicesBlockedByAdm_Object=MibScalar
vmwTunnelNumDevicesBlockedByAdm=_VmwTunnelNumDevicesBlockedByAdm_Object((1,3,6,1,4,1,6876,130,1,1,77),_VmwTunnelNumDevicesBlockedByAdm_Type())
vmwTunnelNumDevicesBlockedByAdm.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumDevicesBlockedByAdm.setStatus(_A)
_VmwTunnelNumDevicesSinceStart_Type=Counter64
_VmwTunnelNumDevicesSinceStart_Object=MibScalar
vmwTunnelNumDevicesSinceStart=_VmwTunnelNumDevicesSinceStart_Object((1,3,6,1,4,1,6876,130,1,1,80),_VmwTunnelNumDevicesSinceStart_Type())
vmwTunnelNumDevicesSinceStart.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumDevicesSinceStart.setStatus(_A)
_VmwTunnelNumConnSuccessful_Type=Counter64
_VmwTunnelNumConnSuccessful_Object=MibScalar
vmwTunnelNumConnSuccessful=_VmwTunnelNumConnSuccessful_Object((1,3,6,1,4,1,6876,130,1,1,90),_VmwTunnelNumConnSuccessful_Type())
vmwTunnelNumConnSuccessful.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumConnSuccessful.setStatus(_A)
_VmwTunnelNumConnFailed_Type=Counter64
_VmwTunnelNumConnFailed_Object=MibScalar
vmwTunnelNumConnFailed=_VmwTunnelNumConnFailed_Object((1,3,6,1,4,1,6876,130,1,1,91),_VmwTunnelNumConnFailed_Type())
vmwTunnelNumConnFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumConnFailed.setStatus(_A)
_VmwTunnelNumConnBlockedByZTNA_Type=Counter64
_VmwTunnelNumConnBlockedByZTNA_Object=MibScalar
vmwTunnelNumConnBlockedByZTNA=_VmwTunnelNumConnBlockedByZTNA_Object((1,3,6,1,4,1,6876,130,1,1,92),_VmwTunnelNumConnBlockedByZTNA_Type())
vmwTunnelNumConnBlockedByZTNA.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumConnBlockedByZTNA.setStatus(_A)
class _VmwTunnelNumBackEnds_Type(Unsigned32):defaultValue=0
_VmwTunnelNumBackEnds_Type.__name__=_D
_VmwTunnelNumBackEnds_Object=MibScalar
vmwTunnelNumBackEnds=_VmwTunnelNumBackEnds_Object((1,3,6,1,4,1,6876,130,1,1,100),_VmwTunnelNumBackEnds_Type())
vmwTunnelNumBackEnds.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumBackEnds.setStatus(_A)
class _VmwTunnelNumBackEndsDown_Type(Unsigned32):defaultValue=0
_VmwTunnelNumBackEndsDown_Type.__name__=_D
_VmwTunnelNumBackEndsDown_Object=MibScalar
vmwTunnelNumBackEndsDown=_VmwTunnelNumBackEndsDown_Object((1,3,6,1,4,1,6876,130,1,1,101),_VmwTunnelNumBackEndsDown_Type())
vmwTunnelNumBackEndsDown.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumBackEndsDown.setStatus(_A)
class _VmwTunnelMemoryVirtual_Type(Counter64):defaultValue=0
_VmwTunnelMemoryVirtual_Type.__name__=_E
_VmwTunnelMemoryVirtual_Object=MibScalar
vmwTunnelMemoryVirtual=_VmwTunnelMemoryVirtual_Object((1,3,6,1,4,1,6876,130,1,1,110),_VmwTunnelMemoryVirtual_Type())
vmwTunnelMemoryVirtual.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelMemoryVirtual.setStatus(_A)
class _VmwTunnelMemoryResident_Type(Counter64):defaultValue=0
_VmwTunnelMemoryResident_Type.__name__=_E
_VmwTunnelMemoryResident_Object=MibScalar
vmwTunnelMemoryResident=_VmwTunnelMemoryResident_Object((1,3,6,1,4,1,6876,130,1,1,111),_VmwTunnelMemoryResident_Type())
vmwTunnelMemoryResident.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelMemoryResident.setStatus(_A)
class _VmwTunnelMemoryShared_Type(Counter64):defaultValue=0
_VmwTunnelMemoryShared_Type.__name__=_E
_VmwTunnelMemoryShared_Object=MibScalar
vmwTunnelMemoryShared=_VmwTunnelMemoryShared_Object((1,3,6,1,4,1,6876,130,1,1,112),_VmwTunnelMemoryShared_Type())
vmwTunnelMemoryShared.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelMemoryShared.setStatus(_A)
_VmwTunnelServerInfo_ObjectIdentity=ObjectIdentity
vmwTunnelServerInfo=_VmwTunnelServerInfo_ObjectIdentity((1,3,6,1,4,1,6876,130,1,2))
_VmwTunnelServerVersion_Type=VmwLongDisplayString
_VmwTunnelServerVersion_Object=MibScalar
vmwTunnelServerVersion=_VmwTunnelServerVersion_Object((1,3,6,1,4,1,6876,130,1,2,1),_VmwTunnelServerVersion_Type())
vmwTunnelServerVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelServerVersion.setStatus(_A)
_VmwTunnelConsoleVersion_Type=VmwLongDisplayString
_VmwTunnelConsoleVersion_Object=MibScalar
vmwTunnelConsoleVersion=_VmwTunnelConsoleVersion_Object((1,3,6,1,4,1,6876,130,1,2,2),_VmwTunnelConsoleVersion_Type())
vmwTunnelConsoleVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelConsoleVersion.setStatus(_A)
_VmwTunnelOperatingSystem_Type=VmwLongDisplayString
_VmwTunnelOperatingSystem_Object=MibScalar
vmwTunnelOperatingSystem=_VmwTunnelOperatingSystem_Object((1,3,6,1,4,1,6876,130,1,2,3),_VmwTunnelOperatingSystem_Type())
vmwTunnelOperatingSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelOperatingSystem.setStatus(_A)
_VmwTunnelAPIConnectivity_Type=VmwTunnelUpDownState
_VmwTunnelAPIConnectivity_Object=MibScalar
vmwTunnelAPIConnectivity=_VmwTunnelAPIConnectivity_Object((1,3,6,1,4,1,6876,130,1,2,10),_VmwTunnelAPIConnectivity_Type())
vmwTunnelAPIConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelAPIConnectivity.setStatus(_A)
_VmwTunnelAWCMConnectivity_Type=VmwTunnelUpDownState
_VmwTunnelAWCMConnectivity_Object=MibScalar
vmwTunnelAWCMConnectivity=_VmwTunnelAWCMConnectivity_Object((1,3,6,1,4,1,6876,130,1,2,11),_VmwTunnelAWCMConnectivity_Type())
vmwTunnelAWCMConnectivity.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelAWCMConnectivity.setStatus(_A)
_VmwTunnelAPILastResponse_Type=VmwLongDisplayString
_VmwTunnelAPILastResponse_Object=MibScalar
vmwTunnelAPILastResponse=_VmwTunnelAPILastResponse_Object((1,3,6,1,4,1,6876,130,1,2,12),_VmwTunnelAPILastResponse_Type())
vmwTunnelAPILastResponse.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelAPILastResponse.setStatus(_A)
_VmwTunnelAWCMLastResponse_Type=VmwLongDisplayString
_VmwTunnelAWCMLastResponse_Object=MibScalar
vmwTunnelAWCMLastResponse=_VmwTunnelAWCMLastResponse_Object((1,3,6,1,4,1,6876,130,1,2,13),_VmwTunnelAWCMLastResponse_Type())
vmwTunnelAWCMLastResponse.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelAWCMLastResponse.setStatus(_A)
_VmwTunnelAPILastSyncTime_Type=DateAndTime
_VmwTunnelAPILastSyncTime_Object=MibScalar
vmwTunnelAPILastSyncTime=_VmwTunnelAPILastSyncTime_Object((1,3,6,1,4,1,6876,130,1,2,14),_VmwTunnelAPILastSyncTime_Type())
vmwTunnelAPILastSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelAPILastSyncTime.setStatus(_A)
_VmwTunnelAWCMLastSyncTime_Type=DateAndTime
_VmwTunnelAWCMLastSyncTime_Object=MibScalar
vmwTunnelAWCMLastSyncTime=_VmwTunnelAWCMLastSyncTime_Object((1,3,6,1,4,1,6876,130,1,2,15),_VmwTunnelAWCMLastSyncTime_Type())
vmwTunnelAWCMLastSyncTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelAWCMLastSyncTime.setStatus(_A)
_VmwTunnelProcessStartTime_Type=DateAndTime
_VmwTunnelProcessStartTime_Object=MibScalar
vmwTunnelProcessStartTime=_VmwTunnelProcessStartTime_Object((1,3,6,1,4,1,6876,130,1,2,20),_VmwTunnelProcessStartTime_Type())
vmwTunnelProcessStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelProcessStartTime.setStatus(_A)
_VmwTunnelProcessUpTime_Type=Counter64
_VmwTunnelProcessUpTime_Object=MibScalar
vmwTunnelProcessUpTime=_VmwTunnelProcessUpTime_Object((1,3,6,1,4,1,6876,130,1,2,21),_VmwTunnelProcessUpTime_Type())
vmwTunnelProcessUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelProcessUpTime.setStatus(_A)
_VmwTunnelCascadeMode_Type=VmwTunnelCascadeModeState
_VmwTunnelCascadeMode_Object=MibScalar
vmwTunnelCascadeMode=_VmwTunnelCascadeMode_Object((1,3,6,1,4,1,6876,130,1,2,30),_VmwTunnelCascadeMode_Type())
vmwTunnelCascadeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelCascadeMode.setStatus(_A)
_VmwTunnelDeploymentMode_Type=VmwLongDisplayString
_VmwTunnelDeploymentMode_Object=MibScalar
vmwTunnelDeploymentMode=_VmwTunnelDeploymentMode_Object((1,3,6,1,4,1,6876,130,1,2,40),_VmwTunnelDeploymentMode_Type())
vmwTunnelDeploymentMode.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelDeploymentMode.setStatus(_A)
_VmwTunnelTrafficRulesEnabled_Type=TruthValue
_VmwTunnelTrafficRulesEnabled_Object=MibScalar
vmwTunnelTrafficRulesEnabled=_VmwTunnelTrafficRulesEnabled_Object((1,3,6,1,4,1,6876,130,1,2,50),_VmwTunnelTrafficRulesEnabled_Type())
vmwTunnelTrafficRulesEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelTrafficRulesEnabled.setStatus(_A)
_VmwTunnelFIPSEnabled_Type=TruthValue
_VmwTunnelFIPSEnabled_Object=MibScalar
vmwTunnelFIPSEnabled=_VmwTunnelFIPSEnabled_Object((1,3,6,1,4,1,6876,130,1,2,60),_VmwTunnelFIPSEnabled_Type())
vmwTunnelFIPSEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelFIPSEnabled.setStatus(_A)
_VmwTunnelNSXEnabled_Type=TruthValue
_VmwTunnelNSXEnabled_Object=MibScalar
vmwTunnelNSXEnabled=_VmwTunnelNSXEnabled_Object((1,3,6,1,4,1,6876,130,1,2,70),_VmwTunnelNSXEnabled_Type())
vmwTunnelNSXEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNSXEnabled.setStatus(_A)
_VmwTunnelLogLevel_Type=VmwTunnelLogState
_VmwTunnelLogLevel_Object=MibScalar
vmwTunnelLogLevel=_VmwTunnelLogLevel_Object((1,3,6,1,4,1,6876,130,1,2,80),_VmwTunnelLogLevel_Type())
vmwTunnelLogLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelLogLevel.setStatus(_A)
_VmwTunnelServerStatus_Type=VmwTunnelUpDownState
_VmwTunnelServerStatus_Object=MibScalar
vmwTunnelServerStatus=_VmwTunnelServerStatus_Object((1,3,6,1,4,1,6876,130,1,2,90),_VmwTunnelServerStatus_Type())
vmwTunnelServerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelServerStatus.setStatus(_A)
_VmwTunnelTLSPortSharing_Type=TruthValue
_VmwTunnelTLSPortSharing_Object=MibScalar
vmwTunnelTLSPortSharing=_VmwTunnelTLSPortSharing_Object((1,3,6,1,4,1,6876,130,1,2,100),_VmwTunnelTLSPortSharing_Type())
vmwTunnelTLSPortSharing.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelTLSPortSharing.setStatus(_A)
_VmwTunnelZTNADTR_Type=TruthValue
_VmwTunnelZTNADTR_Object=MibScalar
vmwTunnelZTNADTR=_VmwTunnelZTNADTR_Object((1,3,6,1,4,1,6876,130,1,2,110),_VmwTunnelZTNADTR_Type())
vmwTunnelZTNADTR.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelZTNADTR.setStatus(_A)
_VmwTunnelZTNAPDTR_Type=TruthValue
_VmwTunnelZTNAPDTR_Object=MibScalar
vmwTunnelZTNAPDTR=_VmwTunnelZTNAPDTR_Object((1,3,6,1,4,1,6876,130,1,2,111),_VmwTunnelZTNAPDTR_Type())
vmwTunnelZTNAPDTR.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelZTNAPDTR.setStatus(_A)
_VmwTunnelNumZTNADTR_Type=Unsigned32
_VmwTunnelNumZTNADTR_Object=MibScalar
vmwTunnelNumZTNADTR=_VmwTunnelNumZTNADTR_Object((1,3,6,1,4,1,6876,130,1,2,112),_VmwTunnelNumZTNADTR_Type())
vmwTunnelNumZTNADTR.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumZTNADTR.setStatus(_A)
_VmwTunnelNumZTNAPDTR_Type=Unsigned32
_VmwTunnelNumZTNAPDTR_Object=MibScalar
vmwTunnelNumZTNAPDTR=_VmwTunnelNumZTNAPDTR_Object((1,3,6,1,4,1,6876,130,1,2,113),_VmwTunnelNumZTNAPDTR_Type())
vmwTunnelNumZTNAPDTR.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelNumZTNAPDTR.setStatus(_A)
_VmwTunnelIsAppliance_Type=TruthValue
_VmwTunnelIsAppliance_Object=MibScalar
vmwTunnelIsAppliance=_VmwTunnelIsAppliance_Object((1,3,6,1,4,1,6876,130,1,2,120),_VmwTunnelIsAppliance_Type())
vmwTunnelIsAppliance.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelIsAppliance.setStatus(_A)
_VmwTunnelIsContainer_Type=TruthValue
_VmwTunnelIsContainer_Object=MibScalar
vmwTunnelIsContainer=_VmwTunnelIsContainer_Object((1,3,6,1,4,1,6876,130,1,2,130),_VmwTunnelIsContainer_Type())
vmwTunnelIsContainer.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelIsContainer.setStatus(_A)
_VmwTunnelGeneveMetadata_Type=TruthValue
_VmwTunnelGeneveMetadata_Object=MibScalar
vmwTunnelGeneveMetadata=_VmwTunnelGeneveMetadata_Object((1,3,6,1,4,1,6876,130,1,2,140),_VmwTunnelGeneveMetadata_Type())
vmwTunnelGeneveMetadata.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwTunnelGeneveMetadata.setStatus(_A)
_VmwTunnelServerMIBConformance_ObjectIdentity=ObjectIdentity
vmwTunnelServerMIBConformance=_VmwTunnelServerMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,130,1,3))
_VmwTunnelServerMIBCompliances_ObjectIdentity=ObjectIdentity
vmwTunnelServerMIBCompliances=_VmwTunnelServerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,130,1,3,1))
_VmwTunnelServerMIBGroups_ObjectIdentity=ObjectIdentity
vmwTunnelServerMIBGroups=_VmwTunnelServerMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,130,1,3,2))
vmwTunnelServerStatGroup=ObjectGroup((1,3,6,1,4,1,6876,130,1,3,2,1))
vmwTunnelServerStatGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:vmwTunnelServerStatGroup.setStatus(_A)
vmwTunnelServerInfoGroup=ObjectGroup((1,3,6,1,4,1,6876,130,1,3,2,2))
vmwTunnelServerInfoGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:vmwTunnelServerInfoGroup.setStatus(_A)
vmwTunnelServerStatGroup2=ObjectGroup((1,3,6,1,4,1,6876,130,1,3,2,3))
vmwTunnelServerStatGroup2.setObjects(*((_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:vmwTunnelServerStatGroup2.setStatus(_A)
vmwTunnelServerInfoGroup2=ObjectGroup((1,3,6,1,4,1,6876,130,1,3,2,4))
vmwTunnelServerInfoGroup2.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:vmwTunnelServerInfoGroup2.setStatus(_A)
vmwTunnelServerStatGroup3=ObjectGroup((1,3,6,1,4,1,6876,130,1,3,2,5))
vmwTunnelServerStatGroup3.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:vmwTunnelServerStatGroup3.setStatus(_A)
vmwTunnelServerInfoGroup3=ObjectGroup((1,3,6,1,4,1,6876,130,1,3,2,6))
vmwTunnelServerInfoGroup3.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:vmwTunnelServerInfoGroup3.setStatus(_A)
vmwTunnelServerStatGroup4=ObjectGroup((1,3,6,1,4,1,6876,130,1,3,2,7))
vmwTunnelServerStatGroup4.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:vmwTunnelServerStatGroup4.setStatus(_A)
vmwTunnelServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6876,130,1,3,1,1))
vmwTunnelServerMIBCompliance.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:vmwTunnelServerMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VmwTunnelUpDownState':VmwTunnelUpDownState,'VmwTunnelCascadeModeState':VmwTunnelCascadeModeState,'VmwTunnelLogState':VmwTunnelLogState,'vmwTunnelServerMIB':vmwTunnelServerMIB,'vmwTunnelServerStat':vmwTunnelServerStat,_G:vmwTunnelNumDevices,_H:vmwTunnelNumDevicesPeak,_I:vmwTunnelNumConnections,_J:vmwTunnelNumConnectionsPeak,_K:vmwTunnelDownstreamBitRate,_L:vmwTunnelUpstreamBitRate,_M:vmwTunnelNumProxies,_N:vmwTunnelNumProxiesDown,_O:vmwTunnelNumTrafficRules,_P:vmwTunnelNumAllowListedDevices,_Q:vmwTunnelNumClosedHandshakes,_R:vmwTunnelNumFailedHandshakes,_i:vmwTunnelNumNotInAllowlist,_j:vmwTunnelNumNonCompliant,_k:vmwTunnelNumNonManaged,_o:vmwTunnelNumDDoSRejected,_A4:vmwTunnelNumDevicesBlockedByZTNA,_A5:vmwTunnelNumDevicesBlockedByAdm,_S:vmwTunnelNumDevicesSinceStart,_p:vmwTunnelNumConnSuccessful,_q:vmwTunnelNumConnFailed,_A6:vmwTunnelNumConnBlockedByZTNA,_r:vmwTunnelNumBackEnds,_s:vmwTunnelNumBackEndsDown,_t:vmwTunnelMemoryVirtual,_u:vmwTunnelMemoryResident,_v:vmwTunnelMemoryShared,'vmwTunnelServerInfo':vmwTunnelServerInfo,_T:vmwTunnelServerVersion,_U:vmwTunnelConsoleVersion,_V:vmwTunnelOperatingSystem,_W:vmwTunnelAPIConnectivity,_X:vmwTunnelAWCMConnectivity,_Y:vmwTunnelAPILastResponse,_Z:vmwTunnelAWCMLastResponse,_a:vmwTunnelAPILastSyncTime,_b:vmwTunnelAWCMLastSyncTime,_c:vmwTunnelProcessStartTime,_m:vmwTunnelProcessUpTime,_d:vmwTunnelCascadeMode,_e:vmwTunnelDeploymentMode,_f:vmwTunnelTrafficRulesEnabled,_g:vmwTunnelFIPSEnabled,_h:vmwTunnelNSXEnabled,_l:vmwTunnelLogLevel,_n:vmwTunnelServerStatus,_w:vmwTunnelTLSPortSharing,_x:vmwTunnelZTNADTR,_y:vmwTunnelZTNAPDTR,_z:vmwTunnelNumZTNADTR,_A0:vmwTunnelNumZTNAPDTR,_A1:vmwTunnelIsAppliance,_A2:vmwTunnelIsContainer,_A3:vmwTunnelGeneveMetadata,'vmwTunnelServerMIBConformance':vmwTunnelServerMIBConformance,'vmwTunnelServerMIBCompliances':vmwTunnelServerMIBCompliances,'vmwTunnelServerMIBCompliance':vmwTunnelServerMIBCompliance,'vmwTunnelServerMIBGroups':vmwTunnelServerMIBGroups,_AA:vmwTunnelServerStatGroup,_A7:vmwTunnelServerInfoGroup,_AB:vmwTunnelServerStatGroup2,_A8:vmwTunnelServerInfoGroup2,_AC:vmwTunnelServerStatGroup3,_A9:vmwTunnelServerInfoGroup3,_AD:vmwTunnelServerStatGroup4})