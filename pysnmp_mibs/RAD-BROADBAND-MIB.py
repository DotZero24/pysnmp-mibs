_N='prtPhyIntervalNumber'
_M='read-create'
_L='notApplicable'
_K='prtBdbandIndEvent'
_J='prtBdbandIndSig'
_I='prtBdbandIdx'
_H='prtBdbandCnfgIdx'
_G='OctetString'
_F='ifIndex'
_E='IF-MIB'
_D='RAD-BROADBAND-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
diverseIfWanGen,=mibBuilder.importSymbols('RAD-SMI-MIB','diverseIfWanGen')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
broadbandIf=ModuleIdentity((1,3,6,1,4,1,164,3,1,6,8))
_BdbandConfig_ObjectIdentity=ObjectIdentity
bdbandConfig=_BdbandConfig_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,8,1))
_PrtBdbandIndTable_Object=MibTable
prtBdbandIndTable=_PrtBdbandIndTable_Object((1,3,6,1,4,1,164,3,1,6,8,1,1))
if mibBuilder.loadTexts:prtBdbandIndTable.setStatus(_A)
_PrtBdbandIndEntry_Object=MibTableRow
prtBdbandIndEntry=_PrtBdbandIndEntry_Object((1,3,6,1,4,1,164,3,1,6,8,1,1,1))
prtBdbandIndEntry.setIndexNames((0,_D,_H),(0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:prtBdbandIndEntry.setStatus(_A)
class _PrtBdbandCnfgIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_PrtBdbandCnfgIdx_Type.__name__=_C
_PrtBdbandCnfgIdx_Object=MibTableColumn
prtBdbandCnfgIdx=_PrtBdbandCnfgIdx_Object((1,3,6,1,4,1,164,3,1,6,8,1,1,1,1),_PrtBdbandCnfgIdx_Type())
prtBdbandCnfgIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:prtBdbandCnfgIdx.setStatus(_A)
_PrtBdbandIdx_Type=Integer32
_PrtBdbandIdx_Object=MibTableColumn
prtBdbandIdx=_PrtBdbandIdx_Object((1,3,6,1,4,1,164,3,1,6,8,1,1,1,2),_PrtBdbandIdx_Type())
prtBdbandIdx.setMaxAccess(_B)
if mibBuilder.loadTexts:prtBdbandIdx.setStatus(_A)
class _PrtBdbandIndSig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ais',1),('rdi',2),('aisAndRdi',3)))
_PrtBdbandIndSig_Type.__name__=_C
_PrtBdbandIndSig_Object=MibTableColumn
prtBdbandIndSig=_PrtBdbandIndSig_Object((1,3,6,1,4,1,164,3,1,6,8,1,1,1,3),_PrtBdbandIndSig_Type())
prtBdbandIndSig.setMaxAccess(_B)
if mibBuilder.loadTexts:prtBdbandIndSig.setStatus(_A)
class _PrtBdbandIndEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),('slm',2),('fail',3),('eed',4),('pathTrace',5),('lom',6),('lop',7),('slu',8)))
_PrtBdbandIndEvent_Type.__name__=_C
_PrtBdbandIndEvent_Object=MibTableColumn
prtBdbandIndEvent=_PrtBdbandIndEvent_Object((1,3,6,1,4,1,164,3,1,6,8,1,1,1,4),_PrtBdbandIndEvent_Type())
prtBdbandIndEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:prtBdbandIndEvent.setStatus(_A)
class _PrtBdbandIndSigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('disable',2),('enable',3)))
_PrtBdbandIndSigEnable_Type.__name__=_C
_PrtBdbandIndSigEnable_Object=MibTableColumn
prtBdbandIndSigEnable=_PrtBdbandIndSigEnable_Object((1,3,6,1,4,1,164,3,1,6,8,1,1,1,5),_PrtBdbandIndSigEnable_Type())
prtBdbandIndSigEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:prtBdbandIndSigEnable.setStatus(_A)
_PrtBdbandRowStatus_Type=RowStatus
_PrtBdbandRowStatus_Object=MibTableColumn
prtBdbandRowStatus=_PrtBdbandRowStatus_Object((1,3,6,1,4,1,164,3,1,6,8,1,1,1,6),_PrtBdbandRowStatus_Type())
prtBdbandRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:prtBdbandRowStatus.setStatus(_A)
_PrtPhyConfigTable_Object=MibTable
prtPhyConfigTable=_PrtPhyConfigTable_Object((1,3,6,1,4,1,164,3,1,6,8,1,2))
if mibBuilder.loadTexts:prtPhyConfigTable.setStatus(_A)
_PrtPhyConfigEntry_Object=MibTableRow
prtPhyConfigEntry=_PrtPhyConfigEntry_Object((1,3,6,1,4,1,164,3,1,6,8,1,2,1))
prtPhyConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:prtPhyConfigEntry.setStatus(_A)
class _PrtPhyTimeElapsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,899))
_PrtPhyTimeElapsed_Type.__name__=_C
_PrtPhyTimeElapsed_Object=MibTableColumn
prtPhyTimeElapsed=_PrtPhyTimeElapsed_Object((1,3,6,1,4,1,164,3,1,6,8,1,2,1,1),_PrtPhyTimeElapsed_Type())
prtPhyTimeElapsed.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyTimeElapsed.setStatus(_A)
class _PrtPhyValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_PrtPhyValidIntervals_Type.__name__=_C
_PrtPhyValidIntervals_Object=MibTableColumn
prtPhyValidIntervals=_PrtPhyValidIntervals_Object((1,3,6,1,4,1,164,3,1,6,8,1,2,1,2),_PrtPhyValidIntervals_Type())
prtPhyValidIntervals.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyValidIntervals.setStatus(_A)
_PrtPhyPerfHistory_ObjectIdentity=ObjectIdentity
prtPhyPerfHistory=_PrtPhyPerfHistory_ObjectIdentity((1,3,6,1,4,1,164,3,1,6,8,2))
_PrtPhyCurrentTable_Object=MibTable
prtPhyCurrentTable=_PrtPhyCurrentTable_Object((1,3,6,1,4,1,164,3,1,6,8,2,1))
if mibBuilder.loadTexts:prtPhyCurrentTable.setStatus(_A)
_PrtPhyCurrentEntry_Object=MibTableRow
prtPhyCurrentEntry=_PrtPhyCurrentEntry_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1))
prtPhyCurrentEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:prtPhyCurrentEntry.setStatus(_A)
_PrtPhyCurrentLOS_Type=Gauge32
_PrtPhyCurrentLOS_Object=MibTableColumn
prtPhyCurrentLOS=_PrtPhyCurrentLOS_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1,1),_PrtPhyCurrentLOS_Type())
prtPhyCurrentLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyCurrentLOS.setStatus(_A)
_PrtPhyCurrentLSV_Type=Gauge32
_PrtPhyCurrentLSV_Object=MibTableColumn
prtPhyCurrentLSV=_PrtPhyCurrentLSV_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1,2),_PrtPhyCurrentLSV_Type())
prtPhyCurrentLSV.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyCurrentLSV.setStatus(_A)
_PrtPhyCurrentUAS_Type=Gauge32
_PrtPhyCurrentUAS_Object=MibTableColumn
prtPhyCurrentUAS=_PrtPhyCurrentUAS_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1,3),_PrtPhyCurrentUAS_Type())
prtPhyCurrentUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyCurrentUAS.setStatus(_A)
_PrtPhyCurrentSES_Type=Gauge32
_PrtPhyCurrentSES_Object=MibTableColumn
prtPhyCurrentSES=_PrtPhyCurrentSES_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1,4),_PrtPhyCurrentSES_Type())
prtPhyCurrentSES.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyCurrentSES.setStatus(_A)
_PrtPhyCurrentES_Type=Gauge32
_PrtPhyCurrentES_Object=MibTableColumn
prtPhyCurrentES=_PrtPhyCurrentES_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1,5),_PrtPhyCurrentES_Type())
prtPhyCurrentES.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyCurrentES.setStatus(_A)
class _PrtPhyCurrentStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_PrtPhyCurrentStatus_Type.__name__=_G
_PrtPhyCurrentStatus_Object=MibTableColumn
prtPhyCurrentStatus=_PrtPhyCurrentStatus_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1,6),_PrtPhyCurrentStatus_Type())
prtPhyCurrentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyCurrentStatus.setStatus(_A)
_PrtPhyCurrentLOF_Type=Gauge32
_PrtPhyCurrentLOF_Object=MibTableColumn
prtPhyCurrentLOF=_PrtPhyCurrentLOF_Object((1,3,6,1,4,1,164,3,1,6,8,2,1,1,7),_PrtPhyCurrentLOF_Type())
prtPhyCurrentLOF.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyCurrentLOF.setStatus(_A)
_PrtPhyIntervalTable_Object=MibTable
prtPhyIntervalTable=_PrtPhyIntervalTable_Object((1,3,6,1,4,1,164,3,1,6,8,2,2))
if mibBuilder.loadTexts:prtPhyIntervalTable.setStatus(_A)
_PrtPhyIntervalEntry_Object=MibTableRow
prtPhyIntervalEntry=_PrtPhyIntervalEntry_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1))
prtPhyIntervalEntry.setIndexNames((0,_E,_F),(0,_D,_N))
if mibBuilder.loadTexts:prtPhyIntervalEntry.setStatus(_A)
class _PrtPhyIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_PrtPhyIntervalNumber_Type.__name__=_C
_PrtPhyIntervalNumber_Object=MibTableColumn
prtPhyIntervalNumber=_PrtPhyIntervalNumber_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,1),_PrtPhyIntervalNumber_Type())
prtPhyIntervalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalNumber.setStatus(_A)
_PrtPhyIntervalLOS_Type=Gauge32
_PrtPhyIntervalLOS_Object=MibTableColumn
prtPhyIntervalLOS=_PrtPhyIntervalLOS_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,2),_PrtPhyIntervalLOS_Type())
prtPhyIntervalLOS.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalLOS.setStatus(_A)
_PrtPhyIntervalLSV_Type=Gauge32
_PrtPhyIntervalLSV_Object=MibTableColumn
prtPhyIntervalLSV=_PrtPhyIntervalLSV_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,3),_PrtPhyIntervalLSV_Type())
prtPhyIntervalLSV.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalLSV.setStatus(_A)
_PrtPhyIntervalUAS_Type=Gauge32
_PrtPhyIntervalUAS_Object=MibTableColumn
prtPhyIntervalUAS=_PrtPhyIntervalUAS_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,4),_PrtPhyIntervalUAS_Type())
prtPhyIntervalUAS.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalUAS.setStatus(_A)
_PrtPhyIntervalSES_Type=Gauge32
_PrtPhyIntervalSES_Object=MibTableColumn
prtPhyIntervalSES=_PrtPhyIntervalSES_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,5),_PrtPhyIntervalSES_Type())
prtPhyIntervalSES.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalSES.setStatus(_A)
_PrtPhyIntervalES_Type=Gauge32
_PrtPhyIntervalES_Object=MibTableColumn
prtPhyIntervalES=_PrtPhyIntervalES_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,6),_PrtPhyIntervalES_Type())
prtPhyIntervalES.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalES.setStatus(_A)
class _PrtPhyIntervalStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_PrtPhyIntervalStatus_Type.__name__=_G
_PrtPhyIntervalStatus_Object=MibTableColumn
prtPhyIntervalStatus=_PrtPhyIntervalStatus_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,7),_PrtPhyIntervalStatus_Type())
prtPhyIntervalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalStatus.setStatus(_A)
_PrtPhyIntervalLOF_Type=Gauge32
_PrtPhyIntervalLOF_Object=MibTableColumn
prtPhyIntervalLOF=_PrtPhyIntervalLOF_Object((1,3,6,1,4,1,164,3,1,6,8,2,2,1,8),_PrtPhyIntervalLOF_Type())
prtPhyIntervalLOF.setMaxAccess(_B)
if mibBuilder.loadTexts:prtPhyIntervalLOF.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'broadbandIf':broadbandIf,'bdbandConfig':bdbandConfig,'prtBdbandIndTable':prtBdbandIndTable,'prtBdbandIndEntry':prtBdbandIndEntry,_H:prtBdbandCnfgIdx,_I:prtBdbandIdx,_J:prtBdbandIndSig,_K:prtBdbandIndEvent,'prtBdbandIndSigEnable':prtBdbandIndSigEnable,'prtBdbandRowStatus':prtBdbandRowStatus,'prtPhyConfigTable':prtPhyConfigTable,'prtPhyConfigEntry':prtPhyConfigEntry,'prtPhyTimeElapsed':prtPhyTimeElapsed,'prtPhyValidIntervals':prtPhyValidIntervals,'prtPhyPerfHistory':prtPhyPerfHistory,'prtPhyCurrentTable':prtPhyCurrentTable,'prtPhyCurrentEntry':prtPhyCurrentEntry,'prtPhyCurrentLOS':prtPhyCurrentLOS,'prtPhyCurrentLSV':prtPhyCurrentLSV,'prtPhyCurrentUAS':prtPhyCurrentUAS,'prtPhyCurrentSES':prtPhyCurrentSES,'prtPhyCurrentES':prtPhyCurrentES,'prtPhyCurrentStatus':prtPhyCurrentStatus,'prtPhyCurrentLOF':prtPhyCurrentLOF,'prtPhyIntervalTable':prtPhyIntervalTable,'prtPhyIntervalEntry':prtPhyIntervalEntry,_N:prtPhyIntervalNumber,'prtPhyIntervalLOS':prtPhyIntervalLOS,'prtPhyIntervalLSV':prtPhyIntervalLSV,'prtPhyIntervalUAS':prtPhyIntervalUAS,'prtPhyIntervalSES':prtPhyIntervalSES,'prtPhyIntervalES':prtPhyIntervalES,'prtPhyIntervalStatus':prtPhyIntervalStatus,'prtPhyIntervalLOF':prtPhyIntervalLOF})