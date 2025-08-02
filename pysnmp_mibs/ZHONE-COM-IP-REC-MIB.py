_T='ipUnnumberedIndex'
_S='not-accessible'
_R='ipIfAliasAddr'
_Q='ZhoneRDIndex'
_P='InterfaceIndexOrZero'
_O='InterfaceIndex'
_N='AtmVpIdentifier'
_M='AtmVcIdentifier'
_L='ZHONE-COM-IP-REC-MIB'
_K='Unsigned32'
_J='ifIndex'
_I='IF-MIB'
_H='read-write'
_G='deprecated'
_F='00000000'
_E='IpAddress'
_D='TruthValue'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB',_M,_N)
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_I,_O,_P,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_E,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
ZhoneRDIndex,=mibBuilder.importSymbols('ZHONE-COM-IP-RD-MIB',_Q)
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneAdminString,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString','ZhoneRowStatus')
ipRecord=ModuleIdentity((1,3,6,1,4,1,5504,6,59))
if mibBuilder.loadTexts:ipRecord.setRevisions(('2010-09-01 09:17','2010-05-04 02:24','2008-06-27 08:14','2006-02-17 17:37','2006-01-23 09:26','2005-07-20 17:22','2004-07-21 08:46','2004-05-27 09:56','2004-04-28 14:02','2003-04-18 10:03','2002-04-17 16:48','2002-02-11 16:57','2001-10-30 10:44','2001-06-06 16:00','2001-03-15 10:28','2001-02-26 13:58','2001-02-13 11:13','2001-01-19 18:16','2001-01-17 16:18','2000-11-20 10:18','2000-10-05 15:12','2000-09-15 14:30','2000-09-12 10:06'))
_IpRecordObjects_ObjectIdentity=ObjectIdentity
ipRecordObjects=_IpRecordObjects_ObjectIdentity((1,3,6,1,4,1,5504,4,1,9))
if mibBuilder.loadTexts:ipRecordObjects.setStatus(_A)
_IpInterfaceTable_Object=MibTable
ipInterfaceTable=_IpInterfaceTable_Object((1,3,6,1,4,1,5504,4,1,9,2))
if mibBuilder.loadTexts:ipInterfaceTable.setStatus(_A)
_IpInterfaceEntry_Object=MibTableRow
ipInterfaceEntry=_IpInterfaceEntry_Object((1,3,6,1,4,1,5504,4,1,9,2,1))
ipInterfaceEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:ipInterfaceEntry.setStatus(_A)
class _IpIfLgId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IpIfLgId_Type.__name__=_C
_IpIfLgId_Object=MibTableColumn
ipIfLgId=_IpIfLgId_Object((1,3,6,1,4,1,5504,4,1,9,2,1,1),_IpIfLgId_Type())
ipIfLgId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfLgId.setStatus('obsolete')
class _IpIfVpi_Type(AtmVpIdentifier):defaultValue=0
_IpIfVpi_Type.__name__=_N
_IpIfVpi_Object=MibTableColumn
ipIfVpi=_IpIfVpi_Object((1,3,6,1,4,1,5504,4,1,9,2,1,2),_IpIfVpi_Type())
ipIfVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfVpi.setStatus(_A)
class _IpIfVci_Type(AtmVcIdentifier):defaultValue=0
_IpIfVci_Type.__name__=_M
_IpIfVci_Object=MibTableColumn
ipIfVci=_IpIfVci_Object((1,3,6,1,4,1,5504,4,1,9,2,1,3),_IpIfVci_Type())
ipIfVci.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfVci.setStatus(_A)
class _IpIfRDIndex_Type(ZhoneRDIndex):defaultValue=0
_IpIfRDIndex_Type.__name__=_Q
_IpIfRDIndex_Object=MibTableColumn
ipIfRDIndex=_IpIfRDIndex_Object((1,3,6,1,4,1,5504,4,1,9,2,1,4),_IpIfRDIndex_Type())
ipIfRDIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfRDIndex.setStatus(_A)
class _IpIfDhcp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noDhcp',1),('dhcpClient',2),('dhcpServer',3),('dhcpBoth',4)))
_IpIfDhcp_Type.__name__=_C
_IpIfDhcp_Object=MibTableColumn
ipIfDhcp=_IpIfDhcp_Object((1,3,6,1,4,1,5504,4,1,9,2,1,5),_IpIfDhcp_Type())
ipIfDhcp.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfDhcp.setStatus(_G)
class _IpIfAddr_Type(IpAddress):defaultHexValue=_F
_IpIfAddr_Type.__name__=_E
_IpIfAddr_Object=MibTableColumn
ipIfAddr=_IpIfAddr_Object((1,3,6,1,4,1,5504,4,1,9,2,1,6),_IpIfAddr_Type())
ipIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfAddr.setStatus(_A)
class _IpIfNetMask_Type(IpAddress):defaultHexValue=_F
_IpIfNetMask_Type.__name__=_E
_IpIfNetMask_Object=MibTableColumn
ipIfNetMask=_IpIfNetMask_Object((1,3,6,1,4,1,5504,4,1,9,2,1,7),_IpIfNetMask_Type())
ipIfNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfNetMask.setStatus(_A)
class _IpIfBcastAddr_Type(IpAddress):defaultHexValue=_F
_IpIfBcastAddr_Type.__name__=_E
_IpIfBcastAddr_Object=MibTableColumn
ipIfBcastAddr=_IpIfBcastAddr_Object((1,3,6,1,4,1,5504,4,1,9,2,1,8),_IpIfBcastAddr_Type())
ipIfBcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfBcastAddr.setStatus(_A)
class _IpIfDestAddr_Type(IpAddress):defaultHexValue=_F
_IpIfDestAddr_Type.__name__=_E
_IpIfDestAddr_Object=MibTableColumn
ipIfDestAddr=_IpIfDestAddr_Object((1,3,6,1,4,1,5504,4,1,9,2,1,9),_IpIfDestAddr_Type())
ipIfDestAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfDestAddr.setStatus(_A)
class _IpIfFarEndAddr_Type(IpAddress):defaultHexValue=_F
_IpIfFarEndAddr_Type.__name__=_E
_IpIfFarEndAddr_Object=MibTableColumn
ipIfFarEndAddr=_IpIfFarEndAddr_Object((1,3,6,1,4,1,5504,4,1,9,2,1,10),_IpIfFarEndAddr_Type())
ipIfFarEndAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfFarEndAddr.setStatus(_A)
class _IpIfMru_Type(Unsigned32):defaultValue=1500
_IpIfMru_Type.__name__=_K
_IpIfMru_Object=MibTableColumn
ipIfMru=_IpIfMru_Object((1,3,6,1,4,1,5504,4,1,9,2,1,11),_IpIfMru_Type())
ipIfMru.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfMru.setStatus(_A)
class _IpIfReasmMaxSize_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_IpIfReasmMaxSize_Type.__name__=_C
_IpIfReasmMaxSize_Object=MibTableColumn
ipIfReasmMaxSize=_IpIfReasmMaxSize_Object((1,3,6,1,4,1,5504,4,1,9,2,1,12),_IpIfReasmMaxSize_Type())
ipIfReasmMaxSize.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfReasmMaxSize.setStatus(_A)
_IpIfIngressFilterName_Type=ZhoneAdminString
_IpIfIngressFilterName_Object=MibTableColumn
ipIfIngressFilterName=_IpIfIngressFilterName_Object((1,3,6,1,4,1,5504,4,1,9,2,1,13),_IpIfIngressFilterName_Type())
ipIfIngressFilterName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfIngressFilterName.setStatus(_G)
_IpIfEgressFilterName_Type=ZhoneAdminString
_IpIfEgressFilterName_Object=MibTableColumn
ipIfEgressFilterName=_IpIfEgressFilterName_Object((1,3,6,1,4,1,5504,4,1,9,2,1,14),_IpIfEgressFilterName_Type())
ipIfEgressFilterName.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfEgressFilterName.setStatus(_G)
class _IpIfPointToPoint_Type(TruthValue):defaultValue=2
_IpIfPointToPoint_Type.__name__=_D
_IpIfPointToPoint_Object=MibTableColumn
ipIfPointToPoint=_IpIfPointToPoint_Object((1,3,6,1,4,1,5504,4,1,9,2,1,15),_IpIfPointToPoint_Type())
ipIfPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfPointToPoint.setStatus(_A)
class _IpIfMcastEnabled_Type(TruthValue):defaultValue=1
_IpIfMcastEnabled_Type.__name__=_D
_IpIfMcastEnabled_Object=MibTableColumn
ipIfMcastEnabled=_IpIfMcastEnabled_Object((1,3,6,1,4,1,5504,4,1,9,2,1,16),_IpIfMcastEnabled_Type())
ipIfMcastEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfMcastEnabled.setStatus(_A)
class _IpIfIpFwdEnabled_Type(TruthValue):defaultValue=1
_IpIfIpFwdEnabled_Type.__name__=_D
_IpIfIpFwdEnabled_Object=MibTableColumn
ipIfIpFwdEnabled=_IpIfIpFwdEnabled_Object((1,3,6,1,4,1,5504,4,1,9,2,1,17),_IpIfIpFwdEnabled_Type())
ipIfIpFwdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfIpFwdEnabled.setStatus(_A)
class _IpIfMcastFwdEnabled_Type(TruthValue):defaultValue=1
_IpIfMcastFwdEnabled_Type.__name__=_D
_IpIfMcastFwdEnabled_Object=MibTableColumn
ipIfMcastFwdEnabled=_IpIfMcastFwdEnabled_Object((1,3,6,1,4,1,5504,4,1,9,2,1,18),_IpIfMcastFwdEnabled_Type())
ipIfMcastFwdEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfMcastFwdEnabled.setStatus(_A)
class _IpIfNATEnabled_Type(TruthValue):defaultValue=2
_IpIfNATEnabled_Type.__name__=_D
_IpIfNATEnabled_Object=MibTableColumn
ipIfNATEnabled=_IpIfNATEnabled_Object((1,3,6,1,4,1,5504,4,1,9,2,1,19),_IpIfNATEnabled_Type())
ipIfNATEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfNATEnabled.setStatus(_A)
class _IpIfBcastEnabled_Type(TruthValue):defaultValue=1
_IpIfBcastEnabled_Type.__name__=_D
_IpIfBcastEnabled_Object=MibTableColumn
ipIfBcastEnabled=_IpIfBcastEnabled_Object((1,3,6,1,4,1,5504,4,1,9,2,1,20),_IpIfBcastEnabled_Type())
ipIfBcastEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfBcastEnabled.setStatus(_A)
_IpIfRowStatus_Type=ZhoneRowStatus
_IpIfRowStatus_Object=MibTableColumn
ipIfRowStatus=_IpIfRowStatus_Object((1,3,6,1,4,1,5504,4,1,9,2,1,21),_IpIfRowStatus_Type())
ipIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfRowStatus.setStatus(_A)
class _IpIfAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_IpIfAdminStatus_Type.__name__=_C
_IpIfAdminStatus_Object=MibTableColumn
ipIfAdminStatus=_IpIfAdminStatus_Object((1,3,6,1,4,1,5504,4,1,9,2,1,22),_IpIfAdminStatus_Type())
ipIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfAdminStatus.setStatus(_A)
class _IpIfIngressPacketRuleGroupIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IpIfIngressPacketRuleGroupIndex_Type.__name__=_C
_IpIfIngressPacketRuleGroupIndex_Object=MibTableColumn
ipIfIngressPacketRuleGroupIndex=_IpIfIngressPacketRuleGroupIndex_Object((1,3,6,1,4,1,5504,4,1,9,2,1,23),_IpIfIngressPacketRuleGroupIndex_Type())
ipIfIngressPacketRuleGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfIngressPacketRuleGroupIndex.setStatus(_A)
class _IpIfEgressPacketRuleGroupIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IpIfEgressPacketRuleGroupIndex_Type.__name__=_C
_IpIfEgressPacketRuleGroupIndex_Object=MibTableColumn
ipIfEgressPacketRuleGroupIndex=_IpIfEgressPacketRuleGroupIndex_Object((1,3,6,1,4,1,5504,4,1,9,2,1,24),_IpIfEgressPacketRuleGroupIndex_Type())
ipIfEgressPacketRuleGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfEgressPacketRuleGroupIndex.setStatus(_A)
_IpIfLowerIfIndex_Type=InterfaceIndexOrZero
_IpIfLowerIfIndex_Object=MibTableColumn
ipIfLowerIfIndex=_IpIfLowerIfIndex_Object((1,3,6,1,4,1,5504,4,1,9,2,1,25),_IpIfLowerIfIndex_Type())
ipIfLowerIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfLowerIfIndex.setStatus(_A)
class _IpIfPppEnabled_Type(TruthValue):defaultValue=2
_IpIfPppEnabled_Type.__name__=_D
_IpIfPppEnabled_Object=MibTableColumn
ipIfPppEnabled=_IpIfPppEnabled_Object((1,3,6,1,4,1,5504,4,1,9,2,1,26),_IpIfPppEnabled_Type())
ipIfPppEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfPppEnabled.setStatus(_A)
class _IpAddrDynamic_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('static',1),('ppp',2),('dhcpclient',3),('unnumbered',4),('cpemgr',5)))
_IpAddrDynamic_Type.__name__=_C
_IpAddrDynamic_Object=MibTableColumn
ipAddrDynamic=_IpAddrDynamic_Object((1,3,6,1,4,1,5504,4,1,9,2,1,27),_IpAddrDynamic_Type())
ipAddrDynamic.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAddrDynamic.setStatus(_A)
class _DhcpServerEnable_Type(TruthValue):defaultValue=2
_DhcpServerEnable_Type.__name__=_D
_DhcpServerEnable_Object=MibTableColumn
dhcpServerEnable=_DhcpServerEnable_Object((1,3,6,1,4,1,5504,4,1,9,2,1,28),_DhcpServerEnable_Type())
dhcpServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpServerEnable.setStatus(_A)
class _DhcpSubnetGroup_Type(Integer32):defaultValue=0
_DhcpSubnetGroup_Type.__name__=_C
_DhcpSubnetGroup_Object=MibTableColumn
dhcpSubnetGroup=_DhcpSubnetGroup_Object((1,3,6,1,4,1,5504,4,1,9,2,1,29),_DhcpSubnetGroup_Type())
dhcpSubnetGroup.setMaxAccess(_H)
if mibBuilder.loadTexts:dhcpSubnetGroup.setStatus(_A)
class _UnnumberedIndex_Type(Integer32):defaultValue=0
_UnnumberedIndex_Type.__name__=_C
_UnnumberedIndex_Object=MibTableColumn
unnumberedIndex=_UnnumberedIndex_Object((1,3,6,1,4,1,5504,4,1,9,2,1,30),_UnnumberedIndex_Type())
unnumberedIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:unnumberedIndex.setStatus(_A)
_McastControlList_Type=SnmpAdminString
_McastControlList_Object=MibTableColumn
mcastControlList=_McastControlList_Object((1,3,6,1,4,1,5504,4,1,9,2,1,31),_McastControlList_Type())
mcastControlList.setMaxAccess(_B)
if mibBuilder.loadTexts:mcastControlList.setStatus(_A)
class _Vlanid_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Vlanid_Type.__name__=_C
_Vlanid_Object=MibTableColumn
vlanid=_Vlanid_Object((1,3,6,1,4,1,5504,4,1,9,2,1,32),_Vlanid_Type())
vlanid.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanid.setStatus(_A)
class _MaxVideoStreams_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_MaxVideoStreams_Type.__name__=_K
_MaxVideoStreams_Object=MibTableColumn
maxVideoStreams=_MaxVideoStreams_Object((1,3,6,1,4,1,5504,4,1,9,2,1,33),_MaxVideoStreams_Type())
maxVideoStreams.setMaxAccess(_B)
if mibBuilder.loadTexts:maxVideoStreams.setStatus(_A)
class _TosOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tosOptionDisable',1),('tosOptionOriginate',2),('tosOptionAll',3)))
_TosOption_Type.__name__=_C
_TosOption_Object=MibTableColumn
tosOption=_TosOption_Object((1,3,6,1,4,1,5504,4,1,9,2,1,34),_TosOption_Type())
tosOption.setMaxAccess(_B)
if mibBuilder.loadTexts:tosOption.setStatus(_A)
class _TosCOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_TosCOS_Type.__name__=_C
_TosCOS_Object=MibTableColumn
tosCOS=_TosCOS_Object((1,3,6,1,4,1,5504,4,1,9,2,1,35),_TosCOS_Type())
tosCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:tosCOS.setStatus(_A)
class _VlanCOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_VlanCOS_Type.__name__=_C
_VlanCOS_Object=MibTableColumn
vlanCOS=_VlanCOS_Object((1,3,6,1,4,1,5504,4,1,9,2,1,36),_VlanCOS_Type())
vlanCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanCOS.setStatus(_A)
class _IpStagTPID_Type(Integer32):defaultValue=33024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(33024,33024),ValueRangeConstraint(34984,34984),ValueRangeConstraint(37120,37120),ValueRangeConstraint(37376,37376))
_IpStagTPID_Type.__name__=_C
_IpStagTPID_Object=MibTableColumn
ipStagTPID=_IpStagTPID_Object((1,3,6,1,4,1,5504,4,1,9,2,1,37),_IpStagTPID_Type())
ipStagTPID.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStagTPID.setStatus(_A)
class _IpStagId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_IpStagId_Type.__name__=_C
_IpStagId_Object=MibTableColumn
ipStagId=_IpStagId_Object((1,3,6,1,4,1,5504,4,1,9,2,1,38),_IpStagId_Type())
ipStagId.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStagId.setStatus(_A)
class _IpStagIdCOS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_IpStagIdCOS_Type.__name__=_C
_IpStagIdCOS_Object=MibTableColumn
ipStagIdCOS=_IpStagIdCOS_Object((1,3,6,1,4,1,5504,4,1,9,2,1,39),_IpStagIdCOS_Type())
ipStagIdCOS.setMaxAccess(_B)
if mibBuilder.loadTexts:ipStagIdCOS.setStatus(_A)
class _IpOnDemandStatsEnabled_Type(TruthValue):defaultValue=2
_IpOnDemandStatsEnabled_Type.__name__=_D
_IpOnDemandStatsEnabled_Object=MibTableColumn
ipOnDemandStatsEnabled=_IpOnDemandStatsEnabled_Object((1,3,6,1,4,1,5504,4,1,9,2,1,40),_IpOnDemandStatsEnabled_Type())
ipOnDemandStatsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ipOnDemandStatsEnabled.setStatus(_A)
_IpIfAliasTable_Object=MibTable
ipIfAliasTable=_IpIfAliasTable_Object((1,3,6,1,4,1,5504,4,1,9,5))
if mibBuilder.loadTexts:ipIfAliasTable.setStatus(_A)
_IpIfAliasEntry_Object=MibTableRow
ipIfAliasEntry=_IpIfAliasEntry_Object((1,3,6,1,4,1,5504,4,1,9,5,1))
ipIfAliasEntry.setIndexNames((0,_I,_J),(0,_L,_R))
if mibBuilder.loadTexts:ipIfAliasEntry.setStatus(_A)
_IpIfAliasAddr_Type=IpAddress
_IpIfAliasAddr_Object=MibTableColumn
ipIfAliasAddr=_IpIfAliasAddr_Object((1,3,6,1,4,1,5504,4,1,9,5,1,1),_IpIfAliasAddr_Type())
ipIfAliasAddr.setMaxAccess(_S)
if mibBuilder.loadTexts:ipIfAliasAddr.setStatus(_A)
_IpIfAliasRowStatus_Type=ZhoneRowStatus
_IpIfAliasRowStatus_Object=MibTableColumn
ipIfAliasRowStatus=_IpIfAliasRowStatus_Object((1,3,6,1,4,1,5504,4,1,9,5,1,2),_IpIfAliasRowStatus_Type())
ipIfAliasRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfAliasRowStatus.setStatus(_A)
class _IpIfAliasNetMask_Type(IpAddress):defaultHexValue=_F
_IpIfAliasNetMask_Type.__name__=_E
_IpIfAliasNetMask_Object=MibTableColumn
ipIfAliasNetMask=_IpIfAliasNetMask_Object((1,3,6,1,4,1,5504,4,1,9,5,1,3),_IpIfAliasNetMask_Type())
ipIfAliasNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfAliasNetMask.setStatus(_A)
class _IpIfAliasBcastAddr_Type(IpAddress):defaultHexValue=_F
_IpIfAliasBcastAddr_Type.__name__=_E
_IpIfAliasBcastAddr_Object=MibTableColumn
ipIfAliasBcastAddr=_IpIfAliasBcastAddr_Object((1,3,6,1,4,1,5504,4,1,9,5,1,4),_IpIfAliasBcastAddr_Type())
ipIfAliasBcastAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ipIfAliasBcastAddr.setStatus(_A)
_IpUnnumbered_ObjectIdentity=ObjectIdentity
ipUnnumbered=_IpUnnumbered_ObjectIdentity((1,3,6,1,4,1,5504,4,1,10))
if mibBuilder.loadTexts:ipUnnumbered.setStatus(_G)
class _IpUnnumberedEnabled_Type(TruthValue):defaultValue=2
_IpUnnumberedEnabled_Type.__name__=_D
_IpUnnumberedEnabled_Object=MibScalar
ipUnnumberedEnabled=_IpUnnumberedEnabled_Object((1,3,6,1,4,1,5504,4,1,10,1),_IpUnnumberedEnabled_Type())
ipUnnumberedEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:ipUnnumberedEnabled.setStatus(_G)
class _IpUnnumberedInterfaceIndex_Type(InterfaceIndexOrZero):defaultValue=0
_IpUnnumberedInterfaceIndex_Type.__name__=_P
_IpUnnumberedInterfaceIndex_Object=MibScalar
ipUnnumberedInterfaceIndex=_IpUnnumberedInterfaceIndex_Object((1,3,6,1,4,1,5504,4,1,10,2),_IpUnnumberedInterfaceIndex_Type())
ipUnnumberedInterfaceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ipUnnumberedInterfaceIndex.setStatus(_G)
_IpUnnumberedObjects_ObjectIdentity=ObjectIdentity
ipUnnumberedObjects=_IpUnnumberedObjects_ObjectIdentity((1,3,6,1,4,1,5504,4,1,14))
_IpUnnumberedObjectNext_Type=Integer32
_IpUnnumberedObjectNext_Object=MibScalar
ipUnnumberedObjectNext=_IpUnnumberedObjectNext_Object((1,3,6,1,4,1,5504,4,1,14,1),_IpUnnumberedObjectNext_Type())
ipUnnumberedObjectNext.setMaxAccess('read-only')
if mibBuilder.loadTexts:ipUnnumberedObjectNext.setStatus(_A)
_IpUnnumberedTable_Object=MibTable
ipUnnumberedTable=_IpUnnumberedTable_Object((1,3,6,1,4,1,5504,4,1,14,2))
if mibBuilder.loadTexts:ipUnnumberedTable.setStatus(_A)
_IpUnnumberedEntry_Object=MibTableRow
ipUnnumberedEntry=_IpUnnumberedEntry_Object((1,3,6,1,4,1,5504,4,1,14,2,1))
ipUnnumberedEntry.setIndexNames((0,_L,_T))
if mibBuilder.loadTexts:ipUnnumberedEntry.setStatus(_A)
class _IpUnnumberedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_IpUnnumberedIndex_Type.__name__=_C
_IpUnnumberedIndex_Object=MibTableColumn
ipUnnumberedIndex=_IpUnnumberedIndex_Object((1,3,6,1,4,1,5504,4,1,14,2,1,1),_IpUnnumberedIndex_Type())
ipUnnumberedIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:ipUnnumberedIndex.setStatus(_A)
_IpUnnumberedRowStatus_Type=ZhoneRowStatus
_IpUnnumberedRowStatus_Object=MibTableColumn
ipUnnumberedRowStatus=_IpUnnumberedRowStatus_Object((1,3,6,1,4,1,5504,4,1,14,2,1,2),_IpUnnumberedRowStatus_Type())
ipUnnumberedRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ipUnnumberedRowStatus.setStatus(_A)
class _IpUnnumberedIfIName_Type(InterfaceIndex):defaultValue=1
_IpUnnumberedIfIName_Type.__name__=_O
_IpUnnumberedIfIName_Object=MibTableColumn
ipUnnumberedIfIName=_IpUnnumberedIfIName_Object((1,3,6,1,4,1,5504,4,1,14,2,1,3),_IpUnnumberedIfIName_Type())
ipUnnumberedIfIName.setMaxAccess(_H)
if mibBuilder.loadTexts:ipUnnumberedIfIName.setStatus(_A)
mibBuilder.exportSymbols(_L,**{'ipRecordObjects':ipRecordObjects,'ipInterfaceTable':ipInterfaceTable,'ipInterfaceEntry':ipInterfaceEntry,'ipIfLgId':ipIfLgId,'ipIfVpi':ipIfVpi,'ipIfVci':ipIfVci,'ipIfRDIndex':ipIfRDIndex,'ipIfDhcp':ipIfDhcp,'ipIfAddr':ipIfAddr,'ipIfNetMask':ipIfNetMask,'ipIfBcastAddr':ipIfBcastAddr,'ipIfDestAddr':ipIfDestAddr,'ipIfFarEndAddr':ipIfFarEndAddr,'ipIfMru':ipIfMru,'ipIfReasmMaxSize':ipIfReasmMaxSize,'ipIfIngressFilterName':ipIfIngressFilterName,'ipIfEgressFilterName':ipIfEgressFilterName,'ipIfPointToPoint':ipIfPointToPoint,'ipIfMcastEnabled':ipIfMcastEnabled,'ipIfIpFwdEnabled':ipIfIpFwdEnabled,'ipIfMcastFwdEnabled':ipIfMcastFwdEnabled,'ipIfNATEnabled':ipIfNATEnabled,'ipIfBcastEnabled':ipIfBcastEnabled,'ipIfRowStatus':ipIfRowStatus,'ipIfAdminStatus':ipIfAdminStatus,'ipIfIngressPacketRuleGroupIndex':ipIfIngressPacketRuleGroupIndex,'ipIfEgressPacketRuleGroupIndex':ipIfEgressPacketRuleGroupIndex,'ipIfLowerIfIndex':ipIfLowerIfIndex,'ipIfPppEnabled':ipIfPppEnabled,'ipAddrDynamic':ipAddrDynamic,'dhcpServerEnable':dhcpServerEnable,'dhcpSubnetGroup':dhcpSubnetGroup,'unnumberedIndex':unnumberedIndex,'mcastControlList':mcastControlList,'vlanid':vlanid,'maxVideoStreams':maxVideoStreams,'tosOption':tosOption,'tosCOS':tosCOS,'vlanCOS':vlanCOS,'ipStagTPID':ipStagTPID,'ipStagId':ipStagId,'ipStagIdCOS':ipStagIdCOS,'ipOnDemandStatsEnabled':ipOnDemandStatsEnabled,'ipIfAliasTable':ipIfAliasTable,'ipIfAliasEntry':ipIfAliasEntry,_R:ipIfAliasAddr,'ipIfAliasRowStatus':ipIfAliasRowStatus,'ipIfAliasNetMask':ipIfAliasNetMask,'ipIfAliasBcastAddr':ipIfAliasBcastAddr,'ipUnnumbered':ipUnnumbered,'ipUnnumberedEnabled':ipUnnumberedEnabled,'ipUnnumberedInterfaceIndex':ipUnnumberedInterfaceIndex,'ipUnnumberedObjects':ipUnnumberedObjects,'ipUnnumberedObjectNext':ipUnnumberedObjectNext,'ipUnnumberedTable':ipUnnumberedTable,'ipUnnumberedEntry':ipUnnumberedEntry,_T:ipUnnumberedIndex,'ipUnnumberedRowStatus':ipUnnumberedRowStatus,'ipUnnumberedIfIName':ipUnnumberedIfIName,'ipRecord':ipRecord})