_k='balSetGroup'
_j='balWanGroup'
_i='balLinkGroup'
_h='balSystemGroup'
_g='lanConfigSubnetMask'
_f='lanConfigIp'
_e='portLanSpeedConfig'
_d='portWanSpeedConfig'
_c='balReboot'
_b='wanUsageDataTransferred'
_a='wanUsageThroughputOut'
_Z='wanUsageThroughputIn'
_Y='linkDataTransferred'
_X='linkThroughputOut'
_W='linkThroughputIn'
_V='linkIp'
_U='linkStatus'
_T='linkName'
_S='balLinkNumber'
_R='balLanSubnetMask'
_Q='balLanIp'
_P='balLanStatus'
_O='balUpTime'
_N='balTime'
_M='balSerialNumber'
_L='balFirmware'
_K='portWanSpeedConfigIndex'
_J='wanUsageIndex'
_I='linkIpIndex'
_H='linkIpConnNum'
_G='linkConnNum'
_F='2009-03-05 00:00'
_E='read-write'
_D='not-accessible'
_C='read-only'
_B='PEPLINK-BALANCE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
peplinkBalance=ModuleIdentity((1,3,6,1,4,1,23695,1))
if mibBuilder.loadTexts:peplinkBalance.setRevisions((_F,_F))
class TableIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ConnectionNum(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class NameString(TextualConvention,OctetString):status=_A;displayHint='80a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
class PortSpeedType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',0),('auto',1),('fullDulplex10',2),('halfDulplex10',3),('fullDulplex100',4),('halfDulplex100',5),('fullDulplex1000',6),('halfDulplex1000',7)))
_BalanceStatus_ObjectIdentity=ObjectIdentity
balanceStatus=_BalanceStatus_ObjectIdentity((1,3,6,1,4,1,23695,1,1))
_BalanceSystem_ObjectIdentity=ObjectIdentity
balanceSystem=_BalanceSystem_ObjectIdentity((1,3,6,1,4,1,23695,1,1,1))
_BalFirmware_Type=NameString
_BalFirmware_Object=MibScalar
balFirmware=_BalFirmware_Object((1,3,6,1,4,1,23695,1,1,1,1),_BalFirmware_Type())
balFirmware.setMaxAccess(_C)
if mibBuilder.loadTexts:balFirmware.setStatus(_A)
_BalSerialNumber_Type=NameString
_BalSerialNumber_Object=MibScalar
balSerialNumber=_BalSerialNumber_Object((1,3,6,1,4,1,23695,1,1,1,2),_BalSerialNumber_Type())
balSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:balSerialNumber.setStatus(_A)
_BalTime_Type=NameString
_BalTime_Object=MibScalar
balTime=_BalTime_Object((1,3,6,1,4,1,23695,1,1,1,3),_BalTime_Type())
balTime.setMaxAccess(_C)
if mibBuilder.loadTexts:balTime.setStatus(_A)
_BalUpTime_Type=TimeTicks
_BalUpTime_Object=MibScalar
balUpTime=_BalUpTime_Object((1,3,6,1,4,1,23695,1,1,1,4),_BalUpTime_Type())
balUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:balUpTime.setStatus(_A)
_BalanceLan_ObjectIdentity=ObjectIdentity
balanceLan=_BalanceLan_ObjectIdentity((1,3,6,1,4,1,23695,1,1,1,6))
_BalLanStatus_Type=NameString
_BalLanStatus_Object=MibScalar
balLanStatus=_BalLanStatus_Object((1,3,6,1,4,1,23695,1,1,1,6,1),_BalLanStatus_Type())
balLanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:balLanStatus.setStatus(_A)
_BalLanIp_Type=IpAddress
_BalLanIp_Object=MibScalar
balLanIp=_BalLanIp_Object((1,3,6,1,4,1,23695,1,1,1,6,2),_BalLanIp_Type())
balLanIp.setMaxAccess(_C)
if mibBuilder.loadTexts:balLanIp.setStatus(_A)
_BalLanSubnetMask_Type=IpAddress
_BalLanSubnetMask_Object=MibScalar
balLanSubnetMask=_BalLanSubnetMask_Object((1,3,6,1,4,1,23695,1,1,1,6,3),_BalLanSubnetMask_Type())
balLanSubnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:balLanSubnetMask.setStatus(_A)
_BalLinkStatus_ObjectIdentity=ObjectIdentity
balLinkStatus=_BalLinkStatus_ObjectIdentity((1,3,6,1,4,1,23695,1,1,2))
_BalLinkNumber_Type=Counter32
_BalLinkNumber_Object=MibScalar
balLinkNumber=_BalLinkNumber_Object((1,3,6,1,4,1,23695,1,1,2,1),_BalLinkNumber_Type())
balLinkNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:balLinkNumber.setStatus(_A)
_LinkTable_Object=MibTable
linkTable=_LinkTable_Object((1,3,6,1,4,1,23695,1,1,2,2))
if mibBuilder.loadTexts:linkTable.setStatus(_A)
_LinkEntry_Object=MibTableRow
linkEntry=_LinkEntry_Object((1,3,6,1,4,1,23695,1,1,2,2,1))
linkEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:linkEntry.setStatus(_A)
_LinkConnNum_Type=ConnectionNum
_LinkConnNum_Object=MibTableColumn
linkConnNum=_LinkConnNum_Object((1,3,6,1,4,1,23695,1,1,2,2,1,1),_LinkConnNum_Type())
linkConnNum.setMaxAccess(_D)
if mibBuilder.loadTexts:linkConnNum.setStatus(_A)
_LinkName_Type=NameString
_LinkName_Object=MibTableColumn
linkName=_LinkName_Object((1,3,6,1,4,1,23695,1,1,2,2,1,2),_LinkName_Type())
linkName.setMaxAccess(_C)
if mibBuilder.loadTexts:linkName.setStatus(_A)
_LinkStatus_Type=NameString
_LinkStatus_Object=MibTableColumn
linkStatus=_LinkStatus_Object((1,3,6,1,4,1,23695,1,1,2,2,1,3),_LinkStatus_Type())
linkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:linkStatus.setStatus(_A)
_LinkThroughputIn_Type=Counter32
_LinkThroughputIn_Object=MibTableColumn
linkThroughputIn=_LinkThroughputIn_Object((1,3,6,1,4,1,23695,1,1,2,2,1,4),_LinkThroughputIn_Type())
linkThroughputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:linkThroughputIn.setStatus(_A)
_LinkThroughputOut_Type=Counter32
_LinkThroughputOut_Object=MibTableColumn
linkThroughputOut=_LinkThroughputOut_Object((1,3,6,1,4,1,23695,1,1,2,2,1,5),_LinkThroughputOut_Type())
linkThroughputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:linkThroughputOut.setStatus(_A)
_LinkDataTransferred_Type=Counter64
_LinkDataTransferred_Object=MibTableColumn
linkDataTransferred=_LinkDataTransferred_Object((1,3,6,1,4,1,23695,1,1,2,2,1,6),_LinkDataTransferred_Type())
linkDataTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:linkDataTransferred.setStatus(_A)
_LinkIpTable_Object=MibTable
linkIpTable=_LinkIpTable_Object((1,3,6,1,4,1,23695,1,1,2,3))
if mibBuilder.loadTexts:linkIpTable.setStatus(_A)
_LinkIpEntry_Object=MibTableRow
linkIpEntry=_LinkIpEntry_Object((1,3,6,1,4,1,23695,1,1,2,3,1))
linkIpEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:linkIpEntry.setStatus(_A)
_LinkIpConnNum_Type=ConnectionNum
_LinkIpConnNum_Object=MibTableColumn
linkIpConnNum=_LinkIpConnNum_Object((1,3,6,1,4,1,23695,1,1,2,3,1,1),_LinkIpConnNum_Type())
linkIpConnNum.setMaxAccess(_D)
if mibBuilder.loadTexts:linkIpConnNum.setStatus(_A)
_LinkIpIndex_Type=TableIndex
_LinkIpIndex_Object=MibTableColumn
linkIpIndex=_LinkIpIndex_Object((1,3,6,1,4,1,23695,1,1,2,3,1,2),_LinkIpIndex_Type())
linkIpIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:linkIpIndex.setStatus(_A)
_LinkIp_Type=IpAddress
_LinkIp_Object=MibTableColumn
linkIp=_LinkIp_Object((1,3,6,1,4,1,23695,1,1,2,3,1,3),_LinkIp_Type())
linkIp.setMaxAccess(_C)
if mibBuilder.loadTexts:linkIp.setStatus(_A)
_WanUsageTable_Object=MibTable
wanUsageTable=_WanUsageTable_Object((1,3,6,1,4,1,23695,1,1,3))
if mibBuilder.loadTexts:wanUsageTable.setStatus(_A)
_WanUsageEntry_Object=MibTableRow
wanUsageEntry=_WanUsageEntry_Object((1,3,6,1,4,1,23695,1,1,3,1))
wanUsageEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:wanUsageEntry.setStatus(_A)
_WanUsageIndex_Type=TableIndex
_WanUsageIndex_Object=MibTableColumn
wanUsageIndex=_WanUsageIndex_Object((1,3,6,1,4,1,23695,1,1,3,1,1),_WanUsageIndex_Type())
wanUsageIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wanUsageIndex.setStatus(_A)
_WanUsageThroughputIn_Type=Counter32
_WanUsageThroughputIn_Object=MibTableColumn
wanUsageThroughputIn=_WanUsageThroughputIn_Object((1,3,6,1,4,1,23695,1,1,3,1,2),_WanUsageThroughputIn_Type())
wanUsageThroughputIn.setMaxAccess(_C)
if mibBuilder.loadTexts:wanUsageThroughputIn.setStatus(_A)
_WanUsageThroughputOut_Type=Counter32
_WanUsageThroughputOut_Object=MibTableColumn
wanUsageThroughputOut=_WanUsageThroughputOut_Object((1,3,6,1,4,1,23695,1,1,3,1,3),_WanUsageThroughputOut_Type())
wanUsageThroughputOut.setMaxAccess(_C)
if mibBuilder.loadTexts:wanUsageThroughputOut.setStatus(_A)
_WanUsageDataTransferred_Type=Counter64
_WanUsageDataTransferred_Object=MibTableColumn
wanUsageDataTransferred=_WanUsageDataTransferred_Object((1,3,6,1,4,1,23695,1,1,3,1,4),_WanUsageDataTransferred_Type())
wanUsageDataTransferred.setMaxAccess(_C)
if mibBuilder.loadTexts:wanUsageDataTransferred.setStatus(_A)
_BalanceMaintenance_ObjectIdentity=ObjectIdentity
balanceMaintenance=_BalanceMaintenance_ObjectIdentity((1,3,6,1,4,1,23695,1,2))
_BalReboot_Type=NameString
_BalReboot_Object=MibScalar
balReboot=_BalReboot_Object((1,3,6,1,4,1,23695,1,2,1),_BalReboot_Type())
balReboot.setMaxAccess(_E)
if mibBuilder.loadTexts:balReboot.setStatus(_A)
_BalanceLanConfig_ObjectIdentity=ObjectIdentity
balanceLanConfig=_BalanceLanConfig_ObjectIdentity((1,3,6,1,4,1,23695,1,3))
_PortLanSpeedConfig_Type=PortSpeedType
_PortLanSpeedConfig_Object=MibScalar
portLanSpeedConfig=_PortLanSpeedConfig_Object((1,3,6,1,4,1,23695,1,3,1),_PortLanSpeedConfig_Type())
portLanSpeedConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:portLanSpeedConfig.setStatus(_A)
_PortWanSpeedConfigTable_Object=MibTable
portWanSpeedConfigTable=_PortWanSpeedConfigTable_Object((1,3,6,1,4,1,23695,1,3,2))
if mibBuilder.loadTexts:portWanSpeedConfigTable.setStatus(_A)
_PortWanSpeedConfigEntry_Object=MibTableRow
portWanSpeedConfigEntry=_PortWanSpeedConfigEntry_Object((1,3,6,1,4,1,23695,1,3,2,1))
portWanSpeedConfigEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:portWanSpeedConfigEntry.setStatus(_A)
_PortWanSpeedConfigIndex_Type=TableIndex
_PortWanSpeedConfigIndex_Object=MibTableColumn
portWanSpeedConfigIndex=_PortWanSpeedConfigIndex_Object((1,3,6,1,4,1,23695,1,3,2,1,1),_PortWanSpeedConfigIndex_Type())
portWanSpeedConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:portWanSpeedConfigIndex.setStatus(_A)
_PortWanSpeedConfig_Type=PortSpeedType
_PortWanSpeedConfig_Object=MibTableColumn
portWanSpeedConfig=_PortWanSpeedConfig_Object((1,3,6,1,4,1,23695,1,3,2,1,2),_PortWanSpeedConfig_Type())
portWanSpeedConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:portWanSpeedConfig.setStatus(_A)
_LanConfigIp_Type=IpAddress
_LanConfigIp_Object=MibScalar
lanConfigIp=_LanConfigIp_Object((1,3,6,1,4,1,23695,1,3,3),_LanConfigIp_Type())
lanConfigIp.setMaxAccess(_E)
if mibBuilder.loadTexts:lanConfigIp.setStatus(_A)
_LanConfigSubnetMask_Type=IpAddress
_LanConfigSubnetMask_Object=MibScalar
lanConfigSubnetMask=_LanConfigSubnetMask_Object((1,3,6,1,4,1,23695,1,3,4),_LanConfigSubnetMask_Type())
lanConfigSubnetMask.setMaxAccess(_E)
if mibBuilder.loadTexts:lanConfigSubnetMask.setStatus(_A)
_BalanceConformance_ObjectIdentity=ObjectIdentity
balanceConformance=_BalanceConformance_ObjectIdentity((1,3,6,1,4,1,23695,1,50))
_BalCompliances_ObjectIdentity=ObjectIdentity
balCompliances=_BalCompliances_ObjectIdentity((1,3,6,1,4,1,23695,1,50,1))
_BalGroups_ObjectIdentity=ObjectIdentity
balGroups=_BalGroups_ObjectIdentity((1,3,6,1,4,1,23695,1,50,2))
balSystemGroup=ObjectGroup((1,3,6,1,4,1,23695,1,50,2,1))
balSystemGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:balSystemGroup.setStatus(_A)
balLinkGroup=ObjectGroup((1,3,6,1,4,1,23695,1,50,2,2))
balLinkGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:balLinkGroup.setStatus(_A)
balWanGroup=ObjectGroup((1,3,6,1,4,1,23695,1,50,2,3))
balWanGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:balWanGroup.setStatus(_A)
balSetGroup=ObjectGroup((1,3,6,1,4,1,23695,1,50,2,4))
balSetGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:balSetGroup.setStatus(_A)
balCompliance=ModuleCompliance((1,3,6,1,4,1,23695,1,50,1,1))
balCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:balCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TableIndex':TableIndex,'ConnectionNum':ConnectionNum,'NameString':NameString,'PortSpeedType':PortSpeedType,'peplinkBalance':peplinkBalance,'balanceStatus':balanceStatus,'balanceSystem':balanceSystem,_L:balFirmware,_M:balSerialNumber,_N:balTime,_O:balUpTime,'balanceLan':balanceLan,_P:balLanStatus,_Q:balLanIp,_R:balLanSubnetMask,'balLinkStatus':balLinkStatus,_S:balLinkNumber,'linkTable':linkTable,'linkEntry':linkEntry,_G:linkConnNum,_T:linkName,_U:linkStatus,_W:linkThroughputIn,_X:linkThroughputOut,_Y:linkDataTransferred,'linkIpTable':linkIpTable,'linkIpEntry':linkIpEntry,_H:linkIpConnNum,_I:linkIpIndex,_V:linkIp,'wanUsageTable':wanUsageTable,'wanUsageEntry':wanUsageEntry,_J:wanUsageIndex,_Z:wanUsageThroughputIn,_a:wanUsageThroughputOut,_b:wanUsageDataTransferred,'balanceMaintenance':balanceMaintenance,_c:balReboot,'balanceLanConfig':balanceLanConfig,_e:portLanSpeedConfig,'portWanSpeedConfigTable':portWanSpeedConfigTable,'portWanSpeedConfigEntry':portWanSpeedConfigEntry,_K:portWanSpeedConfigIndex,_d:portWanSpeedConfig,_f:lanConfigIp,_g:lanConfigSubnetMask,'balanceConformance':balanceConformance,'balCompliances':balCompliances,'balCompliance':balCompliance,'balGroups':balGroups,_h:balSystemGroup,_i:balLinkGroup,_j:balWanGroup,_k:balSetGroup})