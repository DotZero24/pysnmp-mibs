_G='logUtilization'
_F='ramUtilization'
_E='cpuUtilization'
_D='currentlyLoggedIn'
_C='SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sonicwallSMAAppliance,=mibBuilder.importSymbols('SONICWALL-SMA-MIB','sonicwallSMAAppliance')
sonicwallSystemHealth=ModuleIdentity((1,3,6,1,4,1,8741,8,1,2))
_AuthenticatedUsers_ObjectIdentity=ObjectIdentity
authenticatedUsers=_AuthenticatedUsers_ObjectIdentity((1,3,6,1,4,1,8741,8,1,2,1))
_CurrentlyLoggedIn_Type=Integer32
_CurrentlyLoggedIn_Object=MibScalar
currentlyLoggedIn=_CurrentlyLoggedIn_Object((1,3,6,1,4,1,8741,8,1,2,1,1),_CurrentlyLoggedIn_Type())
currentlyLoggedIn.setMaxAccess(_B)
if mibBuilder.loadTexts:currentlyLoggedIn.setStatus(_A)
_PeakLoggedIn_Type=Integer32
_PeakLoggedIn_Object=MibScalar
peakLoggedIn=_PeakLoggedIn_Object((1,3,6,1,4,1,8741,8,1,2,1,2),_PeakLoggedIn_Type())
peakLoggedIn.setMaxAccess(_B)
if mibBuilder.loadTexts:peakLoggedIn.setStatus(_A)
_MaximumlicensedUsers_Type=Integer32
_MaximumlicensedUsers_Object=MibScalar
maximumlicensedUsers=_MaximumlicensedUsers_Object((1,3,6,1,4,1,8741,8,1,2,1,3),_MaximumlicensedUsers_Type())
maximumlicensedUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:maximumlicensedUsers.setStatus(_A)
_ConnectionUtilization_ObjectIdentity=ObjectIdentity
connectionUtilization=_ConnectionUtilization_ObjectIdentity((1,3,6,1,4,1,8741,8,1,2,2))
_CurrentConnections_Type=Integer32
_CurrentConnections_Object=MibScalar
currentConnections=_CurrentConnections_Object((1,3,6,1,4,1,8741,8,1,2,2,1),_CurrentConnections_Type())
currentConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:currentConnections.setStatus(_A)
_PeakConnections_Type=Integer32
_PeakConnections_Object=MibScalar
peakConnections=_PeakConnections_Object((1,3,6,1,4,1,8741,8,1,2,2,2),_PeakConnections_Type())
peakConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:peakConnections.setStatus(_A)
_CpuUtilization_Type=Integer32
_CpuUtilization_Object=MibScalar
cpuUtilization=_CpuUtilization_Object((1,3,6,1,4,1,8741,8,1,2,3),_CpuUtilization_Type())
cpuUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUtilization.setStatus(_A)
_MemoryTotalUtilization_ObjectIdentity=ObjectIdentity
memoryTotalUtilization=_MemoryTotalUtilization_ObjectIdentity((1,3,6,1,4,1,8741,8,1,2,4))
_RamUtilization_Type=Integer32
_RamUtilization_Object=MibScalar
ramUtilization=_RamUtilization_Object((1,3,6,1,4,1,8741,8,1,2,4,1),_RamUtilization_Type())
ramUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:ramUtilization.setStatus(_A)
_SwapUtilization_Type=Integer32
_SwapUtilization_Object=MibScalar
swapUtilization=_SwapUtilization_Object((1,3,6,1,4,1,8741,8,1,2,4,2),_SwapUtilization_Type())
swapUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:swapUtilization.setStatus(_A)
_BandwidthUtilization_ObjectIdentity=ObjectIdentity
bandwidthUtilization=_BandwidthUtilization_ObjectIdentity((1,3,6,1,4,1,8741,8,1,2,5))
_InternalInterfaceCurrentThroughput_Type=Integer32
_InternalInterfaceCurrentThroughput_Object=MibScalar
internalInterfaceCurrentThroughput=_InternalInterfaceCurrentThroughput_Object((1,3,6,1,4,1,8741,8,1,2,5,1),_InternalInterfaceCurrentThroughput_Type())
internalInterfaceCurrentThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:internalInterfaceCurrentThroughput.setStatus(_A)
_InternalInterfacePeakThroughput_Type=Integer32
_InternalInterfacePeakThroughput_Object=MibScalar
internalInterfacePeakThroughput=_InternalInterfacePeakThroughput_Object((1,3,6,1,4,1,8741,8,1,2,5,2),_InternalInterfacePeakThroughput_Type())
internalInterfacePeakThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:internalInterfacePeakThroughput.setStatus(_A)
_ExternalInterfaceCurrentThroughput_Type=Integer32
_ExternalInterfaceCurrentThroughput_Object=MibScalar
externalInterfaceCurrentThroughput=_ExternalInterfaceCurrentThroughput_Object((1,3,6,1,4,1,8741,8,1,2,5,3),_ExternalInterfaceCurrentThroughput_Type())
externalInterfaceCurrentThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:externalInterfaceCurrentThroughput.setStatus(_A)
_ExternalInterfacePeakThroughput_Type=Integer32
_ExternalInterfacePeakThroughput_Object=MibScalar
externalInterfacePeakThroughput=_ExternalInterfacePeakThroughput_Object((1,3,6,1,4,1,8741,8,1,2,5,4),_ExternalInterfacePeakThroughput_Type())
externalInterfacePeakThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:externalInterfacePeakThroughput.setStatus(_A)
_ClusterlInterfaceCurrentThroughput_Type=Integer32
_ClusterlInterfaceCurrentThroughput_Object=MibScalar
clusterlInterfaceCurrentThroughput=_ClusterlInterfaceCurrentThroughput_Object((1,3,6,1,4,1,8741,8,1,2,5,5),_ClusterlInterfaceCurrentThroughput_Type())
clusterlInterfaceCurrentThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:clusterlInterfaceCurrentThroughput.setStatus(_A)
_ClusterInterfacePeakThroughput_Type=Integer32
_ClusterInterfacePeakThroughput_Object=MibScalar
clusterInterfacePeakThroughput=_ClusterInterfacePeakThroughput_Object((1,3,6,1,4,1,8741,8,1,2,5,6),_ClusterInterfacePeakThroughput_Type())
clusterInterfacePeakThroughput.setMaxAccess(_B)
if mibBuilder.loadTexts:clusterInterfacePeakThroughput.setStatus(_A)
_LogUtilization_Type=Integer32
_LogUtilization_Object=MibScalar
logUtilization=_LogUtilization_Object((1,3,6,1,4,1,8741,8,1,2,9),_LogUtilization_Type())
logUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:logUtilization.setStatus(_A)
cpuCapacityWarning=NotificationType((1,3,6,1,4,1,8741,8,1,2,6))
cpuCapacityWarning.setObjects((_C,_E))
if mibBuilder.loadTexts:cpuCapacityWarning.setStatus(_A)
memoryCapacityWarning=NotificationType((1,3,6,1,4,1,8741,8,1,2,7))
memoryCapacityWarning.setObjects((_C,_F))
if mibBuilder.loadTexts:memoryCapacityWarning.setStatus(_A)
userLimitWarning=NotificationType((1,3,6,1,4,1,8741,8,1,2,8))
userLimitWarning.setObjects((_C,_D))
if mibBuilder.loadTexts:userLimitWarning.setStatus(_A)
logCapacityWarning=NotificationType((1,3,6,1,4,1,8741,8,1,2,100))
logCapacityWarning.setObjects((_C,_G))
if mibBuilder.loadTexts:logCapacityWarning.setStatus(_A)
userLimitReached=NotificationType((1,3,6,1,4,1,8741,8,1,2,102))
userLimitReached.setObjects((_C,_D))
if mibBuilder.loadTexts:userLimitReached.setStatus(_A)
userLimitExceeded=NotificationType((1,3,6,1,4,1,8741,8,1,2,103))
userLimitExceeded.setObjects((_C,_D))
if mibBuilder.loadTexts:userLimitExceeded.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'sonicwallSystemHealth':sonicwallSystemHealth,'authenticatedUsers':authenticatedUsers,_D:currentlyLoggedIn,'peakLoggedIn':peakLoggedIn,'maximumlicensedUsers':maximumlicensedUsers,'connectionUtilization':connectionUtilization,'currentConnections':currentConnections,'peakConnections':peakConnections,_E:cpuUtilization,'memoryTotalUtilization':memoryTotalUtilization,_F:ramUtilization,'swapUtilization':swapUtilization,'bandwidthUtilization':bandwidthUtilization,'internalInterfaceCurrentThroughput':internalInterfaceCurrentThroughput,'internalInterfacePeakThroughput':internalInterfacePeakThroughput,'externalInterfaceCurrentThroughput':externalInterfaceCurrentThroughput,'externalInterfacePeakThroughput':externalInterfacePeakThroughput,'clusterlInterfaceCurrentThroughput':clusterlInterfaceCurrentThroughput,'clusterInterfacePeakThroughput':clusterInterfacePeakThroughput,'cpuCapacityWarning':cpuCapacityWarning,'memoryCapacityWarning':memoryCapacityWarning,'userLimitWarning':userLimitWarning,_G:logUtilization,'logCapacityWarning':logCapacityWarning,'userLimitReached':userLimitReached,'userLimitExceeded':userLimitExceeded})