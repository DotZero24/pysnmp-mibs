_a='vdslLineExtSCMGroup'
_Z='vdslLineSCMPhysBandCurrAtn'
_Y='vdslLineSCMPhysBandCurrSnrMgn'
_X='vdslLineSCMPhysBandCurrCenterFrequency'
_W='vdslLineSCMPhysBandCurrConstellationSize'
_V='vdslLineSCMPhysBandCurrSymbolRate'
_U='vdslLineSCMPhysBandCurrPSDLevel'
_T='vdslLineSCMPhysBandInUse'
_S='vdslLineSCMConfProfileBandRowStatus'
_R='vdslLineSCMConfProfileBandCenterFrequency'
_Q='vdslLineSCMConfProfileBandConstellationSize'
_P='vdslLineSCMConfProfileBandSymbolRate'
_O='vdslLineSCMConfProfileBandTransmitPSDLevel'
_N='vdslLineSCMConfProfileBandInUse'
_M='0.25 dB'
_L='vdslLineSCMPhysBandId'
_K='not-accessible'
_J='vdslLineSCMConfProfileBandId'
_I='vdslLineConfProfileName'
_H='VDSL-LINE-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='Unsigned32'
_D='read-create'
_C='read-only'
_B='VDSL-LINE-EXT-SCM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','transmission')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
vdslLineConfProfileName,=mibBuilder.importSymbols(_H,_I)
vdslExtSCMMIB=ModuleIdentity((1,3,6,1,2,1,10,228))
if mibBuilder.loadTexts:vdslExtSCMMIB.setRevisions(('2005-04-28 00:00',))
class VdslSCMBandId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('optionalBand',1),('firstDownstreamBand',2),('firstUpstreamBand',3),('secondDownstreamBand',4),('secondUpstreamBand',5),('thirdDownstreamBand',6),('thirdUpstreamBand',7)))
_VdslLineExtSCMMib_ObjectIdentity=ObjectIdentity
vdslLineExtSCMMib=_VdslLineExtSCMMib_ObjectIdentity((1,3,6,1,2,1,10,228,1))
_VdslLineExtSCMMibObjects_ObjectIdentity=ObjectIdentity
vdslLineExtSCMMibObjects=_VdslLineExtSCMMibObjects_ObjectIdentity((1,3,6,1,2,1,10,228,1,1))
_VdslLineSCMConfProfileBandTable_Object=MibTable
vdslLineSCMConfProfileBandTable=_VdslLineSCMConfProfileBandTable_Object((1,3,6,1,2,1,10,228,1,1,1))
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandTable.setStatus(_A)
_VdslLineSCMConfProfileBandEntry_Object=MibTableRow
vdslLineSCMConfProfileBandEntry=_VdslLineSCMConfProfileBandEntry_Object((1,3,6,1,2,1,10,228,1,1,1,1))
vdslLineSCMConfProfileBandEntry.setIndexNames((0,_H,_I),(0,_B,_J))
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandEntry.setStatus(_A)
_VdslLineSCMConfProfileBandId_Type=VdslSCMBandId
_VdslLineSCMConfProfileBandId_Object=MibTableColumn
vdslLineSCMConfProfileBandId=_VdslLineSCMConfProfileBandId_Object((1,3,6,1,2,1,10,228,1,1,1,1,1),_VdslLineSCMConfProfileBandId_Type())
vdslLineSCMConfProfileBandId.setMaxAccess(_K)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandId.setStatus(_A)
_VdslLineSCMConfProfileBandInUse_Type=TruthValue
_VdslLineSCMConfProfileBandInUse_Object=MibTableColumn
vdslLineSCMConfProfileBandInUse=_VdslLineSCMConfProfileBandInUse_Object((1,3,6,1,2,1,10,228,1,1,1,1,2),_VdslLineSCMConfProfileBandInUse_Type())
vdslLineSCMConfProfileBandInUse.setMaxAccess(_D)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandInUse.setStatus(_A)
_VdslLineSCMConfProfileBandCenterFrequency_Type=Unsigned32
_VdslLineSCMConfProfileBandCenterFrequency_Object=MibTableColumn
vdslLineSCMConfProfileBandCenterFrequency=_VdslLineSCMConfProfileBandCenterFrequency_Object((1,3,6,1,2,1,10,228,1,1,1,1,3),_VdslLineSCMConfProfileBandCenterFrequency_Type())
vdslLineSCMConfProfileBandCenterFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandCenterFrequency.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandCenterFrequency.setUnits('Hz')
_VdslLineSCMConfProfileBandSymbolRate_Type=Unsigned32
_VdslLineSCMConfProfileBandSymbolRate_Object=MibTableColumn
vdslLineSCMConfProfileBandSymbolRate=_VdslLineSCMConfProfileBandSymbolRate_Object((1,3,6,1,2,1,10,228,1,1,1,1,4),_VdslLineSCMConfProfileBandSymbolRate_Type())
vdslLineSCMConfProfileBandSymbolRate.setMaxAccess(_D)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandSymbolRate.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandSymbolRate.setUnits('baud')
class _VdslLineSCMConfProfileBandConstellationSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_VdslLineSCMConfProfileBandConstellationSize_Type.__name__=_E
_VdslLineSCMConfProfileBandConstellationSize_Object=MibTableColumn
vdslLineSCMConfProfileBandConstellationSize=_VdslLineSCMConfProfileBandConstellationSize_Object((1,3,6,1,2,1,10,228,1,1,1,1,5),_VdslLineSCMConfProfileBandConstellationSize_Type())
vdslLineSCMConfProfileBandConstellationSize.setMaxAccess(_D)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandConstellationSize.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandConstellationSize.setUnits('log2')
_VdslLineSCMConfProfileBandTransmitPSDLevel_Type=Unsigned32
_VdslLineSCMConfProfileBandTransmitPSDLevel_Object=MibTableColumn
vdslLineSCMConfProfileBandTransmitPSDLevel=_VdslLineSCMConfProfileBandTransmitPSDLevel_Object((1,3,6,1,2,1,10,228,1,1,1,1,6),_VdslLineSCMConfProfileBandTransmitPSDLevel_Type())
vdslLineSCMConfProfileBandTransmitPSDLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandTransmitPSDLevel.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandTransmitPSDLevel.setUnits('-0.25 dBm/Hz')
_VdslLineSCMConfProfileBandRowStatus_Type=RowStatus
_VdslLineSCMConfProfileBandRowStatus_Object=MibTableColumn
vdslLineSCMConfProfileBandRowStatus=_VdslLineSCMConfProfileBandRowStatus_Object((1,3,6,1,2,1,10,228,1,1,1,1,7),_VdslLineSCMConfProfileBandRowStatus_Type())
vdslLineSCMConfProfileBandRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:vdslLineSCMConfProfileBandRowStatus.setStatus(_A)
_VdslLineSCMPhysBandTable_Object=MibTable
vdslLineSCMPhysBandTable=_VdslLineSCMPhysBandTable_Object((1,3,6,1,2,1,10,228,1,1,2))
if mibBuilder.loadTexts:vdslLineSCMPhysBandTable.setStatus(_A)
_VdslLineSCMPhysBandEntry_Object=MibTableRow
vdslLineSCMPhysBandEntry=_VdslLineSCMPhysBandEntry_Object((1,3,6,1,2,1,10,228,1,1,2,1))
vdslLineSCMPhysBandEntry.setIndexNames((0,_F,_G),(0,_B,_L))
if mibBuilder.loadTexts:vdslLineSCMPhysBandEntry.setStatus(_A)
_VdslLineSCMPhysBandId_Type=VdslSCMBandId
_VdslLineSCMPhysBandId_Object=MibTableColumn
vdslLineSCMPhysBandId=_VdslLineSCMPhysBandId_Object((1,3,6,1,2,1,10,228,1,1,2,1,1),_VdslLineSCMPhysBandId_Type())
vdslLineSCMPhysBandId.setMaxAccess(_K)
if mibBuilder.loadTexts:vdslLineSCMPhysBandId.setStatus(_A)
_VdslLineSCMPhysBandInUse_Type=TruthValue
_VdslLineSCMPhysBandInUse_Object=MibTableColumn
vdslLineSCMPhysBandInUse=_VdslLineSCMPhysBandInUse_Object((1,3,6,1,2,1,10,228,1,1,2,1,2),_VdslLineSCMPhysBandInUse_Type())
vdslLineSCMPhysBandInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:vdslLineSCMPhysBandInUse.setStatus(_A)
_VdslLineSCMPhysBandCurrCenterFrequency_Type=Unsigned32
_VdslLineSCMPhysBandCurrCenterFrequency_Object=MibTableColumn
vdslLineSCMPhysBandCurrCenterFrequency=_VdslLineSCMPhysBandCurrCenterFrequency_Object((1,3,6,1,2,1,10,228,1,1,2,1,3),_VdslLineSCMPhysBandCurrCenterFrequency_Type())
vdslLineSCMPhysBandCurrCenterFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrCenterFrequency.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrCenterFrequency.setUnits('Hz')
_VdslLineSCMPhysBandCurrSymbolRate_Type=Unsigned32
_VdslLineSCMPhysBandCurrSymbolRate_Object=MibTableColumn
vdslLineSCMPhysBandCurrSymbolRate=_VdslLineSCMPhysBandCurrSymbolRate_Object((1,3,6,1,2,1,10,228,1,1,2,1,4),_VdslLineSCMPhysBandCurrSymbolRate_Type())
vdslLineSCMPhysBandCurrSymbolRate.setMaxAccess(_C)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrSymbolRate.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrSymbolRate.setUnits('baud')
class _VdslLineSCMPhysBandCurrConstellationSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_VdslLineSCMPhysBandCurrConstellationSize_Type.__name__=_E
_VdslLineSCMPhysBandCurrConstellationSize_Object=MibTableColumn
vdslLineSCMPhysBandCurrConstellationSize=_VdslLineSCMPhysBandCurrConstellationSize_Object((1,3,6,1,2,1,10,228,1,1,2,1,5),_VdslLineSCMPhysBandCurrConstellationSize_Type())
vdslLineSCMPhysBandCurrConstellationSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrConstellationSize.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrConstellationSize.setUnits('log2')
_VdslLineSCMPhysBandCurrPSDLevel_Type=Unsigned32
_VdslLineSCMPhysBandCurrPSDLevel_Object=MibTableColumn
vdslLineSCMPhysBandCurrPSDLevel=_VdslLineSCMPhysBandCurrPSDLevel_Object((1,3,6,1,2,1,10,228,1,1,2,1,6),_VdslLineSCMPhysBandCurrPSDLevel_Type())
vdslLineSCMPhysBandCurrPSDLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrPSDLevel.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrPSDLevel.setUnits('- 0.25 dBm/Hz')
_VdslLineSCMPhysBandCurrSnrMgn_Type=Integer32
_VdslLineSCMPhysBandCurrSnrMgn_Object=MibTableColumn
vdslLineSCMPhysBandCurrSnrMgn=_VdslLineSCMPhysBandCurrSnrMgn_Object((1,3,6,1,2,1,10,228,1,1,2,1,7),_VdslLineSCMPhysBandCurrSnrMgn_Type())
vdslLineSCMPhysBandCurrSnrMgn.setMaxAccess(_C)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrSnrMgn.setUnits(_M)
class _VdslLineSCMPhysBandCurrAtn_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VdslLineSCMPhysBandCurrAtn_Type.__name__=_E
_VdslLineSCMPhysBandCurrAtn_Object=MibTableColumn
vdslLineSCMPhysBandCurrAtn=_VdslLineSCMPhysBandCurrAtn_Object((1,3,6,1,2,1,10,228,1,1,2,1,8),_VdslLineSCMPhysBandCurrAtn_Type())
vdslLineSCMPhysBandCurrAtn.setMaxAccess(_C)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrAtn.setStatus(_A)
if mibBuilder.loadTexts:vdslLineSCMPhysBandCurrAtn.setUnits(_M)
_VdslLineExtSCMConformance_ObjectIdentity=ObjectIdentity
vdslLineExtSCMConformance=_VdslLineExtSCMConformance_ObjectIdentity((1,3,6,1,2,1,10,228,1,2))
_VdslLineExtSCMGroups_ObjectIdentity=ObjectIdentity
vdslLineExtSCMGroups=_VdslLineExtSCMGroups_ObjectIdentity((1,3,6,1,2,1,10,228,1,2,1))
_VdslLineExtSCMCompliances_ObjectIdentity=ObjectIdentity
vdslLineExtSCMCompliances=_VdslLineExtSCMCompliances_ObjectIdentity((1,3,6,1,2,1,10,228,1,2,2))
vdslLineExtSCMGroup=ObjectGroup((1,3,6,1,2,1,10,228,1,2,1,1))
vdslLineExtSCMGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:vdslLineExtSCMGroup.setStatus(_A)
vdslLineExtSCMMibCompliance=ModuleCompliance((1,3,6,1,2,1,10,228,1,2,2,1))
vdslLineExtSCMMibCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:vdslLineExtSCMMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VdslSCMBandId':VdslSCMBandId,'vdslExtSCMMIB':vdslExtSCMMIB,'vdslLineExtSCMMib':vdslLineExtSCMMib,'vdslLineExtSCMMibObjects':vdslLineExtSCMMibObjects,'vdslLineSCMConfProfileBandTable':vdslLineSCMConfProfileBandTable,'vdslLineSCMConfProfileBandEntry':vdslLineSCMConfProfileBandEntry,_J:vdslLineSCMConfProfileBandId,_N:vdslLineSCMConfProfileBandInUse,_R:vdslLineSCMConfProfileBandCenterFrequency,_P:vdslLineSCMConfProfileBandSymbolRate,_Q:vdslLineSCMConfProfileBandConstellationSize,_O:vdslLineSCMConfProfileBandTransmitPSDLevel,_S:vdslLineSCMConfProfileBandRowStatus,'vdslLineSCMPhysBandTable':vdslLineSCMPhysBandTable,'vdslLineSCMPhysBandEntry':vdslLineSCMPhysBandEntry,_L:vdslLineSCMPhysBandId,_T:vdslLineSCMPhysBandInUse,_X:vdslLineSCMPhysBandCurrCenterFrequency,_V:vdslLineSCMPhysBandCurrSymbolRate,_W:vdslLineSCMPhysBandCurrConstellationSize,_U:vdslLineSCMPhysBandCurrPSDLevel,_Y:vdslLineSCMPhysBandCurrSnrMgn,_Z:vdslLineSCMPhysBandCurrAtn,'vdslLineExtSCMConformance':vdslLineExtSCMConformance,'vdslLineExtSCMGroups':vdslLineExtSCMGroups,_a:vdslLineExtSCMGroup,'vdslLineExtSCMCompliances':vdslLineExtSCMCompliances,'vdslLineExtSCMMibCompliance':vdslLineExtSCMMibCompliance})