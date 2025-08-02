_A4='atmNteVcAlarmVci'
_A3='atmNteVcAlarmVpi'
_A2='atmNteVpAlarmVpi'
_A1='ds0Bundle'
_A0='bridgePort'
_z='notConnected'
_y='upStream'
_x='downStream'
_w='endToEndAisAndRdi'
_v='endToEndRdi'
_u='endToEndAis'
_t='segmentAisAndRdi'
_s='segmentRdi'
_r='segmentAis'
_q='conflict'
_p='denied'
_o='timeout'
_n='initial'
_m='intermediate'
_l='endToEndLlid'
_k='segmentLlid'
_j='endToEnd'
_i='segment'
_h='originateActivationCells'
_g='listenToActivationCells'
_f='policingAndShaping'
_e='shaping'
_d='monitor'
_c='police'
_b='enable'
_a='external'
_Z='internal'
_Y='atmVplVpi'
_X='atmVclVpi'
_W='atmVclVci'
_V='manual'
_U='none'
_T='off'
_S='disabled'
_R='endToEndTermination'
_Q='segmentTermination'
_P='disable'
_O='OctetString'
_N='RAD-NtePrtCo-MIB'
_M='both'
_L='notApplicable'
_K='ATM-MIB'
_J='down'
_I='up'
_H='sink'
_G='source'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclVci,atmVclVpi,atmVplVpi=mibBuilder.importSymbols(_K,_W,_X,_Y)
ifIndex,=mibBuilder.importSymbols(_E,_F)
rad,=mibBuilder.importSymbols('RAD-SMI-MIB','rad')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
radAtm=ModuleIdentity((1,3,6,1,4,1,164,12))
_AtmNte_ObjectIdentity=ObjectIdentity
atmNte=_AtmNte_ObjectIdentity((1,3,6,1,4,1,164,12,3))
_AtmNteEvents_ObjectIdentity=ObjectIdentity
atmNteEvents=_AtmNteEvents_ObjectIdentity((1,3,6,1,4,1,164,12,3,0))
if mibBuilder.loadTexts:atmNteEvents.setStatus(_A)
_AtmNtePrt_ObjectIdentity=ObjectIdentity
atmNtePrt=_AtmNtePrt_ObjectIdentity((1,3,6,1,4,1,164,12,3,2))
_AtmNtePrtConfig_ObjectIdentity=ObjectIdentity
atmNtePrtConfig=_AtmNtePrtConfig_ObjectIdentity((1,3,6,1,4,1,164,12,3,2,1))
_AtmNteConfIfTable_Object=MibTable
atmNteConfIfTable=_AtmNteConfIfTable_Object((1,3,6,1,4,1,164,12,3,2,1,1))
if mibBuilder.loadTexts:atmNteConfIfTable.setStatus(_A)
_AtmNteConfIfEntry_Object=MibTableRow
atmNteConfIfEntry=_AtmNteConfIfEntry_Object((1,3,6,1,4,1,164,12,3,2,1,1,1))
atmNteConfIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:atmNteConfIfEntry.setStatus(_A)
class _AtmConfIfTransmitClk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_Z,2),(_a,3),('loopback',4),('adaptive',5)))
_AtmConfIfTransmitClk_Type.__name__=_C
_AtmConfIfTransmitClk_Object=MibTableColumn
atmConfIfTransmitClk=_AtmConfIfTransmitClk_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,1),_AtmConfIfTransmitClk_Type())
atmConfIfTransmitClk.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfTransmitClk.setStatus(_A)
class _AtmConfIfLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_Z,2),(_a,3),(_P,4)))
_AtmConfIfLoopback_Type.__name__=_C
_AtmConfIfLoopback_Object=MibTableColumn
atmConfIfLoopback=_AtmConfIfLoopback_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,2),_AtmConfIfLoopback_Type())
atmConfIfLoopback.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfLoopback.setStatus(_A)
class _AtmConfIfFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),('sonet',2),('sdh',3),('direct',4),('plcpInternal',5),('plcpExternal',6),('e3',7),('ethCrcTrans',8),('ethCrcNotTrans',9),('directNoScrmbling',10),('plcpInternalNoScrmbling',11),('plcpExternalNoScrmbling',12)))
_AtmConfIfFrameType_Type.__name__=_C
_AtmConfIfFrameType_Object=MibTableColumn
atmConfIfFrameType=_AtmConfIfFrameType_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,3),_AtmConfIfFrameType_Type())
atmConfIfFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfFrameType.setStatus(_A)
class _AtmConfIfCardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_L,1),('sc13m-155',2),('st13s-155',3),('st13l-155',4),('utp-155',5),('cx-bnc-155',6),('e3',7),('t3',8),('e1',9),('e1-ltu',10),('fc13l-155',11),('fc13lh-155',12),('fc15lh-155',13),('fc13l-e3',14),('fc13lh-e3',15),('fc15lh-e3',16),('fc13l-t3',17),('fc13lh-t3',18),('fc15lh-t3',19)))
_AtmConfIfCardType_Type.__name__=_C
_AtmConfIfCardType_Object=MibTableColumn
atmConfIfCardType=_AtmConfIfCardType_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,4),_AtmConfIfCardType_Type())
atmConfIfCardType.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfIfCardType.setStatus('deprecated')
class _AtmConfAtmIfVpiVciLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('bits15',2),('bits17',3)))
_AtmConfAtmIfVpiVciLimit_Type.__name__=_C
_AtmConfAtmIfVpiVciLimit_Object=MibTableColumn
atmConfAtmIfVpiVciLimit=_AtmConfAtmIfVpiVciLimit_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,5),_AtmConfAtmIfVpiVciLimit_Type())
atmConfAtmIfVpiVciLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfAtmIfVpiVciLimit.setStatus(_A)
class _AtmConfIfHwFeatures_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_b,2)))
_AtmConfIfHwFeatures_Type.__name__=_C
_AtmConfIfHwFeatures_Object=MibTableColumn
atmConfIfHwFeatures=_AtmConfIfHwFeatures_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,6),_AtmConfIfHwFeatures_Type())
atmConfIfHwFeatures.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfHwFeatures.setStatus(_A)
_AtmConfIfOutputRate_Type=Integer32
_AtmConfIfOutputRate_Object=MibTableColumn
atmConfIfOutputRate=_AtmConfIfOutputRate_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,7),_AtmConfIfOutputRate_Type())
atmConfIfOutputRate.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfOutputRate.setStatus(_A)
_AtmConfIfInputRate_Type=Integer32
_AtmConfIfInputRate_Object=MibTableColumn
atmConfIfInputRate=_AtmConfIfInputRate_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,8),_AtmConfIfInputRate_Type())
atmConfIfInputRate.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfInputRate.setStatus(_A)
class _AtmConfAlarmForwarding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_P,2),(_b,3)))
_AtmConfAlarmForwarding_Type.__name__=_C
_AtmConfAlarmForwarding_Object=MibTableColumn
atmConfAlarmForwarding=_AtmConfAlarmForwarding_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,9),_AtmConfAlarmForwarding_Type())
atmConfAlarmForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfAlarmForwarding.setStatus(_A)
_AtmConfIfAllocatedBw_Type=Integer32
_AtmConfIfAllocatedBw_Object=MibTableColumn
atmConfIfAllocatedBw=_AtmConfIfAllocatedBw_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,10),_AtmConfIfAllocatedBw_Type())
atmConfIfAllocatedBw.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfIfAllocatedBw.setStatus(_A)
_AtmConfIfLowerVpi_Type=Integer32
_AtmConfIfLowerVpi_Object=MibTableColumn
atmConfIfLowerVpi=_AtmConfIfLowerVpi_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,11),_AtmConfIfLowerVpi_Type())
atmConfIfLowerVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfLowerVpi.setStatus(_A)
class _AtmConfIfOamMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_Q,2),(_R,3)))
_AtmConfIfOamMode_Type.__name__=_C
_AtmConfIfOamMode_Object=MibTableColumn
atmConfIfOamMode=_AtmConfIfOamMode_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,12),_AtmConfIfOamMode_Type())
atmConfIfOamMode.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfOamMode.setStatus(_A)
class _AtmConfIfOamFailureInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_S,2),('ais',3),('rdi',4),('aisAndRdi',5)))
_AtmConfIfOamFailureInd_Type.__name__=_C
_AtmConfIfOamFailureInd_Object=MibTableColumn
atmConfIfOamFailureInd=_AtmConfIfOamFailureInd_Object((1,3,6,1,4,1,164,12,3,2,1,1,1,13),_AtmConfIfOamFailureInd_Type())
atmConfIfOamFailureInd.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfIfOamFailureInd.setStatus(_A)
_AtmNteAlarmIfTable_Object=MibTable
atmNteAlarmIfTable=_AtmNteAlarmIfTable_Object((1,3,6,1,4,1,164,12,3,2,1,2))
if mibBuilder.loadTexts:atmNteAlarmIfTable.setStatus(_A)
_AtmNteAlarmIfEntry_Object=MibTableRow
atmNteAlarmIfEntry=_AtmNteAlarmIfEntry_Object((1,3,6,1,4,1,164,12,3,2,1,2,1))
atmNteAlarmIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:atmNteAlarmIfEntry.setStatus(_A)
_AtmInterfaceActiveAlarms_Type=Integer32
_AtmInterfaceActiveAlarms_Object=MibTableColumn
atmInterfaceActiveAlarms=_AtmInterfaceActiveAlarms_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,1),_AtmInterfaceActiveAlarms_Type())
atmInterfaceActiveAlarms.setMaxAccess(_D)
if mibBuilder.loadTexts:atmInterfaceActiveAlarms.setStatus(_A)
_AtmThresholdSectionBIP_Type=Integer32
_AtmThresholdSectionBIP_Object=MibTableColumn
atmThresholdSectionBIP=_AtmThresholdSectionBIP_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,2),_AtmThresholdSectionBIP_Type())
atmThresholdSectionBIP.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdSectionBIP.setStatus(_A)
_AtmThresholdLineBIP_Type=Integer32
_AtmThresholdLineBIP_Object=MibTableColumn
atmThresholdLineBIP=_AtmThresholdLineBIP_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,3),_AtmThresholdLineBIP_Type())
atmThresholdLineBIP.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdLineBIP.setStatus(_A)
_AtmThresholdLineFEBE_Type=Integer32
_AtmThresholdLineFEBE_Object=MibTableColumn
atmThresholdLineFEBE=_AtmThresholdLineFEBE_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,4),_AtmThresholdLineFEBE_Type())
atmThresholdLineFEBE.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdLineFEBE.setStatus(_A)
_AtmThresholdPathBIP_Type=Integer32
_AtmThresholdPathBIP_Object=MibTableColumn
atmThresholdPathBIP=_AtmThresholdPathBIP_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,5),_AtmThresholdPathBIP_Type())
atmThresholdPathBIP.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdPathBIP.setStatus(_A)
_AtmThresholdPathFEBE_Type=Integer32
_AtmThresholdPathFEBE_Object=MibTableColumn
atmThresholdPathFEBE=_AtmThresholdPathFEBE_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,6),_AtmThresholdPathFEBE_Type())
atmThresholdPathFEBE.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdPathFEBE.setStatus(_A)
_AtmThresholdErroredCells_Type=Integer32
_AtmThresholdErroredCells_Object=MibTableColumn
atmThresholdErroredCells=_AtmThresholdErroredCells_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,7),_AtmThresholdErroredCells_Type())
atmThresholdErroredCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdErroredCells.setStatus(_A)
_AtmThresholdLostCells_Type=Integer32
_AtmThresholdLostCells_Object=MibTableColumn
atmThresholdLostCells=_AtmThresholdLostCells_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,8),_AtmThresholdLostCells_Type())
atmThresholdLostCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdLostCells.setStatus(_A)
_AtmThresholdMisinsertedCells_Type=Integer32
_AtmThresholdMisinsertedCells_Object=MibTableColumn
atmThresholdMisinsertedCells=_AtmThresholdMisinsertedCells_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,9),_AtmThresholdMisinsertedCells_Type())
atmThresholdMisinsertedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:atmThresholdMisinsertedCells.setStatus(_A)
class _AtmInterfaceAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_T,2),('on',3)))
_AtmInterfaceAlarmStatus_Type.__name__=_C
_AtmInterfaceAlarmStatus_Object=MibTableColumn
atmInterfaceAlarmStatus=_AtmInterfaceAlarmStatus_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,10),_AtmInterfaceAlarmStatus_Type())
atmInterfaceAlarmStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmInterfaceAlarmStatus.setStatus(_A)
_AtmInterfaceMaskAlarms_Type=Integer32
_AtmInterfaceMaskAlarms_Object=MibTableColumn
atmInterfaceMaskAlarms=_AtmInterfaceMaskAlarms_Object((1,3,6,1,4,1,164,12,3,2,1,2,1,11),_AtmInterfaceMaskAlarms_Type())
atmInterfaceMaskAlarms.setMaxAccess(_B)
if mibBuilder.loadTexts:atmInterfaceMaskAlarms.setStatus(_A)
_AtmNteConfVpTable_Object=MibTable
atmNteConfVpTable=_AtmNteConfVpTable_Object((1,3,6,1,4,1,164,12,3,2,1,3))
if mibBuilder.loadTexts:atmNteConfVpTable.setStatus(_A)
_AtmNteConfVpEntry_Object=MibTableRow
atmNteConfVpEntry=_AtmNteConfVpEntry_Object((1,3,6,1,4,1,164,12,3,2,1,3,1))
atmNteConfVpEntry.setIndexNames((0,_E,_F),(0,_K,_Y))
if mibBuilder.loadTexts:atmNteConfVpEntry.setStatus(_A)
class _AtmConfVpPolicing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_U,1),(_c,2),(_d,3),(_e,4),(_f,5)))
_AtmConfVpPolicing_Type.__name__=_C
_AtmConfVpPolicing_Object=MibTableColumn
atmConfVpPolicing=_AtmConfVpPolicing_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,1),_AtmConfVpPolicing_Type())
atmConfVpPolicing.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpPolicing.setStatus(_A)
class _AtmConfVpCCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_I,2),(_J,3),(_G,4),(_H,5),(_g,6),(_h,7)))
_AtmConfVpCCAdminStatus_Type.__name__=_C
_AtmConfVpCCAdminStatus_Object=MibTableColumn
atmConfVpCCAdminStatus=_AtmConfVpCCAdminStatus_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,2),_AtmConfVpCCAdminStatus_Type())
atmConfVpCCAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpCCAdminStatus.setStatus(_A)
class _AtmConfVpLoopbackAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,2),(_J,3),('llid',4),(_i,5),(_j,6),(_k,7),(_l,8)))
_AtmConfVpLoopbackAdminStatus_Type.__name__=_C
_AtmConfVpLoopbackAdminStatus_Object=MibTableColumn
atmConfVpLoopbackAdminStatus=_AtmConfVpLoopbackAdminStatus_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,3),_AtmConfVpLoopbackAdminStatus_Type())
atmConfVpLoopbackAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpLoopbackAdminStatus.setStatus(_A)
class _AtmConfVpLoopbackSinkAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_AtmConfVpLoopbackSinkAddress_Type.__name__=_O
_AtmConfVpLoopbackSinkAddress_Object=MibTableColumn
atmConfVpLoopbackSinkAddress=_AtmConfVpLoopbackSinkAddress_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,4),_AtmConfVpLoopbackSinkAddress_Type())
atmConfVpLoopbackSinkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpLoopbackSinkAddress.setStatus(_A)
_AtmConfVpCongestionControl_Type=OctetString
_AtmConfVpCongestionControl_Object=MibTableColumn
atmConfVpCongestionControl=_AtmConfVpCongestionControl_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,5),_AtmConfVpCongestionControl_Type())
atmConfVpCongestionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpCongestionControl.setStatus(_A)
class _AtmConfVpCCDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,5)));namedValues=NamedValues(*((_M,2),(_G,4),(_H,5)))
_AtmConfVpCCDirection_Type.__name__=_C
_AtmConfVpCCDirection_Object=MibTableColumn
atmConfVpCCDirection=_AtmConfVpCCDirection_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,6),_AtmConfVpCCDirection_Type())
atmConfVpCCDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpCCDirection.setStatus(_A)
_AtmConfVpCreationTime_Type=DateAndTime
_AtmConfVpCreationTime_Object=MibTableColumn
atmConfVpCreationTime=_AtmConfVpCreationTime_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,7),_AtmConfVpCreationTime_Type())
atmConfVpCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfVpCreationTime.setStatus(_A)
class _AtmConfVpOamSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_m,1),(_Q,2),(_R,3)))
_AtmConfVpOamSupport_Type.__name__=_C
_AtmConfVpOamSupport_Object=MibTableColumn
atmConfVpOamSupport=_AtmConfVpOamSupport_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,8),_AtmConfVpOamSupport_Type())
atmConfVpOamSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpOamSupport.setStatus(_A)
class _AtmConfVpCCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,5,8,9,10,11,12)));namedValues=NamedValues(*((_n,1),(_G,4),(_H,5),(_M,8),(_o,9),(_p,10),(_q,11),(_V,12)))
_AtmConfVpCCOperStatus_Type.__name__=_C
_AtmConfVpCCOperStatus_Object=MibTableColumn
atmConfVpCCOperStatus=_AtmConfVpCCOperStatus_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,9),_AtmConfVpCCOperStatus_Type())
atmConfVpCCOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfVpCCOperStatus.setStatus(_A)
class _AtmConfVpLoopbackTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_T,2),('on',3)))
_AtmConfVpLoopbackTraffic_Type.__name__=_C
_AtmConfVpLoopbackTraffic_Object=MibTableColumn
atmConfVpLoopbackTraffic=_AtmConfVpLoopbackTraffic_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,10),_AtmConfVpLoopbackTraffic_Type())
atmConfVpLoopbackTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpLoopbackTraffic.setStatus(_A)
class _AtmConfVpLoopbackFailureInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7),(_w,8)))
_AtmConfVpLoopbackFailureInd_Type.__name__=_C
_AtmConfVpLoopbackFailureInd_Object=MibTableColumn
atmConfVpLoopbackFailureInd=_AtmConfVpLoopbackFailureInd_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,11),_AtmConfVpLoopbackFailureInd_Type())
atmConfVpLoopbackFailureInd.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpLoopbackFailureInd.setStatus(_A)
_AtmConfVpLoopbackFailureThreshold_Type=Integer32
_AtmConfVpLoopbackFailureThreshold_Object=MibTableColumn
atmConfVpLoopbackFailureThreshold=_AtmConfVpLoopbackFailureThreshold_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,12),_AtmConfVpLoopbackFailureThreshold_Type())
atmConfVpLoopbackFailureThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpLoopbackFailureThreshold.setStatus(_A)
class _AtmConfVpOamDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_x,2),(_y,3)))
_AtmConfVpOamDirection_Type.__name__=_C
_AtmConfVpOamDirection_Object=MibTableColumn
atmConfVpOamDirection=_AtmConfVpOamDirection_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,13),_AtmConfVpOamDirection_Type())
atmConfVpOamDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpOamDirection.setStatus(_A)
_AtmConfVpOamDescrIndex_Type=Integer32
_AtmConfVpOamDescrIndex_Object=MibTableColumn
atmConfVpOamDescrIndex=_AtmConfVpOamDescrIndex_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,14),_AtmConfVpOamDescrIndex_Type())
atmConfVpOamDescrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpOamDescrIndex.setStatus(_A)
class _AtmConfVpConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_z,1),('mng',2),(_A0,3),(_A1,4),('atm',5),('pw',6)))
_AtmConfVpConnected_Type.__name__=_C
_AtmConfVpConnected_Object=MibTableColumn
atmConfVpConnected=_AtmConfVpConnected_Object((1,3,6,1,4,1,164,12,3,2,1,3,1,15),_AtmConfVpConnected_Type())
atmConfVpConnected.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVpConnected.setStatus(_A)
_AtmNteConfVcTable_Object=MibTable
atmNteConfVcTable=_AtmNteConfVcTable_Object((1,3,6,1,4,1,164,12,3,2,1,4))
if mibBuilder.loadTexts:atmNteConfVcTable.setStatus(_A)
_AtmNteConfVcEntry_Object=MibTableRow
atmNteConfVcEntry=_AtmNteConfVcEntry_Object((1,3,6,1,4,1,164,12,3,2,1,4,1))
atmNteConfVcEntry.setIndexNames((0,_E,_F),(0,_K,_X),(0,_K,_W))
if mibBuilder.loadTexts:atmNteConfVcEntry.setStatus(_A)
class _AtmConfVcPolicing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,255)));namedValues=NamedValues(*((_U,1),(_c,2),(_d,3),(_e,4),(_f,5),(_L,255)))
_AtmConfVcPolicing_Type.__name__=_C
_AtmConfVcPolicing_Object=MibTableColumn
atmConfVcPolicing=_AtmConfVcPolicing_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,1),_AtmConfVcPolicing_Type())
atmConfVcPolicing.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcPolicing.setStatus(_A)
class _AtmConfVcCCAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7)));namedValues=NamedValues(*((_I,2),(_J,3),(_G,4),(_H,5),(_g,6),(_h,7)))
_AtmConfVcCCAdminStatus_Type.__name__=_C
_AtmConfVcCCAdminStatus_Object=MibTableColumn
atmConfVcCCAdminStatus=_AtmConfVcCCAdminStatus_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,2),_AtmConfVcCCAdminStatus_Type())
atmConfVcCCAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcCCAdminStatus.setStatus(_A)
class _AtmConfVcLoopbackAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8)));namedValues=NamedValues(*((_I,2),(_J,3),('llid',4),(_i,5),(_j,6),(_k,7),(_l,8)))
_AtmConfVcLoopbackAdminStatus_Type.__name__=_C
_AtmConfVcLoopbackAdminStatus_Object=MibTableColumn
atmConfVcLoopbackAdminStatus=_AtmConfVcLoopbackAdminStatus_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,3),_AtmConfVcLoopbackAdminStatus_Type())
atmConfVcLoopbackAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcLoopbackAdminStatus.setStatus(_A)
class _AtmConfVcLoopbackSinkAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,20))
_AtmConfVcLoopbackSinkAddress_Type.__name__=_O
_AtmConfVcLoopbackSinkAddress_Object=MibTableColumn
atmConfVcLoopbackSinkAddress=_AtmConfVcLoopbackSinkAddress_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,4),_AtmConfVcLoopbackSinkAddress_Type())
atmConfVcLoopbackSinkAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcLoopbackSinkAddress.setStatus(_A)
_AtmConfVcCongestionControl_Type=OctetString
_AtmConfVcCongestionControl_Object=MibTableColumn
atmConfVcCongestionControl=_AtmConfVcCongestionControl_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,5),_AtmConfVcCongestionControl_Type())
atmConfVcCongestionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcCongestionControl.setStatus(_A)
class _AtmConfVcCCDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5)));namedValues=NamedValues(*((_M,2),(_U,3),(_G,4),(_H,5)))
_AtmConfVcCCDirection_Type.__name__=_C
_AtmConfVcCCDirection_Object=MibTableColumn
atmConfVcCCDirection=_AtmConfVcCCDirection_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,6),_AtmConfVcCCDirection_Type())
atmConfVcCCDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcCCDirection.setStatus(_A)
_AtmConfVcCreationTime_Type=DateAndTime
_AtmConfVcCreationTime_Object=MibTableColumn
atmConfVcCreationTime=_AtmConfVcCreationTime_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,7),_AtmConfVcCreationTime_Type())
atmConfVcCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfVcCreationTime.setStatus(_A)
class _AtmConfVcOamSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_m,1),(_Q,2),(_R,3),('endToEndAndSegment',4)))
_AtmConfVcOamSupport_Type.__name__=_C
_AtmConfVcOamSupport_Object=MibTableColumn
atmConfVcOamSupport=_AtmConfVcOamSupport_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,8),_AtmConfVcOamSupport_Type())
atmConfVcOamSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcOamSupport.setStatus(_A)
class _AtmConfVcCCActivationCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_V,1),('activator',2),('listener',3)))
_AtmConfVcCCActivationCtrl_Type.__name__=_C
_AtmConfVcCCActivationCtrl_Object=MibTableColumn
atmConfVcCCActivationCtrl=_AtmConfVcCCActivationCtrl_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,9),_AtmConfVcCCActivationCtrl_Type())
atmConfVcCCActivationCtrl.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcCCActivationCtrl.setStatus(_A)
class _AtmConfVcCCOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,8,9,10,11,12)));namedValues=NamedValues(*((_n,1),(_I,2),(_J,3),(_G,4),(_H,5),(_M,8),(_o,9),(_p,10),(_q,11),(_V,12)))
_AtmConfVcCCOperStatus_Type.__name__=_C
_AtmConfVcCCOperStatus_Object=MibTableColumn
atmConfVcCCOperStatus=_AtmConfVcCCOperStatus_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,10),_AtmConfVcCCOperStatus_Type())
atmConfVcCCOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfVcCCOperStatus.setStatus(_A)
class _AtmConfVcLoopbackTraffic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_T,2),('on',3)))
_AtmConfVcLoopbackTraffic_Type.__name__=_C
_AtmConfVcLoopbackTraffic_Object=MibTableColumn
atmConfVcLoopbackTraffic=_AtmConfVcLoopbackTraffic_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,11),_AtmConfVcLoopbackTraffic_Type())
atmConfVcLoopbackTraffic.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcLoopbackTraffic.setStatus(_A)
class _AtmConfVcLoopbackFailureInd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,2),(_r,3),(_s,4),(_t,5),(_u,6),(_v,7),(_w,8)))
_AtmConfVcLoopbackFailureInd_Type.__name__=_C
_AtmConfVcLoopbackFailureInd_Object=MibTableColumn
atmConfVcLoopbackFailureInd=_AtmConfVcLoopbackFailureInd_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,12),_AtmConfVcLoopbackFailureInd_Type())
atmConfVcLoopbackFailureInd.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcLoopbackFailureInd.setStatus(_A)
_AtmConfVcLoopbackFailureThreshold_Type=Integer32
_AtmConfVcLoopbackFailureThreshold_Object=MibTableColumn
atmConfVcLoopbackFailureThreshold=_AtmConfVcLoopbackFailureThreshold_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,13),_AtmConfVcLoopbackFailureThreshold_Type())
atmConfVcLoopbackFailureThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcLoopbackFailureThreshold.setStatus(_A)
class _AtmConfVcOamDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_x,2),(_y,3)))
_AtmConfVcOamDirection_Type.__name__=_C
_AtmConfVcOamDirection_Object=MibTableColumn
atmConfVcOamDirection=_AtmConfVcOamDirection_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,14),_AtmConfVcOamDirection_Type())
atmConfVcOamDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcOamDirection.setStatus(_A)
_AtmConfVcName_Type=DisplayString
_AtmConfVcName_Object=MibTableColumn
atmConfVcName=_AtmConfVcName_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,15),_AtmConfVcName_Type())
atmConfVcName.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcName.setStatus(_A)
class _AtmConfVcConnected_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_z,1),('mng',2),(_A0,3),(_A1,4),('atm',5),('pw',6),('routerInterface',7),('qos',8),('other',9),('logicalMac',10),('atmAal2',11)))
_AtmConfVcConnected_Type.__name__=_C
_AtmConfVcConnected_Object=MibTableColumn
atmConfVcConnected=_AtmConfVcConnected_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,16),_AtmConfVcConnected_Type())
atmConfVcConnected.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcConnected.setStatus(_A)
_AtmConfVcOamDescrIndex_Type=Integer32
_AtmConfVcOamDescrIndex_Object=MibTableColumn
atmConfVcOamDescrIndex=_AtmConfVcOamDescrIndex_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,17),_AtmConfVcOamDescrIndex_Type())
atmConfVcOamDescrIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atmConfVcOamDescrIndex.setStatus(_A)
_AtmConfVcNoOfUsages_Type=Unsigned32
_AtmConfVcNoOfUsages_Object=MibTableColumn
atmConfVcNoOfUsages=_AtmConfVcNoOfUsages_Object((1,3,6,1,4,1,164,12,3,2,1,4,1,18),_AtmConfVcNoOfUsages_Type())
atmConfVcNoOfUsages.setMaxAccess(_D)
if mibBuilder.loadTexts:atmConfVcNoOfUsages.setStatus(_A)
_AtmNteAlarmVpTable_Object=MibTable
atmNteAlarmVpTable=_AtmNteAlarmVpTable_Object((1,3,6,1,4,1,164,12,3,2,1,5))
if mibBuilder.loadTexts:atmNteAlarmVpTable.setStatus(_A)
_AtmNteAlarmVpEntry_Object=MibTableRow
atmNteAlarmVpEntry=_AtmNteAlarmVpEntry_Object((1,3,6,1,4,1,164,12,3,2,1,5,1))
atmNteAlarmVpEntry.setIndexNames((0,_E,_F),(0,_N,_A2))
if mibBuilder.loadTexts:atmNteAlarmVpEntry.setStatus(_A)
_AtmNteVpAlarmVpi_Type=Integer32
_AtmNteVpAlarmVpi_Object=MibTableColumn
atmNteVpAlarmVpi=_AtmNteVpAlarmVpi_Object((1,3,6,1,4,1,164,12,3,2,1,5,1,1),_AtmNteVpAlarmVpi_Type())
atmNteVpAlarmVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:atmNteVpAlarmVpi.setStatus(_A)
_AtmNteVpActiveAlarms_Type=Integer32
_AtmNteVpActiveAlarms_Object=MibTableColumn
atmNteVpActiveAlarms=_AtmNteVpActiveAlarms_Object((1,3,6,1,4,1,164,12,3,2,1,5,1,2),_AtmNteVpActiveAlarms_Type())
atmNteVpActiveAlarms.setMaxAccess(_D)
if mibBuilder.loadTexts:atmNteVpActiveAlarms.setStatus(_A)
_AtmNteAlarmVcTable_Object=MibTable
atmNteAlarmVcTable=_AtmNteAlarmVcTable_Object((1,3,6,1,4,1,164,12,3,2,1,6))
if mibBuilder.loadTexts:atmNteAlarmVcTable.setStatus(_A)
_AtmNteAlarmVcEntry_Object=MibTableRow
atmNteAlarmVcEntry=_AtmNteAlarmVcEntry_Object((1,3,6,1,4,1,164,12,3,2,1,6,1))
atmNteAlarmVcEntry.setIndexNames((0,_E,_F),(0,_N,_A3),(0,_N,_A4))
if mibBuilder.loadTexts:atmNteAlarmVcEntry.setStatus(_A)
_AtmNteVcAlarmVpi_Type=Integer32
_AtmNteVcAlarmVpi_Object=MibTableColumn
atmNteVcAlarmVpi=_AtmNteVcAlarmVpi_Object((1,3,6,1,4,1,164,12,3,2,1,6,1,1),_AtmNteVcAlarmVpi_Type())
atmNteVcAlarmVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:atmNteVcAlarmVpi.setStatus(_A)
_AtmNteVcAlarmVci_Type=Integer32
_AtmNteVcAlarmVci_Object=MibTableColumn
atmNteVcAlarmVci=_AtmNteVcAlarmVci_Object((1,3,6,1,4,1,164,12,3,2,1,6,1,2),_AtmNteVcAlarmVci_Type())
atmNteVcAlarmVci.setMaxAccess(_D)
if mibBuilder.loadTexts:atmNteVcAlarmVci.setStatus(_A)
_AtmNteVcActiveAlarms_Type=Integer32
_AtmNteVcActiveAlarms_Object=MibTableColumn
atmNteVcActiveAlarms=_AtmNteVcActiveAlarms_Object((1,3,6,1,4,1,164,12,3,2,1,6,1,3),_AtmNteVcActiveAlarms_Type())
atmNteVcActiveAlarms.setMaxAccess(_D)
if mibBuilder.loadTexts:atmNteVcActiveAlarms.setStatus(_A)
mibBuilder.exportSymbols(_N,**{'radAtm':radAtm,'atmNte':atmNte,'atmNteEvents':atmNteEvents,'atmNtePrt':atmNtePrt,'atmNtePrtConfig':atmNtePrtConfig,'atmNteConfIfTable':atmNteConfIfTable,'atmNteConfIfEntry':atmNteConfIfEntry,'atmConfIfTransmitClk':atmConfIfTransmitClk,'atmConfIfLoopback':atmConfIfLoopback,'atmConfIfFrameType':atmConfIfFrameType,'atmConfIfCardType':atmConfIfCardType,'atmConfAtmIfVpiVciLimit':atmConfAtmIfVpiVciLimit,'atmConfIfHwFeatures':atmConfIfHwFeatures,'atmConfIfOutputRate':atmConfIfOutputRate,'atmConfIfInputRate':atmConfIfInputRate,'atmConfAlarmForwarding':atmConfAlarmForwarding,'atmConfIfAllocatedBw':atmConfIfAllocatedBw,'atmConfIfLowerVpi':atmConfIfLowerVpi,'atmConfIfOamMode':atmConfIfOamMode,'atmConfIfOamFailureInd':atmConfIfOamFailureInd,'atmNteAlarmIfTable':atmNteAlarmIfTable,'atmNteAlarmIfEntry':atmNteAlarmIfEntry,'atmInterfaceActiveAlarms':atmInterfaceActiveAlarms,'atmThresholdSectionBIP':atmThresholdSectionBIP,'atmThresholdLineBIP':atmThresholdLineBIP,'atmThresholdLineFEBE':atmThresholdLineFEBE,'atmThresholdPathBIP':atmThresholdPathBIP,'atmThresholdPathFEBE':atmThresholdPathFEBE,'atmThresholdErroredCells':atmThresholdErroredCells,'atmThresholdLostCells':atmThresholdLostCells,'atmThresholdMisinsertedCells':atmThresholdMisinsertedCells,'atmInterfaceAlarmStatus':atmInterfaceAlarmStatus,'atmInterfaceMaskAlarms':atmInterfaceMaskAlarms,'atmNteConfVpTable':atmNteConfVpTable,'atmNteConfVpEntry':atmNteConfVpEntry,'atmConfVpPolicing':atmConfVpPolicing,'atmConfVpCCAdminStatus':atmConfVpCCAdminStatus,'atmConfVpLoopbackAdminStatus':atmConfVpLoopbackAdminStatus,'atmConfVpLoopbackSinkAddress':atmConfVpLoopbackSinkAddress,'atmConfVpCongestionControl':atmConfVpCongestionControl,'atmConfVpCCDirection':atmConfVpCCDirection,'atmConfVpCreationTime':atmConfVpCreationTime,'atmConfVpOamSupport':atmConfVpOamSupport,'atmConfVpCCOperStatus':atmConfVpCCOperStatus,'atmConfVpLoopbackTraffic':atmConfVpLoopbackTraffic,'atmConfVpLoopbackFailureInd':atmConfVpLoopbackFailureInd,'atmConfVpLoopbackFailureThreshold':atmConfVpLoopbackFailureThreshold,'atmConfVpOamDirection':atmConfVpOamDirection,'atmConfVpOamDescrIndex':atmConfVpOamDescrIndex,'atmConfVpConnected':atmConfVpConnected,'atmNteConfVcTable':atmNteConfVcTable,'atmNteConfVcEntry':atmNteConfVcEntry,'atmConfVcPolicing':atmConfVcPolicing,'atmConfVcCCAdminStatus':atmConfVcCCAdminStatus,'atmConfVcLoopbackAdminStatus':atmConfVcLoopbackAdminStatus,'atmConfVcLoopbackSinkAddress':atmConfVcLoopbackSinkAddress,'atmConfVcCongestionControl':atmConfVcCongestionControl,'atmConfVcCCDirection':atmConfVcCCDirection,'atmConfVcCreationTime':atmConfVcCreationTime,'atmConfVcOamSupport':atmConfVcOamSupport,'atmConfVcCCActivationCtrl':atmConfVcCCActivationCtrl,'atmConfVcCCOperStatus':atmConfVcCCOperStatus,'atmConfVcLoopbackTraffic':atmConfVcLoopbackTraffic,'atmConfVcLoopbackFailureInd':atmConfVcLoopbackFailureInd,'atmConfVcLoopbackFailureThreshold':atmConfVcLoopbackFailureThreshold,'atmConfVcOamDirection':atmConfVcOamDirection,'atmConfVcName':atmConfVcName,'atmConfVcConnected':atmConfVcConnected,'atmConfVcOamDescrIndex':atmConfVcOamDescrIndex,'atmConfVcNoOfUsages':atmConfVcNoOfUsages,'atmNteAlarmVpTable':atmNteAlarmVpTable,'atmNteAlarmVpEntry':atmNteAlarmVpEntry,_A2:atmNteVpAlarmVpi,'atmNteVpActiveAlarms':atmNteVpActiveAlarms,'atmNteAlarmVcTable':atmNteAlarmVcTable,'atmNteAlarmVcEntry':atmNteAlarmVcEntry,_A3:atmNteVcAlarmVpi,_A4:atmNteVcAlarmVci,'atmNteVcActiveAlarms':atmNteVcActiveAlarms})