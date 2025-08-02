_X='tmsHostFault'
_W='tmsTrapIpv6Nexthop'
_V='tmsTrapIpv6BgpPeer'
_U='tmsTrapIpv6GreDestination'
_T='tmsTrapIpv6GreSource'
_S='tmsTrapNexthop'
_R='tmsTrapBgpPeer'
_Q='tmsTrapGreDestination'
_P='tmsTrapGreSource'
_O='obsolete'
_N='Unsigned32'
_M='tmsMitigationName'
_L='tmsTrapSubhostName'
_K='tmsMitigationIndex'
_J='ifName'
_I='IF-MIB'
_H='tmsTrapComponentName'
_G='read-only'
_F='tmsTrapDetail'
_E='tmsTrapString'
_D='sysName'
_C='SNMPv2-MIB'
_B='current'
_A='PEAKFLOW-TMS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arbornetworksProducts,=mibBuilder.importSymbols('ARBOR-SMI','arbornetworksProducts')
ifName,=mibBuilder.importSymbols(_I,_J)
Ipv6Address,Ipv6AddressPrefix=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressPrefix')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_C,_D)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
peakflowTmsMIB=ModuleIdentity((1,3,6,1,4,1,9694,1,5))
if mibBuilder.loadTexts:peakflowTmsMIB.setRevisions(('2019-08-29 00:00','2019-08-27 00:00','2014-03-12 00:00','2013-09-19 00:00','2013-08-19 00:00','2012-03-29 12:00','2012-01-12 12:00','2011-06-14 16:00','2011-06-03 16:00','2011-06-03 00:00','2011-05-23 00:00','2011-01-21 00:00','2010-10-28 00:00','2010-09-07 00:00','2009-05-27 00:00','2009-05-08 00:00','2009-03-11 00:00','2009-02-13 00:00','2008-11-13 00:00','2008-04-07 00:00','2007-11-20 00:00','2007-04-27 00:00'))
class TmsTableIndex(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class TmsTableIndexOrZero(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class TmsPercentage(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
class TmsHundredths(TextualConvention,Integer32):status=_B;displayHint='d-2'
_PeakflowTmsMgr_ObjectIdentity=ObjectIdentity
peakflowTmsMgr=_PeakflowTmsMgr_ObjectIdentity((1,3,6,1,4,1,9694,1,5,2))
_TmsHostFault_Type=DisplayString
_TmsHostFault_Object=MibScalar
tmsHostFault=_TmsHostFault_Object((1,3,6,1,4,1,9694,1,5,2,1),_TmsHostFault_Type())
tmsHostFault.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsHostFault.setStatus(_B)
_TmsHostUpTime_Type=TimeTicks
_TmsHostUpTime_Object=MibScalar
tmsHostUpTime=_TmsHostUpTime_Object((1,3,6,1,4,1,9694,1,5,2,2),_TmsHostUpTime_Type())
tmsHostUpTime.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsHostUpTime.setStatus(_B)
_DeviceCpuLoadAvg1min_Type=TmsHundredths
_DeviceCpuLoadAvg1min_Object=MibScalar
deviceCpuLoadAvg1min=_DeviceCpuLoadAvg1min_Object((1,3,6,1,4,1,9694,1,5,2,3),_DeviceCpuLoadAvg1min_Type())
deviceCpuLoadAvg1min.setMaxAccess(_G)
if mibBuilder.loadTexts:deviceCpuLoadAvg1min.setStatus(_B)
_DeviceCpuLoadAvg5min_Type=TmsHundredths
_DeviceCpuLoadAvg5min_Object=MibScalar
deviceCpuLoadAvg5min=_DeviceCpuLoadAvg5min_Object((1,3,6,1,4,1,9694,1,5,2,4),_DeviceCpuLoadAvg5min_Type())
deviceCpuLoadAvg5min.setMaxAccess(_G)
if mibBuilder.loadTexts:deviceCpuLoadAvg5min.setStatus(_B)
_DeviceCpuLoadAvg15min_Type=TmsHundredths
_DeviceCpuLoadAvg15min_Object=MibScalar
deviceCpuLoadAvg15min=_DeviceCpuLoadAvg15min_Object((1,3,6,1,4,1,9694,1,5,2,5),_DeviceCpuLoadAvg15min_Type())
deviceCpuLoadAvg15min.setMaxAccess(_G)
if mibBuilder.loadTexts:deviceCpuLoadAvg15min.setStatus(_B)
_DeviceDiskUsage_Type=TmsPercentage
_DeviceDiskUsage_Object=MibScalar
deviceDiskUsage=_DeviceDiskUsage_Object((1,3,6,1,4,1,9694,1,5,2,6),_DeviceDiskUsage_Type())
deviceDiskUsage.setMaxAccess(_G)
if mibBuilder.loadTexts:deviceDiskUsage.setStatus(_B)
_DevicePhysicalMemoryUsage_Type=TmsPercentage
_DevicePhysicalMemoryUsage_Object=MibScalar
devicePhysicalMemoryUsage=_DevicePhysicalMemoryUsage_Object((1,3,6,1,4,1,9694,1,5,2,7),_DevicePhysicalMemoryUsage_Type())
devicePhysicalMemoryUsage.setMaxAccess(_G)
if mibBuilder.loadTexts:devicePhysicalMemoryUsage.setStatus(_B)
_DeviceSwapSpaceUsage_Type=TmsPercentage
_DeviceSwapSpaceUsage_Object=MibScalar
deviceSwapSpaceUsage=_DeviceSwapSpaceUsage_Object((1,3,6,1,4,1,9694,1,5,2,8),_DeviceSwapSpaceUsage_Type())
deviceSwapSpaceUsage.setMaxAccess(_G)
if mibBuilder.loadTexts:deviceSwapSpaceUsage.setStatus(_B)
_TmsTrapString_Type=DisplayString
_TmsTrapString_Object=MibScalar
tmsTrapString=_TmsTrapString_Object((1,3,6,1,4,1,9694,1,5,2,9),_TmsTrapString_Type())
tmsTrapString.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapString.setStatus(_B)
_TmsTrapDetail_Type=DisplayString
_TmsTrapDetail_Object=MibScalar
tmsTrapDetail=_TmsTrapDetail_Object((1,3,6,1,4,1,9694,1,5,2,10),_TmsTrapDetail_Type())
tmsTrapDetail.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapDetail.setStatus(_B)
_TmsTrapSubhostName_Type=DisplayString
_TmsTrapSubhostName_Object=MibScalar
tmsTrapSubhostName=_TmsTrapSubhostName_Object((1,3,6,1,4,1,9694,1,5,2,11),_TmsTrapSubhostName_Type())
tmsTrapSubhostName.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapSubhostName.setStatus(_B)
_TmsTrapComponentName_Type=DisplayString
_TmsTrapComponentName_Object=MibScalar
tmsTrapComponentName=_TmsTrapComponentName_Object((1,3,6,1,4,1,9694,1,5,2,12),_TmsTrapComponentName_Type())
tmsTrapComponentName.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapComponentName.setStatus(_B)
_TmsTrapBgpPeer_Type=IpAddress
_TmsTrapBgpPeer_Object=MibScalar
tmsTrapBgpPeer=_TmsTrapBgpPeer_Object((1,3,6,1,4,1,9694,1,5,2,13),_TmsTrapBgpPeer_Type())
tmsTrapBgpPeer.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapBgpPeer.setStatus(_B)
_TmsTrapGreSource_Type=IpAddress
_TmsTrapGreSource_Object=MibScalar
tmsTrapGreSource=_TmsTrapGreSource_Object((1,3,6,1,4,1,9694,1,5,2,14),_TmsTrapGreSource_Type())
tmsTrapGreSource.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapGreSource.setStatus(_B)
_TmsTrapGreDestination_Type=IpAddress
_TmsTrapGreDestination_Object=MibScalar
tmsTrapGreDestination=_TmsTrapGreDestination_Object((1,3,6,1,4,1,9694,1,5,2,15),_TmsTrapGreDestination_Type())
tmsTrapGreDestination.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapGreDestination.setStatus(_B)
_TmsTrapNexthop_Type=IpAddress
_TmsTrapNexthop_Object=MibScalar
tmsTrapNexthop=_TmsTrapNexthop_Object((1,3,6,1,4,1,9694,1,5,2,16),_TmsTrapNexthop_Type())
tmsTrapNexthop.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapNexthop.setStatus(_B)
_TmsTrapIpv6BgpPeer_Type=Ipv6Address
_TmsTrapIpv6BgpPeer_Object=MibScalar
tmsTrapIpv6BgpPeer=_TmsTrapIpv6BgpPeer_Object((1,3,6,1,4,1,9694,1,5,2,17),_TmsTrapIpv6BgpPeer_Type())
tmsTrapIpv6BgpPeer.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapIpv6BgpPeer.setStatus(_B)
_TmsTrapIpv6GreSource_Type=Ipv6Address
_TmsTrapIpv6GreSource_Object=MibScalar
tmsTrapIpv6GreSource=_TmsTrapIpv6GreSource_Object((1,3,6,1,4,1,9694,1,5,2,18),_TmsTrapIpv6GreSource_Type())
tmsTrapIpv6GreSource.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapIpv6GreSource.setStatus(_B)
_TmsTrapIpv6GreDestination_Type=Ipv6Address
_TmsTrapIpv6GreDestination_Object=MibScalar
tmsTrapIpv6GreDestination=_TmsTrapIpv6GreDestination_Object((1,3,6,1,4,1,9694,1,5,2,19),_TmsTrapIpv6GreDestination_Type())
tmsTrapIpv6GreDestination.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapIpv6GreDestination.setStatus(_B)
_TmsTrapIpv6Nexthop_Type=Ipv6Address
_TmsTrapIpv6Nexthop_Object=MibScalar
tmsTrapIpv6Nexthop=_TmsTrapIpv6Nexthop_Object((1,3,6,1,4,1,9694,1,5,2,20),_TmsTrapIpv6Nexthop_Type())
tmsTrapIpv6Nexthop.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapIpv6Nexthop.setStatus(_B)
_TmsTrapGreName_Type=DisplayString
_TmsTrapGreName_Object=MibScalar
tmsTrapGreName=_TmsTrapGreName_Object((1,3,6,1,4,1,9694,1,5,2,21),_TmsTrapGreName_Type())
tmsTrapGreName.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsTrapGreName.setStatus(_B)
_TmsOverrunDropRatePps_Type=Gauge32
_TmsOverrunDropRatePps_Object=MibScalar
tmsOverrunDropRatePps=_TmsOverrunDropRatePps_Object((1,3,6,1,4,1,9694,1,5,2,39),_TmsOverrunDropRatePps_Type())
tmsOverrunDropRatePps.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsOverrunDropRatePps.setStatus(_B)
_PeakflowTmsTraps_ObjectIdentity=ObjectIdentity
peakflowTmsTraps=_PeakflowTmsTraps_ObjectIdentity((1,3,6,1,4,1,9694,1,5,3))
_PeakflowTmsTrapsEnumerate_ObjectIdentity=ObjectIdentity
peakflowTmsTrapsEnumerate=_PeakflowTmsTrapsEnumerate_ObjectIdentity((1,3,6,1,4,1,9694,1,5,3,0))
_PeakflowTmsObj_ObjectIdentity=ObjectIdentity
peakflowTmsObj=_PeakflowTmsObj_ObjectIdentity((1,3,6,1,4,1,9694,1,5,5))
_TmsDpiConfig_ObjectIdentity=ObjectIdentity
tmsDpiConfig=_TmsDpiConfig_ObjectIdentity((1,3,6,1,4,1,9694,1,5,5,1))
_TmsVersion_Type=DisplayString
_TmsVersion_Object=MibScalar
tmsVersion=_TmsVersion_Object((1,3,6,1,4,1,9694,1,5,5,1,1),_TmsVersion_Type())
tmsVersion.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsVersion.setStatus(_B)
_TmsLastUpdate_Type=DisplayString
_TmsLastUpdate_Object=MibScalar
tmsLastUpdate=_TmsLastUpdate_Object((1,3,6,1,4,1,9694,1,5,5,1,2),_TmsLastUpdate_Type())
tmsLastUpdate.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsLastUpdate.setStatus(_B)
_TmsMitigationConfig_ObjectIdentity=ObjectIdentity
tmsMitigationConfig=_TmsMitigationConfig_ObjectIdentity((1,3,6,1,4,1,9694,1,5,5,2))
_TmsMitigationLastUpdate_Type=DisplayString
_TmsMitigationLastUpdate_Object=MibScalar
tmsMitigationLastUpdate=_TmsMitigationLastUpdate_Object((1,3,6,1,4,1,9694,1,5,5,2,1),_TmsMitigationLastUpdate_Type())
tmsMitigationLastUpdate.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsMitigationLastUpdate.setStatus(_B)
_TmsMitigationNumber_Type=TmsTableIndexOrZero
_TmsMitigationNumber_Object=MibScalar
tmsMitigationNumber=_TmsMitigationNumber_Object((1,3,6,1,4,1,9694,1,5,5,2,2),_TmsMitigationNumber_Type())
tmsMitigationNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsMitigationNumber.setStatus(_B)
_TmsMitigationTable_Object=MibTable
tmsMitigationTable=_TmsMitigationTable_Object((1,3,6,1,4,1,9694,1,5,5,2,3))
if mibBuilder.loadTexts:tmsMitigationTable.setStatus(_B)
_TmsMitigationEntry_Object=MibTableRow
tmsMitigationEntry=_TmsMitigationEntry_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1))
tmsMitigationEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:tmsMitigationEntry.setStatus(_B)
_TmsMitigationIndex_Type=TmsTableIndex
_TmsMitigationIndex_Object=MibTableColumn
tmsMitigationIndex=_TmsMitigationIndex_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1,1),_TmsMitigationIndex_Type())
tmsMitigationIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsMitigationIndex.setStatus(_B)
_TmsMitigationId_Type=Unsigned32
_TmsMitigationId_Object=MibTableColumn
tmsMitigationId=_TmsMitigationId_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1,2),_TmsMitigationId_Type())
tmsMitigationId.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsMitigationId.setStatus(_B)
_TmsDestinationPrefix_Type=IpAddress
_TmsDestinationPrefix_Object=MibTableColumn
tmsDestinationPrefix=_TmsDestinationPrefix_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1,3),_TmsDestinationPrefix_Type())
tmsDestinationPrefix.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsDestinationPrefix.setStatus(_B)
class _TmsDestinationPrefixMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_TmsDestinationPrefixMask_Type.__name__=_N
_TmsDestinationPrefixMask_Object=MibTableColumn
tmsDestinationPrefixMask=_TmsDestinationPrefixMask_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1,4),_TmsDestinationPrefixMask_Type())
tmsDestinationPrefixMask.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsDestinationPrefixMask.setStatus(_B)
_TmsMitigationName_Type=DisplayString
_TmsMitigationName_Object=MibTableColumn
tmsMitigationName=_TmsMitigationName_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1,5),_TmsMitigationName_Type())
tmsMitigationName.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsMitigationName.setStatus(_B)
_TmsIpv6DestinationPrefix_Type=Ipv6AddressPrefix
_TmsIpv6DestinationPrefix_Object=MibTableColumn
tmsIpv6DestinationPrefix=_TmsIpv6DestinationPrefix_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1,6),_TmsIpv6DestinationPrefix_Type())
tmsIpv6DestinationPrefix.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsIpv6DestinationPrefix.setStatus(_B)
class _TmsIpv6DestinationPrefixMask_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_TmsIpv6DestinationPrefixMask_Type.__name__=_N
_TmsIpv6DestinationPrefixMask_Object=MibTableColumn
tmsIpv6DestinationPrefixMask=_TmsIpv6DestinationPrefixMask_Object((1,3,6,1,4,1,9694,1,5,5,2,3,1,7),_TmsIpv6DestinationPrefixMask_Type())
tmsIpv6DestinationPrefixMask.setMaxAccess(_G)
if mibBuilder.loadTexts:tmsIpv6DestinationPrefixMask.setStatus(_B)
hostFault=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,1))
hostFault.setObjects(*((_C,_D),(_A,_X)))
if mibBuilder.loadTexts:hostFault.setStatus(_O)
greTunnelDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,2))
greTunnelDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:greTunnelDown.setStatus(_B)
greTunnelUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,3))
greTunnelUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:greTunnelUp.setStatus(_B)
tmsLinkUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,4))
tmsLinkUp.setObjects(*((_C,_D),(_A,_E)))
if mibBuilder.loadTexts:tmsLinkUp.setStatus(_O)
tmsLinkDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,5))
tmsLinkDown.setObjects(*((_C,_D),(_A,_E)))
if mibBuilder.loadTexts:tmsLinkDown.setStatus(_O)
subHostUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,6))
subHostUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_L)))
if mibBuilder.loadTexts:subHostUp.setStatus(_B)
subHostDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,7))
subHostDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_L)))
if mibBuilder.loadTexts:subHostDown.setStatus(_B)
tmsBgpNeighborDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,8))
tmsBgpNeighborDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_R)))
if mibBuilder.loadTexts:tmsBgpNeighborDown.setStatus(_B)
tmsBgpNeighborUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,9))
tmsBgpNeighborUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_R)))
if mibBuilder.loadTexts:tmsBgpNeighborUp.setStatus(_B)
tmsNexthopDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,10))
tmsNexthopDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_S),(_I,_J)))
if mibBuilder.loadTexts:tmsNexthopDown.setStatus(_B)
tmsNexthopUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,11))
tmsNexthopUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_S),(_I,_J)))
if mibBuilder.loadTexts:tmsNexthopUp.setStatus(_B)
tmsMitigationError=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,12))
tmsMitigationError.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_M)))
if mibBuilder.loadTexts:tmsMitigationError.setStatus(_B)
tmsMitigationSuspended=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,13))
tmsMitigationSuspended.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_M)))
if mibBuilder.loadTexts:tmsMitigationSuspended.setStatus(_B)
tmsMitigationRunning=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,14))
tmsMitigationRunning.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_K),(_A,_M)))
if mibBuilder.loadTexts:tmsMitigationRunning.setStatus(_B)
tmsConfigMissing=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,15))
tmsConfigMissing.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsConfigMissing.setStatus(_B)
tmsConfigError=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,16))
tmsConfigError.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsConfigError.setStatus(_B)
tmsConfigOk=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,17))
tmsConfigOk.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsConfigOk.setStatus(_B)
tmsHwDeviceDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,18))
tmsHwDeviceDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsHwDeviceDown.setStatus(_B)
tmsHwDeviceUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,19))
tmsHwDeviceUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsHwDeviceUp.setStatus(_B)
tmsHwSensorCritical=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,20))
tmsHwSensorCritical.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsHwSensorCritical.setStatus(_B)
tmsHwSensorOk=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,21))
tmsHwSensorOk.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsHwSensorOk.setStatus(_B)
tmsSwComponentDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,22))
tmsSwComponentDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_L),(_A,_H)))
if mibBuilder.loadTexts:tmsSwComponentDown.setStatus(_B)
tmsSwComponentUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,23))
tmsSwComponentUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_L),(_A,_H)))
if mibBuilder.loadTexts:tmsSwComponentUp.setStatus(_B)
tmsSystemStatusCritical=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,24))
tmsSystemStatusCritical.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSystemStatusCritical.setStatus(_B)
tmsSystemStatusDegraded=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,25))
tmsSystemStatusDegraded.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSystemStatusDegraded.setStatus(_B)
tmsSystemStatusNominal=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,26))
tmsSystemStatusNominal.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSystemStatusNominal.setStatus(_B)
tmsFilesystemCritical=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,27))
tmsFilesystemCritical.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsFilesystemCritical.setStatus(_B)
tmsFilesystemNominal=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,28))
tmsFilesystemNominal.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsFilesystemNominal.setStatus(_B)
tmsHwSensorUnknown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,29))
tmsHwSensorUnknown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsHwSensorUnknown.setStatus(_B)
tmsSpCommunicationUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,30))
tmsSpCommunicationUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSpCommunicationUp.setStatus(_B)
tmsSpCommunicationDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,31))
tmsSpCommunicationDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSpCommunicationDown.setStatus(_B)
tmsSystemStatusError=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,32))
tmsSystemStatusError.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSystemStatusError.setStatus(_B)
tmsAutomitigationBgpEnabled=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,33))
tmsAutomitigationBgpEnabled.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsAutomitigationBgpEnabled.setStatus(_B)
tmsAutomitigationBgpDisabled=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,34))
tmsAutomitigationBgpDisabled.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsAutomitigationBgpDisabled.setStatus(_B)
tmsAutomitigationBgpSuspended=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,35))
tmsAutomitigationBgpSuspended.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsAutomitigationBgpSuspended.setStatus(_B)
tmsIpv6GreTunnelDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,36))
tmsIpv6GreTunnelDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:tmsIpv6GreTunnelDown.setStatus(_B)
tmsIpv6GreTunnelUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,37))
tmsIpv6GreTunnelUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:tmsIpv6GreTunnelUp.setStatus(_B)
tmsIpv6BgpNeighborDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,38))
tmsIpv6BgpNeighborDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_V)))
if mibBuilder.loadTexts:tmsIpv6BgpNeighborDown.setStatus(_B)
tmsIpv6BgpNeighborUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,39))
tmsIpv6BgpNeighborUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_V)))
if mibBuilder.loadTexts:tmsIpv6BgpNeighborUp.setStatus(_B)
tmsIpv6NexthopDown=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,40))
tmsIpv6NexthopDown.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_W),(_I,_J)))
if mibBuilder.loadTexts:tmsIpv6NexthopDown.setStatus(_B)
tmsIpv6NexthopUp=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,41))
tmsIpv6NexthopUp.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_W),(_I,_J)))
if mibBuilder.loadTexts:tmsIpv6NexthopUp.setStatus(_B)
tmsPerformanceOk=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,42))
tmsPerformanceOk.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsPerformanceOk.setStatus(_B)
tmsPerformanceLossy=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,43))
tmsPerformanceLossy.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsPerformanceLossy.setStatus(_B)
tmsSystemPrefixesOk=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,44))
tmsSystemPrefixesOk.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSystemPrefixesOk.setStatus(_B)
tmsSystemPrefixesMissing=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,45))
tmsSystemPrefixesMissing.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSystemPrefixesMissing.setStatus(_B)
tmsSpCommunicationDegraded=NotificationType((1,3,6,1,4,1,9694,1,5,3,0,46))
tmsSpCommunicationDegraded.setObjects(*((_C,_D),(_A,_E),(_A,_F),(_A,_H)))
if mibBuilder.loadTexts:tmsSpCommunicationDegraded.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'TmsTableIndex':TmsTableIndex,'TmsTableIndexOrZero':TmsTableIndexOrZero,'TmsPercentage':TmsPercentage,'TmsHundredths':TmsHundredths,'peakflowTmsMIB':peakflowTmsMIB,'peakflowTmsMgr':peakflowTmsMgr,_X:tmsHostFault,'tmsHostUpTime':tmsHostUpTime,'deviceCpuLoadAvg1min':deviceCpuLoadAvg1min,'deviceCpuLoadAvg5min':deviceCpuLoadAvg5min,'deviceCpuLoadAvg15min':deviceCpuLoadAvg15min,'deviceDiskUsage':deviceDiskUsage,'devicePhysicalMemoryUsage':devicePhysicalMemoryUsage,'deviceSwapSpaceUsage':deviceSwapSpaceUsage,_E:tmsTrapString,_F:tmsTrapDetail,_L:tmsTrapSubhostName,_H:tmsTrapComponentName,_R:tmsTrapBgpPeer,_P:tmsTrapGreSource,_Q:tmsTrapGreDestination,_S:tmsTrapNexthop,_V:tmsTrapIpv6BgpPeer,_T:tmsTrapIpv6GreSource,_U:tmsTrapIpv6GreDestination,_W:tmsTrapIpv6Nexthop,'tmsTrapGreName':tmsTrapGreName,'tmsOverrunDropRatePps':tmsOverrunDropRatePps,'peakflowTmsTraps':peakflowTmsTraps,'peakflowTmsTrapsEnumerate':peakflowTmsTrapsEnumerate,'hostFault':hostFault,'greTunnelDown':greTunnelDown,'greTunnelUp':greTunnelUp,'tmsLinkUp':tmsLinkUp,'tmsLinkDown':tmsLinkDown,'subHostUp':subHostUp,'subHostDown':subHostDown,'tmsBgpNeighborDown':tmsBgpNeighborDown,'tmsBgpNeighborUp':tmsBgpNeighborUp,'tmsNexthopDown':tmsNexthopDown,'tmsNexthopUp':tmsNexthopUp,'tmsMitigationError':tmsMitigationError,'tmsMitigationSuspended':tmsMitigationSuspended,'tmsMitigationRunning':tmsMitigationRunning,'tmsConfigMissing':tmsConfigMissing,'tmsConfigError':tmsConfigError,'tmsConfigOk':tmsConfigOk,'tmsHwDeviceDown':tmsHwDeviceDown,'tmsHwDeviceUp':tmsHwDeviceUp,'tmsHwSensorCritical':tmsHwSensorCritical,'tmsHwSensorOk':tmsHwSensorOk,'tmsSwComponentDown':tmsSwComponentDown,'tmsSwComponentUp':tmsSwComponentUp,'tmsSystemStatusCritical':tmsSystemStatusCritical,'tmsSystemStatusDegraded':tmsSystemStatusDegraded,'tmsSystemStatusNominal':tmsSystemStatusNominal,'tmsFilesystemCritical':tmsFilesystemCritical,'tmsFilesystemNominal':tmsFilesystemNominal,'tmsHwSensorUnknown':tmsHwSensorUnknown,'tmsSpCommunicationUp':tmsSpCommunicationUp,'tmsSpCommunicationDown':tmsSpCommunicationDown,'tmsSystemStatusError':tmsSystemStatusError,'tmsAutomitigationBgpEnabled':tmsAutomitigationBgpEnabled,'tmsAutomitigationBgpDisabled':tmsAutomitigationBgpDisabled,'tmsAutomitigationBgpSuspended':tmsAutomitigationBgpSuspended,'tmsIpv6GreTunnelDown':tmsIpv6GreTunnelDown,'tmsIpv6GreTunnelUp':tmsIpv6GreTunnelUp,'tmsIpv6BgpNeighborDown':tmsIpv6BgpNeighborDown,'tmsIpv6BgpNeighborUp':tmsIpv6BgpNeighborUp,'tmsIpv6NexthopDown':tmsIpv6NexthopDown,'tmsIpv6NexthopUp':tmsIpv6NexthopUp,'tmsPerformanceOk':tmsPerformanceOk,'tmsPerformanceLossy':tmsPerformanceLossy,'tmsSystemPrefixesOk':tmsSystemPrefixesOk,'tmsSystemPrefixesMissing':tmsSystemPrefixesMissing,'tmsSpCommunicationDegraded':tmsSpCommunicationDegraded,'peakflowTmsObj':peakflowTmsObj,'tmsDpiConfig':tmsDpiConfig,'tmsVersion':tmsVersion,'tmsLastUpdate':tmsLastUpdate,'tmsMitigationConfig':tmsMitigationConfig,'tmsMitigationLastUpdate':tmsMitigationLastUpdate,'tmsMitigationNumber':tmsMitigationNumber,'tmsMitigationTable':tmsMitigationTable,'tmsMitigationEntry':tmsMitigationEntry,_K:tmsMitigationIndex,'tmsMitigationId':tmsMitigationId,'tmsDestinationPrefix':tmsDestinationPrefix,'tmsDestinationPrefixMask':tmsDestinationPrefixMask,_M:tmsMitigationName,'tmsIpv6DestinationPrefix':tmsIpv6DestinationPrefix,'tmsIpv6DestinationPrefixMask':tmsIpv6DestinationPrefixMask})