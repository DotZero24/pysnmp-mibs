_i='fmmC12ScgPtpGroup'
_h='fmmC5ScgPtpGroup'
_g='fmmC12ScgPtpRxPowerOffset'
_f='fmmC12ScgPtpPassiveMirrorProvNeighborTP'
_e='fmmC12ScgPtpAvailableFreqSlotList'
_d='fmmC12ScgPtpUsedFreqSlotList'
_c='fmmC12ScgPtpPmHistStatsEnable'
_b='fmmC12ScgPtpProvisionedNeighborAdTpType'
_a='fmmC12ScgPtpProvisionedNeighborTP'
_Z='fmmC12ScgPtpInterfaceType'
_Y='fmmC12ScgPtpDiscoveredNeighborTP'
_X='fmmC12ScgPtpAutoDiscoveryState'
_W='fmmC12ScgPtpScgSupEqptType'
_V='fmmC12ScgPtpScgNumber'
_U='fmmC5ScgPtpRxPowerOffset'
_T='fmmC5ScgPtpPassiveMirrorProvNeighborTP'
_S='fmmC5ScgPtpAllowedPassBandList'
_R='fmmC5ScgPtpTxPowerOffset'
_Q='fmmC5ScgPtpAutoDiscSoakTime'
_P='fmmC5ScgPtpAvailableFreqSlotList'
_O='fmmC5ScgPtpUsedFreqSlotList'
_N='fmmC5ScgPtpPmHistStatsEnable'
_M='fmmC5ScgPtpProvisionedNeighborAdTpType'
_L='fmmC5ScgPtpProvisionedNeighborTP'
_K='fmmC5ScgPtpInterfaceType'
_J='fmmC5ScgPtpDiscoveredNeighborTP'
_I='fmmC5ScgPtpAutoDiscoveryState'
_H='fmmC5ScgPtpScgSupEqptType'
_G='fmmC5ScgPtpScgNumber'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-FMMCSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,FloatTenths,InfnAdTpType,InfnAutoDiscoveryState,InfnEnableDisable,InfnEqptType,InfnPmHistStatsControl,InfnWaveInterfaceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnAdTpType','InfnAutoDiscoveryState','InfnEnableDisable','InfnEqptType','InfnPmHistStatsControl','InfnWaveInterfaceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fmmCScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,63))
if mibBuilder.loadTexts:fmmCScgPtpMIB.setRevisions(('2015-05-20 00:00',))
_FmmC5ScgPtpTable_Object=MibTable
fmmC5ScgPtpTable=_FmmC5ScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1))
if mibBuilder.loadTexts:fmmC5ScgPtpTable.setStatus(_A)
_FmmC5ScgPtpEntry_Object=MibTableRow
fmmC5ScgPtpEntry=_FmmC5ScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1))
fmmC5ScgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fmmC5ScgPtpEntry.setStatus(_A)
_FmmC5ScgPtpScgNumber_Type=Integer32
_FmmC5ScgPtpScgNumber_Object=MibTableColumn
fmmC5ScgPtpScgNumber=_FmmC5ScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,1),_FmmC5ScgPtpScgNumber_Type())
fmmC5ScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpScgNumber.setStatus(_A)
_FmmC5ScgPtpScgSupEqptType_Type=InfnEqptType
_FmmC5ScgPtpScgSupEqptType_Object=MibTableColumn
fmmC5ScgPtpScgSupEqptType=_FmmC5ScgPtpScgSupEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,2),_FmmC5ScgPtpScgSupEqptType_Type())
fmmC5ScgPtpScgSupEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC5ScgPtpScgSupEqptType.setStatus(_A)
_FmmC5ScgPtpAutoDiscoveryState_Type=InfnAutoDiscoveryState
_FmmC5ScgPtpAutoDiscoveryState_Object=MibTableColumn
fmmC5ScgPtpAutoDiscoveryState=_FmmC5ScgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,3),_FmmC5ScgPtpAutoDiscoveryState_Type())
fmmC5ScgPtpAutoDiscoveryState.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpAutoDiscoveryState.setStatus(_A)
_FmmC5ScgPtpDiscoveredNeighborTP_Type=DisplayString
_FmmC5ScgPtpDiscoveredNeighborTP_Object=MibTableColumn
fmmC5ScgPtpDiscoveredNeighborTP=_FmmC5ScgPtpDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,4),_FmmC5ScgPtpDiscoveredNeighborTP_Type())
fmmC5ScgPtpDiscoveredNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpDiscoveredNeighborTP.setStatus(_A)
_FmmC5ScgPtpProvisionedNeighborTP_Type=DisplayString
_FmmC5ScgPtpProvisionedNeighborTP_Object=MibTableColumn
fmmC5ScgPtpProvisionedNeighborTP=_FmmC5ScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,5),_FmmC5ScgPtpProvisionedNeighborTP_Type())
fmmC5ScgPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpProvisionedNeighborTP.setStatus(_A)
_FmmC5ScgPtpProvisionedNeighborAdTpType_Type=InfnAdTpType
_FmmC5ScgPtpProvisionedNeighborAdTpType_Object=MibTableColumn
fmmC5ScgPtpProvisionedNeighborAdTpType=_FmmC5ScgPtpProvisionedNeighborAdTpType_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,6),_FmmC5ScgPtpProvisionedNeighborAdTpType_Type())
fmmC5ScgPtpProvisionedNeighborAdTpType.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpProvisionedNeighborAdTpType.setStatus(_A)
_FmmC5ScgPtpInterfaceType_Type=InfnWaveInterfaceType
_FmmC5ScgPtpInterfaceType_Object=MibTableColumn
fmmC5ScgPtpInterfaceType=_FmmC5ScgPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,7),_FmmC5ScgPtpInterfaceType_Type())
fmmC5ScgPtpInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC5ScgPtpInterfaceType.setStatus(_A)
_FmmC5ScgPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_FmmC5ScgPtpPmHistStatsEnable_Object=MibTableColumn
fmmC5ScgPtpPmHistStatsEnable=_FmmC5ScgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,8),_FmmC5ScgPtpPmHistStatsEnable_Type())
fmmC5ScgPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC5ScgPtpPmHistStatsEnable.setStatus(_A)
_FmmC5ScgPtpUsedFreqSlotList_Type=DisplayString
_FmmC5ScgPtpUsedFreqSlotList_Object=MibTableColumn
fmmC5ScgPtpUsedFreqSlotList=_FmmC5ScgPtpUsedFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,9),_FmmC5ScgPtpUsedFreqSlotList_Type())
fmmC5ScgPtpUsedFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpUsedFreqSlotList.setStatus(_A)
_FmmC5ScgPtpAvailableFreqSlotList_Type=DisplayString
_FmmC5ScgPtpAvailableFreqSlotList_Object=MibTableColumn
fmmC5ScgPtpAvailableFreqSlotList=_FmmC5ScgPtpAvailableFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,10),_FmmC5ScgPtpAvailableFreqSlotList_Type())
fmmC5ScgPtpAvailableFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpAvailableFreqSlotList.setStatus(_A)
_FmmC5ScgPtpAutoDiscSoakTime_Type=Integer32
_FmmC5ScgPtpAutoDiscSoakTime_Object=MibTableColumn
fmmC5ScgPtpAutoDiscSoakTime=_FmmC5ScgPtpAutoDiscSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,11),_FmmC5ScgPtpAutoDiscSoakTime_Type())
fmmC5ScgPtpAutoDiscSoakTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC5ScgPtpAutoDiscSoakTime.setStatus(_A)
_FmmC5ScgPtpTxPowerOffset_Type=FloatTenths
_FmmC5ScgPtpTxPowerOffset_Object=MibTableColumn
fmmC5ScgPtpTxPowerOffset=_FmmC5ScgPtpTxPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,12),_FmmC5ScgPtpTxPowerOffset_Type())
fmmC5ScgPtpTxPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC5ScgPtpTxPowerOffset.setStatus(_A)
_FmmC5ScgPtpAllowedPassBandList_Type=DisplayString
_FmmC5ScgPtpAllowedPassBandList_Object=MibTableColumn
fmmC5ScgPtpAllowedPassBandList=_FmmC5ScgPtpAllowedPassBandList_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,13),_FmmC5ScgPtpAllowedPassBandList_Type())
fmmC5ScgPtpAllowedPassBandList.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpAllowedPassBandList.setStatus(_A)
_FmmC5ScgPtpPassiveMirrorProvNeighborTP_Type=DisplayString
_FmmC5ScgPtpPassiveMirrorProvNeighborTP_Object=MibTableColumn
fmmC5ScgPtpPassiveMirrorProvNeighborTP=_FmmC5ScgPtpPassiveMirrorProvNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,14),_FmmC5ScgPtpPassiveMirrorProvNeighborTP_Type())
fmmC5ScgPtpPassiveMirrorProvNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC5ScgPtpPassiveMirrorProvNeighborTP.setStatus(_A)
_FmmC5ScgPtpRxPowerOffset_Type=FloatTenths
_FmmC5ScgPtpRxPowerOffset_Object=MibTableColumn
fmmC5ScgPtpRxPowerOffset=_FmmC5ScgPtpRxPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,63,1,1,15),_FmmC5ScgPtpRxPowerOffset_Type())
fmmC5ScgPtpRxPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC5ScgPtpRxPowerOffset.setStatus(_A)
_FmmC12ScgPtpTable_Object=MibTable
fmmC12ScgPtpTable=_FmmC12ScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2))
if mibBuilder.loadTexts:fmmC12ScgPtpTable.setStatus(_A)
_FmmC12ScgPtpEntry_Object=MibTableRow
fmmC12ScgPtpEntry=_FmmC12ScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1))
fmmC12ScgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fmmC12ScgPtpEntry.setStatus(_A)
_FmmC12ScgPtpScgNumber_Type=Integer32
_FmmC12ScgPtpScgNumber_Object=MibTableColumn
fmmC12ScgPtpScgNumber=_FmmC12ScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,1),_FmmC12ScgPtpScgNumber_Type())
fmmC12ScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpScgNumber.setStatus(_A)
_FmmC12ScgPtpScgSupEqptType_Type=InfnEqptType
_FmmC12ScgPtpScgSupEqptType_Object=MibTableColumn
fmmC12ScgPtpScgSupEqptType=_FmmC12ScgPtpScgSupEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,2),_FmmC12ScgPtpScgSupEqptType_Type())
fmmC12ScgPtpScgSupEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC12ScgPtpScgSupEqptType.setStatus(_A)
_FmmC12ScgPtpAutoDiscoveryState_Type=InfnAutoDiscoveryState
_FmmC12ScgPtpAutoDiscoveryState_Object=MibTableColumn
fmmC12ScgPtpAutoDiscoveryState=_FmmC12ScgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,3),_FmmC12ScgPtpAutoDiscoveryState_Type())
fmmC12ScgPtpAutoDiscoveryState.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpAutoDiscoveryState.setStatus(_A)
_FmmC12ScgPtpDiscoveredNeighborTP_Type=DisplayString
_FmmC12ScgPtpDiscoveredNeighborTP_Object=MibTableColumn
fmmC12ScgPtpDiscoveredNeighborTP=_FmmC12ScgPtpDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,4),_FmmC12ScgPtpDiscoveredNeighborTP_Type())
fmmC12ScgPtpDiscoveredNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpDiscoveredNeighborTP.setStatus(_A)
_FmmC12ScgPtpProvisionedNeighborTP_Type=DisplayString
_FmmC12ScgPtpProvisionedNeighborTP_Object=MibTableColumn
fmmC12ScgPtpProvisionedNeighborTP=_FmmC12ScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,5),_FmmC12ScgPtpProvisionedNeighborTP_Type())
fmmC12ScgPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpProvisionedNeighborTP.setStatus(_A)
_FmmC12ScgPtpProvisionedNeighborAdTpType_Type=InfnAdTpType
_FmmC12ScgPtpProvisionedNeighborAdTpType_Object=MibTableColumn
fmmC12ScgPtpProvisionedNeighborAdTpType=_FmmC12ScgPtpProvisionedNeighborAdTpType_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,6),_FmmC12ScgPtpProvisionedNeighborAdTpType_Type())
fmmC12ScgPtpProvisionedNeighborAdTpType.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpProvisionedNeighborAdTpType.setStatus(_A)
_FmmC12ScgPtpInterfaceType_Type=InfnWaveInterfaceType
_FmmC12ScgPtpInterfaceType_Object=MibTableColumn
fmmC12ScgPtpInterfaceType=_FmmC12ScgPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,7),_FmmC12ScgPtpInterfaceType_Type())
fmmC12ScgPtpInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC12ScgPtpInterfaceType.setStatus(_A)
_FmmC12ScgPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_FmmC12ScgPtpPmHistStatsEnable_Object=MibTableColumn
fmmC12ScgPtpPmHistStatsEnable=_FmmC12ScgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,8),_FmmC12ScgPtpPmHistStatsEnable_Type())
fmmC12ScgPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC12ScgPtpPmHistStatsEnable.setStatus(_A)
_FmmC12ScgPtpUsedFreqSlotList_Type=DisplayString
_FmmC12ScgPtpUsedFreqSlotList_Object=MibTableColumn
fmmC12ScgPtpUsedFreqSlotList=_FmmC12ScgPtpUsedFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,9),_FmmC12ScgPtpUsedFreqSlotList_Type())
fmmC12ScgPtpUsedFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpUsedFreqSlotList.setStatus(_A)
_FmmC12ScgPtpAvailableFreqSlotList_Type=DisplayString
_FmmC12ScgPtpAvailableFreqSlotList_Object=MibTableColumn
fmmC12ScgPtpAvailableFreqSlotList=_FmmC12ScgPtpAvailableFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,10),_FmmC12ScgPtpAvailableFreqSlotList_Type())
fmmC12ScgPtpAvailableFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpAvailableFreqSlotList.setStatus(_A)
_FmmC12ScgPtpAllowedPassBandList_Type=DisplayString
_FmmC12ScgPtpAllowedPassBandList_Object=MibTableColumn
fmmC12ScgPtpAllowedPassBandList=_FmmC12ScgPtpAllowedPassBandList_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,11),_FmmC12ScgPtpAllowedPassBandList_Type())
fmmC12ScgPtpAllowedPassBandList.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpAllowedPassBandList.setStatus(_A)
_FmmC12ScgPtpPassiveMirrorProvNeighborTP_Type=DisplayString
_FmmC12ScgPtpPassiveMirrorProvNeighborTP_Object=MibTableColumn
fmmC12ScgPtpPassiveMirrorProvNeighborTP=_FmmC12ScgPtpPassiveMirrorProvNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,12),_FmmC12ScgPtpPassiveMirrorProvNeighborTP_Type())
fmmC12ScgPtpPassiveMirrorProvNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmC12ScgPtpPassiveMirrorProvNeighborTP.setStatus(_A)
_FmmC12ScgPtpRxPowerOffset_Type=FloatTenths
_FmmC12ScgPtpRxPowerOffset_Object=MibTableColumn
fmmC12ScgPtpRxPowerOffset=_FmmC12ScgPtpRxPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,63,2,1,13),_FmmC12ScgPtpRxPowerOffset_Type())
fmmC12ScgPtpRxPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmC12ScgPtpRxPowerOffset.setStatus(_A)
_FmmCScgPtpConformance_ObjectIdentity=ObjectIdentity
fmmCScgPtpConformance=_FmmCScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,63,3))
_FmmCScgPtpCompliances_ObjectIdentity=ObjectIdentity
fmmCScgPtpCompliances=_FmmCScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,63,3,1))
_FmmCScgPtpGroups_ObjectIdentity=ObjectIdentity
fmmCScgPtpGroups=_FmmCScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,63,3,2))
fmmC5ScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,63,3,2,1))
fmmC5ScgPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:fmmC5ScgPtpGroup.setStatus(_A)
fmmC12ScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,63,3,2,2))
fmmC12ScgPtpGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:fmmC12ScgPtpGroup.setStatus(_A)
fmmCScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,63,3,1,1))
fmmCScgPtpCompliance.setObjects((_B,_h))
if mibBuilder.loadTexts:fmmCScgPtpCompliance.setStatus(_A)
fmmC12ScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,63,3,1,2))
fmmC12ScgPtpCompliance.setObjects((_B,_i))
if mibBuilder.loadTexts:fmmC12ScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmmCScgPtpMIB':fmmCScgPtpMIB,'fmmC5ScgPtpTable':fmmC5ScgPtpTable,'fmmC5ScgPtpEntry':fmmC5ScgPtpEntry,_G:fmmC5ScgPtpScgNumber,_H:fmmC5ScgPtpScgSupEqptType,_I:fmmC5ScgPtpAutoDiscoveryState,_J:fmmC5ScgPtpDiscoveredNeighborTP,_L:fmmC5ScgPtpProvisionedNeighborTP,_M:fmmC5ScgPtpProvisionedNeighborAdTpType,_K:fmmC5ScgPtpInterfaceType,_N:fmmC5ScgPtpPmHistStatsEnable,_O:fmmC5ScgPtpUsedFreqSlotList,_P:fmmC5ScgPtpAvailableFreqSlotList,_Q:fmmC5ScgPtpAutoDiscSoakTime,_R:fmmC5ScgPtpTxPowerOffset,_S:fmmC5ScgPtpAllowedPassBandList,_T:fmmC5ScgPtpPassiveMirrorProvNeighborTP,_U:fmmC5ScgPtpRxPowerOffset,'fmmC12ScgPtpTable':fmmC12ScgPtpTable,'fmmC12ScgPtpEntry':fmmC12ScgPtpEntry,_V:fmmC12ScgPtpScgNumber,_W:fmmC12ScgPtpScgSupEqptType,_X:fmmC12ScgPtpAutoDiscoveryState,_Y:fmmC12ScgPtpDiscoveredNeighborTP,_a:fmmC12ScgPtpProvisionedNeighborTP,_b:fmmC12ScgPtpProvisionedNeighborAdTpType,_Z:fmmC12ScgPtpInterfaceType,_c:fmmC12ScgPtpPmHistStatsEnable,_d:fmmC12ScgPtpUsedFreqSlotList,_e:fmmC12ScgPtpAvailableFreqSlotList,'fmmC12ScgPtpAllowedPassBandList':fmmC12ScgPtpAllowedPassBandList,_f:fmmC12ScgPtpPassiveMirrorProvNeighborTP,_g:fmmC12ScgPtpRxPowerOffset,'fmmCScgPtpConformance':fmmCScgPtpConformance,'fmmCScgPtpCompliances':fmmCScgPtpCompliances,'fmmCScgPtpCompliance':fmmCScgPtpCompliance,'fmmC12ScgPtpCompliance':fmmC12ScgPtpCompliance,'fmmCScgPtpGroups':fmmCScgPtpGroups,_h:fmmC5ScgPtpGroup,_i:fmmC12ScgPtpGroup})