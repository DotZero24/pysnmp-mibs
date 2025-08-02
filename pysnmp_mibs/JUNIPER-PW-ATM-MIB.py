_L='jnxpwAtmPerf1DayIntervalNumber'
_K='jnxpwAtmPerfIntervalNumber'
_J='Integer32'
_I='JUNIPER-PW-ATM-MIB'
_H='Unsigned32'
_G='jnxVpnPwVpnType'
_F='jnxVpnPwVpnName'
_E='jnxVpnPwIndex'
_D='not-accessible'
_C='JUNIPER-VPN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
jnxVpnPwIndex,jnxVpnPwVpnName,jnxVpnPwVpnType=mibBuilder.importSymbols(_C,_E,_F,_G)
PerfCurrentCount,PerfIntervalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso','mib-2')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus','TextualConvention','TruthValue')
jnxPWAtmMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,57))
if mibBuilder.loadTexts:jnxPWAtmMIB.setRevisions(('2009-09-01 00:00',))
_JnxpwAtmNotifications_ObjectIdentity=ObjectIdentity
jnxpwAtmNotifications=_JnxpwAtmNotifications_ObjectIdentity((1,3,6,1,4,1,2636,3,57,0))
_JnxpwAtmObjects_ObjectIdentity=ObjectIdentity
jnxpwAtmObjects=_JnxpwAtmObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,57,1))
_JnxpwAtmCfgTable_Object=MibTable
jnxpwAtmCfgTable=_JnxpwAtmCfgTable_Object((1,3,6,1,4,1,2636,3,57,1,1))
if mibBuilder.loadTexts:jnxpwAtmCfgTable.setStatus(_A)
_JnxpwAtmCfgEntry_Object=MibTableRow
jnxpwAtmCfgEntry=_JnxpwAtmCfgEntry_Object((1,3,6,1,4,1,2636,3,57,1,1,1))
jnxpwAtmCfgEntry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:jnxpwAtmCfgEntry.setStatus(_A)
class _JnxpwAtmCfgMaxCellConcatenation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_JnxpwAtmCfgMaxCellConcatenation_Type.__name__=_H
_JnxpwAtmCfgMaxCellConcatenation_Object=MibTableColumn
jnxpwAtmCfgMaxCellConcatenation=_JnxpwAtmCfgMaxCellConcatenation_Object((1,3,6,1,4,1,2636,3,57,1,1,1,1),_JnxpwAtmCfgMaxCellConcatenation_Type())
jnxpwAtmCfgMaxCellConcatenation.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmCfgMaxCellConcatenation.setStatus(_A)
class _JnxpwAtmCfgFarEndMaxCellConcatenation_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,29))
_JnxpwAtmCfgFarEndMaxCellConcatenation_Type.__name__=_H
_JnxpwAtmCfgFarEndMaxCellConcatenation_Object=MibTableColumn
jnxpwAtmCfgFarEndMaxCellConcatenation=_JnxpwAtmCfgFarEndMaxCellConcatenation_Object((1,3,6,1,4,1,2636,3,57,1,1,1,2),_JnxpwAtmCfgFarEndMaxCellConcatenation_Type())
jnxpwAtmCfgFarEndMaxCellConcatenation.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmCfgFarEndMaxCellConcatenation.setStatus(_A)
class _JnxpwAtmCfgTimeoutMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('disabled',2),('enabled',3)))
_JnxpwAtmCfgTimeoutMode_Type.__name__=_J
_JnxpwAtmCfgTimeoutMode_Object=MibTableColumn
jnxpwAtmCfgTimeoutMode=_JnxpwAtmCfgTimeoutMode_Object((1,3,6,1,4,1,2636,3,57,1,1,1,3),_JnxpwAtmCfgTimeoutMode_Type())
jnxpwAtmCfgTimeoutMode.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmCfgTimeoutMode.setStatus(_A)
_JnxpwAtmClpQosMapping_Type=TruthValue
_JnxpwAtmClpQosMapping_Object=MibTableColumn
jnxpwAtmClpQosMapping=_JnxpwAtmClpQosMapping_Object((1,3,6,1,4,1,2636,3,57,1,1,1,4),_JnxpwAtmClpQosMapping_Type())
jnxpwAtmClpQosMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmClpQosMapping.setStatus(_A)
_JnxpwAtmOutboundNto1Table_Object=MibTable
jnxpwAtmOutboundNto1Table=_JnxpwAtmOutboundNto1Table_Object((1,3,6,1,4,1,2636,3,57,1,2))
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1Table.setStatus(_A)
_JnxpwAtmOutboundNto1Entry_Object=MibTableRow
jnxpwAtmOutboundNto1Entry=_JnxpwAtmOutboundNto1Entry_Object((1,3,6,1,4,1,2636,3,57,1,2,1))
jnxpwAtmOutboundNto1Entry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1Entry.setStatus(_A)
_JnxpwAtmOutboundNto1AtmIf_Type=InterfaceIndex
_JnxpwAtmOutboundNto1AtmIf_Object=MibTableColumn
jnxpwAtmOutboundNto1AtmIf=_JnxpwAtmOutboundNto1AtmIf_Object((1,3,6,1,4,1,2636,3,57,1,2,1,1),_JnxpwAtmOutboundNto1AtmIf_Type())
jnxpwAtmOutboundNto1AtmIf.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1AtmIf.setStatus(_A)
_JnxpwAtmOutboundNto1Vpi_Type=AtmVpIdentifier
_JnxpwAtmOutboundNto1Vpi_Object=MibTableColumn
jnxpwAtmOutboundNto1Vpi=_JnxpwAtmOutboundNto1Vpi_Object((1,3,6,1,4,1,2636,3,57,1,2,1,2),_JnxpwAtmOutboundNto1Vpi_Type())
jnxpwAtmOutboundNto1Vpi.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1Vpi.setStatus(_A)
_JnxpwAtmOutboundNto1Vci_Type=AtmVcIdentifier
_JnxpwAtmOutboundNto1Vci_Object=MibTableColumn
jnxpwAtmOutboundNto1Vci=_JnxpwAtmOutboundNto1Vci_Object((1,3,6,1,4,1,2636,3,57,1,2,1,3),_JnxpwAtmOutboundNto1Vci_Type())
jnxpwAtmOutboundNto1Vci.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1Vci.setStatus(_A)
_JnxpwAtmOutboundNto1RowStatus_Type=RowStatus
_JnxpwAtmOutboundNto1RowStatus_Object=MibTableColumn
jnxpwAtmOutboundNto1RowStatus=_JnxpwAtmOutboundNto1RowStatus_Object((1,3,6,1,4,1,2636,3,57,1,2,1,4),_JnxpwAtmOutboundNto1RowStatus_Type())
jnxpwAtmOutboundNto1RowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1RowStatus.setStatus(_A)
_JnxpwAtmOutboundNto1TrafficParamDescr_Type=RowPointer
_JnxpwAtmOutboundNto1TrafficParamDescr_Object=MibTableColumn
jnxpwAtmOutboundNto1TrafficParamDescr=_JnxpwAtmOutboundNto1TrafficParamDescr_Object((1,3,6,1,4,1,2636,3,57,1,2,1,5),_JnxpwAtmOutboundNto1TrafficParamDescr_Type())
jnxpwAtmOutboundNto1TrafficParamDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1TrafficParamDescr.setStatus(_A)
_JnxpwAtmOutboundNto1MappedVpi_Type=AtmVpIdentifier
_JnxpwAtmOutboundNto1MappedVpi_Object=MibTableColumn
jnxpwAtmOutboundNto1MappedVpi=_JnxpwAtmOutboundNto1MappedVpi_Object((1,3,6,1,4,1,2636,3,57,1,2,1,6),_JnxpwAtmOutboundNto1MappedVpi_Type())
jnxpwAtmOutboundNto1MappedVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1MappedVpi.setStatus(_A)
_JnxpwAtmOutboundNto1MappedVci_Type=AtmVcIdentifier
_JnxpwAtmOutboundNto1MappedVci_Object=MibTableColumn
jnxpwAtmOutboundNto1MappedVci=_JnxpwAtmOutboundNto1MappedVci_Object((1,3,6,1,4,1,2636,3,57,1,2,1,7),_JnxpwAtmOutboundNto1MappedVci_Type())
jnxpwAtmOutboundNto1MappedVci.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmOutboundNto1MappedVci.setStatus(_A)
_JnxpwAtmInboundNto1Table_Object=MibTable
jnxpwAtmInboundNto1Table=_JnxpwAtmInboundNto1Table_Object((1,3,6,1,4,1,2636,3,57,1,3))
if mibBuilder.loadTexts:jnxpwAtmInboundNto1Table.setStatus(_A)
_JnxpwAtmInboundNto1Entry_Object=MibTableRow
jnxpwAtmInboundNto1Entry=_JnxpwAtmInboundNto1Entry_Object((1,3,6,1,4,1,2636,3,57,1,3,1))
jnxpwAtmInboundNto1Entry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:jnxpwAtmInboundNto1Entry.setStatus(_A)
_JnxpwAtmInboundNto1AtmIf_Type=InterfaceIndex
_JnxpwAtmInboundNto1AtmIf_Object=MibTableColumn
jnxpwAtmInboundNto1AtmIf=_JnxpwAtmInboundNto1AtmIf_Object((1,3,6,1,4,1,2636,3,57,1,3,1,1),_JnxpwAtmInboundNto1AtmIf_Type())
jnxpwAtmInboundNto1AtmIf.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmInboundNto1AtmIf.setStatus(_A)
_JnxpwAtmInboundNto1Vpi_Type=AtmVpIdentifier
_JnxpwAtmInboundNto1Vpi_Object=MibTableColumn
jnxpwAtmInboundNto1Vpi=_JnxpwAtmInboundNto1Vpi_Object((1,3,6,1,4,1,2636,3,57,1,3,1,2),_JnxpwAtmInboundNto1Vpi_Type())
jnxpwAtmInboundNto1Vpi.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmInboundNto1Vpi.setStatus(_A)
_JnxpwAtmInboundNto1Vci_Type=AtmVcIdentifier
_JnxpwAtmInboundNto1Vci_Object=MibTableColumn
jnxpwAtmInboundNto1Vci=_JnxpwAtmInboundNto1Vci_Object((1,3,6,1,4,1,2636,3,57,1,3,1,3),_JnxpwAtmInboundNto1Vci_Type())
jnxpwAtmInboundNto1Vci.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmInboundNto1Vci.setStatus(_A)
_JnxpwAtmInboundNto1RowStatus_Type=RowStatus
_JnxpwAtmInboundNto1RowStatus_Object=MibTableColumn
jnxpwAtmInboundNto1RowStatus=_JnxpwAtmInboundNto1RowStatus_Object((1,3,6,1,4,1,2636,3,57,1,3,1,4),_JnxpwAtmInboundNto1RowStatus_Type())
jnxpwAtmInboundNto1RowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmInboundNto1RowStatus.setStatus(_A)
_JnxpwAtmInboundNto1TrafficParamDescr_Type=RowPointer
_JnxpwAtmInboundNto1TrafficParamDescr_Object=MibTableColumn
jnxpwAtmInboundNto1TrafficParamDescr=_JnxpwAtmInboundNto1TrafficParamDescr_Object((1,3,6,1,4,1,2636,3,57,1,3,1,5),_JnxpwAtmInboundNto1TrafficParamDescr_Type())
jnxpwAtmInboundNto1TrafficParamDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmInboundNto1TrafficParamDescr.setStatus(_A)
_JnxpwAtmInboundNto1MappedVpi_Type=AtmVpIdentifier
_JnxpwAtmInboundNto1MappedVpi_Object=MibTableColumn
jnxpwAtmInboundNto1MappedVpi=_JnxpwAtmInboundNto1MappedVpi_Object((1,3,6,1,4,1,2636,3,57,1,3,1,6),_JnxpwAtmInboundNto1MappedVpi_Type())
jnxpwAtmInboundNto1MappedVpi.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmInboundNto1MappedVpi.setStatus(_A)
_JnxpwAtmInboundNto1MappedVci_Type=AtmVcIdentifier
_JnxpwAtmInboundNto1MappedVci_Object=MibTableColumn
jnxpwAtmInboundNto1MappedVci=_JnxpwAtmInboundNto1MappedVci_Object((1,3,6,1,4,1,2636,3,57,1,3,1,7),_JnxpwAtmInboundNto1MappedVci_Type())
jnxpwAtmInboundNto1MappedVci.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmInboundNto1MappedVci.setStatus(_A)
_JnxpwAtmPerfCurrentTable_Object=MibTable
jnxpwAtmPerfCurrentTable=_JnxpwAtmPerfCurrentTable_Object((1,3,6,1,4,1,2636,3,57,1,4))
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentTable.setStatus(_A)
_JnxpwAtmPerfCurrentEntry_Object=MibTableRow
jnxpwAtmPerfCurrentEntry=_JnxpwAtmPerfCurrentEntry_Object((1,3,6,1,4,1,2636,3,57,1,4,1))
jnxpwAtmPerfCurrentEntry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_C,_E))
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentEntry.setStatus(_A)
_JnxpwAtmPerfCurrentMissingPkts_Type=PerfCurrentCount
_JnxpwAtmPerfCurrentMissingPkts_Object=MibTableColumn
jnxpwAtmPerfCurrentMissingPkts=_JnxpwAtmPerfCurrentMissingPkts_Object((1,3,6,1,4,1,2636,3,57,1,4,1,1),_JnxpwAtmPerfCurrentMissingPkts_Type())
jnxpwAtmPerfCurrentMissingPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentMissingPkts.setStatus(_A)
_JnxpwAtmPerfCurrentPktsReOrder_Type=PerfCurrentCount
_JnxpwAtmPerfCurrentPktsReOrder_Object=MibTableColumn
jnxpwAtmPerfCurrentPktsReOrder=_JnxpwAtmPerfCurrentPktsReOrder_Object((1,3,6,1,4,1,2636,3,57,1,4,1,2),_JnxpwAtmPerfCurrentPktsReOrder_Type())
jnxpwAtmPerfCurrentPktsReOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentPktsReOrder.setStatus(_A)
_JnxpwAtmPerfCurrentPktsMisOrder_Type=PerfCurrentCount
_JnxpwAtmPerfCurrentPktsMisOrder_Object=MibTableColumn
jnxpwAtmPerfCurrentPktsMisOrder=_JnxpwAtmPerfCurrentPktsMisOrder_Object((1,3,6,1,4,1,2636,3,57,1,4,1,3),_JnxpwAtmPerfCurrentPktsMisOrder_Type())
jnxpwAtmPerfCurrentPktsMisOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentPktsMisOrder.setStatus(_A)
_JnxpwAtmPerfCurrentPktsTimeout_Type=PerfCurrentCount
_JnxpwAtmPerfCurrentPktsTimeout_Object=MibTableColumn
jnxpwAtmPerfCurrentPktsTimeout=_JnxpwAtmPerfCurrentPktsTimeout_Object((1,3,6,1,4,1,2636,3,57,1,4,1,4),_JnxpwAtmPerfCurrentPktsTimeout_Type())
jnxpwAtmPerfCurrentPktsTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentPktsTimeout.setStatus(_A)
_JnxpwAtmPerfCurrentPktsXmit_Type=Counter64
_JnxpwAtmPerfCurrentPktsXmit_Object=MibTableColumn
jnxpwAtmPerfCurrentPktsXmit=_JnxpwAtmPerfCurrentPktsXmit_Object((1,3,6,1,4,1,2636,3,57,1,4,1,5),_JnxpwAtmPerfCurrentPktsXmit_Type())
jnxpwAtmPerfCurrentPktsXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentPktsXmit.setStatus(_A)
_JnxpwAtmPerfCurrentCellsDropped_Type=PerfCurrentCount
_JnxpwAtmPerfCurrentCellsDropped_Object=MibTableColumn
jnxpwAtmPerfCurrentCellsDropped=_JnxpwAtmPerfCurrentCellsDropped_Object((1,3,6,1,4,1,2636,3,57,1,4,1,6),_JnxpwAtmPerfCurrentCellsDropped_Type())
jnxpwAtmPerfCurrentCellsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentCellsDropped.setStatus(_A)
_JnxpwAtmPerfCurrentPktsReceived_Type=Counter64
_JnxpwAtmPerfCurrentPktsReceived_Object=MibTableColumn
jnxpwAtmPerfCurrentPktsReceived=_JnxpwAtmPerfCurrentPktsReceived_Object((1,3,6,1,4,1,2636,3,57,1,4,1,7),_JnxpwAtmPerfCurrentPktsReceived_Type())
jnxpwAtmPerfCurrentPktsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentPktsReceived.setStatus(_A)
_JnxpwAtmPerfCurrentUnknownCells_Type=Counter64
_JnxpwAtmPerfCurrentUnknownCells_Object=MibTableColumn
jnxpwAtmPerfCurrentUnknownCells=_JnxpwAtmPerfCurrentUnknownCells_Object((1,3,6,1,4,1,2636,3,57,1,4,1,8),_JnxpwAtmPerfCurrentUnknownCells_Type())
jnxpwAtmPerfCurrentUnknownCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfCurrentUnknownCells.setStatus(_A)
_JnxpwAtmPerfIntervalTable_Object=MibTable
jnxpwAtmPerfIntervalTable=_JnxpwAtmPerfIntervalTable_Object((1,3,6,1,4,1,2636,3,57,1,5))
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalTable.setStatus(_A)
_JnxpwAtmPerfIntervalEntry_Object=MibTableRow
jnxpwAtmPerfIntervalEntry=_JnxpwAtmPerfIntervalEntry_Object((1,3,6,1,4,1,2636,3,57,1,5,1))
jnxpwAtmPerfIntervalEntry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_C,_E),(0,_I,_K))
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalEntry.setStatus(_A)
class _JnxpwAtmPerfIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_JnxpwAtmPerfIntervalNumber_Type.__name__=_H
_JnxpwAtmPerfIntervalNumber_Object=MibTableColumn
jnxpwAtmPerfIntervalNumber=_JnxpwAtmPerfIntervalNumber_Object((1,3,6,1,4,1,2636,3,57,1,5,1,1),_JnxpwAtmPerfIntervalNumber_Type())
jnxpwAtmPerfIntervalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalNumber.setStatus(_A)
_JnxpwAtmPerfIntervalValidData_Type=TruthValue
_JnxpwAtmPerfIntervalValidData_Object=MibTableColumn
jnxpwAtmPerfIntervalValidData=_JnxpwAtmPerfIntervalValidData_Object((1,3,6,1,4,1,2636,3,57,1,5,1,2),_JnxpwAtmPerfIntervalValidData_Type())
jnxpwAtmPerfIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalValidData.setStatus(_A)
_JnxpwAtmPerfIntervalDuration_Type=Unsigned32
_JnxpwAtmPerfIntervalDuration_Object=MibTableColumn
jnxpwAtmPerfIntervalDuration=_JnxpwAtmPerfIntervalDuration_Object((1,3,6,1,4,1,2636,3,57,1,5,1,3),_JnxpwAtmPerfIntervalDuration_Type())
jnxpwAtmPerfIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalDuration.setStatus(_A)
_JnxpwAtmPerfIntervalMissingPkts_Type=PerfIntervalCount
_JnxpwAtmPerfIntervalMissingPkts_Object=MibTableColumn
jnxpwAtmPerfIntervalMissingPkts=_JnxpwAtmPerfIntervalMissingPkts_Object((1,3,6,1,4,1,2636,3,57,1,5,1,4),_JnxpwAtmPerfIntervalMissingPkts_Type())
jnxpwAtmPerfIntervalMissingPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalMissingPkts.setStatus(_A)
_JnxpwAtmPerfIntervalPktsReOrder_Type=PerfIntervalCount
_JnxpwAtmPerfIntervalPktsReOrder_Object=MibTableColumn
jnxpwAtmPerfIntervalPktsReOrder=_JnxpwAtmPerfIntervalPktsReOrder_Object((1,3,6,1,4,1,2636,3,57,1,5,1,5),_JnxpwAtmPerfIntervalPktsReOrder_Type())
jnxpwAtmPerfIntervalPktsReOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalPktsReOrder.setStatus(_A)
_JnxpwAtmPerfIntervalPktsMisOrder_Type=PerfIntervalCount
_JnxpwAtmPerfIntervalPktsMisOrder_Object=MibTableColumn
jnxpwAtmPerfIntervalPktsMisOrder=_JnxpwAtmPerfIntervalPktsMisOrder_Object((1,3,6,1,4,1,2636,3,57,1,5,1,6),_JnxpwAtmPerfIntervalPktsMisOrder_Type())
jnxpwAtmPerfIntervalPktsMisOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalPktsMisOrder.setStatus(_A)
_JnxpwAtmPerfIntervalPktsTimeout_Type=PerfIntervalCount
_JnxpwAtmPerfIntervalPktsTimeout_Object=MibTableColumn
jnxpwAtmPerfIntervalPktsTimeout=_JnxpwAtmPerfIntervalPktsTimeout_Object((1,3,6,1,4,1,2636,3,57,1,5,1,7),_JnxpwAtmPerfIntervalPktsTimeout_Type())
jnxpwAtmPerfIntervalPktsTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalPktsTimeout.setStatus(_A)
_JnxpwAtmPerfIntervalPktsXmit_Type=Counter64
_JnxpwAtmPerfIntervalPktsXmit_Object=MibTableColumn
jnxpwAtmPerfIntervalPktsXmit=_JnxpwAtmPerfIntervalPktsXmit_Object((1,3,6,1,4,1,2636,3,57,1,5,1,8),_JnxpwAtmPerfIntervalPktsXmit_Type())
jnxpwAtmPerfIntervalPktsXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalPktsXmit.setStatus(_A)
_JnxpwAtmPerfIntervalCellsDropped_Type=PerfIntervalCount
_JnxpwAtmPerfIntervalCellsDropped_Object=MibTableColumn
jnxpwAtmPerfIntervalCellsDropped=_JnxpwAtmPerfIntervalCellsDropped_Object((1,3,6,1,4,1,2636,3,57,1,5,1,9),_JnxpwAtmPerfIntervalCellsDropped_Type())
jnxpwAtmPerfIntervalCellsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalCellsDropped.setStatus(_A)
_JnxpwAtmPerfIntervalPktsReceived_Type=Counter64
_JnxpwAtmPerfIntervalPktsReceived_Object=MibTableColumn
jnxpwAtmPerfIntervalPktsReceived=_JnxpwAtmPerfIntervalPktsReceived_Object((1,3,6,1,4,1,2636,3,57,1,5,1,10),_JnxpwAtmPerfIntervalPktsReceived_Type())
jnxpwAtmPerfIntervalPktsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalPktsReceived.setStatus(_A)
_JnxpwAtmPerfIntervalUnknownCells_Type=Counter64
_JnxpwAtmPerfIntervalUnknownCells_Object=MibTableColumn
jnxpwAtmPerfIntervalUnknownCells=_JnxpwAtmPerfIntervalUnknownCells_Object((1,3,6,1,4,1,2636,3,57,1,5,1,11),_JnxpwAtmPerfIntervalUnknownCells_Type())
jnxpwAtmPerfIntervalUnknownCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerfIntervalUnknownCells.setStatus(_A)
_JnxpwAtmPerf1DayIntervalTable_Object=MibTable
jnxpwAtmPerf1DayIntervalTable=_JnxpwAtmPerf1DayIntervalTable_Object((1,3,6,1,4,1,2636,3,57,1,6))
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalTable.setStatus(_A)
_JnxpwAtmPerf1DayIntervalEntry_Object=MibTableRow
jnxpwAtmPerf1DayIntervalEntry=_JnxpwAtmPerf1DayIntervalEntry_Object((1,3,6,1,4,1,2636,3,57,1,6,1))
jnxpwAtmPerf1DayIntervalEntry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_C,_E),(0,_I,_L))
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalEntry.setStatus(_A)
class _JnxpwAtmPerf1DayIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,365))
_JnxpwAtmPerf1DayIntervalNumber_Type.__name__=_H
_JnxpwAtmPerf1DayIntervalNumber_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalNumber=_JnxpwAtmPerf1DayIntervalNumber_Object((1,3,6,1,4,1,2636,3,57,1,6,1,1),_JnxpwAtmPerf1DayIntervalNumber_Type())
jnxpwAtmPerf1DayIntervalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalNumber.setStatus(_A)
_JnxpwAtmPerf1DayIntervalValidData_Type=TruthValue
_JnxpwAtmPerf1DayIntervalValidData_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalValidData=_JnxpwAtmPerf1DayIntervalValidData_Object((1,3,6,1,4,1,2636,3,57,1,6,1,2),_JnxpwAtmPerf1DayIntervalValidData_Type())
jnxpwAtmPerf1DayIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalValidData.setStatus(_A)
_JnxpwAtmPerf1DayIntervalDuration_Type=Unsigned32
_JnxpwAtmPerf1DayIntervalDuration_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalDuration=_JnxpwAtmPerf1DayIntervalDuration_Object((1,3,6,1,4,1,2636,3,57,1,6,1,3),_JnxpwAtmPerf1DayIntervalDuration_Type())
jnxpwAtmPerf1DayIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalDuration.setStatus(_A)
_JnxpwAtmPerf1DayIntervalMissingPkts_Type=Counter32
_JnxpwAtmPerf1DayIntervalMissingPkts_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalMissingPkts=_JnxpwAtmPerf1DayIntervalMissingPkts_Object((1,3,6,1,4,1,2636,3,57,1,6,1,4),_JnxpwAtmPerf1DayIntervalMissingPkts_Type())
jnxpwAtmPerf1DayIntervalMissingPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalMissingPkts.setStatus(_A)
_JnxpwAtmPerf1DayIntervalPktsReOrder_Type=Counter32
_JnxpwAtmPerf1DayIntervalPktsReOrder_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalPktsReOrder=_JnxpwAtmPerf1DayIntervalPktsReOrder_Object((1,3,6,1,4,1,2636,3,57,1,6,1,5),_JnxpwAtmPerf1DayIntervalPktsReOrder_Type())
jnxpwAtmPerf1DayIntervalPktsReOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalPktsReOrder.setStatus(_A)
_JnxpwAtmPerf1DayIntervalPktsMisOrder_Type=Counter32
_JnxpwAtmPerf1DayIntervalPktsMisOrder_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalPktsMisOrder=_JnxpwAtmPerf1DayIntervalPktsMisOrder_Object((1,3,6,1,4,1,2636,3,57,1,6,1,6),_JnxpwAtmPerf1DayIntervalPktsMisOrder_Type())
jnxpwAtmPerf1DayIntervalPktsMisOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalPktsMisOrder.setStatus(_A)
_JnxpwAtmPerf1DayIntervalPktsTimeout_Type=Counter32
_JnxpwAtmPerf1DayIntervalPktsTimeout_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalPktsTimeout=_JnxpwAtmPerf1DayIntervalPktsTimeout_Object((1,3,6,1,4,1,2636,3,57,1,6,1,7),_JnxpwAtmPerf1DayIntervalPktsTimeout_Type())
jnxpwAtmPerf1DayIntervalPktsTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalPktsTimeout.setStatus(_A)
_JnxpwAtmPerf1DayIntervalPktsXmit_Type=Counter64
_JnxpwAtmPerf1DayIntervalPktsXmit_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalPktsXmit=_JnxpwAtmPerf1DayIntervalPktsXmit_Object((1,3,6,1,4,1,2636,3,57,1,6,1,8),_JnxpwAtmPerf1DayIntervalPktsXmit_Type())
jnxpwAtmPerf1DayIntervalPktsXmit.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalPktsXmit.setStatus(_A)
_JnxpwAtmPerf1DayIntervalCellsDropped_Type=Counter32
_JnxpwAtmPerf1DayIntervalCellsDropped_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalCellsDropped=_JnxpwAtmPerf1DayIntervalCellsDropped_Object((1,3,6,1,4,1,2636,3,57,1,6,1,9),_JnxpwAtmPerf1DayIntervalCellsDropped_Type())
jnxpwAtmPerf1DayIntervalCellsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalCellsDropped.setStatus(_A)
_JnxpwAtmPerf1DayIntervalPktsReceived_Type=Counter64
_JnxpwAtmPerf1DayIntervalPktsReceived_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalPktsReceived=_JnxpwAtmPerf1DayIntervalPktsReceived_Object((1,3,6,1,4,1,2636,3,57,1,6,1,10),_JnxpwAtmPerf1DayIntervalPktsReceived_Type())
jnxpwAtmPerf1DayIntervalPktsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalPktsReceived.setStatus(_A)
_JnxpwAtmPerf1DayIntervalUnknownCells_Type=Counter64
_JnxpwAtmPerf1DayIntervalUnknownCells_Object=MibTableColumn
jnxpwAtmPerf1DayIntervalUnknownCells=_JnxpwAtmPerf1DayIntervalUnknownCells_Object((1,3,6,1,4,1,2636,3,57,1,6,1,11),_JnxpwAtmPerf1DayIntervalUnknownCells_Type())
jnxpwAtmPerf1DayIntervalUnknownCells.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxpwAtmPerf1DayIntervalUnknownCells.setStatus(_A)
_JnxpwAtmConformance_ObjectIdentity=ObjectIdentity
jnxpwAtmConformance=_JnxpwAtmConformance_ObjectIdentity((1,3,6,1,4,1,2636,3,57,2))
mibBuilder.exportSymbols(_I,**{'jnxPWAtmMIB':jnxPWAtmMIB,'jnxpwAtmNotifications':jnxpwAtmNotifications,'jnxpwAtmObjects':jnxpwAtmObjects,'jnxpwAtmCfgTable':jnxpwAtmCfgTable,'jnxpwAtmCfgEntry':jnxpwAtmCfgEntry,'jnxpwAtmCfgMaxCellConcatenation':jnxpwAtmCfgMaxCellConcatenation,'jnxpwAtmCfgFarEndMaxCellConcatenation':jnxpwAtmCfgFarEndMaxCellConcatenation,'jnxpwAtmCfgTimeoutMode':jnxpwAtmCfgTimeoutMode,'jnxpwAtmClpQosMapping':jnxpwAtmClpQosMapping,'jnxpwAtmOutboundNto1Table':jnxpwAtmOutboundNto1Table,'jnxpwAtmOutboundNto1Entry':jnxpwAtmOutboundNto1Entry,'jnxpwAtmOutboundNto1AtmIf':jnxpwAtmOutboundNto1AtmIf,'jnxpwAtmOutboundNto1Vpi':jnxpwAtmOutboundNto1Vpi,'jnxpwAtmOutboundNto1Vci':jnxpwAtmOutboundNto1Vci,'jnxpwAtmOutboundNto1RowStatus':jnxpwAtmOutboundNto1RowStatus,'jnxpwAtmOutboundNto1TrafficParamDescr':jnxpwAtmOutboundNto1TrafficParamDescr,'jnxpwAtmOutboundNto1MappedVpi':jnxpwAtmOutboundNto1MappedVpi,'jnxpwAtmOutboundNto1MappedVci':jnxpwAtmOutboundNto1MappedVci,'jnxpwAtmInboundNto1Table':jnxpwAtmInboundNto1Table,'jnxpwAtmInboundNto1Entry':jnxpwAtmInboundNto1Entry,'jnxpwAtmInboundNto1AtmIf':jnxpwAtmInboundNto1AtmIf,'jnxpwAtmInboundNto1Vpi':jnxpwAtmInboundNto1Vpi,'jnxpwAtmInboundNto1Vci':jnxpwAtmInboundNto1Vci,'jnxpwAtmInboundNto1RowStatus':jnxpwAtmInboundNto1RowStatus,'jnxpwAtmInboundNto1TrafficParamDescr':jnxpwAtmInboundNto1TrafficParamDescr,'jnxpwAtmInboundNto1MappedVpi':jnxpwAtmInboundNto1MappedVpi,'jnxpwAtmInboundNto1MappedVci':jnxpwAtmInboundNto1MappedVci,'jnxpwAtmPerfCurrentTable':jnxpwAtmPerfCurrentTable,'jnxpwAtmPerfCurrentEntry':jnxpwAtmPerfCurrentEntry,'jnxpwAtmPerfCurrentMissingPkts':jnxpwAtmPerfCurrentMissingPkts,'jnxpwAtmPerfCurrentPktsReOrder':jnxpwAtmPerfCurrentPktsReOrder,'jnxpwAtmPerfCurrentPktsMisOrder':jnxpwAtmPerfCurrentPktsMisOrder,'jnxpwAtmPerfCurrentPktsTimeout':jnxpwAtmPerfCurrentPktsTimeout,'jnxpwAtmPerfCurrentPktsXmit':jnxpwAtmPerfCurrentPktsXmit,'jnxpwAtmPerfCurrentCellsDropped':jnxpwAtmPerfCurrentCellsDropped,'jnxpwAtmPerfCurrentPktsReceived':jnxpwAtmPerfCurrentPktsReceived,'jnxpwAtmPerfCurrentUnknownCells':jnxpwAtmPerfCurrentUnknownCells,'jnxpwAtmPerfIntervalTable':jnxpwAtmPerfIntervalTable,'jnxpwAtmPerfIntervalEntry':jnxpwAtmPerfIntervalEntry,_K:jnxpwAtmPerfIntervalNumber,'jnxpwAtmPerfIntervalValidData':jnxpwAtmPerfIntervalValidData,'jnxpwAtmPerfIntervalDuration':jnxpwAtmPerfIntervalDuration,'jnxpwAtmPerfIntervalMissingPkts':jnxpwAtmPerfIntervalMissingPkts,'jnxpwAtmPerfIntervalPktsReOrder':jnxpwAtmPerfIntervalPktsReOrder,'jnxpwAtmPerfIntervalPktsMisOrder':jnxpwAtmPerfIntervalPktsMisOrder,'jnxpwAtmPerfIntervalPktsTimeout':jnxpwAtmPerfIntervalPktsTimeout,'jnxpwAtmPerfIntervalPktsXmit':jnxpwAtmPerfIntervalPktsXmit,'jnxpwAtmPerfIntervalCellsDropped':jnxpwAtmPerfIntervalCellsDropped,'jnxpwAtmPerfIntervalPktsReceived':jnxpwAtmPerfIntervalPktsReceived,'jnxpwAtmPerfIntervalUnknownCells':jnxpwAtmPerfIntervalUnknownCells,'jnxpwAtmPerf1DayIntervalTable':jnxpwAtmPerf1DayIntervalTable,'jnxpwAtmPerf1DayIntervalEntry':jnxpwAtmPerf1DayIntervalEntry,_L:jnxpwAtmPerf1DayIntervalNumber,'jnxpwAtmPerf1DayIntervalValidData':jnxpwAtmPerf1DayIntervalValidData,'jnxpwAtmPerf1DayIntervalDuration':jnxpwAtmPerf1DayIntervalDuration,'jnxpwAtmPerf1DayIntervalMissingPkts':jnxpwAtmPerf1DayIntervalMissingPkts,'jnxpwAtmPerf1DayIntervalPktsReOrder':jnxpwAtmPerf1DayIntervalPktsReOrder,'jnxpwAtmPerf1DayIntervalPktsMisOrder':jnxpwAtmPerf1DayIntervalPktsMisOrder,'jnxpwAtmPerf1DayIntervalPktsTimeout':jnxpwAtmPerf1DayIntervalPktsTimeout,'jnxpwAtmPerf1DayIntervalPktsXmit':jnxpwAtmPerf1DayIntervalPktsXmit,'jnxpwAtmPerf1DayIntervalCellsDropped':jnxpwAtmPerf1DayIntervalCellsDropped,'jnxpwAtmPerf1DayIntervalPktsReceived':jnxpwAtmPerf1DayIntervalPktsReceived,'jnxpwAtmPerf1DayIntervalUnknownCells':jnxpwAtmPerf1DayIntervalUnknownCells,'jnxpwAtmConformance':jnxpwAtmConformance})