_s='hpicfVrrpOperationsGroup1'
_r='hpicfVrrpOperationsGroup'
_q='hpicfVrrpVrMainPreempt'
_p='hpicfVrrpTrackState'
_o='hpicfVrrpRemoveConfig'
_n='hpicfVrrpRespondToPing'
_m='hpicfVrrpNonstop'
_l='hpicfVrrpVrRespondToPing'
_k='hpicfVrrpAdminStatus'
_j='hpicfVrrpStatsEntry'
_i='hpicfVrrpAssoIpAddrEntry'
_h='hpicfVrrpOperEntry'
_g='read-only'
_f='not-accessible'
_e='hpicfVrrpVrTrackEntity'
_d='hpicfVrrpVrTrackType'
_c='vrrpOperVrId'
_b='VRRP-MIB'
_a='IpAddress'
_Z='Counter32'
_Y='SnmpAdminString'
_X='ifIndex'
_W='IF-MIB'
_V='hpicfVrrpOperGroup2'
_U='hpicfVrrpOperGroup1'
_T='hpicfVrrpNonstopGroup'
_S='hpicfVrrpVrPingGroup'
_R='hpicfVrrpTrackGroup'
_Q='hpicfVrrpStatsNearFailovers'
_P='hpicfVrrpVrControl'
_O='hpicfVrrpTrackRowStatus'
_N='hpicfVrrpAssoIpMask'
_M='hpicfVrrpVrPreemptDelayTime'
_L='hpicfVrrpVrTransferControl'
_K='hpicfVrrpVrMasterPreempt'
_J='hpicfVrrpVrMode'
_I='read-write'
_H='Integer32'
_G='hpicfVrrpTrackGroup1'
_F='hpicfVrrpOperGroup'
_E='read-create'
_D='TruthValue'
_C='deprecated'
_B='current'
_A='HP-ICF-VRRP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ifIndex,=mibBuilder.importSymbols(_W,_X)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Y)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_Z,'Counter64','Gauge32',_H,_a,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
vrrpAssoIpAddrEntry,vrrpOperEntry,vrrpOperVrId=mibBuilder.importSymbols(_b,'vrrpAssoIpAddrEntry','vrrpOperEntry',_c)
hpicfVrrpMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,31))
if mibBuilder.loadTexts:hpicfVrrpMIB.setRevisions(('2021-06-10 00:00','2012-11-15 00:00','2013-06-12 00:00','2012-02-22 00:00','2010-10-20 00:00','2010-07-28 00:00','2009-05-19 00:00','2008-02-20 00:00','2007-12-12 00:00','2007-08-22 00:00','2005-07-14 00:00'))
_HpicfVrrpOperations_ObjectIdentity=ObjectIdentity
hpicfVrrpOperations=_HpicfVrrpOperations_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,31,1))
class _HpicfVrrpAdminStatus_Type(TruthValue):defaultValue=2
_HpicfVrrpAdminStatus_Type.__name__=_D
_HpicfVrrpAdminStatus_Object=MibScalar
hpicfVrrpAdminStatus=_HpicfVrrpAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,1),_HpicfVrrpAdminStatus_Type())
hpicfVrrpAdminStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpicfVrrpAdminStatus.setStatus(_C)
_HpicfVrrpOperTable_Object=MibTable
hpicfVrrpOperTable=_HpicfVrrpOperTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2))
if mibBuilder.loadTexts:hpicfVrrpOperTable.setStatus(_B)
_HpicfVrrpOperEntry_Object=MibTableRow
hpicfVrrpOperEntry=_HpicfVrrpOperEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1))
if mibBuilder.loadTexts:hpicfVrrpOperEntry.setStatus(_B)
class _HpicfVrrpVrMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('owner',1),('backup',2),('uninitialized',3)))
_HpicfVrrpVrMode_Type.__name__=_H
_HpicfVrrpVrMode_Object=MibTableColumn
hpicfVrrpVrMode=_HpicfVrrpVrMode_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1,1),_HpicfVrrpVrMode_Type())
hpicfVrrpVrMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpVrMode.setStatus(_B)
class _HpicfVrrpVrMasterPreempt_Type(TruthValue):defaultValue=2
_HpicfVrrpVrMasterPreempt_Type.__name__=_D
_HpicfVrrpVrMasterPreempt_Object=MibTableColumn
hpicfVrrpVrMasterPreempt=_HpicfVrrpVrMasterPreempt_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1,2),_HpicfVrrpVrMasterPreempt_Type())
hpicfVrrpVrMasterPreempt.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpVrMasterPreempt.setStatus(_B)
class _HpicfVrrpVrTransferControl_Type(TruthValue):defaultValue=2
_HpicfVrrpVrTransferControl_Type.__name__=_D
_HpicfVrrpVrTransferControl_Object=MibTableColumn
hpicfVrrpVrTransferControl=_HpicfVrrpVrTransferControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1,3),_HpicfVrrpVrTransferControl_Type())
hpicfVrrpVrTransferControl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpVrTransferControl.setStatus(_B)
class _HpicfVrrpVrPreemptDelayTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_HpicfVrrpVrPreemptDelayTime_Type.__name__=_H
_HpicfVrrpVrPreemptDelayTime_Object=MibTableColumn
hpicfVrrpVrPreemptDelayTime=_HpicfVrrpVrPreemptDelayTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1,4),_HpicfVrrpVrPreemptDelayTime_Type())
hpicfVrrpVrPreemptDelayTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpVrPreemptDelayTime.setStatus(_B)
class _HpicfVrrpVrControl_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('failback',1),('failover',2),('failoverWithMonitoring',3),('invalid',4)))
_HpicfVrrpVrControl_Type.__name__=_H
_HpicfVrrpVrControl_Object=MibTableColumn
hpicfVrrpVrControl=_HpicfVrrpVrControl_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1,5),_HpicfVrrpVrControl_Type())
hpicfVrrpVrControl.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpVrControl.setStatus(_B)
class _HpicfVrrpVrRespondToPing_Type(TruthValue):defaultValue=1
_HpicfVrrpVrRespondToPing_Type.__name__=_D
_HpicfVrrpVrRespondToPing_Object=MibTableColumn
hpicfVrrpVrRespondToPing=_HpicfVrrpVrRespondToPing_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1,6),_HpicfVrrpVrRespondToPing_Type())
hpicfVrrpVrRespondToPing.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpVrRespondToPing.setStatus(_B)
class _HpicfVrrpVrMainPreempt_Type(TruthValue):defaultValue=2
_HpicfVrrpVrMainPreempt_Type.__name__=_D
_HpicfVrrpVrMainPreempt_Object=MibTableColumn
hpicfVrrpVrMainPreempt=_HpicfVrrpVrMainPreempt_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,2,1,7),_HpicfVrrpVrMainPreempt_Type())
hpicfVrrpVrMainPreempt.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpVrMainPreempt.setStatus(_B)
_HpicfVrrpAssoIpAddrTable_Object=MibTable
hpicfVrrpAssoIpAddrTable=_HpicfVrrpAssoIpAddrTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,3))
if mibBuilder.loadTexts:hpicfVrrpAssoIpAddrTable.setStatus(_B)
_HpicfVrrpAssoIpAddrEntry_Object=MibTableRow
hpicfVrrpAssoIpAddrEntry=_HpicfVrrpAssoIpAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,3,1))
if mibBuilder.loadTexts:hpicfVrrpAssoIpAddrEntry.setStatus(_B)
class _HpicfVrrpAssoIpMask_Type(IpAddress):defaultHexValue='00000000'
_HpicfVrrpAssoIpMask_Type.__name__=_a
_HpicfVrrpAssoIpMask_Object=MibTableColumn
hpicfVrrpAssoIpMask=_HpicfVrrpAssoIpMask_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,3,1,1),_HpicfVrrpAssoIpMask_Type())
hpicfVrrpAssoIpMask.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpAssoIpMask.setStatus(_B)
_HpicfVrrpTrackTable_Object=MibTable
hpicfVrrpTrackTable=_HpicfVrrpTrackTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,5))
if mibBuilder.loadTexts:hpicfVrrpTrackTable.setStatus(_B)
_HpicfVrrpTrackEntry_Object=MibTableRow
hpicfVrrpTrackEntry=_HpicfVrrpTrackEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,5,1))
hpicfVrrpTrackEntry.setIndexNames((0,_W,_X),(0,_b,_c),(0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:hpicfVrrpTrackEntry.setStatus(_B)
class _HpicfVrrpVrTrackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('port',1),('trunk',2),('vlan',3)))
_HpicfVrrpVrTrackType_Type.__name__=_H
_HpicfVrrpVrTrackType_Object=MibTableColumn
hpicfVrrpVrTrackType=_HpicfVrrpVrTrackType_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,5,1,1),_HpicfVrrpVrTrackType_Type())
hpicfVrrpVrTrackType.setMaxAccess(_f)
if mibBuilder.loadTexts:hpicfVrrpVrTrackType.setStatus(_B)
class _HpicfVrrpVrTrackEntity_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpicfVrrpVrTrackEntity_Type.__name__=_Y
_HpicfVrrpVrTrackEntity_Object=MibTableColumn
hpicfVrrpVrTrackEntity=_HpicfVrrpVrTrackEntity_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,5,1,2),_HpicfVrrpVrTrackEntity_Type())
hpicfVrrpVrTrackEntity.setMaxAccess(_f)
if mibBuilder.loadTexts:hpicfVrrpVrTrackEntity.setStatus(_B)
_HpicfVrrpTrackRowStatus_Type=RowStatus
_HpicfVrrpTrackRowStatus_Object=MibTableColumn
hpicfVrrpTrackRowStatus=_HpicfVrrpTrackRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,5,1,3),_HpicfVrrpTrackRowStatus_Type())
hpicfVrrpTrackRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfVrrpTrackRowStatus.setStatus(_B)
class _HpicfVrrpTrackState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_HpicfVrrpTrackState_Type.__name__=_H
_HpicfVrrpTrackState_Object=MibTableColumn
hpicfVrrpTrackState=_HpicfVrrpTrackState_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,5,1,4),_HpicfVrrpTrackState_Type())
hpicfVrrpTrackState.setMaxAccess(_g)
if mibBuilder.loadTexts:hpicfVrrpTrackState.setStatus(_B)
_HpicfVrrpStatsTable_Object=MibTable
hpicfVrrpStatsTable=_HpicfVrrpStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,6))
if mibBuilder.loadTexts:hpicfVrrpStatsTable.setStatus(_B)
_HpicfVrrpStatsEntry_Object=MibTableRow
hpicfVrrpStatsEntry=_HpicfVrrpStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,6,1))
if mibBuilder.loadTexts:hpicfVrrpStatsEntry.setStatus(_B)
class _HpicfVrrpStatsNearFailovers_Type(Counter32):defaultValue=0
_HpicfVrrpStatsNearFailovers_Type.__name__=_Z
_HpicfVrrpStatsNearFailovers_Object=MibTableColumn
hpicfVrrpStatsNearFailovers=_HpicfVrrpStatsNearFailovers_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,6,1,1),_HpicfVrrpStatsNearFailovers_Type())
hpicfVrrpStatsNearFailovers.setMaxAccess(_g)
if mibBuilder.loadTexts:hpicfVrrpStatsNearFailovers.setStatus(_B)
class _HpicfVrrpRespondToPing_Type(TruthValue):defaultValue=2
_HpicfVrrpRespondToPing_Type.__name__=_D
_HpicfVrrpRespondToPing_Object=MibScalar
hpicfVrrpRespondToPing=_HpicfVrrpRespondToPing_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,7),_HpicfVrrpRespondToPing_Type())
hpicfVrrpRespondToPing.setMaxAccess(_I)
if mibBuilder.loadTexts:hpicfVrrpRespondToPing.setStatus(_C)
class _HpicfVrrpRemoveConfig_Type(TruthValue):defaultValue=2
_HpicfVrrpRemoveConfig_Type.__name__=_D
_HpicfVrrpRemoveConfig_Object=MibScalar
hpicfVrrpRemoveConfig=_HpicfVrrpRemoveConfig_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,8),_HpicfVrrpRemoveConfig_Type())
hpicfVrrpRemoveConfig.setMaxAccess(_I)
if mibBuilder.loadTexts:hpicfVrrpRemoveConfig.setStatus(_C)
class _HpicfVrrpNonstop_Type(TruthValue):defaultValue=2
_HpicfVrrpNonstop_Type.__name__=_D
_HpicfVrrpNonstop_Object=MibScalar
hpicfVrrpNonstop=_HpicfVrrpNonstop_Object((1,3,6,1,4,1,11,2,14,11,5,1,31,1,9),_HpicfVrrpNonstop_Type())
hpicfVrrpNonstop.setMaxAccess(_I)
if mibBuilder.loadTexts:hpicfVrrpNonstop.setStatus(_C)
_HpicfVrrpConformance_ObjectIdentity=ObjectIdentity
hpicfVrrpConformance=_HpicfVrrpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,31,2))
_HpicfVrrpMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfVrrpMIBCompliances=_HpicfVrrpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1))
_HpicfVrrpMIBGroups_ObjectIdentity=ObjectIdentity
hpicfVrrpMIBGroups=_HpicfVrrpMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2))
vrrpOperEntry.registerAugmentions((_A,_h))
hpicfVrrpOperEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
vrrpAssoIpAddrEntry.registerAugmentions((_A,_i))
hpicfVrrpAssoIpAddrEntry.setIndexNames(*vrrpAssoIpAddrEntry.getIndexNames())
vrrpOperEntry.registerAugmentions((_A,_j))
hpicfVrrpStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())
hpicfVrrpOperGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,1))
hpicfVrrpOperGroup.setObjects(*((_A,_k),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfVrrpOperGroup.setStatus(_C)
hpicfVrrpTrackGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,2))
hpicfVrrpTrackGroup.setObjects(*((_A,_O),(_A,_P)))
if mibBuilder.loadTexts:hpicfVrrpTrackGroup.setStatus(_C)
hpicfVrrpVrPingGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,3))
hpicfVrrpVrPingGroup.setObjects((_A,_l))
if mibBuilder.loadTexts:hpicfVrrpVrPingGroup.setStatus(_B)
hpicfVrrpNonstopGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,4))
hpicfVrrpNonstopGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:hpicfVrrpNonstopGroup.setStatus(_C)
hpicfVrrpOperationsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,5))
hpicfVrrpOperationsGroup.setObjects(*((_A,_n),(_A,_o),(_A,_Q)))
if mibBuilder.loadTexts:hpicfVrrpOperationsGroup.setStatus(_C)
hpicfVrrpTrackGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,6))
hpicfVrrpTrackGroup1.setObjects(*((_A,_O),(_A,_P),(_A,_p)))
if mibBuilder.loadTexts:hpicfVrrpTrackGroup1.setStatus(_B)
hpicfVrrpOperGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,7))
hpicfVrrpOperGroup1.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:hpicfVrrpOperGroup1.setStatus(_C)
hpicfVrrpOperationsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,8))
hpicfVrrpOperationsGroup1.setObjects((_A,_Q))
if mibBuilder.loadTexts:hpicfVrrpOperationsGroup1.setStatus(_B)
hpicfVrrpOperGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,31,2,2,9))
hpicfVrrpOperGroup2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_q)))
if mibBuilder.loadTexts:hpicfVrrpOperGroup2.setStatus(_B)
hpicfVrrpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,1))
hpicfVrrpMIBCompliance.setObjects(*((_A,_F),(_A,_F)))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance.setStatus(_C)
hpicfVrrpMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,2))
hpicfVrrpMIBCompliance1.setObjects(*((_A,_F),(_A,_R),(_A,_F),(_A,_R)))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance1.setStatus(_C)
hpicfVrrpMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,3))
hpicfVrrpMIBCompliance2.setObjects(*((_A,_S),(_A,_S)))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance2.setStatus(_B)
hpicfVrrpMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,4))
hpicfVrrpMIBCompliance3.setObjects(*((_A,_T),(_A,_T)))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance3.setStatus(_C)
hpicfVrrpMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,5))
hpicfVrrpMIBCompliance4.setObjects((_A,_r))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance4.setStatus(_C)
hpicfVrrpMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,6))
hpicfVrrpMIBCompliance5.setObjects(*((_A,_F),(_A,_G),(_A,_F),(_A,_G)))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance5.setStatus(_C)
hpicfVrrpMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,7))
hpicfVrrpMIBCompliance6.setObjects(*((_A,_U),(_A,_G),(_A,_U),(_A,_G)))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance6.setStatus(_C)
hpicfVrrpMIBCompliance7=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,8))
hpicfVrrpMIBCompliance7.setObjects((_A,_s))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance7.setStatus(_B)
hpicfVrrpMIBCompliance8=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,31,2,1,9))
hpicfVrrpMIBCompliance8.setObjects(*((_A,_V),(_A,_G),(_A,_V),(_A,_G)))
if mibBuilder.loadTexts:hpicfVrrpMIBCompliance8.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfVrrpMIB':hpicfVrrpMIB,'hpicfVrrpOperations':hpicfVrrpOperations,_k:hpicfVrrpAdminStatus,'hpicfVrrpOperTable':hpicfVrrpOperTable,_h:hpicfVrrpOperEntry,_J:hpicfVrrpVrMode,_K:hpicfVrrpVrMasterPreempt,_L:hpicfVrrpVrTransferControl,_M:hpicfVrrpVrPreemptDelayTime,_P:hpicfVrrpVrControl,_l:hpicfVrrpVrRespondToPing,_q:hpicfVrrpVrMainPreempt,'hpicfVrrpAssoIpAddrTable':hpicfVrrpAssoIpAddrTable,_i:hpicfVrrpAssoIpAddrEntry,_N:hpicfVrrpAssoIpMask,'hpicfVrrpTrackTable':hpicfVrrpTrackTable,'hpicfVrrpTrackEntry':hpicfVrrpTrackEntry,_d:hpicfVrrpVrTrackType,_e:hpicfVrrpVrTrackEntity,_O:hpicfVrrpTrackRowStatus,_p:hpicfVrrpTrackState,'hpicfVrrpStatsTable':hpicfVrrpStatsTable,_j:hpicfVrrpStatsEntry,_Q:hpicfVrrpStatsNearFailovers,_n:hpicfVrrpRespondToPing,_o:hpicfVrrpRemoveConfig,_m:hpicfVrrpNonstop,'hpicfVrrpConformance':hpicfVrrpConformance,'hpicfVrrpMIBCompliances':hpicfVrrpMIBCompliances,'hpicfVrrpMIBCompliance':hpicfVrrpMIBCompliance,'hpicfVrrpMIBCompliance1':hpicfVrrpMIBCompliance1,'hpicfVrrpMIBCompliance2':hpicfVrrpMIBCompliance2,'hpicfVrrpMIBCompliance3':hpicfVrrpMIBCompliance3,'hpicfVrrpMIBCompliance4':hpicfVrrpMIBCompliance4,'hpicfVrrpMIBCompliance5':hpicfVrrpMIBCompliance5,'hpicfVrrpMIBCompliance6':hpicfVrrpMIBCompliance6,'hpicfVrrpMIBCompliance7':hpicfVrrpMIBCompliance7,'hpicfVrrpMIBCompliance8':hpicfVrrpMIBCompliance8,'hpicfVrrpMIBGroups':hpicfVrrpMIBGroups,_F:hpicfVrrpOperGroup,_R:hpicfVrrpTrackGroup,_S:hpicfVrrpVrPingGroup,_T:hpicfVrrpNonstopGroup,_r:hpicfVrrpOperationsGroup,_G:hpicfVrrpTrackGroup1,_U:hpicfVrrpOperGroup1,_s:hpicfVrrpOperationsGroup1,_V:hpicfVrrpOperGroup2})