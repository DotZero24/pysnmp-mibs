_AR='cpeExtPseInfoPwrGroup'
_AQ='cpeExtMainPseGroup'
_AP='cpeExtPolicingNotif'
_AO='cpeExtMainPseRemainingPower'
_AN='cpeExtMainPseUsedPower'
_AM='cpeExtPsePortLldpPdPwrPairsOrZero'
_AL='cpeExtPsePortLldpPdPwrSupport'
_AK='cpeExtPsePortLldpPdPwrClass'
_AJ='cpeExtPsePortLldpPwrClass'
_AI='cpeExtPsePortCapabilities'
_AH='cpeExtPsePortLldpPdPwrAlloc'
_AG='cpeExtPsePortLldpPwrAlloc'
_AF='cpeExtPsePortLldpPdPwrReq'
_AE='cpeExtPsePortLldpPwrReq'
_AD='cpeExtPsePortLldpPdPwrPriority'
_AC='cpeExtPsePortLldpPwrPriority'
_AB='cpeExtPsePortLldpPdPwrSrc'
_AA='cpeExtPsePortLldpPwrSrc'
_A9='cpeExtPsePortLldpPdPwrType'
_A8='cpeExtPsePortLldpPwrType'
_A7='cpeExtPowerPriorityEnable'
_A6='cpeExtPolicingNotifEnable'
_A5='cpeExtPsePortPwrManAlloc'
_A4='cpeExtPdStatsDeviceCount'
_A3='cpeExtPdStatsTotalDevices'
_A2='cpeExtPsePortPolicingEnable'
_A1='cpeExtPsePortPolicingCapable'
_A0='cpeExtPsePortEntPhyIndex'
_z='cpeExtDefaultAllocation'
_y='cpeExtPsePortPwrConsumption'
_x='cpeExtPsePortPwrAvailable'
_w='cpeExtPsePortPwrMax'
_v='cpeExtPsePortIeeePd'
_u='cpeExtPsePortDeviceDetected'
_t='cpeExtPsePortDiscoverMode'
_s='cpeExtPsePortEnable'
_r='cpeExtPsePortEntry'
_q='cpeExtPdStatsClass'
_p='miliwatts'
_o='class4'
_n='class3'
_m='class2'
_l='class1'
_k='class0'
_j='pethPsePortIndex'
_i='pethPsePortGroupIndex'
_h='pethMainPseGroupIndex'
_g='cpeExtPsePortLldpPowerGroup'
_f='cpeExtPsePortPolicingAction'
_e='cpeExtMainPsePwrMonitorCapable'
_d='cpeExtMainPseDescr'
_c='cpeExtMainPseEntPhyIndex'
_b='cpeExtPsePortMaxPwrDrawn'
_a='cpeExtPsePortPwrAllocated'
_Z='cpeExtPsePortAdditionalStatus'
_Y='cpeExtPsePortCapabilitiesGroup'
_X='cpeExtPsePortLldpGroup'
_W='cpeExtPowerPriorityGroup'
_V='Bits'
_U='POWER-ETHERNET-MIB'
_T='cpeExtPolicingNotifGroup'
_S='cpeExtPolicingNotifEnableGroup'
_R='cpeExtPortPwrManAllocGroup'
_Q='cpeExtPortPolicingActionGroup'
_P='cpeExtPdStatsGroup'
_O='cpeExtPortPolicingGroup'
_N='cpeExtPortEntityIndexGroup'
_M='cpeExtPseGrpPwrGroup'
_L='cpeExtMainPseGroup2'
_K='unknown'
_J='cpeExtPsePortPwrMonitorGroup'
_I='deprecated'
_H='cpeExtPsePortGlobalConfigGroup'
_G='cpeExtPsePortGroup'
_F='Integer32'
_E='read-write'
_D='milliwatts'
_C='read-only'
_B='current'
_A='CISCO-POWER-ETHERNET-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
EntPhysicalIndexOrZero,=mibBuilder.importSymbols('CISCO-TC','EntPhysicalIndexOrZero')
pethMainPseGroupIndex,pethPsePortEntry,pethPsePortGroupIndex,pethPsePortIndex=mibBuilder.importSymbols(_U,_h,'pethPsePortEntry',_i,_j)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_V,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
ciscoPowerEthernetExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,402))
if mibBuilder.loadTexts:ciscoPowerEthernetExtMIB.setRevisions(('2018-01-19 00:00','2013-07-10 00:00','2011-07-18 00:00','2009-12-04 00:00','2007-04-12 00:00','2007-02-02 00:00','2005-06-10 00:00','2004-04-12 00:00'))
class CpeExtLldpPwrType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('type1Pd',1),('type1Pse',2),('type2Pd',3),('type2Pse',4)))
class CpeExtLldpPwrSrc(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pseAndLocal',1),('local',2),('pse',3),('backupSrc',4),('primarySrc',5),(_K,6)))
class CpeExtPwrPriority(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3),(_K,4)))
class CpeExtLldpPwrClassOrZero(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_K,0),(_k,1),(_l,2),(_m,3),(_n,4),(_o,5)))
_CpeExtMIBNotifs_ObjectIdentity=ObjectIdentity
cpeExtMIBNotifs=_CpeExtMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,402,0))
_CpeExtMIBObjects_ObjectIdentity=ObjectIdentity
cpeExtMIBObjects=_CpeExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,402,1))
_CpeExtDefaultAllocation_Type=Unsigned32
_CpeExtDefaultAllocation_Object=MibScalar
cpeExtDefaultAllocation=_CpeExtDefaultAllocation_Object((1,3,6,1,4,1,9,9,402,1,1),_CpeExtDefaultAllocation_Type())
cpeExtDefaultAllocation.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtDefaultAllocation.setStatus(_B)
if mibBuilder.loadTexts:cpeExtDefaultAllocation.setUnits(_D)
_CpeExtPsePortTable_Object=MibTable
cpeExtPsePortTable=_CpeExtPsePortTable_Object((1,3,6,1,4,1,9,9,402,1,2))
if mibBuilder.loadTexts:cpeExtPsePortTable.setStatus(_B)
_CpeExtPsePortEntry_Object=MibTableRow
cpeExtPsePortEntry=_CpeExtPsePortEntry_Object((1,3,6,1,4,1,9,9,402,1,2,1))
if mibBuilder.loadTexts:cpeExtPsePortEntry.setStatus(_B)
class _CpeExtPsePortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('static',2),('limit',3),('disable',4)))
_CpeExtPsePortEnable_Type.__name__=_F
_CpeExtPsePortEnable_Object=MibTableColumn
cpeExtPsePortEnable=_CpeExtPsePortEnable_Object((1,3,6,1,4,1,9,9,402,1,2,1,1),_CpeExtPsePortEnable_Type())
cpeExtPsePortEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtPsePortEnable.setStatus(_B)
class _CpeExtPsePortDiscoverMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),('off',2),('ieee',3),('cisco',4),('ieeeAndCisco',5)))
_CpeExtPsePortDiscoverMode_Type.__name__=_F
_CpeExtPsePortDiscoverMode_Object=MibTableColumn
cpeExtPsePortDiscoverMode=_CpeExtPsePortDiscoverMode_Object((1,3,6,1,4,1,9,9,402,1,2,1,2),_CpeExtPsePortDiscoverMode_Type())
cpeExtPsePortDiscoverMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortDiscoverMode.setStatus(_B)
_CpeExtPsePortDeviceDetected_Type=TruthValue
_CpeExtPsePortDeviceDetected_Object=MibTableColumn
cpeExtPsePortDeviceDetected=_CpeExtPsePortDeviceDetected_Object((1,3,6,1,4,1,9,9,402,1,2,1,3),_CpeExtPsePortDeviceDetected_Type())
cpeExtPsePortDeviceDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortDeviceDetected.setStatus(_B)
_CpeExtPsePortIeeePd_Type=TruthValue
_CpeExtPsePortIeeePd_Object=MibTableColumn
cpeExtPsePortIeeePd=_CpeExtPsePortIeeePd_Object((1,3,6,1,4,1,9,9,402,1,2,1,4),_CpeExtPsePortIeeePd_Type())
cpeExtPsePortIeeePd.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortIeeePd.setStatus(_B)
class _CpeExtPsePortAdditionalStatus_Type(Bits):namedValues=NamedValues(*(('deny',0),('overdraw',1),('overdrawLog',2)))
_CpeExtPsePortAdditionalStatus_Type.__name__=_V
_CpeExtPsePortAdditionalStatus_Object=MibTableColumn
cpeExtPsePortAdditionalStatus=_CpeExtPsePortAdditionalStatus_Object((1,3,6,1,4,1,9,9,402,1,2,1,5),_CpeExtPsePortAdditionalStatus_Type())
cpeExtPsePortAdditionalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortAdditionalStatus.setStatus(_B)
_CpeExtPsePortPwrMax_Type=Unsigned32
_CpeExtPsePortPwrMax_Object=MibTableColumn
cpeExtPsePortPwrMax=_CpeExtPsePortPwrMax_Object((1,3,6,1,4,1,9,9,402,1,2,1,6),_CpeExtPsePortPwrMax_Type())
cpeExtPsePortPwrMax.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtPsePortPwrMax.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortPwrMax.setUnits(_D)
_CpeExtPsePortPwrAllocated_Type=Unsigned32
_CpeExtPsePortPwrAllocated_Object=MibTableColumn
cpeExtPsePortPwrAllocated=_CpeExtPsePortPwrAllocated_Object((1,3,6,1,4,1,9,9,402,1,2,1,7),_CpeExtPsePortPwrAllocated_Type())
cpeExtPsePortPwrAllocated.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortPwrAllocated.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortPwrAllocated.setUnits(_D)
_CpeExtPsePortPwrAvailable_Type=Unsigned32
_CpeExtPsePortPwrAvailable_Object=MibTableColumn
cpeExtPsePortPwrAvailable=_CpeExtPsePortPwrAvailable_Object((1,3,6,1,4,1,9,9,402,1,2,1,8),_CpeExtPsePortPwrAvailable_Type())
cpeExtPsePortPwrAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortPwrAvailable.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortPwrAvailable.setUnits(_D)
_CpeExtPsePortPwrConsumption_Type=Unsigned32
_CpeExtPsePortPwrConsumption_Object=MibTableColumn
cpeExtPsePortPwrConsumption=_CpeExtPsePortPwrConsumption_Object((1,3,6,1,4,1,9,9,402,1,2,1,9),_CpeExtPsePortPwrConsumption_Type())
cpeExtPsePortPwrConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortPwrConsumption.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortPwrConsumption.setUnits(_D)
_CpeExtPsePortMaxPwrDrawn_Type=Unsigned32
_CpeExtPsePortMaxPwrDrawn_Object=MibTableColumn
cpeExtPsePortMaxPwrDrawn=_CpeExtPsePortMaxPwrDrawn_Object((1,3,6,1,4,1,9,9,402,1,2,1,10),_CpeExtPsePortMaxPwrDrawn_Type())
cpeExtPsePortMaxPwrDrawn.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortMaxPwrDrawn.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortMaxPwrDrawn.setUnits(_D)
_CpeExtPsePortEntPhyIndex_Type=EntPhysicalIndexOrZero
_CpeExtPsePortEntPhyIndex_Object=MibTableColumn
cpeExtPsePortEntPhyIndex=_CpeExtPsePortEntPhyIndex_Object((1,3,6,1,4,1,9,9,402,1,2,1,11),_CpeExtPsePortEntPhyIndex_Type())
cpeExtPsePortEntPhyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortEntPhyIndex.setStatus(_B)
_CpeExtPsePortPolicingCapable_Type=TruthValue
_CpeExtPsePortPolicingCapable_Object=MibTableColumn
cpeExtPsePortPolicingCapable=_CpeExtPsePortPolicingCapable_Object((1,3,6,1,4,1,9,9,402,1,2,1,12),_CpeExtPsePortPolicingCapable_Type())
cpeExtPsePortPolicingCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortPolicingCapable.setStatus(_B)
class _CpeExtPsePortPolicingEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_CpeExtPsePortPolicingEnable_Type.__name__=_F
_CpeExtPsePortPolicingEnable_Object=MibTableColumn
cpeExtPsePortPolicingEnable=_CpeExtPsePortPolicingEnable_Object((1,3,6,1,4,1,9,9,402,1,2,1,13),_CpeExtPsePortPolicingEnable_Type())
cpeExtPsePortPolicingEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtPsePortPolicingEnable.setStatus(_B)
class _CpeExtPsePortPolicingAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('logOnly',2)))
_CpeExtPsePortPolicingAction_Type.__name__=_F
_CpeExtPsePortPolicingAction_Object=MibTableColumn
cpeExtPsePortPolicingAction=_CpeExtPsePortPolicingAction_Object((1,3,6,1,4,1,9,9,402,1,2,1,14),_CpeExtPsePortPolicingAction_Type())
cpeExtPsePortPolicingAction.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtPsePortPolicingAction.setStatus(_B)
_CpeExtPsePortPwrManAlloc_Type=Unsigned32
_CpeExtPsePortPwrManAlloc_Object=MibTableColumn
cpeExtPsePortPwrManAlloc=_CpeExtPsePortPwrManAlloc_Object((1,3,6,1,4,1,9,9,402,1,2,1,15),_CpeExtPsePortPwrManAlloc_Type())
cpeExtPsePortPwrManAlloc.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtPsePortPwrManAlloc.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortPwrManAlloc.setUnits(_D)
class _CpeExtPsePortCapabilities_Type(Bits):namedValues=NamedValues(*(('policing',0),('poePlus',1)))
_CpeExtPsePortCapabilities_Type.__name__=_V
_CpeExtPsePortCapabilities_Object=MibTableColumn
cpeExtPsePortCapabilities=_CpeExtPsePortCapabilities_Object((1,3,6,1,4,1,9,9,402,1,2,1,16),_CpeExtPsePortCapabilities_Type())
cpeExtPsePortCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortCapabilities.setStatus(_B)
_CpeExtMainPseTable_Object=MibTable
cpeExtMainPseTable=_CpeExtMainPseTable_Object((1,3,6,1,4,1,9,9,402,1,3))
if mibBuilder.loadTexts:cpeExtMainPseTable.setStatus(_B)
_CpeExtMainPseEntry_Object=MibTableRow
cpeExtMainPseEntry=_CpeExtMainPseEntry_Object((1,3,6,1,4,1,9,9,402,1,3,1))
cpeExtMainPseEntry.setIndexNames((0,_U,_h))
if mibBuilder.loadTexts:cpeExtMainPseEntry.setStatus(_B)
_CpeExtMainPseEntPhyIndex_Type=EntPhysicalIndexOrZero
_CpeExtMainPseEntPhyIndex_Object=MibTableColumn
cpeExtMainPseEntPhyIndex=_CpeExtMainPseEntPhyIndex_Object((1,3,6,1,4,1,9,9,402,1,3,1,1),_CpeExtMainPseEntPhyIndex_Type())
cpeExtMainPseEntPhyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtMainPseEntPhyIndex.setStatus(_B)
_CpeExtMainPseDescr_Type=SnmpAdminString
_CpeExtMainPseDescr_Object=MibTableColumn
cpeExtMainPseDescr=_CpeExtMainPseDescr_Object((1,3,6,1,4,1,9,9,402,1,3,1,2),_CpeExtMainPseDescr_Type())
cpeExtMainPseDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtMainPseDescr.setStatus(_B)
_CpeExtMainPsePwrMonitorCapable_Type=TruthValue
_CpeExtMainPsePwrMonitorCapable_Object=MibTableColumn
cpeExtMainPsePwrMonitorCapable=_CpeExtMainPsePwrMonitorCapable_Object((1,3,6,1,4,1,9,9,402,1,3,1,3),_CpeExtMainPsePwrMonitorCapable_Type())
cpeExtMainPsePwrMonitorCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtMainPsePwrMonitorCapable.setStatus(_B)
_CpeExtMainPseUsedPower_Type=Unsigned32
_CpeExtMainPseUsedPower_Object=MibTableColumn
cpeExtMainPseUsedPower=_CpeExtMainPseUsedPower_Object((1,3,6,1,4,1,9,9,402,1,3,1,4),_CpeExtMainPseUsedPower_Type())
cpeExtMainPseUsedPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtMainPseUsedPower.setStatus(_B)
if mibBuilder.loadTexts:cpeExtMainPseUsedPower.setUnits(_p)
_CpeExtMainPseRemainingPower_Type=Unsigned32
_CpeExtMainPseRemainingPower_Object=MibTableColumn
cpeExtMainPseRemainingPower=_CpeExtMainPseRemainingPower_Object((1,3,6,1,4,1,9,9,402,1,3,1,5),_CpeExtMainPseRemainingPower_Type())
cpeExtMainPseRemainingPower.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtMainPseRemainingPower.setStatus(_B)
if mibBuilder.loadTexts:cpeExtMainPseRemainingPower.setUnits(_p)
_CpeExtPdStatistics_ObjectIdentity=ObjectIdentity
cpeExtPdStatistics=_CpeExtPdStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,402,1,4))
_CpeExtPdStatsTotalDevices_Type=Unsigned32
_CpeExtPdStatsTotalDevices_Object=MibScalar
cpeExtPdStatsTotalDevices=_CpeExtPdStatsTotalDevices_Object((1,3,6,1,4,1,9,9,402,1,4,1),_CpeExtPdStatsTotalDevices_Type())
cpeExtPdStatsTotalDevices.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPdStatsTotalDevices.setStatus(_B)
_CpeExtPdStatsTable_Object=MibTable
cpeExtPdStatsTable=_CpeExtPdStatsTable_Object((1,3,6,1,4,1,9,9,402,1,4,2))
if mibBuilder.loadTexts:cpeExtPdStatsTable.setStatus(_B)
_CpeExtPdStatsEntry_Object=MibTableRow
cpeExtPdStatsEntry=_CpeExtPdStatsEntry_Object((1,3,6,1,4,1,9,9,402,1,4,2,1))
cpeExtPdStatsEntry.setIndexNames((0,_A,_q))
if mibBuilder.loadTexts:cpeExtPdStatsEntry.setStatus(_B)
class _CpeExtPdStatsClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cisco',1),(_k,2),(_l,3),(_m,4),(_n,5),(_o,6)))
_CpeExtPdStatsClass_Type.__name__=_F
_CpeExtPdStatsClass_Object=MibTableColumn
cpeExtPdStatsClass=_CpeExtPdStatsClass_Object((1,3,6,1,4,1,9,9,402,1,4,2,1,1),_CpeExtPdStatsClass_Type())
cpeExtPdStatsClass.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cpeExtPdStatsClass.setStatus(_B)
_CpeExtPdStatsDeviceCount_Type=Unsigned32
_CpeExtPdStatsDeviceCount_Object=MibTableColumn
cpeExtPdStatsDeviceCount=_CpeExtPdStatsDeviceCount_Object((1,3,6,1,4,1,9,9,402,1,4,2,1,2),_CpeExtPdStatsDeviceCount_Type())
cpeExtPdStatsDeviceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPdStatsDeviceCount.setStatus(_B)
_CpeExtPolicingNotifEnable_Type=TruthValue
_CpeExtPolicingNotifEnable_Object=MibScalar
cpeExtPolicingNotifEnable=_CpeExtPolicingNotifEnable_Object((1,3,6,1,4,1,9,9,402,1,5),_CpeExtPolicingNotifEnable_Type())
cpeExtPolicingNotifEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtPolicingNotifEnable.setStatus(_B)
_CpeExtPowerPriorityEnable_Type=TruthValue
_CpeExtPowerPriorityEnable_Object=MibScalar
cpeExtPowerPriorityEnable=_CpeExtPowerPriorityEnable_Object((1,3,6,1,4,1,9,9,402,1,6),_CpeExtPowerPriorityEnable_Type())
cpeExtPowerPriorityEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cpeExtPowerPriorityEnable.setStatus(_B)
_CpeExtPsePortLldpTable_Object=MibTable
cpeExtPsePortLldpTable=_CpeExtPsePortLldpTable_Object((1,3,6,1,4,1,9,9,402,1,7))
if mibBuilder.loadTexts:cpeExtPsePortLldpTable.setStatus(_B)
_CpeExtPsePortLldpEntry_Object=MibTableRow
cpeExtPsePortLldpEntry=_CpeExtPsePortLldpEntry_Object((1,3,6,1,4,1,9,9,402,1,7,1))
cpeExtPsePortLldpEntry.setIndexNames((0,_U,_i),(0,_U,_j))
if mibBuilder.loadTexts:cpeExtPsePortLldpEntry.setStatus(_B)
_CpeExtPsePortLldpPwrType_Type=CpeExtLldpPwrType
_CpeExtPsePortLldpPwrType_Object=MibTableColumn
cpeExtPsePortLldpPwrType=_CpeExtPsePortLldpPwrType_Object((1,3,6,1,4,1,9,9,402,1,7,1,1),_CpeExtPsePortLldpPwrType_Type())
cpeExtPsePortLldpPwrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrType.setStatus(_B)
_CpeExtPsePortLldpPdPwrType_Type=CpeExtLldpPwrType
_CpeExtPsePortLldpPdPwrType_Object=MibTableColumn
cpeExtPsePortLldpPdPwrType=_CpeExtPsePortLldpPdPwrType_Object((1,3,6,1,4,1,9,9,402,1,7,1,2),_CpeExtPsePortLldpPdPwrType_Type())
cpeExtPsePortLldpPdPwrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrType.setStatus(_B)
_CpeExtPsePortLldpPwrSrc_Type=CpeExtLldpPwrSrc
_CpeExtPsePortLldpPwrSrc_Object=MibTableColumn
cpeExtPsePortLldpPwrSrc=_CpeExtPsePortLldpPwrSrc_Object((1,3,6,1,4,1,9,9,402,1,7,1,3),_CpeExtPsePortLldpPwrSrc_Type())
cpeExtPsePortLldpPwrSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrSrc.setStatus(_B)
_CpeExtPsePortLldpPdPwrSrc_Type=CpeExtLldpPwrSrc
_CpeExtPsePortLldpPdPwrSrc_Object=MibTableColumn
cpeExtPsePortLldpPdPwrSrc=_CpeExtPsePortLldpPdPwrSrc_Object((1,3,6,1,4,1,9,9,402,1,7,1,4),_CpeExtPsePortLldpPdPwrSrc_Type())
cpeExtPsePortLldpPdPwrSrc.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrSrc.setStatus(_B)
_CpeExtPsePortLldpPwrPriority_Type=CpeExtPwrPriority
_CpeExtPsePortLldpPwrPriority_Object=MibTableColumn
cpeExtPsePortLldpPwrPriority=_CpeExtPsePortLldpPwrPriority_Object((1,3,6,1,4,1,9,9,402,1,7,1,5),_CpeExtPsePortLldpPwrPriority_Type())
cpeExtPsePortLldpPwrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrPriority.setStatus(_B)
_CpeExtPsePortLldpPdPwrPriority_Type=CpeExtPwrPriority
_CpeExtPsePortLldpPdPwrPriority_Object=MibTableColumn
cpeExtPsePortLldpPdPwrPriority=_CpeExtPsePortLldpPdPwrPriority_Object((1,3,6,1,4,1,9,9,402,1,7,1,6),_CpeExtPsePortLldpPdPwrPriority_Type())
cpeExtPsePortLldpPdPwrPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrPriority.setStatus(_B)
_CpeExtPsePortLldpPwrReq_Type=Unsigned32
_CpeExtPsePortLldpPwrReq_Object=MibTableColumn
cpeExtPsePortLldpPwrReq=_CpeExtPsePortLldpPwrReq_Object((1,3,6,1,4,1,9,9,402,1,7,1,7),_CpeExtPsePortLldpPwrReq_Type())
cpeExtPsePortLldpPwrReq.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrReq.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrReq.setUnits(_D)
_CpeExtPsePortLldpPdPwrReq_Type=Unsigned32
_CpeExtPsePortLldpPdPwrReq_Object=MibTableColumn
cpeExtPsePortLldpPdPwrReq=_CpeExtPsePortLldpPdPwrReq_Object((1,3,6,1,4,1,9,9,402,1,7,1,8),_CpeExtPsePortLldpPdPwrReq_Type())
cpeExtPsePortLldpPdPwrReq.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrReq.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrReq.setUnits(_D)
_CpeExtPsePortLldpPwrAlloc_Type=Unsigned32
_CpeExtPsePortLldpPwrAlloc_Object=MibTableColumn
cpeExtPsePortLldpPwrAlloc=_CpeExtPsePortLldpPwrAlloc_Object((1,3,6,1,4,1,9,9,402,1,7,1,9),_CpeExtPsePortLldpPwrAlloc_Type())
cpeExtPsePortLldpPwrAlloc.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrAlloc.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrAlloc.setUnits(_D)
_CpeExtPsePortLldpPdPwrAlloc_Type=Unsigned32
_CpeExtPsePortLldpPdPwrAlloc_Object=MibTableColumn
cpeExtPsePortLldpPdPwrAlloc=_CpeExtPsePortLldpPdPwrAlloc_Object((1,3,6,1,4,1,9,9,402,1,7,1,10),_CpeExtPsePortLldpPdPwrAlloc_Type())
cpeExtPsePortLldpPdPwrAlloc.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrAlloc.setStatus(_B)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrAlloc.setUnits(_D)
_CpeExtPsePortLldpPwrClass_Type=CpeExtLldpPwrClassOrZero
_CpeExtPsePortLldpPwrClass_Object=MibTableColumn
cpeExtPsePortLldpPwrClass=_CpeExtPsePortLldpPwrClass_Object((1,3,6,1,4,1,9,9,402,1,7,1,11),_CpeExtPsePortLldpPwrClass_Type())
cpeExtPsePortLldpPwrClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPwrClass.setStatus(_B)
_CpeExtPsePortLldpPdPwrClass_Type=CpeExtLldpPwrClassOrZero
_CpeExtPsePortLldpPdPwrClass_Object=MibTableColumn
cpeExtPsePortLldpPdPwrClass=_CpeExtPsePortLldpPdPwrClass_Object((1,3,6,1,4,1,9,9,402,1,7,1,12),_CpeExtPsePortLldpPdPwrClass_Type())
cpeExtPsePortLldpPdPwrClass.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrClass.setStatus(_B)
class _CpeExtPsePortLldpPdPwrSupport_Type(Bits):namedValues=NamedValues(*(('portClass',0),('pseMdiPwrSupport',1),('pseMdiPwrState',2),('psePairCtrlAbility',3)))
_CpeExtPsePortLldpPdPwrSupport_Type.__name__=_V
_CpeExtPsePortLldpPdPwrSupport_Object=MibTableColumn
cpeExtPsePortLldpPdPwrSupport=_CpeExtPsePortLldpPdPwrSupport_Object((1,3,6,1,4,1,9,9,402,1,7,1,13),_CpeExtPsePortLldpPdPwrSupport_Type())
cpeExtPsePortLldpPdPwrSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrSupport.setStatus(_B)
class _CpeExtPsePortLldpPdPwrPairsOrZero_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('signal',1),('spare',2)))
_CpeExtPsePortLldpPdPwrPairsOrZero_Type.__name__=_F
_CpeExtPsePortLldpPdPwrPairsOrZero_Object=MibTableColumn
cpeExtPsePortLldpPdPwrPairsOrZero=_CpeExtPsePortLldpPdPwrPairsOrZero_Object((1,3,6,1,4,1,9,9,402,1,7,1,14),_CpeExtPsePortLldpPdPwrPairsOrZero_Type())
cpeExtPsePortLldpPdPwrPairsOrZero.setMaxAccess(_C)
if mibBuilder.loadTexts:cpeExtPsePortLldpPdPwrPairsOrZero.setStatus(_B)
_CpeExtMIBConformance_ObjectIdentity=ObjectIdentity
cpeExtMIBConformance=_CpeExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,402,2))
_CpeExtMIBCompliances_ObjectIdentity=ObjectIdentity
cpeExtMIBCompliances=_CpeExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,402,2,1))
_CpeExtMIBGroups_ObjectIdentity=ObjectIdentity
cpeExtMIBGroups=_CpeExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,402,2,2))
pethPsePortEntry.registerAugmentions((_A,_r))
cpeExtPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
cpeExtPsePortGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,1))
cpeExtPsePortGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_Z),(_A,_w),(_A,_a),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:cpeExtPsePortGroup.setStatus(_B)
cpeExtPsePortGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,2))
cpeExtPsePortGlobalConfigGroup.setObjects((_A,_z))
if mibBuilder.loadTexts:cpeExtPsePortGlobalConfigGroup.setStatus(_B)
cpeExtPsePortPwrMonitorGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,3))
cpeExtPsePortPwrMonitorGroup.setObjects((_A,_b))
if mibBuilder.loadTexts:cpeExtPsePortPwrMonitorGroup.setStatus(_B)
cpeExtMainPseGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,4))
cpeExtMainPseGroup.setObjects(*((_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cpeExtMainPseGroup.setStatus(_I)
cpeExtPortEntityIndexGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,5))
cpeExtPortEntityIndexGroup.setObjects((_A,_A0))
if mibBuilder.loadTexts:cpeExtPortEntityIndexGroup.setStatus(_B)
cpeExtPortPolicingGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,6))
cpeExtPortPolicingGroup.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:cpeExtPortPolicingGroup.setStatus(_B)
cpeExtPdStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,7))
cpeExtPdStatsGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:cpeExtPdStatsGroup.setStatus(_B)
cpeExtMainPseGroup2=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,8))
cpeExtMainPseGroup2.setObjects(*((_A,_c),(_A,_d)))
if mibBuilder.loadTexts:cpeExtMainPseGroup2.setStatus(_B)
cpeExtPseGrpPwrGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,9))
cpeExtPseGrpPwrGroup.setObjects((_A,_e))
if mibBuilder.loadTexts:cpeExtPseGrpPwrGroup.setStatus(_B)
cpeExtPortPolicingActionGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,10))
cpeExtPortPolicingActionGroup.setObjects((_A,_f))
if mibBuilder.loadTexts:cpeExtPortPolicingActionGroup.setStatus(_B)
cpeExtPortPwrManAllocGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,11))
cpeExtPortPwrManAllocGroup.setObjects((_A,_A5))
if mibBuilder.loadTexts:cpeExtPortPwrManAllocGroup.setStatus(_B)
cpeExtPolicingNotifEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,12))
cpeExtPolicingNotifEnableGroup.setObjects((_A,_A6))
if mibBuilder.loadTexts:cpeExtPolicingNotifEnableGroup.setStatus(_B)
cpeExtPowerPriorityGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,14))
cpeExtPowerPriorityGroup.setObjects((_A,_A7))
if mibBuilder.loadTexts:cpeExtPowerPriorityGroup.setStatus(_B)
cpeExtPsePortLldpGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,15))
cpeExtPsePortLldpGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:cpeExtPsePortLldpGroup.setStatus(_B)
cpeExtPsePortCapabilitiesGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,16))
cpeExtPsePortCapabilitiesGroup.setObjects((_A,_AI))
if mibBuilder.loadTexts:cpeExtPsePortCapabilitiesGroup.setStatus(_B)
cpeExtPsePortLldpPowerGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,17))
cpeExtPsePortLldpPowerGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM)))
if mibBuilder.loadTexts:cpeExtPsePortLldpPowerGroup.setStatus(_B)
cpeExtPseInfoPwrGroup=ObjectGroup((1,3,6,1,4,1,9,9,402,2,2,18))
cpeExtPseInfoPwrGroup.setObjects(*((_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:cpeExtPseInfoPwrGroup.setStatus(_B)
cpeExtPolicingNotif=NotificationType((1,3,6,1,4,1,9,9,402,0,1))
cpeExtPolicingNotif.setObjects(*((_A,_f),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cpeExtPolicingNotif.setStatus(_B)
cpeExtPolicingNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,402,2,2,13))
cpeExtPolicingNotifGroup.setObjects((_A,_AP))
if mibBuilder.loadTexts:cpeExtPolicingNotifGroup.setStatus(_B)
cpeExtMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,402,2,1,1))
cpeExtMIBCompliance.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cpeExtMIBCompliance.setStatus(_I)
cpeExtMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,402,2,1,2))
cpeExtMIBCompliance2.setObjects(*((_A,_G),(_A,_H),(_A,_J),(_A,_AQ)))
if mibBuilder.loadTexts:cpeExtMIBCompliance2.setStatus(_I)
cpeExtMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,402,2,1,3))
cpeExtMIBCompliance3.setObjects(*((_A,_G),(_A,_H),(_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:cpeExtMIBCompliance3.setStatus(_I)
cpeExtMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,402,2,1,4))
cpeExtMIBCompliance4.setObjects(*((_A,_G),(_A,_H),(_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cpeExtMIBCompliance4.setStatus(_I)
cpeExtMIBCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,402,2,1,5))
cpeExtMIBCompliance5.setObjects(*((_A,_G),(_A,_H),(_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_W),(_A,_X),(_A,_Y),(_A,_g)))
if mibBuilder.loadTexts:cpeExtMIBCompliance5.setStatus(_I)
cpeExtMIBCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,402,2,1,6))
cpeExtMIBCompliance6.setObjects(*((_A,_G),(_A,_H),(_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_W),(_A,_X),(_A,_Y),(_A,_g),(_A,_AR)))
if mibBuilder.loadTexts:cpeExtMIBCompliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CpeExtLldpPwrType':CpeExtLldpPwrType,'CpeExtLldpPwrSrc':CpeExtLldpPwrSrc,'CpeExtPwrPriority':CpeExtPwrPriority,'CpeExtLldpPwrClassOrZero':CpeExtLldpPwrClassOrZero,'ciscoPowerEthernetExtMIB':ciscoPowerEthernetExtMIB,'cpeExtMIBNotifs':cpeExtMIBNotifs,_AP:cpeExtPolicingNotif,'cpeExtMIBObjects':cpeExtMIBObjects,_z:cpeExtDefaultAllocation,'cpeExtPsePortTable':cpeExtPsePortTable,_r:cpeExtPsePortEntry,_s:cpeExtPsePortEnable,_t:cpeExtPsePortDiscoverMode,_u:cpeExtPsePortDeviceDetected,_v:cpeExtPsePortIeeePd,_Z:cpeExtPsePortAdditionalStatus,_w:cpeExtPsePortPwrMax,_a:cpeExtPsePortPwrAllocated,_x:cpeExtPsePortPwrAvailable,_y:cpeExtPsePortPwrConsumption,_b:cpeExtPsePortMaxPwrDrawn,_A0:cpeExtPsePortEntPhyIndex,_A1:cpeExtPsePortPolicingCapable,_A2:cpeExtPsePortPolicingEnable,_f:cpeExtPsePortPolicingAction,_A5:cpeExtPsePortPwrManAlloc,_AI:cpeExtPsePortCapabilities,'cpeExtMainPseTable':cpeExtMainPseTable,'cpeExtMainPseEntry':cpeExtMainPseEntry,_c:cpeExtMainPseEntPhyIndex,_d:cpeExtMainPseDescr,_e:cpeExtMainPsePwrMonitorCapable,_AN:cpeExtMainPseUsedPower,_AO:cpeExtMainPseRemainingPower,'cpeExtPdStatistics':cpeExtPdStatistics,_A3:cpeExtPdStatsTotalDevices,'cpeExtPdStatsTable':cpeExtPdStatsTable,'cpeExtPdStatsEntry':cpeExtPdStatsEntry,_q:cpeExtPdStatsClass,_A4:cpeExtPdStatsDeviceCount,_A6:cpeExtPolicingNotifEnable,_A7:cpeExtPowerPriorityEnable,'cpeExtPsePortLldpTable':cpeExtPsePortLldpTable,'cpeExtPsePortLldpEntry':cpeExtPsePortLldpEntry,_A8:cpeExtPsePortLldpPwrType,_A9:cpeExtPsePortLldpPdPwrType,_AA:cpeExtPsePortLldpPwrSrc,_AB:cpeExtPsePortLldpPdPwrSrc,_AC:cpeExtPsePortLldpPwrPriority,_AD:cpeExtPsePortLldpPdPwrPriority,_AE:cpeExtPsePortLldpPwrReq,_AF:cpeExtPsePortLldpPdPwrReq,_AG:cpeExtPsePortLldpPwrAlloc,_AH:cpeExtPsePortLldpPdPwrAlloc,_AJ:cpeExtPsePortLldpPwrClass,_AK:cpeExtPsePortLldpPdPwrClass,_AL:cpeExtPsePortLldpPdPwrSupport,_AM:cpeExtPsePortLldpPdPwrPairsOrZero,'cpeExtMIBConformance':cpeExtMIBConformance,'cpeExtMIBCompliances':cpeExtMIBCompliances,'cpeExtMIBCompliance':cpeExtMIBCompliance,'cpeExtMIBCompliance2':cpeExtMIBCompliance2,'cpeExtMIBCompliance3':cpeExtMIBCompliance3,'cpeExtMIBCompliance4':cpeExtMIBCompliance4,'cpeExtMIBCompliance5':cpeExtMIBCompliance5,'cpeExtMIBCompliance6':cpeExtMIBCompliance6,'cpeExtMIBGroups':cpeExtMIBGroups,_G:cpeExtPsePortGroup,_H:cpeExtPsePortGlobalConfigGroup,_J:cpeExtPsePortPwrMonitorGroup,_AQ:cpeExtMainPseGroup,_N:cpeExtPortEntityIndexGroup,_O:cpeExtPortPolicingGroup,_P:cpeExtPdStatsGroup,_L:cpeExtMainPseGroup2,_M:cpeExtPseGrpPwrGroup,_Q:cpeExtPortPolicingActionGroup,_R:cpeExtPortPwrManAllocGroup,_S:cpeExtPolicingNotifEnableGroup,_T:cpeExtPolicingNotifGroup,_W:cpeExtPowerPriorityGroup,_X:cpeExtPsePortLldpGroup,_Y:cpeExtPsePortCapabilitiesGroup,_g:cpeExtPsePortLldpPowerGroup,_AR:cpeExtPseInfoPwrGroup})