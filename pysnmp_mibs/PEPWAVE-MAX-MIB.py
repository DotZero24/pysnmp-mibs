_j='maxSetGroup'
_i='maxWanGroup'
_h='maxLinkGroup'
_g='maxSystemGroup'
_f='lanConfigSubnetMask'
_e='lanConfigIp'
_d='portLanSpeedConfig'
_c='portWanSpeedConfig'
_b='maxReboot'
_a='wanUsageDataTransferred'
_Z='wanUsageThroughputOut'
_Y='wanUsageThroughputIn'
_X='linkDataTransferred'
_W='linkThroughputOut'
_V='linkThroughputIn'
_U='linkIp'
_T='linkStatus'
_S='linkName'
_R='maxLinkNumber'
_Q='maxLanSubnetMask'
_P='maxLanIp'
_O='maxLanStatus'
_N='maxUpTime'
_M='maxTime'
_L='maxSerialNumber'
_K='maxFirmware'
_J='portWanSpeedConfigIndex'
_I='wanUsageIndex'
_H='linkIpIndex'
_G='linkIpConnNum'
_F='linkConnNum'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='PEPWAVE-MAX-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pepwaveMAX=ModuleIdentity((1,3,6,1,4,1,27662,1))
if mibBuilder.loadTexts:pepwaveMAX.setRevisions(('2012-06-06 00:00',))
class TableIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ConnectionNum(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NameString(TextualConvention,OctetString):status=_A;displayHint='80a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
class PortSpeedType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',0),('auto',1),('fullDulplex10',2),('halfDulplex10',3),('fullDulplex100',4),('halfDulplex100',5),('fullDulplex1000',6),('halfDulplex1000',7)))
_MaxStatus_ObjectIdentity=ObjectIdentity
maxStatus=_MaxStatus_ObjectIdentity((1,3,6,1,4,1,27662,1,1))
_MaxSystem_ObjectIdentity=ObjectIdentity
maxSystem=_MaxSystem_ObjectIdentity((1,3,6,1,4,1,27662,1,1,1))
_MaxFirmware_Type=NameString
_MaxFirmware_Object=MibScalar
maxFirmware=_MaxFirmware_Object((1,3,6,1,4,1,27662,1,1,1,1),_MaxFirmware_Type())
maxFirmware.setMaxAccess(_C)
if mibBuilder.loadTexts:maxFirmware.setStatus(_A)
_MaxSerialNumber_Type=NameString
_MaxSerialNumber_Object=MibScalar
maxSerialNumber=_MaxSerialNumber_Object((1,3,6,1,4,1,27662,1,1,1,2),_MaxSerialNumber_Type())
maxSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:maxSerialNumber.setStatus(_A)
_MaxTime_Type=NameString
_MaxTime_Object=MibScalar
maxTime=_MaxTime_Object((1,3,6,1,4,1,27662,1,1,1,3),_MaxTime_Type())
maxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:maxTime.setStatus(_A)
_MaxUpTime_Type=TimeTicks
_MaxUpTime_Object=MibScalar
maxUpTime=_MaxUpTime_Object((1,3,6,1,4,1,27662,1,1,1,4),_MaxUpTime_Type())
maxUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:maxUpTime.setStatus(_A)
_MaxLan_ObjectIdentity=ObjectIdentity
maxLan=_MaxLan_ObjectIdentity((1,3,6,1,4,1,27662,1,1,1,6))
_MaxLanStatus_Type=NameString
_MaxLanStatus_Object=MibScalar
maxLanStatus=_MaxLanStatus_Object((1,3,6,1,4,1,27662,1,1,1,6,1),_MaxLanStatus_Type())
maxLanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:maxLanStatus.setStatus(_A)
_MaxLanIp_Type=IpAddress
_MaxLanIp_Object=MibScalar
maxLanIp=_MaxLanIp_Object((1,3,6,1,4,1,27662,1,1,1,6,2),_MaxLanIp_Type())
maxLanIp.setMaxAccess(_C)
if mibBuilder.loadTexts:maxLanIp.setStatus(_A)
_MaxLanSubnetMask_Type=IpAddress
_MaxLanSubnetMask_Object=MibScalar
maxLanSubnetMask=_MaxLanSubnetMask_Object((1,3,6,1,4,1,27662,1,1,1,6,3),_MaxLanSubnetMask_Type())
maxLanSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:maxLanSubnetMask.setStatus(_A)
_MaxLinkStatus_ObjectIdentity=ObjectIdentity
maxLinkStatus=_MaxLinkStatus_ObjectIdentity((1,3,6,1,4,1,27662,1,1,2))
_MaxLinkNumber_Type=Counter32
_MaxLinkNumber_Object=MibScalar
maxLinkNumber=_MaxLinkNumber_Object((1,3,6,1,4,1,27662,1,1,2,1),_MaxLinkNumber_Type())
maxLinkNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:maxLinkNumber.setStatus(_A)
_LinkTable_Object=MibTable
linkTable=_LinkTable_Object((1,3,6,1,4,1,27662,1,1,2,2))
if mibBuilder.loadTexts:linkTable.setStatus(_A)
_LinkEntry_Object=MibTableRow
linkEntry=_LinkEntry_Object((1,3,6,1,4,1,27662,1,1,2,2,1))
linkEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:linkEntry.setStatus(_A)
_LinkConnNum_Type=ConnectionNum
_LinkConnNum_Object=MibTableColumn
linkConnNum=_LinkConnNum_Object((1,3,6,1,4,1,27662,1,1,2,2,1,1),_LinkConnNum_Type())
linkConnNum.setMaxAccess(_D)
if mibBuilder.loadTexts:linkConnNum.setStatus(_A)
_LinkName_Type=NameString
_LinkName_Object=MibTableColumn
linkName=_LinkName_Object((1,3,6,1,4,1,27662,1,1,2,2,1,2),_LinkName_Type())
linkName.setMaxAccess(_C)
if mibBuilder.loadTexts:linkName.setStatus(_A)
_LinkStatus_Type=NameString
_LinkStatus_Object=MibTableColumn
linkStatus=_LinkStatus_Object((1,3,6,1,4,1,27662,1,1,2,2,1,3),_LinkStatus_Type())
linkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:linkStatus.setStatus(_A)
_LinkThroughputIn_Type=Counter32
_LinkThroughputIn_Object=MibTableColumn
linkThroughputIn=_LinkThroughputIn_Object((1,3,6,1,4,1,27662,1,1,2,2,1,4),_LinkThroughputIn_Type())
linkThroughputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:linkThroughputIn.setStatus(_A)
_LinkThroughputOut_Type=Counter32
_LinkThroughputOut_Object=MibTableColumn
linkThroughputOut=_LinkThroughputOut_Object((1,3,6,1,4,1,27662,1,1,2,2,1,5),_LinkThroughputOut_Type())
linkThroughputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:linkThroughputOut.setStatus(_A)
_LinkDataTransferred_Type=Counter64
_LinkDataTransferred_Object=MibTableColumn
linkDataTransferred=_LinkDataTransferred_Object((1,3,6,1,4,1,27662,1,1,2,2,1,6),_LinkDataTransferred_Type())
linkDataTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:linkDataTransferred.setStatus(_A)
_LinkIpTable_Object=MibTable
linkIpTable=_LinkIpTable_Object((1,3,6,1,4,1,27662,1,1,2,3))
if mibBuilder.loadTexts:linkIpTable.setStatus(_A)
_LinkIpEntry_Object=MibTableRow
linkIpEntry=_LinkIpEntry_Object((1,3,6,1,4,1,27662,1,1,2,3,1))
linkIpEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:linkIpEntry.setStatus(_A)
_LinkIpConnNum_Type=ConnectionNum
_LinkIpConnNum_Object=MibTableColumn
linkIpConnNum=_LinkIpConnNum_Object((1,3,6,1,4,1,27662,1,1,2,3,1,1),_LinkIpConnNum_Type())
linkIpConnNum.setMaxAccess(_D)
if mibBuilder.loadTexts:linkIpConnNum.setStatus(_A)
_LinkIpIndex_Type=TableIndex
_LinkIpIndex_Object=MibTableColumn
linkIpIndex=_LinkIpIndex_Object((1,3,6,1,4,1,27662,1,1,2,3,1,2),_LinkIpIndex_Type())
linkIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:linkIpIndex.setStatus(_A)
_LinkIp_Type=IpAddress
_LinkIp_Object=MibTableColumn
linkIp=_LinkIp_Object((1,3,6,1,4,1,27662,1,1,2,3,1,3),_LinkIp_Type())
linkIp.setMaxAccess(_C)
if mibBuilder.loadTexts:linkIp.setStatus(_A)
_WanUsageTable_Object=MibTable
wanUsageTable=_WanUsageTable_Object((1,3,6,1,4,1,27662,1,1,3))
if mibBuilder.loadTexts:wanUsageTable.setStatus(_A)
_WanUsageEntry_Object=MibTableRow
wanUsageEntry=_WanUsageEntry_Object((1,3,6,1,4,1,27662,1,1,3,1))
wanUsageEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:wanUsageEntry.setStatus(_A)
_WanUsageIndex_Type=TableIndex
_WanUsageIndex_Object=MibTableColumn
wanUsageIndex=_WanUsageIndex_Object((1,3,6,1,4,1,27662,1,1,3,1,1),_WanUsageIndex_Type())
wanUsageIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wanUsageIndex.setStatus(_A)
_WanUsageThroughputIn_Type=Counter32
_WanUsageThroughputIn_Object=MibTableColumn
wanUsageThroughputIn=_WanUsageThroughputIn_Object((1,3,6,1,4,1,27662,1,1,3,1,2),_WanUsageThroughputIn_Type())
wanUsageThroughputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:wanUsageThroughputIn.setStatus(_A)
_WanUsageThroughputOut_Type=Counter32
_WanUsageThroughputOut_Object=MibTableColumn
wanUsageThroughputOut=_WanUsageThroughputOut_Object((1,3,6,1,4,1,27662,1,1,3,1,3),_WanUsageThroughputOut_Type())
wanUsageThroughputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:wanUsageThroughputOut.setStatus(_A)
_WanUsageDataTransferred_Type=Counter64
_WanUsageDataTransferred_Object=MibTableColumn
wanUsageDataTransferred=_WanUsageDataTransferred_Object((1,3,6,1,4,1,27662,1,1,3,1,4),_WanUsageDataTransferred_Type())
wanUsageDataTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:wanUsageDataTransferred.setStatus(_A)
_MaxMaintenance_ObjectIdentity=ObjectIdentity
maxMaintenance=_MaxMaintenance_ObjectIdentity((1,3,6,1,4,1,27662,1,2))
_MaxReboot_Type=NameString
_MaxReboot_Object=MibScalar
maxReboot=_MaxReboot_Object((1,3,6,1,4,1,27662,1,2,1),_MaxReboot_Type())
maxReboot.setMaxAccess(_E)
if mibBuilder.loadTexts:maxReboot.setStatus(_A)
_MaxLanConfig_ObjectIdentity=ObjectIdentity
maxLanConfig=_MaxLanConfig_ObjectIdentity((1,3,6,1,4,1,27662,1,3))
_PortLanSpeedConfig_Type=PortSpeedType
_PortLanSpeedConfig_Object=MibScalar
portLanSpeedConfig=_PortLanSpeedConfig_Object((1,3,6,1,4,1,27662,1,3,1),_PortLanSpeedConfig_Type())
portLanSpeedConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:portLanSpeedConfig.setStatus(_A)
_PortWanSpeedConfigTable_Object=MibTable
portWanSpeedConfigTable=_PortWanSpeedConfigTable_Object((1,3,6,1,4,1,27662,1,3,2))
if mibBuilder.loadTexts:portWanSpeedConfigTable.setStatus(_A)
_PortWanSpeedConfigEntry_Object=MibTableRow
portWanSpeedConfigEntry=_PortWanSpeedConfigEntry_Object((1,3,6,1,4,1,27662,1,3,2,1))
portWanSpeedConfigEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:portWanSpeedConfigEntry.setStatus(_A)
_PortWanSpeedConfigIndex_Type=TableIndex
_PortWanSpeedConfigIndex_Object=MibTableColumn
portWanSpeedConfigIndex=_PortWanSpeedConfigIndex_Object((1,3,6,1,4,1,27662,1,3,2,1,1),_PortWanSpeedConfigIndex_Type())
portWanSpeedConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portWanSpeedConfigIndex.setStatus(_A)
_PortWanSpeedConfig_Type=PortSpeedType
_PortWanSpeedConfig_Object=MibTableColumn
portWanSpeedConfig=_PortWanSpeedConfig_Object((1,3,6,1,4,1,27662,1,3,2,1,2),_PortWanSpeedConfig_Type())
portWanSpeedConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:portWanSpeedConfig.setStatus(_A)
_LanConfigIp_Type=IpAddress
_LanConfigIp_Object=MibScalar
lanConfigIp=_LanConfigIp_Object((1,3,6,1,4,1,27662,1,3,3),_LanConfigIp_Type())
lanConfigIp.setMaxAccess(_E)
if mibBuilder.loadTexts:lanConfigIp.setStatus(_A)
_LanConfigSubnetMask_Type=IpAddress
_LanConfigSubnetMask_Object=MibScalar
lanConfigSubnetMask=_LanConfigSubnetMask_Object((1,3,6,1,4,1,27662,1,3,4),_LanConfigSubnetMask_Type())
lanConfigSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:lanConfigSubnetMask.setStatus(_A)
_MaxConformance_ObjectIdentity=ObjectIdentity
maxConformance=_MaxConformance_ObjectIdentity((1,3,6,1,4,1,27662,1,50))
_MaxCompliances_ObjectIdentity=ObjectIdentity
maxCompliances=_MaxCompliances_ObjectIdentity((1,3,6,1,4,1,27662,1,50,1))
_MaxGroups_ObjectIdentity=ObjectIdentity
maxGroups=_MaxGroups_ObjectIdentity((1,3,6,1,4,1,27662,1,50,2))
maxSystemGroup=ObjectGroup((1,3,6,1,4,1,27662,1,50,2,1))
maxSystemGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:maxSystemGroup.setStatus(_A)
maxLinkGroup=ObjectGroup((1,3,6,1,4,1,27662,1,50,2,2))
maxLinkGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:maxLinkGroup.setStatus(_A)
maxWanGroup=ObjectGroup((1,3,6,1,4,1,27662,1,50,2,3))
maxWanGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:maxWanGroup.setStatus(_A)
maxSetGroup=ObjectGroup((1,3,6,1,4,1,27662,1,50,2,4))
maxSetGroup.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:maxSetGroup.setStatus(_A)
maxCompliance=ModuleCompliance((1,3,6,1,4,1,27662,1,50,1,1))
maxCompliance.setObjects(*((_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:maxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TableIndex':TableIndex,'ConnectionNum':ConnectionNum,'NameString':NameString,'PortSpeedType':PortSpeedType,'pepwaveMAX':pepwaveMAX,'maxStatus':maxStatus,'maxSystem':maxSystem,_K:maxFirmware,_L:maxSerialNumber,_M:maxTime,_N:maxUpTime,'maxLan':maxLan,_O:maxLanStatus,_P:maxLanIp,_Q:maxLanSubnetMask,'maxLinkStatus':maxLinkStatus,_R:maxLinkNumber,'linkTable':linkTable,'linkEntry':linkEntry,_F:linkConnNum,_S:linkName,_T:linkStatus,_V:linkThroughputIn,_W:linkThroughputOut,_X:linkDataTransferred,'linkIpTable':linkIpTable,'linkIpEntry':linkIpEntry,_G:linkIpConnNum,_H:linkIpIndex,_U:linkIp,'wanUsageTable':wanUsageTable,'wanUsageEntry':wanUsageEntry,_I:wanUsageIndex,_Y:wanUsageThroughputIn,_Z:wanUsageThroughputOut,_a:wanUsageDataTransferred,'maxMaintenance':maxMaintenance,_b:maxReboot,'maxLanConfig':maxLanConfig,_d:portLanSpeedConfig,'portWanSpeedConfigTable':portWanSpeedConfigTable,'portWanSpeedConfigEntry':portWanSpeedConfigEntry,_J:portWanSpeedConfigIndex,_c:portWanSpeedConfig,_e:lanConfigIp,_f:lanConfigSubnetMask,'maxConformance':maxConformance,'maxCompliances':maxCompliances,'maxCompliance':maxCompliance,'maxGroups':maxGroups,_g:maxSystemGroup,_h:maxLinkGroup,_i:maxWanGroup,_j:maxSetGroup})