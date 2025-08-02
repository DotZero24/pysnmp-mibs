_Aq='cvsVSLLinkPortGroup'
_Ap='cvsDualActiveDetectionNotif'
_Ao='cvsVSLConnectionChangeNotif'
_An='cvsVSLLinkPeerInterface'
_Am='cvsDualActiveDetectionNotifEnable'
_Al='cvsCoreSwitchLocation'
_Ak='cvsModuleRprWarm'
_Aj='cvsVSLPortRxPeerInfoMismatchPkts'
_Ai='cvsVSLPortRxDomainIdMismatchPkts'
_Ah='cvsVSLPortRxBadSwitchIdPkts'
_Ag='cvsVSLPortRxBadMacAddressPkts'
_Af='cvsVSLPortRxMyInfoAbsentPkts'
_Ae='cvsVSLPortRxMyInfoMismatchPkts'
_Ad='cvsVSLRxChksumErrHCPkts'
_Ac='cvsVSLRxErrorHCPkts'
_Ab='cvsVSLRxTotalHCPkts'
_Aa='cvsVSLTxChksumErrHCPkts'
_AZ='cvsVSLTxErrorHCPkts'
_AY='cvsVSLTxTotalHCPkts'
_AX='cvsVSLRxAckEobcPkts'
_AW='cvsVSLRxDataEobcPkts'
_AV='cvsVSLRxProtoEobcPkts'
_AU='cvsVSLRxPingEobcPkts'
_AT='cvsVSLRxRrpEobcPkts'
_AS='cvsVSLRxLmpEobcPkts'
_AR='cvsVSLRxTotalEobcPkts'
_AQ='cvsVSLTxAckEobcPkts'
_AP='cvsVSLTxDataEobcPkts'
_AO='cvsVSLTxProtoEobcPkts'
_AN='cvsVSLTxPingEobcPkts'
_AM='cvsVSLTxRrpEobcPkts'
_AL='cvsVSLTxLmpEobcPkts'
_AK='cvsVSLTxTotalEobcPkts'
_AJ='cvsVSLRxAckPkts'
_AI='cvsVSLRxDataPkts'
_AH='cvsVSLRxProtoPkts'
_AG='cvsVSLRxPingPkts'
_AF='cvsVSLRxRrpPkts'
_AE='cvsVSLRxLmpPkts'
_AD='cvsVSLTxAckPkts'
_AC='cvsVSLTxDataPkts'
_AB='cvsVSLTxProtoPkts'
_AA='cvsVSLTxPingPkts'
_A9='cvsVSLTxRrpPkts'
_A8='cvsVSLTxLmpPkts'
_A7='cvsModuleSlotNumber'
_A6='cvsModuleVSLCapable'
_A5='cvsModuleVSSupported'
_A4='cvsVSLPortRxBadPkts'
_A3='cvsVSLPortRxFailPkts'
_A2='cvsVSLPortRxUnidirPkts'
_A1='cvsVSLPortRxBidirPkts'
_A0='cvsVSLPortTxFailPkts'
_z='cvsVSLPortTxOkPkts'
_y='cvsVSLRxChksumErrPkts'
_x='cvsVSLRxErrorPkts'
_w='cvsVSLRxTotalPkts'
_v='cvsVSLTxChksumErrPkts'
_u='cvsVSLTxErrorPkts'
_t='cvsVSLTxTotalPkts'
_s='cvsVSLConnectionRowStatus'
_r='cvsVSLOperationalPortCount'
_q='cvsVSLConfiguredPortCount'
_p='cvsVSLLastConnectionStateChange'
_o='cvsVSLCoreSwitchID'
_n='cvsChassisUpTime'
_m='cvsChassisRole'
_l='cvsChassisSwitchID'
_k='cvsCoreSwitchPreempt'
_j='cvsCoreSwitchPriority'
_i='cvsVSLChangeNotifEnable'
_h='cvsSwitchConvertingStatus'
_g='cvsSwitchMode'
_f='cvsSwitchCapability'
_e='cvsDomain'
_d='read-create'
_c='cvsCoreSwitchID'
_b='Integer32'
_a='cvsDualActiveDetectionNotifsGroup'
_Z='cvsDualActiveDetectionNotifsInfoGroup'
_Y='cvsDualActiveDetectionNotifsControlGroup'
_X='cvsCoreSwitchLocationGroup'
_W='deprecated'
_V='cvsDualActiveDetectionInformation'
_U='cvsVSLConnectOperStatus'
_T='cvsSwitchID'
_S='cvsVSLPortStatsIfindex'
_R='not-accessible'
_Q='standalone'
_P='entPhysicalIndex'
_O='ENTITY-MIB'
_N='cvsVSLStatisticsExtGroup'
_M='cvsVssModuleStandbyGroup'
_L='cvsConnectionNotifsGroup'
_K='cvsVSLStatisticsGroup'
_J='cvsVSLConnectionGroup'
_I='cvsChassisGroup'
_H='cvsCoreSwitchGroup'
_G='cvsModuleGroup'
_F='cvsGlobalGroup'
_E='cvsVSLChannelIfindex'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-VIRTUAL-SWITCH-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,=mibBuilder.importSymbols(_O,_P)
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_b,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoVirtualSwitchMIB=ModuleIdentity((1,3,6,1,4,1,9,9,388))
if mibBuilder.loadTexts:ciscoVirtualSwitchMIB.setRevisions(('2015-03-04 00:00','2012-04-10 00:00','2010-01-21 00:00','2007-09-25 00:00'))
class VSSwitchID(TextualConvention,Unsigned32):status=_B
class VSSwitchCapability(TextualConvention,Bits):status=_B;namedValues=NamedValues(*((_Q,0),('core',1)))
class VSSwitchMode(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),('multiNode',2)))
class VSSwitchRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),('active',2),('standby',3)))
class VSConnectStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CiscoVirtualSwitchMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoVirtualSwitchMIBNotifs=_CiscoVirtualSwitchMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,388,0))
_CiscoVirtualSwitchMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVirtualSwitchMIBObjects=_CiscoVirtualSwitchMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,388,1))
_CvsGlobalObjects_ObjectIdentity=ObjectIdentity
cvsGlobalObjects=_CvsGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,388,1,1))
_CvsDomain_Type=Unsigned32
_CvsDomain_Object=MibScalar
cvsDomain=_CvsDomain_Object((1,3,6,1,4,1,9,9,388,1,1,1),_CvsDomain_Type())
cvsDomain.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsDomain.setStatus(_B)
_CvsSwitchID_Type=VSSwitchID
_CvsSwitchID_Object=MibScalar
cvsSwitchID=_CvsSwitchID_Object((1,3,6,1,4,1,9,9,388,1,1,2),_CvsSwitchID_Type())
cvsSwitchID.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsSwitchID.setStatus(_B)
_CvsSwitchCapability_Type=VSSwitchCapability
_CvsSwitchCapability_Object=MibScalar
cvsSwitchCapability=_CvsSwitchCapability_Object((1,3,6,1,4,1,9,9,388,1,1,3),_CvsSwitchCapability_Type())
cvsSwitchCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsSwitchCapability.setStatus(_B)
_CvsSwitchMode_Type=VSSwitchMode
_CvsSwitchMode_Object=MibScalar
cvsSwitchMode=_CvsSwitchMode_Object((1,3,6,1,4,1,9,9,388,1,1,4),_CvsSwitchMode_Type())
cvsSwitchMode.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsSwitchMode.setStatus(_B)
_CvsSwitchConvertingStatus_Type=TruthValue
_CvsSwitchConvertingStatus_Object=MibScalar
cvsSwitchConvertingStatus=_CvsSwitchConvertingStatus_Object((1,3,6,1,4,1,9,9,388,1,1,5),_CvsSwitchConvertingStatus_Type())
cvsSwitchConvertingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsSwitchConvertingStatus.setStatus(_B)
_CvsVSLChangeNotifEnable_Type=TruthValue
_CvsVSLChangeNotifEnable_Object=MibScalar
cvsVSLChangeNotifEnable=_CvsVSLChangeNotifEnable_Object((1,3,6,1,4,1,9,9,388,1,1,6),_CvsVSLChangeNotifEnable_Type())
cvsVSLChangeNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsVSLChangeNotifEnable.setStatus(_B)
_CvsChassisObjects_ObjectIdentity=ObjectIdentity
cvsChassisObjects=_CvsChassisObjects_ObjectIdentity((1,3,6,1,4,1,9,9,388,1,2))
_CvsCoreSwitchConfigTable_Object=MibTable
cvsCoreSwitchConfigTable=_CvsCoreSwitchConfigTable_Object((1,3,6,1,4,1,9,9,388,1,2,1))
if mibBuilder.loadTexts:cvsCoreSwitchConfigTable.setStatus(_B)
_CvsCoreSwitchConfigEntry_Object=MibTableRow
cvsCoreSwitchConfigEntry=_CvsCoreSwitchConfigEntry_Object((1,3,6,1,4,1,9,9,388,1,2,1,1))
cvsCoreSwitchConfigEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:cvsCoreSwitchConfigEntry.setStatus(_B)
_CvsCoreSwitchID_Type=VSSwitchID
_CvsCoreSwitchID_Object=MibTableColumn
cvsCoreSwitchID=_CvsCoreSwitchID_Object((1,3,6,1,4,1,9,9,388,1,2,1,1,1),_CvsCoreSwitchID_Type())
cvsCoreSwitchID.setMaxAccess(_R)
if mibBuilder.loadTexts:cvsCoreSwitchID.setStatus(_B)
_CvsCoreSwitchPriority_Type=Unsigned32
_CvsCoreSwitchPriority_Object=MibTableColumn
cvsCoreSwitchPriority=_CvsCoreSwitchPriority_Object((1,3,6,1,4,1,9,9,388,1,2,1,1,2),_CvsCoreSwitchPriority_Type())
cvsCoreSwitchPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsCoreSwitchPriority.setStatus(_B)
_CvsCoreSwitchPreempt_Type=TruthValue
_CvsCoreSwitchPreempt_Object=MibTableColumn
cvsCoreSwitchPreempt=_CvsCoreSwitchPreempt_Object((1,3,6,1,4,1,9,9,388,1,2,1,1,3),_CvsCoreSwitchPreempt_Type())
cvsCoreSwitchPreempt.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsCoreSwitchPreempt.setStatus(_B)
_CvsCoreSwitchLocation_Type=SnmpAdminString
_CvsCoreSwitchLocation_Object=MibTableColumn
cvsCoreSwitchLocation=_CvsCoreSwitchLocation_Object((1,3,6,1,4,1,9,9,388,1,2,1,1,4),_CvsCoreSwitchLocation_Type())
cvsCoreSwitchLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsCoreSwitchLocation.setStatus(_B)
_CvsChassisTable_Object=MibTable
cvsChassisTable=_CvsChassisTable_Object((1,3,6,1,4,1,9,9,388,1,2,2))
if mibBuilder.loadTexts:cvsChassisTable.setStatus(_B)
_CvsChassisEntry_Object=MibTableRow
cvsChassisEntry=_CvsChassisEntry_Object((1,3,6,1,4,1,9,9,388,1,2,2,1))
cvsChassisEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:cvsChassisEntry.setStatus(_B)
_CvsChassisSwitchID_Type=VSSwitchID
_CvsChassisSwitchID_Object=MibTableColumn
cvsChassisSwitchID=_CvsChassisSwitchID_Object((1,3,6,1,4,1,9,9,388,1,2,2,1,1),_CvsChassisSwitchID_Type())
cvsChassisSwitchID.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsChassisSwitchID.setStatus(_B)
_CvsChassisRole_Type=VSSwitchRole
_CvsChassisRole_Object=MibTableColumn
cvsChassisRole=_CvsChassisRole_Object((1,3,6,1,4,1,9,9,388,1,2,2,1,2),_CvsChassisRole_Type())
cvsChassisRole.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsChassisRole.setStatus(_B)
_CvsChassisUpTime_Type=TimeStamp
_CvsChassisUpTime_Object=MibTableColumn
cvsChassisUpTime=_CvsChassisUpTime_Object((1,3,6,1,4,1,9,9,388,1,2,2,1,3),_CvsChassisUpTime_Type())
cvsChassisUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsChassisUpTime.setStatus(_B)
_CvsVSLObjects_ObjectIdentity=ObjectIdentity
cvsVSLObjects=_CvsVSLObjects_ObjectIdentity((1,3,6,1,4,1,9,9,388,1,3))
_CvsVSLConnectionTable_Object=MibTable
cvsVSLConnectionTable=_CvsVSLConnectionTable_Object((1,3,6,1,4,1,9,9,388,1,3,1))
if mibBuilder.loadTexts:cvsVSLConnectionTable.setStatus(_B)
_CvsVSLConnectionEntry_Object=MibTableRow
cvsVSLConnectionEntry=_CvsVSLConnectionEntry_Object((1,3,6,1,4,1,9,9,388,1,3,1,1))
cvsVSLConnectionEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:cvsVSLConnectionEntry.setStatus(_B)
_CvsVSLChannelIfindex_Type=InterfaceIndex
_CvsVSLChannelIfindex_Object=MibTableColumn
cvsVSLChannelIfindex=_CvsVSLChannelIfindex_Object((1,3,6,1,4,1,9,9,388,1,3,1,1,1),_CvsVSLChannelIfindex_Type())
cvsVSLChannelIfindex.setMaxAccess(_R)
if mibBuilder.loadTexts:cvsVSLChannelIfindex.setStatus(_B)
_CvsVSLCoreSwitchID_Type=VSSwitchID
_CvsVSLCoreSwitchID_Object=MibTableColumn
cvsVSLCoreSwitchID=_CvsVSLCoreSwitchID_Object((1,3,6,1,4,1,9,9,388,1,3,1,1,2),_CvsVSLCoreSwitchID_Type())
cvsVSLCoreSwitchID.setMaxAccess(_d)
if mibBuilder.loadTexts:cvsVSLCoreSwitchID.setStatus(_B)
_CvsVSLConnectOperStatus_Type=VSConnectStatus
_CvsVSLConnectOperStatus_Object=MibTableColumn
cvsVSLConnectOperStatus=_CvsVSLConnectOperStatus_Object((1,3,6,1,4,1,9,9,388,1,3,1,1,3),_CvsVSLConnectOperStatus_Type())
cvsVSLConnectOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLConnectOperStatus.setStatus(_B)
_CvsVSLLastConnectionStateChange_Type=DateAndTime
_CvsVSLLastConnectionStateChange_Object=MibTableColumn
cvsVSLLastConnectionStateChange=_CvsVSLLastConnectionStateChange_Object((1,3,6,1,4,1,9,9,388,1,3,1,1,4),_CvsVSLLastConnectionStateChange_Type())
cvsVSLLastConnectionStateChange.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLLastConnectionStateChange.setStatus(_B)
_CvsVSLConfiguredPortCount_Type=Unsigned32
_CvsVSLConfiguredPortCount_Object=MibTableColumn
cvsVSLConfiguredPortCount=_CvsVSLConfiguredPortCount_Object((1,3,6,1,4,1,9,9,388,1,3,1,1,5),_CvsVSLConfiguredPortCount_Type())
cvsVSLConfiguredPortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLConfiguredPortCount.setStatus(_B)
_CvsVSLOperationalPortCount_Type=Unsigned32
_CvsVSLOperationalPortCount_Object=MibTableColumn
cvsVSLOperationalPortCount=_CvsVSLOperationalPortCount_Object((1,3,6,1,4,1,9,9,388,1,3,1,1,6),_CvsVSLOperationalPortCount_Type())
cvsVSLOperationalPortCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLOperationalPortCount.setStatus(_B)
_CvsVSLConnectionRowStatus_Type=RowStatus
_CvsVSLConnectionRowStatus_Object=MibTableColumn
cvsVSLConnectionRowStatus=_CvsVSLConnectionRowStatus_Object((1,3,6,1,4,1,9,9,388,1,3,1,1,7),_CvsVSLConnectionRowStatus_Type())
cvsVSLConnectionRowStatus.setMaxAccess(_d)
if mibBuilder.loadTexts:cvsVSLConnectionRowStatus.setStatus(_B)
_CvsVSLStatsTable_Object=MibTable
cvsVSLStatsTable=_CvsVSLStatsTable_Object((1,3,6,1,4,1,9,9,388,1,3,2))
if mibBuilder.loadTexts:cvsVSLStatsTable.setStatus(_B)
_CvsVSLStatsEntry_Object=MibTableRow
cvsVSLStatsEntry=_CvsVSLStatsEntry_Object((1,3,6,1,4,1,9,9,388,1,3,2,1))
cvsVSLStatsEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:cvsVSLStatsEntry.setStatus(_B)
_CvsVSLTxTotalPkts_Type=Counter32
_CvsVSLTxTotalPkts_Object=MibTableColumn
cvsVSLTxTotalPkts=_CvsVSLTxTotalPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,1),_CvsVSLTxTotalPkts_Type())
cvsVSLTxTotalPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxTotalPkts.setStatus(_B)
_CvsVSLTxErrorPkts_Type=Counter32
_CvsVSLTxErrorPkts_Object=MibTableColumn
cvsVSLTxErrorPkts=_CvsVSLTxErrorPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,2),_CvsVSLTxErrorPkts_Type())
cvsVSLTxErrorPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxErrorPkts.setStatus(_B)
_CvsVSLTxChksumErrPkts_Type=Counter32
_CvsVSLTxChksumErrPkts_Object=MibTableColumn
cvsVSLTxChksumErrPkts=_CvsVSLTxChksumErrPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,3),_CvsVSLTxChksumErrPkts_Type())
cvsVSLTxChksumErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxChksumErrPkts.setStatus(_B)
_CvsVSLRxTotalPkts_Type=Counter32
_CvsVSLRxTotalPkts_Object=MibTableColumn
cvsVSLRxTotalPkts=_CvsVSLRxTotalPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,4),_CvsVSLRxTotalPkts_Type())
cvsVSLRxTotalPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxTotalPkts.setStatus(_B)
_CvsVSLRxErrorPkts_Type=Counter32
_CvsVSLRxErrorPkts_Object=MibTableColumn
cvsVSLRxErrorPkts=_CvsVSLRxErrorPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,5),_CvsVSLRxErrorPkts_Type())
cvsVSLRxErrorPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxErrorPkts.setStatus(_B)
_CvsVSLRxChksumErrPkts_Type=Counter32
_CvsVSLRxChksumErrPkts_Object=MibTableColumn
cvsVSLRxChksumErrPkts=_CvsVSLRxChksumErrPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,6),_CvsVSLRxChksumErrPkts_Type())
cvsVSLRxChksumErrPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxChksumErrPkts.setStatus(_B)
_CvsVSLTxLmpPkts_Type=Counter64
_CvsVSLTxLmpPkts_Object=MibTableColumn
cvsVSLTxLmpPkts=_CvsVSLTxLmpPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,7),_CvsVSLTxLmpPkts_Type())
cvsVSLTxLmpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxLmpPkts.setStatus(_B)
_CvsVSLTxRrpPkts_Type=Counter64
_CvsVSLTxRrpPkts_Object=MibTableColumn
cvsVSLTxRrpPkts=_CvsVSLTxRrpPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,8),_CvsVSLTxRrpPkts_Type())
cvsVSLTxRrpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxRrpPkts.setStatus(_B)
_CvsVSLTxPingPkts_Type=Counter64
_CvsVSLTxPingPkts_Object=MibTableColumn
cvsVSLTxPingPkts=_CvsVSLTxPingPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,9),_CvsVSLTxPingPkts_Type())
cvsVSLTxPingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxPingPkts.setStatus(_B)
_CvsVSLTxProtoPkts_Type=Counter64
_CvsVSLTxProtoPkts_Object=MibTableColumn
cvsVSLTxProtoPkts=_CvsVSLTxProtoPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,10),_CvsVSLTxProtoPkts_Type())
cvsVSLTxProtoPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxProtoPkts.setStatus(_B)
_CvsVSLTxDataPkts_Type=Counter64
_CvsVSLTxDataPkts_Object=MibTableColumn
cvsVSLTxDataPkts=_CvsVSLTxDataPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,11),_CvsVSLTxDataPkts_Type())
cvsVSLTxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxDataPkts.setStatus(_B)
_CvsVSLTxAckPkts_Type=Counter64
_CvsVSLTxAckPkts_Object=MibTableColumn
cvsVSLTxAckPkts=_CvsVSLTxAckPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,12),_CvsVSLTxAckPkts_Type())
cvsVSLTxAckPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxAckPkts.setStatus(_B)
_CvsVSLRxLmpPkts_Type=Counter64
_CvsVSLRxLmpPkts_Object=MibTableColumn
cvsVSLRxLmpPkts=_CvsVSLRxLmpPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,13),_CvsVSLRxLmpPkts_Type())
cvsVSLRxLmpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxLmpPkts.setStatus(_B)
_CvsVSLRxRrpPkts_Type=Counter64
_CvsVSLRxRrpPkts_Object=MibTableColumn
cvsVSLRxRrpPkts=_CvsVSLRxRrpPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,14),_CvsVSLRxRrpPkts_Type())
cvsVSLRxRrpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxRrpPkts.setStatus(_B)
_CvsVSLRxPingPkts_Type=Counter64
_CvsVSLRxPingPkts_Object=MibTableColumn
cvsVSLRxPingPkts=_CvsVSLRxPingPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,15),_CvsVSLRxPingPkts_Type())
cvsVSLRxPingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxPingPkts.setStatus(_B)
_CvsVSLRxProtoPkts_Type=Counter64
_CvsVSLRxProtoPkts_Object=MibTableColumn
cvsVSLRxProtoPkts=_CvsVSLRxProtoPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,16),_CvsVSLRxProtoPkts_Type())
cvsVSLRxProtoPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxProtoPkts.setStatus(_B)
_CvsVSLRxDataPkts_Type=Counter64
_CvsVSLRxDataPkts_Object=MibTableColumn
cvsVSLRxDataPkts=_CvsVSLRxDataPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,17),_CvsVSLRxDataPkts_Type())
cvsVSLRxDataPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxDataPkts.setStatus(_B)
_CvsVSLRxAckPkts_Type=Counter64
_CvsVSLRxAckPkts_Object=MibTableColumn
cvsVSLRxAckPkts=_CvsVSLRxAckPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,18),_CvsVSLRxAckPkts_Type())
cvsVSLRxAckPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxAckPkts.setStatus(_B)
_CvsVSLTxTotalEobcPkts_Type=Counter64
_CvsVSLTxTotalEobcPkts_Object=MibTableColumn
cvsVSLTxTotalEobcPkts=_CvsVSLTxTotalEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,19),_CvsVSLTxTotalEobcPkts_Type())
cvsVSLTxTotalEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxTotalEobcPkts.setStatus(_B)
_CvsVSLTxLmpEobcPkts_Type=Counter64
_CvsVSLTxLmpEobcPkts_Object=MibTableColumn
cvsVSLTxLmpEobcPkts=_CvsVSLTxLmpEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,20),_CvsVSLTxLmpEobcPkts_Type())
cvsVSLTxLmpEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxLmpEobcPkts.setStatus(_B)
_CvsVSLTxRrpEobcPkts_Type=Counter64
_CvsVSLTxRrpEobcPkts_Object=MibTableColumn
cvsVSLTxRrpEobcPkts=_CvsVSLTxRrpEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,21),_CvsVSLTxRrpEobcPkts_Type())
cvsVSLTxRrpEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxRrpEobcPkts.setStatus(_B)
_CvsVSLTxPingEobcPkts_Type=Counter64
_CvsVSLTxPingEobcPkts_Object=MibTableColumn
cvsVSLTxPingEobcPkts=_CvsVSLTxPingEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,22),_CvsVSLTxPingEobcPkts_Type())
cvsVSLTxPingEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxPingEobcPkts.setStatus(_B)
_CvsVSLTxProtoEobcPkts_Type=Counter64
_CvsVSLTxProtoEobcPkts_Object=MibTableColumn
cvsVSLTxProtoEobcPkts=_CvsVSLTxProtoEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,23),_CvsVSLTxProtoEobcPkts_Type())
cvsVSLTxProtoEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxProtoEobcPkts.setStatus(_B)
_CvsVSLTxDataEobcPkts_Type=Counter64
_CvsVSLTxDataEobcPkts_Object=MibTableColumn
cvsVSLTxDataEobcPkts=_CvsVSLTxDataEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,24),_CvsVSLTxDataEobcPkts_Type())
cvsVSLTxDataEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxDataEobcPkts.setStatus(_B)
_CvsVSLTxAckEobcPkts_Type=Counter64
_CvsVSLTxAckEobcPkts_Object=MibTableColumn
cvsVSLTxAckEobcPkts=_CvsVSLTxAckEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,25),_CvsVSLTxAckEobcPkts_Type())
cvsVSLTxAckEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxAckEobcPkts.setStatus(_B)
_CvsVSLRxTotalEobcPkts_Type=Counter64
_CvsVSLRxTotalEobcPkts_Object=MibTableColumn
cvsVSLRxTotalEobcPkts=_CvsVSLRxTotalEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,26),_CvsVSLRxTotalEobcPkts_Type())
cvsVSLRxTotalEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxTotalEobcPkts.setStatus(_B)
_CvsVSLRxLmpEobcPkts_Type=Counter64
_CvsVSLRxLmpEobcPkts_Object=MibTableColumn
cvsVSLRxLmpEobcPkts=_CvsVSLRxLmpEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,27),_CvsVSLRxLmpEobcPkts_Type())
cvsVSLRxLmpEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxLmpEobcPkts.setStatus(_B)
_CvsVSLRxRrpEobcPkts_Type=Counter64
_CvsVSLRxRrpEobcPkts_Object=MibTableColumn
cvsVSLRxRrpEobcPkts=_CvsVSLRxRrpEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,28),_CvsVSLRxRrpEobcPkts_Type())
cvsVSLRxRrpEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxRrpEobcPkts.setStatus(_B)
_CvsVSLRxPingEobcPkts_Type=Counter64
_CvsVSLRxPingEobcPkts_Object=MibTableColumn
cvsVSLRxPingEobcPkts=_CvsVSLRxPingEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,29),_CvsVSLRxPingEobcPkts_Type())
cvsVSLRxPingEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxPingEobcPkts.setStatus(_B)
_CvsVSLRxProtoEobcPkts_Type=Counter64
_CvsVSLRxProtoEobcPkts_Object=MibTableColumn
cvsVSLRxProtoEobcPkts=_CvsVSLRxProtoEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,30),_CvsVSLRxProtoEobcPkts_Type())
cvsVSLRxProtoEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxProtoEobcPkts.setStatus(_B)
_CvsVSLRxDataEobcPkts_Type=Counter64
_CvsVSLRxDataEobcPkts_Object=MibTableColumn
cvsVSLRxDataEobcPkts=_CvsVSLRxDataEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,31),_CvsVSLRxDataEobcPkts_Type())
cvsVSLRxDataEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxDataEobcPkts.setStatus(_B)
_CvsVSLRxAckEobcPkts_Type=Counter64
_CvsVSLRxAckEobcPkts_Object=MibTableColumn
cvsVSLRxAckEobcPkts=_CvsVSLRxAckEobcPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,32),_CvsVSLRxAckEobcPkts_Type())
cvsVSLRxAckEobcPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxAckEobcPkts.setStatus(_B)
_CvsVSLTxTotalHCPkts_Type=Counter64
_CvsVSLTxTotalHCPkts_Object=MibTableColumn
cvsVSLTxTotalHCPkts=_CvsVSLTxTotalHCPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,33),_CvsVSLTxTotalHCPkts_Type())
cvsVSLTxTotalHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxTotalHCPkts.setStatus(_B)
_CvsVSLTxErrorHCPkts_Type=Counter64
_CvsVSLTxErrorHCPkts_Object=MibTableColumn
cvsVSLTxErrorHCPkts=_CvsVSLTxErrorHCPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,34),_CvsVSLTxErrorHCPkts_Type())
cvsVSLTxErrorHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxErrorHCPkts.setStatus(_B)
_CvsVSLTxChksumErrHCPkts_Type=Counter64
_CvsVSLTxChksumErrHCPkts_Object=MibTableColumn
cvsVSLTxChksumErrHCPkts=_CvsVSLTxChksumErrHCPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,35),_CvsVSLTxChksumErrHCPkts_Type())
cvsVSLTxChksumErrHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLTxChksumErrHCPkts.setStatus(_B)
_CvsVSLRxTotalHCPkts_Type=Counter64
_CvsVSLRxTotalHCPkts_Object=MibTableColumn
cvsVSLRxTotalHCPkts=_CvsVSLRxTotalHCPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,36),_CvsVSLRxTotalHCPkts_Type())
cvsVSLRxTotalHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxTotalHCPkts.setStatus(_B)
_CvsVSLRxErrorHCPkts_Type=Counter64
_CvsVSLRxErrorHCPkts_Object=MibTableColumn
cvsVSLRxErrorHCPkts=_CvsVSLRxErrorHCPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,37),_CvsVSLRxErrorHCPkts_Type())
cvsVSLRxErrorHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxErrorHCPkts.setStatus(_B)
_CvsVSLRxChksumErrHCPkts_Type=Counter64
_CvsVSLRxChksumErrHCPkts_Object=MibTableColumn
cvsVSLRxChksumErrHCPkts=_CvsVSLRxChksumErrHCPkts_Object((1,3,6,1,4,1,9,9,388,1,3,2,1,38),_CvsVSLRxChksumErrHCPkts_Type())
cvsVSLRxChksumErrHCPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLRxChksumErrHCPkts.setStatus(_B)
_CvsVSLPortStatsTable_Object=MibTable
cvsVSLPortStatsTable=_CvsVSLPortStatsTable_Object((1,3,6,1,4,1,9,9,388,1,3,3))
if mibBuilder.loadTexts:cvsVSLPortStatsTable.setStatus(_B)
_CvsVSLPortStatsEntry_Object=MibTableRow
cvsVSLPortStatsEntry=_CvsVSLPortStatsEntry_Object((1,3,6,1,4,1,9,9,388,1,3,3,1))
cvsVSLPortStatsEntry.setIndexNames((0,_A,_E),(0,_A,_S))
if mibBuilder.loadTexts:cvsVSLPortStatsEntry.setStatus(_B)
_CvsVSLPortStatsIfindex_Type=InterfaceIndex
_CvsVSLPortStatsIfindex_Object=MibTableColumn
cvsVSLPortStatsIfindex=_CvsVSLPortStatsIfindex_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,1),_CvsVSLPortStatsIfindex_Type())
cvsVSLPortStatsIfindex.setMaxAccess(_R)
if mibBuilder.loadTexts:cvsVSLPortStatsIfindex.setStatus(_B)
_CvsVSLPortTxOkPkts_Type=Counter32
_CvsVSLPortTxOkPkts_Object=MibTableColumn
cvsVSLPortTxOkPkts=_CvsVSLPortTxOkPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,2),_CvsVSLPortTxOkPkts_Type())
cvsVSLPortTxOkPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortTxOkPkts.setStatus(_B)
_CvsVSLPortTxFailPkts_Type=Counter32
_CvsVSLPortTxFailPkts_Object=MibTableColumn
cvsVSLPortTxFailPkts=_CvsVSLPortTxFailPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,3),_CvsVSLPortTxFailPkts_Type())
cvsVSLPortTxFailPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortTxFailPkts.setStatus(_B)
_CvsVSLPortRxBidirPkts_Type=Counter32
_CvsVSLPortRxBidirPkts_Object=MibTableColumn
cvsVSLPortRxBidirPkts=_CvsVSLPortRxBidirPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,4),_CvsVSLPortRxBidirPkts_Type())
cvsVSLPortRxBidirPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxBidirPkts.setStatus(_B)
_CvsVSLPortRxUnidirPkts_Type=Counter32
_CvsVSLPortRxUnidirPkts_Object=MibTableColumn
cvsVSLPortRxUnidirPkts=_CvsVSLPortRxUnidirPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,5),_CvsVSLPortRxUnidirPkts_Type())
cvsVSLPortRxUnidirPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxUnidirPkts.setStatus(_B)
_CvsVSLPortRxFailPkts_Type=Counter32
_CvsVSLPortRxFailPkts_Object=MibTableColumn
cvsVSLPortRxFailPkts=_CvsVSLPortRxFailPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,6),_CvsVSLPortRxFailPkts_Type())
cvsVSLPortRxFailPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxFailPkts.setStatus(_B)
_CvsVSLPortRxBadPkts_Type=Counter32
_CvsVSLPortRxBadPkts_Object=MibTableColumn
cvsVSLPortRxBadPkts=_CvsVSLPortRxBadPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,7),_CvsVSLPortRxBadPkts_Type())
cvsVSLPortRxBadPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxBadPkts.setStatus(_B)
_CvsVSLPortRxMyInfoMismatchPkts_Type=Counter32
_CvsVSLPortRxMyInfoMismatchPkts_Object=MibTableColumn
cvsVSLPortRxMyInfoMismatchPkts=_CvsVSLPortRxMyInfoMismatchPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,8),_CvsVSLPortRxMyInfoMismatchPkts_Type())
cvsVSLPortRxMyInfoMismatchPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxMyInfoMismatchPkts.setStatus(_B)
_CvsVSLPortRxMyInfoAbsentPkts_Type=Counter32
_CvsVSLPortRxMyInfoAbsentPkts_Object=MibTableColumn
cvsVSLPortRxMyInfoAbsentPkts=_CvsVSLPortRxMyInfoAbsentPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,9),_CvsVSLPortRxMyInfoAbsentPkts_Type())
cvsVSLPortRxMyInfoAbsentPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxMyInfoAbsentPkts.setStatus(_B)
_CvsVSLPortRxBadMacAddressPkts_Type=Counter32
_CvsVSLPortRxBadMacAddressPkts_Object=MibTableColumn
cvsVSLPortRxBadMacAddressPkts=_CvsVSLPortRxBadMacAddressPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,10),_CvsVSLPortRxBadMacAddressPkts_Type())
cvsVSLPortRxBadMacAddressPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxBadMacAddressPkts.setStatus(_B)
_CvsVSLPortRxBadSwitchIdPkts_Type=Counter32
_CvsVSLPortRxBadSwitchIdPkts_Object=MibTableColumn
cvsVSLPortRxBadSwitchIdPkts=_CvsVSLPortRxBadSwitchIdPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,11),_CvsVSLPortRxBadSwitchIdPkts_Type())
cvsVSLPortRxBadSwitchIdPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxBadSwitchIdPkts.setStatus(_B)
_CvsVSLPortRxDomainIdMismatchPkts_Type=Counter32
_CvsVSLPortRxDomainIdMismatchPkts_Object=MibTableColumn
cvsVSLPortRxDomainIdMismatchPkts=_CvsVSLPortRxDomainIdMismatchPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,12),_CvsVSLPortRxDomainIdMismatchPkts_Type())
cvsVSLPortRxDomainIdMismatchPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxDomainIdMismatchPkts.setStatus(_B)
_CvsVSLPortRxPeerInfoMismatchPkts_Type=Counter32
_CvsVSLPortRxPeerInfoMismatchPkts_Object=MibTableColumn
cvsVSLPortRxPeerInfoMismatchPkts=_CvsVSLPortRxPeerInfoMismatchPkts_Object((1,3,6,1,4,1,9,9,388,1,3,3,1,13),_CvsVSLPortRxPeerInfoMismatchPkts_Type())
cvsVSLPortRxPeerInfoMismatchPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLPortRxPeerInfoMismatchPkts.setStatus(_B)
_CvsVSLLinkPortTable_Object=MibTable
cvsVSLLinkPortTable=_CvsVSLLinkPortTable_Object((1,3,6,1,4,1,9,9,388,1,3,4))
if mibBuilder.loadTexts:cvsVSLLinkPortTable.setStatus(_B)
_CvsVSLLinkPortEntry_Object=MibTableRow
cvsVSLLinkPortEntry=_CvsVSLLinkPortEntry_Object((1,3,6,1,4,1,9,9,388,1,3,4,1))
cvsVSLLinkPortEntry.setIndexNames((0,_A,_E),(0,_A,_S))
if mibBuilder.loadTexts:cvsVSLLinkPortEntry.setStatus(_B)
_CvsVSLLinkPeerInterface_Type=SnmpAdminString
_CvsVSLLinkPeerInterface_Object=MibTableColumn
cvsVSLLinkPeerInterface=_CvsVSLLinkPeerInterface_Object((1,3,6,1,4,1,9,9,388,1,3,4,1,1),_CvsVSLLinkPeerInterface_Type())
cvsVSLLinkPeerInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsVSLLinkPeerInterface.setStatus(_B)
_CvsModuleObjects_ObjectIdentity=ObjectIdentity
cvsModuleObjects=_CvsModuleObjects_ObjectIdentity((1,3,6,1,4,1,9,9,388,1,4))
_CvsModuleTable_Object=MibTable
cvsModuleTable=_CvsModuleTable_Object((1,3,6,1,4,1,9,9,388,1,4,1))
if mibBuilder.loadTexts:cvsModuleTable.setStatus(_B)
_CvsModuleEntry_Object=MibTableRow
cvsModuleEntry=_CvsModuleEntry_Object((1,3,6,1,4,1,9,9,388,1,4,1,1))
cvsModuleEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:cvsModuleEntry.setStatus(_B)
_CvsModuleVSSupported_Type=TruthValue
_CvsModuleVSSupported_Object=MibTableColumn
cvsModuleVSSupported=_CvsModuleVSSupported_Object((1,3,6,1,4,1,9,9,388,1,4,1,1,1),_CvsModuleVSSupported_Type())
cvsModuleVSSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsModuleVSSupported.setStatus(_B)
_CvsModuleVSLCapable_Type=TruthValue
_CvsModuleVSLCapable_Object=MibTableColumn
cvsModuleVSLCapable=_CvsModuleVSLCapable_Object((1,3,6,1,4,1,9,9,388,1,4,1,1,2),_CvsModuleVSLCapable_Type())
cvsModuleVSLCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsModuleVSLCapable.setStatus(_B)
_CvsModuleSlotNumber_Type=Unsigned32
_CvsModuleSlotNumber_Object=MibTableColumn
cvsModuleSlotNumber=_CvsModuleSlotNumber_Object((1,3,6,1,4,1,9,9,388,1,4,1,1,3),_CvsModuleSlotNumber_Type())
cvsModuleSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsModuleSlotNumber.setStatus(_B)
class _CvsModuleRprWarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('rprWarm',2),('cSSO',3)))
_CvsModuleRprWarm_Type.__name__=_b
_CvsModuleRprWarm_Object=MibTableColumn
cvsModuleRprWarm=_CvsModuleRprWarm_Object((1,3,6,1,4,1,9,9,388,1,4,1,1,4),_CvsModuleRprWarm_Type())
cvsModuleRprWarm.setMaxAccess(_C)
if mibBuilder.loadTexts:cvsModuleRprWarm.setStatus(_B)
_CvsDualActiveDetection_ObjectIdentity=ObjectIdentity
cvsDualActiveDetection=_CvsDualActiveDetection_ObjectIdentity((1,3,6,1,4,1,9,9,388,1,5))
_CvsDualActiveDetectionNotifEnable_Type=TruthValue
_CvsDualActiveDetectionNotifEnable_Object=MibScalar
cvsDualActiveDetectionNotifEnable=_CvsDualActiveDetectionNotifEnable_Object((1,3,6,1,4,1,9,9,388,1,5,1),_CvsDualActiveDetectionNotifEnable_Type())
cvsDualActiveDetectionNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cvsDualActiveDetectionNotifEnable.setStatus(_B)
_CvsDualActiveDetectionInformation_Type=SnmpAdminString
_CvsDualActiveDetectionInformation_Object=MibScalar
cvsDualActiveDetectionInformation=_CvsDualActiveDetectionInformation_Object((1,3,6,1,4,1,9,9,388,1,5,2),_CvsDualActiveDetectionInformation_Type())
cvsDualActiveDetectionInformation.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:cvsDualActiveDetectionInformation.setStatus(_B)
_CiscoVirtualSwitchMIBConform_ObjectIdentity=ObjectIdentity
ciscoVirtualSwitchMIBConform=_CiscoVirtualSwitchMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,388,2))
_CvsMIBCompliances_ObjectIdentity=ObjectIdentity
cvsMIBCompliances=_CvsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,388,2,1))
_CvsMIBGroups_ObjectIdentity=ObjectIdentity
cvsMIBGroups=_CvsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,388,2,2))
cvsGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,1))
cvsGlobalGroup.setObjects(*((_A,_e),(_A,_T),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:cvsGlobalGroup.setStatus(_B)
cvsCoreSwitchGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,2))
cvsCoreSwitchGroup.setObjects(*((_A,_j),(_A,_k)))
if mibBuilder.loadTexts:cvsCoreSwitchGroup.setStatus(_B)
cvsChassisGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,3))
cvsChassisGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cvsChassisGroup.setStatus(_B)
cvsVSLConnectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,4))
cvsVSLConnectionGroup.setObjects(*((_A,_o),(_A,_U),(_A,_p),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:cvsVSLConnectionGroup.setStatus(_B)
cvsVSLStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,5))
cvsVSLStatisticsGroup.setObjects(*((_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:cvsVSLStatisticsGroup.setStatus(_B)
cvsModuleGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,6))
cvsModuleGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:cvsModuleGroup.setStatus(_B)
cvsVSLStatisticsExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,8))
cvsVSLStatisticsExtGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:cvsVSLStatisticsExtGroup.setStatus(_B)
cvsVssModuleStandbyGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,9))
cvsVssModuleStandbyGroup.setObjects((_A,_Ak))
if mibBuilder.loadTexts:cvsVssModuleStandbyGroup.setStatus(_B)
cvsCoreSwitchLocationGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,10))
cvsCoreSwitchLocationGroup.setObjects((_A,_Al))
if mibBuilder.loadTexts:cvsCoreSwitchLocationGroup.setStatus(_B)
cvsDualActiveDetectionNotifsControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,11))
cvsDualActiveDetectionNotifsControlGroup.setObjects((_A,_Am))
if mibBuilder.loadTexts:cvsDualActiveDetectionNotifsControlGroup.setStatus(_B)
cvsDualActiveDetectionNotifsInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,12))
cvsDualActiveDetectionNotifsInfoGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:cvsDualActiveDetectionNotifsInfoGroup.setStatus(_B)
cvsVSLLinkPortGroup=ObjectGroup((1,3,6,1,4,1,9,9,388,2,2,14))
cvsVSLLinkPortGroup.setObjects((_A,_An))
if mibBuilder.loadTexts:cvsVSLLinkPortGroup.setStatus(_B)
cvsVSLConnectionChangeNotif=NotificationType((1,3,6,1,4,1,9,9,388,0,1))
cvsVSLConnectionChangeNotif.setObjects((_A,_U))
if mibBuilder.loadTexts:cvsVSLConnectionChangeNotif.setStatus(_B)
cvsDualActiveDetectionNotif=NotificationType((1,3,6,1,4,1,9,9,388,0,2))
cvsDualActiveDetectionNotif.setObjects(*((_A,_T),(_A,_V)))
if mibBuilder.loadTexts:cvsDualActiveDetectionNotif.setStatus(_B)
cvsConnectionNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,388,2,2,7))
cvsConnectionNotifsGroup.setObjects((_A,_Ao))
if mibBuilder.loadTexts:cvsConnectionNotifsGroup.setStatus(_B)
cvsDualActiveDetectionNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,388,2,2,13))
cvsDualActiveDetectionNotifsGroup.setObjects((_A,_Ap))
if mibBuilder.loadTexts:cvsDualActiveDetectionNotifsGroup.setStatus(_B)
cvsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,388,2,1,1))
cvsMIBCompliance.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cvsMIBCompliance.setStatus(_W)
cvsMIBComplianceV02=ModuleCompliance((1,3,6,1,4,1,9,9,388,2,1,2))
cvsMIBComplianceV02.setObjects(*((_A,_F),(_A,_G),(_A,_M),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_N)))
if mibBuilder.loadTexts:cvsMIBComplianceV02.setStatus(_W)
cvsMIBComplianceV03=ModuleCompliance((1,3,6,1,4,1,9,9,388,2,1,3))
cvsMIBComplianceV03.setObjects(*((_A,_F),(_A,_G),(_A,_M),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_N),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cvsMIBComplianceV03.setStatus(_W)
cvsMIBComplianceV04=ModuleCompliance((1,3,6,1,4,1,9,9,388,2,1,4))
cvsMIBComplianceV04.setObjects(*((_A,_F),(_A,_G),(_A,_M),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_N),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_Aq)))
if mibBuilder.loadTexts:cvsMIBComplianceV04.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VSSwitchID':VSSwitchID,'VSSwitchCapability':VSSwitchCapability,'VSSwitchMode':VSSwitchMode,'VSSwitchRole':VSSwitchRole,'VSConnectStatus':VSConnectStatus,'ciscoVirtualSwitchMIB':ciscoVirtualSwitchMIB,'ciscoVirtualSwitchMIBNotifs':ciscoVirtualSwitchMIBNotifs,_Ao:cvsVSLConnectionChangeNotif,_Ap:cvsDualActiveDetectionNotif,'ciscoVirtualSwitchMIBObjects':ciscoVirtualSwitchMIBObjects,'cvsGlobalObjects':cvsGlobalObjects,_e:cvsDomain,_T:cvsSwitchID,_f:cvsSwitchCapability,_g:cvsSwitchMode,_h:cvsSwitchConvertingStatus,_i:cvsVSLChangeNotifEnable,'cvsChassisObjects':cvsChassisObjects,'cvsCoreSwitchConfigTable':cvsCoreSwitchConfigTable,'cvsCoreSwitchConfigEntry':cvsCoreSwitchConfigEntry,_c:cvsCoreSwitchID,_j:cvsCoreSwitchPriority,_k:cvsCoreSwitchPreempt,_Al:cvsCoreSwitchLocation,'cvsChassisTable':cvsChassisTable,'cvsChassisEntry':cvsChassisEntry,_l:cvsChassisSwitchID,_m:cvsChassisRole,_n:cvsChassisUpTime,'cvsVSLObjects':cvsVSLObjects,'cvsVSLConnectionTable':cvsVSLConnectionTable,'cvsVSLConnectionEntry':cvsVSLConnectionEntry,_E:cvsVSLChannelIfindex,_o:cvsVSLCoreSwitchID,_U:cvsVSLConnectOperStatus,_p:cvsVSLLastConnectionStateChange,_q:cvsVSLConfiguredPortCount,_r:cvsVSLOperationalPortCount,_s:cvsVSLConnectionRowStatus,'cvsVSLStatsTable':cvsVSLStatsTable,'cvsVSLStatsEntry':cvsVSLStatsEntry,_t:cvsVSLTxTotalPkts,_u:cvsVSLTxErrorPkts,_v:cvsVSLTxChksumErrPkts,_w:cvsVSLRxTotalPkts,_x:cvsVSLRxErrorPkts,_y:cvsVSLRxChksumErrPkts,_A8:cvsVSLTxLmpPkts,_A9:cvsVSLTxRrpPkts,_AA:cvsVSLTxPingPkts,_AB:cvsVSLTxProtoPkts,_AC:cvsVSLTxDataPkts,_AD:cvsVSLTxAckPkts,_AE:cvsVSLRxLmpPkts,_AF:cvsVSLRxRrpPkts,_AG:cvsVSLRxPingPkts,_AH:cvsVSLRxProtoPkts,_AI:cvsVSLRxDataPkts,_AJ:cvsVSLRxAckPkts,_AK:cvsVSLTxTotalEobcPkts,_AL:cvsVSLTxLmpEobcPkts,_AM:cvsVSLTxRrpEobcPkts,_AN:cvsVSLTxPingEobcPkts,_AO:cvsVSLTxProtoEobcPkts,_AP:cvsVSLTxDataEobcPkts,_AQ:cvsVSLTxAckEobcPkts,_AR:cvsVSLRxTotalEobcPkts,_AS:cvsVSLRxLmpEobcPkts,_AT:cvsVSLRxRrpEobcPkts,_AU:cvsVSLRxPingEobcPkts,_AV:cvsVSLRxProtoEobcPkts,_AW:cvsVSLRxDataEobcPkts,_AX:cvsVSLRxAckEobcPkts,_AY:cvsVSLTxTotalHCPkts,_AZ:cvsVSLTxErrorHCPkts,_Aa:cvsVSLTxChksumErrHCPkts,_Ab:cvsVSLRxTotalHCPkts,_Ac:cvsVSLRxErrorHCPkts,_Ad:cvsVSLRxChksumErrHCPkts,'cvsVSLPortStatsTable':cvsVSLPortStatsTable,'cvsVSLPortStatsEntry':cvsVSLPortStatsEntry,_S:cvsVSLPortStatsIfindex,_z:cvsVSLPortTxOkPkts,_A0:cvsVSLPortTxFailPkts,_A1:cvsVSLPortRxBidirPkts,_A2:cvsVSLPortRxUnidirPkts,_A3:cvsVSLPortRxFailPkts,_A4:cvsVSLPortRxBadPkts,_Ae:cvsVSLPortRxMyInfoMismatchPkts,_Af:cvsVSLPortRxMyInfoAbsentPkts,_Ag:cvsVSLPortRxBadMacAddressPkts,_Ah:cvsVSLPortRxBadSwitchIdPkts,_Ai:cvsVSLPortRxDomainIdMismatchPkts,_Aj:cvsVSLPortRxPeerInfoMismatchPkts,'cvsVSLLinkPortTable':cvsVSLLinkPortTable,'cvsVSLLinkPortEntry':cvsVSLLinkPortEntry,_An:cvsVSLLinkPeerInterface,'cvsModuleObjects':cvsModuleObjects,'cvsModuleTable':cvsModuleTable,'cvsModuleEntry':cvsModuleEntry,_A5:cvsModuleVSSupported,_A6:cvsModuleVSLCapable,_A7:cvsModuleSlotNumber,_Ak:cvsModuleRprWarm,'cvsDualActiveDetection':cvsDualActiveDetection,_Am:cvsDualActiveDetectionNotifEnable,_V:cvsDualActiveDetectionInformation,'ciscoVirtualSwitchMIBConform':ciscoVirtualSwitchMIBConform,'cvsMIBCompliances':cvsMIBCompliances,'cvsMIBCompliance':cvsMIBCompliance,'cvsMIBComplianceV02':cvsMIBComplianceV02,'cvsMIBComplianceV03':cvsMIBComplianceV03,'cvsMIBComplianceV04':cvsMIBComplianceV04,'cvsMIBGroups':cvsMIBGroups,_F:cvsGlobalGroup,_H:cvsCoreSwitchGroup,_I:cvsChassisGroup,_J:cvsVSLConnectionGroup,_K:cvsVSLStatisticsGroup,_G:cvsModuleGroup,_L:cvsConnectionNotifsGroup,_N:cvsVSLStatisticsExtGroup,_M:cvsVssModuleStandbyGroup,_X:cvsCoreSwitchLocationGroup,_Y:cvsDualActiveDetectionNotifsControlGroup,_Z:cvsDualActiveDetectionNotifsInfoGroup,_a:cvsDualActiveDetectionNotifsGroup,_Aq:cvsVSLLinkPortGroup})