_A1='me1200LldpControlStatisticsClearGlobalInfoGroup'
_A0='me1200LldpControlStatisticsClearTableInfoGroup'
_z='me1200LldpNeighborsManagementInformationInfoGroup'
_y='me1200LldpNeighborsInformationInfoGroup'
_x='me1200LldpStatisticsTableInfoGroup'
_w='me1200LldpStatisticsGlobalCountersInfoGroup'
_v='me1200LldpConfigurationInfoGroup'
_u='me1200LldpGlobalInfoGroup'
_t='me1200LldpControlStatisticsClearGlobalClear'
_s='me1200LldpControlStatisticsClearStatisticsClear'
_r='me1200LldpNeighborsManagementInformationSystemManagementAddress'
_q='me1200LldpNeighborsInformationSystemCapabilitiesEnable'
_p='me1200LldpNeighborsInformationSystemCapabilities'
_o='me1200LldpNeighborsInformationSystemDescription'
_n='me1200LldpNeighborsInformationSystemName'
_m='me1200LldpNeighborsInformationPortDescription'
_l='me1200LldpNeighborsInformationPortId'
_k='me1200LldpNeighborsInformationChassisId'
_j='me1200LldpStatisticsAgeOuts'
_i='me1200LldpStatisticsTLVsOrgDiscarded'
_h='me1200LldpStatisticsTLVsUnrecognized'
_g='me1200LldpStatisticsTLVsDiscarded'
_f='me1200LldpStatisticsRxDiscarded'
_e='me1200LldpStatisticsRxError'
_d='me1200LldpStatisticsRxTotal'
_c='me1200LldpStatisticsTxTotal'
_b='me1200LldpStatisticsGlobalCountersLastChangeTime'
_a='me1200LldpStatisticsGlobalCountersTableAgeOuts'
_Z='me1200LldpStatisticsGlobalCountersTableDrops'
_Y='me1200LldpStatisticsGlobalCountersTableDeletes'
_X='me1200LldpStatisticsGlobalCountersTableInserts'
_W='me1200LldpConfigurationOptionalTlvs'
_V='me1200LldpConfigurationCdpAware'
_U='me1200LldpConfigurationAdminState'
_T='me1200LldpGlobalTxDelay'
_S='me1200LldpGlobalMsgTxInterval'
_R='me1200LldpGlobalMsgTxHold'
_Q='me1200LldpGlobalInitDelay'
_P='me1200LldpControlStatisticsClearIfIndex'
_O='me1200LldpNeighborsManagementInformationLldpManagement'
_N='me1200LldpNeighborsManagementInformationLldpIndex'
_M='me1200LldpNeighborsManagementInformationIfIndex'
_L='me1200LldpNeighborsInformationLldpIndex'
_K='me1200LldpNeighborsInformationIfIndex'
_J='me1200LldpStatisticsIfIndex'
_I='me1200LldpConfigurationIfIndex'
_H='ME1200Unsigned8'
_G='Integer32'
_F='ME1200DisplayString'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='ME1200-LLDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200DisplayString,ME1200InterfaceIndex,ME1200Unsigned16,ME1200Unsigned64,ME1200Unsigned8=mibBuilder.importSymbols('ME1200-TC',_F,'ME1200InterfaceIndex','ME1200Unsigned16','ME1200Unsigned64',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200LldpMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,34))
if mibBuilder.loadTexts:me1200LldpMib.setRevisions(('2014-03-11 00:00','2014-02-18 00:00','2014-01-29 00:00','2013-10-08 00:00'))
class ME1200lldpAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disabled',0),('txAndRx',1),('txOnly',2),('rxOnly',3)))
_Me1200LldpObjects_ObjectIdentity=ObjectIdentity
me1200LldpObjects=_Me1200LldpObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1))
_Me1200LldpConfig_ObjectIdentity=ObjectIdentity
me1200LldpConfig=_Me1200LldpConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,2))
_Me1200LldpGlobal_ObjectIdentity=ObjectIdentity
me1200LldpGlobal=_Me1200LldpGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,2,1))
_Me1200LldpGlobalInitDelay_Type=ME1200Unsigned16
_Me1200LldpGlobalInitDelay_Object=MibScalar
me1200LldpGlobalInitDelay=_Me1200LldpGlobalInitDelay_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,1,1),_Me1200LldpGlobalInitDelay_Type())
me1200LldpGlobalInitDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpGlobalInitDelay.setStatus(_A)
_Me1200LldpGlobalMsgTxHold_Type=ME1200Unsigned16
_Me1200LldpGlobalMsgTxHold_Object=MibScalar
me1200LldpGlobalMsgTxHold=_Me1200LldpGlobalMsgTxHold_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,1,2),_Me1200LldpGlobalMsgTxHold_Type())
me1200LldpGlobalMsgTxHold.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpGlobalMsgTxHold.setStatus(_A)
_Me1200LldpGlobalMsgTxInterval_Type=ME1200Unsigned16
_Me1200LldpGlobalMsgTxInterval_Object=MibScalar
me1200LldpGlobalMsgTxInterval=_Me1200LldpGlobalMsgTxInterval_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,1,3),_Me1200LldpGlobalMsgTxInterval_Type())
me1200LldpGlobalMsgTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpGlobalMsgTxInterval.setStatus(_A)
_Me1200LldpGlobalTxDelay_Type=ME1200Unsigned16
_Me1200LldpGlobalTxDelay_Object=MibScalar
me1200LldpGlobalTxDelay=_Me1200LldpGlobalTxDelay_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,1,4),_Me1200LldpGlobalTxDelay_Type())
me1200LldpGlobalTxDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpGlobalTxDelay.setStatus(_A)
_Me1200LldpConfigurationTable_Object=MibTable
me1200LldpConfigurationTable=_Me1200LldpConfigurationTable_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,2))
if mibBuilder.loadTexts:me1200LldpConfigurationTable.setStatus(_A)
_Me1200LldpConfigurationEntry_Object=MibTableRow
me1200LldpConfigurationEntry=_Me1200LldpConfigurationEntry_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,2,1))
me1200LldpConfigurationEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:me1200LldpConfigurationEntry.setStatus(_A)
_Me1200LldpConfigurationIfIndex_Type=ME1200InterfaceIndex
_Me1200LldpConfigurationIfIndex_Object=MibTableColumn
me1200LldpConfigurationIfIndex=_Me1200LldpConfigurationIfIndex_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,2,1,1),_Me1200LldpConfigurationIfIndex_Type())
me1200LldpConfigurationIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpConfigurationIfIndex.setStatus(_A)
_Me1200LldpConfigurationAdminState_Type=ME1200lldpAdminState
_Me1200LldpConfigurationAdminState_Object=MibTableColumn
me1200LldpConfigurationAdminState=_Me1200LldpConfigurationAdminState_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,2,1,3),_Me1200LldpConfigurationAdminState_Type())
me1200LldpConfigurationAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpConfigurationAdminState.setStatus(_A)
_Me1200LldpConfigurationCdpAware_Type=TruthValue
_Me1200LldpConfigurationCdpAware_Object=MibTableColumn
me1200LldpConfigurationCdpAware=_Me1200LldpConfigurationCdpAware_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,2,1,4),_Me1200LldpConfigurationCdpAware_Type())
me1200LldpConfigurationCdpAware.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpConfigurationCdpAware.setStatus(_A)
class _Me1200LldpConfigurationOptionalTlvs_Type(ME1200Unsigned8):subtypeSpec=ME1200Unsigned8.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_Me1200LldpConfigurationOptionalTlvs_Type.__name__=_H
_Me1200LldpConfigurationOptionalTlvs_Object=MibTableColumn
me1200LldpConfigurationOptionalTlvs=_Me1200LldpConfigurationOptionalTlvs_Object((1,3,6,1,4,1,9,9,815,1,34,1,2,2,1,5),_Me1200LldpConfigurationOptionalTlvs_Type())
me1200LldpConfigurationOptionalTlvs.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpConfigurationOptionalTlvs.setStatus(_A)
_Me1200LldpStatus_ObjectIdentity=ObjectIdentity
me1200LldpStatus=_Me1200LldpStatus_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,3))
_Me1200LldpStatistics_ObjectIdentity=ObjectIdentity
me1200LldpStatistics=_Me1200LldpStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,3,2))
_Me1200LldpStatisticsGlobalCounters_ObjectIdentity=ObjectIdentity
me1200LldpStatisticsGlobalCounters=_Me1200LldpStatisticsGlobalCounters_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,3,2,1))
_Me1200LldpStatisticsGlobalCountersTableInserts_Type=Unsigned32
_Me1200LldpStatisticsGlobalCountersTableInserts_Object=MibScalar
me1200LldpStatisticsGlobalCountersTableInserts=_Me1200LldpStatisticsGlobalCountersTableInserts_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,1,1),_Me1200LldpStatisticsGlobalCountersTableInserts_Type())
me1200LldpStatisticsGlobalCountersTableInserts.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsGlobalCountersTableInserts.setStatus(_A)
_Me1200LldpStatisticsGlobalCountersTableDeletes_Type=Unsigned32
_Me1200LldpStatisticsGlobalCountersTableDeletes_Object=MibScalar
me1200LldpStatisticsGlobalCountersTableDeletes=_Me1200LldpStatisticsGlobalCountersTableDeletes_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,1,2),_Me1200LldpStatisticsGlobalCountersTableDeletes_Type())
me1200LldpStatisticsGlobalCountersTableDeletes.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsGlobalCountersTableDeletes.setStatus(_A)
_Me1200LldpStatisticsGlobalCountersTableDrops_Type=Unsigned32
_Me1200LldpStatisticsGlobalCountersTableDrops_Object=MibScalar
me1200LldpStatisticsGlobalCountersTableDrops=_Me1200LldpStatisticsGlobalCountersTableDrops_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,1,3),_Me1200LldpStatisticsGlobalCountersTableDrops_Type())
me1200LldpStatisticsGlobalCountersTableDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsGlobalCountersTableDrops.setStatus(_A)
_Me1200LldpStatisticsGlobalCountersTableAgeOuts_Type=Unsigned32
_Me1200LldpStatisticsGlobalCountersTableAgeOuts_Object=MibScalar
me1200LldpStatisticsGlobalCountersTableAgeOuts=_Me1200LldpStatisticsGlobalCountersTableAgeOuts_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,1,4),_Me1200LldpStatisticsGlobalCountersTableAgeOuts_Type())
me1200LldpStatisticsGlobalCountersTableAgeOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsGlobalCountersTableAgeOuts.setStatus(_A)
_Me1200LldpStatisticsGlobalCountersLastChangeTime_Type=ME1200Unsigned64
_Me1200LldpStatisticsGlobalCountersLastChangeTime_Object=MibScalar
me1200LldpStatisticsGlobalCountersLastChangeTime=_Me1200LldpStatisticsGlobalCountersLastChangeTime_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,1,5),_Me1200LldpStatisticsGlobalCountersLastChangeTime_Type())
me1200LldpStatisticsGlobalCountersLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsGlobalCountersLastChangeTime.setStatus(_A)
_Me1200LldpStatisticsTable_Object=MibTable
me1200LldpStatisticsTable=_Me1200LldpStatisticsTable_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2))
if mibBuilder.loadTexts:me1200LldpStatisticsTable.setStatus(_A)
_Me1200LldpStatisticsEntry_Object=MibTableRow
me1200LldpStatisticsEntry=_Me1200LldpStatisticsEntry_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1))
me1200LldpStatisticsEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:me1200LldpStatisticsEntry.setStatus(_A)
_Me1200LldpStatisticsIfIndex_Type=ME1200InterfaceIndex
_Me1200LldpStatisticsIfIndex_Object=MibTableColumn
me1200LldpStatisticsIfIndex=_Me1200LldpStatisticsIfIndex_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,1),_Me1200LldpStatisticsIfIndex_Type())
me1200LldpStatisticsIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpStatisticsIfIndex.setStatus(_A)
_Me1200LldpStatisticsTxTotal_Type=Unsigned32
_Me1200LldpStatisticsTxTotal_Object=MibTableColumn
me1200LldpStatisticsTxTotal=_Me1200LldpStatisticsTxTotal_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,2),_Me1200LldpStatisticsTxTotal_Type())
me1200LldpStatisticsTxTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsTxTotal.setStatus(_A)
_Me1200LldpStatisticsRxTotal_Type=Unsigned32
_Me1200LldpStatisticsRxTotal_Object=MibTableColumn
me1200LldpStatisticsRxTotal=_Me1200LldpStatisticsRxTotal_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,3),_Me1200LldpStatisticsRxTotal_Type())
me1200LldpStatisticsRxTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsRxTotal.setStatus(_A)
_Me1200LldpStatisticsRxError_Type=Unsigned32
_Me1200LldpStatisticsRxError_Object=MibTableColumn
me1200LldpStatisticsRxError=_Me1200LldpStatisticsRxError_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,4),_Me1200LldpStatisticsRxError_Type())
me1200LldpStatisticsRxError.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsRxError.setStatus(_A)
_Me1200LldpStatisticsRxDiscarded_Type=Unsigned32
_Me1200LldpStatisticsRxDiscarded_Object=MibTableColumn
me1200LldpStatisticsRxDiscarded=_Me1200LldpStatisticsRxDiscarded_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,5),_Me1200LldpStatisticsRxDiscarded_Type())
me1200LldpStatisticsRxDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsRxDiscarded.setStatus(_A)
_Me1200LldpStatisticsTLVsDiscarded_Type=Unsigned32
_Me1200LldpStatisticsTLVsDiscarded_Object=MibTableColumn
me1200LldpStatisticsTLVsDiscarded=_Me1200LldpStatisticsTLVsDiscarded_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,6),_Me1200LldpStatisticsTLVsDiscarded_Type())
me1200LldpStatisticsTLVsDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsTLVsDiscarded.setStatus(_A)
_Me1200LldpStatisticsTLVsUnrecognized_Type=Unsigned32
_Me1200LldpStatisticsTLVsUnrecognized_Object=MibTableColumn
me1200LldpStatisticsTLVsUnrecognized=_Me1200LldpStatisticsTLVsUnrecognized_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,7),_Me1200LldpStatisticsTLVsUnrecognized_Type())
me1200LldpStatisticsTLVsUnrecognized.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsTLVsUnrecognized.setStatus(_A)
_Me1200LldpStatisticsTLVsOrgDiscarded_Type=Unsigned32
_Me1200LldpStatisticsTLVsOrgDiscarded_Object=MibTableColumn
me1200LldpStatisticsTLVsOrgDiscarded=_Me1200LldpStatisticsTLVsOrgDiscarded_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,8),_Me1200LldpStatisticsTLVsOrgDiscarded_Type())
me1200LldpStatisticsTLVsOrgDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsTLVsOrgDiscarded.setStatus(_A)
_Me1200LldpStatisticsAgeOuts_Type=Unsigned32
_Me1200LldpStatisticsAgeOuts_Object=MibTableColumn
me1200LldpStatisticsAgeOuts=_Me1200LldpStatisticsAgeOuts_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,2,2,1,9),_Me1200LldpStatisticsAgeOuts_Type())
me1200LldpStatisticsAgeOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpStatisticsAgeOuts.setStatus(_A)
_Me1200LldpNeighborsInformationTable_Object=MibTable
me1200LldpNeighborsInformationTable=_Me1200LldpNeighborsInformationTable_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3))
if mibBuilder.loadTexts:me1200LldpNeighborsInformationTable.setStatus(_A)
_Me1200LldpNeighborsInformationEntry_Object=MibTableRow
me1200LldpNeighborsInformationEntry=_Me1200LldpNeighborsInformationEntry_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1))
me1200LldpNeighborsInformationEntry.setIndexNames((0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:me1200LldpNeighborsInformationEntry.setStatus(_A)
_Me1200LldpNeighborsInformationIfIndex_Type=ME1200InterfaceIndex
_Me1200LldpNeighborsInformationIfIndex_Object=MibTableColumn
me1200LldpNeighborsInformationIfIndex=_Me1200LldpNeighborsInformationIfIndex_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,1),_Me1200LldpNeighborsInformationIfIndex_Type())
me1200LldpNeighborsInformationIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationIfIndex.setStatus(_A)
class _Me1200LldpNeighborsInformationLldpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,192))
_Me1200LldpNeighborsInformationLldpIndex_Type.__name__=_G
_Me1200LldpNeighborsInformationLldpIndex_Object=MibTableColumn
me1200LldpNeighborsInformationLldpIndex=_Me1200LldpNeighborsInformationLldpIndex_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,2),_Me1200LldpNeighborsInformationLldpIndex_Type())
me1200LldpNeighborsInformationLldpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationLldpIndex.setStatus(_A)
class _Me1200LldpNeighborsInformationChassisId_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200LldpNeighborsInformationChassisId_Type.__name__=_F
_Me1200LldpNeighborsInformationChassisId_Object=MibTableColumn
me1200LldpNeighborsInformationChassisId=_Me1200LldpNeighborsInformationChassisId_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,4),_Me1200LldpNeighborsInformationChassisId_Type())
me1200LldpNeighborsInformationChassisId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationChassisId.setStatus(_A)
class _Me1200LldpNeighborsInformationPortId_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200LldpNeighborsInformationPortId_Type.__name__=_F
_Me1200LldpNeighborsInformationPortId_Object=MibTableColumn
me1200LldpNeighborsInformationPortId=_Me1200LldpNeighborsInformationPortId_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,5),_Me1200LldpNeighborsInformationPortId_Type())
me1200LldpNeighborsInformationPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationPortId.setStatus(_A)
class _Me1200LldpNeighborsInformationPortDescription_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200LldpNeighborsInformationPortDescription_Type.__name__=_F
_Me1200LldpNeighborsInformationPortDescription_Object=MibTableColumn
me1200LldpNeighborsInformationPortDescription=_Me1200LldpNeighborsInformationPortDescription_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,6),_Me1200LldpNeighborsInformationPortDescription_Type())
me1200LldpNeighborsInformationPortDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationPortDescription.setStatus(_A)
class _Me1200LldpNeighborsInformationSystemName_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200LldpNeighborsInformationSystemName_Type.__name__=_F
_Me1200LldpNeighborsInformationSystemName_Object=MibTableColumn
me1200LldpNeighborsInformationSystemName=_Me1200LldpNeighborsInformationSystemName_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,7),_Me1200LldpNeighborsInformationSystemName_Type())
me1200LldpNeighborsInformationSystemName.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationSystemName.setStatus(_A)
class _Me1200LldpNeighborsInformationSystemDescription_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,254))
_Me1200LldpNeighborsInformationSystemDescription_Type.__name__=_F
_Me1200LldpNeighborsInformationSystemDescription_Object=MibTableColumn
me1200LldpNeighborsInformationSystemDescription=_Me1200LldpNeighborsInformationSystemDescription_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,8),_Me1200LldpNeighborsInformationSystemDescription_Type())
me1200LldpNeighborsInformationSystemDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationSystemDescription.setStatus(_A)
_Me1200LldpNeighborsInformationSystemCapabilities_Type=ME1200Unsigned16
_Me1200LldpNeighborsInformationSystemCapabilities_Object=MibTableColumn
me1200LldpNeighborsInformationSystemCapabilities=_Me1200LldpNeighborsInformationSystemCapabilities_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,9),_Me1200LldpNeighborsInformationSystemCapabilities_Type())
me1200LldpNeighborsInformationSystemCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationSystemCapabilities.setStatus(_A)
_Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Type=ME1200Unsigned16
_Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Object=MibTableColumn
me1200LldpNeighborsInformationSystemCapabilitiesEnable=_Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,3,1,10),_Me1200LldpNeighborsInformationSystemCapabilitiesEnable_Type())
me1200LldpNeighborsInformationSystemCapabilitiesEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsInformationSystemCapabilitiesEnable.setStatus(_A)
_Me1200LldpNeighborsManagementInformationTable_Object=MibTable
me1200LldpNeighborsManagementInformationTable=_Me1200LldpNeighborsManagementInformationTable_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,4))
if mibBuilder.loadTexts:me1200LldpNeighborsManagementInformationTable.setStatus(_A)
_Me1200LldpNeighborsManagementInformationEntry_Object=MibTableRow
me1200LldpNeighborsManagementInformationEntry=_Me1200LldpNeighborsManagementInformationEntry_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,4,1))
me1200LldpNeighborsManagementInformationEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:me1200LldpNeighborsManagementInformationEntry.setStatus(_A)
_Me1200LldpNeighborsManagementInformationIfIndex_Type=ME1200InterfaceIndex
_Me1200LldpNeighborsManagementInformationIfIndex_Object=MibTableColumn
me1200LldpNeighborsManagementInformationIfIndex=_Me1200LldpNeighborsManagementInformationIfIndex_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,4,1,1),_Me1200LldpNeighborsManagementInformationIfIndex_Type())
me1200LldpNeighborsManagementInformationIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpNeighborsManagementInformationIfIndex.setStatus(_A)
class _Me1200LldpNeighborsManagementInformationLldpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,192))
_Me1200LldpNeighborsManagementInformationLldpIndex_Type.__name__=_G
_Me1200LldpNeighborsManagementInformationLldpIndex_Object=MibTableColumn
me1200LldpNeighborsManagementInformationLldpIndex=_Me1200LldpNeighborsManagementInformationLldpIndex_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,4,1,2),_Me1200LldpNeighborsManagementInformationLldpIndex_Type())
me1200LldpNeighborsManagementInformationLldpIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpNeighborsManagementInformationLldpIndex.setStatus(_A)
class _Me1200LldpNeighborsManagementInformationLldpManagement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_Me1200LldpNeighborsManagementInformationLldpManagement_Type.__name__=_G
_Me1200LldpNeighborsManagementInformationLldpManagement_Object=MibTableColumn
me1200LldpNeighborsManagementInformationLldpManagement=_Me1200LldpNeighborsManagementInformationLldpManagement_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,4,1,3),_Me1200LldpNeighborsManagementInformationLldpManagement_Type())
me1200LldpNeighborsManagementInformationLldpManagement.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpNeighborsManagementInformationLldpManagement.setStatus(_A)
class _Me1200LldpNeighborsManagementInformationSystemManagementAddress_Type(ME1200DisplayString):subtypeSpec=ME1200DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,166))
_Me1200LldpNeighborsManagementInformationSystemManagementAddress_Type.__name__=_F
_Me1200LldpNeighborsManagementInformationSystemManagementAddress_Object=MibTableColumn
me1200LldpNeighborsManagementInformationSystemManagementAddress=_Me1200LldpNeighborsManagementInformationSystemManagementAddress_Object((1,3,6,1,4,1,9,9,815,1,34,1,3,4,1,5),_Me1200LldpNeighborsManagementInformationSystemManagementAddress_Type())
me1200LldpNeighborsManagementInformationSystemManagementAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200LldpNeighborsManagementInformationSystemManagementAddress.setStatus(_A)
_Me1200LldpControl_ObjectIdentity=ObjectIdentity
me1200LldpControl=_Me1200LldpControl_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,4))
_Me1200LldpStatisticsClear_ObjectIdentity=ObjectIdentity
me1200LldpStatisticsClear=_Me1200LldpStatisticsClear_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,4,1))
_Me1200LldpControlStatisticsClearTable_Object=MibTable
me1200LldpControlStatisticsClearTable=_Me1200LldpControlStatisticsClearTable_Object((1,3,6,1,4,1,9,9,815,1,34,1,4,1,1))
if mibBuilder.loadTexts:me1200LldpControlStatisticsClearTable.setStatus(_A)
_Me1200LldpControlStatisticsClearEntry_Object=MibTableRow
me1200LldpControlStatisticsClearEntry=_Me1200LldpControlStatisticsClearEntry_Object((1,3,6,1,4,1,9,9,815,1,34,1,4,1,1,1))
me1200LldpControlStatisticsClearEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:me1200LldpControlStatisticsClearEntry.setStatus(_A)
_Me1200LldpControlStatisticsClearIfIndex_Type=ME1200InterfaceIndex
_Me1200LldpControlStatisticsClearIfIndex_Object=MibTableColumn
me1200LldpControlStatisticsClearIfIndex=_Me1200LldpControlStatisticsClearIfIndex_Object((1,3,6,1,4,1,9,9,815,1,34,1,4,1,1,1,1),_Me1200LldpControlStatisticsClearIfIndex_Type())
me1200LldpControlStatisticsClearIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:me1200LldpControlStatisticsClearIfIndex.setStatus(_A)
_Me1200LldpControlStatisticsClearStatisticsClear_Type=TruthValue
_Me1200LldpControlStatisticsClearStatisticsClear_Object=MibTableColumn
me1200LldpControlStatisticsClearStatisticsClear=_Me1200LldpControlStatisticsClearStatisticsClear_Object((1,3,6,1,4,1,9,9,815,1,34,1,4,1,1,1,2),_Me1200LldpControlStatisticsClearStatisticsClear_Type())
me1200LldpControlStatisticsClearStatisticsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpControlStatisticsClearStatisticsClear.setStatus(_A)
_Me1200LldpControlStatisticsClearGlobal_ObjectIdentity=ObjectIdentity
me1200LldpControlStatisticsClearGlobal=_Me1200LldpControlStatisticsClearGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,1,4,1,2))
_Me1200LldpControlStatisticsClearGlobalClear_Type=TruthValue
_Me1200LldpControlStatisticsClearGlobalClear_Object=MibScalar
me1200LldpControlStatisticsClearGlobalClear=_Me1200LldpControlStatisticsClearGlobalClear_Object((1,3,6,1,4,1,9,9,815,1,34,1,4,1,2,1),_Me1200LldpControlStatisticsClearGlobalClear_Type())
me1200LldpControlStatisticsClearGlobalClear.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200LldpControlStatisticsClearGlobalClear.setStatus(_A)
_Me1200LldpMibConformance_ObjectIdentity=ObjectIdentity
me1200LldpMibConformance=_Me1200LldpMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,3))
_Me1200LldpMibCompliances_ObjectIdentity=ObjectIdentity
me1200LldpMibCompliances=_Me1200LldpMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,3,1))
_Me1200LldpMibGroups_ObjectIdentity=ObjectIdentity
me1200LldpMibGroups=_Me1200LldpMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,34,3,2))
me1200LldpGlobalInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,1))
me1200LldpGlobalInfoGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:me1200LldpGlobalInfoGroup.setStatus(_A)
me1200LldpConfigurationInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,2))
me1200LldpConfigurationInfoGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:me1200LldpConfigurationInfoGroup.setStatus(_A)
me1200LldpStatisticsGlobalCountersInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,3))
me1200LldpStatisticsGlobalCountersInfoGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:me1200LldpStatisticsGlobalCountersInfoGroup.setStatus(_A)
me1200LldpStatisticsTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,4))
me1200LldpStatisticsTableInfoGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:me1200LldpStatisticsTableInfoGroup.setStatus(_A)
me1200LldpNeighborsInformationInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,5))
me1200LldpNeighborsInformationInfoGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:me1200LldpNeighborsInformationInfoGroup.setStatus(_A)
me1200LldpNeighborsManagementInformationInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,6))
me1200LldpNeighborsManagementInformationInfoGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:me1200LldpNeighborsManagementInformationInfoGroup.setStatus(_A)
me1200LldpControlStatisticsClearTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,7))
me1200LldpControlStatisticsClearTableInfoGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:me1200LldpControlStatisticsClearTableInfoGroup.setStatus(_A)
me1200LldpControlStatisticsClearGlobalInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,34,3,2,8))
me1200LldpControlStatisticsClearGlobalInfoGroup.setObjects((_B,_t))
if mibBuilder.loadTexts:me1200LldpControlStatisticsClearGlobalInfoGroup.setStatus(_A)
me1200LldpMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,34,3,1,1))
me1200LldpMibCompliance.setObjects(*((_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:me1200LldpMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200lldpAdminState':ME1200lldpAdminState,'me1200LldpMib':me1200LldpMib,'me1200LldpObjects':me1200LldpObjects,'me1200LldpConfig':me1200LldpConfig,'me1200LldpGlobal':me1200LldpGlobal,_Q:me1200LldpGlobalInitDelay,_R:me1200LldpGlobalMsgTxHold,_S:me1200LldpGlobalMsgTxInterval,_T:me1200LldpGlobalTxDelay,'me1200LldpConfigurationTable':me1200LldpConfigurationTable,'me1200LldpConfigurationEntry':me1200LldpConfigurationEntry,_I:me1200LldpConfigurationIfIndex,_U:me1200LldpConfigurationAdminState,_V:me1200LldpConfigurationCdpAware,_W:me1200LldpConfigurationOptionalTlvs,'me1200LldpStatus':me1200LldpStatus,'me1200LldpStatistics':me1200LldpStatistics,'me1200LldpStatisticsGlobalCounters':me1200LldpStatisticsGlobalCounters,_X:me1200LldpStatisticsGlobalCountersTableInserts,_Y:me1200LldpStatisticsGlobalCountersTableDeletes,_Z:me1200LldpStatisticsGlobalCountersTableDrops,_a:me1200LldpStatisticsGlobalCountersTableAgeOuts,_b:me1200LldpStatisticsGlobalCountersLastChangeTime,'me1200LldpStatisticsTable':me1200LldpStatisticsTable,'me1200LldpStatisticsEntry':me1200LldpStatisticsEntry,_J:me1200LldpStatisticsIfIndex,_c:me1200LldpStatisticsTxTotal,_d:me1200LldpStatisticsRxTotal,_e:me1200LldpStatisticsRxError,_f:me1200LldpStatisticsRxDiscarded,_g:me1200LldpStatisticsTLVsDiscarded,_h:me1200LldpStatisticsTLVsUnrecognized,_i:me1200LldpStatisticsTLVsOrgDiscarded,_j:me1200LldpStatisticsAgeOuts,'me1200LldpNeighborsInformationTable':me1200LldpNeighborsInformationTable,'me1200LldpNeighborsInformationEntry':me1200LldpNeighborsInformationEntry,_K:me1200LldpNeighborsInformationIfIndex,_L:me1200LldpNeighborsInformationLldpIndex,_k:me1200LldpNeighborsInformationChassisId,_l:me1200LldpNeighborsInformationPortId,_m:me1200LldpNeighborsInformationPortDescription,_n:me1200LldpNeighborsInformationSystemName,_o:me1200LldpNeighborsInformationSystemDescription,_p:me1200LldpNeighborsInformationSystemCapabilities,_q:me1200LldpNeighborsInformationSystemCapabilitiesEnable,'me1200LldpNeighborsManagementInformationTable':me1200LldpNeighborsManagementInformationTable,'me1200LldpNeighborsManagementInformationEntry':me1200LldpNeighborsManagementInformationEntry,_M:me1200LldpNeighborsManagementInformationIfIndex,_N:me1200LldpNeighborsManagementInformationLldpIndex,_O:me1200LldpNeighborsManagementInformationLldpManagement,_r:me1200LldpNeighborsManagementInformationSystemManagementAddress,'me1200LldpControl':me1200LldpControl,'me1200LldpStatisticsClear':me1200LldpStatisticsClear,'me1200LldpControlStatisticsClearTable':me1200LldpControlStatisticsClearTable,'me1200LldpControlStatisticsClearEntry':me1200LldpControlStatisticsClearEntry,_P:me1200LldpControlStatisticsClearIfIndex,_s:me1200LldpControlStatisticsClearStatisticsClear,'me1200LldpControlStatisticsClearGlobal':me1200LldpControlStatisticsClearGlobal,_t:me1200LldpControlStatisticsClearGlobalClear,'me1200LldpMibConformance':me1200LldpMibConformance,'me1200LldpMibCompliances':me1200LldpMibCompliances,'me1200LldpMibCompliance':me1200LldpMibCompliance,'me1200LldpMibGroups':me1200LldpMibGroups,_u:me1200LldpGlobalInfoGroup,_v:me1200LldpConfigurationInfoGroup,_w:me1200LldpStatisticsGlobalCountersInfoGroup,_x:me1200LldpStatisticsTableInfoGroup,_y:me1200LldpNeighborsInformationInfoGroup,_z:me1200LldpNeighborsManagementInformationInfoGroup,_A0:me1200LldpControlStatisticsClearTableInfoGroup,_A1:me1200LldpControlStatisticsClearGlobalInfoGroup})