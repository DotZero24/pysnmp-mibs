_AM='pwAtmInboundNto1Group'
_AL='pwAtmOutboundNto1Group'
_AK='pwAtmInbound1to1Group'
_AJ='pwAtmOutbound1to1Group'
_AI='pwAtmPerfGroup'
_AH='pwAtmCfgGroup'
_AG='pwAtmInboundNto1MappedVci'
_AF='pwAtmInboundNto1MappedVpi'
_AE='pwAtmInboundNto1TrafficParamDescr'
_AD='pwAtmInboundNto1RowStatus'
_AC='pwAtmOutboundNto1MappedVci'
_AB='pwAtmOutboundNto1MappedVpi'
_AA='pwAtmOutboundNto1TrafficParamDescr'
_A9='pwAtmOutboundNto1RowStatus'
_A8='pwAtmInboundRowStatus'
_A7='pwAtmInboundTrafficParamDescr'
_A6='pwAtmInboundVci'
_A5='pwAtmInboundVpi'
_A4='pwAtmInboundAtmIf'
_A3='pwAtmOutboundRowStatus'
_A2='pwAtmOutboundTrafficParamDescr'
_A1='pwAtmOutboundVci'
_A0='pwAtmOutboundVpi'
_z='pwAtmOutboundAtmIf'
_y='pwAtmPerf1DayIntervalUnknownCells'
_x='pwAtmPerf1DayIntervalCellsReceived'
_w='pwAtmPerf1DayIntervalCellsDropped'
_v='pwAtmPerf1DayIntervalCellsXmit'
_u='pwAtmPerf1DayIntervalPktsTimeout'
_t='pwAtmPerf1DayIntervalPktsMisOrder'
_s='pwAtmPerf1DayIntervalPktsReOrder'
_r='pwAtmPerf1DayIntervalMissingPkts'
_q='pwAtmPerf1DayIntervalDuration'
_p='pwAtmPerf1DayIntervalValidData'
_o='pwAtmPerfIntervalUnknownCells'
_n='pwAtmPerfIntervalCellsReceived'
_m='pwAtmPerfIntervalCellsDropped'
_l='pwAtmPerfIntervalCellsXmit'
_k='pwAtmPerfIntervalPktsTimeout'
_j='pwAtmPerfIntervalPktsMisOrder'
_i='pwAtmPerfIntervalPktsReOrder'
_h='pwAtmPerfIntervalMissingPkts'
_g='pwAtmPerfIntervalDuration'
_f='pwAtmPerfIntervalValidData'
_e='pwAtmPerfCurrentUnknownCells'
_d='pwAtmPerfCurrentCellsReceived'
_c='pwAtmPerfCurrentCellsDropped'
_b='pwAtmPerfCurrentCellsXmit'
_a='pwAtmPerfCurrentPktsTimeout'
_Z='pwAtmPerfCurrentPktsMisOrder'
_Y='pwAtmPerfCurrentPktsReOrder'
_X='pwAtmPerfCurrentMissingPkts'
_W='pwAtmOamCellSupported'
_V='pwAtmClpQosMapping'
_U='pwAtmCfgTimeoutMode'
_T='pwAtmCfgFarEndMaxCellConcatenation'
_S='pwAtmCfgMaxCellConcatenation'
_R='pwAtmPerf1DayIntervalNumber'
_Q='pwAtmPerfIntervalNumber'
_P='pwAtmInboundNto1Vci'
_O='pwAtmInboundNto1Vpi'
_N='pwAtmInboundNto1AtmIf'
_M='pwAtmOutboundNto1Vci'
_L='pwAtmOutboundNto1Vpi'
_K='pwAtmOutboundNto1AtmIf'
_J='Integer32'
_I='Unsigned32'
_H='read-write'
_G='not-accessible'
_F='pwIndex'
_E='PW-STD-R-MIB'
_D='read-create'
_C='read-only'
_B='PW-ATM-R-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
pwIndex,=mibBuilder.importSymbols(_E,_F)
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso','transmission')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TruthValue')
pwAtmMIBR=ModuleIdentity((1,3,6,1,4,1,164,20,16))
if mibBuilder.loadTexts:pwAtmMIBR.setRevisions(('2007-02-04 00:00','2006-08-21 00:00','2003-10-16 00:00'))
_RadExperimental_ObjectIdentity=ObjectIdentity
radExperimental=_RadExperimental_ObjectIdentity((1,3,6,1,4,1,164,20))
_PwAtmNotifications_ObjectIdentity=ObjectIdentity
pwAtmNotifications=_PwAtmNotifications_ObjectIdentity((1,3,6,1,4,1,164,20,16,0))
_PwAtmObjects_ObjectIdentity=ObjectIdentity
pwAtmObjects=_PwAtmObjects_ObjectIdentity((1,3,6,1,4,1,164,20,16,1))
_PwAtmOutboundTable_Object=MibTable
pwAtmOutboundTable=_PwAtmOutboundTable_Object((1,3,6,1,4,1,164,20,16,1,1))
if mibBuilder.loadTexts:pwAtmOutboundTable.setStatus(_A)
_PwAtmOutboundEntry_Object=MibTableRow
pwAtmOutboundEntry=_PwAtmOutboundEntry_Object((1,3,6,1,4,1,164,20,16,1,1,1))
pwAtmOutboundEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pwAtmOutboundEntry.setStatus(_A)
_PwAtmOutboundAtmIf_Type=InterfaceIndex
_PwAtmOutboundAtmIf_Object=MibTableColumn
pwAtmOutboundAtmIf=_PwAtmOutboundAtmIf_Object((1,3,6,1,4,1,164,20,16,1,1,1,1),_PwAtmOutboundAtmIf_Type())
pwAtmOutboundAtmIf.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundAtmIf.setStatus(_A)
_PwAtmOutboundVpi_Type=AtmVpIdentifier
_PwAtmOutboundVpi_Object=MibTableColumn
pwAtmOutboundVpi=_PwAtmOutboundVpi_Object((1,3,6,1,4,1,164,20,16,1,1,1,2),_PwAtmOutboundVpi_Type())
pwAtmOutboundVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundVpi.setStatus(_A)
_PwAtmOutboundVci_Type=AtmVcIdentifier
_PwAtmOutboundVci_Object=MibTableColumn
pwAtmOutboundVci=_PwAtmOutboundVci_Object((1,3,6,1,4,1,164,20,16,1,1,1,3),_PwAtmOutboundVci_Type())
pwAtmOutboundVci.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundVci.setStatus(_A)
_PwAtmOutboundTrafficParamDescr_Type=RowPointer
_PwAtmOutboundTrafficParamDescr_Object=MibTableColumn
pwAtmOutboundTrafficParamDescr=_PwAtmOutboundTrafficParamDescr_Object((1,3,6,1,4,1,164,20,16,1,1,1,4),_PwAtmOutboundTrafficParamDescr_Type())
pwAtmOutboundTrafficParamDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundTrafficParamDescr.setStatus(_A)
_PwAtmOutboundRowStatus_Type=RowStatus
_PwAtmOutboundRowStatus_Object=MibTableColumn
pwAtmOutboundRowStatus=_PwAtmOutboundRowStatus_Object((1,3,6,1,4,1,164,20,16,1,1,1,5),_PwAtmOutboundRowStatus_Type())
pwAtmOutboundRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundRowStatus.setStatus(_A)
_PwAtmInboundTable_Object=MibTable
pwAtmInboundTable=_PwAtmInboundTable_Object((1,3,6,1,4,1,164,20,16,1,3))
if mibBuilder.loadTexts:pwAtmInboundTable.setStatus(_A)
_PwAtmInboundEntry_Object=MibTableRow
pwAtmInboundEntry=_PwAtmInboundEntry_Object((1,3,6,1,4,1,164,20,16,1,3,1))
pwAtmInboundEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pwAtmInboundEntry.setStatus(_A)
_PwAtmInboundAtmIf_Type=InterfaceIndex
_PwAtmInboundAtmIf_Object=MibTableColumn
pwAtmInboundAtmIf=_PwAtmInboundAtmIf_Object((1,3,6,1,4,1,164,20,16,1,3,1,1),_PwAtmInboundAtmIf_Type())
pwAtmInboundAtmIf.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundAtmIf.setStatus(_A)
_PwAtmInboundVpi_Type=AtmVpIdentifier
_PwAtmInboundVpi_Object=MibTableColumn
pwAtmInboundVpi=_PwAtmInboundVpi_Object((1,3,6,1,4,1,164,20,16,1,3,1,2),_PwAtmInboundVpi_Type())
pwAtmInboundVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundVpi.setStatus(_A)
_PwAtmInboundVci_Type=AtmVcIdentifier
_PwAtmInboundVci_Object=MibTableColumn
pwAtmInboundVci=_PwAtmInboundVci_Object((1,3,6,1,4,1,164,20,16,1,3,1,3),_PwAtmInboundVci_Type())
pwAtmInboundVci.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundVci.setStatus(_A)
_PwAtmInboundTrafficParamDescr_Type=RowPointer
_PwAtmInboundTrafficParamDescr_Object=MibTableColumn
pwAtmInboundTrafficParamDescr=_PwAtmInboundTrafficParamDescr_Object((1,3,6,1,4,1,164,20,16,1,3,1,4),_PwAtmInboundTrafficParamDescr_Type())
pwAtmInboundTrafficParamDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundTrafficParamDescr.setStatus(_A)
_PwAtmInboundRowStatus_Type=RowStatus
_PwAtmInboundRowStatus_Object=MibTableColumn
pwAtmInboundRowStatus=_PwAtmInboundRowStatus_Object((1,3,6,1,4,1,164,20,16,1,3,1,5),_PwAtmInboundRowStatus_Type())
pwAtmInboundRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundRowStatus.setStatus(_A)
_PwAtmCfgTable_Object=MibTable
pwAtmCfgTable=_PwAtmCfgTable_Object((1,3,6,1,4,1,164,20,16,1,5))
if mibBuilder.loadTexts:pwAtmCfgTable.setStatus(_A)
_PwAtmCfgEntry_Object=MibTableRow
pwAtmCfgEntry=_PwAtmCfgEntry_Object((1,3,6,1,4,1,164,20,16,1,5,1))
pwAtmCfgEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pwAtmCfgEntry.setStatus(_A)
class _PwAtmCfgMaxCellConcatenation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_PwAtmCfgMaxCellConcatenation_Type.__name__=_I
_PwAtmCfgMaxCellConcatenation_Object=MibTableColumn
pwAtmCfgMaxCellConcatenation=_PwAtmCfgMaxCellConcatenation_Object((1,3,6,1,4,1,164,20,16,1,5,1,1),_PwAtmCfgMaxCellConcatenation_Type())
pwAtmCfgMaxCellConcatenation.setMaxAccess(_H)
if mibBuilder.loadTexts:pwAtmCfgMaxCellConcatenation.setStatus(_A)
class _PwAtmCfgFarEndMaxCellConcatenation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_PwAtmCfgFarEndMaxCellConcatenation_Type.__name__=_I
_PwAtmCfgFarEndMaxCellConcatenation_Object=MibTableColumn
pwAtmCfgFarEndMaxCellConcatenation=_PwAtmCfgFarEndMaxCellConcatenation_Object((1,3,6,1,4,1,164,20,16,1,5,1,2),_PwAtmCfgFarEndMaxCellConcatenation_Type())
pwAtmCfgFarEndMaxCellConcatenation.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmCfgFarEndMaxCellConcatenation.setStatus(_A)
class _PwAtmCfgTimeoutMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('disabled',2),('enabled',3)))
_PwAtmCfgTimeoutMode_Type.__name__=_J
_PwAtmCfgTimeoutMode_Object=MibTableColumn
pwAtmCfgTimeoutMode=_PwAtmCfgTimeoutMode_Object((1,3,6,1,4,1,164,20,16,1,5,1,3),_PwAtmCfgTimeoutMode_Type())
pwAtmCfgTimeoutMode.setMaxAccess(_H)
if mibBuilder.loadTexts:pwAtmCfgTimeoutMode.setStatus(_A)
_PwAtmClpQosMapping_Type=TruthValue
_PwAtmClpQosMapping_Object=MibTableColumn
pwAtmClpQosMapping=_PwAtmClpQosMapping_Object((1,3,6,1,4,1,164,20,16,1,5,1,4),_PwAtmClpQosMapping_Type())
pwAtmClpQosMapping.setMaxAccess(_H)
if mibBuilder.loadTexts:pwAtmClpQosMapping.setStatus(_A)
_PwAtmOamCellSupported_Type=TruthValue
_PwAtmOamCellSupported_Object=MibTableColumn
pwAtmOamCellSupported=_PwAtmOamCellSupported_Object((1,3,6,1,4,1,164,20,16,1,5,1,5),_PwAtmOamCellSupported_Type())
pwAtmOamCellSupported.setMaxAccess(_H)
if mibBuilder.loadTexts:pwAtmOamCellSupported.setStatus(_A)
_PwAtmOutboundNto1Table_Object=MibTable
pwAtmOutboundNto1Table=_PwAtmOutboundNto1Table_Object((1,3,6,1,4,1,164,20,16,1,6))
if mibBuilder.loadTexts:pwAtmOutboundNto1Table.setStatus(_A)
_PwAtmOutboundNto1Entry_Object=MibTableRow
pwAtmOutboundNto1Entry=_PwAtmOutboundNto1Entry_Object((1,3,6,1,4,1,164,20,16,1,6,1))
pwAtmOutboundNto1Entry.setIndexNames((0,_E,_F),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:pwAtmOutboundNto1Entry.setStatus(_A)
_PwAtmOutboundNto1AtmIf_Type=InterfaceIndex
_PwAtmOutboundNto1AtmIf_Object=MibTableColumn
pwAtmOutboundNto1AtmIf=_PwAtmOutboundNto1AtmIf_Object((1,3,6,1,4,1,164,20,16,1,6,1,1),_PwAtmOutboundNto1AtmIf_Type())
pwAtmOutboundNto1AtmIf.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmOutboundNto1AtmIf.setStatus(_A)
_PwAtmOutboundNto1Vpi_Type=AtmVpIdentifier
_PwAtmOutboundNto1Vpi_Object=MibTableColumn
pwAtmOutboundNto1Vpi=_PwAtmOutboundNto1Vpi_Object((1,3,6,1,4,1,164,20,16,1,6,1,2),_PwAtmOutboundNto1Vpi_Type())
pwAtmOutboundNto1Vpi.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmOutboundNto1Vpi.setStatus(_A)
_PwAtmOutboundNto1Vci_Type=AtmVcIdentifier
_PwAtmOutboundNto1Vci_Object=MibTableColumn
pwAtmOutboundNto1Vci=_PwAtmOutboundNto1Vci_Object((1,3,6,1,4,1,164,20,16,1,6,1,3),_PwAtmOutboundNto1Vci_Type())
pwAtmOutboundNto1Vci.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmOutboundNto1Vci.setStatus(_A)
_PwAtmOutboundNto1RowStatus_Type=RowStatus
_PwAtmOutboundNto1RowStatus_Object=MibTableColumn
pwAtmOutboundNto1RowStatus=_PwAtmOutboundNto1RowStatus_Object((1,3,6,1,4,1,164,20,16,1,6,1,4),_PwAtmOutboundNto1RowStatus_Type())
pwAtmOutboundNto1RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundNto1RowStatus.setStatus(_A)
_PwAtmOutboundNto1TrafficParamDescr_Type=RowPointer
_PwAtmOutboundNto1TrafficParamDescr_Object=MibTableColumn
pwAtmOutboundNto1TrafficParamDescr=_PwAtmOutboundNto1TrafficParamDescr_Object((1,3,6,1,4,1,164,20,16,1,6,1,5),_PwAtmOutboundNto1TrafficParamDescr_Type())
pwAtmOutboundNto1TrafficParamDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundNto1TrafficParamDescr.setStatus(_A)
_PwAtmOutboundNto1MappedVpi_Type=AtmVpIdentifier
_PwAtmOutboundNto1MappedVpi_Object=MibTableColumn
pwAtmOutboundNto1MappedVpi=_PwAtmOutboundNto1MappedVpi_Object((1,3,6,1,4,1,164,20,16,1,6,1,6),_PwAtmOutboundNto1MappedVpi_Type())
pwAtmOutboundNto1MappedVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundNto1MappedVpi.setStatus(_A)
_PwAtmOutboundNto1MappedVci_Type=AtmVcIdentifier
_PwAtmOutboundNto1MappedVci_Object=MibTableColumn
pwAtmOutboundNto1MappedVci=_PwAtmOutboundNto1MappedVci_Object((1,3,6,1,4,1,164,20,16,1,6,1,7),_PwAtmOutboundNto1MappedVci_Type())
pwAtmOutboundNto1MappedVci.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmOutboundNto1MappedVci.setStatus(_A)
_PwAtmInboundNto1Table_Object=MibTable
pwAtmInboundNto1Table=_PwAtmInboundNto1Table_Object((1,3,6,1,4,1,164,20,16,1,7))
if mibBuilder.loadTexts:pwAtmInboundNto1Table.setStatus(_A)
_PwAtmInboundNto1Entry_Object=MibTableRow
pwAtmInboundNto1Entry=_PwAtmInboundNto1Entry_Object((1,3,6,1,4,1,164,20,16,1,7,1))
pwAtmInboundNto1Entry.setIndexNames((0,_E,_F),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:pwAtmInboundNto1Entry.setStatus(_A)
_PwAtmInboundNto1AtmIf_Type=InterfaceIndex
_PwAtmInboundNto1AtmIf_Object=MibTableColumn
pwAtmInboundNto1AtmIf=_PwAtmInboundNto1AtmIf_Object((1,3,6,1,4,1,164,20,16,1,7,1,1),_PwAtmInboundNto1AtmIf_Type())
pwAtmInboundNto1AtmIf.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmInboundNto1AtmIf.setStatus(_A)
_PwAtmInboundNto1Vpi_Type=AtmVpIdentifier
_PwAtmInboundNto1Vpi_Object=MibTableColumn
pwAtmInboundNto1Vpi=_PwAtmInboundNto1Vpi_Object((1,3,6,1,4,1,164,20,16,1,7,1,2),_PwAtmInboundNto1Vpi_Type())
pwAtmInboundNto1Vpi.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmInboundNto1Vpi.setStatus(_A)
_PwAtmInboundNto1Vci_Type=AtmVcIdentifier
_PwAtmInboundNto1Vci_Object=MibTableColumn
pwAtmInboundNto1Vci=_PwAtmInboundNto1Vci_Object((1,3,6,1,4,1,164,20,16,1,7,1,3),_PwAtmInboundNto1Vci_Type())
pwAtmInboundNto1Vci.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmInboundNto1Vci.setStatus(_A)
_PwAtmInboundNto1RowStatus_Type=RowStatus
_PwAtmInboundNto1RowStatus_Object=MibTableColumn
pwAtmInboundNto1RowStatus=_PwAtmInboundNto1RowStatus_Object((1,3,6,1,4,1,164,20,16,1,7,1,4),_PwAtmInboundNto1RowStatus_Type())
pwAtmInboundNto1RowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundNto1RowStatus.setStatus(_A)
_PwAtmInboundNto1TrafficParamDescr_Type=RowPointer
_PwAtmInboundNto1TrafficParamDescr_Object=MibTableColumn
pwAtmInboundNto1TrafficParamDescr=_PwAtmInboundNto1TrafficParamDescr_Object((1,3,6,1,4,1,164,20,16,1,7,1,5),_PwAtmInboundNto1TrafficParamDescr_Type())
pwAtmInboundNto1TrafficParamDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundNto1TrafficParamDescr.setStatus(_A)
_PwAtmInboundNto1MappedVpi_Type=AtmVpIdentifier
_PwAtmInboundNto1MappedVpi_Object=MibTableColumn
pwAtmInboundNto1MappedVpi=_PwAtmInboundNto1MappedVpi_Object((1,3,6,1,4,1,164,20,16,1,7,1,6),_PwAtmInboundNto1MappedVpi_Type())
pwAtmInboundNto1MappedVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundNto1MappedVpi.setStatus(_A)
_PwAtmInboundNto1MappedVci_Type=AtmVcIdentifier
_PwAtmInboundNto1MappedVci_Object=MibTableColumn
pwAtmInboundNto1MappedVci=_PwAtmInboundNto1MappedVci_Object((1,3,6,1,4,1,164,20,16,1,7,1,7),_PwAtmInboundNto1MappedVci_Type())
pwAtmInboundNto1MappedVci.setMaxAccess(_D)
if mibBuilder.loadTexts:pwAtmInboundNto1MappedVci.setStatus(_A)
_PwAtmPerfCurrentTable_Object=MibTable
pwAtmPerfCurrentTable=_PwAtmPerfCurrentTable_Object((1,3,6,1,4,1,164,20,16,1,8))
if mibBuilder.loadTexts:pwAtmPerfCurrentTable.setStatus(_A)
_PwAtmPerfCurrentEntry_Object=MibTableRow
pwAtmPerfCurrentEntry=_PwAtmPerfCurrentEntry_Object((1,3,6,1,4,1,164,20,16,1,8,1))
pwAtmPerfCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pwAtmPerfCurrentEntry.setStatus(_A)
_PwAtmPerfCurrentMissingPkts_Type=PerfCurrentCount
_PwAtmPerfCurrentMissingPkts_Object=MibTableColumn
pwAtmPerfCurrentMissingPkts=_PwAtmPerfCurrentMissingPkts_Object((1,3,6,1,4,1,164,20,16,1,8,1,1),_PwAtmPerfCurrentMissingPkts_Type())
pwAtmPerfCurrentMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentMissingPkts.setStatus(_A)
_PwAtmPerfCurrentPktsReOrder_Type=PerfCurrentCount
_PwAtmPerfCurrentPktsReOrder_Object=MibTableColumn
pwAtmPerfCurrentPktsReOrder=_PwAtmPerfCurrentPktsReOrder_Object((1,3,6,1,4,1,164,20,16,1,8,1,2),_PwAtmPerfCurrentPktsReOrder_Type())
pwAtmPerfCurrentPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentPktsReOrder.setStatus(_A)
_PwAtmPerfCurrentPktsMisOrder_Type=PerfCurrentCount
_PwAtmPerfCurrentPktsMisOrder_Object=MibTableColumn
pwAtmPerfCurrentPktsMisOrder=_PwAtmPerfCurrentPktsMisOrder_Object((1,3,6,1,4,1,164,20,16,1,8,1,3),_PwAtmPerfCurrentPktsMisOrder_Type())
pwAtmPerfCurrentPktsMisOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentPktsMisOrder.setStatus(_A)
_PwAtmPerfCurrentPktsTimeout_Type=PerfCurrentCount
_PwAtmPerfCurrentPktsTimeout_Object=MibTableColumn
pwAtmPerfCurrentPktsTimeout=_PwAtmPerfCurrentPktsTimeout_Object((1,3,6,1,4,1,164,20,16,1,8,1,4),_PwAtmPerfCurrentPktsTimeout_Type())
pwAtmPerfCurrentPktsTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentPktsTimeout.setStatus(_A)
_PwAtmPerfCurrentCellsXmit_Type=PerfCurrentCount
_PwAtmPerfCurrentCellsXmit_Object=MibTableColumn
pwAtmPerfCurrentCellsXmit=_PwAtmPerfCurrentCellsXmit_Object((1,3,6,1,4,1,164,20,16,1,8,1,5),_PwAtmPerfCurrentCellsXmit_Type())
pwAtmPerfCurrentCellsXmit.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentCellsXmit.setStatus(_A)
_PwAtmPerfCurrentCellsDropped_Type=PerfCurrentCount
_PwAtmPerfCurrentCellsDropped_Object=MibTableColumn
pwAtmPerfCurrentCellsDropped=_PwAtmPerfCurrentCellsDropped_Object((1,3,6,1,4,1,164,20,16,1,8,1,6),_PwAtmPerfCurrentCellsDropped_Type())
pwAtmPerfCurrentCellsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentCellsDropped.setStatus(_A)
_PwAtmPerfCurrentCellsReceived_Type=PerfCurrentCount
_PwAtmPerfCurrentCellsReceived_Object=MibTableColumn
pwAtmPerfCurrentCellsReceived=_PwAtmPerfCurrentCellsReceived_Object((1,3,6,1,4,1,164,20,16,1,8,1,7),_PwAtmPerfCurrentCellsReceived_Type())
pwAtmPerfCurrentCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentCellsReceived.setStatus(_A)
_PwAtmPerfCurrentUnknownCells_Type=PerfCurrentCount
_PwAtmPerfCurrentUnknownCells_Object=MibTableColumn
pwAtmPerfCurrentUnknownCells=_PwAtmPerfCurrentUnknownCells_Object((1,3,6,1,4,1,164,20,16,1,8,1,8),_PwAtmPerfCurrentUnknownCells_Type())
pwAtmPerfCurrentUnknownCells.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfCurrentUnknownCells.setStatus(_A)
_PwAtmPerfIntervalTable_Object=MibTable
pwAtmPerfIntervalTable=_PwAtmPerfIntervalTable_Object((1,3,6,1,4,1,164,20,16,1,9))
if mibBuilder.loadTexts:pwAtmPerfIntervalTable.setStatus(_A)
_PwAtmPerfIntervalEntry_Object=MibTableRow
pwAtmPerfIntervalEntry=_PwAtmPerfIntervalEntry_Object((1,3,6,1,4,1,164,20,16,1,9,1))
pwAtmPerfIntervalEntry.setIndexNames((0,_E,_F),(0,_B,_Q))
if mibBuilder.loadTexts:pwAtmPerfIntervalEntry.setStatus(_A)
_PwAtmPerfIntervalNumber_Type=Unsigned32
_PwAtmPerfIntervalNumber_Object=MibTableColumn
pwAtmPerfIntervalNumber=_PwAtmPerfIntervalNumber_Object((1,3,6,1,4,1,164,20,16,1,9,1,1),_PwAtmPerfIntervalNumber_Type())
pwAtmPerfIntervalNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmPerfIntervalNumber.setStatus(_A)
_PwAtmPerfIntervalValidData_Type=TruthValue
_PwAtmPerfIntervalValidData_Object=MibTableColumn
pwAtmPerfIntervalValidData=_PwAtmPerfIntervalValidData_Object((1,3,6,1,4,1,164,20,16,1,9,1,2),_PwAtmPerfIntervalValidData_Type())
pwAtmPerfIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalValidData.setStatus(_A)
_PwAtmPerfIntervalDuration_Type=Unsigned32
_PwAtmPerfIntervalDuration_Object=MibTableColumn
pwAtmPerfIntervalDuration=_PwAtmPerfIntervalDuration_Object((1,3,6,1,4,1,164,20,16,1,9,1,3),_PwAtmPerfIntervalDuration_Type())
pwAtmPerfIntervalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalDuration.setStatus(_A)
_PwAtmPerfIntervalMissingPkts_Type=PerfIntervalCount
_PwAtmPerfIntervalMissingPkts_Object=MibTableColumn
pwAtmPerfIntervalMissingPkts=_PwAtmPerfIntervalMissingPkts_Object((1,3,6,1,4,1,164,20,16,1,9,1,4),_PwAtmPerfIntervalMissingPkts_Type())
pwAtmPerfIntervalMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalMissingPkts.setStatus(_A)
_PwAtmPerfIntervalPktsReOrder_Type=PerfIntervalCount
_PwAtmPerfIntervalPktsReOrder_Object=MibTableColumn
pwAtmPerfIntervalPktsReOrder=_PwAtmPerfIntervalPktsReOrder_Object((1,3,6,1,4,1,164,20,16,1,9,1,5),_PwAtmPerfIntervalPktsReOrder_Type())
pwAtmPerfIntervalPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalPktsReOrder.setStatus(_A)
_PwAtmPerfIntervalPktsMisOrder_Type=PerfIntervalCount
_PwAtmPerfIntervalPktsMisOrder_Object=MibTableColumn
pwAtmPerfIntervalPktsMisOrder=_PwAtmPerfIntervalPktsMisOrder_Object((1,3,6,1,4,1,164,20,16,1,9,1,6),_PwAtmPerfIntervalPktsMisOrder_Type())
pwAtmPerfIntervalPktsMisOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalPktsMisOrder.setStatus(_A)
_PwAtmPerfIntervalPktsTimeout_Type=PerfIntervalCount
_PwAtmPerfIntervalPktsTimeout_Object=MibTableColumn
pwAtmPerfIntervalPktsTimeout=_PwAtmPerfIntervalPktsTimeout_Object((1,3,6,1,4,1,164,20,16,1,9,1,7),_PwAtmPerfIntervalPktsTimeout_Type())
pwAtmPerfIntervalPktsTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalPktsTimeout.setStatus(_A)
_PwAtmPerfIntervalCellsXmit_Type=PerfIntervalCount
_PwAtmPerfIntervalCellsXmit_Object=MibTableColumn
pwAtmPerfIntervalCellsXmit=_PwAtmPerfIntervalCellsXmit_Object((1,3,6,1,4,1,164,20,16,1,9,1,8),_PwAtmPerfIntervalCellsXmit_Type())
pwAtmPerfIntervalCellsXmit.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalCellsXmit.setStatus(_A)
_PwAtmPerfIntervalCellsDropped_Type=PerfIntervalCount
_PwAtmPerfIntervalCellsDropped_Object=MibTableColumn
pwAtmPerfIntervalCellsDropped=_PwAtmPerfIntervalCellsDropped_Object((1,3,6,1,4,1,164,20,16,1,9,1,9),_PwAtmPerfIntervalCellsDropped_Type())
pwAtmPerfIntervalCellsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalCellsDropped.setStatus(_A)
_PwAtmPerfIntervalCellsReceived_Type=PerfIntervalCount
_PwAtmPerfIntervalCellsReceived_Object=MibTableColumn
pwAtmPerfIntervalCellsReceived=_PwAtmPerfIntervalCellsReceived_Object((1,3,6,1,4,1,164,20,16,1,9,1,10),_PwAtmPerfIntervalCellsReceived_Type())
pwAtmPerfIntervalCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalCellsReceived.setStatus(_A)
_PwAtmPerfIntervalUnknownCells_Type=PerfIntervalCount
_PwAtmPerfIntervalUnknownCells_Object=MibTableColumn
pwAtmPerfIntervalUnknownCells=_PwAtmPerfIntervalUnknownCells_Object((1,3,6,1,4,1,164,20,16,1,9,1,11),_PwAtmPerfIntervalUnknownCells_Type())
pwAtmPerfIntervalUnknownCells.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerfIntervalUnknownCells.setStatus(_A)
_PwAtmPerf1DayIntervalTable_Object=MibTable
pwAtmPerf1DayIntervalTable=_PwAtmPerf1DayIntervalTable_Object((1,3,6,1,4,1,164,20,16,1,10))
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalTable.setStatus(_A)
_PwAtmPerf1DayIntervalEntry_Object=MibTableRow
pwAtmPerf1DayIntervalEntry=_PwAtmPerf1DayIntervalEntry_Object((1,3,6,1,4,1,164,20,16,1,10,1))
pwAtmPerf1DayIntervalEntry.setIndexNames((0,_E,_F),(0,_B,_R))
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalEntry.setStatus(_A)
_PwAtmPerf1DayIntervalNumber_Type=Unsigned32
_PwAtmPerf1DayIntervalNumber_Object=MibTableColumn
pwAtmPerf1DayIntervalNumber=_PwAtmPerf1DayIntervalNumber_Object((1,3,6,1,4,1,164,20,16,1,10,1,1),_PwAtmPerf1DayIntervalNumber_Type())
pwAtmPerf1DayIntervalNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalNumber.setStatus(_A)
_PwAtmPerf1DayIntervalValidData_Type=TruthValue
_PwAtmPerf1DayIntervalValidData_Object=MibTableColumn
pwAtmPerf1DayIntervalValidData=_PwAtmPerf1DayIntervalValidData_Object((1,3,6,1,4,1,164,20,16,1,10,1,2),_PwAtmPerf1DayIntervalValidData_Type())
pwAtmPerf1DayIntervalValidData.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalValidData.setStatus(_A)
_PwAtmPerf1DayIntervalDuration_Type=Unsigned32
_PwAtmPerf1DayIntervalDuration_Object=MibTableColumn
pwAtmPerf1DayIntervalDuration=_PwAtmPerf1DayIntervalDuration_Object((1,3,6,1,4,1,164,20,16,1,10,1,3),_PwAtmPerf1DayIntervalDuration_Type())
pwAtmPerf1DayIntervalDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalDuration.setStatus(_A)
_PwAtmPerf1DayIntervalMissingPkts_Type=Counter32
_PwAtmPerf1DayIntervalMissingPkts_Object=MibTableColumn
pwAtmPerf1DayIntervalMissingPkts=_PwAtmPerf1DayIntervalMissingPkts_Object((1,3,6,1,4,1,164,20,16,1,10,1,4),_PwAtmPerf1DayIntervalMissingPkts_Type())
pwAtmPerf1DayIntervalMissingPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalMissingPkts.setStatus(_A)
_PwAtmPerf1DayIntervalPktsReOrder_Type=Counter32
_PwAtmPerf1DayIntervalPktsReOrder_Object=MibTableColumn
pwAtmPerf1DayIntervalPktsReOrder=_PwAtmPerf1DayIntervalPktsReOrder_Object((1,3,6,1,4,1,164,20,16,1,10,1,5),_PwAtmPerf1DayIntervalPktsReOrder_Type())
pwAtmPerf1DayIntervalPktsReOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalPktsReOrder.setStatus(_A)
_PwAtmPerf1DayIntervalPktsMisOrder_Type=Counter32
_PwAtmPerf1DayIntervalPktsMisOrder_Object=MibTableColumn
pwAtmPerf1DayIntervalPktsMisOrder=_PwAtmPerf1DayIntervalPktsMisOrder_Object((1,3,6,1,4,1,164,20,16,1,10,1,6),_PwAtmPerf1DayIntervalPktsMisOrder_Type())
pwAtmPerf1DayIntervalPktsMisOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalPktsMisOrder.setStatus(_A)
_PwAtmPerf1DayIntervalPktsTimeout_Type=Counter32
_PwAtmPerf1DayIntervalPktsTimeout_Object=MibTableColumn
pwAtmPerf1DayIntervalPktsTimeout=_PwAtmPerf1DayIntervalPktsTimeout_Object((1,3,6,1,4,1,164,20,16,1,10,1,7),_PwAtmPerf1DayIntervalPktsTimeout_Type())
pwAtmPerf1DayIntervalPktsTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalPktsTimeout.setStatus(_A)
_PwAtmPerf1DayIntervalCellsXmit_Type=Counter32
_PwAtmPerf1DayIntervalCellsXmit_Object=MibTableColumn
pwAtmPerf1DayIntervalCellsXmit=_PwAtmPerf1DayIntervalCellsXmit_Object((1,3,6,1,4,1,164,20,16,1,10,1,8),_PwAtmPerf1DayIntervalCellsXmit_Type())
pwAtmPerf1DayIntervalCellsXmit.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalCellsXmit.setStatus(_A)
_PwAtmPerf1DayIntervalCellsDropped_Type=Counter32
_PwAtmPerf1DayIntervalCellsDropped_Object=MibTableColumn
pwAtmPerf1DayIntervalCellsDropped=_PwAtmPerf1DayIntervalCellsDropped_Object((1,3,6,1,4,1,164,20,16,1,10,1,9),_PwAtmPerf1DayIntervalCellsDropped_Type())
pwAtmPerf1DayIntervalCellsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalCellsDropped.setStatus(_A)
_PwAtmPerf1DayIntervalCellsReceived_Type=Counter32
_PwAtmPerf1DayIntervalCellsReceived_Object=MibTableColumn
pwAtmPerf1DayIntervalCellsReceived=_PwAtmPerf1DayIntervalCellsReceived_Object((1,3,6,1,4,1,164,20,16,1,10,1,10),_PwAtmPerf1DayIntervalCellsReceived_Type())
pwAtmPerf1DayIntervalCellsReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalCellsReceived.setStatus(_A)
_PwAtmPerf1DayIntervalUnknownCells_Type=Counter32
_PwAtmPerf1DayIntervalUnknownCells_Object=MibTableColumn
pwAtmPerf1DayIntervalUnknownCells=_PwAtmPerf1DayIntervalUnknownCells_Object((1,3,6,1,4,1,164,20,16,1,10,1,11),_PwAtmPerf1DayIntervalUnknownCells_Type())
pwAtmPerf1DayIntervalUnknownCells.setMaxAccess(_C)
if mibBuilder.loadTexts:pwAtmPerf1DayIntervalUnknownCells.setStatus(_A)
_PwAtmConformance_ObjectIdentity=ObjectIdentity
pwAtmConformance=_PwAtmConformance_ObjectIdentity((1,3,6,1,4,1,164,20,16,2))
_PwAtmGroups_ObjectIdentity=ObjectIdentity
pwAtmGroups=_PwAtmGroups_ObjectIdentity((1,3,6,1,4,1,164,20,16,2,1))
_PwAtmCompliances_ObjectIdentity=ObjectIdentity
pwAtmCompliances=_PwAtmCompliances_ObjectIdentity((1,3,6,1,4,1,164,20,16,2,2))
pwAtmCfgGroup=ObjectGroup((1,3,6,1,4,1,164,20,16,2,1,5))
pwAtmCfgGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:pwAtmCfgGroup.setStatus(_A)
pwAtmPerfGroup=ObjectGroup((1,3,6,1,4,1,164,20,16,2,1,6))
pwAtmPerfGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:pwAtmPerfGroup.setStatus(_A)
pwAtmOutbound1to1Group=ObjectGroup((1,3,6,1,4,1,164,20,16,2,1,7))
pwAtmOutbound1to1Group.setObjects(*((_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:pwAtmOutbound1to1Group.setStatus(_A)
pwAtmInbound1to1Group=ObjectGroup((1,3,6,1,4,1,164,20,16,2,1,8))
pwAtmInbound1to1Group.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:pwAtmInbound1to1Group.setStatus(_A)
pwAtmOutboundNto1Group=ObjectGroup((1,3,6,1,4,1,164,20,16,2,1,9))
pwAtmOutboundNto1Group.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:pwAtmOutboundNto1Group.setStatus(_A)
pwAtmInboundNto1Group=ObjectGroup((1,3,6,1,4,1,164,20,16,2,1,10))
pwAtmInboundNto1Group.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:pwAtmInboundNto1Group.setStatus(_A)
pwAtmCompliance=ModuleCompliance((1,3,6,1,4,1,164,20,16,2,2,2))
pwAtmCompliance.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:pwAtmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'radExperimental':radExperimental,'pwAtmMIBR':pwAtmMIBR,'pwAtmNotifications':pwAtmNotifications,'pwAtmObjects':pwAtmObjects,'pwAtmOutboundTable':pwAtmOutboundTable,'pwAtmOutboundEntry':pwAtmOutboundEntry,_z:pwAtmOutboundAtmIf,_A0:pwAtmOutboundVpi,_A1:pwAtmOutboundVci,_A2:pwAtmOutboundTrafficParamDescr,_A3:pwAtmOutboundRowStatus,'pwAtmInboundTable':pwAtmInboundTable,'pwAtmInboundEntry':pwAtmInboundEntry,_A4:pwAtmInboundAtmIf,_A5:pwAtmInboundVpi,_A6:pwAtmInboundVci,_A7:pwAtmInboundTrafficParamDescr,_A8:pwAtmInboundRowStatus,'pwAtmCfgTable':pwAtmCfgTable,'pwAtmCfgEntry':pwAtmCfgEntry,_S:pwAtmCfgMaxCellConcatenation,_T:pwAtmCfgFarEndMaxCellConcatenation,_U:pwAtmCfgTimeoutMode,_V:pwAtmClpQosMapping,_W:pwAtmOamCellSupported,'pwAtmOutboundNto1Table':pwAtmOutboundNto1Table,'pwAtmOutboundNto1Entry':pwAtmOutboundNto1Entry,_K:pwAtmOutboundNto1AtmIf,_L:pwAtmOutboundNto1Vpi,_M:pwAtmOutboundNto1Vci,_A9:pwAtmOutboundNto1RowStatus,_AA:pwAtmOutboundNto1TrafficParamDescr,_AB:pwAtmOutboundNto1MappedVpi,_AC:pwAtmOutboundNto1MappedVci,'pwAtmInboundNto1Table':pwAtmInboundNto1Table,'pwAtmInboundNto1Entry':pwAtmInboundNto1Entry,_N:pwAtmInboundNto1AtmIf,_O:pwAtmInboundNto1Vpi,_P:pwAtmInboundNto1Vci,_AD:pwAtmInboundNto1RowStatus,_AE:pwAtmInboundNto1TrafficParamDescr,_AF:pwAtmInboundNto1MappedVpi,_AG:pwAtmInboundNto1MappedVci,'pwAtmPerfCurrentTable':pwAtmPerfCurrentTable,'pwAtmPerfCurrentEntry':pwAtmPerfCurrentEntry,_X:pwAtmPerfCurrentMissingPkts,_Y:pwAtmPerfCurrentPktsReOrder,_Z:pwAtmPerfCurrentPktsMisOrder,_a:pwAtmPerfCurrentPktsTimeout,_b:pwAtmPerfCurrentCellsXmit,_c:pwAtmPerfCurrentCellsDropped,_d:pwAtmPerfCurrentCellsReceived,_e:pwAtmPerfCurrentUnknownCells,'pwAtmPerfIntervalTable':pwAtmPerfIntervalTable,'pwAtmPerfIntervalEntry':pwAtmPerfIntervalEntry,_Q:pwAtmPerfIntervalNumber,_f:pwAtmPerfIntervalValidData,_g:pwAtmPerfIntervalDuration,_h:pwAtmPerfIntervalMissingPkts,_i:pwAtmPerfIntervalPktsReOrder,_j:pwAtmPerfIntervalPktsMisOrder,_k:pwAtmPerfIntervalPktsTimeout,_l:pwAtmPerfIntervalCellsXmit,_m:pwAtmPerfIntervalCellsDropped,_n:pwAtmPerfIntervalCellsReceived,_o:pwAtmPerfIntervalUnknownCells,'pwAtmPerf1DayIntervalTable':pwAtmPerf1DayIntervalTable,'pwAtmPerf1DayIntervalEntry':pwAtmPerf1DayIntervalEntry,_R:pwAtmPerf1DayIntervalNumber,_p:pwAtmPerf1DayIntervalValidData,_q:pwAtmPerf1DayIntervalDuration,_r:pwAtmPerf1DayIntervalMissingPkts,_s:pwAtmPerf1DayIntervalPktsReOrder,_t:pwAtmPerf1DayIntervalPktsMisOrder,_u:pwAtmPerf1DayIntervalPktsTimeout,_v:pwAtmPerf1DayIntervalCellsXmit,_w:pwAtmPerf1DayIntervalCellsDropped,_x:pwAtmPerf1DayIntervalCellsReceived,_y:pwAtmPerf1DayIntervalUnknownCells,'pwAtmConformance':pwAtmConformance,'pwAtmGroups':pwAtmGroups,_AH:pwAtmCfgGroup,_AI:pwAtmPerfGroup,_AJ:pwAtmOutbound1to1Group,_AK:pwAtmInbound1to1Group,_AL:pwAtmOutboundNto1Group,_AM:pwAtmInboundNto1Group,'pwAtmCompliances':pwAtmCompliances,'pwAtmCompliance':pwAtmCompliance})