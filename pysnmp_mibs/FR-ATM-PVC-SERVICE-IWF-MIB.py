_y='frAtmIwfConnStatusChange'
_x='frAtmIwfVclCrossConnectIdentifier'
_w='frAtmIwfConnDescriptorRowStatus'
_v='frAtmIwfConnArpTranslationEnabled'
_u='frAtmIwfConnFragAndReassEnabled'
_t='frAtmIwfConnEncapsulationMappings'
_s='frAtmIwfConnEncapsulationMappingMode'
_r='frAtmIwfConnCongestionMappingMode'
_q='frAtmIwfConnClpToDeMappingMode'
_p='frAtmIwfConnDeToClpMappingMode'
_o='frAtmIwfConnectionDescriptorIndexNext'
_n='frAtmIwfConnRowStatus'
_m='frAtmIwfConnSarTimeOuts'
_l='frAtmIwfConnCrcErrors'
_k='frAtmIwfConnOverSizedSDUs'
_j='frAtmIwfConnFailedAal5PduTranslate'
_i='frAtmIwfConnOverSizedFrames'
_h='frAtmIwfConnFailedFrameTranslate'
_g='frAtmIwfConnectionDescriptor'
_f='frAtmIwfConnFr2AtmLastChange'
_e='frAtmIwfConnAtm2FrLastChange'
_d='frAtmIwfConnIndexNext'
_c='frAtmIwfVclEntry'
_b='disabled'
_a='enabled'
_Z='mode2Const1'
_Y='mode2Const0'
_X='frAtmIwfConnectionDescriptorIndex'
_W='Frames'
_V='frAtmIwfConnDlci'
_U='frAtmIwfConnFrPort'
_T='frAtmIwfConnVci'
_S='frAtmIwfConnVpi'
_R='frAtmIwfConnAtmPort'
_Q='frAtmIwfConnIndex'
_P='frAtmIwfNotificationsGroup'
_O='frAtmIwfAtmVclTableAugmentGroup'
_N='frAtmIwfConnectionDescriptorGroup'
_M='frAtmIwfBasicGroup'
_L='frAtmIwfConnFr2AtmOperStatus'
_K='frAtmIwfConnAtm2FrOperStatus'
_J='frAtmIwfConnAdminStatus'
_I='mode1'
_H='PDUs'
_G='down'
_F='not-accessible'
_E='read-create'
_D='read-only'
_C='Integer32'
_B='current'
_A='FR-ATM-PVC-SERVICE-IWF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmVclEntry,=mibBuilder.importSymbols('ATM-MIB','atmVclEntry')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
frAtmIwfMIB=ModuleIdentity((1,3,6,1,2,1,86))
if mibBuilder.loadTexts:frAtmIwfMIB.setRevisions(('2000-09-28 00:00',))
_FrAtmIwfMIBObjects_ObjectIdentity=ObjectIdentity
frAtmIwfMIBObjects=_FrAtmIwfMIBObjects_ObjectIdentity((1,3,6,1,2,1,86,1))
class _FrAtmIwfConnIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrAtmIwfConnIndexNext_Type.__name__=_C
_FrAtmIwfConnIndexNext_Object=MibScalar
frAtmIwfConnIndexNext=_FrAtmIwfConnIndexNext_Object((1,3,6,1,2,1,86,1,1),_FrAtmIwfConnIndexNext_Type())
frAtmIwfConnIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnIndexNext.setStatus(_B)
_FrAtmIwfConnectionTable_Object=MibTable
frAtmIwfConnectionTable=_FrAtmIwfConnectionTable_Object((1,3,6,1,2,1,86,1,2))
if mibBuilder.loadTexts:frAtmIwfConnectionTable.setStatus(_B)
_FrAtmIwfConnectionEntry_Object=MibTableRow
frAtmIwfConnectionEntry=_FrAtmIwfConnectionEntry_Object((1,3,6,1,2,1,86,1,2,1))
frAtmIwfConnectionEntry.setIndexNames((0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_T),(0,_A,_U),(0,_A,_V))
if mibBuilder.loadTexts:frAtmIwfConnectionEntry.setStatus(_B)
class _FrAtmIwfConnIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrAtmIwfConnIndex_Type.__name__=_C
_FrAtmIwfConnIndex_Object=MibTableColumn
frAtmIwfConnIndex=_FrAtmIwfConnIndex_Object((1,3,6,1,2,1,86,1,2,1,1),_FrAtmIwfConnIndex_Type())
frAtmIwfConnIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:frAtmIwfConnIndex.setStatus(_B)
_FrAtmIwfConnAtmPort_Type=InterfaceIndex
_FrAtmIwfConnAtmPort_Object=MibTableColumn
frAtmIwfConnAtmPort=_FrAtmIwfConnAtmPort_Object((1,3,6,1,2,1,86,1,2,1,2),_FrAtmIwfConnAtmPort_Type())
frAtmIwfConnAtmPort.setMaxAccess(_F)
if mibBuilder.loadTexts:frAtmIwfConnAtmPort.setStatus(_B)
_FrAtmIwfConnVpi_Type=AtmVpIdentifier
_FrAtmIwfConnVpi_Object=MibTableColumn
frAtmIwfConnVpi=_FrAtmIwfConnVpi_Object((1,3,6,1,2,1,86,1,2,1,3),_FrAtmIwfConnVpi_Type())
frAtmIwfConnVpi.setMaxAccess(_F)
if mibBuilder.loadTexts:frAtmIwfConnVpi.setStatus(_B)
_FrAtmIwfConnVci_Type=AtmVcIdentifier
_FrAtmIwfConnVci_Object=MibTableColumn
frAtmIwfConnVci=_FrAtmIwfConnVci_Object((1,3,6,1,2,1,86,1,2,1,4),_FrAtmIwfConnVci_Type())
frAtmIwfConnVci.setMaxAccess(_F)
if mibBuilder.loadTexts:frAtmIwfConnVci.setStatus(_B)
_FrAtmIwfConnFrPort_Type=InterfaceIndex
_FrAtmIwfConnFrPort_Object=MibTableColumn
frAtmIwfConnFrPort=_FrAtmIwfConnFrPort_Object((1,3,6,1,2,1,86,1,2,1,5),_FrAtmIwfConnFrPort_Type())
frAtmIwfConnFrPort.setMaxAccess(_F)
if mibBuilder.loadTexts:frAtmIwfConnFrPort.setStatus(_B)
class _FrAtmIwfConnDlci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4194303))
_FrAtmIwfConnDlci_Type.__name__=_C
_FrAtmIwfConnDlci_Object=MibTableColumn
frAtmIwfConnDlci=_FrAtmIwfConnDlci_Object((1,3,6,1,2,1,86,1,2,1,6),_FrAtmIwfConnDlci_Type())
frAtmIwfConnDlci.setMaxAccess(_F)
if mibBuilder.loadTexts:frAtmIwfConnDlci.setStatus(_B)
_FrAtmIwfConnRowStatus_Type=RowStatus
_FrAtmIwfConnRowStatus_Object=MibTableColumn
frAtmIwfConnRowStatus=_FrAtmIwfConnRowStatus_Object((1,3,6,1,2,1,86,1,2,1,7),_FrAtmIwfConnRowStatus_Type())
frAtmIwfConnRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnRowStatus.setStatus(_B)
class _FrAtmIwfConnAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_G,2)))
_FrAtmIwfConnAdminStatus_Type.__name__=_C
_FrAtmIwfConnAdminStatus_Object=MibTableColumn
frAtmIwfConnAdminStatus=_FrAtmIwfConnAdminStatus_Object((1,3,6,1,2,1,86,1,2,1,8),_FrAtmIwfConnAdminStatus_Type())
frAtmIwfConnAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnAdminStatus.setStatus(_B)
class _FrAtmIwfConnAtm2FrOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_G,2)))
_FrAtmIwfConnAtm2FrOperStatus_Type.__name__=_C
_FrAtmIwfConnAtm2FrOperStatus_Object=MibTableColumn
frAtmIwfConnAtm2FrOperStatus=_FrAtmIwfConnAtm2FrOperStatus_Object((1,3,6,1,2,1,86,1,2,1,9),_FrAtmIwfConnAtm2FrOperStatus_Type())
frAtmIwfConnAtm2FrOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnAtm2FrOperStatus.setStatus(_B)
_FrAtmIwfConnAtm2FrLastChange_Type=TimeStamp
_FrAtmIwfConnAtm2FrLastChange_Object=MibTableColumn
frAtmIwfConnAtm2FrLastChange=_FrAtmIwfConnAtm2FrLastChange_Object((1,3,6,1,2,1,86,1,2,1,10),_FrAtmIwfConnAtm2FrLastChange_Type())
frAtmIwfConnAtm2FrLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnAtm2FrLastChange.setStatus(_B)
class _FrAtmIwfConnFr2AtmOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_G,2)))
_FrAtmIwfConnFr2AtmOperStatus_Type.__name__=_C
_FrAtmIwfConnFr2AtmOperStatus_Object=MibTableColumn
frAtmIwfConnFr2AtmOperStatus=_FrAtmIwfConnFr2AtmOperStatus_Object((1,3,6,1,2,1,86,1,2,1,11),_FrAtmIwfConnFr2AtmOperStatus_Type())
frAtmIwfConnFr2AtmOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnFr2AtmOperStatus.setStatus(_B)
_FrAtmIwfConnFr2AtmLastChange_Type=TimeStamp
_FrAtmIwfConnFr2AtmLastChange_Object=MibTableColumn
frAtmIwfConnFr2AtmLastChange=_FrAtmIwfConnFr2AtmLastChange_Object((1,3,6,1,2,1,86,1,2,1,12),_FrAtmIwfConnFr2AtmLastChange_Type())
frAtmIwfConnFr2AtmLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnFr2AtmLastChange.setStatus(_B)
_FrAtmIwfConnectionDescriptor_Type=Integer32
_FrAtmIwfConnectionDescriptor_Object=MibTableColumn
frAtmIwfConnectionDescriptor=_FrAtmIwfConnectionDescriptor_Object((1,3,6,1,2,1,86,1,2,1,13),_FrAtmIwfConnectionDescriptor_Type())
frAtmIwfConnectionDescriptor.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnectionDescriptor.setStatus(_B)
_FrAtmIwfConnFailedFrameTranslate_Type=Counter32
_FrAtmIwfConnFailedFrameTranslate_Object=MibTableColumn
frAtmIwfConnFailedFrameTranslate=_FrAtmIwfConnFailedFrameTranslate_Object((1,3,6,1,2,1,86,1,2,1,14),_FrAtmIwfConnFailedFrameTranslate_Type())
frAtmIwfConnFailedFrameTranslate.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnFailedFrameTranslate.setStatus(_B)
if mibBuilder.loadTexts:frAtmIwfConnFailedFrameTranslate.setUnits(_W)
_FrAtmIwfConnOverSizedFrames_Type=Counter32
_FrAtmIwfConnOverSizedFrames_Object=MibTableColumn
frAtmIwfConnOverSizedFrames=_FrAtmIwfConnOverSizedFrames_Object((1,3,6,1,2,1,86,1,2,1,15),_FrAtmIwfConnOverSizedFrames_Type())
frAtmIwfConnOverSizedFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnOverSizedFrames.setStatus(_B)
if mibBuilder.loadTexts:frAtmIwfConnOverSizedFrames.setUnits(_W)
_FrAtmIwfConnFailedAal5PduTranslate_Type=Counter32
_FrAtmIwfConnFailedAal5PduTranslate_Object=MibTableColumn
frAtmIwfConnFailedAal5PduTranslate=_FrAtmIwfConnFailedAal5PduTranslate_Object((1,3,6,1,2,1,86,1,2,1,16),_FrAtmIwfConnFailedAal5PduTranslate_Type())
frAtmIwfConnFailedAal5PduTranslate.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnFailedAal5PduTranslate.setStatus(_B)
if mibBuilder.loadTexts:frAtmIwfConnFailedAal5PduTranslate.setUnits(_H)
_FrAtmIwfConnOverSizedSDUs_Type=Counter32
_FrAtmIwfConnOverSizedSDUs_Object=MibTableColumn
frAtmIwfConnOverSizedSDUs=_FrAtmIwfConnOverSizedSDUs_Object((1,3,6,1,2,1,86,1,2,1,17),_FrAtmIwfConnOverSizedSDUs_Type())
frAtmIwfConnOverSizedSDUs.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnOverSizedSDUs.setStatus(_B)
if mibBuilder.loadTexts:frAtmIwfConnOverSizedSDUs.setUnits('SDUs')
_FrAtmIwfConnCrcErrors_Type=Counter32
_FrAtmIwfConnCrcErrors_Object=MibTableColumn
frAtmIwfConnCrcErrors=_FrAtmIwfConnCrcErrors_Object((1,3,6,1,2,1,86,1,2,1,18),_FrAtmIwfConnCrcErrors_Type())
frAtmIwfConnCrcErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnCrcErrors.setStatus(_B)
if mibBuilder.loadTexts:frAtmIwfConnCrcErrors.setUnits(_H)
_FrAtmIwfConnSarTimeOuts_Type=Counter32
_FrAtmIwfConnSarTimeOuts_Object=MibTableColumn
frAtmIwfConnSarTimeOuts=_FrAtmIwfConnSarTimeOuts_Object((1,3,6,1,2,1,86,1,2,1,19),_FrAtmIwfConnSarTimeOuts_Type())
frAtmIwfConnSarTimeOuts.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnSarTimeOuts.setStatus(_B)
if mibBuilder.loadTexts:frAtmIwfConnSarTimeOuts.setUnits(_H)
class _FrAtmIwfConnectionDescriptorIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FrAtmIwfConnectionDescriptorIndexNext_Type.__name__=_C
_FrAtmIwfConnectionDescriptorIndexNext_Object=MibScalar
frAtmIwfConnectionDescriptorIndexNext=_FrAtmIwfConnectionDescriptorIndexNext_Object((1,3,6,1,2,1,86,1,3),_FrAtmIwfConnectionDescriptorIndexNext_Type())
frAtmIwfConnectionDescriptorIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfConnectionDescriptorIndexNext.setStatus(_B)
_FrAtmIwfConnectionDescriptorTable_Object=MibTable
frAtmIwfConnectionDescriptorTable=_FrAtmIwfConnectionDescriptorTable_Object((1,3,6,1,2,1,86,1,4))
if mibBuilder.loadTexts:frAtmIwfConnectionDescriptorTable.setStatus(_B)
_FrAtmIwfConnectionDescriptorEntry_Object=MibTableRow
frAtmIwfConnectionDescriptorEntry=_FrAtmIwfConnectionDescriptorEntry_Object((1,3,6,1,2,1,86,1,4,1))
frAtmIwfConnectionDescriptorEntry.setIndexNames((0,_A,_X))
if mibBuilder.loadTexts:frAtmIwfConnectionDescriptorEntry.setStatus(_B)
class _FrAtmIwfConnectionDescriptorIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrAtmIwfConnectionDescriptorIndex_Type.__name__=_C
_FrAtmIwfConnectionDescriptorIndex_Object=MibTableColumn
frAtmIwfConnectionDescriptorIndex=_FrAtmIwfConnectionDescriptorIndex_Object((1,3,6,1,2,1,86,1,4,1,1),_FrAtmIwfConnectionDescriptorIndex_Type())
frAtmIwfConnectionDescriptorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:frAtmIwfConnectionDescriptorIndex.setStatus(_B)
_FrAtmIwfConnDescriptorRowStatus_Type=RowStatus
_FrAtmIwfConnDescriptorRowStatus_Object=MibTableColumn
frAtmIwfConnDescriptorRowStatus=_FrAtmIwfConnDescriptorRowStatus_Object((1,3,6,1,2,1,86,1,4,1,2),_FrAtmIwfConnDescriptorRowStatus_Type())
frAtmIwfConnDescriptorRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnDescriptorRowStatus.setStatus(_B)
class _FrAtmIwfConnDeToClpMappingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_Y,2),(_Z,3)))
_FrAtmIwfConnDeToClpMappingMode_Type.__name__=_C
_FrAtmIwfConnDeToClpMappingMode_Object=MibTableColumn
frAtmIwfConnDeToClpMappingMode=_FrAtmIwfConnDeToClpMappingMode_Object((1,3,6,1,2,1,86,1,4,1,3),_FrAtmIwfConnDeToClpMappingMode_Type())
frAtmIwfConnDeToClpMappingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnDeToClpMappingMode.setStatus(_B)
class _FrAtmIwfConnClpToDeMappingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_Y,2),(_Z,3)))
_FrAtmIwfConnClpToDeMappingMode_Type.__name__=_C
_FrAtmIwfConnClpToDeMappingMode_Object=MibTableColumn
frAtmIwfConnClpToDeMappingMode=_FrAtmIwfConnClpToDeMappingMode_Object((1,3,6,1,2,1,86,1,4,1,4),_FrAtmIwfConnClpToDeMappingMode_Type())
frAtmIwfConnClpToDeMappingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnClpToDeMappingMode.setStatus(_B)
class _FrAtmIwfConnCongestionMappingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),('mode2',2)))
_FrAtmIwfConnCongestionMappingMode_Type.__name__=_C
_FrAtmIwfConnCongestionMappingMode_Object=MibTableColumn
frAtmIwfConnCongestionMappingMode=_FrAtmIwfConnCongestionMappingMode_Object((1,3,6,1,2,1,86,1,4,1,5),_FrAtmIwfConnCongestionMappingMode_Type())
frAtmIwfConnCongestionMappingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnCongestionMappingMode.setStatus(_B)
class _FrAtmIwfConnEncapsulationMappingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('transparentMode',1),('translationMode',2),('translationModeAll',3)))
_FrAtmIwfConnEncapsulationMappingMode_Type.__name__=_C
_FrAtmIwfConnEncapsulationMappingMode_Object=MibTableColumn
frAtmIwfConnEncapsulationMappingMode=_FrAtmIwfConnEncapsulationMappingMode_Object((1,3,6,1,2,1,86,1,4,1,6),_FrAtmIwfConnEncapsulationMappingMode_Type())
frAtmIwfConnEncapsulationMappingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnEncapsulationMappingMode.setStatus(_B)
class _FrAtmIwfConnEncapsulationMappings_Type(Bits):defaultBinValue='1';namedValues=NamedValues(*(('none',0),('bridgedPdus',1),('bridged802dot6',2),('bPdus',3),('routedIp',4),('routedOsi',5),('otherRouted',6),('x25Iso8202',7),('q933q2931',8)))
_FrAtmIwfConnEncapsulationMappings_Type.__name__='Bits'
_FrAtmIwfConnEncapsulationMappings_Object=MibTableColumn
frAtmIwfConnEncapsulationMappings=_FrAtmIwfConnEncapsulationMappings_Object((1,3,6,1,2,1,86,1,4,1,7),_FrAtmIwfConnEncapsulationMappings_Type())
frAtmIwfConnEncapsulationMappings.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnEncapsulationMappings.setStatus(_B)
class _FrAtmIwfConnFragAndReassEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_FrAtmIwfConnFragAndReassEnabled_Type.__name__=_C
_FrAtmIwfConnFragAndReassEnabled_Object=MibTableColumn
frAtmIwfConnFragAndReassEnabled=_FrAtmIwfConnFragAndReassEnabled_Object((1,3,6,1,2,1,86,1,4,1,8),_FrAtmIwfConnFragAndReassEnabled_Type())
frAtmIwfConnFragAndReassEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnFragAndReassEnabled.setStatus(_B)
class _FrAtmIwfConnArpTranslationEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_a,1),(_b,2)))
_FrAtmIwfConnArpTranslationEnabled_Type.__name__=_C
_FrAtmIwfConnArpTranslationEnabled_Object=MibTableColumn
frAtmIwfConnArpTranslationEnabled=_FrAtmIwfConnArpTranslationEnabled_Object((1,3,6,1,2,1,86,1,4,1,9),_FrAtmIwfConnArpTranslationEnabled_Type())
frAtmIwfConnArpTranslationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:frAtmIwfConnArpTranslationEnabled.setStatus(_B)
_FrAtmIwfVclTable_Object=MibTable
frAtmIwfVclTable=_FrAtmIwfVclTable_Object((1,3,6,1,2,1,86,1,5))
if mibBuilder.loadTexts:frAtmIwfVclTable.setStatus(_B)
_FrAtmIwfVclEntry_Object=MibTableRow
frAtmIwfVclEntry=_FrAtmIwfVclEntry_Object((1,3,6,1,2,1,86,1,5,1))
if mibBuilder.loadTexts:frAtmIwfVclEntry.setStatus(_B)
class _FrAtmIwfVclCrossConnectIdentifier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FrAtmIwfVclCrossConnectIdentifier_Type.__name__=_C
_FrAtmIwfVclCrossConnectIdentifier_Object=MibTableColumn
frAtmIwfVclCrossConnectIdentifier=_FrAtmIwfVclCrossConnectIdentifier_Object((1,3,6,1,2,1,86,1,5,1,1),_FrAtmIwfVclCrossConnectIdentifier_Type())
frAtmIwfVclCrossConnectIdentifier.setMaxAccess(_D)
if mibBuilder.loadTexts:frAtmIwfVclCrossConnectIdentifier.setStatus(_B)
_FrAtmIwfTraps_ObjectIdentity=ObjectIdentity
frAtmIwfTraps=_FrAtmIwfTraps_ObjectIdentity((1,3,6,1,2,1,86,2))
_FrAtmIwfTrapsPrefix_ObjectIdentity=ObjectIdentity
frAtmIwfTrapsPrefix=_FrAtmIwfTrapsPrefix_ObjectIdentity((1,3,6,1,2,1,86,2,0))
_FrAtmIwfConformance_ObjectIdentity=ObjectIdentity
frAtmIwfConformance=_FrAtmIwfConformance_ObjectIdentity((1,3,6,1,2,1,86,3))
_FrAtmIwfGroups_ObjectIdentity=ObjectIdentity
frAtmIwfGroups=_FrAtmIwfGroups_ObjectIdentity((1,3,6,1,2,1,86,3,1))
_FrAtmIwfCompliances_ObjectIdentity=ObjectIdentity
frAtmIwfCompliances=_FrAtmIwfCompliances_ObjectIdentity((1,3,6,1,2,1,86,3,2))
atmVclEntry.registerAugmentions((_A,_c))
frAtmIwfVclEntry.setIndexNames(*atmVclEntry.getIndexNames())
frAtmIwfBasicGroup=ObjectGroup((1,3,6,1,2,1,86,3,1,1))
frAtmIwfBasicGroup.setObjects(*((_A,_d),(_A,_J),(_A,_K),(_A,_e),(_A,_L),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:frAtmIwfBasicGroup.setStatus(_B)
frAtmIwfConnectionDescriptorGroup=ObjectGroup((1,3,6,1,2,1,86,3,1,2))
frAtmIwfConnectionDescriptorGroup.setObjects(*((_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:frAtmIwfConnectionDescriptorGroup.setStatus(_B)
frAtmIwfAtmVclTableAugmentGroup=ObjectGroup((1,3,6,1,2,1,86,3,1,3))
frAtmIwfAtmVclTableAugmentGroup.setObjects((_A,_x))
if mibBuilder.loadTexts:frAtmIwfAtmVclTableAugmentGroup.setStatus(_B)
frAtmIwfConnStatusChange=NotificationType((1,3,6,1,2,1,86,2,0,1))
frAtmIwfConnStatusChange.setObjects(*((_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:frAtmIwfConnStatusChange.setStatus(_B)
frAtmIwfNotificationsGroup=NotificationGroup((1,3,6,1,2,1,86,3,1,4))
frAtmIwfNotificationsGroup.setObjects((_A,_y))
if mibBuilder.loadTexts:frAtmIwfNotificationsGroup.setStatus(_B)
frAtmIwfEquipmentCompliance=ModuleCompliance((1,3,6,1,2,1,86,3,2,1))
frAtmIwfEquipmentCompliance.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:frAtmIwfEquipmentCompliance.setStatus(_B)
frAtmIwfServiceCompliance=ModuleCompliance((1,3,6,1,2,1,86,3,2,2))
frAtmIwfServiceCompliance.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:frAtmIwfServiceCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'frAtmIwfMIB':frAtmIwfMIB,'frAtmIwfMIBObjects':frAtmIwfMIBObjects,_d:frAtmIwfConnIndexNext,'frAtmIwfConnectionTable':frAtmIwfConnectionTable,'frAtmIwfConnectionEntry':frAtmIwfConnectionEntry,_Q:frAtmIwfConnIndex,_R:frAtmIwfConnAtmPort,_S:frAtmIwfConnVpi,_T:frAtmIwfConnVci,_U:frAtmIwfConnFrPort,_V:frAtmIwfConnDlci,_n:frAtmIwfConnRowStatus,_J:frAtmIwfConnAdminStatus,_K:frAtmIwfConnAtm2FrOperStatus,_e:frAtmIwfConnAtm2FrLastChange,_L:frAtmIwfConnFr2AtmOperStatus,_f:frAtmIwfConnFr2AtmLastChange,_g:frAtmIwfConnectionDescriptor,_h:frAtmIwfConnFailedFrameTranslate,_i:frAtmIwfConnOverSizedFrames,_j:frAtmIwfConnFailedAal5PduTranslate,_k:frAtmIwfConnOverSizedSDUs,_l:frAtmIwfConnCrcErrors,_m:frAtmIwfConnSarTimeOuts,_o:frAtmIwfConnectionDescriptorIndexNext,'frAtmIwfConnectionDescriptorTable':frAtmIwfConnectionDescriptorTable,'frAtmIwfConnectionDescriptorEntry':frAtmIwfConnectionDescriptorEntry,_X:frAtmIwfConnectionDescriptorIndex,_w:frAtmIwfConnDescriptorRowStatus,_p:frAtmIwfConnDeToClpMappingMode,_q:frAtmIwfConnClpToDeMappingMode,_r:frAtmIwfConnCongestionMappingMode,_s:frAtmIwfConnEncapsulationMappingMode,_t:frAtmIwfConnEncapsulationMappings,_u:frAtmIwfConnFragAndReassEnabled,_v:frAtmIwfConnArpTranslationEnabled,'frAtmIwfVclTable':frAtmIwfVclTable,_c:frAtmIwfVclEntry,_x:frAtmIwfVclCrossConnectIdentifier,'frAtmIwfTraps':frAtmIwfTraps,'frAtmIwfTrapsPrefix':frAtmIwfTrapsPrefix,_y:frAtmIwfConnStatusChange,'frAtmIwfConformance':frAtmIwfConformance,'frAtmIwfGroups':frAtmIwfGroups,_M:frAtmIwfBasicGroup,_N:frAtmIwfConnectionDescriptorGroup,_O:frAtmIwfAtmVclTableAugmentGroup,_P:frAtmIwfNotificationsGroup,'frAtmIwfCompliances':frAtmIwfCompliances,'frAtmIwfEquipmentCompliance':frAtmIwfEquipmentCompliance,'frAtmIwfServiceCompliance':frAtmIwfServiceCompliance})