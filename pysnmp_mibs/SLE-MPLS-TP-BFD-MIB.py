_J='sleMplsTpBfdSessionInfoSessIndex'
_I='sleMplsTpBfdCfgInfoMeIndex'
_H='sleMplsTpBfdCfgInfoMegIndex'
_G='Integer32'
_F='not-accessible'
_E='SLE-MPLS-TP-BFD-MIB'
_D='read-write'
_C='Unsigned32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sleMgmt,=mibBuilder.importSymbols('DASAN-SMI','sleMgmt')
IANAbfdDiagTC,=mibBuilder.importSymbols('IANA-BFD-TC-STD-MIB','IANAbfdDiagTC')
SleControlRequestResultType,SleControlStatusType=mibBuilder.importSymbols('SLE-TC-MIB','SleControlRequestResultType','SleControlStatusType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sleMplsTpBfd=ModuleIdentity((1,3,6,1,4,1,6296,101,16,19))
if mibBuilder.loadTexts:sleMplsTpBfd.setRevisions(('2004-06-03 00:00',))
_SleMpls_ObjectIdentity=ObjectIdentity
sleMpls=_SleMpls_ObjectIdentity((1,3,6,1,4,1,6296,101,16))
if mibBuilder.loadTexts:sleMpls.setStatus(_A)
_SleMplsTpBfdCfg_ObjectIdentity=ObjectIdentity
sleMplsTpBfdCfg=_SleMplsTpBfdCfg_ObjectIdentity((1,3,6,1,4,1,6296,101,16,19,1))
_SleMplsTpBfdCfgInfoTable_Object=MibTable
sleMplsTpBfdCfgInfoTable=_SleMplsTpBfdCfgInfoTable_Object((1,3,6,1,4,1,6296,101,16,19,1,1))
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoTable.setStatus(_A)
_SleMplsTpBfdCfgInfoEntry_Object=MibTableRow
sleMplsTpBfdCfgInfoEntry=_SleMplsTpBfdCfgInfoEntry_Object((1,3,6,1,4,1,6296,101,16,19,1,1,1))
sleMplsTpBfdCfgInfoEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoEntry.setStatus(_A)
class _SleMplsTpBfdCfgInfoMegIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleMplsTpBfdCfgInfoMegIndex_Type.__name__=_C
_SleMplsTpBfdCfgInfoMegIndex_Object=MibTableColumn
sleMplsTpBfdCfgInfoMegIndex=_SleMplsTpBfdCfgInfoMegIndex_Object((1,3,6,1,4,1,6296,101,16,19,1,1,1,1),_SleMplsTpBfdCfgInfoMegIndex_Type())
sleMplsTpBfdCfgInfoMegIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoMegIndex.setStatus(_A)
class _SleMplsTpBfdCfgInfoMeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleMplsTpBfdCfgInfoMeIndex_Type.__name__=_C
_SleMplsTpBfdCfgInfoMeIndex_Object=MibTableColumn
sleMplsTpBfdCfgInfoMeIndex=_SleMplsTpBfdCfgInfoMeIndex_Object((1,3,6,1,4,1,6296,101,16,19,1,1,1,2),_SleMplsTpBfdCfgInfoMeIndex_Type())
sleMplsTpBfdCfgInfoMeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoMeIndex.setStatus(_A)
_SleMplsTpBfdCfgInfoMegName_Type=OctetString
_SleMplsTpBfdCfgInfoMegName_Object=MibTableColumn
sleMplsTpBfdCfgInfoMegName=_SleMplsTpBfdCfgInfoMegName_Object((1,3,6,1,4,1,6296,101,16,19,1,1,1,3),_SleMplsTpBfdCfgInfoMegName_Type())
sleMplsTpBfdCfgInfoMegName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoMegName.setStatus(_A)
_SleMplsTpBfdCfgInfoMeName_Type=OctetString
_SleMplsTpBfdCfgInfoMeName_Object=MibTableColumn
sleMplsTpBfdCfgInfoMeName=_SleMplsTpBfdCfgInfoMeName_Object((1,3,6,1,4,1,6296,101,16,19,1,1,1,4),_SleMplsTpBfdCfgInfoMeName_Type())
sleMplsTpBfdCfgInfoMeName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoMeName.setStatus(_A)
_SleMplsTpBfdCfgInfoTxInterval_Type=OctetString
_SleMplsTpBfdCfgInfoTxInterval_Object=MibTableColumn
sleMplsTpBfdCfgInfoTxInterval=_SleMplsTpBfdCfgInfoTxInterval_Object((1,3,6,1,4,1,6296,101,16,19,1,1,1,5),_SleMplsTpBfdCfgInfoTxInterval_Type())
sleMplsTpBfdCfgInfoTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoTxInterval.setStatus(_A)
_SleMplsTpBfdCfgInfoRXInterval_Type=OctetString
_SleMplsTpBfdCfgInfoRXInterval_Object=MibTableColumn
sleMplsTpBfdCfgInfoRXInterval=_SleMplsTpBfdCfgInfoRXInterval_Object((1,3,6,1,4,1,6296,101,16,19,1,1,1,6),_SleMplsTpBfdCfgInfoRXInterval_Type())
sleMplsTpBfdCfgInfoRXInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdCfgInfoRXInterval.setStatus(_A)
_SleMplsTpBfdCfgControl_ObjectIdentity=ObjectIdentity
sleMplsTpBfdCfgControl=_SleMplsTpBfdCfgControl_ObjectIdentity((1,3,6,1,4,1,6296,101,16,19,1,2))
class _SleMplsTpBfdCfgControlRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('createBfdcfgEntry',1),('deleteBfdCfgEntry',2),('setIntervals',3)))
_SleMplsTpBfdCfgControlRequest_Type.__name__=_G
_SleMplsTpBfdCfgControlRequest_Object=MibScalar
sleMplsTpBfdCfgControlRequest=_SleMplsTpBfdCfgControlRequest_Object((1,3,6,1,4,1,6296,101,16,19,1,2,1),_SleMplsTpBfdCfgControlRequest_Type())
sleMplsTpBfdCfgControlRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlRequest.setStatus(_A)
_SleMplsTpBfdCfgControlStatus_Type=SleControlStatusType
_SleMplsTpBfdCfgControlStatus_Object=MibScalar
sleMplsTpBfdCfgControlStatus=_SleMplsTpBfdCfgControlStatus_Object((1,3,6,1,4,1,6296,101,16,19,1,2,2),_SleMplsTpBfdCfgControlStatus_Type())
sleMplsTpBfdCfgControlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlStatus.setStatus(_A)
_SleMplsTpBfdCfgControlTimer_Type=Gauge32
_SleMplsTpBfdCfgControlTimer_Object=MibScalar
sleMplsTpBfdCfgControlTimer=_SleMplsTpBfdCfgControlTimer_Object((1,3,6,1,4,1,6296,101,16,19,1,2,3),_SleMplsTpBfdCfgControlTimer_Type())
sleMplsTpBfdCfgControlTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlTimer.setStatus(_A)
_SleMplsTpBfdCfgControlTimestamp_Type=TimeTicks
_SleMplsTpBfdCfgControlTimestamp_Object=MibScalar
sleMplsTpBfdCfgControlTimestamp=_SleMplsTpBfdCfgControlTimestamp_Object((1,3,6,1,4,1,6296,101,16,19,1,2,4),_SleMplsTpBfdCfgControlTimestamp_Type())
sleMplsTpBfdCfgControlTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlTimestamp.setStatus(_A)
_SleMplsTpBfdCfgControlReqResult_Type=SleControlRequestResultType
_SleMplsTpBfdCfgControlReqResult_Object=MibScalar
sleMplsTpBfdCfgControlReqResult=_SleMplsTpBfdCfgControlReqResult_Object((1,3,6,1,4,1,6296,101,16,19,1,2,5),_SleMplsTpBfdCfgControlReqResult_Type())
sleMplsTpBfdCfgControlReqResult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlReqResult.setStatus(_A)
_SleMplsTpBfdCfgControlMegName_Type=OctetString
_SleMplsTpBfdCfgControlMegName_Object=MibScalar
sleMplsTpBfdCfgControlMegName=_SleMplsTpBfdCfgControlMegName_Object((1,3,6,1,4,1,6296,101,16,19,1,2,6),_SleMplsTpBfdCfgControlMegName_Type())
sleMplsTpBfdCfgControlMegName.setMaxAccess(_F)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlMegName.setStatus(_A)
_SleMplsTpBfdCfgControlMeName_Type=OctetString
_SleMplsTpBfdCfgControlMeName_Object=MibScalar
sleMplsTpBfdCfgControlMeName=_SleMplsTpBfdCfgControlMeName_Object((1,3,6,1,4,1,6296,101,16,19,1,2,7),_SleMplsTpBfdCfgControlMeName_Type())
sleMplsTpBfdCfgControlMeName.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlMeName.setStatus(_A)
_SleMplsTpBfdCfgControlTxInterval_Type=OctetString
_SleMplsTpBfdCfgControlTxInterval_Object=MibScalar
sleMplsTpBfdCfgControlTxInterval=_SleMplsTpBfdCfgControlTxInterval_Object((1,3,6,1,4,1,6296,101,16,19,1,2,8),_SleMplsTpBfdCfgControlTxInterval_Type())
sleMplsTpBfdCfgControlTxInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlTxInterval.setStatus(_A)
_SleMplsTpBfdCfgControlRXInterval_Type=OctetString
_SleMplsTpBfdCfgControlRXInterval_Object=MibScalar
sleMplsTpBfdCfgControlRXInterval=_SleMplsTpBfdCfgControlRXInterval_Object((1,3,6,1,4,1,6296,101,16,19,1,2,9),_SleMplsTpBfdCfgControlRXInterval_Type())
sleMplsTpBfdCfgControlRXInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:sleMplsTpBfdCfgControlRXInterval.setStatus(_A)
_SleMplsTpBfdSession_ObjectIdentity=ObjectIdentity
sleMplsTpBfdSession=_SleMplsTpBfdSession_ObjectIdentity((1,3,6,1,4,1,6296,101,16,19,2))
_SleMplsTpBfdSessionInfoTable_Object=MibTable
sleMplsTpBfdSessionInfoTable=_SleMplsTpBfdSessionInfoTable_Object((1,3,6,1,4,1,6296,101,16,19,2,1))
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoTable.setStatus(_A)
_SleMplsTpBfdSessionInfoEntry_Object=MibTableRow
sleMplsTpBfdSessionInfoEntry=_SleMplsTpBfdSessionInfoEntry_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1))
sleMplsTpBfdSessionInfoEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoEntry.setStatus(_A)
class _SleMplsTpBfdSessionInfoSessIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SleMplsTpBfdSessionInfoSessIndex_Type.__name__=_C
_SleMplsTpBfdSessionInfoSessIndex_Object=MibTableColumn
sleMplsTpBfdSessionInfoSessIndex=_SleMplsTpBfdSessionInfoSessIndex_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,1),_SleMplsTpBfdSessionInfoSessIndex_Type())
sleMplsTpBfdSessionInfoSessIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoSessIndex.setStatus(_A)
_SleMplsTpBfdSessionInfoMegName_Type=OctetString
_SleMplsTpBfdSessionInfoMegName_Object=MibTableColumn
sleMplsTpBfdSessionInfoMegName=_SleMplsTpBfdSessionInfoMegName_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,2),_SleMplsTpBfdSessionInfoMegName_Type())
sleMplsTpBfdSessionInfoMegName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoMegName.setStatus(_A)
_SleMplsTpBfdSessionInfoMeName_Type=OctetString
_SleMplsTpBfdSessionInfoMeName_Object=MibTableColumn
sleMplsTpBfdSessionInfoMeName=_SleMplsTpBfdSessionInfoMeName_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,3),_SleMplsTpBfdSessionInfoMeName_Type())
sleMplsTpBfdSessionInfoMeName.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoMeName.setStatus(_A)
class _SleMplsTpBfdSessionInfoVersionNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SleMplsTpBfdSessionInfoVersionNumber_Type.__name__=_C
_SleMplsTpBfdSessionInfoVersionNumber_Object=MibTableColumn
sleMplsTpBfdSessionInfoVersionNumber=_SleMplsTpBfdSessionInfoVersionNumber_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,4),_SleMplsTpBfdSessionInfoVersionNumber_Type())
sleMplsTpBfdSessionInfoVersionNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoVersionNumber.setStatus(_A)
class _SleMplsTpBfdSessionInfoDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SleMplsTpBfdSessionInfoDiscriminator_Type.__name__=_C
_SleMplsTpBfdSessionInfoDiscriminator_Object=MibTableColumn
sleMplsTpBfdSessionInfoDiscriminator=_SleMplsTpBfdSessionInfoDiscriminator_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,5),_SleMplsTpBfdSessionInfoDiscriminator_Type())
sleMplsTpBfdSessionInfoDiscriminator.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoDiscriminator.setStatus(_A)
class _SleMplsTpBfdSessionInfoRemoteDiscriminator_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_SleMplsTpBfdSessionInfoRemoteDiscriminator_Type.__name__=_C
_SleMplsTpBfdSessionInfoRemoteDiscriminator_Object=MibTableColumn
sleMplsTpBfdSessionInfoRemoteDiscriminator=_SleMplsTpBfdSessionInfoRemoteDiscriminator_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,6),_SleMplsTpBfdSessionInfoRemoteDiscriminator_Type())
sleMplsTpBfdSessionInfoRemoteDiscriminator.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoRemoteDiscriminator.setStatus(_A)
class _SleMplsTpBfdSessionInfoState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('adminDown',0),('stateDown',1),('stateInit',2),('stateUp',3),('unknown',4)))
_SleMplsTpBfdSessionInfoState_Type.__name__=_G
_SleMplsTpBfdSessionInfoState_Object=MibTableColumn
sleMplsTpBfdSessionInfoState=_SleMplsTpBfdSessionInfoState_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,7),_SleMplsTpBfdSessionInfoState_Type())
sleMplsTpBfdSessionInfoState.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoState.setStatus(_A)
_SleMplsTpBfdSessionInfoDiag_Type=IANAbfdDiagTC
_SleMplsTpBfdSessionInfoDiag_Object=MibTableColumn
sleMplsTpBfdSessionInfoDiag=_SleMplsTpBfdSessionInfoDiag_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,8),_SleMplsTpBfdSessionInfoDiag_Type())
sleMplsTpBfdSessionInfoDiag.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoDiag.setStatus(_A)
_SleMplsTpBfdSessionInfoDesiredMinTxInterval_Type=OctetString
_SleMplsTpBfdSessionInfoDesiredMinTxInterval_Object=MibTableColumn
sleMplsTpBfdSessionInfoDesiredMinTxInterval=_SleMplsTpBfdSessionInfoDesiredMinTxInterval_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,9),_SleMplsTpBfdSessionInfoDesiredMinTxInterval_Type())
sleMplsTpBfdSessionInfoDesiredMinTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoDesiredMinTxInterval.setStatus(_A)
_SleMplsTpBfdSessionInfoReqMinRxInterval_Type=OctetString
_SleMplsTpBfdSessionInfoReqMinRxInterval_Object=MibTableColumn
sleMplsTpBfdSessionInfoReqMinRxInterval=_SleMplsTpBfdSessionInfoReqMinRxInterval_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,10),_SleMplsTpBfdSessionInfoReqMinRxInterval_Type())
sleMplsTpBfdSessionInfoReqMinRxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoReqMinRxInterval.setStatus(_A)
_SleMplsTpBfdSessionInfoDetectMult_Type=Unsigned32
_SleMplsTpBfdSessionInfoDetectMult_Object=MibTableColumn
sleMplsTpBfdSessionInfoDetectMult=_SleMplsTpBfdSessionInfoDetectMult_Object((1,3,6,1,4,1,6296,101,16,19,2,1,1,11),_SleMplsTpBfdSessionInfoDetectMult_Type())
sleMplsTpBfdSessionInfoDetectMult.setMaxAccess(_B)
if mibBuilder.loadTexts:sleMplsTpBfdSessionInfoDetectMult.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'sleMpls':sleMpls,'sleMplsTpBfd':sleMplsTpBfd,'sleMplsTpBfdCfg':sleMplsTpBfdCfg,'sleMplsTpBfdCfgInfoTable':sleMplsTpBfdCfgInfoTable,'sleMplsTpBfdCfgInfoEntry':sleMplsTpBfdCfgInfoEntry,_H:sleMplsTpBfdCfgInfoMegIndex,_I:sleMplsTpBfdCfgInfoMeIndex,'sleMplsTpBfdCfgInfoMegName':sleMplsTpBfdCfgInfoMegName,'sleMplsTpBfdCfgInfoMeName':sleMplsTpBfdCfgInfoMeName,'sleMplsTpBfdCfgInfoTxInterval':sleMplsTpBfdCfgInfoTxInterval,'sleMplsTpBfdCfgInfoRXInterval':sleMplsTpBfdCfgInfoRXInterval,'sleMplsTpBfdCfgControl':sleMplsTpBfdCfgControl,'sleMplsTpBfdCfgControlRequest':sleMplsTpBfdCfgControlRequest,'sleMplsTpBfdCfgControlStatus':sleMplsTpBfdCfgControlStatus,'sleMplsTpBfdCfgControlTimer':sleMplsTpBfdCfgControlTimer,'sleMplsTpBfdCfgControlTimestamp':sleMplsTpBfdCfgControlTimestamp,'sleMplsTpBfdCfgControlReqResult':sleMplsTpBfdCfgControlReqResult,'sleMplsTpBfdCfgControlMegName':sleMplsTpBfdCfgControlMegName,'sleMplsTpBfdCfgControlMeName':sleMplsTpBfdCfgControlMeName,'sleMplsTpBfdCfgControlTxInterval':sleMplsTpBfdCfgControlTxInterval,'sleMplsTpBfdCfgControlRXInterval':sleMplsTpBfdCfgControlRXInterval,'sleMplsTpBfdSession':sleMplsTpBfdSession,'sleMplsTpBfdSessionInfoTable':sleMplsTpBfdSessionInfoTable,'sleMplsTpBfdSessionInfoEntry':sleMplsTpBfdSessionInfoEntry,_J:sleMplsTpBfdSessionInfoSessIndex,'sleMplsTpBfdSessionInfoMegName':sleMplsTpBfdSessionInfoMegName,'sleMplsTpBfdSessionInfoMeName':sleMplsTpBfdSessionInfoMeName,'sleMplsTpBfdSessionInfoVersionNumber':sleMplsTpBfdSessionInfoVersionNumber,'sleMplsTpBfdSessionInfoDiscriminator':sleMplsTpBfdSessionInfoDiscriminator,'sleMplsTpBfdSessionInfoRemoteDiscriminator':sleMplsTpBfdSessionInfoRemoteDiscriminator,'sleMplsTpBfdSessionInfoState':sleMplsTpBfdSessionInfoState,'sleMplsTpBfdSessionInfoDiag':sleMplsTpBfdSessionInfoDiag,'sleMplsTpBfdSessionInfoDesiredMinTxInterval':sleMplsTpBfdSessionInfoDesiredMinTxInterval,'sleMplsTpBfdSessionInfoReqMinRxInterval':sleMplsTpBfdSessionInfoReqMinRxInterval,'sleMplsTpBfdSessionInfoDetectMult':sleMplsTpBfdSessionInfoDetectMult})