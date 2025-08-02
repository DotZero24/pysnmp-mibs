_B2='atmOamF4PingStatus'
_B1='atmVpiAutoCreateComplete'
_B0='atmOamF5PingStatus'
_A_='atmVplOperStatusChange'
_Az='atmVclBandwidthUnavailable'
_Ay='atmInterfaceTCAlarmStateChange'
_Ax='atmDsx3PlcpAlarmStatusChange'
_Aw='atmVclOperStatusChange'
_Av='zhoneAtmVclExtOamF4PingStatus'
_Au='atmVclToMulticastMapRowStatus'
_At='atmVclToMulticastMapVci'
_As='atmVclToMulticastMapVpi'
_Ar='atmVclToMulticastMapIfIndex'
_Aq='atmVclToMulticastMapMulticastAddress'
_Ap='atmVclToMulticastMapRoutingDomain'
_Ao='atmVclToMulticastMapIndexNext'
_An='zhoneAtmVplPonTrafficContainerIndex'
_Am='zhoneAtmVclPonTrafficContainerIndex'
_Al='zhoneAtmVpiMaxVciPerVp'
_Ak='zhoneAtmVpiOamF4Ping'
_Aj='zhoneAtmVpiRowStatus'
_Ai='zhoneAtmVpiSwitched'
_Ah='zhoneAtmVpiMaxVci'
_Ag='zhoneAtmConnectionsAllocated'
_Af='zhoneAtmConnectionsAvailable'
_Ae='zhoneAtmVplExtTrafficContainerIndex'
_Ad='zhoneAtmVplExtFaultDetectionType'
_Ac='zhoneAtmVclRateExtParam16Grp2'
_Ab='zhoneAtmVclRateExtParam15Grp2'
_Aa='zhoneAtmVclRateExtParam14Grp2'
_AZ='zhoneAtmVclRateExtParam13Grp2'
_AY='zhoneAtmVclRateExtParam12Grp2'
_AX='zhoneAtmVclRateExtParam11Grp2'
_AW='zhoneAtmVclRateExtParam10Grp2'
_AV='zhoneAtmVclRateExtParam9Grp2'
_AU='zhoneAtmVclRateExtParam8Grp2'
_AT='zhoneAtmVclRateExtParam7Grp2'
_AS='zhoneAtmVclRateExtParam6Grp2'
_AR='zhoneAtmVclRateExtParam5Grp2'
_AQ='zhoneAtmVclRateExtParam4Grp2'
_AP='zhoneAtmVclRateExtParam3Grp2'
_AO='zhoneAtmVclRateExtParam2Grp2'
_AN='zhoneAtmVclRateExtParam1Grp2'
_AM='zhoneAtmVclRateExtParam16'
_AL='zhoneAtmVclRateExtParam15'
_AK='zhoneAtmVclRateExtParam14'
_AJ='zhoneAtmVclRateExtParam13'
_AI='zhoneAtmVclRateExtParam12'
_AH='zhoneAtmVclRateExtParam11'
_AG='zhoneAtmVclRateExtParam10'
_AF='zhoneAtmVclRateExtParam9'
_AE='zhoneAtmVclRateExtParam8'
_AD='zhoneAtmVclRateExtParam7'
_AC='zhoneAtmVclRateExtParam6'
_AB='zhoneAtmVclRateExtParam5'
_AA='zhoneAtmVclRateExtParam4'
_A9='zhoneAtmVclRateExtParam3'
_A8='zhoneAtmVclRateExtParam2'
_A7='zhoneAtmVclRateExtParam1'
_A6='zhoneAtmStatsTotalInitialCellsTx'
_A5='zhoneAtmStatsTotalFinalCLP1CellsTx'
_A4='zhoneAtmStatsTotalFinalCLP0CellsTx'
_A3='zhoneAtmStatsTotalFabricCellsTx'
_A2='zhoneAtmStatsTotalFinalCLP1CellsRx'
_A1='zhoneAtmStatsTotalFinalCLP0CellsRx'
_A0='zhoneAtmStatsTotalFabricCellsRx'
_z='zhoneAtmStatsTotalInitialCellsRx'
_y='zhoneAtmTrafficDescrParamExtUsageParameterControl'
_x='zhoneAtmTrafficDescrParamExtCacDivider'
_w='zhoneAtmTrafficDescrParamExtTrnkVclRate'
_v='zhoneAtmVclExtTrafficContainerIndex'
_u='zhoneAtmVclExtOamF5Ping'
_t='zhoneAtmVclExtFaultDetectionType'
_s='zhoneAtmVcCrossConnectExtEntry'
_r='zhoneAtmInterfaceTcExtEntry'
_q='zhoneAtmVplPonExtEntry'
_p='zhoneAtmPonExtEntry'
_o='zhoneAtmVplExtEntry'
_n='zhoneAtmStatsExtEntry'
_m='zhoneAtmTrafficDescrParamExtEntry'
_l='zhoneAtmVclExtEntry'
_k='atmVclToMulticastMapIndex'
_j='zhoneSlotIndex'
_i='zhoneShelfIndex'
_h='TruthValue'
_g='atmVplVpi'
_f='atmVplOperStatus'
_e='atmVplLastChange'
_d='atmVplAdminStatus'
_c='atmVclTransmitTrafficDescrIndex'
_b='atmVclReceiveTrafficDescrIndex'
_a='atmVclOperStatus'
_Z='atmVclLastChange'
_Y='atmVclAdminStatus'
_X='atmInterfaceTCAlarmState'
_W='atmInterfaceDs3PlcpAlarmState'
_V='OctetString'
_U='zhoneAtmVpiOamF4PingStatus'
_T='atmVpiAutoCreateCount'
_S='atmVpiAutoCreateDone'
_R='zhoneAtmVclExtOamF5PingStatus'
_Q='segment'
_P='endToEnd'
_O='Zhone'
_N='atmVci'
_M='atmVpi'
_L='disabled'
_K='ifIndex'
_J='IF-MIB'
_I='deprecated'
_H='accessible-for-notify'
_G='ATM-MIB'
_F='read-only'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='ZHONE-COM-ATM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_V,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmInterfaceDs3PlcpAlarmState,atmInterfaceTCAlarmState,atmInterfaceTCEntry,atmTrafficDescrParamEntry,atmVcCrossConnectEntry,atmVccAal5CpcsReceiveSduSize,atmVccAal5CpcsTransmitSduSize,atmVccAal5EncapsType,atmVccAalType,atmVclAdminStatus,atmVclCastType,atmVclConnKind,atmVclCrossConnectIdentifier,atmVclEntry,atmVclLastChange,atmVclOperStatus,atmVclReceiveTrafficDescrIndex,atmVclRowStatus,atmVclTransmitTrafficDescrIndex,atmVclVci,atmVclVpi,atmVplAdminStatus,atmVplCastType,atmVplConnKind,atmVplCrossConnectIdentifier,atmVplEntry,atmVplLastChange,atmVplOperStatus,atmVplReceiveTrafficDescrIndex,atmVplRowStatus,atmVplTransmitTrafficDescrIndex,atmVplVpi=mibBuilder.importSymbols(_G,_W,_X,'atmInterfaceTCEntry','atmTrafficDescrParamEntry','atmVcCrossConnectEntry','atmVccAal5CpcsReceiveSduSize','atmVccAal5CpcsTransmitSduSize','atmVccAal5EncapsType','atmVccAalType',_Y,'atmVclCastType','atmVclConnKind','atmVclCrossConnectIdentifier','atmVclEntry',_Z,_a,_b,'atmVclRowStatus',_c,'atmVclVci','atmVclVpi',_d,'atmVplCastType','atmVplConnKind','atmVplCrossConnectIdentifier','atmVplEntry',_e,_f,'atmVplReceiveTrafficDescrIndex','atmVplRowStatus','atmVplTransmitTrafficDescrIndex',_g)
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_J,'InterfaceIndex',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_h)
zhoneAtm,zhoneModules,zhoneShelfIndex,zhoneSlotIndex=mibBuilder.importSymbols(_O,'zhoneAtm','zhoneModules',_i,_j)
ZhoneAdminString,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString','ZhoneRowStatus')
comAtmExtension=ModuleIdentity((1,3,6,1,4,1,5504,6,25))
if mibBuilder.loadTexts:comAtmExtension.setRevisions(('2005-04-05 16:44','2005-02-28 13:18','2004-09-07 10:44','2004-06-19 10:15','2004-01-28 12:42','2003-12-04 15:23','2003-09-09 14:11','2003-04-16 16:04','2003-03-11 13:46','2003-02-14 16:55','2003-02-11 13:30','2002-08-23 10:36','2002-08-13 16:14','2002-06-04 20:13','2002-05-28 12:12','2002-05-21 17:29','2002-05-15 17:29','2002-03-20 20:19','2001-12-19 15:24','2001-11-02 17:22','2001-10-29 17:34','2001-09-20 10:54','2001-08-30 17:15','2001-08-14 12:00','2001-07-11 12:00'))
_ZhoneAtmExtension_ObjectIdentity=ObjectIdentity
zhoneAtmExtension=_ZhoneAtmExtension_ObjectIdentity((1,3,6,1,4,1,5504,4,2,2))
if mibBuilder.loadTexts:zhoneAtmExtension.setStatus(_A)
_ZhoneAtmVclExtTable_Object=MibTable
zhoneAtmVclExtTable=_ZhoneAtmVclExtTable_Object((1,3,6,1,4,1,5504,4,2,2,1))
if mibBuilder.loadTexts:zhoneAtmVclExtTable.setStatus(_A)
_ZhoneAtmVclExtEntry_Object=MibTableRow
zhoneAtmVclExtEntry=_ZhoneAtmVclExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,1,1))
if mibBuilder.loadTexts:zhoneAtmVclExtEntry.setStatus(_A)
class _ZhoneAtmVclExtFaultDetectionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('oamF5Loopback',2)))
_ZhoneAtmVclExtFaultDetectionType_Type.__name__=_C
_ZhoneAtmVclExtFaultDetectionType_Object=MibTableColumn
zhoneAtmVclExtFaultDetectionType=_ZhoneAtmVclExtFaultDetectionType_Object((1,3,6,1,4,1,5504,4,2,2,1,1,1),_ZhoneAtmVclExtFaultDetectionType_Type())
zhoneAtmVclExtFaultDetectionType.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVclExtFaultDetectionType.setStatus(_A)
class _ZhoneAtmVclExtOamF5Ping_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_P,2),(_Q,3)))
_ZhoneAtmVclExtOamF5Ping_Type.__name__=_C
_ZhoneAtmVclExtOamF5Ping_Object=MibTableColumn
zhoneAtmVclExtOamF5Ping=_ZhoneAtmVclExtOamF5Ping_Object((1,3,6,1,4,1,5504,4,2,2,1,1,2),_ZhoneAtmVclExtOamF5Ping_Type())
zhoneAtmVclExtOamF5Ping.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVclExtOamF5Ping.setStatus(_A)
_ZhoneAtmVclExtOamF5PingStatus_Type=TruthValue
_ZhoneAtmVclExtOamF5PingStatus_Object=MibTableColumn
zhoneAtmVclExtOamF5PingStatus=_ZhoneAtmVclExtOamF5PingStatus_Object((1,3,6,1,4,1,5504,4,2,2,1,1,3),_ZhoneAtmVclExtOamF5PingStatus_Type())
zhoneAtmVclExtOamF5PingStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zhoneAtmVclExtOamF5PingStatus.setStatus(_A)
class _ZhoneAtmVclExtTrafficContainerIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneAtmVclExtTrafficContainerIndex_Type.__name__=_C
_ZhoneAtmVclExtTrafficContainerIndex_Object=MibTableColumn
zhoneAtmVclExtTrafficContainerIndex=_ZhoneAtmVclExtTrafficContainerIndex_Object((1,3,6,1,4,1,5504,4,2,2,1,1,4),_ZhoneAtmVclExtTrafficContainerIndex_Type())
zhoneAtmVclExtTrafficContainerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVclExtTrafficContainerIndex.setStatus(_A)
class _ZhoneAtmVclExtOamF4Ping_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_P,2),(_Q,3)))
_ZhoneAtmVclExtOamF4Ping_Type.__name__=_C
_ZhoneAtmVclExtOamF4Ping_Object=MibTableColumn
zhoneAtmVclExtOamF4Ping=_ZhoneAtmVclExtOamF4Ping_Object((1,3,6,1,4,1,5504,4,2,2,1,1,5),_ZhoneAtmVclExtOamF4Ping_Type())
zhoneAtmVclExtOamF4Ping.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVclExtOamF4Ping.setStatus(_A)
_ZhoneAtmVclExtOamF4PingStatus_Type=TruthValue
_ZhoneAtmVclExtOamF4PingStatus_Object=MibTableColumn
zhoneAtmVclExtOamF4PingStatus=_ZhoneAtmVclExtOamF4PingStatus_Object((1,3,6,1,4,1,5504,4,2,2,1,1,6),_ZhoneAtmVclExtOamF4PingStatus_Type())
zhoneAtmVclExtOamF4PingStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zhoneAtmVclExtOamF4PingStatus.setStatus(_A)
_ZhoneAtmTraps_ObjectIdentity=ObjectIdentity
zhoneAtmTraps=_ZhoneAtmTraps_ObjectIdentity((1,3,6,1,4,1,5504,4,2,2,2))
if mibBuilder.loadTexts:zhoneAtmTraps.setStatus(_A)
_ZhoneAtmV2Traps_ObjectIdentity=ObjectIdentity
zhoneAtmV2Traps=_ZhoneAtmV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,4,2,2,2,0))
if mibBuilder.loadTexts:zhoneAtmV2Traps.setStatus(_A)
_ZhoneAtmGroups_ObjectIdentity=ObjectIdentity
zhoneAtmGroups=_ZhoneAtmGroups_ObjectIdentity((1,3,6,1,4,1,5504,4,2,2,3))
if mibBuilder.loadTexts:zhoneAtmGroups.setStatus(_A)
_ZhoneAtmTrafficDescrParamExtTable_Object=MibTable
zhoneAtmTrafficDescrParamExtTable=_ZhoneAtmTrafficDescrParamExtTable_Object((1,3,6,1,4,1,5504,4,2,2,4))
if mibBuilder.loadTexts:zhoneAtmTrafficDescrParamExtTable.setStatus(_A)
_ZhoneAtmTrafficDescrParamExtEntry_Object=MibTableRow
zhoneAtmTrafficDescrParamExtEntry=_ZhoneAtmTrafficDescrParamExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,4,1))
if mibBuilder.loadTexts:zhoneAtmTrafficDescrParamExtEntry.setStatus(_A)
class _ZhoneAtmTrafficDescrParamExtTrnkVclRate_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('unused',1),('rate16K',2),('rate32K',3),('rate64K',4),('rate80K',5),('rate128K',6),('rate160K',7),('rate256K',8),('rate320K',9),('rate512K',10),('rate640K',11),('rate1552K',12),('rate2050K',13),('rate12M',14),('rate16M',15),('rate45M',16),('rate155M',17),('rate960K',18),('rate1280K',19),('rate1760K',20),('rate3M',21),('rate4M',22),('rate5M',23),('rate6M',24),('rate7M',25),('rate8M',26),('rate10M',27),('rate14M',28),('rate24M',29),('rate32M',30),('rate64M',31),('rate96M',32),('rate128M',33)))
_ZhoneAtmTrafficDescrParamExtTrnkVclRate_Type.__name__=_C
_ZhoneAtmTrafficDescrParamExtTrnkVclRate_Object=MibTableColumn
zhoneAtmTrafficDescrParamExtTrnkVclRate=_ZhoneAtmTrafficDescrParamExtTrnkVclRate_Object((1,3,6,1,4,1,5504,4,2,2,4,1,1),_ZhoneAtmTrafficDescrParamExtTrnkVclRate_Type())
zhoneAtmTrafficDescrParamExtTrnkVclRate.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmTrafficDescrParamExtTrnkVclRate.setStatus(_A)
class _ZhoneAtmTrafficDescrParamExtCacDivider_Type(Integer32):defaultValue=1
_ZhoneAtmTrafficDescrParamExtCacDivider_Type.__name__=_C
_ZhoneAtmTrafficDescrParamExtCacDivider_Object=MibTableColumn
zhoneAtmTrafficDescrParamExtCacDivider=_ZhoneAtmTrafficDescrParamExtCacDivider_Object((1,3,6,1,4,1,5504,4,2,2,4,1,2),_ZhoneAtmTrafficDescrParamExtCacDivider_Type())
zhoneAtmTrafficDescrParamExtCacDivider.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmTrafficDescrParamExtCacDivider.setStatus(_A)
class _ZhoneAtmTrafficDescrParamExtUsageParameterControl_Type(TruthValue):defaultValue=1
_ZhoneAtmTrafficDescrParamExtUsageParameterControl_Type.__name__=_h
_ZhoneAtmTrafficDescrParamExtUsageParameterControl_Object=MibTableColumn
zhoneAtmTrafficDescrParamExtUsageParameterControl=_ZhoneAtmTrafficDescrParamExtUsageParameterControl_Object((1,3,6,1,4,1,5504,4,2,2,4,1,3),_ZhoneAtmTrafficDescrParamExtUsageParameterControl_Type())
zhoneAtmTrafficDescrParamExtUsageParameterControl.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmTrafficDescrParamExtUsageParameterControl.setStatus(_A)
_ZhoneAtmStatsExtTable_Object=MibTable
zhoneAtmStatsExtTable=_ZhoneAtmStatsExtTable_Object((1,3,6,1,4,1,5504,4,2,2,5))
if mibBuilder.loadTexts:zhoneAtmStatsExtTable.setStatus(_A)
_ZhoneAtmStatsExtEntry_Object=MibTableRow
zhoneAtmStatsExtEntry=_ZhoneAtmStatsExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,5,1))
if mibBuilder.loadTexts:zhoneAtmStatsExtEntry.setStatus(_A)
_ZhoneAtmStatsTotalInitialCellsRx_Type=Counter64
_ZhoneAtmStatsTotalInitialCellsRx_Object=MibTableColumn
zhoneAtmStatsTotalInitialCellsRx=_ZhoneAtmStatsTotalInitialCellsRx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,1),_ZhoneAtmStatsTotalInitialCellsRx_Type())
zhoneAtmStatsTotalInitialCellsRx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalInitialCellsRx.setStatus(_A)
_ZhoneAtmStatsTotalFabricCellsRx_Type=Counter64
_ZhoneAtmStatsTotalFabricCellsRx_Object=MibTableColumn
zhoneAtmStatsTotalFabricCellsRx=_ZhoneAtmStatsTotalFabricCellsRx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,2),_ZhoneAtmStatsTotalFabricCellsRx_Type())
zhoneAtmStatsTotalFabricCellsRx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalFabricCellsRx.setStatus(_A)
_ZhoneAtmStatsTotalFinalCLP0CellsRx_Type=Counter64
_ZhoneAtmStatsTotalFinalCLP0CellsRx_Object=MibTableColumn
zhoneAtmStatsTotalFinalCLP0CellsRx=_ZhoneAtmStatsTotalFinalCLP0CellsRx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,3),_ZhoneAtmStatsTotalFinalCLP0CellsRx_Type())
zhoneAtmStatsTotalFinalCLP0CellsRx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalFinalCLP0CellsRx.setStatus(_A)
_ZhoneAtmStatsTotalFinalCLP1CellsRx_Type=Counter64
_ZhoneAtmStatsTotalFinalCLP1CellsRx_Object=MibTableColumn
zhoneAtmStatsTotalFinalCLP1CellsRx=_ZhoneAtmStatsTotalFinalCLP1CellsRx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,4),_ZhoneAtmStatsTotalFinalCLP1CellsRx_Type())
zhoneAtmStatsTotalFinalCLP1CellsRx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalFinalCLP1CellsRx.setStatus(_A)
_ZhoneAtmStatsTotalInitialCellsTx_Type=Counter64
_ZhoneAtmStatsTotalInitialCellsTx_Object=MibTableColumn
zhoneAtmStatsTotalInitialCellsTx=_ZhoneAtmStatsTotalInitialCellsTx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,5),_ZhoneAtmStatsTotalInitialCellsTx_Type())
zhoneAtmStatsTotalInitialCellsTx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalInitialCellsTx.setStatus(_A)
_ZhoneAtmStatsTotalFabricCellsTx_Type=Counter64
_ZhoneAtmStatsTotalFabricCellsTx_Object=MibTableColumn
zhoneAtmStatsTotalFabricCellsTx=_ZhoneAtmStatsTotalFabricCellsTx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,6),_ZhoneAtmStatsTotalFabricCellsTx_Type())
zhoneAtmStatsTotalFabricCellsTx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalFabricCellsTx.setStatus(_A)
_ZhoneAtmStatsTotalFinalCLP0CellsTx_Type=Counter64
_ZhoneAtmStatsTotalFinalCLP0CellsTx_Object=MibTableColumn
zhoneAtmStatsTotalFinalCLP0CellsTx=_ZhoneAtmStatsTotalFinalCLP0CellsTx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,7),_ZhoneAtmStatsTotalFinalCLP0CellsTx_Type())
zhoneAtmStatsTotalFinalCLP0CellsTx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalFinalCLP0CellsTx.setStatus(_A)
_ZhoneAtmStatsTotalFinalCLP1CellsTx_Type=Counter64
_ZhoneAtmStatsTotalFinalCLP1CellsTx_Object=MibTableColumn
zhoneAtmStatsTotalFinalCLP1CellsTx=_ZhoneAtmStatsTotalFinalCLP1CellsTx_Object((1,3,6,1,4,1,5504,4,2,2,5,1,8),_ZhoneAtmStatsTotalFinalCLP1CellsTx_Type())
zhoneAtmStatsTotalFinalCLP1CellsTx.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmStatsTotalFinalCLP1CellsTx.setStatus(_A)
_ZhoneAtmVclRateExtParam_ObjectIdentity=ObjectIdentity
zhoneAtmVclRateExtParam=_ZhoneAtmVclRateExtParam_ObjectIdentity((1,3,6,1,4,1,5504,4,2,2,6))
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam.setStatus(_A)
class _ZhoneAtmVclRateExtParam1_Type(Integer32):defaultValue=38
_ZhoneAtmVclRateExtParam1_Type.__name__=_C
_ZhoneAtmVclRateExtParam1_Object=MibScalar
zhoneAtmVclRateExtParam1=_ZhoneAtmVclRateExtParam1_Object((1,3,6,1,4,1,5504,4,2,2,6,1),_ZhoneAtmVclRateExtParam1_Type())
zhoneAtmVclRateExtParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam1.setStatus(_A)
class _ZhoneAtmVclRateExtParam2_Type(Integer32):defaultValue=76
_ZhoneAtmVclRateExtParam2_Type.__name__=_C
_ZhoneAtmVclRateExtParam2_Object=MibScalar
zhoneAtmVclRateExtParam2=_ZhoneAtmVclRateExtParam2_Object((1,3,6,1,4,1,5504,4,2,2,6,2),_ZhoneAtmVclRateExtParam2_Type())
zhoneAtmVclRateExtParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam2.setStatus(_A)
class _ZhoneAtmVclRateExtParam3_Type(Integer32):defaultValue=151
_ZhoneAtmVclRateExtParam3_Type.__name__=_C
_ZhoneAtmVclRateExtParam3_Object=MibScalar
zhoneAtmVclRateExtParam3=_ZhoneAtmVclRateExtParam3_Object((1,3,6,1,4,1,5504,4,2,2,6,3),_ZhoneAtmVclRateExtParam3_Type())
zhoneAtmVclRateExtParam3.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam3.setStatus(_A)
class _ZhoneAtmVclRateExtParam4_Type(Integer32):defaultValue=189
_ZhoneAtmVclRateExtParam4_Type.__name__=_C
_ZhoneAtmVclRateExtParam4_Object=MibScalar
zhoneAtmVclRateExtParam4=_ZhoneAtmVclRateExtParam4_Object((1,3,6,1,4,1,5504,4,2,2,6,4),_ZhoneAtmVclRateExtParam4_Type())
zhoneAtmVclRateExtParam4.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam4.setStatus(_A)
class _ZhoneAtmVclRateExtParam5_Type(Integer32):defaultValue=302
_ZhoneAtmVclRateExtParam5_Type.__name__=_C
_ZhoneAtmVclRateExtParam5_Object=MibScalar
zhoneAtmVclRateExtParam5=_ZhoneAtmVclRateExtParam5_Object((1,3,6,1,4,1,5504,4,2,2,6,5),_ZhoneAtmVclRateExtParam5_Type())
zhoneAtmVclRateExtParam5.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam5.setStatus(_A)
class _ZhoneAtmVclRateExtParam6_Type(Integer32):defaultValue=378
_ZhoneAtmVclRateExtParam6_Type.__name__=_C
_ZhoneAtmVclRateExtParam6_Object=MibScalar
zhoneAtmVclRateExtParam6=_ZhoneAtmVclRateExtParam6_Object((1,3,6,1,4,1,5504,4,2,2,6,6),_ZhoneAtmVclRateExtParam6_Type())
zhoneAtmVclRateExtParam6.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam6.setStatus(_A)
class _ZhoneAtmVclRateExtParam7_Type(Integer32):defaultValue=604
_ZhoneAtmVclRateExtParam7_Type.__name__=_C
_ZhoneAtmVclRateExtParam7_Object=MibScalar
zhoneAtmVclRateExtParam7=_ZhoneAtmVclRateExtParam7_Object((1,3,6,1,4,1,5504,4,2,2,6,7),_ZhoneAtmVclRateExtParam7_Type())
zhoneAtmVclRateExtParam7.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam7.setStatus(_A)
class _ZhoneAtmVclRateExtParam8_Type(Integer32):defaultValue=755
_ZhoneAtmVclRateExtParam8_Type.__name__=_C
_ZhoneAtmVclRateExtParam8_Object=MibScalar
zhoneAtmVclRateExtParam8=_ZhoneAtmVclRateExtParam8_Object((1,3,6,1,4,1,5504,4,2,2,6,8),_ZhoneAtmVclRateExtParam8_Type())
zhoneAtmVclRateExtParam8.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam8.setStatus(_A)
class _ZhoneAtmVclRateExtParam9_Type(Integer32):defaultValue=1208
_ZhoneAtmVclRateExtParam9_Type.__name__=_C
_ZhoneAtmVclRateExtParam9_Object=MibScalar
zhoneAtmVclRateExtParam9=_ZhoneAtmVclRateExtParam9_Object((1,3,6,1,4,1,5504,4,2,2,6,9),_ZhoneAtmVclRateExtParam9_Type())
zhoneAtmVclRateExtParam9.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam9.setStatus(_A)
class _ZhoneAtmVclRateExtParam10_Type(Integer32):defaultValue=1510
_ZhoneAtmVclRateExtParam10_Type.__name__=_C
_ZhoneAtmVclRateExtParam10_Object=MibScalar
zhoneAtmVclRateExtParam10=_ZhoneAtmVclRateExtParam10_Object((1,3,6,1,4,1,5504,4,2,2,6,10),_ZhoneAtmVclRateExtParam10_Type())
zhoneAtmVclRateExtParam10.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam10.setStatus(_A)
class _ZhoneAtmVclRateExtParam11_Type(Integer32):defaultValue=3661
_ZhoneAtmVclRateExtParam11_Type.__name__=_C
_ZhoneAtmVclRateExtParam11_Object=MibScalar
zhoneAtmVclRateExtParam11=_ZhoneAtmVclRateExtParam11_Object((1,3,6,1,4,1,5504,4,2,2,6,11),_ZhoneAtmVclRateExtParam11_Type())
zhoneAtmVclRateExtParam11.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam11.setStatus(_A)
class _ZhoneAtmVclRateExtParam12_Type(Integer32):defaultValue=4825
_ZhoneAtmVclRateExtParam12_Type.__name__=_C
_ZhoneAtmVclRateExtParam12_Object=MibScalar
zhoneAtmVclRateExtParam12=_ZhoneAtmVclRateExtParam12_Object((1,3,6,1,4,1,5504,4,2,2,6,12),_ZhoneAtmVclRateExtParam12_Type())
zhoneAtmVclRateExtParam12.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam12.setStatus(_A)
class _ZhoneAtmVclRateExtParam13_Type(Integer32):defaultValue=28302
_ZhoneAtmVclRateExtParam13_Type.__name__=_C
_ZhoneAtmVclRateExtParam13_Object=MibScalar
zhoneAtmVclRateExtParam13=_ZhoneAtmVclRateExtParam13_Object((1,3,6,1,4,1,5504,4,2,2,6,13),_ZhoneAtmVclRateExtParam13_Type())
zhoneAtmVclRateExtParam13.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam13.setStatus(_A)
class _ZhoneAtmVclRateExtParam14_Type(Integer32):defaultValue=37736
_ZhoneAtmVclRateExtParam14_Type.__name__=_C
_ZhoneAtmVclRateExtParam14_Object=MibScalar
zhoneAtmVclRateExtParam14=_ZhoneAtmVclRateExtParam14_Object((1,3,6,1,4,1,5504,4,2,2,6,14),_ZhoneAtmVclRateExtParam14_Type())
zhoneAtmVclRateExtParam14.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam14.setStatus(_A)
class _ZhoneAtmVclRateExtParam15_Type(Integer32):defaultValue=106133
_ZhoneAtmVclRateExtParam15_Type.__name__=_C
_ZhoneAtmVclRateExtParam15_Object=MibScalar
zhoneAtmVclRateExtParam15=_ZhoneAtmVclRateExtParam15_Object((1,3,6,1,4,1,5504,4,2,2,6,15),_ZhoneAtmVclRateExtParam15_Type())
zhoneAtmVclRateExtParam15.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam15.setStatus(_A)
class _ZhoneAtmVclRateExtParam16_Type(Integer32):defaultValue=365567
_ZhoneAtmVclRateExtParam16_Type.__name__=_C
_ZhoneAtmVclRateExtParam16_Object=MibScalar
zhoneAtmVclRateExtParam16=_ZhoneAtmVclRateExtParam16_Object((1,3,6,1,4,1,5504,4,2,2,6,16),_ZhoneAtmVclRateExtParam16_Type())
zhoneAtmVclRateExtParam16.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam16.setStatus(_A)
class _ZhoneAtmVclRateExtParam1Grp2_Type(Integer32):defaultValue=2264
_ZhoneAtmVclRateExtParam1Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam1Grp2_Object=MibScalar
zhoneAtmVclRateExtParam1Grp2=_ZhoneAtmVclRateExtParam1Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,17),_ZhoneAtmVclRateExtParam1Grp2_Type())
zhoneAtmVclRateExtParam1Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam1Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam2Grp2_Type(Integer32):defaultValue=3019
_ZhoneAtmVclRateExtParam2Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam2Grp2_Object=MibScalar
zhoneAtmVclRateExtParam2Grp2=_ZhoneAtmVclRateExtParam2Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,18),_ZhoneAtmVclRateExtParam2Grp2_Type())
zhoneAtmVclRateExtParam2Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam2Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam3Grp2_Type(Integer32):defaultValue=4151
_ZhoneAtmVclRateExtParam3Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam3Grp2_Object=MibScalar
zhoneAtmVclRateExtParam3Grp2=_ZhoneAtmVclRateExtParam3Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,19),_ZhoneAtmVclRateExtParam3Grp2_Type())
zhoneAtmVclRateExtParam3Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam3Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam4Grp2_Type(Integer32):defaultValue=7075
_ZhoneAtmVclRateExtParam4Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam4Grp2_Object=MibScalar
zhoneAtmVclRateExtParam4Grp2=_ZhoneAtmVclRateExtParam4Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,20),_ZhoneAtmVclRateExtParam4Grp2_Type())
zhoneAtmVclRateExtParam4Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam4Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam5Grp2_Type(Integer32):defaultValue=9434
_ZhoneAtmVclRateExtParam5Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam5Grp2_Object=MibScalar
zhoneAtmVclRateExtParam5Grp2=_ZhoneAtmVclRateExtParam5Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,21),_ZhoneAtmVclRateExtParam5Grp2_Type())
zhoneAtmVclRateExtParam5Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam5Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam6Grp2_Type(Integer32):defaultValue=11792
_ZhoneAtmVclRateExtParam6Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam6Grp2_Object=MibScalar
zhoneAtmVclRateExtParam6Grp2=_ZhoneAtmVclRateExtParam6Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,22),_ZhoneAtmVclRateExtParam6Grp2_Type())
zhoneAtmVclRateExtParam6Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam6Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam7Grp2_Type(Integer32):defaultValue=14151
_ZhoneAtmVclRateExtParam7Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam7Grp2_Object=MibScalar
zhoneAtmVclRateExtParam7Grp2=_ZhoneAtmVclRateExtParam7Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,23),_ZhoneAtmVclRateExtParam7Grp2_Type())
zhoneAtmVclRateExtParam7Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam7Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam8Grp2_Type(Integer32):defaultValue=16509
_ZhoneAtmVclRateExtParam8Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam8Grp2_Object=MibScalar
zhoneAtmVclRateExtParam8Grp2=_ZhoneAtmVclRateExtParam8Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,24),_ZhoneAtmVclRateExtParam8Grp2_Type())
zhoneAtmVclRateExtParam8Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam8Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam9Grp2_Type(Integer32):defaultValue=18868
_ZhoneAtmVclRateExtParam9Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam9Grp2_Object=MibScalar
zhoneAtmVclRateExtParam9Grp2=_ZhoneAtmVclRateExtParam9Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,25),_ZhoneAtmVclRateExtParam9Grp2_Type())
zhoneAtmVclRateExtParam9Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam9Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam10Grp2_Type(Integer32):defaultValue=23585
_ZhoneAtmVclRateExtParam10Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam10Grp2_Object=MibScalar
zhoneAtmVclRateExtParam10Grp2=_ZhoneAtmVclRateExtParam10Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,26),_ZhoneAtmVclRateExtParam10Grp2_Type())
zhoneAtmVclRateExtParam10Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam10Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam11Grp2_Type(Integer32):defaultValue=33019
_ZhoneAtmVclRateExtParam11Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam11Grp2_Object=MibScalar
zhoneAtmVclRateExtParam11Grp2=_ZhoneAtmVclRateExtParam11Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,27),_ZhoneAtmVclRateExtParam11Grp2_Type())
zhoneAtmVclRateExtParam11Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam11Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam12Grp2_Type(Integer32):defaultValue=56604
_ZhoneAtmVclRateExtParam12Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam12Grp2_Object=MibScalar
zhoneAtmVclRateExtParam12Grp2=_ZhoneAtmVclRateExtParam12Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,28),_ZhoneAtmVclRateExtParam12Grp2_Type())
zhoneAtmVclRateExtParam12Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam12Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam13Grp2_Type(Integer32):defaultValue=75472
_ZhoneAtmVclRateExtParam13Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam13Grp2_Object=MibScalar
zhoneAtmVclRateExtParam13Grp2=_ZhoneAtmVclRateExtParam13Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,29),_ZhoneAtmVclRateExtParam13Grp2_Type())
zhoneAtmVclRateExtParam13Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam13Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam14Grp2_Type(Integer32):defaultValue=150943
_ZhoneAtmVclRateExtParam14Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam14Grp2_Object=MibScalar
zhoneAtmVclRateExtParam14Grp2=_ZhoneAtmVclRateExtParam14Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,30),_ZhoneAtmVclRateExtParam14Grp2_Type())
zhoneAtmVclRateExtParam14Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam14Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam15Grp2_Type(Integer32):defaultValue=226415
_ZhoneAtmVclRateExtParam15Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam15Grp2_Object=MibScalar
zhoneAtmVclRateExtParam15Grp2=_ZhoneAtmVclRateExtParam15Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,31),_ZhoneAtmVclRateExtParam15Grp2_Type())
zhoneAtmVclRateExtParam15Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam15Grp2.setStatus(_A)
class _ZhoneAtmVclRateExtParam16Grp2_Type(Integer32):defaultValue=301887
_ZhoneAtmVclRateExtParam16Grp2_Type.__name__=_C
_ZhoneAtmVclRateExtParam16Grp2_Object=MibScalar
zhoneAtmVclRateExtParam16Grp2=_ZhoneAtmVclRateExtParam16Grp2_Object((1,3,6,1,4,1,5504,4,2,2,6,32),_ZhoneAtmVclRateExtParam16Grp2_Type())
zhoneAtmVclRateExtParam16Grp2.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVclRateExtParam16Grp2.setStatus(_A)
_ZhoneAtmVplExtTable_Object=MibTable
zhoneAtmVplExtTable=_ZhoneAtmVplExtTable_Object((1,3,6,1,4,1,5504,4,2,2,7))
if mibBuilder.loadTexts:zhoneAtmVplExtTable.setStatus(_A)
_ZhoneAtmVplExtEntry_Object=MibTableRow
zhoneAtmVplExtEntry=_ZhoneAtmVplExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,7,1))
if mibBuilder.loadTexts:zhoneAtmVplExtEntry.setStatus(_A)
class _ZhoneAtmVplExtFaultDetectionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('oamF4Loopback',2)))
_ZhoneAtmVplExtFaultDetectionType_Type.__name__=_C
_ZhoneAtmVplExtFaultDetectionType_Object=MibTableColumn
zhoneAtmVplExtFaultDetectionType=_ZhoneAtmVplExtFaultDetectionType_Object((1,3,6,1,4,1,5504,4,2,2,7,1,1),_ZhoneAtmVplExtFaultDetectionType_Type())
zhoneAtmVplExtFaultDetectionType.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVplExtFaultDetectionType.setStatus(_A)
class _ZhoneAtmVplExtTrafficContainerIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneAtmVplExtTrafficContainerIndex_Type.__name__=_C
_ZhoneAtmVplExtTrafficContainerIndex_Object=MibTableColumn
zhoneAtmVplExtTrafficContainerIndex=_ZhoneAtmVplExtTrafficContainerIndex_Object((1,3,6,1,4,1,5504,4,2,2,7,1,2),_ZhoneAtmVplExtTrafficContainerIndex_Type())
zhoneAtmVplExtTrafficContainerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVplExtTrafficContainerIndex.setStatus(_A)
_ZhoneAtmConnectionStatsTable_Object=MibTable
zhoneAtmConnectionStatsTable=_ZhoneAtmConnectionStatsTable_Object((1,3,6,1,4,1,5504,4,2,2,8))
if mibBuilder.loadTexts:zhoneAtmConnectionStatsTable.setStatus(_A)
_ZhoneAtmConnectionStatsEntry_Object=MibTableRow
zhoneAtmConnectionStatsEntry=_ZhoneAtmConnectionStatsEntry_Object((1,3,6,1,4,1,5504,4,2,2,8,1))
zhoneAtmConnectionStatsEntry.setIndexNames((0,_O,_i),(0,_O,_j))
if mibBuilder.loadTexts:zhoneAtmConnectionStatsEntry.setStatus(_A)
_ZhoneAtmConnectionsAvailable_Type=Integer32
_ZhoneAtmConnectionsAvailable_Object=MibTableColumn
zhoneAtmConnectionsAvailable=_ZhoneAtmConnectionsAvailable_Object((1,3,6,1,4,1,5504,4,2,2,8,1,1),_ZhoneAtmConnectionsAvailable_Type())
zhoneAtmConnectionsAvailable.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmConnectionsAvailable.setStatus(_A)
_ZhoneAtmConnectionsAllocated_Type=Integer32
_ZhoneAtmConnectionsAllocated_Object=MibTableColumn
zhoneAtmConnectionsAllocated=_ZhoneAtmConnectionsAllocated_Object((1,3,6,1,4,1,5504,4,2,2,8,1,2),_ZhoneAtmConnectionsAllocated_Type())
zhoneAtmConnectionsAllocated.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmConnectionsAllocated.setStatus(_A)
_ZhoneAtmVpiTable_Object=MibTable
zhoneAtmVpiTable=_ZhoneAtmVpiTable_Object((1,3,6,1,4,1,5504,4,2,2,9))
if mibBuilder.loadTexts:zhoneAtmVpiTable.setStatus(_A)
_ZhoneAtmVpiEntry_Object=MibTableRow
zhoneAtmVpiEntry=_ZhoneAtmVpiEntry_Object((1,3,6,1,4,1,5504,4,2,2,9,1))
zhoneAtmVpiEntry.setIndexNames((0,_J,_K),(0,_G,_g))
if mibBuilder.loadTexts:zhoneAtmVpiEntry.setStatus(_A)
class _ZhoneAtmVpiMaxVci_Type(Integer32):defaultValue=0
_ZhoneAtmVpiMaxVci_Type.__name__=_C
_ZhoneAtmVpiMaxVci_Object=MibTableColumn
zhoneAtmVpiMaxVci=_ZhoneAtmVpiMaxVci_Object((1,3,6,1,4,1,5504,4,2,2,9,1,1),_ZhoneAtmVpiMaxVci_Type())
zhoneAtmVpiMaxVci.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVpiMaxVci.setStatus(_A)
class _ZhoneAtmVpiSwitched_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vp',1),('vc',2)))
_ZhoneAtmVpiSwitched_Type.__name__=_C
_ZhoneAtmVpiSwitched_Object=MibTableColumn
zhoneAtmVpiSwitched=_ZhoneAtmVpiSwitched_Object((1,3,6,1,4,1,5504,4,2,2,9,1,2),_ZhoneAtmVpiSwitched_Type())
zhoneAtmVpiSwitched.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVpiSwitched.setStatus(_A)
_ZhoneAtmVpiRowStatus_Type=ZhoneRowStatus
_ZhoneAtmVpiRowStatus_Object=MibTableColumn
zhoneAtmVpiRowStatus=_ZhoneAtmVpiRowStatus_Object((1,3,6,1,4,1,5504,4,2,2,9,1,3),_ZhoneAtmVpiRowStatus_Type())
zhoneAtmVpiRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVpiRowStatus.setStatus(_A)
class _ZhoneAtmVpiOamF4Ping_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_P,2),(_Q,3)))
_ZhoneAtmVpiOamF4Ping_Type.__name__=_C
_ZhoneAtmVpiOamF4Ping_Object=MibTableColumn
zhoneAtmVpiOamF4Ping=_ZhoneAtmVpiOamF4Ping_Object((1,3,6,1,4,1,5504,4,2,2,9,1,4),_ZhoneAtmVpiOamF4Ping_Type())
zhoneAtmVpiOamF4Ping.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVpiOamF4Ping.setStatus(_A)
_ZhoneAtmVpiOamF4PingStatus_Type=TruthValue
_ZhoneAtmVpiOamF4PingStatus_Object=MibTableColumn
zhoneAtmVpiOamF4PingStatus=_ZhoneAtmVpiOamF4PingStatus_Object((1,3,6,1,4,1,5504,4,2,2,9,1,5),_ZhoneAtmVpiOamF4PingStatus_Type())
zhoneAtmVpiOamF4PingStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:zhoneAtmVpiOamF4PingStatus.setStatus(_A)
_ZhoneAtmVpiMaxVciPerVp_Type=Integer32
_ZhoneAtmVpiMaxVciPerVp_Object=MibTableColumn
zhoneAtmVpiMaxVciPerVp=_ZhoneAtmVpiMaxVciPerVp_Object((1,3,6,1,4,1,5504,4,2,2,9,1,6),_ZhoneAtmVpiMaxVciPerVp_Type())
zhoneAtmVpiMaxVciPerVp.setMaxAccess(_D)
if mibBuilder.loadTexts:zhoneAtmVpiMaxVciPerVp.setStatus(_A)
_AtmVpi_Type=AtmVpIdentifier
_AtmVpi_Object=MibScalar
atmVpi=_AtmVpi_Object((1,3,6,1,4,1,5504,4,2,2,10),_AtmVpi_Type())
atmVpi.setMaxAccess(_H)
if mibBuilder.loadTexts:atmVpi.setStatus(_A)
_AtmVci_Type=AtmVcIdentifier
_AtmVci_Object=MibScalar
atmVci=_AtmVci_Object((1,3,6,1,4,1,5504,4,2,2,11),_AtmVci_Type())
atmVci.setMaxAccess(_H)
if mibBuilder.loadTexts:atmVci.setStatus(_A)
_AtmVpiAutoCreateDone_Type=TruthValue
_AtmVpiAutoCreateDone_Object=MibScalar
atmVpiAutoCreateDone=_AtmVpiAutoCreateDone_Object((1,3,6,1,4,1,5504,4,2,2,12),_AtmVpiAutoCreateDone_Type())
atmVpiAutoCreateDone.setMaxAccess(_H)
if mibBuilder.loadTexts:atmVpiAutoCreateDone.setStatus(_A)
_AtmVpiAutoCreateCount_Type=Integer32
_AtmVpiAutoCreateCount_Object=MibScalar
atmVpiAutoCreateCount=_AtmVpiAutoCreateCount_Object((1,3,6,1,4,1,5504,4,2,2,13),_AtmVpiAutoCreateCount_Type())
atmVpiAutoCreateCount.setMaxAccess(_H)
if mibBuilder.loadTexts:atmVpiAutoCreateCount.setStatus(_A)
_AtmVclToMulticastMap_ObjectIdentity=ObjectIdentity
atmVclToMulticastMap=_AtmVclToMulticastMap_ObjectIdentity((1,3,6,1,4,1,5504,4,2,2,16))
class _AtmVclToMulticastMapIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmVclToMulticastMapIndexNext_Type.__name__=_C
_AtmVclToMulticastMapIndexNext_Object=MibScalar
atmVclToMulticastMapIndexNext=_AtmVclToMulticastMapIndexNext_Object((1,3,6,1,4,1,5504,4,2,2,16,1),_AtmVclToMulticastMapIndexNext_Type())
atmVclToMulticastMapIndexNext.setMaxAccess(_F)
if mibBuilder.loadTexts:atmVclToMulticastMapIndexNext.setStatus(_A)
_AtmVclToMulticastMapTable_Object=MibTable
atmVclToMulticastMapTable=_AtmVclToMulticastMapTable_Object((1,3,6,1,4,1,5504,4,2,2,16,2))
if mibBuilder.loadTexts:atmVclToMulticastMapTable.setStatus(_A)
_AtmVclToMulticastMapEntry_Object=MibTableRow
atmVclToMulticastMapEntry=_AtmVclToMulticastMapEntry_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1))
atmVclToMulticastMapEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:atmVclToMulticastMapEntry.setStatus(_A)
class _AtmVclToMulticastMapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtmVclToMulticastMapIndex_Type.__name__=_C
_AtmVclToMulticastMapIndex_Object=MibTableColumn
atmVclToMulticastMapIndex=_AtmVclToMulticastMapIndex_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1,1),_AtmVclToMulticastMapIndex_Type())
atmVclToMulticastMapIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:atmVclToMulticastMapIndex.setStatus(_A)
class _AtmVclToMulticastMapRoutingDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtmVclToMulticastMapRoutingDomain_Type.__name__=_C
_AtmVclToMulticastMapRoutingDomain_Object=MibTableColumn
atmVclToMulticastMapRoutingDomain=_AtmVclToMulticastMapRoutingDomain_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1,2),_AtmVclToMulticastMapRoutingDomain_Type())
atmVclToMulticastMapRoutingDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVclToMulticastMapRoutingDomain.setStatus(_A)
_AtmVclToMulticastMapMulticastAddress_Type=IpAddress
_AtmVclToMulticastMapMulticastAddress_Object=MibTableColumn
atmVclToMulticastMapMulticastAddress=_AtmVclToMulticastMapMulticastAddress_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1,3),_AtmVclToMulticastMapMulticastAddress_Type())
atmVclToMulticastMapMulticastAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVclToMulticastMapMulticastAddress.setStatus(_A)
_AtmVclToMulticastMapIfIndex_Type=InterfaceIndex
_AtmVclToMulticastMapIfIndex_Object=MibTableColumn
atmVclToMulticastMapIfIndex=_AtmVclToMulticastMapIfIndex_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1,4),_AtmVclToMulticastMapIfIndex_Type())
atmVclToMulticastMapIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVclToMulticastMapIfIndex.setStatus(_A)
_AtmVclToMulticastMapVpi_Type=AtmVpIdentifier
_AtmVclToMulticastMapVpi_Object=MibTableColumn
atmVclToMulticastMapVpi=_AtmVclToMulticastMapVpi_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1,5),_AtmVclToMulticastMapVpi_Type())
atmVclToMulticastMapVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVclToMulticastMapVpi.setStatus(_A)
_AtmVclToMulticastMapVci_Type=AtmVcIdentifier
_AtmVclToMulticastMapVci_Object=MibTableColumn
atmVclToMulticastMapVci=_AtmVclToMulticastMapVci_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1,6),_AtmVclToMulticastMapVci_Type())
atmVclToMulticastMapVci.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVclToMulticastMapVci.setStatus(_A)
_AtmVclToMulticastMapRowStatus_Type=ZhoneRowStatus
_AtmVclToMulticastMapRowStatus_Object=MibTableColumn
atmVclToMulticastMapRowStatus=_AtmVclToMulticastMapRowStatus_Object((1,3,6,1,4,1,5504,4,2,2,16,2,1,7),_AtmVclToMulticastMapRowStatus_Type())
atmVclToMulticastMapRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:atmVclToMulticastMapRowStatus.setStatus(_A)
_ZhoneAtmPonExtTable_Object=MibTable
zhoneAtmPonExtTable=_ZhoneAtmPonExtTable_Object((1,3,6,1,4,1,5504,4,2,2,17))
if mibBuilder.loadTexts:zhoneAtmPonExtTable.setStatus(_I)
_ZhoneAtmPonExtEntry_Object=MibTableRow
zhoneAtmPonExtEntry=_ZhoneAtmPonExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,17,1))
if mibBuilder.loadTexts:zhoneAtmPonExtEntry.setStatus(_I)
class _ZhoneAtmVclPonTrafficContainerIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZhoneAtmVclPonTrafficContainerIndex_Type.__name__=_C
_ZhoneAtmVclPonTrafficContainerIndex_Object=MibTableColumn
zhoneAtmVclPonTrafficContainerIndex=_ZhoneAtmVclPonTrafficContainerIndex_Object((1,3,6,1,4,1,5504,4,2,2,17,1,1),_ZhoneAtmVclPonTrafficContainerIndex_Type())
zhoneAtmVclPonTrafficContainerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVclPonTrafficContainerIndex.setStatus(_I)
_ZhoneAtmVplPonExtTable_Object=MibTable
zhoneAtmVplPonExtTable=_ZhoneAtmVplPonExtTable_Object((1,3,6,1,4,1,5504,4,2,2,18))
if mibBuilder.loadTexts:zhoneAtmVplPonExtTable.setStatus(_I)
_ZhoneAtmVplPonExtEntry_Object=MibTableRow
zhoneAtmVplPonExtEntry=_ZhoneAtmVplPonExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,18,1))
if mibBuilder.loadTexts:zhoneAtmVplPonExtEntry.setStatus(_I)
class _ZhoneAtmVplPonTrafficContainerIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZhoneAtmVplPonTrafficContainerIndex_Type.__name__=_C
_ZhoneAtmVplPonTrafficContainerIndex_Object=MibTableColumn
zhoneAtmVplPonTrafficContainerIndex=_ZhoneAtmVplPonTrafficContainerIndex_Object((1,3,6,1,4,1,5504,4,2,2,18,1,1),_ZhoneAtmVplPonTrafficContainerIndex_Type())
zhoneAtmVplPonTrafficContainerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVplPonTrafficContainerIndex.setStatus(_I)
_ZhoneAtmInterfaceTcExtTable_Object=MibTable
zhoneAtmInterfaceTcExtTable=_ZhoneAtmInterfaceTcExtTable_Object((1,3,6,1,4,1,5504,4,2,2,19))
if mibBuilder.loadTexts:zhoneAtmInterfaceTcExtTable.setStatus(_A)
_ZhoneAtmInterfaceTcExtEntry_Object=MibTableRow
zhoneAtmInterfaceTcExtEntry=_ZhoneAtmInterfaceTcExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,19,1))
if mibBuilder.loadTexts:zhoneAtmInterfaceTcExtEntry.setStatus(_A)
_ZhoneAtmInterfaceNCDEvents_Type=Counter32
_ZhoneAtmInterfaceNCDEvents_Object=MibTableColumn
zhoneAtmInterfaceNCDEvents=_ZhoneAtmInterfaceNCDEvents_Object((1,3,6,1,4,1,5504,4,2,2,19,1,1),_ZhoneAtmInterfaceNCDEvents_Type())
zhoneAtmInterfaceNCDEvents.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmInterfaceNCDEvents.setStatus(_A)
_ZhoneAtmInterfaceHECEvents_Type=Counter32
_ZhoneAtmInterfaceHECEvents_Object=MibTableColumn
zhoneAtmInterfaceHECEvents=_ZhoneAtmInterfaceHECEvents_Object((1,3,6,1,4,1,5504,4,2,2,19,1,2),_ZhoneAtmInterfaceHECEvents_Type())
zhoneAtmInterfaceHECEvents.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmInterfaceHECEvents.setStatus(_A)
_ZhoneAtmInterfaceFeOCDEvents_Type=Counter32
_ZhoneAtmInterfaceFeOCDEvents_Object=MibTableColumn
zhoneAtmInterfaceFeOCDEvents=_ZhoneAtmInterfaceFeOCDEvents_Object((1,3,6,1,4,1,5504,4,2,2,19,1,3),_ZhoneAtmInterfaceFeOCDEvents_Type())
zhoneAtmInterfaceFeOCDEvents.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmInterfaceFeOCDEvents.setStatus(_A)
_ZhoneAtmInterfaceFeNCDEvents_Type=Counter32
_ZhoneAtmInterfaceFeNCDEvents_Object=MibTableColumn
zhoneAtmInterfaceFeNCDEvents=_ZhoneAtmInterfaceFeNCDEvents_Object((1,3,6,1,4,1,5504,4,2,2,19,1,4),_ZhoneAtmInterfaceFeNCDEvents_Type())
zhoneAtmInterfaceFeNCDEvents.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmInterfaceFeNCDEvents.setStatus(_A)
_ZhoneAtmInterfaceFeHECEvents_Type=Counter32
_ZhoneAtmInterfaceFeHECEvents_Object=MibTableColumn
zhoneAtmInterfaceFeHECEvents=_ZhoneAtmInterfaceFeHECEvents_Object((1,3,6,1,4,1,5504,4,2,2,19,1,5),_ZhoneAtmInterfaceFeHECEvents_Type())
zhoneAtmInterfaceFeHECEvents.setMaxAccess(_F)
if mibBuilder.loadTexts:zhoneAtmInterfaceFeHECEvents.setStatus(_A)
_ZhoneAtmVcCrossConnectExtTable_Object=MibTable
zhoneAtmVcCrossConnectExtTable=_ZhoneAtmVcCrossConnectExtTable_Object((1,3,6,1,4,1,5504,4,2,2,20))
if mibBuilder.loadTexts:zhoneAtmVcCrossConnectExtTable.setStatus(_A)
_ZhoneAtmVcCrossConnectExtEntry_Object=MibTableRow
zhoneAtmVcCrossConnectExtEntry=_ZhoneAtmVcCrossConnectExtEntry_Object((1,3,6,1,4,1,5504,4,2,2,20,1))
if mibBuilder.loadTexts:zhoneAtmVcCrossConnectExtEntry.setStatus(_A)
class _ZhoneAtmVcCrossConnectExtHandleId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_ZhoneAtmVcCrossConnectExtHandleId_Type.__name__=_V
_ZhoneAtmVcCrossConnectExtHandleId_Object=MibTableColumn
zhoneAtmVcCrossConnectExtHandleId=_ZhoneAtmVcCrossConnectExtHandleId_Object((1,3,6,1,4,1,5504,4,2,2,20,1,1),_ZhoneAtmVcCrossConnectExtHandleId_Type())
zhoneAtmVcCrossConnectExtHandleId.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneAtmVcCrossConnectExtHandleId.setStatus(_A)
atmVclEntry.registerAugmentions((_B,_l))
zhoneAtmVclExtEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmTrafficDescrParamEntry.registerAugmentions((_B,_m))
zhoneAtmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
atmVclEntry.registerAugmentions((_B,_n))
zhoneAtmStatsExtEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions((_B,_o))
zhoneAtmVplExtEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmVclEntry.registerAugmentions((_B,_p))
zhoneAtmPonExtEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions((_B,_q))
zhoneAtmVplPonExtEntry.setIndexNames(*atmVplEntry.getIndexNames())
atmInterfaceTCEntry.registerAugmentions((_B,_r))
zhoneAtmInterfaceTcExtEntry.setIndexNames(*atmInterfaceTCEntry.getIndexNames())
atmVcCrossConnectEntry.registerAugmentions((_B,_s))
zhoneAtmVcCrossConnectExtEntry.setIndexNames(*atmVcCrossConnectEntry.getIndexNames())
zhoneAtmVclExtGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,1))
zhoneAtmVclExtGroup.setObjects(*((_B,_t),(_B,_u),(_B,_R),(_B,_v)))
if mibBuilder.loadTexts:zhoneAtmVclExtGroup.setStatus(_A)
zhoneAtmTrafficDescrParamExtGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,3))
zhoneAtmTrafficDescrParamExtGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:zhoneAtmTrafficDescrParamExtGroup.setStatus(_A)
zhoneAtmStatsExtTableGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,4))
zhoneAtmStatsExtTableGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:zhoneAtmStatsExtTableGroup.setStatus(_A)
zhoneAtmVclRateExtParamGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,5))
zhoneAtmVclRateExtParamGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac)))
if mibBuilder.loadTexts:zhoneAtmVclRateExtParamGroup.setStatus(_A)
zhoneAtmVplExtGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,6))
zhoneAtmVplExtGroup.setObjects(*((_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:zhoneAtmVplExtGroup.setStatus(_A)
zhoneAtmConnectionStatsGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,7))
zhoneAtmConnectionStatsGroup.setObjects(*((_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:zhoneAtmConnectionStatsGroup.setStatus(_A)
zhoneAtmVpiGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,8))
zhoneAtmVpiGroup.setObjects(*((_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_M),(_B,_N),(_B,_S),(_B,_T),(_B,_Ak),(_B,_U),(_B,_Al)))
if mibBuilder.loadTexts:zhoneAtmVpiGroup.setStatus(_A)
zhoneAtmPonGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,9))
zhoneAtmPonGroup.setObjects(*((_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:zhoneAtmPonGroup.setStatus(_I)
zhoneAtmVclMulticastGroup=ObjectGroup((1,3,6,1,4,1,5504,4,2,2,3,10))
zhoneAtmVclMulticastGroup.setObjects(*((_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:zhoneAtmVclMulticastGroup.setStatus(_A)
atmVclOperStatusChange=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,1))
atmVclOperStatusChange.setObjects(*((_G,_Y),(_G,_a),(_G,_Z)))
if mibBuilder.loadTexts:atmVclOperStatusChange.setStatus(_A)
atmDsx3PlcpAlarmStatusChange=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,2))
atmDsx3PlcpAlarmStatusChange.setObjects((_G,_W))
if mibBuilder.loadTexts:atmDsx3PlcpAlarmStatusChange.setStatus(_A)
atmInterfaceTCAlarmStateChange=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,3))
atmInterfaceTCAlarmStateChange.setObjects((_G,_X))
if mibBuilder.loadTexts:atmInterfaceTCAlarmStateChange.setStatus(_A)
atmVclBandwidthUnavailable=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,4))
atmVclBandwidthUnavailable.setObjects(*((_G,_b),(_G,_c)))
if mibBuilder.loadTexts:atmVclBandwidthUnavailable.setStatus(_A)
atmVplOperStatusChange=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,5))
atmVplOperStatusChange.setObjects(*((_G,_d),(_G,_f),(_G,_e)))
if mibBuilder.loadTexts:atmVplOperStatusChange.setStatus(_A)
atmOamF5PingStatus=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,6))
atmOamF5PingStatus.setObjects(*((_J,_K),(_B,_M),(_B,_N),(_B,_R)))
if mibBuilder.loadTexts:atmOamF5PingStatus.setStatus(_A)
atmVpiAutoCreateComplete=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,7))
atmVpiAutoCreateComplete.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:atmVpiAutoCreateComplete.setStatus(_A)
atmOamF4PingStatus=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,8))
atmOamF4PingStatus.setObjects(*((_J,_K),(_B,_M),(_B,_N),(_B,_U)))
if mibBuilder.loadTexts:atmOamF4PingStatus.setStatus(_A)
atmVclExtOamF4PingStatus=NotificationType((1,3,6,1,4,1,5504,4,2,2,2,0,9))
atmVclExtOamF4PingStatus.setObjects(*((_J,_K),(_B,_M),(_B,_N),(_B,_Av)))
if mibBuilder.loadTexts:atmVclExtOamF4PingStatus.setStatus(_A)
zhoneAtmTrapsGroup=NotificationGroup((1,3,6,1,4,1,5504,4,2,2,3,2))
zhoneAtmTrapsGroup.setObjects(*((_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2)))
if mibBuilder.loadTexts:zhoneAtmTrapsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zhoneAtmExtension':zhoneAtmExtension,'zhoneAtmVclExtTable':zhoneAtmVclExtTable,_l:zhoneAtmVclExtEntry,_t:zhoneAtmVclExtFaultDetectionType,_u:zhoneAtmVclExtOamF5Ping,_R:zhoneAtmVclExtOamF5PingStatus,_v:zhoneAtmVclExtTrafficContainerIndex,'zhoneAtmVclExtOamF4Ping':zhoneAtmVclExtOamF4Ping,_Av:zhoneAtmVclExtOamF4PingStatus,'zhoneAtmTraps':zhoneAtmTraps,'zhoneAtmV2Traps':zhoneAtmV2Traps,_Aw:atmVclOperStatusChange,_Ax:atmDsx3PlcpAlarmStatusChange,_Ay:atmInterfaceTCAlarmStateChange,_Az:atmVclBandwidthUnavailable,_A_:atmVplOperStatusChange,_B0:atmOamF5PingStatus,_B1:atmVpiAutoCreateComplete,_B2:atmOamF4PingStatus,'atmVclExtOamF4PingStatus':atmVclExtOamF4PingStatus,'zhoneAtmGroups':zhoneAtmGroups,'zhoneAtmVclExtGroup':zhoneAtmVclExtGroup,'zhoneAtmTrapsGroup':zhoneAtmTrapsGroup,'zhoneAtmTrafficDescrParamExtGroup':zhoneAtmTrafficDescrParamExtGroup,'zhoneAtmStatsExtTableGroup':zhoneAtmStatsExtTableGroup,'zhoneAtmVclRateExtParamGroup':zhoneAtmVclRateExtParamGroup,'zhoneAtmVplExtGroup':zhoneAtmVplExtGroup,'zhoneAtmConnectionStatsGroup':zhoneAtmConnectionStatsGroup,'zhoneAtmVpiGroup':zhoneAtmVpiGroup,'zhoneAtmPonGroup':zhoneAtmPonGroup,'zhoneAtmVclMulticastGroup':zhoneAtmVclMulticastGroup,'zhoneAtmTrafficDescrParamExtTable':zhoneAtmTrafficDescrParamExtTable,_m:zhoneAtmTrafficDescrParamExtEntry,_w:zhoneAtmTrafficDescrParamExtTrnkVclRate,_x:zhoneAtmTrafficDescrParamExtCacDivider,_y:zhoneAtmTrafficDescrParamExtUsageParameterControl,'zhoneAtmStatsExtTable':zhoneAtmStatsExtTable,_n:zhoneAtmStatsExtEntry,_z:zhoneAtmStatsTotalInitialCellsRx,_A0:zhoneAtmStatsTotalFabricCellsRx,_A1:zhoneAtmStatsTotalFinalCLP0CellsRx,_A2:zhoneAtmStatsTotalFinalCLP1CellsRx,_A6:zhoneAtmStatsTotalInitialCellsTx,_A3:zhoneAtmStatsTotalFabricCellsTx,_A4:zhoneAtmStatsTotalFinalCLP0CellsTx,_A5:zhoneAtmStatsTotalFinalCLP1CellsTx,'zhoneAtmVclRateExtParam':zhoneAtmVclRateExtParam,_A7:zhoneAtmVclRateExtParam1,_A8:zhoneAtmVclRateExtParam2,_A9:zhoneAtmVclRateExtParam3,_AA:zhoneAtmVclRateExtParam4,_AB:zhoneAtmVclRateExtParam5,_AC:zhoneAtmVclRateExtParam6,_AD:zhoneAtmVclRateExtParam7,_AE:zhoneAtmVclRateExtParam8,_AF:zhoneAtmVclRateExtParam9,_AG:zhoneAtmVclRateExtParam10,_AH:zhoneAtmVclRateExtParam11,_AI:zhoneAtmVclRateExtParam12,_AJ:zhoneAtmVclRateExtParam13,_AK:zhoneAtmVclRateExtParam14,_AL:zhoneAtmVclRateExtParam15,_AM:zhoneAtmVclRateExtParam16,_AN:zhoneAtmVclRateExtParam1Grp2,_AO:zhoneAtmVclRateExtParam2Grp2,_AP:zhoneAtmVclRateExtParam3Grp2,_AQ:zhoneAtmVclRateExtParam4Grp2,_AR:zhoneAtmVclRateExtParam5Grp2,_AS:zhoneAtmVclRateExtParam6Grp2,_AT:zhoneAtmVclRateExtParam7Grp2,_AU:zhoneAtmVclRateExtParam8Grp2,_AV:zhoneAtmVclRateExtParam9Grp2,_AW:zhoneAtmVclRateExtParam10Grp2,_AX:zhoneAtmVclRateExtParam11Grp2,_AY:zhoneAtmVclRateExtParam12Grp2,_AZ:zhoneAtmVclRateExtParam13Grp2,_Aa:zhoneAtmVclRateExtParam14Grp2,_Ab:zhoneAtmVclRateExtParam15Grp2,_Ac:zhoneAtmVclRateExtParam16Grp2,'zhoneAtmVplExtTable':zhoneAtmVplExtTable,_o:zhoneAtmVplExtEntry,_Ad:zhoneAtmVplExtFaultDetectionType,_Ae:zhoneAtmVplExtTrafficContainerIndex,'zhoneAtmConnectionStatsTable':zhoneAtmConnectionStatsTable,'zhoneAtmConnectionStatsEntry':zhoneAtmConnectionStatsEntry,_Af:zhoneAtmConnectionsAvailable,_Ag:zhoneAtmConnectionsAllocated,'zhoneAtmVpiTable':zhoneAtmVpiTable,'zhoneAtmVpiEntry':zhoneAtmVpiEntry,_Ah:zhoneAtmVpiMaxVci,_Ai:zhoneAtmVpiSwitched,_Aj:zhoneAtmVpiRowStatus,_Ak:zhoneAtmVpiOamF4Ping,_U:zhoneAtmVpiOamF4PingStatus,_Al:zhoneAtmVpiMaxVciPerVp,_M:atmVpi,_N:atmVci,_S:atmVpiAutoCreateDone,_T:atmVpiAutoCreateCount,'atmVclToMulticastMap':atmVclToMulticastMap,_Ao:atmVclToMulticastMapIndexNext,'atmVclToMulticastMapTable':atmVclToMulticastMapTable,'atmVclToMulticastMapEntry':atmVclToMulticastMapEntry,_k:atmVclToMulticastMapIndex,_Ap:atmVclToMulticastMapRoutingDomain,_Aq:atmVclToMulticastMapMulticastAddress,_Ar:atmVclToMulticastMapIfIndex,_As:atmVclToMulticastMapVpi,_At:atmVclToMulticastMapVci,_Au:atmVclToMulticastMapRowStatus,'zhoneAtmPonExtTable':zhoneAtmPonExtTable,_p:zhoneAtmPonExtEntry,_Am:zhoneAtmVclPonTrafficContainerIndex,'zhoneAtmVplPonExtTable':zhoneAtmVplPonExtTable,_q:zhoneAtmVplPonExtEntry,_An:zhoneAtmVplPonTrafficContainerIndex,'zhoneAtmInterfaceTcExtTable':zhoneAtmInterfaceTcExtTable,_r:zhoneAtmInterfaceTcExtEntry,'zhoneAtmInterfaceNCDEvents':zhoneAtmInterfaceNCDEvents,'zhoneAtmInterfaceHECEvents':zhoneAtmInterfaceHECEvents,'zhoneAtmInterfaceFeOCDEvents':zhoneAtmInterfaceFeOCDEvents,'zhoneAtmInterfaceFeNCDEvents':zhoneAtmInterfaceFeNCDEvents,'zhoneAtmInterfaceFeHECEvents':zhoneAtmInterfaceFeHECEvents,'zhoneAtmVcCrossConnectExtTable':zhoneAtmVcCrossConnectExtTable,_s:zhoneAtmVcCrossConnectExtEntry,'zhoneAtmVcCrossConnectExtHandleId':zhoneAtmVcCrossConnectExtHandleId,'comAtmExtension':comAtmExtension})