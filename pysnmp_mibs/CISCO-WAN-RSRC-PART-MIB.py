_A0='cwRsrcSvcAggrGroup'
_z='cwRsrcSvcAggrRowStatus'
_y='cwRsrcSvcAggrChanVADDutyCycle'
_x='cwRsrcSvcAggrChanVADTolerance'
_w='cwRsrcSvcAggrIngPctBw'
_v='cwRsrcSvcAggrEgrPctBw'
_u='cwRsrcSvcAggrVpiHigh'
_t='cwRsrcSvcAggrVpiLow'
_s='cwRsrcPartCtlrRowStatus'
_r='cwRsrcPartIlmiConPollInactFactor'
_q='cwRsrcPartIlmiCheckConPollIntvl'
_p='cwRsrcPartIlmiEstablishConPollIntvl'
_o='cwRsrcPartIlmiTrapEnable'
_n='cwRsrcPartSignallingVci'
_m='cwRsrcPartSignallingVpi'
_l='cwRsrcPartIlmiEnabled'
_k='cwRsrcPartRowStatus'
_j='cwRsrcPartAvailCon'
_i='cwRsrcPartUsedCon'
_h='cwRsrcPartMaxCon'
_g='cwRsrcPartGuarCon'
_f='cwRsrcPartVciHigh'
_e='cwRsrcPartVciLo'
_d='cwRsrcPartVpiHigh'
_c='cwRsrcPartVpiLo'
_b='cwRsrcPartIngPctBwUsed'
_a='cwRsrcPartEgrPctBwUsed'
_Z='cwRsrcPartIngPctBwAvail'
_Y='cwRsrcPartEgrPctBwAvail'
_X='cwRsrcPartIngMaxPctBwConf'
_W='cwRsrcPartIngGuarPctBwConf'
_V='cwRsrcPartEgrMaxPctBwConf'
_U='cwRsrcPartEgrGuarPctBwConf'
_T='cwRsrcPartController'
_S='percent'
_R='cwRsrcPartCtlrController'
_Q='seconds'
_P='not-accessible'
_O='TruthValue'
_N='cwRsrcPartMappingGroup'
_M='cwRsrcPartIlmiMIBGroup'
_L='cwRsrcPartMIBGroup'
_K='cwRsrcPartID'
_J='ifIndex'
_I='IF-MIB'
_H='read-only'
_G='read-write'
_F='Integer32'
_E='0.0001 percentage'
_D='read-create'
_C='Unsigned32'
_B='CISCO-WAN-RSRC-PART-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_O)
ciscoWANRsrcPartMIB=ModuleIdentity((1,3,6,1,4,1,9,9,125))
if mibBuilder.loadTexts:ciscoWANRsrcPartMIB.setRevisions(('2002-09-14 00:00','2002-03-06 00:00','1999-10-12 00:00'))
_CiscoWANRsrcPartMIBObjects_ObjectIdentity=ObjectIdentity
ciscoWANRsrcPartMIBObjects=_CiscoWANRsrcPartMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,125,1))
_CwRsrcPartConfGrp_ObjectIdentity=ObjectIdentity
cwRsrcPartConfGrp=_CwRsrcPartConfGrp_ObjectIdentity((1,3,6,1,4,1,9,9,125,1,1))
_CwRsrcPartConfTable_Object=MibTable
cwRsrcPartConfTable=_CwRsrcPartConfTable_Object((1,3,6,1,4,1,9,9,125,1,1,1))
if mibBuilder.loadTexts:cwRsrcPartConfTable.setStatus(_A)
_CwRsrcPartConfEntry_Object=MibTableRow
cwRsrcPartConfEntry=_CwRsrcPartConfEntry_Object((1,3,6,1,4,1,9,9,125,1,1,1,1))
cwRsrcPartConfEntry.setIndexNames((0,_I,_J),(0,_B,_K))
if mibBuilder.loadTexts:cwRsrcPartConfEntry.setStatus(_A)
class _CwRsrcPartID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CwRsrcPartID_Type.__name__=_C
_CwRsrcPartID_Object=MibTableColumn
cwRsrcPartID=_CwRsrcPartID_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,1),_CwRsrcPartID_Type())
cwRsrcPartID.setMaxAccess(_P)
if mibBuilder.loadTexts:cwRsrcPartID.setStatus(_A)
class _CwRsrcPartController_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CwRsrcPartController_Type.__name__=_C
_CwRsrcPartController_Object=MibTableColumn
cwRsrcPartController=_CwRsrcPartController_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,2),_CwRsrcPartController_Type())
cwRsrcPartController.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartController.setStatus(_A)
class _CwRsrcPartEgrGuarPctBwConf_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartEgrGuarPctBwConf_Type.__name__=_C
_CwRsrcPartEgrGuarPctBwConf_Object=MibTableColumn
cwRsrcPartEgrGuarPctBwConf=_CwRsrcPartEgrGuarPctBwConf_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,3),_CwRsrcPartEgrGuarPctBwConf_Type())
cwRsrcPartEgrGuarPctBwConf.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartEgrGuarPctBwConf.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartEgrGuarPctBwConf.setUnits(_E)
class _CwRsrcPartEgrMaxPctBwConf_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartEgrMaxPctBwConf_Type.__name__=_C
_CwRsrcPartEgrMaxPctBwConf_Object=MibTableColumn
cwRsrcPartEgrMaxPctBwConf=_CwRsrcPartEgrMaxPctBwConf_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,4),_CwRsrcPartEgrMaxPctBwConf_Type())
cwRsrcPartEgrMaxPctBwConf.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartEgrMaxPctBwConf.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartEgrMaxPctBwConf.setUnits(_E)
class _CwRsrcPartIngGuarPctBwConf_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartIngGuarPctBwConf_Type.__name__=_C
_CwRsrcPartIngGuarPctBwConf_Object=MibTableColumn
cwRsrcPartIngGuarPctBwConf=_CwRsrcPartIngGuarPctBwConf_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,5),_CwRsrcPartIngGuarPctBwConf_Type())
cwRsrcPartIngGuarPctBwConf.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartIngGuarPctBwConf.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartIngGuarPctBwConf.setUnits(_E)
class _CwRsrcPartIngMaxPctBwConf_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartIngMaxPctBwConf_Type.__name__=_C
_CwRsrcPartIngMaxPctBwConf_Object=MibTableColumn
cwRsrcPartIngMaxPctBwConf=_CwRsrcPartIngMaxPctBwConf_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,6),_CwRsrcPartIngMaxPctBwConf_Type())
cwRsrcPartIngMaxPctBwConf.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartIngMaxPctBwConf.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartIngMaxPctBwConf.setUnits(_E)
class _CwRsrcPartEgrPctBwUsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartEgrPctBwUsed_Type.__name__=_C
_CwRsrcPartEgrPctBwUsed_Object=MibTableColumn
cwRsrcPartEgrPctBwUsed=_CwRsrcPartEgrPctBwUsed_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,7),_CwRsrcPartEgrPctBwUsed_Type())
cwRsrcPartEgrPctBwUsed.setMaxAccess(_H)
if mibBuilder.loadTexts:cwRsrcPartEgrPctBwUsed.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartEgrPctBwUsed.setUnits(_E)
class _CwRsrcPartIngPctBwUsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartIngPctBwUsed_Type.__name__=_C
_CwRsrcPartIngPctBwUsed_Object=MibTableColumn
cwRsrcPartIngPctBwUsed=_CwRsrcPartIngPctBwUsed_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,8),_CwRsrcPartIngPctBwUsed_Type())
cwRsrcPartIngPctBwUsed.setMaxAccess(_H)
if mibBuilder.loadTexts:cwRsrcPartIngPctBwUsed.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartIngPctBwUsed.setUnits(_E)
class _CwRsrcPartEgrPctBwAvail_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartEgrPctBwAvail_Type.__name__=_C
_CwRsrcPartEgrPctBwAvail_Object=MibTableColumn
cwRsrcPartEgrPctBwAvail=_CwRsrcPartEgrPctBwAvail_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,9),_CwRsrcPartEgrPctBwAvail_Type())
cwRsrcPartEgrPctBwAvail.setMaxAccess(_H)
if mibBuilder.loadTexts:cwRsrcPartEgrPctBwAvail.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartEgrPctBwAvail.setUnits(_E)
class _CwRsrcPartIngPctBwAvail_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_CwRsrcPartIngPctBwAvail_Type.__name__=_C
_CwRsrcPartIngPctBwAvail_Object=MibTableColumn
cwRsrcPartIngPctBwAvail=_CwRsrcPartIngPctBwAvail_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,10),_CwRsrcPartIngPctBwAvail_Type())
cwRsrcPartIngPctBwAvail.setMaxAccess(_H)
if mibBuilder.loadTexts:cwRsrcPartIngPctBwAvail.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartIngPctBwAvail.setUnits(_E)
class _CwRsrcPartVpiLo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwRsrcPartVpiLo_Type.__name__=_C
_CwRsrcPartVpiLo_Object=MibTableColumn
cwRsrcPartVpiLo=_CwRsrcPartVpiLo_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,11),_CwRsrcPartVpiLo_Type())
cwRsrcPartVpiLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartVpiLo.setStatus(_A)
class _CwRsrcPartVpiHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwRsrcPartVpiHigh_Type.__name__=_C
_CwRsrcPartVpiHigh_Object=MibTableColumn
cwRsrcPartVpiHigh=_CwRsrcPartVpiHigh_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,12),_CwRsrcPartVpiHigh_Type())
cwRsrcPartVpiHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartVpiHigh.setStatus(_A)
class _CwRsrcPartVciLo_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwRsrcPartVciLo_Type.__name__=_C
_CwRsrcPartVciLo_Object=MibTableColumn
cwRsrcPartVciLo=_CwRsrcPartVciLo_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,13),_CwRsrcPartVciLo_Type())
cwRsrcPartVciLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartVciLo.setStatus(_A)
class _CwRsrcPartVciHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwRsrcPartVciHigh_Type.__name__=_C
_CwRsrcPartVciHigh_Object=MibTableColumn
cwRsrcPartVciHigh=_CwRsrcPartVciHigh_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,14),_CwRsrcPartVciHigh_Type())
cwRsrcPartVciHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartVciHigh.setStatus(_A)
class _CwRsrcPartGuarCon_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131072))
_CwRsrcPartGuarCon_Type.__name__=_C
_CwRsrcPartGuarCon_Object=MibTableColumn
cwRsrcPartGuarCon=_CwRsrcPartGuarCon_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,15),_CwRsrcPartGuarCon_Type())
cwRsrcPartGuarCon.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartGuarCon.setStatus(_A)
class _CwRsrcPartMaxCon_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131072))
_CwRsrcPartMaxCon_Type.__name__=_C
_CwRsrcPartMaxCon_Object=MibTableColumn
cwRsrcPartMaxCon=_CwRsrcPartMaxCon_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,16),_CwRsrcPartMaxCon_Type())
cwRsrcPartMaxCon.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartMaxCon.setStatus(_A)
class _CwRsrcPartUsedCon_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131072))
_CwRsrcPartUsedCon_Type.__name__=_C
_CwRsrcPartUsedCon_Object=MibTableColumn
cwRsrcPartUsedCon=_CwRsrcPartUsedCon_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,17),_CwRsrcPartUsedCon_Type())
cwRsrcPartUsedCon.setMaxAccess(_H)
if mibBuilder.loadTexts:cwRsrcPartUsedCon.setStatus(_A)
class _CwRsrcPartAvailCon_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131072))
_CwRsrcPartAvailCon_Type.__name__=_C
_CwRsrcPartAvailCon_Object=MibTableColumn
cwRsrcPartAvailCon=_CwRsrcPartAvailCon_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,18),_CwRsrcPartAvailCon_Type())
cwRsrcPartAvailCon.setMaxAccess(_H)
if mibBuilder.loadTexts:cwRsrcPartAvailCon.setStatus(_A)
_CwRsrcPartRowStatus_Type=RowStatus
_CwRsrcPartRowStatus_Object=MibTableColumn
cwRsrcPartRowStatus=_CwRsrcPartRowStatus_Object((1,3,6,1,4,1,9,9,125,1,1,1,1,19),_CwRsrcPartRowStatus_Type())
cwRsrcPartRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartRowStatus.setStatus(_A)
_CwRsrcPartIlmiTable_Object=MibTable
cwRsrcPartIlmiTable=_CwRsrcPartIlmiTable_Object((1,3,6,1,4,1,9,9,125,1,1,2))
if mibBuilder.loadTexts:cwRsrcPartIlmiTable.setStatus(_A)
_CwRsrcPartIlmiEntry_Object=MibTableRow
cwRsrcPartIlmiEntry=_CwRsrcPartIlmiEntry_Object((1,3,6,1,4,1,9,9,125,1,1,2,1))
cwRsrcPartIlmiEntry.setIndexNames((0,_I,_J),(0,_B,_K))
if mibBuilder.loadTexts:cwRsrcPartIlmiEntry.setStatus(_A)
class _CwRsrcPartIlmiEnabled_Type(TruthValue):defaultValue=2
_CwRsrcPartIlmiEnabled_Type.__name__=_O
_CwRsrcPartIlmiEnabled_Object=MibTableColumn
cwRsrcPartIlmiEnabled=_CwRsrcPartIlmiEnabled_Object((1,3,6,1,4,1,9,9,125,1,1,2,1,1),_CwRsrcPartIlmiEnabled_Type())
cwRsrcPartIlmiEnabled.setMaxAccess(_G)
if mibBuilder.loadTexts:cwRsrcPartIlmiEnabled.setStatus(_A)
class _CwRsrcPartSignallingVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwRsrcPartSignallingVpi_Type.__name__=_F
_CwRsrcPartSignallingVpi_Object=MibTableColumn
cwRsrcPartSignallingVpi=_CwRsrcPartSignallingVpi_Object((1,3,6,1,4,1,9,9,125,1,1,2,1,2),_CwRsrcPartSignallingVpi_Type())
cwRsrcPartSignallingVpi.setMaxAccess(_G)
if mibBuilder.loadTexts:cwRsrcPartSignallingVpi.setStatus(_A)
class _CwRsrcPartSignallingVci_Type(Integer32):defaultValue=16;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwRsrcPartSignallingVci_Type.__name__=_F
_CwRsrcPartSignallingVci_Object=MibTableColumn
cwRsrcPartSignallingVci=_CwRsrcPartSignallingVci_Object((1,3,6,1,4,1,9,9,125,1,1,2,1,3),_CwRsrcPartSignallingVci_Type())
cwRsrcPartSignallingVci.setMaxAccess(_G)
if mibBuilder.loadTexts:cwRsrcPartSignallingVci.setStatus(_A)
_CwRsrcPartIlmiTrapEnable_Type=TruthValue
_CwRsrcPartIlmiTrapEnable_Object=MibTableColumn
cwRsrcPartIlmiTrapEnable=_CwRsrcPartIlmiTrapEnable_Object((1,3,6,1,4,1,9,9,125,1,1,2,1,4),_CwRsrcPartIlmiTrapEnable_Type())
cwRsrcPartIlmiTrapEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:cwRsrcPartIlmiTrapEnable.setStatus(_A)
class _CwRsrcPartIlmiEstablishConPollIntvl_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CwRsrcPartIlmiEstablishConPollIntvl_Type.__name__=_C
_CwRsrcPartIlmiEstablishConPollIntvl_Object=MibTableColumn
cwRsrcPartIlmiEstablishConPollIntvl=_CwRsrcPartIlmiEstablishConPollIntvl_Object((1,3,6,1,4,1,9,9,125,1,1,2,1,5),_CwRsrcPartIlmiEstablishConPollIntvl_Type())
cwRsrcPartIlmiEstablishConPollIntvl.setMaxAccess(_G)
if mibBuilder.loadTexts:cwRsrcPartIlmiEstablishConPollIntvl.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartIlmiEstablishConPollIntvl.setUnits(_Q)
class _CwRsrcPartIlmiCheckConPollIntvl_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwRsrcPartIlmiCheckConPollIntvl_Type.__name__=_C
_CwRsrcPartIlmiCheckConPollIntvl_Object=MibTableColumn
cwRsrcPartIlmiCheckConPollIntvl=_CwRsrcPartIlmiCheckConPollIntvl_Object((1,3,6,1,4,1,9,9,125,1,1,2,1,6),_CwRsrcPartIlmiCheckConPollIntvl_Type())
cwRsrcPartIlmiCheckConPollIntvl.setMaxAccess(_G)
if mibBuilder.loadTexts:cwRsrcPartIlmiCheckConPollIntvl.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcPartIlmiCheckConPollIntvl.setUnits(_Q)
class _CwRsrcPartIlmiConPollInactFactor_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwRsrcPartIlmiConPollInactFactor_Type.__name__=_C
_CwRsrcPartIlmiConPollInactFactor_Object=MibTableColumn
cwRsrcPartIlmiConPollInactFactor=_CwRsrcPartIlmiConPollInactFactor_Object((1,3,6,1,4,1,9,9,125,1,1,2,1,7),_CwRsrcPartIlmiConPollInactFactor_Type())
cwRsrcPartIlmiConPollInactFactor.setMaxAccess(_G)
if mibBuilder.loadTexts:cwRsrcPartIlmiConPollInactFactor.setStatus(_A)
_CwRsrcPartCtlrConfTable_Object=MibTable
cwRsrcPartCtlrConfTable=_CwRsrcPartCtlrConfTable_Object((1,3,6,1,4,1,9,9,125,1,1,3))
if mibBuilder.loadTexts:cwRsrcPartCtlrConfTable.setStatus(_A)
_CwRsrcPartCtlrConfEntry_Object=MibTableRow
cwRsrcPartCtlrConfEntry=_CwRsrcPartCtlrConfEntry_Object((1,3,6,1,4,1,9,9,125,1,1,3,1))
cwRsrcPartCtlrConfEntry.setIndexNames((0,_I,_J),(0,_B,_K),(0,_B,_R))
if mibBuilder.loadTexts:cwRsrcPartCtlrConfEntry.setStatus(_A)
class _CwRsrcPartCtlrController_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CwRsrcPartCtlrController_Type.__name__=_C
_CwRsrcPartCtlrController_Object=MibTableColumn
cwRsrcPartCtlrController=_CwRsrcPartCtlrController_Object((1,3,6,1,4,1,9,9,125,1,1,3,1,1),_CwRsrcPartCtlrController_Type())
cwRsrcPartCtlrController.setMaxAccess(_P)
if mibBuilder.loadTexts:cwRsrcPartCtlrController.setStatus(_A)
_CwRsrcPartCtlrRowStatus_Type=RowStatus
_CwRsrcPartCtlrRowStatus_Object=MibTableColumn
cwRsrcPartCtlrRowStatus=_CwRsrcPartCtlrRowStatus_Object((1,3,6,1,4,1,9,9,125,1,1,3,1,2),_CwRsrcPartCtlrRowStatus_Type())
cwRsrcPartCtlrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcPartCtlrRowStatus.setStatus(_A)
_CwRsrcSvcAggrGrp_ObjectIdentity=ObjectIdentity
cwRsrcSvcAggrGrp=_CwRsrcSvcAggrGrp_ObjectIdentity((1,3,6,1,4,1,9,9,125,1,2))
_CwRsrcSvcAggregateTable_Object=MibTable
cwRsrcSvcAggregateTable=_CwRsrcSvcAggregateTable_Object((1,3,6,1,4,1,9,9,125,1,2,1))
if mibBuilder.loadTexts:cwRsrcSvcAggregateTable.setStatus(_A)
_CwRsrcSvcAggregateEntry_Object=MibTableRow
cwRsrcSvcAggregateEntry=_CwRsrcSvcAggregateEntry_Object((1,3,6,1,4,1,9,9,125,1,2,1,1))
cwRsrcSvcAggregateEntry.setIndexNames((0,_I,_J),(0,_B,_K))
if mibBuilder.loadTexts:cwRsrcSvcAggregateEntry.setStatus(_A)
class _CwRsrcSvcAggrVpiLow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwRsrcSvcAggrVpiLow_Type.__name__=_C
_CwRsrcSvcAggrVpiLow_Object=MibTableColumn
cwRsrcSvcAggrVpiLow=_CwRsrcSvcAggrVpiLow_Object((1,3,6,1,4,1,9,9,125,1,2,1,1,1),_CwRsrcSvcAggrVpiLow_Type())
cwRsrcSvcAggrVpiLow.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcSvcAggrVpiLow.setStatus(_A)
class _CwRsrcSvcAggrVpiHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwRsrcSvcAggrVpiHigh_Type.__name__=_C
_CwRsrcSvcAggrVpiHigh_Object=MibTableColumn
cwRsrcSvcAggrVpiHigh=_CwRsrcSvcAggrVpiHigh_Object((1,3,6,1,4,1,9,9,125,1,2,1,1,2),_CwRsrcSvcAggrVpiHigh_Type())
cwRsrcSvcAggrVpiHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcSvcAggrVpiHigh.setStatus(_A)
class _CwRsrcSvcAggrEgrPctBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CwRsrcSvcAggrEgrPctBw_Type.__name__=_F
_CwRsrcSvcAggrEgrPctBw_Object=MibTableColumn
cwRsrcSvcAggrEgrPctBw=_CwRsrcSvcAggrEgrPctBw_Object((1,3,6,1,4,1,9,9,125,1,2,1,1,3),_CwRsrcSvcAggrEgrPctBw_Type())
cwRsrcSvcAggrEgrPctBw.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcSvcAggrEgrPctBw.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcSvcAggrEgrPctBw.setUnits(_S)
class _CwRsrcSvcAggrIngPctBw_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CwRsrcSvcAggrIngPctBw_Type.__name__=_F
_CwRsrcSvcAggrIngPctBw_Object=MibTableColumn
cwRsrcSvcAggrIngPctBw=_CwRsrcSvcAggrIngPctBw_Object((1,3,6,1,4,1,9,9,125,1,2,1,1,4),_CwRsrcSvcAggrIngPctBw_Type())
cwRsrcSvcAggrIngPctBw.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcSvcAggrIngPctBw.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcSvcAggrIngPctBw.setUnits(_S)
class _CwRsrcSvcAggrChanVADTolerance_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_CwRsrcSvcAggrChanVADTolerance_Type.__name__=_F
_CwRsrcSvcAggrChanVADTolerance_Object=MibTableColumn
cwRsrcSvcAggrChanVADTolerance=_CwRsrcSvcAggrChanVADTolerance_Object((1,3,6,1,4,1,9,9,125,1,2,1,1,5),_CwRsrcSvcAggrChanVADTolerance_Type())
cwRsrcSvcAggrChanVADTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcSvcAggrChanVADTolerance.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcSvcAggrChanVADTolerance.setUnits('0.0001')
class _CwRsrcSvcAggrChanVADDutyCycle_Type(Integer32):defaultValue=61;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_CwRsrcSvcAggrChanVADDutyCycle_Type.__name__=_F
_CwRsrcSvcAggrChanVADDutyCycle_Object=MibTableColumn
cwRsrcSvcAggrChanVADDutyCycle=_CwRsrcSvcAggrChanVADDutyCycle_Object((1,3,6,1,4,1,9,9,125,1,2,1,1,6),_CwRsrcSvcAggrChanVADDutyCycle_Type())
cwRsrcSvcAggrChanVADDutyCycle.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcSvcAggrChanVADDutyCycle.setStatus(_A)
if mibBuilder.loadTexts:cwRsrcSvcAggrChanVADDutyCycle.setUnits('0.01')
_CwRsrcSvcAggrRowStatus_Type=RowStatus
_CwRsrcSvcAggrRowStatus_Object=MibTableColumn
cwRsrcSvcAggrRowStatus=_CwRsrcSvcAggrRowStatus_Object((1,3,6,1,4,1,9,9,125,1,2,1,1,7),_CwRsrcSvcAggrRowStatus_Type())
cwRsrcSvcAggrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cwRsrcSvcAggrRowStatus.setStatus(_A)
_CwRsrcPartMIBConformance_ObjectIdentity=ObjectIdentity
cwRsrcPartMIBConformance=_CwRsrcPartMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,125,3))
_CwRsrcPartMIBCompliances_ObjectIdentity=ObjectIdentity
cwRsrcPartMIBCompliances=_CwRsrcPartMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,125,3,1))
_CwRsrcPartMIBGroups_ObjectIdentity=ObjectIdentity
cwRsrcPartMIBGroups=_CwRsrcPartMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,125,3,2))
cwRsrcPartMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,125,3,2,1))
cwRsrcPartMIBGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:cwRsrcPartMIBGroup.setStatus(_A)
cwRsrcPartIlmiMIBGroup=ObjectGroup((1,3,6,1,4,1,9,9,125,3,2,2))
cwRsrcPartIlmiMIBGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:cwRsrcPartIlmiMIBGroup.setStatus(_A)
cwRsrcPartMappingGroup=ObjectGroup((1,3,6,1,4,1,9,9,125,3,2,3))
cwRsrcPartMappingGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:cwRsrcPartMappingGroup.setStatus(_A)
cwRsrcSvcAggrGroup=ObjectGroup((1,3,6,1,4,1,9,9,125,3,2,4))
cwRsrcSvcAggrGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:cwRsrcSvcAggrGroup.setStatus(_A)
cwRsrcPartMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,125,3,1,1))
cwRsrcPartMIBCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cwRsrcPartMIBCompliance.setStatus('deprecated')
cwRsrcPartMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,125,3,1,2))
cwRsrcPartMIBComplianceRev1.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_A0)))
if mibBuilder.loadTexts:cwRsrcPartMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWANRsrcPartMIB':ciscoWANRsrcPartMIB,'ciscoWANRsrcPartMIBObjects':ciscoWANRsrcPartMIBObjects,'cwRsrcPartConfGrp':cwRsrcPartConfGrp,'cwRsrcPartConfTable':cwRsrcPartConfTable,'cwRsrcPartConfEntry':cwRsrcPartConfEntry,_K:cwRsrcPartID,_T:cwRsrcPartController,_U:cwRsrcPartEgrGuarPctBwConf,_V:cwRsrcPartEgrMaxPctBwConf,_W:cwRsrcPartIngGuarPctBwConf,_X:cwRsrcPartIngMaxPctBwConf,_a:cwRsrcPartEgrPctBwUsed,_b:cwRsrcPartIngPctBwUsed,_Y:cwRsrcPartEgrPctBwAvail,_Z:cwRsrcPartIngPctBwAvail,_c:cwRsrcPartVpiLo,_d:cwRsrcPartVpiHigh,_e:cwRsrcPartVciLo,_f:cwRsrcPartVciHigh,_g:cwRsrcPartGuarCon,_h:cwRsrcPartMaxCon,_i:cwRsrcPartUsedCon,_j:cwRsrcPartAvailCon,_k:cwRsrcPartRowStatus,'cwRsrcPartIlmiTable':cwRsrcPartIlmiTable,'cwRsrcPartIlmiEntry':cwRsrcPartIlmiEntry,_l:cwRsrcPartIlmiEnabled,_m:cwRsrcPartSignallingVpi,_n:cwRsrcPartSignallingVci,_o:cwRsrcPartIlmiTrapEnable,_p:cwRsrcPartIlmiEstablishConPollIntvl,_q:cwRsrcPartIlmiCheckConPollIntvl,_r:cwRsrcPartIlmiConPollInactFactor,'cwRsrcPartCtlrConfTable':cwRsrcPartCtlrConfTable,'cwRsrcPartCtlrConfEntry':cwRsrcPartCtlrConfEntry,_R:cwRsrcPartCtlrController,_s:cwRsrcPartCtlrRowStatus,'cwRsrcSvcAggrGrp':cwRsrcSvcAggrGrp,'cwRsrcSvcAggregateTable':cwRsrcSvcAggregateTable,'cwRsrcSvcAggregateEntry':cwRsrcSvcAggregateEntry,_t:cwRsrcSvcAggrVpiLow,_u:cwRsrcSvcAggrVpiHigh,_v:cwRsrcSvcAggrEgrPctBw,_w:cwRsrcSvcAggrIngPctBw,_x:cwRsrcSvcAggrChanVADTolerance,_y:cwRsrcSvcAggrChanVADDutyCycle,_z:cwRsrcSvcAggrRowStatus,'cwRsrcPartMIBConformance':cwRsrcPartMIBConformance,'cwRsrcPartMIBCompliances':cwRsrcPartMIBCompliances,'cwRsrcPartMIBCompliance':cwRsrcPartMIBCompliance,'cwRsrcPartMIBComplianceRev1':cwRsrcPartMIBComplianceRev1,'cwRsrcPartMIBGroups':cwRsrcPartMIBGroups,_L:cwRsrcPartMIBGroup,_M:cwRsrcPartIlmiMIBGroup,_N:cwRsrcPartMappingGroup,_A0:cwRsrcSvcAggrGroup})