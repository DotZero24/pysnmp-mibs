_AC='tnRoeRawStatsPortId'
_AB='tnRoeDeMapperRawCountStatsPortId'
_AA='tnRoeMapperRawCountStatsPortId'
_A9='tnMMACStatsBin'
_A8='tnMMACStatsInterval'
_A7='tnMMACStatsPortId'
_A6='tnPMACStatsBin'
_A5='tnPMACStatsInterval'
_A4='tnPMACStatsPortId'
_A3='tnEMACStatsBin'
_A2='tnEMACStatsInterval'
_A1='tnEMACStatsPortId'
_A0='tnRoeDeMapperStatsBin'
_z='tnRoeDeMapperStatsInterval'
_y='tnRoeDeMapperStatsDeMapperID'
_x='tnRoeDeMapperStatsPortId'
_w='tnRoeMapperStatsBin'
_v='tnRoeMapperStatsInterval'
_u='tnRoeMapperStatsMapperID'
_t='tnRoeMapperStatsPortId'
_s='tnRoeStatsBin'
_r='tnRoeStatsInterval'
_q='tnRoeStatsPortId'
_p='tnPktWanifRawCountStatsPortId'
_o='tnPktWanifStatsBin'
_n='tnPktWanifStatsInterval'
_m='tnPktWanifStatsPortId'
_l='tnEthCfmTWLmStatsBin'
_k='tnEthCfmTWLmStatsInterval'
_j='tnEthCfmTWLmStatsTestName'
_i='tnEthCfmTWDmStatsBin'
_h='tnEthCfmTWDmStatsInterval'
_g='tnEthCfmTWDmStatsTestName'
_f='tnEthCfmTWSlmStatsBin'
_e='tnEthCfmTWSlmStatsInterval'
_d='tnEthCfmTWSlmStatsTestName'
_c='tnSapStatsMeterId'
_b='tnEthPortStatsQueueId'
_a='tnPmonTcaId'
_Z='tnPmonTcaSubgroup'
_Y='tnPmonTcaInterval'
_X='AluWdmStatsBinNumber'
_W='AluWdmStatsIntervalType'
_V='tnPmonClearType'
_U='TQueueId'
_T='TItemDescription'
_S='SnmpAdminString'
_R='tnSapStatsBin'
_Q='tnSapStatsInterval'
_P='tnSapStatsEncapVal'
_O='tnSapStatsPortId'
_N='tnEthPortStatsBin'
_M='tnEthPortStatsInterval'
_L='tnEthPortStatsPortId'
_K='tnPmonPolicyId'
_J='tnPmonPolicyType'
_I='read-write'
_H='tnSysSwitchId'
_G='TROPIC-SYSTEM-MIB'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='TN-PMON-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_S)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
TSapIngQueueId,=mibBuilder.importSymbols('TN-SERV-MIB','TSapIngQueueId')
TItemDescription,TQueueId,TmnxEncapVal,TmnxPortID=mibBuilder.importSymbols('TN-TC-MIB',_T,_U,'TmnxEncapVal','TmnxPortID')
tnSRMIBModules,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_G,_H)
TnCommand,=mibBuilder.importSymbols('TROPIC-TC','TnCommand')
tnPmonMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,99))
if mibBuilder.loadTexts:tnPmonMIBModule.setRevisions(('2021-06-04 00:00','2020-03-13 00:00','2019-11-22 00:00','2019-04-28 00:00','2019-04-22 00:00','2019-02-07 00:00','2018-11-09 00:00','2018-10-26 00:00','2018-10-12 00:00','2018-02-23 00:00','2015-02-17 00:00','2013-07-29 00:00','2013-05-20 00:00','2013-03-26 00:00','2012-11-13 00:00'))
class AluWdmPmonPolicyType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,20)));namedValues=NamedValues(*(('port',1),('sap',2),('eth-cfm-two-way-slm',3),('eth-cfm-two-way-dm',4),('eth-cfm-two-way-lm',5),('roe',20)))
class AluWdmStatsIntervalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2))
class AluWdmStatsBinNumber(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,32))
class AluWdmStatsBinStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('valid',1),('rxValid',2),('txValid',3),('invalid',4),('dataNotAvailable',5),('partial',6),('adjusted',7),('dataLong',8),('dataComplete',9)))
class AluWdmPmonStatsClearType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('port',1),('sap',2),('eth-cfm-oam-test',3),('roe',4),('roe-mapper',5),('roe-demapper',6),('emac',7),('pmac',8),('mmac',9)))
_TnPmonObjs_ObjectIdentity=ObjectIdentity
tnPmonObjs=_TnPmonObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,99))
_TnPmonPolicyAttributeTotal_Type=Integer32
_TnPmonPolicyAttributeTotal_Object=MibScalar
tnPmonPolicyAttributeTotal=_TnPmonPolicyAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,1),_TnPmonPolicyAttributeTotal_Type())
tnPmonPolicyAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPmonPolicyAttributeTotal.setStatus(_A)
_TnPmonPolicyTable_Object=MibTable
tnPmonPolicyTable=_TnPmonPolicyTable_Object((1,3,6,1,4,1,7483,6,1,2,99,2))
if mibBuilder.loadTexts:tnPmonPolicyTable.setStatus(_A)
_TnPmonPolicyEntry_Object=MibTableRow
tnPmonPolicyEntry=_TnPmonPolicyEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1))
tnPmonPolicyEntry.setIndexNames((0,_G,_H),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:tnPmonPolicyEntry.setStatus(_A)
_TnPmonPolicyType_Type=AluWdmPmonPolicyType
_TnPmonPolicyType_Object=MibTableColumn
tnPmonPolicyType=_TnPmonPolicyType_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,1),_TnPmonPolicyType_Type())
tnPmonPolicyType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPmonPolicyType.setStatus(_A)
class _TnPmonPolicyId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TnPmonPolicyId_Type.__name__=_E
_TnPmonPolicyId_Object=MibTableColumn
tnPmonPolicyId=_TnPmonPolicyId_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,2),_TnPmonPolicyId_Type())
tnPmonPolicyId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPmonPolicyId.setStatus(_A)
_TnPmonPolicyRowStatus_Type=RowStatus
_TnPmonPolicyRowStatus_Object=MibTableColumn
tnPmonPolicyRowStatus=_TnPmonPolicyRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,3),_TnPmonPolicyRowStatus_Type())
tnPmonPolicyRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyRowStatus.setStatus(_A)
class _TnPmonPolicyDescription_Type(TItemDescription):defaultHexValue=''
_TnPmonPolicyDescription_Type.__name__=_T
_TnPmonPolicyDescription_Object=MibTableColumn
tnPmonPolicyDescription=_TnPmonPolicyDescription_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,4),_TnPmonPolicyDescription_Type())
tnPmonPolicyDescription.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyDescription.setStatus(_A)
class _TnPmonPolicyNumOfBins15Min_Type(Integer32):defaultValue=33;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_TnPmonPolicyNumOfBins15Min_Type.__name__=_E
_TnPmonPolicyNumOfBins15Min_Object=MibTableColumn
tnPmonPolicyNumOfBins15Min=_TnPmonPolicyNumOfBins15Min_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,5),_TnPmonPolicyNumOfBins15Min_Type())
tnPmonPolicyNumOfBins15Min.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyNumOfBins15Min.setStatus(_A)
class _TnPmonPolicyNumOfBins1Day_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TnPmonPolicyNumOfBins1Day_Type.__name__=_E
_TnPmonPolicyNumOfBins1Day_Object=MibTableColumn
tnPmonPolicyNumOfBins1Day=_TnPmonPolicyNumOfBins1Day_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,6),_TnPmonPolicyNumOfBins1Day_Type())
tnPmonPolicyNumOfBins1Day.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyNumOfBins1Day.setStatus(_A)
class _TnPmonPolicyFlrInterval15Min_Type(Integer32):defaultValue=1
_TnPmonPolicyFlrInterval15Min_Type.__name__=_E
_TnPmonPolicyFlrInterval15Min_Object=MibTableColumn
tnPmonPolicyFlrInterval15Min=_TnPmonPolicyFlrInterval15Min_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,7),_TnPmonPolicyFlrInterval15Min_Type())
tnPmonPolicyFlrInterval15Min.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyFlrInterval15Min.setStatus(_A)
class _TnPmonPolicyFlrInterval1Day_Type(Integer32):defaultValue=60
_TnPmonPolicyFlrInterval1Day_Type.__name__=_E
_TnPmonPolicyFlrInterval1Day_Object=MibTableColumn
tnPmonPolicyFlrInterval1Day=_TnPmonPolicyFlrInterval1Day_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,8),_TnPmonPolicyFlrInterval1Day_Type())
tnPmonPolicyFlrInterval1Day.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyFlrInterval1Day.setStatus(_A)
class _TnPmonPolicyFlrAvailabilityInterval15Min_Type(Integer32):defaultValue=10
_TnPmonPolicyFlrAvailabilityInterval15Min_Type.__name__=_E
_TnPmonPolicyFlrAvailabilityInterval15Min_Object=MibTableColumn
tnPmonPolicyFlrAvailabilityInterval15Min=_TnPmonPolicyFlrAvailabilityInterval15Min_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,9),_TnPmonPolicyFlrAvailabilityInterval15Min_Type())
tnPmonPolicyFlrAvailabilityInterval15Min.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyFlrAvailabilityInterval15Min.setStatus(_A)
class _TnPmonPolicyFlrAvailabilityInterval1Day_Type(Integer32):defaultValue=10
_TnPmonPolicyFlrAvailabilityInterval1Day_Type.__name__=_E
_TnPmonPolicyFlrAvailabilityInterval1Day_Object=MibTableColumn
tnPmonPolicyFlrAvailabilityInterval1Day=_TnPmonPolicyFlrAvailabilityInterval1Day_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,10),_TnPmonPolicyFlrAvailabilityInterval1Day_Type())
tnPmonPolicyFlrAvailabilityInterval1Day.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyFlrAvailabilityInterval1Day.setStatus(_A)
class _TnPmonPolicyNumOfBinsContinuous_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_TnPmonPolicyNumOfBinsContinuous_Type.__name__=_E
_TnPmonPolicyNumOfBinsContinuous_Object=MibTableColumn
tnPmonPolicyNumOfBinsContinuous=_TnPmonPolicyNumOfBinsContinuous_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,11),_TnPmonPolicyNumOfBinsContinuous_Type())
tnPmonPolicyNumOfBinsContinuous.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyNumOfBinsContinuous.setStatus(_A)
class _TnPmonPolicyAvailFlrThreshold_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TnPmonPolicyAvailFlrThreshold_Type.__name__=_E
_TnPmonPolicyAvailFlrThreshold_Object=MibTableColumn
tnPmonPolicyAvailFlrThreshold=_TnPmonPolicyAvailFlrThreshold_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,12),_TnPmonPolicyAvailFlrThreshold_Type())
tnPmonPolicyAvailFlrThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyAvailFlrThreshold.setStatus(_A)
class _TnPmonPolicyAvailFlrNumOfIntervals_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TnPmonPolicyAvailFlrNumOfIntervals_Type.__name__=_E
_TnPmonPolicyAvailFlrNumOfIntervals_Object=MibTableColumn
tnPmonPolicyAvailFlrNumOfIntervals=_TnPmonPolicyAvailFlrNumOfIntervals_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,13),_TnPmonPolicyAvailFlrNumOfIntervals_Type())
tnPmonPolicyAvailFlrNumOfIntervals.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyAvailFlrNumOfIntervals.setStatus(_A)
class _TnPmonPolicyFramesPerDeltaT_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_TnPmonPolicyFramesPerDeltaT_Type.__name__=_E
_TnPmonPolicyFramesPerDeltaT_Object=MibTableColumn
tnPmonPolicyFramesPerDeltaT=_TnPmonPolicyFramesPerDeltaT_Object((1,3,6,1,4,1,7483,6,1,2,99,2,1,14),_TnPmonPolicyFramesPerDeltaT_Type())
tnPmonPolicyFramesPerDeltaT.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonPolicyFramesPerDeltaT.setStatus(_A)
_TnPmonClearAttributeTotal_Type=Integer32
_TnPmonClearAttributeTotal_Object=MibScalar
tnPmonClearAttributeTotal=_TnPmonClearAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,3),_TnPmonClearAttributeTotal_Type())
tnPmonClearAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPmonClearAttributeTotal.setStatus(_A)
_TnPmonClearTable_Object=MibTable
tnPmonClearTable=_TnPmonClearTable_Object((1,3,6,1,4,1,7483,6,1,2,99,4))
if mibBuilder.loadTexts:tnPmonClearTable.setStatus(_A)
_TnPmonClearEntry_Object=MibTableRow
tnPmonClearEntry=_TnPmonClearEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1))
tnPmonClearEntry.setIndexNames((0,_G,_H),(0,_C,_V))
if mibBuilder.loadTexts:tnPmonClearEntry.setStatus(_A)
_TnPmonClearType_Type=AluWdmPmonStatsClearType
_TnPmonClearType_Object=MibTableColumn
tnPmonClearType=_TnPmonClearType_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,1),_TnPmonClearType_Type())
tnPmonClearType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPmonClearType.setStatus(_A)
_TnPmonClearPortId_Type=TmnxPortID
_TnPmonClearPortId_Object=MibTableColumn
tnPmonClearPortId=_TnPmonClearPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,2),_TnPmonClearPortId_Type())
tnPmonClearPortId.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPmonClearPortId.setStatus(_A)
_TnPmonClearEncapValue_Type=TmnxEncapVal
_TnPmonClearEncapValue_Object=MibTableColumn
tnPmonClearEncapValue=_TnPmonClearEncapValue_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,3),_TnPmonClearEncapValue_Type())
tnPmonClearEncapValue.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPmonClearEncapValue.setStatus(_A)
_TnPmonClearTestName_Type=SnmpAdminString
_TnPmonClearTestName_Object=MibTableColumn
tnPmonClearTestName=_TnPmonClearTestName_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,4),_TnPmonClearTestName_Type())
tnPmonClearTestName.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPmonClearTestName.setStatus(_A)
class _TnPmonClearInterval_Type(AluWdmStatsIntervalType):defaultValue=-1
_TnPmonClearInterval_Type.__name__=_W
_TnPmonClearInterval_Object=MibTableColumn
tnPmonClearInterval=_TnPmonClearInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,5),_TnPmonClearInterval_Type())
tnPmonClearInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPmonClearInterval.setStatus(_A)
class _TnPmonClearBin_Type(AluWdmStatsBinNumber):defaultValue=-1
_TnPmonClearBin_Type.__name__=_X
_TnPmonClearBin_Object=MibTableColumn
tnPmonClearBin=_TnPmonClearBin_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,6),_TnPmonClearBin_Type())
tnPmonClearBin.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPmonClearBin.setStatus(_A)
class _TnPmonClearRoeMapperId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_TnPmonClearRoeMapperId_Type.__name__=_E
_TnPmonClearRoeMapperId_Object=MibTableColumn
tnPmonClearRoeMapperId=_TnPmonClearRoeMapperId_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,7),_TnPmonClearRoeMapperId_Type())
tnPmonClearRoeMapperId.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPmonClearRoeMapperId.setStatus(_A)
class _TnPmonClearRoeDeMapperId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,80))
_TnPmonClearRoeDeMapperId_Type.__name__=_E
_TnPmonClearRoeDeMapperId_Object=MibTableColumn
tnPmonClearRoeDeMapperId=_TnPmonClearRoeDeMapperId_Object((1,3,6,1,4,1,7483,6,1,2,99,4,1,8),_TnPmonClearRoeDeMapperId_Type())
tnPmonClearRoeDeMapperId.setMaxAccess(_I)
if mibBuilder.loadTexts:tnPmonClearRoeDeMapperId.setStatus(_A)
_TnPmonTcaAttributeTotal_Type=Integer32
_TnPmonTcaAttributeTotal_Object=MibScalar
tnPmonTcaAttributeTotal=_TnPmonTcaAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,5),_TnPmonTcaAttributeTotal_Type())
tnPmonTcaAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPmonTcaAttributeTotal.setStatus(_A)
_TnPmonTcaTable_Object=MibTable
tnPmonTcaTable=_TnPmonTcaTable_Object((1,3,6,1,4,1,7483,6,1,2,99,6))
if mibBuilder.loadTexts:tnPmonTcaTable.setStatus(_A)
_TnPmonTcaEntry_Object=MibTableRow
tnPmonTcaEntry=_TnPmonTcaEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,6,1))
tnPmonTcaEntry.setIndexNames((0,_G,_H),(0,_C,_J),(0,_C,_K),(0,_C,_Y),(0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:tnPmonTcaEntry.setStatus(_A)
_TnPmonTcaInterval_Type=AluWdmStatsIntervalType
_TnPmonTcaInterval_Object=MibTableColumn
tnPmonTcaInterval=_TnPmonTcaInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,6,1,1),_TnPmonTcaInterval_Type())
tnPmonTcaInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPmonTcaInterval.setStatus(_A)
_TnPmonTcaSubgroup_Type=Integer32
_TnPmonTcaSubgroup_Object=MibTableColumn
tnPmonTcaSubgroup=_TnPmonTcaSubgroup_Object((1,3,6,1,4,1,7483,6,1,2,99,6,1,2),_TnPmonTcaSubgroup_Type())
tnPmonTcaSubgroup.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPmonTcaSubgroup.setStatus(_A)
_TnPmonTcaId_Type=Integer32
_TnPmonTcaId_Object=MibTableColumn
tnPmonTcaId=_TnPmonTcaId_Object((1,3,6,1,4,1,7483,6,1,2,99,6,1,3),_TnPmonTcaId_Type())
tnPmonTcaId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPmonTcaId.setStatus(_A)
_TnPmonTcaVariable_Type=ObjectIdentifier
_TnPmonTcaVariable_Object=MibTableColumn
tnPmonTcaVariable=_TnPmonTcaVariable_Object((1,3,6,1,4,1,7483,6,1,2,99,6,1,4),_TnPmonTcaVariable_Type())
tnPmonTcaVariable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPmonTcaVariable.setStatus(_A)
class _TnPmonTcaValue_Type(SnmpAdminString):defaultHexValue='00';subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_TnPmonTcaValue_Type.__name__=_S
_TnPmonTcaValue_Object=MibTableColumn
tnPmonTcaValue=_TnPmonTcaValue_Object((1,3,6,1,4,1,7483,6,1,2,99,6,1,5),_TnPmonTcaValue_Type())
tnPmonTcaValue.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPmonTcaValue.setStatus(_A)
_TnEthPortStatsAttributeTotal_Type=Integer32
_TnEthPortStatsAttributeTotal_Object=MibScalar
tnEthPortStatsAttributeTotal=_TnEthPortStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,7),_TnEthPortStatsAttributeTotal_Type())
tnEthPortStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsAttributeTotal.setStatus(_A)
_TnEthPortStatsTable_Object=MibTable
tnEthPortStatsTable=_TnEthPortStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,8))
if mibBuilder.loadTexts:tnEthPortStatsTable.setStatus(_A)
_TnEthPortStatsEntry_Object=MibTableRow
tnEthPortStatsEntry=_TnEthPortStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1))
tnEthPortStatsEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:tnEthPortStatsEntry.setStatus(_A)
_TnEthPortStatsPortId_Type=TmnxPortID
_TnEthPortStatsPortId_Object=MibTableColumn
tnEthPortStatsPortId=_TnEthPortStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,1),_TnEthPortStatsPortId_Type())
tnEthPortStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthPortStatsPortId.setStatus(_A)
_TnEthPortStatsInterval_Type=AluWdmStatsIntervalType
_TnEthPortStatsInterval_Object=MibTableColumn
tnEthPortStatsInterval=_TnEthPortStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,2),_TnEthPortStatsInterval_Type())
tnEthPortStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthPortStatsInterval.setStatus(_A)
_TnEthPortStatsBin_Type=AluWdmStatsBinNumber
_TnEthPortStatsBin_Object=MibTableColumn
tnEthPortStatsBin=_TnEthPortStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,3),_TnEthPortStatsBin_Type())
tnEthPortStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthPortStatsBin.setStatus(_A)
_TnEthPortStatsBinStatus_Type=AluWdmStatsBinStatus
_TnEthPortStatsBinStatus_Object=MibTableColumn
tnEthPortStatsBinStatus=_TnEthPortStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,4),_TnEthPortStatsBinStatus_Type())
tnEthPortStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsBinStatus.setStatus(_A)
_TnEthPortStatsStartTime_Type=DateAndTime
_TnEthPortStatsStartTime_Object=MibTableColumn
tnEthPortStatsStartTime=_TnEthPortStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,5),_TnEthPortStatsStartTime_Type())
tnEthPortStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsStartTime.setStatus(_A)
_TnEthPortStatsTotalMembers_Type=Integer32
_TnEthPortStatsTotalMembers_Object=MibTableColumn
tnEthPortStatsTotalMembers=_TnEthPortStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,6),_TnEthPortStatsTotalMembers_Type())
tnEthPortStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsTotalMembers.setStatus(_A)
_TnEthPortStatsIfInOctets_Type=Counter64
_TnEthPortStatsIfInOctets_Object=MibTableColumn
tnEthPortStatsIfInOctets=_TnEthPortStatsIfInOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,7),_TnEthPortStatsIfInOctets_Type())
tnEthPortStatsIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInOctets.setStatus(_A)
_TnEthPortStatsIfInUcastPkts_Type=Counter64
_TnEthPortStatsIfInUcastPkts_Object=MibTableColumn
tnEthPortStatsIfInUcastPkts=_TnEthPortStatsIfInUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,8),_TnEthPortStatsIfInUcastPkts_Type())
tnEthPortStatsIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInUcastPkts.setStatus(_A)
_TnEthPortStatsIfInDiscards_Type=Counter64
_TnEthPortStatsIfInDiscards_Object=MibTableColumn
tnEthPortStatsIfInDiscards=_TnEthPortStatsIfInDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,9),_TnEthPortStatsIfInDiscards_Type())
tnEthPortStatsIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInDiscards.setStatus(_A)
_TnEthPortStatsIfInErrors_Type=Counter64
_TnEthPortStatsIfInErrors_Object=MibTableColumn
tnEthPortStatsIfInErrors=_TnEthPortStatsIfInErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,10),_TnEthPortStatsIfInErrors_Type())
tnEthPortStatsIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInErrors.setStatus(_A)
_TnEthPortStatsIfInUnknownProtos_Type=Counter64
_TnEthPortStatsIfInUnknownProtos_Object=MibTableColumn
tnEthPortStatsIfInUnknownProtos=_TnEthPortStatsIfInUnknownProtos_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,11),_TnEthPortStatsIfInUnknownProtos_Type())
tnEthPortStatsIfInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInUnknownProtos.setStatus(_A)
_TnEthPortStatsIfInMulticastPkts_Type=Counter64
_TnEthPortStatsIfInMulticastPkts_Object=MibTableColumn
tnEthPortStatsIfInMulticastPkts=_TnEthPortStatsIfInMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,12),_TnEthPortStatsIfInMulticastPkts_Type())
tnEthPortStatsIfInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInMulticastPkts.setStatus(_A)
_TnEthPortStatsIfInBroadcastPkts_Type=Counter64
_TnEthPortStatsIfInBroadcastPkts_Object=MibTableColumn
tnEthPortStatsIfInBroadcastPkts=_TnEthPortStatsIfInBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,13),_TnEthPortStatsIfInBroadcastPkts_Type())
tnEthPortStatsIfInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInBroadcastPkts.setStatus(_A)
_TnEthPortStatsIfOutOctets_Type=Counter64
_TnEthPortStatsIfOutOctets_Object=MibTableColumn
tnEthPortStatsIfOutOctets=_TnEthPortStatsIfOutOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,14),_TnEthPortStatsIfOutOctets_Type())
tnEthPortStatsIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfOutOctets.setStatus(_A)
_TnEthPortStatsIfOutUcastPkts_Type=Counter64
_TnEthPortStatsIfOutUcastPkts_Object=MibTableColumn
tnEthPortStatsIfOutUcastPkts=_TnEthPortStatsIfOutUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,15),_TnEthPortStatsIfOutUcastPkts_Type())
tnEthPortStatsIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfOutUcastPkts.setStatus(_A)
_TnEthPortStatsIfOutDiscards_Type=Counter64
_TnEthPortStatsIfOutDiscards_Object=MibTableColumn
tnEthPortStatsIfOutDiscards=_TnEthPortStatsIfOutDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,16),_TnEthPortStatsIfOutDiscards_Type())
tnEthPortStatsIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfOutDiscards.setStatus(_A)
_TnEthPortStatsIfOutErrors_Type=Counter64
_TnEthPortStatsIfOutErrors_Object=MibTableColumn
tnEthPortStatsIfOutErrors=_TnEthPortStatsIfOutErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,17),_TnEthPortStatsIfOutErrors_Type())
tnEthPortStatsIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfOutErrors.setStatus(_A)
_TnEthPortStatsIfOutMulticastPkts_Type=Counter64
_TnEthPortStatsIfOutMulticastPkts_Object=MibTableColumn
tnEthPortStatsIfOutMulticastPkts=_TnEthPortStatsIfOutMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,18),_TnEthPortStatsIfOutMulticastPkts_Type())
tnEthPortStatsIfOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfOutMulticastPkts.setStatus(_A)
_TnEthPortStatsIfOutBroadcastPkts_Type=Counter64
_TnEthPortStatsIfOutBroadcastPkts_Object=MibTableColumn
tnEthPortStatsIfOutBroadcastPkts=_TnEthPortStatsIfOutBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,19),_TnEthPortStatsIfOutBroadcastPkts_Type())
tnEthPortStatsIfOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfOutBroadcastPkts.setStatus(_A)
_TnEthPortStatsIfInPkts_Type=Counter64
_TnEthPortStatsIfInPkts_Object=MibTableColumn
tnEthPortStatsIfInPkts=_TnEthPortStatsIfInPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,20),_TnEthPortStatsIfInPkts_Type())
tnEthPortStatsIfInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfInPkts.setStatus(_A)
_TnEthPortStatsIfOutPkts_Type=Counter64
_TnEthPortStatsIfOutPkts_Object=MibTableColumn
tnEthPortStatsIfOutPkts=_TnEthPortStatsIfOutPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,21),_TnEthPortStatsIfOutPkts_Type())
tnEthPortStatsIfOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortStatsIfOutPkts.setStatus(_A)
_TnEthPortEtherStatsDropEvents_Type=Counter64
_TnEthPortEtherStatsDropEvents_Object=MibTableColumn
tnEthPortEtherStatsDropEvents=_TnEthPortEtherStatsDropEvents_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,22),_TnEthPortEtherStatsDropEvents_Type())
tnEthPortEtherStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsDropEvents.setStatus(_A)
_TnEthPortEtherStatsBroadcastPkts_Type=Counter64
_TnEthPortEtherStatsBroadcastPkts_Object=MibTableColumn
tnEthPortEtherStatsBroadcastPkts=_TnEthPortEtherStatsBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,23),_TnEthPortEtherStatsBroadcastPkts_Type())
tnEthPortEtherStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsBroadcastPkts.setStatus(_A)
_TnEthPortEtherStatsMulticastPkts_Type=Counter64
_TnEthPortEtherStatsMulticastPkts_Object=MibTableColumn
tnEthPortEtherStatsMulticastPkts=_TnEthPortEtherStatsMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,24),_TnEthPortEtherStatsMulticastPkts_Type())
tnEthPortEtherStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsMulticastPkts.setStatus(_A)
_TnEthPortEtherStatsCRCAlignErrors_Type=Counter64
_TnEthPortEtherStatsCRCAlignErrors_Object=MibTableColumn
tnEthPortEtherStatsCRCAlignErrors=_TnEthPortEtherStatsCRCAlignErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,25),_TnEthPortEtherStatsCRCAlignErrors_Type())
tnEthPortEtherStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsCRCAlignErrors.setStatus(_A)
_TnEthPortEtherStatsUndersizePkts_Type=Counter64
_TnEthPortEtherStatsUndersizePkts_Object=MibTableColumn
tnEthPortEtherStatsUndersizePkts=_TnEthPortEtherStatsUndersizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,26),_TnEthPortEtherStatsUndersizePkts_Type())
tnEthPortEtherStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsUndersizePkts.setStatus(_A)
_TnEthPortEtherStatsOversizePkts_Type=Counter64
_TnEthPortEtherStatsOversizePkts_Object=MibTableColumn
tnEthPortEtherStatsOversizePkts=_TnEthPortEtherStatsOversizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,27),_TnEthPortEtherStatsOversizePkts_Type())
tnEthPortEtherStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsOversizePkts.setStatus(_A)
_TnEthPortEtherStatsFragments_Type=Counter64
_TnEthPortEtherStatsFragments_Object=MibTableColumn
tnEthPortEtherStatsFragments=_TnEthPortEtherStatsFragments_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,28),_TnEthPortEtherStatsFragments_Type())
tnEthPortEtherStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsFragments.setStatus(_A)
_TnEthPortEtherStatsJabbers_Type=Counter64
_TnEthPortEtherStatsJabbers_Object=MibTableColumn
tnEthPortEtherStatsJabbers=_TnEthPortEtherStatsJabbers_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,29),_TnEthPortEtherStatsJabbers_Type())
tnEthPortEtherStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsJabbers.setStatus(_A)
_TnEthPortEtherStatsCollisions_Type=Counter64
_TnEthPortEtherStatsCollisions_Object=MibTableColumn
tnEthPortEtherStatsCollisions=_TnEthPortEtherStatsCollisions_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,30),_TnEthPortEtherStatsCollisions_Type())
tnEthPortEtherStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsCollisions.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts=_TnEthPortEtherStatsHighCapacityPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,31),_TnEthPortEtherStatsHighCapacityPkts_Type())
tnEthPortEtherStatsHighCapacityPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts.setStatus(_A)
_TnEthPortEtherStatsHighCapacityOctets_Type=Counter64
_TnEthPortEtherStatsHighCapacityOctets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityOctets=_TnEthPortEtherStatsHighCapacityOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,32),_TnEthPortEtherStatsHighCapacityOctets_Type())
tnEthPortEtherStatsHighCapacityOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityOctets.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts64Octets_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts64Octets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts64Octets=_TnEthPortEtherStatsHighCapacityPkts64Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,33),_TnEthPortEtherStatsHighCapacityPkts64Octets_Type())
tnEthPortEtherStatsHighCapacityPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts64Octets.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts65to127Octets=_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,34),_TnEthPortEtherStatsHighCapacityPkts65to127Octets_Type())
tnEthPortEtherStatsHighCapacityPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts65to127Octets.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts128to255Octets=_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,35),_TnEthPortEtherStatsHighCapacityPkts128to255Octets_Type())
tnEthPortEtherStatsHighCapacityPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts128to255Octets.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts256to511Octets=_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,36),_TnEthPortEtherStatsHighCapacityPkts256to511Octets_Type())
tnEthPortEtherStatsHighCapacityPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts256to511Octets.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts512to1023Octets=_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,37),_TnEthPortEtherStatsHighCapacityPkts512to1023Octets_Type())
tnEthPortEtherStatsHighCapacityPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts512to1023Octets.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts1024to1518Octets=_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,38),_TnEthPortEtherStatsHighCapacityPkts1024to1518Octets_Type())
tnEthPortEtherStatsHighCapacityPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts1024to1518Octets.setStatus(_A)
_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Type=Counter64
_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Object=MibTableColumn
tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets=_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,8,1,39),_TnEthPortEtherStatsHighCapacityPkts1519toMaxOctets_Type())
tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets.setStatus(_A)
_TnEthPortEgrQueueStatsAttributeTotal_Type=Integer32
_TnEthPortEgrQueueStatsAttributeTotal_Object=MibScalar
tnEthPortEgrQueueStatsAttributeTotal=_TnEthPortEgrQueueStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,9),_TnEthPortEgrQueueStatsAttributeTotal_Type())
tnEthPortEgrQueueStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsAttributeTotal.setStatus(_A)
_TnEthPortEgrQueueStatsTable_Object=MibTable
tnEthPortEgrQueueStatsTable=_TnEthPortEgrQueueStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,10))
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsTable.setStatus(_A)
_TnEthPortEgrQueueStatsEntry_Object=MibTableRow
tnEthPortEgrQueueStatsEntry=_TnEthPortEgrQueueStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1))
tnEthPortEgrQueueStatsEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N),(0,_C,_b))
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsEntry.setStatus(_A)
class _TnEthPortStatsQueueId_Type(TQueueId):subtypeSpec=TQueueId.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_TnEthPortStatsQueueId_Type.__name__=_U
_TnEthPortStatsQueueId_Object=MibTableColumn
tnEthPortStatsQueueId=_TnEthPortStatsQueueId_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,1),_TnEthPortStatsQueueId_Type())
tnEthPortStatsQueueId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthPortStatsQueueId.setStatus(_A)
_TnEthPortEgrQueueStatsInProfilePktsForwarded_Type=Counter64
_TnEthPortEgrQueueStatsInProfilePktsForwarded_Object=MibTableColumn
tnEthPortEgrQueueStatsInProfilePktsForwarded=_TnEthPortEgrQueueStatsInProfilePktsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,2),_TnEthPortEgrQueueStatsInProfilePktsForwarded_Type())
tnEthPortEgrQueueStatsInProfilePktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsInProfilePktsForwarded.setStatus(_A)
_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Type=Counter64
_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Object=MibTableColumn
tnEthPortEgrQueueStatsOutOfProfilePktsForwarded=_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,3),_TnEthPortEgrQueueStatsOutOfProfilePktsForwarded_Type())
tnEthPortEgrQueueStatsOutOfProfilePktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsOutOfProfilePktsForwarded.setStatus(_A)
_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Type=Counter64
_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Object=MibTableColumn
tnEthPortEgrQueueStatsInProfileOctetsForwarded=_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,4),_TnEthPortEgrQueueStatsInProfileOctetsForwarded_Type())
tnEthPortEgrQueueStatsInProfileOctetsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsInProfileOctetsForwarded.setStatus(_A)
_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Type=Counter64
_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Object=MibTableColumn
tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded=_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,5),_TnEthPortEgrQueueStatsOutOfProfileOctetsForwarded_Type())
tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded.setStatus(_A)
_TnEthPortEgrQueueStatsInProfilePktsDropped_Type=Counter64
_TnEthPortEgrQueueStatsInProfilePktsDropped_Object=MibTableColumn
tnEthPortEgrQueueStatsInProfilePktsDropped=_TnEthPortEgrQueueStatsInProfilePktsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,6),_TnEthPortEgrQueueStatsInProfilePktsDropped_Type())
tnEthPortEgrQueueStatsInProfilePktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsInProfilePktsDropped.setStatus(_A)
_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Type=Counter64
_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Object=MibTableColumn
tnEthPortEgrQueueStatsOutOfProfilePktsDropped=_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,7),_TnEthPortEgrQueueStatsOutOfProfilePktsDropped_Type())
tnEthPortEgrQueueStatsOutOfProfilePktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsOutOfProfilePktsDropped.setStatus(_A)
_TnEthPortEgrQueueStatsInProfileOctetsDropped_Type=Counter64
_TnEthPortEgrQueueStatsInProfileOctetsDropped_Object=MibTableColumn
tnEthPortEgrQueueStatsInProfileOctetsDropped=_TnEthPortEgrQueueStatsInProfileOctetsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,8),_TnEthPortEgrQueueStatsInProfileOctetsDropped_Type())
tnEthPortEgrQueueStatsInProfileOctetsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsInProfileOctetsDropped.setStatus(_A)
_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Type=Counter64
_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Object=MibTableColumn
tnEthPortEgrQueueStatsOutOfProfileOctetsDropped=_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,10,1,9),_TnEthPortEgrQueueStatsOutOfProfileOctetsDropped_Type())
tnEthPortEgrQueueStatsOutOfProfileOctetsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthPortEgrQueueStatsOutOfProfileOctetsDropped.setStatus(_A)
_TnSapStatsAttributeTotal_Type=Integer32
_TnSapStatsAttributeTotal_Object=MibScalar
tnSapStatsAttributeTotal=_TnSapStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,11),_TnSapStatsAttributeTotal_Type())
tnSapStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsAttributeTotal.setStatus(_A)
_TnSapStatsTable_Object=MibTable
tnSapStatsTable=_TnSapStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,12))
if mibBuilder.loadTexts:tnSapStatsTable.setStatus(_A)
_TnSapStatsEntry_Object=MibTableRow
tnSapStatsEntry=_TnSapStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1))
tnSapStatsEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:tnSapStatsEntry.setStatus(_A)
_TnSapStatsPortId_Type=TmnxPortID
_TnSapStatsPortId_Object=MibTableColumn
tnSapStatsPortId=_TnSapStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,1),_TnSapStatsPortId_Type())
tnSapStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapStatsPortId.setStatus(_A)
_TnSapStatsEncapVal_Type=TmnxEncapVal
_TnSapStatsEncapVal_Object=MibTableColumn
tnSapStatsEncapVal=_TnSapStatsEncapVal_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,2),_TnSapStatsEncapVal_Type())
tnSapStatsEncapVal.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapStatsEncapVal.setStatus(_A)
_TnSapStatsInterval_Type=AluWdmStatsIntervalType
_TnSapStatsInterval_Object=MibTableColumn
tnSapStatsInterval=_TnSapStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,3),_TnSapStatsInterval_Type())
tnSapStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapStatsInterval.setStatus(_A)
_TnSapStatsBin_Type=AluWdmStatsBinNumber
_TnSapStatsBin_Object=MibTableColumn
tnSapStatsBin=_TnSapStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,4),_TnSapStatsBin_Type())
tnSapStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapStatsBin.setStatus(_A)
_TnSapStatsBinStatus_Type=AluWdmStatsBinStatus
_TnSapStatsBinStatus_Object=MibTableColumn
tnSapStatsBinStatus=_TnSapStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,5),_TnSapStatsBinStatus_Type())
tnSapStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsBinStatus.setStatus(_A)
_TnSapStatsStartTime_Type=DateAndTime
_TnSapStatsStartTime_Object=MibTableColumn
tnSapStatsStartTime=_TnSapStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,6),_TnSapStatsStartTime_Type())
tnSapStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsStartTime.setStatus(_A)
_TnSapStatsTotalMembers_Type=Integer32
_TnSapStatsTotalMembers_Object=MibTableColumn
tnSapStatsTotalMembers=_TnSapStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,7),_TnSapStatsTotalMembers_Type())
tnSapStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsTotalMembers.setStatus(_A)
_TnSapStatsIngressPktsForwarded_Type=Counter64
_TnSapStatsIngressPktsForwarded_Object=MibTableColumn
tnSapStatsIngressPktsForwarded=_TnSapStatsIngressPktsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,8),_TnSapStatsIngressPktsForwarded_Type())
tnSapStatsIngressPktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsIngressPktsForwarded.setStatus(_A)
_TnSapStatsIngressOctetsForwarded_Type=Counter64
_TnSapStatsIngressOctetsForwarded_Object=MibTableColumn
tnSapStatsIngressOctetsForwarded=_TnSapStatsIngressOctetsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,9),_TnSapStatsIngressOctetsForwarded_Type())
tnSapStatsIngressOctetsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsIngressOctetsForwarded.setStatus(_A)
_TnSapStatsEgressPktsForwarded_Type=Counter64
_TnSapStatsEgressPktsForwarded_Object=MibTableColumn
tnSapStatsEgressPktsForwarded=_TnSapStatsEgressPktsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,10),_TnSapStatsEgressPktsForwarded_Type())
tnSapStatsEgressPktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsEgressPktsForwarded.setStatus(_A)
_TnSapStatsEgressOctetsForwarded_Type=Counter64
_TnSapStatsEgressOctetsForwarded_Object=MibTableColumn
tnSapStatsEgressOctetsForwarded=_TnSapStatsEgressOctetsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,11),_TnSapStatsEgressOctetsForwarded_Type())
tnSapStatsEgressOctetsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsEgressOctetsForwarded.setStatus(_A)
_TnSapStatsIngressPktsDropped_Type=Counter64
_TnSapStatsIngressPktsDropped_Object=MibTableColumn
tnSapStatsIngressPktsDropped=_TnSapStatsIngressPktsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,12),_TnSapStatsIngressPktsDropped_Type())
tnSapStatsIngressPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsIngressPktsDropped.setStatus(_A)
_TnSapStatsIngressOctetsDropped_Type=Counter64
_TnSapStatsIngressOctetsDropped_Object=MibTableColumn
tnSapStatsIngressOctetsDropped=_TnSapStatsIngressOctetsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,13),_TnSapStatsIngressOctetsDropped_Type())
tnSapStatsIngressOctetsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsIngressOctetsDropped.setStatus(_A)
_TnSapStatsIngressExtraTagPktsDropped_Type=Counter64
_TnSapStatsIngressExtraTagPktsDropped_Object=MibTableColumn
tnSapStatsIngressExtraTagPktsDropped=_TnSapStatsIngressExtraTagPktsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,14),_TnSapStatsIngressExtraTagPktsDropped_Type())
tnSapStatsIngressExtraTagPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsIngressExtraTagPktsDropped.setStatus(_A)
_TnSapStatsIngressExtraTagOctetsDropped_Type=Counter64
_TnSapStatsIngressExtraTagOctetsDropped_Object=MibTableColumn
tnSapStatsIngressExtraTagOctetsDropped=_TnSapStatsIngressExtraTagOctetsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,12,1,15),_TnSapStatsIngressExtraTagOctetsDropped_Type())
tnSapStatsIngressExtraTagOctetsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapStatsIngressExtraTagOctetsDropped.setStatus(_A)
_TnSapMeterStatsAttributeTotal_Type=Integer32
_TnSapMeterStatsAttributeTotal_Object=MibScalar
tnSapMeterStatsAttributeTotal=_TnSapMeterStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,13),_TnSapMeterStatsAttributeTotal_Type())
tnSapMeterStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapMeterStatsAttributeTotal.setStatus(_A)
_TnSapMeterStatsTable_Object=MibTable
tnSapMeterStatsTable=_TnSapMeterStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,14))
if mibBuilder.loadTexts:tnSapMeterStatsTable.setStatus(_A)
_TnSapMeterStatsEntry_Object=MibTableRow
tnSapMeterStatsEntry=_TnSapMeterStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,14,1))
tnSapMeterStatsEntry.setIndexNames((0,_C,_O),(0,_C,_P),(0,_C,_Q),(0,_C,_R),(0,_C,_c))
if mibBuilder.loadTexts:tnSapMeterStatsEntry.setStatus(_A)
_TnSapStatsMeterId_Type=TSapIngQueueId
_TnSapStatsMeterId_Object=MibTableColumn
tnSapStatsMeterId=_TnSapStatsMeterId_Object((1,3,6,1,4,1,7483,6,1,2,99,14,1,1),_TnSapStatsMeterId_Type())
tnSapStatsMeterId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSapStatsMeterId.setStatus(_A)
_TnSapMeterStatsInProfilePktsForwarded_Type=Counter64
_TnSapMeterStatsInProfilePktsForwarded_Object=MibTableColumn
tnSapMeterStatsInProfilePktsForwarded=_TnSapMeterStatsInProfilePktsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,14,1,2),_TnSapMeterStatsInProfilePktsForwarded_Type())
tnSapMeterStatsInProfilePktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapMeterStatsInProfilePktsForwarded.setStatus(_A)
_TnSapMeterStatsOutOfProfilePktsForwarded_Type=Counter64
_TnSapMeterStatsOutOfProfilePktsForwarded_Object=MibTableColumn
tnSapMeterStatsOutOfProfilePktsForwarded=_TnSapMeterStatsOutOfProfilePktsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,14,1,3),_TnSapMeterStatsOutOfProfilePktsForwarded_Type())
tnSapMeterStatsOutOfProfilePktsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapMeterStatsOutOfProfilePktsForwarded.setStatus(_A)
_TnSapMeterStatsInProfileOctetsForwarded_Type=Counter64
_TnSapMeterStatsInProfileOctetsForwarded_Object=MibTableColumn
tnSapMeterStatsInProfileOctetsForwarded=_TnSapMeterStatsInProfileOctetsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,14,1,4),_TnSapMeterStatsInProfileOctetsForwarded_Type())
tnSapMeterStatsInProfileOctetsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapMeterStatsInProfileOctetsForwarded.setStatus(_A)
_TnSapMeterStatsOutOfProfileOctetsForwarded_Type=Counter64
_TnSapMeterStatsOutOfProfileOctetsForwarded_Object=MibTableColumn
tnSapMeterStatsOutOfProfileOctetsForwarded=_TnSapMeterStatsOutOfProfileOctetsForwarded_Object((1,3,6,1,4,1,7483,6,1,2,99,14,1,5),_TnSapMeterStatsOutOfProfileOctetsForwarded_Type())
tnSapMeterStatsOutOfProfileOctetsForwarded.setMaxAccess(_B)
if mibBuilder.loadTexts:tnSapMeterStatsOutOfProfileOctetsForwarded.setStatus(_A)
_TnEthCfmTWSlmStatsAttributeTotal_Type=Integer32
_TnEthCfmTWSlmStatsAttributeTotal_Object=MibScalar
tnEthCfmTWSlmStatsAttributeTotal=_TnEthCfmTWSlmStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,15),_TnEthCfmTWSlmStatsAttributeTotal_Type())
tnEthCfmTWSlmStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsAttributeTotal.setStatus(_A)
_TnEthCfmTWSlmStatsTable_Object=MibTable
tnEthCfmTWSlmStatsTable=_TnEthCfmTWSlmStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,16))
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsTable.setStatus(_A)
_TnEthCfmTWSlmStatsEntry_Object=MibTableRow
tnEthCfmTWSlmStatsEntry=_TnEthCfmTWSlmStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1))
tnEthCfmTWSlmStatsEntry.setIndexNames((0,_G,_H),(0,_C,_d),(0,_C,_e),(0,_C,_f))
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsEntry.setStatus(_A)
_TnEthCfmTWSlmStatsTestName_Type=SnmpAdminString
_TnEthCfmTWSlmStatsTestName_Object=MibTableColumn
tnEthCfmTWSlmStatsTestName=_TnEthCfmTWSlmStatsTestName_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,1),_TnEthCfmTWSlmStatsTestName_Type())
tnEthCfmTWSlmStatsTestName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsTestName.setStatus(_A)
_TnEthCfmTWSlmStatsInterval_Type=AluWdmStatsIntervalType
_TnEthCfmTWSlmStatsInterval_Object=MibTableColumn
tnEthCfmTWSlmStatsInterval=_TnEthCfmTWSlmStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,2),_TnEthCfmTWSlmStatsInterval_Type())
tnEthCfmTWSlmStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsInterval.setStatus(_A)
_TnEthCfmTWSlmStatsBin_Type=AluWdmStatsBinNumber
_TnEthCfmTWSlmStatsBin_Object=MibTableColumn
tnEthCfmTWSlmStatsBin=_TnEthCfmTWSlmStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,3),_TnEthCfmTWSlmStatsBin_Type())
tnEthCfmTWSlmStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsBin.setStatus(_A)
_TnEthCfmTWSlmStatsBinStatus_Type=AluWdmStatsBinStatus
_TnEthCfmTWSlmStatsBinStatus_Object=MibTableColumn
tnEthCfmTWSlmStatsBinStatus=_TnEthCfmTWSlmStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,4),_TnEthCfmTWSlmStatsBinStatus_Type())
tnEthCfmTWSlmStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsBinStatus.setStatus(_A)
_TnEthCfmTWSlmStatsStartTime_Type=DateAndTime
_TnEthCfmTWSlmStatsStartTime_Object=MibTableColumn
tnEthCfmTWSlmStatsStartTime=_TnEthCfmTWSlmStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,5),_TnEthCfmTWSlmStatsStartTime_Type())
tnEthCfmTWSlmStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsStartTime.setStatus(_A)
_TnEthCfmTWSlmStatsTotalMembers_Type=Integer32
_TnEthCfmTWSlmStatsTotalMembers_Object=MibTableColumn
tnEthCfmTWSlmStatsTotalMembers=_TnEthCfmTWSlmStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,6),_TnEthCfmTWSlmStatsTotalMembers_Type())
tnEthCfmTWSlmStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsTotalMembers.setStatus(_A)
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Type=Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Object=MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioMin=_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,7),_TnEthCfmTWSlmStatsNearEndFrameLossRatioMin_Type())
tnEthCfmTWSlmStatsNearEndFrameLossRatioMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsNearEndFrameLossRatioMin.setStatus(_A)
_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Type=Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Object=MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage=_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,8),_TnEthCfmTWSlmStatsNearEndFrameLossRatioAverage_Type())
tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage.setStatus(_A)
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Type=Integer32
_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Object=MibTableColumn
tnEthCfmTWSlmStatsNearEndFrameLossRatioMax=_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,9),_TnEthCfmTWSlmStatsNearEndFrameLossRatioMax_Type())
tnEthCfmTWSlmStatsNearEndFrameLossRatioMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsNearEndFrameLossRatioMax.setStatus(_A)
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Type=Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Object=MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioMin=_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,10),_TnEthCfmTWSlmStatsFarEndFrameLossRatioMin_Type())
tnEthCfmTWSlmStatsFarEndFrameLossRatioMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsFarEndFrameLossRatioMin.setStatus(_A)
_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Type=Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Object=MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage=_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,11),_TnEthCfmTWSlmStatsFarEndFrameLossRatioAverage_Type())
tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage.setStatus(_A)
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Type=Integer32
_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Object=MibTableColumn
tnEthCfmTWSlmStatsFarEndFrameLossRatioMax=_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,12),_TnEthCfmTWSlmStatsFarEndFrameLossRatioMax_Type())
tnEthCfmTWSlmStatsFarEndFrameLossRatioMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsFarEndFrameLossRatioMax.setStatus(_A)
_TnEthCfmTWSlmStatsNearEndHighLoss_Type=Integer32
_TnEthCfmTWSlmStatsNearEndHighLoss_Object=MibTableColumn
tnEthCfmTWSlmStatsNearEndHighLoss=_TnEthCfmTWSlmStatsNearEndHighLoss_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,13),_TnEthCfmTWSlmStatsNearEndHighLoss_Type())
tnEthCfmTWSlmStatsNearEndHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsNearEndHighLoss.setStatus(_A)
_TnEthCfmTWSlmStatsFarEndHighLoss_Type=Integer32
_TnEthCfmTWSlmStatsFarEndHighLoss_Object=MibTableColumn
tnEthCfmTWSlmStatsFarEndHighLoss=_TnEthCfmTWSlmStatsFarEndHighLoss_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,14),_TnEthCfmTWSlmStatsFarEndHighLoss_Type())
tnEthCfmTWSlmStatsFarEndHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsFarEndHighLoss.setStatus(_A)
_TnEthCfmTWSlmStatsNearEndUnavailable_Type=Integer32
_TnEthCfmTWSlmStatsNearEndUnavailable_Object=MibTableColumn
tnEthCfmTWSlmStatsNearEndUnavailable=_TnEthCfmTWSlmStatsNearEndUnavailable_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,15),_TnEthCfmTWSlmStatsNearEndUnavailable_Type())
tnEthCfmTWSlmStatsNearEndUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsNearEndUnavailable.setStatus(_A)
_TnEthCfmTWSlmStatsFarEndUnavailable_Type=Integer32
_TnEthCfmTWSlmStatsFarEndUnavailable_Object=MibTableColumn
tnEthCfmTWSlmStatsFarEndUnavailable=_TnEthCfmTWSlmStatsFarEndUnavailable_Object((1,3,6,1,4,1,7483,6,1,2,99,16,1,16),_TnEthCfmTWSlmStatsFarEndUnavailable_Type())
tnEthCfmTWSlmStatsFarEndUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWSlmStatsFarEndUnavailable.setStatus(_A)
_TnEthCfmTWDmStatsAttributeTotal_Type=Integer32
_TnEthCfmTWDmStatsAttributeTotal_Object=MibScalar
tnEthCfmTWDmStatsAttributeTotal=_TnEthCfmTWDmStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,17),_TnEthCfmTWDmStatsAttributeTotal_Type())
tnEthCfmTWDmStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsAttributeTotal.setStatus(_A)
_TnEthCfmTWDmStatsTable_Object=MibTable
tnEthCfmTWDmStatsTable=_TnEthCfmTWDmStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,18))
if mibBuilder.loadTexts:tnEthCfmTWDmStatsTable.setStatus(_A)
_TnEthCfmTWDmStatsEntry_Object=MibTableRow
tnEthCfmTWDmStatsEntry=_TnEthCfmTWDmStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1))
tnEthCfmTWDmStatsEntry.setIndexNames((0,_G,_H),(0,_C,_g),(0,_C,_h),(0,_C,_i))
if mibBuilder.loadTexts:tnEthCfmTWDmStatsEntry.setStatus(_A)
_TnEthCfmTWDmStatsTestName_Type=SnmpAdminString
_TnEthCfmTWDmStatsTestName_Object=MibTableColumn
tnEthCfmTWDmStatsTestName=_TnEthCfmTWDmStatsTestName_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,1),_TnEthCfmTWDmStatsTestName_Type())
tnEthCfmTWDmStatsTestName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsTestName.setStatus(_A)
_TnEthCfmTWDmStatsInterval_Type=AluWdmStatsIntervalType
_TnEthCfmTWDmStatsInterval_Object=MibTableColumn
tnEthCfmTWDmStatsInterval=_TnEthCfmTWDmStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,2),_TnEthCfmTWDmStatsInterval_Type())
tnEthCfmTWDmStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsInterval.setStatus(_A)
_TnEthCfmTWDmStatsBin_Type=AluWdmStatsBinNumber
_TnEthCfmTWDmStatsBin_Object=MibTableColumn
tnEthCfmTWDmStatsBin=_TnEthCfmTWDmStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,3),_TnEthCfmTWDmStatsBin_Type())
tnEthCfmTWDmStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsBin.setStatus(_A)
_TnEthCfmTWDmStatsBinStatus_Type=AluWdmStatsBinStatus
_TnEthCfmTWDmStatsBinStatus_Object=MibTableColumn
tnEthCfmTWDmStatsBinStatus=_TnEthCfmTWDmStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,4),_TnEthCfmTWDmStatsBinStatus_Type())
tnEthCfmTWDmStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsBinStatus.setStatus(_A)
_TnEthCfmTWDmStatsStartTime_Type=DateAndTime
_TnEthCfmTWDmStatsStartTime_Object=MibTableColumn
tnEthCfmTWDmStatsStartTime=_TnEthCfmTWDmStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,5),_TnEthCfmTWDmStatsStartTime_Type())
tnEthCfmTWDmStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsStartTime.setStatus(_A)
_TnEthCfmTWDmStatsTotalMembers_Type=Integer32
_TnEthCfmTWDmStatsTotalMembers_Object=MibTableColumn
tnEthCfmTWDmStatsTotalMembers=_TnEthCfmTWDmStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,6),_TnEthCfmTWDmStatsTotalMembers_Type())
tnEthCfmTWDmStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsTotalMembers.setStatus(_A)
_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Type=Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Object=MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayMin=_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,7),_TnEthCfmTWDmStatsRoundTripFrameDelayMin_Type())
tnEthCfmTWDmStatsRoundTripFrameDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsRoundTripFrameDelayMin.setStatus(_A)
_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Type=Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Object=MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayAverage=_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,8),_TnEthCfmTWDmStatsRoundTripFrameDelayAverage_Type())
tnEthCfmTWDmStatsRoundTripFrameDelayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsRoundTripFrameDelayAverage.setStatus(_A)
_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Type=Integer32
_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Object=MibTableColumn
tnEthCfmTWDmStatsRoundTripFrameDelayMax=_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,9),_TnEthCfmTWDmStatsRoundTripFrameDelayMax_Type())
tnEthCfmTWDmStatsRoundTripFrameDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsRoundTripFrameDelayMax.setStatus(_A)
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Type=Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Object=MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationMin=_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,10),_TnEthCfmTWDmStatsNearEndFrameDelayVariationMin_Type())
tnEthCfmTWDmStatsNearEndFrameDelayVariationMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsNearEndFrameDelayVariationMin.setStatus(_A)
_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Type=Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Object=MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage=_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,11),_TnEthCfmTWDmStatsNearEndFrameDelayVariationAverage_Type())
tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage.setStatus(_A)
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Type=Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Object=MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayVariationMax=_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,12),_TnEthCfmTWDmStatsNearEndFrameDelayVariationMax_Type())
tnEthCfmTWDmStatsNearEndFrameDelayVariationMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsNearEndFrameDelayVariationMax.setStatus(_A)
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Type=Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Object=MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationMin=_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,13),_TnEthCfmTWDmStatsFarEndFrameDelayVariationMin_Type())
tnEthCfmTWDmStatsFarEndFrameDelayVariationMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsFarEndFrameDelayVariationMin.setStatus(_A)
_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Type=Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Object=MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage=_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,14),_TnEthCfmTWDmStatsFarEndFrameDelayVariationAverage_Type())
tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage.setStatus(_A)
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Type=Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Object=MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayVariationMax=_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,15),_TnEthCfmTWDmStatsFarEndFrameDelayVariationMax_Type())
tnEthCfmTWDmStatsFarEndFrameDelayVariationMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsFarEndFrameDelayVariationMax.setStatus(_A)
_TnEthCfmTWDmStatsNearEndFrameDelayMin_Type=Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayMin_Object=MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayMin=_TnEthCfmTWDmStatsNearEndFrameDelayMin_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,16),_TnEthCfmTWDmStatsNearEndFrameDelayMin_Type())
tnEthCfmTWDmStatsNearEndFrameDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsNearEndFrameDelayMin.setStatus(_A)
_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Type=Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Object=MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayAverage=_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,17),_TnEthCfmTWDmStatsNearEndFrameDelayAverage_Type())
tnEthCfmTWDmStatsNearEndFrameDelayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsNearEndFrameDelayAverage.setStatus(_A)
_TnEthCfmTWDmStatsNearEndFrameDelayMax_Type=Integer32
_TnEthCfmTWDmStatsNearEndFrameDelayMax_Object=MibTableColumn
tnEthCfmTWDmStatsNearEndFrameDelayMax=_TnEthCfmTWDmStatsNearEndFrameDelayMax_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,18),_TnEthCfmTWDmStatsNearEndFrameDelayMax_Type())
tnEthCfmTWDmStatsNearEndFrameDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsNearEndFrameDelayMax.setStatus(_A)
_TnEthCfmTWDmStatsFarEndFrameDelayMin_Type=Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayMin_Object=MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayMin=_TnEthCfmTWDmStatsFarEndFrameDelayMin_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,19),_TnEthCfmTWDmStatsFarEndFrameDelayMin_Type())
tnEthCfmTWDmStatsFarEndFrameDelayMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsFarEndFrameDelayMin.setStatus(_A)
_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Type=Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Object=MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayAverage=_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,20),_TnEthCfmTWDmStatsFarEndFrameDelayAverage_Type())
tnEthCfmTWDmStatsFarEndFrameDelayAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsFarEndFrameDelayAverage.setStatus(_A)
_TnEthCfmTWDmStatsFarEndFrameDelayMax_Type=Integer32
_TnEthCfmTWDmStatsFarEndFrameDelayMax_Object=MibTableColumn
tnEthCfmTWDmStatsFarEndFrameDelayMax=_TnEthCfmTWDmStatsFarEndFrameDelayMax_Object((1,3,6,1,4,1,7483,6,1,2,99,18,1,21),_TnEthCfmTWDmStatsFarEndFrameDelayMax_Type())
tnEthCfmTWDmStatsFarEndFrameDelayMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWDmStatsFarEndFrameDelayMax.setStatus(_A)
_TnEthCfmTWLmStatsAttributeTotal_Type=Integer32
_TnEthCfmTWLmStatsAttributeTotal_Object=MibScalar
tnEthCfmTWLmStatsAttributeTotal=_TnEthCfmTWLmStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,19),_TnEthCfmTWLmStatsAttributeTotal_Type())
tnEthCfmTWLmStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsAttributeTotal.setStatus(_A)
_TnEthCfmTWLmStatsTable_Object=MibTable
tnEthCfmTWLmStatsTable=_TnEthCfmTWLmStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,20))
if mibBuilder.loadTexts:tnEthCfmTWLmStatsTable.setStatus(_A)
_TnEthCfmTWLmStatsEntry_Object=MibTableRow
tnEthCfmTWLmStatsEntry=_TnEthCfmTWLmStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1))
tnEthCfmTWLmStatsEntry.setIndexNames((0,_G,_H),(0,_C,_j),(0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:tnEthCfmTWLmStatsEntry.setStatus(_A)
_TnEthCfmTWLmStatsTestName_Type=SnmpAdminString
_TnEthCfmTWLmStatsTestName_Object=MibTableColumn
tnEthCfmTWLmStatsTestName=_TnEthCfmTWLmStatsTestName_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,1),_TnEthCfmTWLmStatsTestName_Type())
tnEthCfmTWLmStatsTestName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsTestName.setStatus(_A)
_TnEthCfmTWLmStatsInterval_Type=AluWdmStatsIntervalType
_TnEthCfmTWLmStatsInterval_Object=MibTableColumn
tnEthCfmTWLmStatsInterval=_TnEthCfmTWLmStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,2),_TnEthCfmTWLmStatsInterval_Type())
tnEthCfmTWLmStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsInterval.setStatus(_A)
_TnEthCfmTWLmStatsBin_Type=AluWdmStatsBinNumber
_TnEthCfmTWLmStatsBin_Object=MibTableColumn
tnEthCfmTWLmStatsBin=_TnEthCfmTWLmStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,3),_TnEthCfmTWLmStatsBin_Type())
tnEthCfmTWLmStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsBin.setStatus(_A)
_TnEthCfmTWLmStatsBinStatus_Type=AluWdmStatsBinStatus
_TnEthCfmTWLmStatsBinStatus_Object=MibTableColumn
tnEthCfmTWLmStatsBinStatus=_TnEthCfmTWLmStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,4),_TnEthCfmTWLmStatsBinStatus_Type())
tnEthCfmTWLmStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsBinStatus.setStatus(_A)
_TnEthCfmTWLmStatsStartTime_Type=DateAndTime
_TnEthCfmTWLmStatsStartTime_Object=MibTableColumn
tnEthCfmTWLmStatsStartTime=_TnEthCfmTWLmStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,5),_TnEthCfmTWLmStatsStartTime_Type())
tnEthCfmTWLmStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsStartTime.setStatus(_A)
_TnEthCfmTWLmStatsTotalMembers_Type=Integer32
_TnEthCfmTWLmStatsTotalMembers_Object=MibTableColumn
tnEthCfmTWLmStatsTotalMembers=_TnEthCfmTWLmStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,6),_TnEthCfmTWLmStatsTotalMembers_Type())
tnEthCfmTWLmStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsTotalMembers.setStatus(_A)
_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Type=Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Object=MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioMin=_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,7),_TnEthCfmTWLmStatsNearEndFrameLossRatioMin_Type())
tnEthCfmTWLmStatsNearEndFrameLossRatioMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsNearEndFrameLossRatioMin.setStatus(_A)
_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Type=Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Object=MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioAverage=_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,8),_TnEthCfmTWLmStatsNearEndFrameLossRatioAverage_Type())
tnEthCfmTWLmStatsNearEndFrameLossRatioAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsNearEndFrameLossRatioAverage.setStatus(_A)
_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Type=Integer32
_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Object=MibTableColumn
tnEthCfmTWLmStatsNearEndFrameLossRatioMax=_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,9),_TnEthCfmTWLmStatsNearEndFrameLossRatioMax_Type())
tnEthCfmTWLmStatsNearEndFrameLossRatioMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsNearEndFrameLossRatioMax.setStatus(_A)
_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Type=Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Object=MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioMin=_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,10),_TnEthCfmTWLmStatsFarEndFrameLossRatioMin_Type())
tnEthCfmTWLmStatsFarEndFrameLossRatioMin.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsFarEndFrameLossRatioMin.setStatus(_A)
_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Type=Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Object=MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioAverage=_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,11),_TnEthCfmTWLmStatsFarEndFrameLossRatioAverage_Type())
tnEthCfmTWLmStatsFarEndFrameLossRatioAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsFarEndFrameLossRatioAverage.setStatus(_A)
_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Type=Integer32
_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Object=MibTableColumn
tnEthCfmTWLmStatsFarEndFrameLossRatioMax=_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,12),_TnEthCfmTWLmStatsFarEndFrameLossRatioMax_Type())
tnEthCfmTWLmStatsFarEndFrameLossRatioMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsFarEndFrameLossRatioMax.setStatus(_A)
_TnEthCfmTWLmStatsNearEndHighLoss_Type=Integer32
_TnEthCfmTWLmStatsNearEndHighLoss_Object=MibTableColumn
tnEthCfmTWLmStatsNearEndHighLoss=_TnEthCfmTWLmStatsNearEndHighLoss_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,13),_TnEthCfmTWLmStatsNearEndHighLoss_Type())
tnEthCfmTWLmStatsNearEndHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsNearEndHighLoss.setStatus(_A)
_TnEthCfmTWLmStatsFarEndHighLoss_Type=Integer32
_TnEthCfmTWLmStatsFarEndHighLoss_Object=MibTableColumn
tnEthCfmTWLmStatsFarEndHighLoss=_TnEthCfmTWLmStatsFarEndHighLoss_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,14),_TnEthCfmTWLmStatsFarEndHighLoss_Type())
tnEthCfmTWLmStatsFarEndHighLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsFarEndHighLoss.setStatus(_A)
_TnEthCfmTWLmStatsNearEndUnavailable_Type=Integer32
_TnEthCfmTWLmStatsNearEndUnavailable_Object=MibTableColumn
tnEthCfmTWLmStatsNearEndUnavailable=_TnEthCfmTWLmStatsNearEndUnavailable_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,15),_TnEthCfmTWLmStatsNearEndUnavailable_Type())
tnEthCfmTWLmStatsNearEndUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsNearEndUnavailable.setStatus(_A)
_TnEthCfmTWLmStatsFarEndUnavailable_Type=Integer32
_TnEthCfmTWLmStatsFarEndUnavailable_Object=MibTableColumn
tnEthCfmTWLmStatsFarEndUnavailable=_TnEthCfmTWLmStatsFarEndUnavailable_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,16),_TnEthCfmTWLmStatsFarEndUnavailable_Type())
tnEthCfmTWLmStatsFarEndUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsFarEndUnavailable.setStatus(_A)
_TnEthCfmTWLmStatsTransmittedLMMFrame_Type=Counter64
_TnEthCfmTWLmStatsTransmittedLMMFrame_Object=MibTableColumn
tnEthCfmTWLmStatsTransmittedLMMFrame=_TnEthCfmTWLmStatsTransmittedLMMFrame_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,17),_TnEthCfmTWLmStatsTransmittedLMMFrame_Type())
tnEthCfmTWLmStatsTransmittedLMMFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsTransmittedLMMFrame.setStatus(_A)
_TnEthCfmTWLmStatsReceivedLMRFrame_Type=Counter64
_TnEthCfmTWLmStatsReceivedLMRFrame_Object=MibTableColumn
tnEthCfmTWLmStatsReceivedLMRFrame=_TnEthCfmTWLmStatsReceivedLMRFrame_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,18),_TnEthCfmTWLmStatsReceivedLMRFrame_Type())
tnEthCfmTWLmStatsReceivedLMRFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsReceivedLMRFrame.setStatus(_A)
_TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Type=Counter64
_TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Object=MibTableColumn
tnEthCfmTWLmStatsNearEndTransmittedDataFrame=_TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,19),_TnEthCfmTWLmStatsNearEndTransmittedDataFrame_Type())
tnEthCfmTWLmStatsNearEndTransmittedDataFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsNearEndTransmittedDataFrame.setStatus(_A)
_TnEthCfmTWLmStatsNearEndReceivedDataFrame_Type=Counter64
_TnEthCfmTWLmStatsNearEndReceivedDataFrame_Object=MibTableColumn
tnEthCfmTWLmStatsNearEndReceivedDataFrame=_TnEthCfmTWLmStatsNearEndReceivedDataFrame_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,20),_TnEthCfmTWLmStatsNearEndReceivedDataFrame_Type())
tnEthCfmTWLmStatsNearEndReceivedDataFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsNearEndReceivedDataFrame.setStatus(_A)
_TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Type=Counter64
_TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Object=MibTableColumn
tnEthCfmTWLmStatsFarEndTransmittedDataFrame=_TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,21),_TnEthCfmTWLmStatsFarEndTransmittedDataFrame_Type())
tnEthCfmTWLmStatsFarEndTransmittedDataFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsFarEndTransmittedDataFrame.setStatus(_A)
_TnEthCfmTWLmStatsFarEndReceivedDataFrame_Type=Counter64
_TnEthCfmTWLmStatsFarEndReceivedDataFrame_Object=MibTableColumn
tnEthCfmTWLmStatsFarEndReceivedDataFrame=_TnEthCfmTWLmStatsFarEndReceivedDataFrame_Object((1,3,6,1,4,1,7483,6,1,2,99,20,1,22),_TnEthCfmTWLmStatsFarEndReceivedDataFrame_Type())
tnEthCfmTWLmStatsFarEndReceivedDataFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEthCfmTWLmStatsFarEndReceivedDataFrame.setStatus(_A)
_TnPktWanifStatsAttributeTotal_Type=Integer32
_TnPktWanifStatsAttributeTotal_Object=MibScalar
tnPktWanifStatsAttributeTotal=_TnPktWanifStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,21),_TnPktWanifStatsAttributeTotal_Type())
tnPktWanifStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsAttributeTotal.setStatus(_A)
_TnPktWanifStatsTable_Object=MibTable
tnPktWanifStatsTable=_TnPktWanifStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,22))
if mibBuilder.loadTexts:tnPktWanifStatsTable.setStatus(_A)
_TnPktWanifStatsEntry_Object=MibTableRow
tnPktWanifStatsEntry=_TnPktWanifStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1))
tnPktWanifStatsEntry.setIndexNames((0,_C,_m),(0,_C,_n),(0,_C,_o))
if mibBuilder.loadTexts:tnPktWanifStatsEntry.setStatus(_A)
_TnPktWanifStatsPortId_Type=TmnxPortID
_TnPktWanifStatsPortId_Object=MibTableColumn
tnPktWanifStatsPortId=_TnPktWanifStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,1),_TnPktWanifStatsPortId_Type())
tnPktWanifStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPktWanifStatsPortId.setStatus(_A)
_TnPktWanifStatsInterval_Type=AluWdmStatsIntervalType
_TnPktWanifStatsInterval_Object=MibTableColumn
tnPktWanifStatsInterval=_TnPktWanifStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,2),_TnPktWanifStatsInterval_Type())
tnPktWanifStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPktWanifStatsInterval.setStatus(_A)
_TnPktWanifStatsBin_Type=AluWdmStatsBinNumber
_TnPktWanifStatsBin_Object=MibTableColumn
tnPktWanifStatsBin=_TnPktWanifStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,3),_TnPktWanifStatsBin_Type())
tnPktWanifStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPktWanifStatsBin.setStatus(_A)
_TnPktWanifStatsBinStatus_Type=AluWdmStatsBinStatus
_TnPktWanifStatsBinStatus_Object=MibTableColumn
tnPktWanifStatsBinStatus=_TnPktWanifStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,4),_TnPktWanifStatsBinStatus_Type())
tnPktWanifStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsBinStatus.setStatus(_A)
_TnPktWanifStatsStartTime_Type=DateAndTime
_TnPktWanifStatsStartTime_Object=MibTableColumn
tnPktWanifStatsStartTime=_TnPktWanifStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,5),_TnPktWanifStatsStartTime_Type())
tnPktWanifStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsStartTime.setStatus(_A)
_TnPktWanifStatsInPackets_Type=Counter64
_TnPktWanifStatsInPackets_Object=MibTableColumn
tnPktWanifStatsInPackets=_TnPktWanifStatsInPackets_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,6),_TnPktWanifStatsInPackets_Type())
tnPktWanifStatsInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInPackets.setStatus(_A)
_TnPktWanifStatsInOctets_Type=Counter64
_TnPktWanifStatsInOctets_Object=MibTableColumn
tnPktWanifStatsInOctets=_TnPktWanifStatsInOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,7),_TnPktWanifStatsInOctets_Type())
tnPktWanifStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInOctets.setStatus(_A)
_TnPktWanifStatsInUcastPkts_Type=Counter64
_TnPktWanifStatsInUcastPkts_Object=MibTableColumn
tnPktWanifStatsInUcastPkts=_TnPktWanifStatsInUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,8),_TnPktWanifStatsInUcastPkts_Type())
tnPktWanifStatsInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInUcastPkts.setStatus(_A)
_TnPktWanifStatsInDiscards_Type=Counter64
_TnPktWanifStatsInDiscards_Object=MibTableColumn
tnPktWanifStatsInDiscards=_TnPktWanifStatsInDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,9),_TnPktWanifStatsInDiscards_Type())
tnPktWanifStatsInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInDiscards.setStatus(_A)
_TnPktWanifStatsInErrors_Type=Counter64
_TnPktWanifStatsInErrors_Object=MibTableColumn
tnPktWanifStatsInErrors=_TnPktWanifStatsInErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,10),_TnPktWanifStatsInErrors_Type())
tnPktWanifStatsInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInErrors.setStatus(_A)
_TnPktWanifStatsInUnknownProtos_Type=Counter64
_TnPktWanifStatsInUnknownProtos_Object=MibTableColumn
tnPktWanifStatsInUnknownProtos=_TnPktWanifStatsInUnknownProtos_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,11),_TnPktWanifStatsInUnknownProtos_Type())
tnPktWanifStatsInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInUnknownProtos.setStatus(_A)
_TnPktWanifStatsInMulticastPkts_Type=Counter64
_TnPktWanifStatsInMulticastPkts_Object=MibTableColumn
tnPktWanifStatsInMulticastPkts=_TnPktWanifStatsInMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,12),_TnPktWanifStatsInMulticastPkts_Type())
tnPktWanifStatsInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInMulticastPkts.setStatus(_A)
_TnPktWanifStatsInBroadcastPkts_Type=Counter64
_TnPktWanifStatsInBroadcastPkts_Object=MibTableColumn
tnPktWanifStatsInBroadcastPkts=_TnPktWanifStatsInBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,13),_TnPktWanifStatsInBroadcastPkts_Type())
tnPktWanifStatsInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsInBroadcastPkts.setStatus(_A)
_TnPktWanifStatsOutPackets_Type=Counter64
_TnPktWanifStatsOutPackets_Object=MibTableColumn
tnPktWanifStatsOutPackets=_TnPktWanifStatsOutPackets_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,14),_TnPktWanifStatsOutPackets_Type())
tnPktWanifStatsOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOutPackets.setStatus(_A)
_TnPktWanifStatsOutOctets_Type=Counter64
_TnPktWanifStatsOutOctets_Object=MibTableColumn
tnPktWanifStatsOutOctets=_TnPktWanifStatsOutOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,15),_TnPktWanifStatsOutOctets_Type())
tnPktWanifStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOutOctets.setStatus(_A)
_TnPktWanifStatsOutUcastPkts_Type=Counter64
_TnPktWanifStatsOutUcastPkts_Object=MibTableColumn
tnPktWanifStatsOutUcastPkts=_TnPktWanifStatsOutUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,16),_TnPktWanifStatsOutUcastPkts_Type())
tnPktWanifStatsOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOutUcastPkts.setStatus(_A)
_TnPktWanifStatsOutDiscards_Type=Counter64
_TnPktWanifStatsOutDiscards_Object=MibTableColumn
tnPktWanifStatsOutDiscards=_TnPktWanifStatsOutDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,17),_TnPktWanifStatsOutDiscards_Type())
tnPktWanifStatsOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOutDiscards.setStatus(_A)
_TnPktWanifStatsOutErrors_Type=Counter64
_TnPktWanifStatsOutErrors_Object=MibTableColumn
tnPktWanifStatsOutErrors=_TnPktWanifStatsOutErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,18),_TnPktWanifStatsOutErrors_Type())
tnPktWanifStatsOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOutErrors.setStatus(_A)
_TnPktWanifStatsOutMulticastPkts_Type=Counter64
_TnPktWanifStatsOutMulticastPkts_Object=MibTableColumn
tnPktWanifStatsOutMulticastPkts=_TnPktWanifStatsOutMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,19),_TnPktWanifStatsOutMulticastPkts_Type())
tnPktWanifStatsOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOutMulticastPkts.setStatus(_A)
_TnPktWanifStatsOutBroadcastPkts_Type=Counter64
_TnPktWanifStatsOutBroadcastPkts_Object=MibTableColumn
tnPktWanifStatsOutBroadcastPkts=_TnPktWanifStatsOutBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,20),_TnPktWanifStatsOutBroadcastPkts_Type())
tnPktWanifStatsOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOutBroadcastPkts.setStatus(_A)
_TnPktWanifStatsDropEvents_Type=Counter64
_TnPktWanifStatsDropEvents_Object=MibTableColumn
tnPktWanifStatsDropEvents=_TnPktWanifStatsDropEvents_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,21),_TnPktWanifStatsDropEvents_Type())
tnPktWanifStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsDropEvents.setStatus(_A)
_TnPktWanifStatsBroadcastPkts_Type=Counter64
_TnPktWanifStatsBroadcastPkts_Object=MibTableColumn
tnPktWanifStatsBroadcastPkts=_TnPktWanifStatsBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,22),_TnPktWanifStatsBroadcastPkts_Type())
tnPktWanifStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsBroadcastPkts.setStatus(_A)
_TnPktWanifStatsMulticastPkts_Type=Counter64
_TnPktWanifStatsMulticastPkts_Object=MibTableColumn
tnPktWanifStatsMulticastPkts=_TnPktWanifStatsMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,23),_TnPktWanifStatsMulticastPkts_Type())
tnPktWanifStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsMulticastPkts.setStatus(_A)
_TnPktWanifStatsCRCAlignErrors_Type=Counter64
_TnPktWanifStatsCRCAlignErrors_Object=MibTableColumn
tnPktWanifStatsCRCAlignErrors=_TnPktWanifStatsCRCAlignErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,24),_TnPktWanifStatsCRCAlignErrors_Type())
tnPktWanifStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsCRCAlignErrors.setStatus(_A)
_TnPktWanifStatsUndersizePkts_Type=Counter64
_TnPktWanifStatsUndersizePkts_Object=MibTableColumn
tnPktWanifStatsUndersizePkts=_TnPktWanifStatsUndersizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,25),_TnPktWanifStatsUndersizePkts_Type())
tnPktWanifStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsUndersizePkts.setStatus(_A)
_TnPktWanifStatsOversizePkts_Type=Counter64
_TnPktWanifStatsOversizePkts_Object=MibTableColumn
tnPktWanifStatsOversizePkts=_TnPktWanifStatsOversizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,26),_TnPktWanifStatsOversizePkts_Type())
tnPktWanifStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsOversizePkts.setStatus(_A)
_TnPktWanifStatsFragments_Type=Counter64
_TnPktWanifStatsFragments_Object=MibTableColumn
tnPktWanifStatsFragments=_TnPktWanifStatsFragments_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,27),_TnPktWanifStatsFragments_Type())
tnPktWanifStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsFragments.setStatus(_A)
_TnPktWanifStatsJabbers_Type=Counter64
_TnPktWanifStatsJabbers_Object=MibTableColumn
tnPktWanifStatsJabbers=_TnPktWanifStatsJabbers_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,28),_TnPktWanifStatsJabbers_Type())
tnPktWanifStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsJabbers.setStatus(_A)
_TnPktWanifStatsCollisions_Type=Counter64
_TnPktWanifStatsCollisions_Object=MibTableColumn
tnPktWanifStatsCollisions=_TnPktWanifStatsCollisions_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,29),_TnPktWanifStatsCollisions_Type())
tnPktWanifStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsCollisions.setStatus(_A)
_TnPktWanifStatsHighCapacityPkts_Type=Counter64
_TnPktWanifStatsHighCapacityPkts_Object=MibTableColumn
tnPktWanifStatsHighCapacityPkts=_TnPktWanifStatsHighCapacityPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,30),_TnPktWanifStatsHighCapacityPkts_Type())
tnPktWanifStatsHighCapacityPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPkts.setStatus(_A)
_TnPktWanifStatsHighCapacityOctets_Type=Counter64
_TnPktWanifStatsHighCapacityOctets_Object=MibTableColumn
tnPktWanifStatsHighCapacityOctets=_TnPktWanifStatsHighCapacityOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,31),_TnPktWanifStatsHighCapacityOctets_Type())
tnPktWanifStatsHighCapacityOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityOctets.setStatus(_A)
_TnPktWanifStatsHighCapacityPktsSize64_Type=Counter64
_TnPktWanifStatsHighCapacityPktsSize64_Object=MibTableColumn
tnPktWanifStatsHighCapacityPktsSize64=_TnPktWanifStatsHighCapacityPktsSize64_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,32),_TnPktWanifStatsHighCapacityPktsSize64_Type())
tnPktWanifStatsHighCapacityPktsSize64.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPktsSize64.setStatus(_A)
_TnPktWanifStatsHighCapacityPktsSize65to127_Type=Counter64
_TnPktWanifStatsHighCapacityPktsSize65to127_Object=MibTableColumn
tnPktWanifStatsHighCapacityPktsSize65to127=_TnPktWanifStatsHighCapacityPktsSize65to127_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,33),_TnPktWanifStatsHighCapacityPktsSize65to127_Type())
tnPktWanifStatsHighCapacityPktsSize65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPktsSize65to127.setStatus(_A)
_TnPktWanifStatsHighCapacityPktsSize128to255_Type=Counter64
_TnPktWanifStatsHighCapacityPktsSize128to255_Object=MibTableColumn
tnPktWanifStatsHighCapacityPktsSize128to255=_TnPktWanifStatsHighCapacityPktsSize128to255_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,34),_TnPktWanifStatsHighCapacityPktsSize128to255_Type())
tnPktWanifStatsHighCapacityPktsSize128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPktsSize128to255.setStatus(_A)
_TnPktWanifStatsHighCapacityPktsSize256to511_Type=Counter64
_TnPktWanifStatsHighCapacityPktsSize256to511_Object=MibTableColumn
tnPktWanifStatsHighCapacityPktsSize256to511=_TnPktWanifStatsHighCapacityPktsSize256to511_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,35),_TnPktWanifStatsHighCapacityPktsSize256to511_Type())
tnPktWanifStatsHighCapacityPktsSize256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPktsSize256to511.setStatus(_A)
_TnPktWanifStatsHighCapacityPktsSize512to1023_Type=Counter64
_TnPktWanifStatsHighCapacityPktsSize512to1023_Object=MibTableColumn
tnPktWanifStatsHighCapacityPktsSize512to1023=_TnPktWanifStatsHighCapacityPktsSize512to1023_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,36),_TnPktWanifStatsHighCapacityPktsSize512to1023_Type())
tnPktWanifStatsHighCapacityPktsSize512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPktsSize512to1023.setStatus(_A)
_TnPktWanifStatsHighCapacityPktsSize1024to1518_Type=Counter64
_TnPktWanifStatsHighCapacityPktsSize1024to1518_Object=MibTableColumn
tnPktWanifStatsHighCapacityPktsSize1024to1518=_TnPktWanifStatsHighCapacityPktsSize1024to1518_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,37),_TnPktWanifStatsHighCapacityPktsSize1024to1518_Type())
tnPktWanifStatsHighCapacityPktsSize1024to1518.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPktsSize1024to1518.setStatus(_A)
_TnPktWanifStatsHighCapacityPktsSize1519toMax_Type=Counter64
_TnPktWanifStatsHighCapacityPktsSize1519toMax_Object=MibTableColumn
tnPktWanifStatsHighCapacityPktsSize1519toMax=_TnPktWanifStatsHighCapacityPktsSize1519toMax_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,38),_TnPktWanifStatsHighCapacityPktsSize1519toMax_Type())
tnPktWanifStatsHighCapacityPktsSize1519toMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsHighCapacityPktsSize1519toMax.setStatus(_A)
_TnPktWanifStatsTooLongFrames_Type=Counter64
_TnPktWanifStatsTooLongFrames_Object=MibTableColumn
tnPktWanifStatsTooLongFrames=_TnPktWanifStatsTooLongFrames_Object((1,3,6,1,4,1,7483,6,1,2,99,22,1,39),_TnPktWanifStatsTooLongFrames_Type())
tnPktWanifStatsTooLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifStatsTooLongFrames.setStatus(_A)
_TnPktWanifRawCountStatsAttributeTotal_Type=Integer32
_TnPktWanifRawCountStatsAttributeTotal_Object=MibScalar
tnPktWanifRawCountStatsAttributeTotal=_TnPktWanifRawCountStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,23),_TnPktWanifRawCountStatsAttributeTotal_Type())
tnPktWanifRawCountStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsAttributeTotal.setStatus(_A)
_TnPktWanifRawCountStatsTable_Object=MibTable
tnPktWanifRawCountStatsTable=_TnPktWanifRawCountStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,24))
if mibBuilder.loadTexts:tnPktWanifRawCountStatsTable.setStatus(_A)
_TnPktWanifRawCountStatsEntry_Object=MibTableRow
tnPktWanifRawCountStatsEntry=_TnPktWanifRawCountStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1))
tnPktWanifRawCountStatsEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:tnPktWanifRawCountStatsEntry.setStatus(_A)
_TnPktWanifRawCountStatsPortId_Type=TmnxPortID
_TnPktWanifRawCountStatsPortId_Object=MibTableColumn
tnPktWanifRawCountStatsPortId=_TnPktWanifRawCountStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,1),_TnPktWanifRawCountStatsPortId_Type())
tnPktWanifRawCountStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsPortId.setStatus(_A)
_TnPktWanifRawCountStatsClear_Type=TnCommand
_TnPktWanifRawCountStatsClear_Object=MibTableColumn
tnPktWanifRawCountStatsClear=_TnPktWanifRawCountStatsClear_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,2),_TnPktWanifRawCountStatsClear_Type())
tnPktWanifRawCountStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsClear.setStatus(_A)
_TnPktWanifRawCountStatsStartTime_Type=DateAndTime
_TnPktWanifRawCountStatsStartTime_Object=MibTableColumn
tnPktWanifRawCountStatsStartTime=_TnPktWanifRawCountStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,3),_TnPktWanifRawCountStatsStartTime_Type())
tnPktWanifRawCountStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsStartTime.setStatus(_A)
_TnPktWanifRawCountStatsInPackets_Type=Counter64
_TnPktWanifRawCountStatsInPackets_Object=MibTableColumn
tnPktWanifRawCountStatsInPackets=_TnPktWanifRawCountStatsInPackets_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,4),_TnPktWanifRawCountStatsInPackets_Type())
tnPktWanifRawCountStatsInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInPackets.setStatus(_A)
_TnPktWanifRawCountStatsInOctets_Type=Counter64
_TnPktWanifRawCountStatsInOctets_Object=MibTableColumn
tnPktWanifRawCountStatsInOctets=_TnPktWanifRawCountStatsInOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,5),_TnPktWanifRawCountStatsInOctets_Type())
tnPktWanifRawCountStatsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInOctets.setStatus(_A)
_TnPktWanifRawCountStatsInUcastPkts_Type=Counter64
_TnPktWanifRawCountStatsInUcastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsInUcastPkts=_TnPktWanifRawCountStatsInUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,6),_TnPktWanifRawCountStatsInUcastPkts_Type())
tnPktWanifRawCountStatsInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInUcastPkts.setStatus(_A)
_TnPktWanifRawCountStatsInDiscards_Type=Counter64
_TnPktWanifRawCountStatsInDiscards_Object=MibTableColumn
tnPktWanifRawCountStatsInDiscards=_TnPktWanifRawCountStatsInDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,7),_TnPktWanifRawCountStatsInDiscards_Type())
tnPktWanifRawCountStatsInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInDiscards.setStatus(_A)
_TnPktWanifRawCountStatsInErrors_Type=Counter64
_TnPktWanifRawCountStatsInErrors_Object=MibTableColumn
tnPktWanifRawCountStatsInErrors=_TnPktWanifRawCountStatsInErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,8),_TnPktWanifRawCountStatsInErrors_Type())
tnPktWanifRawCountStatsInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInErrors.setStatus(_A)
_TnPktWanifRawCountStatsInUnknownProtos_Type=Counter64
_TnPktWanifRawCountStatsInUnknownProtos_Object=MibTableColumn
tnPktWanifRawCountStatsInUnknownProtos=_TnPktWanifRawCountStatsInUnknownProtos_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,9),_TnPktWanifRawCountStatsInUnknownProtos_Type())
tnPktWanifRawCountStatsInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInUnknownProtos.setStatus(_A)
_TnPktWanifRawCountStatsInMulticastPkts_Type=Counter64
_TnPktWanifRawCountStatsInMulticastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsInMulticastPkts=_TnPktWanifRawCountStatsInMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,10),_TnPktWanifRawCountStatsInMulticastPkts_Type())
tnPktWanifRawCountStatsInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInMulticastPkts.setStatus(_A)
_TnPktWanifRawCountStatsInBroadcastPkts_Type=Counter64
_TnPktWanifRawCountStatsInBroadcastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsInBroadcastPkts=_TnPktWanifRawCountStatsInBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,11),_TnPktWanifRawCountStatsInBroadcastPkts_Type())
tnPktWanifRawCountStatsInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsInBroadcastPkts.setStatus(_A)
_TnPktWanifRawCountStatsOutPackets_Type=Counter64
_TnPktWanifRawCountStatsOutPackets_Object=MibTableColumn
tnPktWanifRawCountStatsOutPackets=_TnPktWanifRawCountStatsOutPackets_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,12),_TnPktWanifRawCountStatsOutPackets_Type())
tnPktWanifRawCountStatsOutPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOutPackets.setStatus(_A)
_TnPktWanifRawCountStatsOutOctets_Type=Counter64
_TnPktWanifRawCountStatsOutOctets_Object=MibTableColumn
tnPktWanifRawCountStatsOutOctets=_TnPktWanifRawCountStatsOutOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,13),_TnPktWanifRawCountStatsOutOctets_Type())
tnPktWanifRawCountStatsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOutOctets.setStatus(_A)
_TnPktWanifRawCountStatsOutUcastPkts_Type=Counter64
_TnPktWanifRawCountStatsOutUcastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsOutUcastPkts=_TnPktWanifRawCountStatsOutUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,14),_TnPktWanifRawCountStatsOutUcastPkts_Type())
tnPktWanifRawCountStatsOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOutUcastPkts.setStatus(_A)
_TnPktWanifRawCountStatsOutDiscards_Type=Counter64
_TnPktWanifRawCountStatsOutDiscards_Object=MibTableColumn
tnPktWanifRawCountStatsOutDiscards=_TnPktWanifRawCountStatsOutDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,15),_TnPktWanifRawCountStatsOutDiscards_Type())
tnPktWanifRawCountStatsOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOutDiscards.setStatus(_A)
_TnPktWanifRawCountStatsOutErrors_Type=Counter64
_TnPktWanifRawCountStatsOutErrors_Object=MibTableColumn
tnPktWanifRawCountStatsOutErrors=_TnPktWanifRawCountStatsOutErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,16),_TnPktWanifRawCountStatsOutErrors_Type())
tnPktWanifRawCountStatsOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOutErrors.setStatus(_A)
_TnPktWanifRawCountStatsOutMulticastPkts_Type=Counter64
_TnPktWanifRawCountStatsOutMulticastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsOutMulticastPkts=_TnPktWanifRawCountStatsOutMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,17),_TnPktWanifRawCountStatsOutMulticastPkts_Type())
tnPktWanifRawCountStatsOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOutMulticastPkts.setStatus(_A)
_TnPktWanifRawCountStatsOutBroadcastPkts_Type=Counter64
_TnPktWanifRawCountStatsOutBroadcastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsOutBroadcastPkts=_TnPktWanifRawCountStatsOutBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,18),_TnPktWanifRawCountStatsOutBroadcastPkts_Type())
tnPktWanifRawCountStatsOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOutBroadcastPkts.setStatus(_A)
_TnPktWanifRawCountStatsDropEvents_Type=Counter64
_TnPktWanifRawCountStatsDropEvents_Object=MibTableColumn
tnPktWanifRawCountStatsDropEvents=_TnPktWanifRawCountStatsDropEvents_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,19),_TnPktWanifRawCountStatsDropEvents_Type())
tnPktWanifRawCountStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsDropEvents.setStatus(_A)
_TnPktWanifRawCountStatsBroadcastPkts_Type=Counter64
_TnPktWanifRawCountStatsBroadcastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsBroadcastPkts=_TnPktWanifRawCountStatsBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,20),_TnPktWanifRawCountStatsBroadcastPkts_Type())
tnPktWanifRawCountStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsBroadcastPkts.setStatus(_A)
_TnPktWanifRawCountStatsMulticastPkts_Type=Counter64
_TnPktWanifRawCountStatsMulticastPkts_Object=MibTableColumn
tnPktWanifRawCountStatsMulticastPkts=_TnPktWanifRawCountStatsMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,21),_TnPktWanifRawCountStatsMulticastPkts_Type())
tnPktWanifRawCountStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsMulticastPkts.setStatus(_A)
_TnPktWanifRawCountStatsCRCAlignErrors_Type=Counter64
_TnPktWanifRawCountStatsCRCAlignErrors_Object=MibTableColumn
tnPktWanifRawCountStatsCRCAlignErrors=_TnPktWanifRawCountStatsCRCAlignErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,22),_TnPktWanifRawCountStatsCRCAlignErrors_Type())
tnPktWanifRawCountStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsCRCAlignErrors.setStatus(_A)
_TnPktWanifRawCountStatsUndersizePkts_Type=Counter64
_TnPktWanifRawCountStatsUndersizePkts_Object=MibTableColumn
tnPktWanifRawCountStatsUndersizePkts=_TnPktWanifRawCountStatsUndersizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,23),_TnPktWanifRawCountStatsUndersizePkts_Type())
tnPktWanifRawCountStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsUndersizePkts.setStatus(_A)
_TnPktWanifRawCountStatsOversizePkts_Type=Counter64
_TnPktWanifRawCountStatsOversizePkts_Object=MibTableColumn
tnPktWanifRawCountStatsOversizePkts=_TnPktWanifRawCountStatsOversizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,24),_TnPktWanifRawCountStatsOversizePkts_Type())
tnPktWanifRawCountStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsOversizePkts.setStatus(_A)
_TnPktWanifRawCountStatsFragments_Type=Counter64
_TnPktWanifRawCountStatsFragments_Object=MibTableColumn
tnPktWanifRawCountStatsFragments=_TnPktWanifRawCountStatsFragments_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,25),_TnPktWanifRawCountStatsFragments_Type())
tnPktWanifRawCountStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsFragments.setStatus(_A)
_TnPktWanifRawCountStatsJabbers_Type=Counter64
_TnPktWanifRawCountStatsJabbers_Object=MibTableColumn
tnPktWanifRawCountStatsJabbers=_TnPktWanifRawCountStatsJabbers_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,26),_TnPktWanifRawCountStatsJabbers_Type())
tnPktWanifRawCountStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsJabbers.setStatus(_A)
_TnPktWanifRawCountStatsCollisions_Type=Counter64
_TnPktWanifRawCountStatsCollisions_Object=MibTableColumn
tnPktWanifRawCountStatsCollisions=_TnPktWanifRawCountStatsCollisions_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,27),_TnPktWanifRawCountStatsCollisions_Type())
tnPktWanifRawCountStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsCollisions.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPkts_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPkts_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPkts=_TnPktWanifRawCountStatsHighCapacityPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,28),_TnPktWanifRawCountStatsHighCapacityPkts_Type())
tnPktWanifRawCountStatsHighCapacityPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPkts.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityOctets_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityOctets_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityOctets=_TnPktWanifRawCountStatsHighCapacityOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,29),_TnPktWanifRawCountStatsHighCapacityOctets_Type())
tnPktWanifRawCountStatsHighCapacityOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityOctets.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPktsSize64_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize64_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize64=_TnPktWanifRawCountStatsHighCapacityPktsSize64_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,30),_TnPktWanifRawCountStatsHighCapacityPktsSize64_Type())
tnPktWanifRawCountStatsHighCapacityPktsSize64.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPktsSize64.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize65to127=_TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,31),_TnPktWanifRawCountStatsHighCapacityPktsSize65to127_Type())
tnPktWanifRawCountStatsHighCapacityPktsSize65to127.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPktsSize65to127.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize128to255=_TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,32),_TnPktWanifRawCountStatsHighCapacityPktsSize128to255_Type())
tnPktWanifRawCountStatsHighCapacityPktsSize128to255.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPktsSize128to255.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize256to511=_TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,33),_TnPktWanifRawCountStatsHighCapacityPktsSize256to511_Type())
tnPktWanifRawCountStatsHighCapacityPktsSize256to511.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPktsSize256to511.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize512to1023=_TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,34),_TnPktWanifRawCountStatsHighCapacityPktsSize512to1023_Type())
tnPktWanifRawCountStatsHighCapacityPktsSize512to1023.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPktsSize512to1023.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518=_TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,35),_TnPktWanifRawCountStatsHighCapacityPktsSize1024to1518_Type())
tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518.setStatus(_A)
_TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Type=Counter64
_TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Object=MibTableColumn
tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax=_TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,36),_TnPktWanifRawCountStatsHighCapacityPktsSize1519toMax_Type())
tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax.setStatus(_A)
_TnPktWanifRawCountStatsTooLongFrames_Type=Counter64
_TnPktWanifRawCountStatsTooLongFrames_Object=MibTableColumn
tnPktWanifRawCountStatsTooLongFrames=_TnPktWanifRawCountStatsTooLongFrames_Object((1,3,6,1,4,1,7483,6,1,2,99,24,1,37),_TnPktWanifRawCountStatsTooLongFrames_Type())
tnPktWanifRawCountStatsTooLongFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPktWanifRawCountStatsTooLongFrames.setStatus(_A)
_TnRoeStatsAttributeTotal_Type=Integer32
_TnRoeStatsAttributeTotal_Object=MibScalar
tnRoeStatsAttributeTotal=_TnRoeStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,25),_TnRoeStatsAttributeTotal_Type())
tnRoeStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeStatsAttributeTotal.setStatus(_A)
_TnRoeStatsTable_Object=MibTable
tnRoeStatsTable=_TnRoeStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,26))
if mibBuilder.loadTexts:tnRoeStatsTable.setStatus(_A)
_TnRoeStatsEntry_Object=MibTableRow
tnRoeStatsEntry=_TnRoeStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1))
tnRoeStatsEntry.setIndexNames((0,_C,_q),(0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:tnRoeStatsEntry.setStatus(_A)
_TnRoeStatsPortId_Type=TmnxPortID
_TnRoeStatsPortId_Object=MibTableColumn
tnRoeStatsPortId=_TnRoeStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1,1),_TnRoeStatsPortId_Type())
tnRoeStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeStatsPortId.setStatus(_A)
_TnRoeStatsInterval_Type=AluWdmStatsIntervalType
_TnRoeStatsInterval_Object=MibTableColumn
tnRoeStatsInterval=_TnRoeStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1,2),_TnRoeStatsInterval_Type())
tnRoeStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeStatsInterval.setStatus(_A)
_TnRoeStatsBin_Type=AluWdmStatsBinNumber
_TnRoeStatsBin_Object=MibTableColumn
tnRoeStatsBin=_TnRoeStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1,3),_TnRoeStatsBin_Type())
tnRoeStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeStatsBin.setStatus(_A)
_TnRoeStatsBinStatus_Type=AluWdmStatsBinStatus
_TnRoeStatsBinStatus_Object=MibTableColumn
tnRoeStatsBinStatus=_TnRoeStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1,4),_TnRoeStatsBinStatus_Type())
tnRoeStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeStatsBinStatus.setStatus(_A)
_TnRoeStatsStartTime_Type=DateAndTime
_TnRoeStatsStartTime_Object=MibTableColumn
tnRoeStatsStartTime=_TnRoeStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1,5),_TnRoeStatsStartTime_Type())
tnRoeStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeStatsStartTime.setStatus(_A)
_TnRoeStatsTotalMembers_Type=Integer32
_TnRoeStatsTotalMembers_Object=MibTableColumn
tnRoeStatsTotalMembers=_TnRoeStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1,6),_TnRoeStatsTotalMembers_Type())
tnRoeStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeStatsTotalMembers.setStatus(_A)
_TnRoeStatsDecapPktsDropped_Type=Counter64
_TnRoeStatsDecapPktsDropped_Object=MibTableColumn
tnRoeStatsDecapPktsDropped=_TnRoeStatsDecapPktsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,26,1,8),_TnRoeStatsDecapPktsDropped_Type())
tnRoeStatsDecapPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeStatsDecapPktsDropped.setStatus(_A)
_TnRoeMapperStatsAttributeTotal_Type=Integer32
_TnRoeMapperStatsAttributeTotal_Object=MibScalar
tnRoeMapperStatsAttributeTotal=_TnRoeMapperStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,27),_TnRoeMapperStatsAttributeTotal_Type())
tnRoeMapperStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsAttributeTotal.setStatus(_A)
_TnRoeMapperStatsTable_Object=MibTable
tnRoeMapperStatsTable=_TnRoeMapperStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,28))
if mibBuilder.loadTexts:tnRoeMapperStatsTable.setStatus(_A)
_TnRoeMapperStatsEntry_Object=MibTableRow
tnRoeMapperStatsEntry=_TnRoeMapperStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1))
tnRoeMapperStatsEntry.setIndexNames((0,_C,_t),(0,_C,_u),(0,_C,_v),(0,_C,_w))
if mibBuilder.loadTexts:tnRoeMapperStatsEntry.setStatus(_A)
_TnRoeMapperStatsPortId_Type=TmnxPortID
_TnRoeMapperStatsPortId_Object=MibTableColumn
tnRoeMapperStatsPortId=_TnRoeMapperStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,1),_TnRoeMapperStatsPortId_Type())
tnRoeMapperStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeMapperStatsPortId.setStatus(_A)
class _TnRoeMapperStatsMapperID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeMapperStatsMapperID_Type.__name__=_E
_TnRoeMapperStatsMapperID_Object=MibTableColumn
tnRoeMapperStatsMapperID=_TnRoeMapperStatsMapperID_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,2),_TnRoeMapperStatsMapperID_Type())
tnRoeMapperStatsMapperID.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeMapperStatsMapperID.setStatus(_A)
_TnRoeMapperStatsInterval_Type=AluWdmStatsIntervalType
_TnRoeMapperStatsInterval_Object=MibTableColumn
tnRoeMapperStatsInterval=_TnRoeMapperStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,3),_TnRoeMapperStatsInterval_Type())
tnRoeMapperStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeMapperStatsInterval.setStatus(_A)
_TnRoeMapperStatsBin_Type=AluWdmStatsBinNumber
_TnRoeMapperStatsBin_Object=MibTableColumn
tnRoeMapperStatsBin=_TnRoeMapperStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,4),_TnRoeMapperStatsBin_Type())
tnRoeMapperStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeMapperStatsBin.setStatus(_A)
_TnRoeMapperStatsBinStatus_Type=AluWdmStatsBinStatus
_TnRoeMapperStatsBinStatus_Object=MibTableColumn
tnRoeMapperStatsBinStatus=_TnRoeMapperStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,5),_TnRoeMapperStatsBinStatus_Type())
tnRoeMapperStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsBinStatus.setStatus(_A)
_TnRoeMapperStatsStartTime_Type=DateAndTime
_TnRoeMapperStatsStartTime_Object=MibTableColumn
tnRoeMapperStatsStartTime=_TnRoeMapperStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,6),_TnRoeMapperStatsStartTime_Type())
tnRoeMapperStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsStartTime.setStatus(_A)
_TnRoeMapperStatsTotalMembers_Type=Integer32
_TnRoeMapperStatsTotalMembers_Object=MibTableColumn
tnRoeMapperStatsTotalMembers=_TnRoeMapperStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,7),_TnRoeMapperStatsTotalMembers_Type())
tnRoeMapperStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsTotalMembers.setStatus(_A)
_TnRoeMapperStatsTxpackets_Type=Counter64
_TnRoeMapperStatsTxpackets_Object=MibTableColumn
tnRoeMapperStatsTxpackets=_TnRoeMapperStatsTxpackets_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,13),_TnRoeMapperStatsTxpackets_Type())
tnRoeMapperStatsTxpackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsTxpackets.setStatus(_A)
_TnRoeMapperStatsTxbytes_Type=Counter64
_TnRoeMapperStatsTxbytes_Object=MibTableColumn
tnRoeMapperStatsTxbytes=_TnRoeMapperStatsTxbytes_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,14),_TnRoeMapperStatsTxbytes_Type())
tnRoeMapperStatsTxbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsTxbytes.setStatus(_A)
_TnRoeMapperStatsTxDropPackets_Type=Counter64
_TnRoeMapperStatsTxDropPackets_Object=MibTableColumn
tnRoeMapperStatsTxDropPackets=_TnRoeMapperStatsTxDropPackets_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,15),_TnRoeMapperStatsTxDropPackets_Type())
tnRoeMapperStatsTxDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsTxDropPackets.setStatus(_A)
_TnRoeMapperStatsEncapQueueOverrun_Type=Counter64
_TnRoeMapperStatsEncapQueueOverrun_Object=MibTableColumn
tnRoeMapperStatsEncapQueueOverrun=_TnRoeMapperStatsEncapQueueOverrun_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,16),_TnRoeMapperStatsEncapQueueOverrun_Type())
tnRoeMapperStatsEncapQueueOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsEncapQueueOverrun.setStatus(_A)
_TnRoeMapperStatsGSMTimeSlotMismatch_Type=Counter64
_TnRoeMapperStatsGSMTimeSlotMismatch_Object=MibTableColumn
tnRoeMapperStatsGSMTimeSlotMismatch=_TnRoeMapperStatsGSMTimeSlotMismatch_Object((1,3,6,1,4,1,7483,6,1,2,99,28,1,17),_TnRoeMapperStatsGSMTimeSlotMismatch_Type())
tnRoeMapperStatsGSMTimeSlotMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperStatsGSMTimeSlotMismatch.setStatus(_A)
_TnRoeDeMapperStatsAttributeTotal_Type=Integer32
_TnRoeDeMapperStatsAttributeTotal_Object=MibScalar
tnRoeDeMapperStatsAttributeTotal=_TnRoeDeMapperStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,29),_TnRoeDeMapperStatsAttributeTotal_Type())
tnRoeDeMapperStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsAttributeTotal.setStatus(_A)
_TnRoeDeMapperStatsTable_Object=MibTable
tnRoeDeMapperStatsTable=_TnRoeDeMapperStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,30))
if mibBuilder.loadTexts:tnRoeDeMapperStatsTable.setStatus(_A)
_TnRoeDeMapperStatsEntry_Object=MibTableRow
tnRoeDeMapperStatsEntry=_TnRoeDeMapperStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1))
tnRoeDeMapperStatsEntry.setIndexNames((0,_C,_x),(0,_C,_y),(0,_C,_z),(0,_C,_A0))
if mibBuilder.loadTexts:tnRoeDeMapperStatsEntry.setStatus(_A)
_TnRoeDeMapperStatsPortId_Type=TmnxPortID
_TnRoeDeMapperStatsPortId_Object=MibTableColumn
tnRoeDeMapperStatsPortId=_TnRoeDeMapperStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,1),_TnRoeDeMapperStatsPortId_Type())
tnRoeDeMapperStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeDeMapperStatsPortId.setStatus(_A)
class _TnRoeDeMapperStatsDeMapperID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeDeMapperStatsDeMapperID_Type.__name__=_E
_TnRoeDeMapperStatsDeMapperID_Object=MibTableColumn
tnRoeDeMapperStatsDeMapperID=_TnRoeDeMapperStatsDeMapperID_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,2),_TnRoeDeMapperStatsDeMapperID_Type())
tnRoeDeMapperStatsDeMapperID.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeDeMapperStatsDeMapperID.setStatus(_A)
_TnRoeDeMapperStatsInterval_Type=AluWdmStatsIntervalType
_TnRoeDeMapperStatsInterval_Object=MibTableColumn
tnRoeDeMapperStatsInterval=_TnRoeDeMapperStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,3),_TnRoeDeMapperStatsInterval_Type())
tnRoeDeMapperStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeDeMapperStatsInterval.setStatus(_A)
_TnRoeDeMapperStatsBin_Type=AluWdmStatsBinNumber
_TnRoeDeMapperStatsBin_Object=MibTableColumn
tnRoeDeMapperStatsBin=_TnRoeDeMapperStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,4),_TnRoeDeMapperStatsBin_Type())
tnRoeDeMapperStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeDeMapperStatsBin.setStatus(_A)
_TnRoeDeMapperStatsBinStatus_Type=AluWdmStatsBinStatus
_TnRoeDeMapperStatsBinStatus_Object=MibTableColumn
tnRoeDeMapperStatsBinStatus=_TnRoeDeMapperStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,5),_TnRoeDeMapperStatsBinStatus_Type())
tnRoeDeMapperStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsBinStatus.setStatus(_A)
_TnRoeDeMapperStatsStartTime_Type=DateAndTime
_TnRoeDeMapperStatsStartTime_Object=MibTableColumn
tnRoeDeMapperStatsStartTime=_TnRoeDeMapperStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,6),_TnRoeDeMapperStatsStartTime_Type())
tnRoeDeMapperStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsStartTime.setStatus(_A)
_TnRoeDeMapperStatsTotalMembers_Type=Integer32
_TnRoeDeMapperStatsTotalMembers_Object=MibTableColumn
tnRoeDeMapperStatsTotalMembers=_TnRoeDeMapperStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,7),_TnRoeDeMapperStatsTotalMembers_Type())
tnRoeDeMapperStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsTotalMembers.setStatus(_A)
_TnRoeDeMapperStatsRxpackets_Type=Counter64
_TnRoeDeMapperStatsRxpackets_Object=MibTableColumn
tnRoeDeMapperStatsRxpackets=_TnRoeDeMapperStatsRxpackets_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,14),_TnRoeDeMapperStatsRxpackets_Type())
tnRoeDeMapperStatsRxpackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsRxpackets.setStatus(_A)
_TnRoeDeMapperStatsRxbytes_Type=Counter64
_TnRoeDeMapperStatsRxbytes_Object=MibTableColumn
tnRoeDeMapperStatsRxbytes=_TnRoeDeMapperStatsRxbytes_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,15),_TnRoeDeMapperStatsRxbytes_Type())
tnRoeDeMapperStatsRxbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsRxbytes.setStatus(_A)
_TnRoeDeMapperStatsDecapQueueOverrun_Type=Counter64
_TnRoeDeMapperStatsDecapQueueOverrun_Object=MibTableColumn
tnRoeDeMapperStatsDecapQueueOverrun=_TnRoeDeMapperStatsDecapQueueOverrun_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,16),_TnRoeDeMapperStatsDecapQueueOverrun_Type())
tnRoeDeMapperStatsDecapQueueOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsDecapQueueOverrun.setStatus(_A)
_TnRoeDeMapperStatsQueueUnderrun_Type=Counter64
_TnRoeDeMapperStatsQueueUnderrun_Object=MibTableColumn
tnRoeDeMapperStatsQueueUnderrun=_TnRoeDeMapperStatsQueueUnderrun_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,17),_TnRoeDeMapperStatsQueueUnderrun_Type())
tnRoeDeMapperStatsQueueUnderrun.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsQueueUnderrun.setStatus(_A)
_TnRoeDeMapperStatsDecapPacketMissing_Type=Counter64
_TnRoeDeMapperStatsDecapPacketMissing_Object=MibTableColumn
tnRoeDeMapperStatsDecapPacketMissing=_TnRoeDeMapperStatsDecapPacketMissing_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,18),_TnRoeDeMapperStatsDecapPacketMissing_Type())
tnRoeDeMapperStatsDecapPacketMissing.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsDecapPacketMissing.setStatus(_A)
_TnRoeDeMapperStatsDecapPacketSizeMismatch_Type=Counter64
_TnRoeDeMapperStatsDecapPacketSizeMismatch_Object=MibTableColumn
tnRoeDeMapperStatsDecapPacketSizeMismatch=_TnRoeDeMapperStatsDecapPacketSizeMismatch_Object((1,3,6,1,4,1,7483,6,1,2,99,30,1,19),_TnRoeDeMapperStatsDecapPacketSizeMismatch_Type())
tnRoeDeMapperStatsDecapPacketSizeMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperStatsDecapPacketSizeMismatch.setStatus(_A)
_TnEMACStatsAttributeTotal_Type=Integer32
_TnEMACStatsAttributeTotal_Object=MibScalar
tnEMACStatsAttributeTotal=_TnEMACStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,31),_TnEMACStatsAttributeTotal_Type())
tnEMACStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsAttributeTotal.setStatus(_A)
_TnEMACStatsTable_Object=MibTable
tnEMACStatsTable=_TnEMACStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,32))
if mibBuilder.loadTexts:tnEMACStatsTable.setStatus(_A)
_TnEMACStatsEntry_Object=MibTableRow
tnEMACStatsEntry=_TnEMACStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1))
tnEMACStatsEntry.setIndexNames((0,_C,_A1),(0,_C,_A2),(0,_C,_A3))
if mibBuilder.loadTexts:tnEMACStatsEntry.setStatus(_A)
_TnEMACStatsPortId_Type=TmnxPortID
_TnEMACStatsPortId_Object=MibTableColumn
tnEMACStatsPortId=_TnEMACStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,1),_TnEMACStatsPortId_Type())
tnEMACStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEMACStatsPortId.setStatus(_A)
_TnEMACStatsInterval_Type=AluWdmStatsIntervalType
_TnEMACStatsInterval_Object=MibTableColumn
tnEMACStatsInterval=_TnEMACStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,2),_TnEMACStatsInterval_Type())
tnEMACStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEMACStatsInterval.setStatus(_A)
_TnEMACStatsBin_Type=AluWdmStatsBinNumber
_TnEMACStatsBin_Object=MibTableColumn
tnEMACStatsBin=_TnEMACStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,3),_TnEMACStatsBin_Type())
tnEMACStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnEMACStatsBin.setStatus(_A)
_TnEMACStatsBinStatus_Type=AluWdmStatsBinStatus
_TnEMACStatsBinStatus_Object=MibTableColumn
tnEMACStatsBinStatus=_TnEMACStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,4),_TnEMACStatsBinStatus_Type())
tnEMACStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsBinStatus.setStatus(_A)
_TnEMACStatsStartTime_Type=DateAndTime
_TnEMACStatsStartTime_Object=MibTableColumn
tnEMACStatsStartTime=_TnEMACStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,5),_TnEMACStatsStartTime_Type())
tnEMACStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsStartTime.setStatus(_A)
_TnEMACStatsTotalMembers_Type=Integer32
_TnEMACStatsTotalMembers_Object=MibTableColumn
tnEMACStatsTotalMembers=_TnEMACStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,6),_TnEMACStatsTotalMembers_Type())
tnEMACStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsTotalMembers.setStatus(_A)
_TnEMACStatsIfInOctets_Type=Counter64
_TnEMACStatsIfInOctets_Object=MibTableColumn
tnEMACStatsIfInOctets=_TnEMACStatsIfInOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,7),_TnEMACStatsIfInOctets_Type())
tnEMACStatsIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInOctets.setStatus(_A)
_TnEMACStatsIfInUcastPkts_Type=Counter64
_TnEMACStatsIfInUcastPkts_Object=MibTableColumn
tnEMACStatsIfInUcastPkts=_TnEMACStatsIfInUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,8),_TnEMACStatsIfInUcastPkts_Type())
tnEMACStatsIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInUcastPkts.setStatus(_A)
_TnEMACStatsIfInDiscards_Type=Counter64
_TnEMACStatsIfInDiscards_Object=MibTableColumn
tnEMACStatsIfInDiscards=_TnEMACStatsIfInDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,9),_TnEMACStatsIfInDiscards_Type())
tnEMACStatsIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInDiscards.setStatus(_A)
_TnEMACStatsIfInErrors_Type=Counter64
_TnEMACStatsIfInErrors_Object=MibTableColumn
tnEMACStatsIfInErrors=_TnEMACStatsIfInErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,10),_TnEMACStatsIfInErrors_Type())
tnEMACStatsIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInErrors.setStatus(_A)
_TnEMACStatsIfInUnknownProtos_Type=Counter64
_TnEMACStatsIfInUnknownProtos_Object=MibTableColumn
tnEMACStatsIfInUnknownProtos=_TnEMACStatsIfInUnknownProtos_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,11),_TnEMACStatsIfInUnknownProtos_Type())
tnEMACStatsIfInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInUnknownProtos.setStatus(_A)
_TnEMACStatsIfInMulticastPkts_Type=Counter64
_TnEMACStatsIfInMulticastPkts_Object=MibTableColumn
tnEMACStatsIfInMulticastPkts=_TnEMACStatsIfInMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,12),_TnEMACStatsIfInMulticastPkts_Type())
tnEMACStatsIfInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInMulticastPkts.setStatus(_A)
_TnEMACStatsIfInBroadcastPkts_Type=Counter64
_TnEMACStatsIfInBroadcastPkts_Object=MibTableColumn
tnEMACStatsIfInBroadcastPkts=_TnEMACStatsIfInBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,13),_TnEMACStatsIfInBroadcastPkts_Type())
tnEMACStatsIfInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInBroadcastPkts.setStatus(_A)
_TnEMACStatsIfOutOctets_Type=Counter64
_TnEMACStatsIfOutOctets_Object=MibTableColumn
tnEMACStatsIfOutOctets=_TnEMACStatsIfOutOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,14),_TnEMACStatsIfOutOctets_Type())
tnEMACStatsIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfOutOctets.setStatus(_A)
_TnEMACStatsIfOutUcastPkts_Type=Counter64
_TnEMACStatsIfOutUcastPkts_Object=MibTableColumn
tnEMACStatsIfOutUcastPkts=_TnEMACStatsIfOutUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,15),_TnEMACStatsIfOutUcastPkts_Type())
tnEMACStatsIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfOutUcastPkts.setStatus(_A)
_TnEMACStatsIfOutDiscards_Type=Counter64
_TnEMACStatsIfOutDiscards_Object=MibTableColumn
tnEMACStatsIfOutDiscards=_TnEMACStatsIfOutDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,16),_TnEMACStatsIfOutDiscards_Type())
tnEMACStatsIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfOutDiscards.setStatus(_A)
_TnEMACStatsIfOutErrors_Type=Counter64
_TnEMACStatsIfOutErrors_Object=MibTableColumn
tnEMACStatsIfOutErrors=_TnEMACStatsIfOutErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,17),_TnEMACStatsIfOutErrors_Type())
tnEMACStatsIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfOutErrors.setStatus(_A)
_TnEMACStatsIfOutMulticastPkts_Type=Counter64
_TnEMACStatsIfOutMulticastPkts_Object=MibTableColumn
tnEMACStatsIfOutMulticastPkts=_TnEMACStatsIfOutMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,18),_TnEMACStatsIfOutMulticastPkts_Type())
tnEMACStatsIfOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfOutMulticastPkts.setStatus(_A)
_TnEMACStatsIfOutBroadcastPkts_Type=Counter64
_TnEMACStatsIfOutBroadcastPkts_Object=MibTableColumn
tnEMACStatsIfOutBroadcastPkts=_TnEMACStatsIfOutBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,19),_TnEMACStatsIfOutBroadcastPkts_Type())
tnEMACStatsIfOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfOutBroadcastPkts.setStatus(_A)
_TnEMACStatsIfInPkts_Type=Counter64
_TnEMACStatsIfInPkts_Object=MibTableColumn
tnEMACStatsIfInPkts=_TnEMACStatsIfInPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,20),_TnEMACStatsIfInPkts_Type())
tnEMACStatsIfInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfInPkts.setStatus(_A)
_TnEMACStatsIfOutPkts_Type=Counter64
_TnEMACStatsIfOutPkts_Object=MibTableColumn
tnEMACStatsIfOutPkts=_TnEMACStatsIfOutPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,21),_TnEMACStatsIfOutPkts_Type())
tnEMACStatsIfOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsIfOutPkts.setStatus(_A)
_TnEMACStatsDropEvents_Type=Counter64
_TnEMACStatsDropEvents_Object=MibTableColumn
tnEMACStatsDropEvents=_TnEMACStatsDropEvents_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,22),_TnEMACStatsDropEvents_Type())
tnEMACStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsDropEvents.setStatus(_A)
_TnEMACStatsBroadcastPkts_Type=Counter64
_TnEMACStatsBroadcastPkts_Object=MibTableColumn
tnEMACStatsBroadcastPkts=_TnEMACStatsBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,23),_TnEMACStatsBroadcastPkts_Type())
tnEMACStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsBroadcastPkts.setStatus(_A)
_TnEMACStatsMulticastPkts_Type=Counter64
_TnEMACStatsMulticastPkts_Object=MibTableColumn
tnEMACStatsMulticastPkts=_TnEMACStatsMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,24),_TnEMACStatsMulticastPkts_Type())
tnEMACStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsMulticastPkts.setStatus(_A)
_TnEMACStatsCRCAlignErrors_Type=Counter64
_TnEMACStatsCRCAlignErrors_Object=MibTableColumn
tnEMACStatsCRCAlignErrors=_TnEMACStatsCRCAlignErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,25),_TnEMACStatsCRCAlignErrors_Type())
tnEMACStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsCRCAlignErrors.setStatus(_A)
_TnEMACStatsUndersizePkts_Type=Counter64
_TnEMACStatsUndersizePkts_Object=MibTableColumn
tnEMACStatsUndersizePkts=_TnEMACStatsUndersizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,26),_TnEMACStatsUndersizePkts_Type())
tnEMACStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsUndersizePkts.setStatus(_A)
_TnEMACStatsOversizePkts_Type=Counter64
_TnEMACStatsOversizePkts_Object=MibTableColumn
tnEMACStatsOversizePkts=_TnEMACStatsOversizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,27),_TnEMACStatsOversizePkts_Type())
tnEMACStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsOversizePkts.setStatus(_A)
_TnEMACStatsFragments_Type=Counter64
_TnEMACStatsFragments_Object=MibTableColumn
tnEMACStatsFragments=_TnEMACStatsFragments_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,28),_TnEMACStatsFragments_Type())
tnEMACStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsFragments.setStatus(_A)
_TnEMACStatsJabbers_Type=Counter64
_TnEMACStatsJabbers_Object=MibTableColumn
tnEMACStatsJabbers=_TnEMACStatsJabbers_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,29),_TnEMACStatsJabbers_Type())
tnEMACStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsJabbers.setStatus(_A)
_TnEMACStatsCollisions_Type=Counter64
_TnEMACStatsCollisions_Object=MibTableColumn
tnEMACStatsCollisions=_TnEMACStatsCollisions_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,30),_TnEMACStatsCollisions_Type())
tnEMACStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsCollisions.setStatus(_A)
_TnEMACStatsHighCapacityPkts_Type=Counter64
_TnEMACStatsHighCapacityPkts_Object=MibTableColumn
tnEMACStatsHighCapacityPkts=_TnEMACStatsHighCapacityPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,31),_TnEMACStatsHighCapacityPkts_Type())
tnEMACStatsHighCapacityPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts.setStatus(_A)
_TnEMACStatsHighCapacityOctets_Type=Counter64
_TnEMACStatsHighCapacityOctets_Object=MibTableColumn
tnEMACStatsHighCapacityOctets=_TnEMACStatsHighCapacityOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,32),_TnEMACStatsHighCapacityOctets_Type())
tnEMACStatsHighCapacityOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityOctets.setStatus(_A)
_TnEMACStatsHighCapacityPkts64Octets_Type=Counter64
_TnEMACStatsHighCapacityPkts64Octets_Object=MibTableColumn
tnEMACStatsHighCapacityPkts64Octets=_TnEMACStatsHighCapacityPkts64Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,33),_TnEMACStatsHighCapacityPkts64Octets_Type())
tnEMACStatsHighCapacityPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts64Octets.setStatus(_A)
_TnEMACStatsHighCapacityPkts65to127Octets_Type=Counter64
_TnEMACStatsHighCapacityPkts65to127Octets_Object=MibTableColumn
tnEMACStatsHighCapacityPkts65to127Octets=_TnEMACStatsHighCapacityPkts65to127Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,34),_TnEMACStatsHighCapacityPkts65to127Octets_Type())
tnEMACStatsHighCapacityPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts65to127Octets.setStatus(_A)
_TnEMACStatsHighCapacityPkts128to255Octets_Type=Counter64
_TnEMACStatsHighCapacityPkts128to255Octets_Object=MibTableColumn
tnEMACStatsHighCapacityPkts128to255Octets=_TnEMACStatsHighCapacityPkts128to255Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,35),_TnEMACStatsHighCapacityPkts128to255Octets_Type())
tnEMACStatsHighCapacityPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts128to255Octets.setStatus(_A)
_TnEMACStatsHighCapacityPkts256to511Octets_Type=Counter64
_TnEMACStatsHighCapacityPkts256to511Octets_Object=MibTableColumn
tnEMACStatsHighCapacityPkts256to511Octets=_TnEMACStatsHighCapacityPkts256to511Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,36),_TnEMACStatsHighCapacityPkts256to511Octets_Type())
tnEMACStatsHighCapacityPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts256to511Octets.setStatus(_A)
_TnEMACStatsHighCapacityPkts512to1023Octets_Type=Counter64
_TnEMACStatsHighCapacityPkts512to1023Octets_Object=MibTableColumn
tnEMACStatsHighCapacityPkts512to1023Octets=_TnEMACStatsHighCapacityPkts512to1023Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,37),_TnEMACStatsHighCapacityPkts512to1023Octets_Type())
tnEMACStatsHighCapacityPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts512to1023Octets.setStatus(_A)
_TnEMACStatsHighCapacityPkts1024to1518Octets_Type=Counter64
_TnEMACStatsHighCapacityPkts1024to1518Octets_Object=MibTableColumn
tnEMACStatsHighCapacityPkts1024to1518Octets=_TnEMACStatsHighCapacityPkts1024to1518Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,38),_TnEMACStatsHighCapacityPkts1024to1518Octets_Type())
tnEMACStatsHighCapacityPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts1024to1518Octets.setStatus(_A)
_TnEMACStatsHighCapacityPkts1519toMaxOctets_Type=Counter64
_TnEMACStatsHighCapacityPkts1519toMaxOctets_Object=MibTableColumn
tnEMACStatsHighCapacityPkts1519toMaxOctets=_TnEMACStatsHighCapacityPkts1519toMaxOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,32,1,39),_TnEMACStatsHighCapacityPkts1519toMaxOctets_Type())
tnEMACStatsHighCapacityPkts1519toMaxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnEMACStatsHighCapacityPkts1519toMaxOctets.setStatus(_A)
_TnPMACStatsAttributeTotal_Type=Integer32
_TnPMACStatsAttributeTotal_Object=MibScalar
tnPMACStatsAttributeTotal=_TnPMACStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,33),_TnPMACStatsAttributeTotal_Type())
tnPMACStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsAttributeTotal.setStatus(_A)
_TnPMACStatsTable_Object=MibTable
tnPMACStatsTable=_TnPMACStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,34))
if mibBuilder.loadTexts:tnPMACStatsTable.setStatus(_A)
_TnPMACStatsEntry_Object=MibTableRow
tnPMACStatsEntry=_TnPMACStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1))
tnPMACStatsEntry.setIndexNames((0,_C,_A4),(0,_C,_A5),(0,_C,_A6))
if mibBuilder.loadTexts:tnPMACStatsEntry.setStatus(_A)
_TnPMACStatsPortId_Type=TmnxPortID
_TnPMACStatsPortId_Object=MibTableColumn
tnPMACStatsPortId=_TnPMACStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,1),_TnPMACStatsPortId_Type())
tnPMACStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPMACStatsPortId.setStatus(_A)
_TnPMACStatsInterval_Type=AluWdmStatsIntervalType
_TnPMACStatsInterval_Object=MibTableColumn
tnPMACStatsInterval=_TnPMACStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,2),_TnPMACStatsInterval_Type())
tnPMACStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPMACStatsInterval.setStatus(_A)
_TnPMACStatsBin_Type=AluWdmStatsBinNumber
_TnPMACStatsBin_Object=MibTableColumn
tnPMACStatsBin=_TnPMACStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,3),_TnPMACStatsBin_Type())
tnPMACStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnPMACStatsBin.setStatus(_A)
_TnPMACStatsBinStatus_Type=AluWdmStatsBinStatus
_TnPMACStatsBinStatus_Object=MibTableColumn
tnPMACStatsBinStatus=_TnPMACStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,4),_TnPMACStatsBinStatus_Type())
tnPMACStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsBinStatus.setStatus(_A)
_TnPMACStatsStartTime_Type=DateAndTime
_TnPMACStatsStartTime_Object=MibTableColumn
tnPMACStatsStartTime=_TnPMACStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,5),_TnPMACStatsStartTime_Type())
tnPMACStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsStartTime.setStatus(_A)
_TnPMACStatsTotalMembers_Type=Integer32
_TnPMACStatsTotalMembers_Object=MibTableColumn
tnPMACStatsTotalMembers=_TnPMACStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,6),_TnPMACStatsTotalMembers_Type())
tnPMACStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsTotalMembers.setStatus(_A)
_TnPMACStatsIfInOctets_Type=Counter64
_TnPMACStatsIfInOctets_Object=MibTableColumn
tnPMACStatsIfInOctets=_TnPMACStatsIfInOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,7),_TnPMACStatsIfInOctets_Type())
tnPMACStatsIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInOctets.setStatus(_A)
_TnPMACStatsIfInUcastPkts_Type=Counter64
_TnPMACStatsIfInUcastPkts_Object=MibTableColumn
tnPMACStatsIfInUcastPkts=_TnPMACStatsIfInUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,8),_TnPMACStatsIfInUcastPkts_Type())
tnPMACStatsIfInUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInUcastPkts.setStatus(_A)
_TnPMACStatsIfInDiscards_Type=Counter64
_TnPMACStatsIfInDiscards_Object=MibTableColumn
tnPMACStatsIfInDiscards=_TnPMACStatsIfInDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,9),_TnPMACStatsIfInDiscards_Type())
tnPMACStatsIfInDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInDiscards.setStatus(_A)
_TnPMACStatsIfInErrors_Type=Counter64
_TnPMACStatsIfInErrors_Object=MibTableColumn
tnPMACStatsIfInErrors=_TnPMACStatsIfInErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,10),_TnPMACStatsIfInErrors_Type())
tnPMACStatsIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInErrors.setStatus(_A)
_TnPMACStatsIfInUnknownProtos_Type=Counter64
_TnPMACStatsIfInUnknownProtos_Object=MibTableColumn
tnPMACStatsIfInUnknownProtos=_TnPMACStatsIfInUnknownProtos_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,11),_TnPMACStatsIfInUnknownProtos_Type())
tnPMACStatsIfInUnknownProtos.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInUnknownProtos.setStatus(_A)
_TnPMACStatsIfInMulticastPkts_Type=Counter64
_TnPMACStatsIfInMulticastPkts_Object=MibTableColumn
tnPMACStatsIfInMulticastPkts=_TnPMACStatsIfInMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,12),_TnPMACStatsIfInMulticastPkts_Type())
tnPMACStatsIfInMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInMulticastPkts.setStatus(_A)
_TnPMACStatsIfInBroadcastPkts_Type=Counter64
_TnPMACStatsIfInBroadcastPkts_Object=MibTableColumn
tnPMACStatsIfInBroadcastPkts=_TnPMACStatsIfInBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,13),_TnPMACStatsIfInBroadcastPkts_Type())
tnPMACStatsIfInBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInBroadcastPkts.setStatus(_A)
_TnPMACStatsIfOutOctets_Type=Counter64
_TnPMACStatsIfOutOctets_Object=MibTableColumn
tnPMACStatsIfOutOctets=_TnPMACStatsIfOutOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,14),_TnPMACStatsIfOutOctets_Type())
tnPMACStatsIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfOutOctets.setStatus(_A)
_TnPMACStatsIfOutUcastPkts_Type=Counter64
_TnPMACStatsIfOutUcastPkts_Object=MibTableColumn
tnPMACStatsIfOutUcastPkts=_TnPMACStatsIfOutUcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,15),_TnPMACStatsIfOutUcastPkts_Type())
tnPMACStatsIfOutUcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfOutUcastPkts.setStatus(_A)
_TnPMACStatsIfOutDiscards_Type=Counter64
_TnPMACStatsIfOutDiscards_Object=MibTableColumn
tnPMACStatsIfOutDiscards=_TnPMACStatsIfOutDiscards_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,16),_TnPMACStatsIfOutDiscards_Type())
tnPMACStatsIfOutDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfOutDiscards.setStatus(_A)
_TnPMACStatsIfOutErrors_Type=Counter64
_TnPMACStatsIfOutErrors_Object=MibTableColumn
tnPMACStatsIfOutErrors=_TnPMACStatsIfOutErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,17),_TnPMACStatsIfOutErrors_Type())
tnPMACStatsIfOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfOutErrors.setStatus(_A)
_TnPMACStatsIfOutMulticastPkts_Type=Counter64
_TnPMACStatsIfOutMulticastPkts_Object=MibTableColumn
tnPMACStatsIfOutMulticastPkts=_TnPMACStatsIfOutMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,18),_TnPMACStatsIfOutMulticastPkts_Type())
tnPMACStatsIfOutMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfOutMulticastPkts.setStatus(_A)
_TnPMACStatsIfOutBroadcastPkts_Type=Counter64
_TnPMACStatsIfOutBroadcastPkts_Object=MibTableColumn
tnPMACStatsIfOutBroadcastPkts=_TnPMACStatsIfOutBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,19),_TnPMACStatsIfOutBroadcastPkts_Type())
tnPMACStatsIfOutBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfOutBroadcastPkts.setStatus(_A)
_TnPMACStatsIfInPkts_Type=Counter64
_TnPMACStatsIfInPkts_Object=MibTableColumn
tnPMACStatsIfInPkts=_TnPMACStatsIfInPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,20),_TnPMACStatsIfInPkts_Type())
tnPMACStatsIfInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfInPkts.setStatus(_A)
_TnPMACStatsIfOutPkts_Type=Counter64
_TnPMACStatsIfOutPkts_Object=MibTableColumn
tnPMACStatsIfOutPkts=_TnPMACStatsIfOutPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,21),_TnPMACStatsIfOutPkts_Type())
tnPMACStatsIfOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsIfOutPkts.setStatus(_A)
_TnPMACStatsDropEvents_Type=Counter64
_TnPMACStatsDropEvents_Object=MibTableColumn
tnPMACStatsDropEvents=_TnPMACStatsDropEvents_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,22),_TnPMACStatsDropEvents_Type())
tnPMACStatsDropEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsDropEvents.setStatus(_A)
_TnPMACStatsBroadcastPkts_Type=Counter64
_TnPMACStatsBroadcastPkts_Object=MibTableColumn
tnPMACStatsBroadcastPkts=_TnPMACStatsBroadcastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,23),_TnPMACStatsBroadcastPkts_Type())
tnPMACStatsBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsBroadcastPkts.setStatus(_A)
_TnPMACStatsMulticastPkts_Type=Counter64
_TnPMACStatsMulticastPkts_Object=MibTableColumn
tnPMACStatsMulticastPkts=_TnPMACStatsMulticastPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,24),_TnPMACStatsMulticastPkts_Type())
tnPMACStatsMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsMulticastPkts.setStatus(_A)
_TnPMACStatsCRCAlignErrors_Type=Counter64
_TnPMACStatsCRCAlignErrors_Object=MibTableColumn
tnPMACStatsCRCAlignErrors=_TnPMACStatsCRCAlignErrors_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,25),_TnPMACStatsCRCAlignErrors_Type())
tnPMACStatsCRCAlignErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsCRCAlignErrors.setStatus(_A)
_TnPMACStatsUndersizePkts_Type=Counter64
_TnPMACStatsUndersizePkts_Object=MibTableColumn
tnPMACStatsUndersizePkts=_TnPMACStatsUndersizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,26),_TnPMACStatsUndersizePkts_Type())
tnPMACStatsUndersizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsUndersizePkts.setStatus(_A)
_TnPMACStatsOversizePkts_Type=Counter64
_TnPMACStatsOversizePkts_Object=MibTableColumn
tnPMACStatsOversizePkts=_TnPMACStatsOversizePkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,27),_TnPMACStatsOversizePkts_Type())
tnPMACStatsOversizePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsOversizePkts.setStatus(_A)
_TnPMACStatsFragments_Type=Counter64
_TnPMACStatsFragments_Object=MibTableColumn
tnPMACStatsFragments=_TnPMACStatsFragments_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,28),_TnPMACStatsFragments_Type())
tnPMACStatsFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsFragments.setStatus(_A)
_TnPMACStatsJabbers_Type=Counter64
_TnPMACStatsJabbers_Object=MibTableColumn
tnPMACStatsJabbers=_TnPMACStatsJabbers_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,29),_TnPMACStatsJabbers_Type())
tnPMACStatsJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsJabbers.setStatus(_A)
_TnPMACStatsCollisions_Type=Counter64
_TnPMACStatsCollisions_Object=MibTableColumn
tnPMACStatsCollisions=_TnPMACStatsCollisions_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,30),_TnPMACStatsCollisions_Type())
tnPMACStatsCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsCollisions.setStatus(_A)
_TnPMACStatsHighCapacityPkts_Type=Counter64
_TnPMACStatsHighCapacityPkts_Object=MibTableColumn
tnPMACStatsHighCapacityPkts=_TnPMACStatsHighCapacityPkts_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,31),_TnPMACStatsHighCapacityPkts_Type())
tnPMACStatsHighCapacityPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts.setStatus(_A)
_TnPMACStatsHighCapacityOctets_Type=Counter64
_TnPMACStatsHighCapacityOctets_Object=MibTableColumn
tnPMACStatsHighCapacityOctets=_TnPMACStatsHighCapacityOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,32),_TnPMACStatsHighCapacityOctets_Type())
tnPMACStatsHighCapacityOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityOctets.setStatus(_A)
_TnPMACStatsHighCapacityPkts64Octets_Type=Counter64
_TnPMACStatsHighCapacityPkts64Octets_Object=MibTableColumn
tnPMACStatsHighCapacityPkts64Octets=_TnPMACStatsHighCapacityPkts64Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,33),_TnPMACStatsHighCapacityPkts64Octets_Type())
tnPMACStatsHighCapacityPkts64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts64Octets.setStatus(_A)
_TnPMACStatsHighCapacityPkts65to127Octets_Type=Counter64
_TnPMACStatsHighCapacityPkts65to127Octets_Object=MibTableColumn
tnPMACStatsHighCapacityPkts65to127Octets=_TnPMACStatsHighCapacityPkts65to127Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,34),_TnPMACStatsHighCapacityPkts65to127Octets_Type())
tnPMACStatsHighCapacityPkts65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts65to127Octets.setStatus(_A)
_TnPMACStatsHighCapacityPkts128to255Octets_Type=Counter64
_TnPMACStatsHighCapacityPkts128to255Octets_Object=MibTableColumn
tnPMACStatsHighCapacityPkts128to255Octets=_TnPMACStatsHighCapacityPkts128to255Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,35),_TnPMACStatsHighCapacityPkts128to255Octets_Type())
tnPMACStatsHighCapacityPkts128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts128to255Octets.setStatus(_A)
_TnPMACStatsHighCapacityPkts256to511Octets_Type=Counter64
_TnPMACStatsHighCapacityPkts256to511Octets_Object=MibTableColumn
tnPMACStatsHighCapacityPkts256to511Octets=_TnPMACStatsHighCapacityPkts256to511Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,36),_TnPMACStatsHighCapacityPkts256to511Octets_Type())
tnPMACStatsHighCapacityPkts256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts256to511Octets.setStatus(_A)
_TnPMACStatsHighCapacityPkts512to1023Octets_Type=Counter64
_TnPMACStatsHighCapacityPkts512to1023Octets_Object=MibTableColumn
tnPMACStatsHighCapacityPkts512to1023Octets=_TnPMACStatsHighCapacityPkts512to1023Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,37),_TnPMACStatsHighCapacityPkts512to1023Octets_Type())
tnPMACStatsHighCapacityPkts512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts512to1023Octets.setStatus(_A)
_TnPMACStatsHighCapacityPkts1024to1518Octets_Type=Counter64
_TnPMACStatsHighCapacityPkts1024to1518Octets_Object=MibTableColumn
tnPMACStatsHighCapacityPkts1024to1518Octets=_TnPMACStatsHighCapacityPkts1024to1518Octets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,38),_TnPMACStatsHighCapacityPkts1024to1518Octets_Type())
tnPMACStatsHighCapacityPkts1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts1024to1518Octets.setStatus(_A)
_TnPMACStatsHighCapacityPkts1519toMaxOctets_Type=Counter64
_TnPMACStatsHighCapacityPkts1519toMaxOctets_Object=MibTableColumn
tnPMACStatsHighCapacityPkts1519toMaxOctets=_TnPMACStatsHighCapacityPkts1519toMaxOctets_Object((1,3,6,1,4,1,7483,6,1,2,99,34,1,39),_TnPMACStatsHighCapacityPkts1519toMaxOctets_Type())
tnPMACStatsHighCapacityPkts1519toMaxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnPMACStatsHighCapacityPkts1519toMaxOctets.setStatus(_A)
_TnMMACStatsAttributeTotal_Type=Integer32
_TnMMACStatsAttributeTotal_Object=MibScalar
tnMMACStatsAttributeTotal=_TnMMACStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,35),_TnMMACStatsAttributeTotal_Type())
tnMMACStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsAttributeTotal.setStatus(_A)
_TnMMACStatsTable_Object=MibTable
tnMMACStatsTable=_TnMMACStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,36))
if mibBuilder.loadTexts:tnMMACStatsTable.setStatus(_A)
_TnMMACStatsEntry_Object=MibTableRow
tnMMACStatsEntry=_TnMMACStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1))
tnMMACStatsEntry.setIndexNames((0,_C,_A7),(0,_C,_A8),(0,_C,_A9))
if mibBuilder.loadTexts:tnMMACStatsEntry.setStatus(_A)
_TnMMACStatsPortId_Type=TmnxPortID
_TnMMACStatsPortId_Object=MibTableColumn
tnMMACStatsPortId=_TnMMACStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,1),_TnMMACStatsPortId_Type())
tnMMACStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMMACStatsPortId.setStatus(_A)
_TnMMACStatsInterval_Type=AluWdmStatsIntervalType
_TnMMACStatsInterval_Object=MibTableColumn
tnMMACStatsInterval=_TnMMACStatsInterval_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,2),_TnMMACStatsInterval_Type())
tnMMACStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMMACStatsInterval.setStatus(_A)
_TnMMACStatsBin_Type=AluWdmStatsBinNumber
_TnMMACStatsBin_Object=MibTableColumn
tnMMACStatsBin=_TnMMACStatsBin_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,3),_TnMMACStatsBin_Type())
tnMMACStatsBin.setMaxAccess(_D)
if mibBuilder.loadTexts:tnMMACStatsBin.setStatus(_A)
_TnMMACStatsBinStatus_Type=AluWdmStatsBinStatus
_TnMMACStatsBinStatus_Object=MibTableColumn
tnMMACStatsBinStatus=_TnMMACStatsBinStatus_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,4),_TnMMACStatsBinStatus_Type())
tnMMACStatsBinStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsBinStatus.setStatus(_A)
_TnMMACStatsStartTime_Type=DateAndTime
_TnMMACStatsStartTime_Object=MibTableColumn
tnMMACStatsStartTime=_TnMMACStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,5),_TnMMACStatsStartTime_Type())
tnMMACStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsStartTime.setStatus(_A)
_TnMMACStatsTotalMembers_Type=Integer32
_TnMMACStatsTotalMembers_Object=MibTableColumn
tnMMACStatsTotalMembers=_TnMMACStatsTotalMembers_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,6),_TnMMACStatsTotalMembers_Type())
tnMMACStatsTotalMembers.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsTotalMembers.setStatus(_A)
_TnMMACStatsFrameAssErrorCount_Type=Counter64
_TnMMACStatsFrameAssErrorCount_Object=MibTableColumn
tnMMACStatsFrameAssErrorCount=_TnMMACStatsFrameAssErrorCount_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,7),_TnMMACStatsFrameAssErrorCount_Type())
tnMMACStatsFrameAssErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsFrameAssErrorCount.setStatus(_A)
_TnMMACStatsFrameSmdErrorCount_Type=Counter64
_TnMMACStatsFrameSmdErrorCount_Object=MibTableColumn
tnMMACStatsFrameSmdErrorCount=_TnMMACStatsFrameSmdErrorCount_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,8),_TnMMACStatsFrameSmdErrorCount_Type())
tnMMACStatsFrameSmdErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsFrameSmdErrorCount.setStatus(_A)
_TnMMACStatsFrameAssOkCount_Type=Counter64
_TnMMACStatsFrameAssOkCount_Object=MibTableColumn
tnMMACStatsFrameAssOkCount=_TnMMACStatsFrameAssOkCount_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,9),_TnMMACStatsFrameAssOkCount_Type())
tnMMACStatsFrameAssOkCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsFrameAssOkCount.setStatus(_A)
_TnMMACStatsFragCountRx_Type=Counter64
_TnMMACStatsFragCountRx_Object=MibTableColumn
tnMMACStatsFragCountRx=_TnMMACStatsFragCountRx_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,10),_TnMMACStatsFragCountRx_Type())
tnMMACStatsFragCountRx.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsFragCountRx.setStatus(_A)
_TnMMACStatsFragCountTx_Type=Counter64
_TnMMACStatsFragCountTx_Object=MibTableColumn
tnMMACStatsFragCountTx=_TnMMACStatsFragCountTx_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,11),_TnMMACStatsFragCountTx_Type())
tnMMACStatsFragCountTx.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsFragCountTx.setStatus(_A)
_TnMMACStatsHoldCount_Type=Counter64
_TnMMACStatsHoldCount_Object=MibTableColumn
tnMMACStatsHoldCount=_TnMMACStatsHoldCount_Object((1,3,6,1,4,1,7483,6,1,2,99,36,1,12),_TnMMACStatsHoldCount_Type())
tnMMACStatsHoldCount.setMaxAccess(_B)
if mibBuilder.loadTexts:tnMMACStatsHoldCount.setStatus(_A)
_TnRoeMapperRawCountStatsAttributeTotal_Type=Integer32
_TnRoeMapperRawCountStatsAttributeTotal_Object=MibScalar
tnRoeMapperRawCountStatsAttributeTotal=_TnRoeMapperRawCountStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,37),_TnRoeMapperRawCountStatsAttributeTotal_Type())
tnRoeMapperRawCountStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawCountStatsAttributeTotal.setStatus(_A)
_TnRoeMapperRawCountStatsTable_Object=MibTable
tnRoeMapperRawCountStatsTable=_TnRoeMapperRawCountStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,38))
if mibBuilder.loadTexts:tnRoeMapperRawCountStatsTable.setStatus(_A)
_TnRoeMapperRawCountStatsEntry_Object=MibTableRow
tnRoeMapperRawCountStatsEntry=_TnRoeMapperRawCountStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1))
tnRoeMapperRawCountStatsEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:tnRoeMapperRawCountStatsEntry.setStatus(_A)
_TnRoeMapperRawCountStatsPortId_Type=TmnxPortID
_TnRoeMapperRawCountStatsPortId_Object=MibTableColumn
tnRoeMapperRawCountStatsPortId=_TnRoeMapperRawCountStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,1),_TnRoeMapperRawCountStatsPortId_Type())
tnRoeMapperRawCountStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeMapperRawCountStatsPortId.setStatus(_A)
class _TnRoeMapperRawStatsMapperID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeMapperRawStatsMapperID_Type.__name__=_E
_TnRoeMapperRawStatsMapperID_Object=MibTableColumn
tnRoeMapperRawStatsMapperID=_TnRoeMapperRawStatsMapperID_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,2),_TnRoeMapperRawStatsMapperID_Type())
tnRoeMapperRawStatsMapperID.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeMapperRawStatsMapperID.setStatus(_A)
_TnRoeMapperRawCountStatsClear_Type=TnCommand
_TnRoeMapperRawCountStatsClear_Object=MibTableColumn
tnRoeMapperRawCountStatsClear=_TnRoeMapperRawCountStatsClear_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,3),_TnRoeMapperRawCountStatsClear_Type())
tnRoeMapperRawCountStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeMapperRawCountStatsClear.setStatus(_A)
_TnRoeMapperRawCountStatsStartTime_Type=DateAndTime
_TnRoeMapperRawCountStatsStartTime_Object=MibTableColumn
tnRoeMapperRawCountStatsStartTime=_TnRoeMapperRawCountStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,4),_TnRoeMapperRawCountStatsStartTime_Type())
tnRoeMapperRawCountStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawCountStatsStartTime.setStatus(_A)
_TnRoeMapperRawCountStatsInPackets_Type=Counter64
_TnRoeMapperRawCountStatsInPackets_Object=MibTableColumn
tnRoeMapperRawCountStatsInPackets=_TnRoeMapperRawCountStatsInPackets_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,5),_TnRoeMapperRawCountStatsInPackets_Type())
tnRoeMapperRawCountStatsInPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawCountStatsInPackets.setStatus(_A)
_TnRoeMapperRawTxpackets_Type=Counter64
_TnRoeMapperRawTxpackets_Object=MibTableColumn
tnRoeMapperRawTxpackets=_TnRoeMapperRawTxpackets_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,6),_TnRoeMapperRawTxpackets_Type())
tnRoeMapperRawTxpackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawTxpackets.setStatus(_A)
_TnRoeMapperRawTxbytes_Type=Counter64
_TnRoeMapperRawTxbytes_Object=MibTableColumn
tnRoeMapperRawTxbytes=_TnRoeMapperRawTxbytes_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,7),_TnRoeMapperRawTxbytes_Type())
tnRoeMapperRawTxbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawTxbytes.setStatus(_A)
_TnRoeMapperRawTxDropPackets_Type=Counter64
_TnRoeMapperRawTxDropPackets_Object=MibTableColumn
tnRoeMapperRawTxDropPackets=_TnRoeMapperRawTxDropPackets_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,8),_TnRoeMapperRawTxDropPackets_Type())
tnRoeMapperRawTxDropPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawTxDropPackets.setStatus(_A)
_TnRoeMapperRawEncapQueueOverrun_Type=Counter64
_TnRoeMapperRawEncapQueueOverrun_Object=MibTableColumn
tnRoeMapperRawEncapQueueOverrun=_TnRoeMapperRawEncapQueueOverrun_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,9),_TnRoeMapperRawEncapQueueOverrun_Type())
tnRoeMapperRawEncapQueueOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawEncapQueueOverrun.setStatus(_A)
_TnRoeMapperRawGSMTimeSlotMismatch_Type=Counter64
_TnRoeMapperRawGSMTimeSlotMismatch_Object=MibTableColumn
tnRoeMapperRawGSMTimeSlotMismatch=_TnRoeMapperRawGSMTimeSlotMismatch_Object((1,3,6,1,4,1,7483,6,1,2,99,38,1,10),_TnRoeMapperRawGSMTimeSlotMismatch_Type())
tnRoeMapperRawGSMTimeSlotMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeMapperRawGSMTimeSlotMismatch.setStatus(_A)
_TnRoeDeMapperRawCountStatsAttributeTotal_Type=Integer32
_TnRoeDeMapperRawCountStatsAttributeTotal_Object=MibScalar
tnRoeDeMapperRawCountStatsAttributeTotal=_TnRoeDeMapperRawCountStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,39),_TnRoeDeMapperRawCountStatsAttributeTotal_Type())
tnRoeDeMapperRawCountStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawCountStatsAttributeTotal.setStatus(_A)
_TnRoeDeMapperRawCountStatsTable_Object=MibTable
tnRoeDeMapperRawCountStatsTable=_TnRoeDeMapperRawCountStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,40))
if mibBuilder.loadTexts:tnRoeDeMapperRawCountStatsTable.setStatus(_A)
_TnRoeDeMapperRawCountStatsEntry_Object=MibTableRow
tnRoeDeMapperRawCountStatsEntry=_TnRoeDeMapperRawCountStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1))
tnRoeDeMapperRawCountStatsEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:tnRoeDeMapperRawCountStatsEntry.setStatus(_A)
_TnRoeDeMapperRawCountStatsPortId_Type=TmnxPortID
_TnRoeDeMapperRawCountStatsPortId_Object=MibTableColumn
tnRoeDeMapperRawCountStatsPortId=_TnRoeDeMapperRawCountStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,1),_TnRoeDeMapperRawCountStatsPortId_Type())
tnRoeDeMapperRawCountStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeDeMapperRawCountStatsPortId.setStatus(_A)
class _TnRoeDeMapperRawStatsDeMapperID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,80))
_TnRoeDeMapperRawStatsDeMapperID_Type.__name__=_E
_TnRoeDeMapperRawStatsDeMapperID_Object=MibTableColumn
tnRoeDeMapperRawStatsDeMapperID=_TnRoeDeMapperRawStatsDeMapperID_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,2),_TnRoeDeMapperRawStatsDeMapperID_Type())
tnRoeDeMapperRawStatsDeMapperID.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeDeMapperRawStatsDeMapperID.setStatus(_A)
_TnRoeDeMapperRawCountStatsClear_Type=TnCommand
_TnRoeDeMapperRawCountStatsClear_Object=MibTableColumn
tnRoeDeMapperRawCountStatsClear=_TnRoeDeMapperRawCountStatsClear_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,3),_TnRoeDeMapperRawCountStatsClear_Type())
tnRoeDeMapperRawCountStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeDeMapperRawCountStatsClear.setStatus(_A)
_TnRoeDeMapperRawStatsStartTime_Type=DateAndTime
_TnRoeDeMapperRawStatsStartTime_Object=MibTableColumn
tnRoeDeMapperRawStatsStartTime=_TnRoeDeMapperRawStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,4),_TnRoeDeMapperRawStatsStartTime_Type())
tnRoeDeMapperRawStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawStatsStartTime.setStatus(_A)
_TnRoeDeMapperRawRxpackets_Type=Counter64
_TnRoeDeMapperRawRxpackets_Object=MibTableColumn
tnRoeDeMapperRawRxpackets=_TnRoeDeMapperRawRxpackets_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,5),_TnRoeDeMapperRawRxpackets_Type())
tnRoeDeMapperRawRxpackets.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawRxpackets.setStatus(_A)
_TnRoeDeMapperRawRxbytes_Type=Counter64
_TnRoeDeMapperRawRxbytes_Object=MibTableColumn
tnRoeDeMapperRawRxbytes=_TnRoeDeMapperRawRxbytes_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,6),_TnRoeDeMapperRawRxbytes_Type())
tnRoeDeMapperRawRxbytes.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawRxbytes.setStatus(_A)
_TnRoeDeMapperRawDecapQueueOverrun_Type=Counter64
_TnRoeDeMapperRawDecapQueueOverrun_Object=MibTableColumn
tnRoeDeMapperRawDecapQueueOverrun=_TnRoeDeMapperRawDecapQueueOverrun_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,7),_TnRoeDeMapperRawDecapQueueOverrun_Type())
tnRoeDeMapperRawDecapQueueOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawDecapQueueOverrun.setStatus(_A)
_TnRoeDeMapperRawQueueUnderrun_Type=Counter64
_TnRoeDeMapperRawQueueUnderrun_Object=MibTableColumn
tnRoeDeMapperRawQueueUnderrun=_TnRoeDeMapperRawQueueUnderrun_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,8),_TnRoeDeMapperRawQueueUnderrun_Type())
tnRoeDeMapperRawQueueUnderrun.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawQueueUnderrun.setStatus(_A)
_TnRoeDeMapperRawDecapPacketMissing_Type=Counter64
_TnRoeDeMapperRawDecapPacketMissing_Object=MibTableColumn
tnRoeDeMapperRawDecapPacketMissing=_TnRoeDeMapperRawDecapPacketMissing_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,9),_TnRoeDeMapperRawDecapPacketMissing_Type())
tnRoeDeMapperRawDecapPacketMissing.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawDecapPacketMissing.setStatus(_A)
_TnRoeDeMapperRawDecapPacketSizeMismatch_Type=Counter64
_TnRoeDeMapperRawDecapPacketSizeMismatch_Object=MibTableColumn
tnRoeDeMapperRawDecapPacketSizeMismatch=_TnRoeDeMapperRawDecapPacketSizeMismatch_Object((1,3,6,1,4,1,7483,6,1,2,99,40,1,10),_TnRoeDeMapperRawDecapPacketSizeMismatch_Type())
tnRoeDeMapperRawDecapPacketSizeMismatch.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeDeMapperRawDecapPacketSizeMismatch.setStatus(_A)
_TnRoeRawCountStatsAttributeTotal_Type=Integer32
_TnRoeRawCountStatsAttributeTotal_Object=MibScalar
tnRoeRawCountStatsAttributeTotal=_TnRoeRawCountStatsAttributeTotal_Object((1,3,6,1,4,1,7483,6,1,2,99,41),_TnRoeRawCountStatsAttributeTotal_Type())
tnRoeRawCountStatsAttributeTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeRawCountStatsAttributeTotal.setStatus(_A)
_TnRoeRawCountStatsTable_Object=MibTable
tnRoeRawCountStatsTable=_TnRoeRawCountStatsTable_Object((1,3,6,1,4,1,7483,6,1,2,99,42))
if mibBuilder.loadTexts:tnRoeRawCountStatsTable.setStatus(_A)
_TnRoeRawCountStatsEntry_Object=MibTableRow
tnRoeRawCountStatsEntry=_TnRoeRawCountStatsEntry_Object((1,3,6,1,4,1,7483,6,1,2,99,42,1))
tnRoeRawCountStatsEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:tnRoeRawCountStatsEntry.setStatus(_A)
_TnRoeRawStatsPortId_Type=TmnxPortID
_TnRoeRawStatsPortId_Object=MibTableColumn
tnRoeRawStatsPortId=_TnRoeRawStatsPortId_Object((1,3,6,1,4,1,7483,6,1,2,99,42,1,1),_TnRoeRawStatsPortId_Type())
tnRoeRawStatsPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tnRoeRawStatsPortId.setStatus(_A)
_TnRoeRawCountStatsClear_Type=TnCommand
_TnRoeRawCountStatsClear_Object=MibTableColumn
tnRoeRawCountStatsClear=_TnRoeRawCountStatsClear_Object((1,3,6,1,4,1,7483,6,1,2,99,42,1,2),_TnRoeRawCountStatsClear_Type())
tnRoeRawCountStatsClear.setMaxAccess(_F)
if mibBuilder.loadTexts:tnRoeRawCountStatsClear.setStatus(_A)
_TnRoeRawStatsStartTime_Type=DateAndTime
_TnRoeRawStatsStartTime_Object=MibTableColumn
tnRoeRawStatsStartTime=_TnRoeRawStatsStartTime_Object((1,3,6,1,4,1,7483,6,1,2,99,42,1,3),_TnRoeRawStatsStartTime_Type())
tnRoeRawStatsStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeRawStatsStartTime.setStatus(_A)
_TnRoeRawDecapPktsDropped_Type=Counter64
_TnRoeRawDecapPktsDropped_Object=MibTableColumn
tnRoeRawDecapPktsDropped=_TnRoeRawDecapPktsDropped_Object((1,3,6,1,4,1,7483,6,1,2,99,42,1,4),_TnRoeRawDecapPktsDropped_Type())
tnRoeRawDecapPktsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:tnRoeRawDecapPktsDropped.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'AluWdmPmonPolicyType':AluWdmPmonPolicyType,_W:AluWdmStatsIntervalType,_X:AluWdmStatsBinNumber,'AluWdmStatsBinStatus':AluWdmStatsBinStatus,'AluWdmPmonStatsClearType':AluWdmPmonStatsClearType,'tnPmonMIBModule':tnPmonMIBModule,'tnPmonObjs':tnPmonObjs,'tnPmonPolicyAttributeTotal':tnPmonPolicyAttributeTotal,'tnPmonPolicyTable':tnPmonPolicyTable,'tnPmonPolicyEntry':tnPmonPolicyEntry,_J:tnPmonPolicyType,_K:tnPmonPolicyId,'tnPmonPolicyRowStatus':tnPmonPolicyRowStatus,'tnPmonPolicyDescription':tnPmonPolicyDescription,'tnPmonPolicyNumOfBins15Min':tnPmonPolicyNumOfBins15Min,'tnPmonPolicyNumOfBins1Day':tnPmonPolicyNumOfBins1Day,'tnPmonPolicyFlrInterval15Min':tnPmonPolicyFlrInterval15Min,'tnPmonPolicyFlrInterval1Day':tnPmonPolicyFlrInterval1Day,'tnPmonPolicyFlrAvailabilityInterval15Min':tnPmonPolicyFlrAvailabilityInterval15Min,'tnPmonPolicyFlrAvailabilityInterval1Day':tnPmonPolicyFlrAvailabilityInterval1Day,'tnPmonPolicyNumOfBinsContinuous':tnPmonPolicyNumOfBinsContinuous,'tnPmonPolicyAvailFlrThreshold':tnPmonPolicyAvailFlrThreshold,'tnPmonPolicyAvailFlrNumOfIntervals':tnPmonPolicyAvailFlrNumOfIntervals,'tnPmonPolicyFramesPerDeltaT':tnPmonPolicyFramesPerDeltaT,'tnPmonClearAttributeTotal':tnPmonClearAttributeTotal,'tnPmonClearTable':tnPmonClearTable,'tnPmonClearEntry':tnPmonClearEntry,_V:tnPmonClearType,'tnPmonClearPortId':tnPmonClearPortId,'tnPmonClearEncapValue':tnPmonClearEncapValue,'tnPmonClearTestName':tnPmonClearTestName,'tnPmonClearInterval':tnPmonClearInterval,'tnPmonClearBin':tnPmonClearBin,'tnPmonClearRoeMapperId':tnPmonClearRoeMapperId,'tnPmonClearRoeDeMapperId':tnPmonClearRoeDeMapperId,'tnPmonTcaAttributeTotal':tnPmonTcaAttributeTotal,'tnPmonTcaTable':tnPmonTcaTable,'tnPmonTcaEntry':tnPmonTcaEntry,_Y:tnPmonTcaInterval,_Z:tnPmonTcaSubgroup,_a:tnPmonTcaId,'tnPmonTcaVariable':tnPmonTcaVariable,'tnPmonTcaValue':tnPmonTcaValue,'tnEthPortStatsAttributeTotal':tnEthPortStatsAttributeTotal,'tnEthPortStatsTable':tnEthPortStatsTable,'tnEthPortStatsEntry':tnEthPortStatsEntry,_L:tnEthPortStatsPortId,_M:tnEthPortStatsInterval,_N:tnEthPortStatsBin,'tnEthPortStatsBinStatus':tnEthPortStatsBinStatus,'tnEthPortStatsStartTime':tnEthPortStatsStartTime,'tnEthPortStatsTotalMembers':tnEthPortStatsTotalMembers,'tnEthPortStatsIfInOctets':tnEthPortStatsIfInOctets,'tnEthPortStatsIfInUcastPkts':tnEthPortStatsIfInUcastPkts,'tnEthPortStatsIfInDiscards':tnEthPortStatsIfInDiscards,'tnEthPortStatsIfInErrors':tnEthPortStatsIfInErrors,'tnEthPortStatsIfInUnknownProtos':tnEthPortStatsIfInUnknownProtos,'tnEthPortStatsIfInMulticastPkts':tnEthPortStatsIfInMulticastPkts,'tnEthPortStatsIfInBroadcastPkts':tnEthPortStatsIfInBroadcastPkts,'tnEthPortStatsIfOutOctets':tnEthPortStatsIfOutOctets,'tnEthPortStatsIfOutUcastPkts':tnEthPortStatsIfOutUcastPkts,'tnEthPortStatsIfOutDiscards':tnEthPortStatsIfOutDiscards,'tnEthPortStatsIfOutErrors':tnEthPortStatsIfOutErrors,'tnEthPortStatsIfOutMulticastPkts':tnEthPortStatsIfOutMulticastPkts,'tnEthPortStatsIfOutBroadcastPkts':tnEthPortStatsIfOutBroadcastPkts,'tnEthPortStatsIfInPkts':tnEthPortStatsIfInPkts,'tnEthPortStatsIfOutPkts':tnEthPortStatsIfOutPkts,'tnEthPortEtherStatsDropEvents':tnEthPortEtherStatsDropEvents,'tnEthPortEtherStatsBroadcastPkts':tnEthPortEtherStatsBroadcastPkts,'tnEthPortEtherStatsMulticastPkts':tnEthPortEtherStatsMulticastPkts,'tnEthPortEtherStatsCRCAlignErrors':tnEthPortEtherStatsCRCAlignErrors,'tnEthPortEtherStatsUndersizePkts':tnEthPortEtherStatsUndersizePkts,'tnEthPortEtherStatsOversizePkts':tnEthPortEtherStatsOversizePkts,'tnEthPortEtherStatsFragments':tnEthPortEtherStatsFragments,'tnEthPortEtherStatsJabbers':tnEthPortEtherStatsJabbers,'tnEthPortEtherStatsCollisions':tnEthPortEtherStatsCollisions,'tnEthPortEtherStatsHighCapacityPkts':tnEthPortEtherStatsHighCapacityPkts,'tnEthPortEtherStatsHighCapacityOctets':tnEthPortEtherStatsHighCapacityOctets,'tnEthPortEtherStatsHighCapacityPkts64Octets':tnEthPortEtherStatsHighCapacityPkts64Octets,'tnEthPortEtherStatsHighCapacityPkts65to127Octets':tnEthPortEtherStatsHighCapacityPkts65to127Octets,'tnEthPortEtherStatsHighCapacityPkts128to255Octets':tnEthPortEtherStatsHighCapacityPkts128to255Octets,'tnEthPortEtherStatsHighCapacityPkts256to511Octets':tnEthPortEtherStatsHighCapacityPkts256to511Octets,'tnEthPortEtherStatsHighCapacityPkts512to1023Octets':tnEthPortEtherStatsHighCapacityPkts512to1023Octets,'tnEthPortEtherStatsHighCapacityPkts1024to1518Octets':tnEthPortEtherStatsHighCapacityPkts1024to1518Octets,'tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets':tnEthPortEtherStatsHighCapacityPkts1519toMaxOctets,'tnEthPortEgrQueueStatsAttributeTotal':tnEthPortEgrQueueStatsAttributeTotal,'tnEthPortEgrQueueStatsTable':tnEthPortEgrQueueStatsTable,'tnEthPortEgrQueueStatsEntry':tnEthPortEgrQueueStatsEntry,_b:tnEthPortStatsQueueId,'tnEthPortEgrQueueStatsInProfilePktsForwarded':tnEthPortEgrQueueStatsInProfilePktsForwarded,'tnEthPortEgrQueueStatsOutOfProfilePktsForwarded':tnEthPortEgrQueueStatsOutOfProfilePktsForwarded,'tnEthPortEgrQueueStatsInProfileOctetsForwarded':tnEthPortEgrQueueStatsInProfileOctetsForwarded,'tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded':tnEthPortEgrQueueStatsOutOfProfileOctetsForwarded,'tnEthPortEgrQueueStatsInProfilePktsDropped':tnEthPortEgrQueueStatsInProfilePktsDropped,'tnEthPortEgrQueueStatsOutOfProfilePktsDropped':tnEthPortEgrQueueStatsOutOfProfilePktsDropped,'tnEthPortEgrQueueStatsInProfileOctetsDropped':tnEthPortEgrQueueStatsInProfileOctetsDropped,'tnEthPortEgrQueueStatsOutOfProfileOctetsDropped':tnEthPortEgrQueueStatsOutOfProfileOctetsDropped,'tnSapStatsAttributeTotal':tnSapStatsAttributeTotal,'tnSapStatsTable':tnSapStatsTable,'tnSapStatsEntry':tnSapStatsEntry,_O:tnSapStatsPortId,_P:tnSapStatsEncapVal,_Q:tnSapStatsInterval,_R:tnSapStatsBin,'tnSapStatsBinStatus':tnSapStatsBinStatus,'tnSapStatsStartTime':tnSapStatsStartTime,'tnSapStatsTotalMembers':tnSapStatsTotalMembers,'tnSapStatsIngressPktsForwarded':tnSapStatsIngressPktsForwarded,'tnSapStatsIngressOctetsForwarded':tnSapStatsIngressOctetsForwarded,'tnSapStatsEgressPktsForwarded':tnSapStatsEgressPktsForwarded,'tnSapStatsEgressOctetsForwarded':tnSapStatsEgressOctetsForwarded,'tnSapStatsIngressPktsDropped':tnSapStatsIngressPktsDropped,'tnSapStatsIngressOctetsDropped':tnSapStatsIngressOctetsDropped,'tnSapStatsIngressExtraTagPktsDropped':tnSapStatsIngressExtraTagPktsDropped,'tnSapStatsIngressExtraTagOctetsDropped':tnSapStatsIngressExtraTagOctetsDropped,'tnSapMeterStatsAttributeTotal':tnSapMeterStatsAttributeTotal,'tnSapMeterStatsTable':tnSapMeterStatsTable,'tnSapMeterStatsEntry':tnSapMeterStatsEntry,_c:tnSapStatsMeterId,'tnSapMeterStatsInProfilePktsForwarded':tnSapMeterStatsInProfilePktsForwarded,'tnSapMeterStatsOutOfProfilePktsForwarded':tnSapMeterStatsOutOfProfilePktsForwarded,'tnSapMeterStatsInProfileOctetsForwarded':tnSapMeterStatsInProfileOctetsForwarded,'tnSapMeterStatsOutOfProfileOctetsForwarded':tnSapMeterStatsOutOfProfileOctetsForwarded,'tnEthCfmTWSlmStatsAttributeTotal':tnEthCfmTWSlmStatsAttributeTotal,'tnEthCfmTWSlmStatsTable':tnEthCfmTWSlmStatsTable,'tnEthCfmTWSlmStatsEntry':tnEthCfmTWSlmStatsEntry,_d:tnEthCfmTWSlmStatsTestName,_e:tnEthCfmTWSlmStatsInterval,_f:tnEthCfmTWSlmStatsBin,'tnEthCfmTWSlmStatsBinStatus':tnEthCfmTWSlmStatsBinStatus,'tnEthCfmTWSlmStatsStartTime':tnEthCfmTWSlmStatsStartTime,'tnEthCfmTWSlmStatsTotalMembers':tnEthCfmTWSlmStatsTotalMembers,'tnEthCfmTWSlmStatsNearEndFrameLossRatioMin':tnEthCfmTWSlmStatsNearEndFrameLossRatioMin,'tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage':tnEthCfmTWSlmStatsNearEndFrameLossRatioAverage,'tnEthCfmTWSlmStatsNearEndFrameLossRatioMax':tnEthCfmTWSlmStatsNearEndFrameLossRatioMax,'tnEthCfmTWSlmStatsFarEndFrameLossRatioMin':tnEthCfmTWSlmStatsFarEndFrameLossRatioMin,'tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage':tnEthCfmTWSlmStatsFarEndFrameLossRatioAverage,'tnEthCfmTWSlmStatsFarEndFrameLossRatioMax':tnEthCfmTWSlmStatsFarEndFrameLossRatioMax,'tnEthCfmTWSlmStatsNearEndHighLoss':tnEthCfmTWSlmStatsNearEndHighLoss,'tnEthCfmTWSlmStatsFarEndHighLoss':tnEthCfmTWSlmStatsFarEndHighLoss,'tnEthCfmTWSlmStatsNearEndUnavailable':tnEthCfmTWSlmStatsNearEndUnavailable,'tnEthCfmTWSlmStatsFarEndUnavailable':tnEthCfmTWSlmStatsFarEndUnavailable,'tnEthCfmTWDmStatsAttributeTotal':tnEthCfmTWDmStatsAttributeTotal,'tnEthCfmTWDmStatsTable':tnEthCfmTWDmStatsTable,'tnEthCfmTWDmStatsEntry':tnEthCfmTWDmStatsEntry,_g:tnEthCfmTWDmStatsTestName,_h:tnEthCfmTWDmStatsInterval,_i:tnEthCfmTWDmStatsBin,'tnEthCfmTWDmStatsBinStatus':tnEthCfmTWDmStatsBinStatus,'tnEthCfmTWDmStatsStartTime':tnEthCfmTWDmStatsStartTime,'tnEthCfmTWDmStatsTotalMembers':tnEthCfmTWDmStatsTotalMembers,'tnEthCfmTWDmStatsRoundTripFrameDelayMin':tnEthCfmTWDmStatsRoundTripFrameDelayMin,'tnEthCfmTWDmStatsRoundTripFrameDelayAverage':tnEthCfmTWDmStatsRoundTripFrameDelayAverage,'tnEthCfmTWDmStatsRoundTripFrameDelayMax':tnEthCfmTWDmStatsRoundTripFrameDelayMax,'tnEthCfmTWDmStatsNearEndFrameDelayVariationMin':tnEthCfmTWDmStatsNearEndFrameDelayVariationMin,'tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage':tnEthCfmTWDmStatsNearEndFrameDelayVariationAverage,'tnEthCfmTWDmStatsNearEndFrameDelayVariationMax':tnEthCfmTWDmStatsNearEndFrameDelayVariationMax,'tnEthCfmTWDmStatsFarEndFrameDelayVariationMin':tnEthCfmTWDmStatsFarEndFrameDelayVariationMin,'tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage':tnEthCfmTWDmStatsFarEndFrameDelayVariationAverage,'tnEthCfmTWDmStatsFarEndFrameDelayVariationMax':tnEthCfmTWDmStatsFarEndFrameDelayVariationMax,'tnEthCfmTWDmStatsNearEndFrameDelayMin':tnEthCfmTWDmStatsNearEndFrameDelayMin,'tnEthCfmTWDmStatsNearEndFrameDelayAverage':tnEthCfmTWDmStatsNearEndFrameDelayAverage,'tnEthCfmTWDmStatsNearEndFrameDelayMax':tnEthCfmTWDmStatsNearEndFrameDelayMax,'tnEthCfmTWDmStatsFarEndFrameDelayMin':tnEthCfmTWDmStatsFarEndFrameDelayMin,'tnEthCfmTWDmStatsFarEndFrameDelayAverage':tnEthCfmTWDmStatsFarEndFrameDelayAverage,'tnEthCfmTWDmStatsFarEndFrameDelayMax':tnEthCfmTWDmStatsFarEndFrameDelayMax,'tnEthCfmTWLmStatsAttributeTotal':tnEthCfmTWLmStatsAttributeTotal,'tnEthCfmTWLmStatsTable':tnEthCfmTWLmStatsTable,'tnEthCfmTWLmStatsEntry':tnEthCfmTWLmStatsEntry,_j:tnEthCfmTWLmStatsTestName,_k:tnEthCfmTWLmStatsInterval,_l:tnEthCfmTWLmStatsBin,'tnEthCfmTWLmStatsBinStatus':tnEthCfmTWLmStatsBinStatus,'tnEthCfmTWLmStatsStartTime':tnEthCfmTWLmStatsStartTime,'tnEthCfmTWLmStatsTotalMembers':tnEthCfmTWLmStatsTotalMembers,'tnEthCfmTWLmStatsNearEndFrameLossRatioMin':tnEthCfmTWLmStatsNearEndFrameLossRatioMin,'tnEthCfmTWLmStatsNearEndFrameLossRatioAverage':tnEthCfmTWLmStatsNearEndFrameLossRatioAverage,'tnEthCfmTWLmStatsNearEndFrameLossRatioMax':tnEthCfmTWLmStatsNearEndFrameLossRatioMax,'tnEthCfmTWLmStatsFarEndFrameLossRatioMin':tnEthCfmTWLmStatsFarEndFrameLossRatioMin,'tnEthCfmTWLmStatsFarEndFrameLossRatioAverage':tnEthCfmTWLmStatsFarEndFrameLossRatioAverage,'tnEthCfmTWLmStatsFarEndFrameLossRatioMax':tnEthCfmTWLmStatsFarEndFrameLossRatioMax,'tnEthCfmTWLmStatsNearEndHighLoss':tnEthCfmTWLmStatsNearEndHighLoss,'tnEthCfmTWLmStatsFarEndHighLoss':tnEthCfmTWLmStatsFarEndHighLoss,'tnEthCfmTWLmStatsNearEndUnavailable':tnEthCfmTWLmStatsNearEndUnavailable,'tnEthCfmTWLmStatsFarEndUnavailable':tnEthCfmTWLmStatsFarEndUnavailable,'tnEthCfmTWLmStatsTransmittedLMMFrame':tnEthCfmTWLmStatsTransmittedLMMFrame,'tnEthCfmTWLmStatsReceivedLMRFrame':tnEthCfmTWLmStatsReceivedLMRFrame,'tnEthCfmTWLmStatsNearEndTransmittedDataFrame':tnEthCfmTWLmStatsNearEndTransmittedDataFrame,'tnEthCfmTWLmStatsNearEndReceivedDataFrame':tnEthCfmTWLmStatsNearEndReceivedDataFrame,'tnEthCfmTWLmStatsFarEndTransmittedDataFrame':tnEthCfmTWLmStatsFarEndTransmittedDataFrame,'tnEthCfmTWLmStatsFarEndReceivedDataFrame':tnEthCfmTWLmStatsFarEndReceivedDataFrame,'tnPktWanifStatsAttributeTotal':tnPktWanifStatsAttributeTotal,'tnPktWanifStatsTable':tnPktWanifStatsTable,'tnPktWanifStatsEntry':tnPktWanifStatsEntry,_m:tnPktWanifStatsPortId,_n:tnPktWanifStatsInterval,_o:tnPktWanifStatsBin,'tnPktWanifStatsBinStatus':tnPktWanifStatsBinStatus,'tnPktWanifStatsStartTime':tnPktWanifStatsStartTime,'tnPktWanifStatsInPackets':tnPktWanifStatsInPackets,'tnPktWanifStatsInOctets':tnPktWanifStatsInOctets,'tnPktWanifStatsInUcastPkts':tnPktWanifStatsInUcastPkts,'tnPktWanifStatsInDiscards':tnPktWanifStatsInDiscards,'tnPktWanifStatsInErrors':tnPktWanifStatsInErrors,'tnPktWanifStatsInUnknownProtos':tnPktWanifStatsInUnknownProtos,'tnPktWanifStatsInMulticastPkts':tnPktWanifStatsInMulticastPkts,'tnPktWanifStatsInBroadcastPkts':tnPktWanifStatsInBroadcastPkts,'tnPktWanifStatsOutPackets':tnPktWanifStatsOutPackets,'tnPktWanifStatsOutOctets':tnPktWanifStatsOutOctets,'tnPktWanifStatsOutUcastPkts':tnPktWanifStatsOutUcastPkts,'tnPktWanifStatsOutDiscards':tnPktWanifStatsOutDiscards,'tnPktWanifStatsOutErrors':tnPktWanifStatsOutErrors,'tnPktWanifStatsOutMulticastPkts':tnPktWanifStatsOutMulticastPkts,'tnPktWanifStatsOutBroadcastPkts':tnPktWanifStatsOutBroadcastPkts,'tnPktWanifStatsDropEvents':tnPktWanifStatsDropEvents,'tnPktWanifStatsBroadcastPkts':tnPktWanifStatsBroadcastPkts,'tnPktWanifStatsMulticastPkts':tnPktWanifStatsMulticastPkts,'tnPktWanifStatsCRCAlignErrors':tnPktWanifStatsCRCAlignErrors,'tnPktWanifStatsUndersizePkts':tnPktWanifStatsUndersizePkts,'tnPktWanifStatsOversizePkts':tnPktWanifStatsOversizePkts,'tnPktWanifStatsFragments':tnPktWanifStatsFragments,'tnPktWanifStatsJabbers':tnPktWanifStatsJabbers,'tnPktWanifStatsCollisions':tnPktWanifStatsCollisions,'tnPktWanifStatsHighCapacityPkts':tnPktWanifStatsHighCapacityPkts,'tnPktWanifStatsHighCapacityOctets':tnPktWanifStatsHighCapacityOctets,'tnPktWanifStatsHighCapacityPktsSize64':tnPktWanifStatsHighCapacityPktsSize64,'tnPktWanifStatsHighCapacityPktsSize65to127':tnPktWanifStatsHighCapacityPktsSize65to127,'tnPktWanifStatsHighCapacityPktsSize128to255':tnPktWanifStatsHighCapacityPktsSize128to255,'tnPktWanifStatsHighCapacityPktsSize256to511':tnPktWanifStatsHighCapacityPktsSize256to511,'tnPktWanifStatsHighCapacityPktsSize512to1023':tnPktWanifStatsHighCapacityPktsSize512to1023,'tnPktWanifStatsHighCapacityPktsSize1024to1518':tnPktWanifStatsHighCapacityPktsSize1024to1518,'tnPktWanifStatsHighCapacityPktsSize1519toMax':tnPktWanifStatsHighCapacityPktsSize1519toMax,'tnPktWanifStatsTooLongFrames':tnPktWanifStatsTooLongFrames,'tnPktWanifRawCountStatsAttributeTotal':tnPktWanifRawCountStatsAttributeTotal,'tnPktWanifRawCountStatsTable':tnPktWanifRawCountStatsTable,'tnPktWanifRawCountStatsEntry':tnPktWanifRawCountStatsEntry,_p:tnPktWanifRawCountStatsPortId,'tnPktWanifRawCountStatsClear':tnPktWanifRawCountStatsClear,'tnPktWanifRawCountStatsStartTime':tnPktWanifRawCountStatsStartTime,'tnPktWanifRawCountStatsInPackets':tnPktWanifRawCountStatsInPackets,'tnPktWanifRawCountStatsInOctets':tnPktWanifRawCountStatsInOctets,'tnPktWanifRawCountStatsInUcastPkts':tnPktWanifRawCountStatsInUcastPkts,'tnPktWanifRawCountStatsInDiscards':tnPktWanifRawCountStatsInDiscards,'tnPktWanifRawCountStatsInErrors':tnPktWanifRawCountStatsInErrors,'tnPktWanifRawCountStatsInUnknownProtos':tnPktWanifRawCountStatsInUnknownProtos,'tnPktWanifRawCountStatsInMulticastPkts':tnPktWanifRawCountStatsInMulticastPkts,'tnPktWanifRawCountStatsInBroadcastPkts':tnPktWanifRawCountStatsInBroadcastPkts,'tnPktWanifRawCountStatsOutPackets':tnPktWanifRawCountStatsOutPackets,'tnPktWanifRawCountStatsOutOctets':tnPktWanifRawCountStatsOutOctets,'tnPktWanifRawCountStatsOutUcastPkts':tnPktWanifRawCountStatsOutUcastPkts,'tnPktWanifRawCountStatsOutDiscards':tnPktWanifRawCountStatsOutDiscards,'tnPktWanifRawCountStatsOutErrors':tnPktWanifRawCountStatsOutErrors,'tnPktWanifRawCountStatsOutMulticastPkts':tnPktWanifRawCountStatsOutMulticastPkts,'tnPktWanifRawCountStatsOutBroadcastPkts':tnPktWanifRawCountStatsOutBroadcastPkts,'tnPktWanifRawCountStatsDropEvents':tnPktWanifRawCountStatsDropEvents,'tnPktWanifRawCountStatsBroadcastPkts':tnPktWanifRawCountStatsBroadcastPkts,'tnPktWanifRawCountStatsMulticastPkts':tnPktWanifRawCountStatsMulticastPkts,'tnPktWanifRawCountStatsCRCAlignErrors':tnPktWanifRawCountStatsCRCAlignErrors,'tnPktWanifRawCountStatsUndersizePkts':tnPktWanifRawCountStatsUndersizePkts,'tnPktWanifRawCountStatsOversizePkts':tnPktWanifRawCountStatsOversizePkts,'tnPktWanifRawCountStatsFragments':tnPktWanifRawCountStatsFragments,'tnPktWanifRawCountStatsJabbers':tnPktWanifRawCountStatsJabbers,'tnPktWanifRawCountStatsCollisions':tnPktWanifRawCountStatsCollisions,'tnPktWanifRawCountStatsHighCapacityPkts':tnPktWanifRawCountStatsHighCapacityPkts,'tnPktWanifRawCountStatsHighCapacityOctets':tnPktWanifRawCountStatsHighCapacityOctets,'tnPktWanifRawCountStatsHighCapacityPktsSize64':tnPktWanifRawCountStatsHighCapacityPktsSize64,'tnPktWanifRawCountStatsHighCapacityPktsSize65to127':tnPktWanifRawCountStatsHighCapacityPktsSize65to127,'tnPktWanifRawCountStatsHighCapacityPktsSize128to255':tnPktWanifRawCountStatsHighCapacityPktsSize128to255,'tnPktWanifRawCountStatsHighCapacityPktsSize256to511':tnPktWanifRawCountStatsHighCapacityPktsSize256to511,'tnPktWanifRawCountStatsHighCapacityPktsSize512to1023':tnPktWanifRawCountStatsHighCapacityPktsSize512to1023,'tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518':tnPktWanifRawCountStatsHighCapacityPktsSize1024to1518,'tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax':tnPktWanifRawCountStatsHighCapacityPktsSize1519toMax,'tnPktWanifRawCountStatsTooLongFrames':tnPktWanifRawCountStatsTooLongFrames,'tnRoeStatsAttributeTotal':tnRoeStatsAttributeTotal,'tnRoeStatsTable':tnRoeStatsTable,'tnRoeStatsEntry':tnRoeStatsEntry,_q:tnRoeStatsPortId,_r:tnRoeStatsInterval,_s:tnRoeStatsBin,'tnRoeStatsBinStatus':tnRoeStatsBinStatus,'tnRoeStatsStartTime':tnRoeStatsStartTime,'tnRoeStatsTotalMembers':tnRoeStatsTotalMembers,'tnRoeStatsDecapPktsDropped':tnRoeStatsDecapPktsDropped,'tnRoeMapperStatsAttributeTotal':tnRoeMapperStatsAttributeTotal,'tnRoeMapperStatsTable':tnRoeMapperStatsTable,'tnRoeMapperStatsEntry':tnRoeMapperStatsEntry,_t:tnRoeMapperStatsPortId,_u:tnRoeMapperStatsMapperID,_v:tnRoeMapperStatsInterval,_w:tnRoeMapperStatsBin,'tnRoeMapperStatsBinStatus':tnRoeMapperStatsBinStatus,'tnRoeMapperStatsStartTime':tnRoeMapperStatsStartTime,'tnRoeMapperStatsTotalMembers':tnRoeMapperStatsTotalMembers,'tnRoeMapperStatsTxpackets':tnRoeMapperStatsTxpackets,'tnRoeMapperStatsTxbytes':tnRoeMapperStatsTxbytes,'tnRoeMapperStatsTxDropPackets':tnRoeMapperStatsTxDropPackets,'tnRoeMapperStatsEncapQueueOverrun':tnRoeMapperStatsEncapQueueOverrun,'tnRoeMapperStatsGSMTimeSlotMismatch':tnRoeMapperStatsGSMTimeSlotMismatch,'tnRoeDeMapperStatsAttributeTotal':tnRoeDeMapperStatsAttributeTotal,'tnRoeDeMapperStatsTable':tnRoeDeMapperStatsTable,'tnRoeDeMapperStatsEntry':tnRoeDeMapperStatsEntry,_x:tnRoeDeMapperStatsPortId,_y:tnRoeDeMapperStatsDeMapperID,_z:tnRoeDeMapperStatsInterval,_A0:tnRoeDeMapperStatsBin,'tnRoeDeMapperStatsBinStatus':tnRoeDeMapperStatsBinStatus,'tnRoeDeMapperStatsStartTime':tnRoeDeMapperStatsStartTime,'tnRoeDeMapperStatsTotalMembers':tnRoeDeMapperStatsTotalMembers,'tnRoeDeMapperStatsRxpackets':tnRoeDeMapperStatsRxpackets,'tnRoeDeMapperStatsRxbytes':tnRoeDeMapperStatsRxbytes,'tnRoeDeMapperStatsDecapQueueOverrun':tnRoeDeMapperStatsDecapQueueOverrun,'tnRoeDeMapperStatsQueueUnderrun':tnRoeDeMapperStatsQueueUnderrun,'tnRoeDeMapperStatsDecapPacketMissing':tnRoeDeMapperStatsDecapPacketMissing,'tnRoeDeMapperStatsDecapPacketSizeMismatch':tnRoeDeMapperStatsDecapPacketSizeMismatch,'tnEMACStatsAttributeTotal':tnEMACStatsAttributeTotal,'tnEMACStatsTable':tnEMACStatsTable,'tnEMACStatsEntry':tnEMACStatsEntry,_A1:tnEMACStatsPortId,_A2:tnEMACStatsInterval,_A3:tnEMACStatsBin,'tnEMACStatsBinStatus':tnEMACStatsBinStatus,'tnEMACStatsStartTime':tnEMACStatsStartTime,'tnEMACStatsTotalMembers':tnEMACStatsTotalMembers,'tnEMACStatsIfInOctets':tnEMACStatsIfInOctets,'tnEMACStatsIfInUcastPkts':tnEMACStatsIfInUcastPkts,'tnEMACStatsIfInDiscards':tnEMACStatsIfInDiscards,'tnEMACStatsIfInErrors':tnEMACStatsIfInErrors,'tnEMACStatsIfInUnknownProtos':tnEMACStatsIfInUnknownProtos,'tnEMACStatsIfInMulticastPkts':tnEMACStatsIfInMulticastPkts,'tnEMACStatsIfInBroadcastPkts':tnEMACStatsIfInBroadcastPkts,'tnEMACStatsIfOutOctets':tnEMACStatsIfOutOctets,'tnEMACStatsIfOutUcastPkts':tnEMACStatsIfOutUcastPkts,'tnEMACStatsIfOutDiscards':tnEMACStatsIfOutDiscards,'tnEMACStatsIfOutErrors':tnEMACStatsIfOutErrors,'tnEMACStatsIfOutMulticastPkts':tnEMACStatsIfOutMulticastPkts,'tnEMACStatsIfOutBroadcastPkts':tnEMACStatsIfOutBroadcastPkts,'tnEMACStatsIfInPkts':tnEMACStatsIfInPkts,'tnEMACStatsIfOutPkts':tnEMACStatsIfOutPkts,'tnEMACStatsDropEvents':tnEMACStatsDropEvents,'tnEMACStatsBroadcastPkts':tnEMACStatsBroadcastPkts,'tnEMACStatsMulticastPkts':tnEMACStatsMulticastPkts,'tnEMACStatsCRCAlignErrors':tnEMACStatsCRCAlignErrors,'tnEMACStatsUndersizePkts':tnEMACStatsUndersizePkts,'tnEMACStatsOversizePkts':tnEMACStatsOversizePkts,'tnEMACStatsFragments':tnEMACStatsFragments,'tnEMACStatsJabbers':tnEMACStatsJabbers,'tnEMACStatsCollisions':tnEMACStatsCollisions,'tnEMACStatsHighCapacityPkts':tnEMACStatsHighCapacityPkts,'tnEMACStatsHighCapacityOctets':tnEMACStatsHighCapacityOctets,'tnEMACStatsHighCapacityPkts64Octets':tnEMACStatsHighCapacityPkts64Octets,'tnEMACStatsHighCapacityPkts65to127Octets':tnEMACStatsHighCapacityPkts65to127Octets,'tnEMACStatsHighCapacityPkts128to255Octets':tnEMACStatsHighCapacityPkts128to255Octets,'tnEMACStatsHighCapacityPkts256to511Octets':tnEMACStatsHighCapacityPkts256to511Octets,'tnEMACStatsHighCapacityPkts512to1023Octets':tnEMACStatsHighCapacityPkts512to1023Octets,'tnEMACStatsHighCapacityPkts1024to1518Octets':tnEMACStatsHighCapacityPkts1024to1518Octets,'tnEMACStatsHighCapacityPkts1519toMaxOctets':tnEMACStatsHighCapacityPkts1519toMaxOctets,'tnPMACStatsAttributeTotal':tnPMACStatsAttributeTotal,'tnPMACStatsTable':tnPMACStatsTable,'tnPMACStatsEntry':tnPMACStatsEntry,_A4:tnPMACStatsPortId,_A5:tnPMACStatsInterval,_A6:tnPMACStatsBin,'tnPMACStatsBinStatus':tnPMACStatsBinStatus,'tnPMACStatsStartTime':tnPMACStatsStartTime,'tnPMACStatsTotalMembers':tnPMACStatsTotalMembers,'tnPMACStatsIfInOctets':tnPMACStatsIfInOctets,'tnPMACStatsIfInUcastPkts':tnPMACStatsIfInUcastPkts,'tnPMACStatsIfInDiscards':tnPMACStatsIfInDiscards,'tnPMACStatsIfInErrors':tnPMACStatsIfInErrors,'tnPMACStatsIfInUnknownProtos':tnPMACStatsIfInUnknownProtos,'tnPMACStatsIfInMulticastPkts':tnPMACStatsIfInMulticastPkts,'tnPMACStatsIfInBroadcastPkts':tnPMACStatsIfInBroadcastPkts,'tnPMACStatsIfOutOctets':tnPMACStatsIfOutOctets,'tnPMACStatsIfOutUcastPkts':tnPMACStatsIfOutUcastPkts,'tnPMACStatsIfOutDiscards':tnPMACStatsIfOutDiscards,'tnPMACStatsIfOutErrors':tnPMACStatsIfOutErrors,'tnPMACStatsIfOutMulticastPkts':tnPMACStatsIfOutMulticastPkts,'tnPMACStatsIfOutBroadcastPkts':tnPMACStatsIfOutBroadcastPkts,'tnPMACStatsIfInPkts':tnPMACStatsIfInPkts,'tnPMACStatsIfOutPkts':tnPMACStatsIfOutPkts,'tnPMACStatsDropEvents':tnPMACStatsDropEvents,'tnPMACStatsBroadcastPkts':tnPMACStatsBroadcastPkts,'tnPMACStatsMulticastPkts':tnPMACStatsMulticastPkts,'tnPMACStatsCRCAlignErrors':tnPMACStatsCRCAlignErrors,'tnPMACStatsUndersizePkts':tnPMACStatsUndersizePkts,'tnPMACStatsOversizePkts':tnPMACStatsOversizePkts,'tnPMACStatsFragments':tnPMACStatsFragments,'tnPMACStatsJabbers':tnPMACStatsJabbers,'tnPMACStatsCollisions':tnPMACStatsCollisions,'tnPMACStatsHighCapacityPkts':tnPMACStatsHighCapacityPkts,'tnPMACStatsHighCapacityOctets':tnPMACStatsHighCapacityOctets,'tnPMACStatsHighCapacityPkts64Octets':tnPMACStatsHighCapacityPkts64Octets,'tnPMACStatsHighCapacityPkts65to127Octets':tnPMACStatsHighCapacityPkts65to127Octets,'tnPMACStatsHighCapacityPkts128to255Octets':tnPMACStatsHighCapacityPkts128to255Octets,'tnPMACStatsHighCapacityPkts256to511Octets':tnPMACStatsHighCapacityPkts256to511Octets,'tnPMACStatsHighCapacityPkts512to1023Octets':tnPMACStatsHighCapacityPkts512to1023Octets,'tnPMACStatsHighCapacityPkts1024to1518Octets':tnPMACStatsHighCapacityPkts1024to1518Octets,'tnPMACStatsHighCapacityPkts1519toMaxOctets':tnPMACStatsHighCapacityPkts1519toMaxOctets,'tnMMACStatsAttributeTotal':tnMMACStatsAttributeTotal,'tnMMACStatsTable':tnMMACStatsTable,'tnMMACStatsEntry':tnMMACStatsEntry,_A7:tnMMACStatsPortId,_A8:tnMMACStatsInterval,_A9:tnMMACStatsBin,'tnMMACStatsBinStatus':tnMMACStatsBinStatus,'tnMMACStatsStartTime':tnMMACStatsStartTime,'tnMMACStatsTotalMembers':tnMMACStatsTotalMembers,'tnMMACStatsFrameAssErrorCount':tnMMACStatsFrameAssErrorCount,'tnMMACStatsFrameSmdErrorCount':tnMMACStatsFrameSmdErrorCount,'tnMMACStatsFrameAssOkCount':tnMMACStatsFrameAssOkCount,'tnMMACStatsFragCountRx':tnMMACStatsFragCountRx,'tnMMACStatsFragCountTx':tnMMACStatsFragCountTx,'tnMMACStatsHoldCount':tnMMACStatsHoldCount,'tnRoeMapperRawCountStatsAttributeTotal':tnRoeMapperRawCountStatsAttributeTotal,'tnRoeMapperRawCountStatsTable':tnRoeMapperRawCountStatsTable,'tnRoeMapperRawCountStatsEntry':tnRoeMapperRawCountStatsEntry,_AA:tnRoeMapperRawCountStatsPortId,'tnRoeMapperRawStatsMapperID':tnRoeMapperRawStatsMapperID,'tnRoeMapperRawCountStatsClear':tnRoeMapperRawCountStatsClear,'tnRoeMapperRawCountStatsStartTime':tnRoeMapperRawCountStatsStartTime,'tnRoeMapperRawCountStatsInPackets':tnRoeMapperRawCountStatsInPackets,'tnRoeMapperRawTxpackets':tnRoeMapperRawTxpackets,'tnRoeMapperRawTxbytes':tnRoeMapperRawTxbytes,'tnRoeMapperRawTxDropPackets':tnRoeMapperRawTxDropPackets,'tnRoeMapperRawEncapQueueOverrun':tnRoeMapperRawEncapQueueOverrun,'tnRoeMapperRawGSMTimeSlotMismatch':tnRoeMapperRawGSMTimeSlotMismatch,'tnRoeDeMapperRawCountStatsAttributeTotal':tnRoeDeMapperRawCountStatsAttributeTotal,'tnRoeDeMapperRawCountStatsTable':tnRoeDeMapperRawCountStatsTable,'tnRoeDeMapperRawCountStatsEntry':tnRoeDeMapperRawCountStatsEntry,_AB:tnRoeDeMapperRawCountStatsPortId,'tnRoeDeMapperRawStatsDeMapperID':tnRoeDeMapperRawStatsDeMapperID,'tnRoeDeMapperRawCountStatsClear':tnRoeDeMapperRawCountStatsClear,'tnRoeDeMapperRawStatsStartTime':tnRoeDeMapperRawStatsStartTime,'tnRoeDeMapperRawRxpackets':tnRoeDeMapperRawRxpackets,'tnRoeDeMapperRawRxbytes':tnRoeDeMapperRawRxbytes,'tnRoeDeMapperRawDecapQueueOverrun':tnRoeDeMapperRawDecapQueueOverrun,'tnRoeDeMapperRawQueueUnderrun':tnRoeDeMapperRawQueueUnderrun,'tnRoeDeMapperRawDecapPacketMissing':tnRoeDeMapperRawDecapPacketMissing,'tnRoeDeMapperRawDecapPacketSizeMismatch':tnRoeDeMapperRawDecapPacketSizeMismatch,'tnRoeRawCountStatsAttributeTotal':tnRoeRawCountStatsAttributeTotal,'tnRoeRawCountStatsTable':tnRoeRawCountStatsTable,'tnRoeRawCountStatsEntry':tnRoeRawCountStatsEntry,_AC:tnRoeRawStatsPortId,'tnRoeRawCountStatsClear':tnRoeRawCountStatsClear,'tnRoeRawStatsStartTime':tnRoeRawStatsStartTime,'tnRoeRawDecapPktsDropped':tnRoeRawDecapPktsDropped})