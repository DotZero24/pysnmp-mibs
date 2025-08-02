_Q='coiPcsPmIntervalNumber'
_P='coiPcsPmHistoryIntervalType'
_O='coiPcsPmCurrentIntervalType'
_N='coiFecPmIntervalNumber'
_M='coiFecPmHistoryIntervalType'
_L='coiFecPmCurrentIntervalType'
_K='coiFcPmIntervalNumber'
_J='coiFcPmHistoryIntervalType'
_I='coiFcPmCurrentIntervalType'
_H='not-accessible'
_G='Unsigned32'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='CISCO-FIBRECHANNEL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,ifName=mibBuilder.importSymbols(_D,_E,'ifName')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoFibreChanMIB=ModuleIdentity((1,3,6,1,4,1,9,9,1053))
class CoiIntervalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fifteenMin',1),('oneDay',2),('thirtySeconds',3)))
_CiscoFibreChanMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoFibreChanMIBNotifs=_CiscoFibreChanMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,1053,0))
_CiscoFibreChanMIBObjects_ObjectIdentity=ObjectIdentity
ciscoFibreChanMIBObjects=_CiscoFibreChanMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1))
_CoiFibreChanController_ObjectIdentity=ObjectIdentity
coiFibreChanController=_CoiFibreChanController_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,1))
_CoiFibreChanControllerTable_Object=MibTable
coiFibreChanControllerTable=_CoiFibreChanControllerTable_Object((1,3,6,1,4,1,9,9,1053,1,1,1))
if mibBuilder.loadTexts:coiFibreChanControllerTable.setStatus(_A)
_CoiFibreChanControllerEntry_Object=MibTableRow
coiFibreChanControllerEntry=_CoiFibreChanControllerEntry_Object((1,3,6,1,4,1,9,9,1053,1,1,1,1))
coiFibreChanControllerEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:coiFibreChanControllerEntry.setStatus(_A)
class _CoiFibreChanControllerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_CoiFibreChanControllerAdminStatus_Type.__name__=_F
_CoiFibreChanControllerAdminStatus_Object=MibTableColumn
coiFibreChanControllerAdminStatus=_CoiFibreChanControllerAdminStatus_Object((1,3,6,1,4,1,9,9,1053,1,1,1,1,1),_CoiFibreChanControllerAdminStatus_Type())
coiFibreChanControllerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFibreChanControllerAdminStatus.setStatus(_A)
class _CoiFibreChanControllerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('down',0),('up',1)))
_CoiFibreChanControllerOperStatus_Type.__name__=_F
_CoiFibreChanControllerOperStatus_Object=MibTableColumn
coiFibreChanControllerOperStatus=_CoiFibreChanControllerOperStatus_Object((1,3,6,1,4,1,9,9,1053,1,1,1,1,2),_CoiFibreChanControllerOperStatus_Type())
coiFibreChanControllerOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFibreChanControllerOperStatus.setStatus(_A)
class _CoiFibreChanControllerLoopbackInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('loopbackNone',0),('loopbackLine',1),('loopbackInternal',2)))
_CoiFibreChanControllerLoopbackInfo_Type.__name__=_F
_CoiFibreChanControllerLoopbackInfo_Object=MibTableColumn
coiFibreChanControllerLoopbackInfo=_CoiFibreChanControllerLoopbackInfo_Object((1,3,6,1,4,1,9,9,1053,1,1,1,1,3),_CoiFibreChanControllerLoopbackInfo_Type())
coiFibreChanControllerLoopbackInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFibreChanControllerLoopbackInfo.setStatus(_A)
class _CoiFibreChanControllerAlarmStatus_Type(Bits):namedValues=NamedValues(*(('noAlarm',0),('los',1),('syncLoss',2),('pcsErr',3),('hiBer',4),('localFault',5),('remoteFault',6),('nos',7),('squelch',8)))
_CoiFibreChanControllerAlarmStatus_Type.__name__='Bits'
_CoiFibreChanControllerAlarmStatus_Object=MibTableColumn
coiFibreChanControllerAlarmStatus=_CoiFibreChanControllerAlarmStatus_Object((1,3,6,1,4,1,9,9,1053,1,1,1,1,4),_CoiFibreChanControllerAlarmStatus_Type())
coiFibreChanControllerAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFibreChanControllerAlarmStatus.setStatus(_A)
_CoiFcPm_ObjectIdentity=ObjectIdentity
coiFcPm=_CoiFcPm_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,2))
_CoiFcPmCurrentTable_ObjectIdentity=ObjectIdentity
coiFcPmCurrentTable=_CoiFcPmCurrentTable_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,2,1))
_CoiFcPmCurrentEntry_Object=MibTableRow
coiFcPmCurrentEntry=_CoiFcPmCurrentEntry_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1))
coiFcPmCurrentEntry.setIndexNames((0,_D,_E),(0,_C,_I))
if mibBuilder.loadTexts:coiFcPmCurrentEntry.setStatus(_A)
_CoiFcPmCurrentIntervalType_Type=CoiIntervalType
_CoiFcPmCurrentIntervalType_Object=MibTableColumn
coiFcPmCurrentIntervalType=_CoiFcPmCurrentIntervalType_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,1),_CoiFcPmCurrentIntervalType_Type())
coiFcPmCurrentIntervalType.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmCurrentIntervalType.setStatus(_A)
_CoiFcPmIfInOctets_Type=Counter64
_CoiFcPmIfInOctets_Object=MibTableColumn
coiFcPmIfInOctets=_CoiFcPmIfInOctets_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,2),_CoiFcPmIfInOctets_Type())
coiFcPmIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmIfInOctets.setStatus(_A)
_CoiFcPmRxTotalPkts_Type=Counter64
_CoiFcPmRxTotalPkts_Object=MibTableColumn
coiFcPmRxTotalPkts=_CoiFcPmRxTotalPkts_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,3),_CoiFcPmRxTotalPkts_Type())
coiFcPmRxTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmRxTotalPkts.setStatus(_A)
_CoiFcPmIfInErrors_Type=Counter64
_CoiFcPmIfInErrors_Object=MibTableColumn
coiFcPmIfInErrors=_CoiFcPmIfInErrors_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,4),_CoiFcPmIfInErrors_Type())
coiFcPmIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmIfInErrors.setStatus(_A)
_CoiFcPmRxBadFcs_Type=Counter64
_CoiFcPmRxBadFcs_Object=MibTableColumn
coiFcPmRxBadFcs=_CoiFcPmRxBadFcs_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,5),_CoiFcPmRxBadFcs_Type())
coiFcPmRxBadFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmRxBadFcs.setStatus(_A)
_CoiFcPmRxFramesTooShort_Type=Counter64
_CoiFcPmRxFramesTooShort_Object=MibTableColumn
coiFcPmRxFramesTooShort=_CoiFcPmRxFramesTooShort_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,6),_CoiFcPmRxFramesTooShort_Type())
coiFcPmRxFramesTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmRxFramesTooShort.setStatus(_A)
_CoiFcPmRxFramesTooLong_Type=Counter64
_CoiFcPmRxFramesTooLong_Object=MibTableColumn
coiFcPmRxFramesTooLong=_CoiFcPmRxFramesTooLong_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,7),_CoiFcPmRxFramesTooLong_Type())
coiFcPmRxFramesTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmRxFramesTooLong.setStatus(_A)
_CoiFcPmIfOutOctets_Type=Counter64
_CoiFcPmIfOutOctets_Object=MibTableColumn
coiFcPmIfOutOctets=_CoiFcPmIfOutOctets_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,8),_CoiFcPmIfOutOctets_Type())
coiFcPmIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmIfOutOctets.setStatus(_A)
_CoiFcPmTxTotalPkts_Type=Counter64
_CoiFcPmTxTotalPkts_Object=MibTableColumn
coiFcPmTxTotalPkts=_CoiFcPmTxTotalPkts_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,9),_CoiFcPmTxTotalPkts_Type())
coiFcPmTxTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmTxTotalPkts.setStatus(_A)
_CoiFcPmTxBadFcs_Type=Counter64
_CoiFcPmTxBadFcs_Object=MibTableColumn
coiFcPmTxBadFcs=_CoiFcPmTxBadFcs_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,10),_CoiFcPmTxBadFcs_Type())
coiFcPmTxBadFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmTxBadFcs.setStatus(_A)
_CoiFcPmTxFramesTooShort_Type=Counter64
_CoiFcPmTxFramesTooShort_Object=MibTableColumn
coiFcPmTxFramesTooShort=_CoiFcPmTxFramesTooShort_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,11),_CoiFcPmTxFramesTooShort_Type())
coiFcPmTxFramesTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmTxFramesTooShort.setStatus(_A)
_CoiFcPmTxFramesTooLong_Type=Counter64
_CoiFcPmTxFramesTooLong_Object=MibTableColumn
coiFcPmTxFramesTooLong=_CoiFcPmTxFramesTooLong_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,12),_CoiFcPmTxFramesTooLong_Type())
coiFcPmTxFramesTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmTxFramesTooLong.setStatus(_A)
_CoiFcCurrentPmValidData_Type=TruthValue
_CoiFcCurrentPmValidData_Object=MibTableColumn
coiFcCurrentPmValidData=_CoiFcCurrentPmValidData_Object((1,3,6,1,4,1,9,9,1053,1,2,1,1,13),_CoiFcCurrentPmValidData_Type())
coiFcCurrentPmValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcCurrentPmValidData.setStatus(_A)
_CoiFcPmHistoryTable_ObjectIdentity=ObjectIdentity
coiFcPmHistoryTable=_CoiFcPmHistoryTable_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,2,2))
_CoiFcPmHistoryEntry_Object=MibTableRow
coiFcPmHistoryEntry=_CoiFcPmHistoryEntry_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1))
coiFcPmHistoryEntry.setIndexNames((0,_D,_E),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:coiFcPmHistoryEntry.setStatus(_A)
_CoiFcPmHistoryIntervalType_Type=CoiIntervalType
_CoiFcPmHistoryIntervalType_Object=MibTableColumn
coiFcPmHistoryIntervalType=_CoiFcPmHistoryIntervalType_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,1),_CoiFcPmHistoryIntervalType_Type())
coiFcPmHistoryIntervalType.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryIntervalType.setStatus(_A)
class _CoiFcPmIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CoiFcPmIntervalNumber_Type.__name__=_G
_CoiFcPmIntervalNumber_Object=MibTableColumn
coiFcPmIntervalNumber=_CoiFcPmIntervalNumber_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,2),_CoiFcPmIntervalNumber_Type())
coiFcPmIntervalNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:coiFcPmIntervalNumber.setStatus(_A)
_CoiFcPmHistoryIfInOctets_Type=Counter64
_CoiFcPmHistoryIfInOctets_Object=MibTableColumn
coiFcPmHistoryIfInOctets=_CoiFcPmHistoryIfInOctets_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,3),_CoiFcPmHistoryIfInOctets_Type())
coiFcPmHistoryIfInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryIfInOctets.setStatus(_A)
_CoiFcPmHistoryRxTotalPkts_Type=Counter64
_CoiFcPmHistoryRxTotalPkts_Object=MibTableColumn
coiFcPmHistoryRxTotalPkts=_CoiFcPmHistoryRxTotalPkts_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,4),_CoiFcPmHistoryRxTotalPkts_Type())
coiFcPmHistoryRxTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryRxTotalPkts.setStatus(_A)
_CoiFcPmHistoryIfInErrors_Type=Counter64
_CoiFcPmHistoryIfInErrors_Object=MibTableColumn
coiFcPmHistoryIfInErrors=_CoiFcPmHistoryIfInErrors_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,5),_CoiFcPmHistoryIfInErrors_Type())
coiFcPmHistoryIfInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryIfInErrors.setStatus(_A)
_CoiFcPmHistoryRxBadFcs_Type=Counter64
_CoiFcPmHistoryRxBadFcs_Object=MibTableColumn
coiFcPmHistoryRxBadFcs=_CoiFcPmHistoryRxBadFcs_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,6),_CoiFcPmHistoryRxBadFcs_Type())
coiFcPmHistoryRxBadFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryRxBadFcs.setStatus(_A)
_CoiFcPmHistoryRxFramesTooShort_Type=Counter64
_CoiFcPmHistoryRxFramesTooShort_Object=MibTableColumn
coiFcPmHistoryRxFramesTooShort=_CoiFcPmHistoryRxFramesTooShort_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,7),_CoiFcPmHistoryRxFramesTooShort_Type())
coiFcPmHistoryRxFramesTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryRxFramesTooShort.setStatus(_A)
_CoiFcPmHistoryRxFramesTooLong_Type=Counter64
_CoiFcPmHistoryRxFramesTooLong_Object=MibTableColumn
coiFcPmHistoryRxFramesTooLong=_CoiFcPmHistoryRxFramesTooLong_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,8),_CoiFcPmHistoryRxFramesTooLong_Type())
coiFcPmHistoryRxFramesTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryRxFramesTooLong.setStatus(_A)
_CoiFcPmHistoryIfOutOctets_Type=Counter64
_CoiFcPmHistoryIfOutOctets_Object=MibTableColumn
coiFcPmHistoryIfOutOctets=_CoiFcPmHistoryIfOutOctets_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,9),_CoiFcPmHistoryIfOutOctets_Type())
coiFcPmHistoryIfOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryIfOutOctets.setStatus(_A)
_CoiFcPmHistoryTxTotalPkts_Type=Counter64
_CoiFcPmHistoryTxTotalPkts_Object=MibTableColumn
coiFcPmHistoryTxTotalPkts=_CoiFcPmHistoryTxTotalPkts_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,10),_CoiFcPmHistoryTxTotalPkts_Type())
coiFcPmHistoryTxTotalPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryTxTotalPkts.setStatus(_A)
_CoiFcPmHistoryTxBadFcs_Type=Counter64
_CoiFcPmHistoryTxBadFcs_Object=MibTableColumn
coiFcPmHistoryTxBadFcs=_CoiFcPmHistoryTxBadFcs_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,11),_CoiFcPmHistoryTxBadFcs_Type())
coiFcPmHistoryTxBadFcs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryTxBadFcs.setStatus(_A)
_CoiFcPmHistoryTxFramesTooShort_Type=Counter64
_CoiFcPmHistoryTxFramesTooShort_Object=MibTableColumn
coiFcPmHistoryTxFramesTooShort=_CoiFcPmHistoryTxFramesTooShort_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,12),_CoiFcPmHistoryTxFramesTooShort_Type())
coiFcPmHistoryTxFramesTooShort.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryTxFramesTooShort.setStatus(_A)
_CoiFcPmHistoryTxFramesTooLong_Type=Counter64
_CoiFcPmHistoryTxFramesTooLong_Object=MibTableColumn
coiFcPmHistoryTxFramesTooLong=_CoiFcPmHistoryTxFramesTooLong_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,13),_CoiFcPmHistoryTxFramesTooLong_Type())
coiFcPmHistoryTxFramesTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryTxFramesTooLong.setStatus(_A)
_CoiFcPmHistoryValidData_Type=TruthValue
_CoiFcPmHistoryValidData_Object=MibTableColumn
coiFcPmHistoryValidData=_CoiFcPmHistoryValidData_Object((1,3,6,1,4,1,9,9,1053,1,2,2,1,14),_CoiFcPmHistoryValidData_Type())
coiFcPmHistoryValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFcPmHistoryValidData.setStatus(_A)
_CoiFecPm_ObjectIdentity=ObjectIdentity
coiFecPm=_CoiFecPm_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,3))
_CoiFecPmCurrentTable_ObjectIdentity=ObjectIdentity
coiFecPmCurrentTable=_CoiFecPmCurrentTable_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,3,1))
_CoiFecPmCurrentEntry_Object=MibTableRow
coiFecPmCurrentEntry=_CoiFecPmCurrentEntry_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1))
coiFecPmCurrentEntry.setIndexNames((0,_D,_E),(0,_C,_L))
if mibBuilder.loadTexts:coiFecPmCurrentEntry.setStatus(_A)
_CoiFecPmCurrentIntervalType_Type=CoiIntervalType
_CoiFecPmCurrentIntervalType_Object=MibTableColumn
coiFecPmCurrentIntervalType=_CoiFecPmCurrentIntervalType_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,1),_CoiFecPmCurrentIntervalType_Type())
coiFecPmCurrentIntervalType.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmCurrentIntervalType.setStatus(_A)
_CoiFecPmCorWordErrs_Type=Counter64
_CoiFecPmCorWordErrs_Object=MibTableColumn
coiFecPmCorWordErrs=_CoiFecPmCorWordErrs_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,2),_CoiFecPmCorWordErrs_Type())
coiFecPmCorWordErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmCorWordErrs.setStatus(_A)
_CoiFecPmUncorWords_Type=Counter64
_CoiFecPmUncorWords_Object=MibTableColumn
coiFecPmUncorWords=_CoiFecPmUncorWords_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,3),_CoiFecPmUncorWords_Type())
coiFecPmUncorWords.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmUncorWords.setStatus(_A)
_CoiFecPmPreFECMin_Type=DisplayString
_CoiFecPmPreFECMin_Object=MibTableColumn
coiFecPmPreFECMin=_CoiFecPmPreFECMin_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,4),_CoiFecPmPreFECMin_Type())
coiFecPmPreFECMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmPreFECMin.setStatus(_A)
_CoiFecPmPreFECMax_Type=DisplayString
_CoiFecPmPreFECMax_Object=MibTableColumn
coiFecPmPreFECMax=_CoiFecPmPreFECMax_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,5),_CoiFecPmPreFECMax_Type())
coiFecPmPreFECMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmPreFECMax.setStatus(_A)
_CoiFecPmPreFECAvg_Type=DisplayString
_CoiFecPmPreFECAvg_Object=MibTableColumn
coiFecPmPreFECAvg=_CoiFecPmPreFECAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,6),_CoiFecPmPreFECAvg_Type())
coiFecPmPreFECAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmPreFECAvg.setStatus(_A)
_CoiFecPmPostFECMin_Type=DisplayString
_CoiFecPmPostFECMin_Object=MibTableColumn
coiFecPmPostFECMin=_CoiFecPmPostFECMin_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,7),_CoiFecPmPostFECMin_Type())
coiFecPmPostFECMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmPostFECMin.setStatus(_A)
_CoiFecPmPostFECMax_Type=DisplayString
_CoiFecPmPostFECMax_Object=MibTableColumn
coiFecPmPostFECMax=_CoiFecPmPostFECMax_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,8),_CoiFecPmPostFECMax_Type())
coiFecPmPostFECMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmPostFECMax.setStatus(_A)
_CoiFecPmPostFECAvg_Type=DisplayString
_CoiFecPmPostFECAvg_Object=MibTableColumn
coiFecPmPostFECAvg=_CoiFecPmPostFECAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,9),_CoiFecPmPostFECAvg_Type())
coiFecPmPostFECAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmPostFECAvg.setStatus(_A)
_CoiFecPmQFactorMin_Type=DisplayString
_CoiFecPmQFactorMin_Object=MibTableColumn
coiFecPmQFactorMin=_CoiFecPmQFactorMin_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,10),_CoiFecPmQFactorMin_Type())
coiFecPmQFactorMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmQFactorMin.setStatus(_A)
_CoiFecPmQFactorMax_Type=DisplayString
_CoiFecPmQFactorMax_Object=MibTableColumn
coiFecPmQFactorMax=_CoiFecPmQFactorMax_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,11),_CoiFecPmQFactorMax_Type())
coiFecPmQFactorMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmQFactorMax.setStatus(_A)
_CoiFecPmQFactorAvg_Type=DisplayString
_CoiFecPmQFactorAvg_Object=MibTableColumn
coiFecPmQFactorAvg=_CoiFecPmQFactorAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,12),_CoiFecPmQFactorAvg_Type())
coiFecPmQFactorAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmQFactorAvg.setStatus(_A)
_CoiFecPmQMarginMin_Type=DisplayString
_CoiFecPmQMarginMin_Object=MibTableColumn
coiFecPmQMarginMin=_CoiFecPmQMarginMin_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,13),_CoiFecPmQMarginMin_Type())
coiFecPmQMarginMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmQMarginMin.setStatus(_A)
_CoiFecPmQMarginMax_Type=DisplayString
_CoiFecPmQMarginMax_Object=MibTableColumn
coiFecPmQMarginMax=_CoiFecPmQMarginMax_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,14),_CoiFecPmQMarginMax_Type())
coiFecPmQMarginMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmQMarginMax.setStatus(_A)
_CoiFecPmQMarginAvg_Type=DisplayString
_CoiFecPmQMarginAvg_Object=MibTableColumn
coiFecPmQMarginAvg=_CoiFecPmQMarginAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,15),_CoiFecPmQMarginAvg_Type())
coiFecPmQMarginAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmQMarginAvg.setStatus(_A)
_CoiFecPmInstQMarginMin_Type=DisplayString
_CoiFecPmInstQMarginMin_Object=MibTableColumn
coiFecPmInstQMarginMin=_CoiFecPmInstQMarginMin_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,16),_CoiFecPmInstQMarginMin_Type())
coiFecPmInstQMarginMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmInstQMarginMin.setStatus(_A)
_CoiFecPmInstQMarginMax_Type=DisplayString
_CoiFecPmInstQMarginMax_Object=MibTableColumn
coiFecPmInstQMarginMax=_CoiFecPmInstQMarginMax_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,17),_CoiFecPmInstQMarginMax_Type())
coiFecPmInstQMarginMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmInstQMarginMax.setStatus(_A)
_CoiFecPmInstQMarginAvg_Type=DisplayString
_CoiFecPmInstQMarginAvg_Object=MibTableColumn
coiFecPmInstQMarginAvg=_CoiFecPmInstQMarginAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,18),_CoiFecPmInstQMarginAvg_Type())
coiFecPmInstQMarginAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmInstQMarginAvg.setStatus(_A)
_CoiFecCurrentPmValidData_Type=TruthValue
_CoiFecCurrentPmValidData_Object=MibTableColumn
coiFecCurrentPmValidData=_CoiFecCurrentPmValidData_Object((1,3,6,1,4,1,9,9,1053,1,3,1,1,19),_CoiFecCurrentPmValidData_Type())
coiFecCurrentPmValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecCurrentPmValidData.setStatus(_A)
_CoiFecPmHistoryTable_ObjectIdentity=ObjectIdentity
coiFecPmHistoryTable=_CoiFecPmHistoryTable_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,3,2))
_CoiFecPmHistoryEntry_Object=MibTableRow
coiFecPmHistoryEntry=_CoiFecPmHistoryEntry_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1))
coiFecPmHistoryEntry.setIndexNames((0,_D,_E),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:coiFecPmHistoryEntry.setStatus(_A)
_CoiFecPmHistoryIntervalType_Type=CoiIntervalType
_CoiFecPmHistoryIntervalType_Object=MibTableColumn
coiFecPmHistoryIntervalType=_CoiFecPmHistoryIntervalType_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,1),_CoiFecPmHistoryIntervalType_Type())
coiFecPmHistoryIntervalType.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryIntervalType.setStatus(_A)
class _CoiFecPmIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CoiFecPmIntervalNumber_Type.__name__=_G
_CoiFecPmIntervalNumber_Object=MibTableColumn
coiFecPmIntervalNumber=_CoiFecPmIntervalNumber_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,2),_CoiFecPmIntervalNumber_Type())
coiFecPmIntervalNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:coiFecPmIntervalNumber.setStatus(_A)
_CoiFecPmHistoryCorWordErrs_Type=Counter64
_CoiFecPmHistoryCorWordErrs_Object=MibTableColumn
coiFecPmHistoryCorWordErrs=_CoiFecPmHistoryCorWordErrs_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,3),_CoiFecPmHistoryCorWordErrs_Type())
coiFecPmHistoryCorWordErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryCorWordErrs.setStatus(_A)
_CoiFecPmHistoryUncorWords_Type=Counter64
_CoiFecPmHistoryUncorWords_Object=MibTableColumn
coiFecPmHistoryUncorWords=_CoiFecPmHistoryUncorWords_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,4),_CoiFecPmHistoryUncorWords_Type())
coiFecPmHistoryUncorWords.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryUncorWords.setStatus(_A)
_CoiFecPmHistoryPreFECMin_Type=DisplayString
_CoiFecPmHistoryPreFECMin_Object=MibTableColumn
coiFecPmHistoryPreFECMin=_CoiFecPmHistoryPreFECMin_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,5),_CoiFecPmHistoryPreFECMin_Type())
coiFecPmHistoryPreFECMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryPreFECMin.setStatus(_A)
_CoiFecPmHistoryPreFECMax_Type=DisplayString
_CoiFecPmHistoryPreFECMax_Object=MibTableColumn
coiFecPmHistoryPreFECMax=_CoiFecPmHistoryPreFECMax_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,6),_CoiFecPmHistoryPreFECMax_Type())
coiFecPmHistoryPreFECMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryPreFECMax.setStatus(_A)
_CoiFecPmHistoryPreFECAvg_Type=DisplayString
_CoiFecPmHistoryPreFECAvg_Object=MibTableColumn
coiFecPmHistoryPreFECAvg=_CoiFecPmHistoryPreFECAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,7),_CoiFecPmHistoryPreFECAvg_Type())
coiFecPmHistoryPreFECAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryPreFECAvg.setStatus(_A)
_CoiFecPmHistoryPostFECMin_Type=DisplayString
_CoiFecPmHistoryPostFECMin_Object=MibTableColumn
coiFecPmHistoryPostFECMin=_CoiFecPmHistoryPostFECMin_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,8),_CoiFecPmHistoryPostFECMin_Type())
coiFecPmHistoryPostFECMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryPostFECMin.setStatus(_A)
_CoiFecPmHistoryPostFECMax_Type=DisplayString
_CoiFecPmHistoryPostFECMax_Object=MibTableColumn
coiFecPmHistoryPostFECMax=_CoiFecPmHistoryPostFECMax_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,9),_CoiFecPmHistoryPostFECMax_Type())
coiFecPmHistoryPostFECMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryPostFECMax.setStatus(_A)
_CoiFecPmHistoryPostFECAvg_Type=DisplayString
_CoiFecPmHistoryPostFECAvg_Object=MibTableColumn
coiFecPmHistoryPostFECAvg=_CoiFecPmHistoryPostFECAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,10),_CoiFecPmHistoryPostFECAvg_Type())
coiFecPmHistoryPostFECAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryPostFECAvg.setStatus(_A)
_CoiFecPmHistoryQFactorMin_Type=DisplayString
_CoiFecPmHistoryQFactorMin_Object=MibTableColumn
coiFecPmHistoryQFactorMin=_CoiFecPmHistoryQFactorMin_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,11),_CoiFecPmHistoryQFactorMin_Type())
coiFecPmHistoryQFactorMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryQFactorMin.setStatus(_A)
_CoiFecPmHistoryQFactorMax_Type=DisplayString
_CoiFecPmHistoryQFactorMax_Object=MibTableColumn
coiFecPmHistoryQFactorMax=_CoiFecPmHistoryQFactorMax_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,12),_CoiFecPmHistoryQFactorMax_Type())
coiFecPmHistoryQFactorMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryQFactorMax.setStatus(_A)
_CoiFecPmHistoryQFactorAvg_Type=DisplayString
_CoiFecPmHistoryQFactorAvg_Object=MibTableColumn
coiFecPmHistoryQFactorAvg=_CoiFecPmHistoryQFactorAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,13),_CoiFecPmHistoryQFactorAvg_Type())
coiFecPmHistoryQFactorAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryQFactorAvg.setStatus(_A)
_CoiFecPmHistoryQMarginMin_Type=DisplayString
_CoiFecPmHistoryQMarginMin_Object=MibTableColumn
coiFecPmHistoryQMarginMin=_CoiFecPmHistoryQMarginMin_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,14),_CoiFecPmHistoryQMarginMin_Type())
coiFecPmHistoryQMarginMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryQMarginMin.setStatus(_A)
_CoiFecPmHistoryQMarginMax_Type=DisplayString
_CoiFecPmHistoryQMarginMax_Object=MibTableColumn
coiFecPmHistoryQMarginMax=_CoiFecPmHistoryQMarginMax_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,15),_CoiFecPmHistoryQMarginMax_Type())
coiFecPmHistoryQMarginMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryQMarginMax.setStatus(_A)
_CoiFecPmHistoryQMarginAvg_Type=DisplayString
_CoiFecPmHistoryQMarginAvg_Object=MibTableColumn
coiFecPmHistoryQMarginAvg=_CoiFecPmHistoryQMarginAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,16),_CoiFecPmHistoryQMarginAvg_Type())
coiFecPmHistoryQMarginAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryQMarginAvg.setStatus(_A)
_CoiFecPmHistoryInstQMarginMin_Type=DisplayString
_CoiFecPmHistoryInstQMarginMin_Object=MibTableColumn
coiFecPmHistoryInstQMarginMin=_CoiFecPmHistoryInstQMarginMin_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,17),_CoiFecPmHistoryInstQMarginMin_Type())
coiFecPmHistoryInstQMarginMin.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryInstQMarginMin.setStatus(_A)
_CoiFecPmHistoryInstQMarginMax_Type=DisplayString
_CoiFecPmHistoryInstQMarginMax_Object=MibTableColumn
coiFecPmHistoryInstQMarginMax=_CoiFecPmHistoryInstQMarginMax_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,18),_CoiFecPmHistoryInstQMarginMax_Type())
coiFecPmHistoryInstQMarginMax.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryInstQMarginMax.setStatus(_A)
_CoiFecPmHistoryInstQMarginAvg_Type=DisplayString
_CoiFecPmHistoryInstQMarginAvg_Object=MibTableColumn
coiFecPmHistoryInstQMarginAvg=_CoiFecPmHistoryInstQMarginAvg_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,19),_CoiFecPmHistoryInstQMarginAvg_Type())
coiFecPmHistoryInstQMarginAvg.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryInstQMarginAvg.setStatus(_A)
_CoiFecPmHistoryValidData_Type=TruthValue
_CoiFecPmHistoryValidData_Object=MibTableColumn
coiFecPmHistoryValidData=_CoiFecPmHistoryValidData_Object((1,3,6,1,4,1,9,9,1053,1,3,2,1,20),_CoiFecPmHistoryValidData_Type())
coiFecPmHistoryValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiFecPmHistoryValidData.setStatus(_A)
_CoiPcsPm_ObjectIdentity=ObjectIdentity
coiPcsPm=_CoiPcsPm_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,4))
_CoiPcsPmCurrentTable_ObjectIdentity=ObjectIdentity
coiPcsPmCurrentTable=_CoiPcsPmCurrentTable_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,4,1))
_CoiPcsPmCurrentEntry_Object=MibTableRow
coiPcsPmCurrentEntry=_CoiPcsPmCurrentEntry_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1))
coiPcsPmCurrentEntry.setIndexNames((0,_D,_E),(0,_C,_O))
if mibBuilder.loadTexts:coiPcsPmCurrentEntry.setStatus(_A)
_CoiPcsPmCurrentIntervalType_Type=CoiIntervalType
_CoiPcsPmCurrentIntervalType_Object=MibTableColumn
coiPcsPmCurrentIntervalType=_CoiPcsPmCurrentIntervalType_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,1),_CoiPcsPmCurrentIntervalType_Type())
coiPcsPmCurrentIntervalType.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmCurrentIntervalType.setStatus(_A)
_CoiPcsPmCumBip_Type=Counter64
_CoiPcsPmCumBip_Object=MibTableColumn
coiPcsPmCumBip=_CoiPcsPmCumBip_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,2),_CoiPcsPmCumBip_Type())
coiPcsPmCumBip.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmCumBip.setStatus(_A)
_CoiPcsPmCumFrmError_Type=Counter64
_CoiPcsPmCumFrmError_Object=MibTableColumn
coiPcsPmCumFrmError=_CoiPcsPmCumFrmError_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,3),_CoiPcsPmCumFrmError_Type())
coiPcsPmCumFrmError.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmCumFrmError.setStatus(_A)
_CoiPcsPmCumBadSh_Type=Counter64
_CoiPcsPmCumBadSh_Object=MibTableColumn
coiPcsPmCumBadSh=_CoiPcsPmCumBadSh_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,4),_CoiPcsPmCumBadSh_Type())
coiPcsPmCumBadSh.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmCumBadSh.setStatus(_A)
_CoiPcsPmEs_Type=Counter64
_CoiPcsPmEs_Object=MibTableColumn
coiPcsPmEs=_CoiPcsPmEs_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,5),_CoiPcsPmEs_Type())
coiPcsPmEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmEs.setStatus(_A)
_CoiPcsPmSes_Type=Counter64
_CoiPcsPmSes_Object=MibTableColumn
coiPcsPmSes=_CoiPcsPmSes_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,6),_CoiPcsPmSes_Type())
coiPcsPmSes.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmSes.setStatus(_A)
_CoiPcsPmUas_Type=Counter64
_CoiPcsPmUas_Object=MibTableColumn
coiPcsPmUas=_CoiPcsPmUas_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,7),_CoiPcsPmUas_Type())
coiPcsPmUas.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmUas.setStatus(_A)
_CoiPcsPmFarEndEs_Type=Counter64
_CoiPcsPmFarEndEs_Object=MibTableColumn
coiPcsPmFarEndEs=_CoiPcsPmFarEndEs_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,8),_CoiPcsPmFarEndEs_Type())
coiPcsPmFarEndEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmFarEndEs.setStatus(_A)
_CoiPcsPmFarEndSes_Type=Counter64
_CoiPcsPmFarEndSes_Object=MibTableColumn
coiPcsPmFarEndSes=_CoiPcsPmFarEndSes_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,9),_CoiPcsPmFarEndSes_Type())
coiPcsPmFarEndSes.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmFarEndSes.setStatus(_A)
_CoiPcsPmFarEndUas_Type=Counter64
_CoiPcsPmFarEndUas_Object=MibTableColumn
coiPcsPmFarEndUas=_CoiPcsPmFarEndUas_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,10),_CoiPcsPmFarEndUas_Type())
coiPcsPmFarEndUas.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmFarEndUas.setStatus(_A)
_CoiPcsCurrentPmValidData_Type=TruthValue
_CoiPcsCurrentPmValidData_Object=MibTableColumn
coiPcsCurrentPmValidData=_CoiPcsCurrentPmValidData_Object((1,3,6,1,4,1,9,9,1053,1,4,1,1,11),_CoiPcsCurrentPmValidData_Type())
coiPcsCurrentPmValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsCurrentPmValidData.setStatus(_A)
_CoiPcsPmHistoryTable_ObjectIdentity=ObjectIdentity
coiPcsPmHistoryTable=_CoiPcsPmHistoryTable_ObjectIdentity((1,3,6,1,4,1,9,9,1053,1,4,2))
_CoiPcsPmHistoryEntry_Object=MibTableRow
coiPcsPmHistoryEntry=_CoiPcsPmHistoryEntry_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1))
coiPcsPmHistoryEntry.setIndexNames((0,_D,_E),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:coiPcsPmHistoryEntry.setStatus(_A)
_CoiPcsPmHistoryIntervalType_Type=CoiIntervalType
_CoiPcsPmHistoryIntervalType_Object=MibTableColumn
coiPcsPmHistoryIntervalType=_CoiPcsPmHistoryIntervalType_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,1),_CoiPcsPmHistoryIntervalType_Type())
coiPcsPmHistoryIntervalType.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryIntervalType.setStatus(_A)
class _CoiPcsPmIntervalNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CoiPcsPmIntervalNumber_Type.__name__=_G
_CoiPcsPmIntervalNumber_Object=MibTableColumn
coiPcsPmIntervalNumber=_CoiPcsPmIntervalNumber_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,2),_CoiPcsPmIntervalNumber_Type())
coiPcsPmIntervalNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:coiPcsPmIntervalNumber.setStatus(_A)
_CoiPcsPmHistoryCumBip_Type=Counter64
_CoiPcsPmHistoryCumBip_Object=MibTableColumn
coiPcsPmHistoryCumBip=_CoiPcsPmHistoryCumBip_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,3),_CoiPcsPmHistoryCumBip_Type())
coiPcsPmHistoryCumBip.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryCumBip.setStatus(_A)
_CoiPcsPmHistoryCumFrmError_Type=Counter64
_CoiPcsPmHistoryCumFrmError_Object=MibTableColumn
coiPcsPmHistoryCumFrmError=_CoiPcsPmHistoryCumFrmError_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,4),_CoiPcsPmHistoryCumFrmError_Type())
coiPcsPmHistoryCumFrmError.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryCumFrmError.setStatus(_A)
_CoiPcsPmHistoryCumBadSh_Type=Counter64
_CoiPcsPmHistoryCumBadSh_Object=MibTableColumn
coiPcsPmHistoryCumBadSh=_CoiPcsPmHistoryCumBadSh_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,5),_CoiPcsPmHistoryCumBadSh_Type())
coiPcsPmHistoryCumBadSh.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryCumBadSh.setStatus(_A)
_CoiPcsPmHistoryEs_Type=Counter64
_CoiPcsPmHistoryEs_Object=MibTableColumn
coiPcsPmHistoryEs=_CoiPcsPmHistoryEs_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,6),_CoiPcsPmHistoryEs_Type())
coiPcsPmHistoryEs.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryEs.setStatus(_A)
_CoiPcsPmHistorySes_Type=Counter64
_CoiPcsPmHistorySes_Object=MibTableColumn
coiPcsPmHistorySes=_CoiPcsPmHistorySes_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,7),_CoiPcsPmHistorySes_Type())
coiPcsPmHistorySes.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistorySes.setStatus(_A)
_CoiPcsPmHistoryUas_Type=Counter64
_CoiPcsPmHistoryUas_Object=MibTableColumn
coiPcsPmHistoryUas=_CoiPcsPmHistoryUas_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,8),_CoiPcsPmHistoryUas_Type())
coiPcsPmHistoryUas.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryUas.setStatus(_A)
_CoiPcsPmHistoryEsFe_Type=Counter64
_CoiPcsPmHistoryEsFe_Object=MibTableColumn
coiPcsPmHistoryEsFe=_CoiPcsPmHistoryEsFe_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,9),_CoiPcsPmHistoryEsFe_Type())
coiPcsPmHistoryEsFe.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryEsFe.setStatus(_A)
_CoiPcsPmHistorySesFe_Type=Counter64
_CoiPcsPmHistorySesFe_Object=MibTableColumn
coiPcsPmHistorySesFe=_CoiPcsPmHistorySesFe_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,10),_CoiPcsPmHistorySesFe_Type())
coiPcsPmHistorySesFe.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistorySesFe.setStatus(_A)
_CoiPcsPmHistoryUasFe_Type=Counter64
_CoiPcsPmHistoryUasFe_Object=MibTableColumn
coiPcsPmHistoryUasFe=_CoiPcsPmHistoryUasFe_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,11),_CoiPcsPmHistoryUasFe_Type())
coiPcsPmHistoryUasFe.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryUasFe.setStatus(_A)
_CoiPcsPmHistoryValidData_Type=TruthValue
_CoiPcsPmHistoryValidData_Object=MibTableColumn
coiPcsPmHistoryValidData=_CoiPcsPmHistoryValidData_Object((1,3,6,1,4,1,9,9,1053,1,4,2,1,12),_CoiPcsPmHistoryValidData_Type())
coiPcsPmHistoryValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:coiPcsPmHistoryValidData.setStatus(_A)
_CiscoFibreChanMIBConformance_ObjectIdentity=ObjectIdentity
ciscoFibreChanMIBConformance=_CiscoFibreChanMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,1053,2))
_CiscoFibreChanMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoFibreChanMIBCompliances=_CiscoFibreChanMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,1053,2,1))
_CiscoFibreChanMIBGroups_ObjectIdentity=ObjectIdentity
ciscoFibreChanMIBGroups=_CiscoFibreChanMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,1053,2,2))
mibBuilder.exportSymbols(_C,**{'CoiIntervalType':CoiIntervalType,'ciscoFibreChanMIB':ciscoFibreChanMIB,'ciscoFibreChanMIBNotifs':ciscoFibreChanMIBNotifs,'ciscoFibreChanMIBObjects':ciscoFibreChanMIBObjects,'coiFibreChanController':coiFibreChanController,'coiFibreChanControllerTable':coiFibreChanControllerTable,'coiFibreChanControllerEntry':coiFibreChanControllerEntry,'coiFibreChanControllerAdminStatus':coiFibreChanControllerAdminStatus,'coiFibreChanControllerOperStatus':coiFibreChanControllerOperStatus,'coiFibreChanControllerLoopbackInfo':coiFibreChanControllerLoopbackInfo,'coiFibreChanControllerAlarmStatus':coiFibreChanControllerAlarmStatus,'coiFcPm':coiFcPm,'coiFcPmCurrentTable':coiFcPmCurrentTable,'coiFcPmCurrentEntry':coiFcPmCurrentEntry,_I:coiFcPmCurrentIntervalType,'coiFcPmIfInOctets':coiFcPmIfInOctets,'coiFcPmRxTotalPkts':coiFcPmRxTotalPkts,'coiFcPmIfInErrors':coiFcPmIfInErrors,'coiFcPmRxBadFcs':coiFcPmRxBadFcs,'coiFcPmRxFramesTooShort':coiFcPmRxFramesTooShort,'coiFcPmRxFramesTooLong':coiFcPmRxFramesTooLong,'coiFcPmIfOutOctets':coiFcPmIfOutOctets,'coiFcPmTxTotalPkts':coiFcPmTxTotalPkts,'coiFcPmTxBadFcs':coiFcPmTxBadFcs,'coiFcPmTxFramesTooShort':coiFcPmTxFramesTooShort,'coiFcPmTxFramesTooLong':coiFcPmTxFramesTooLong,'coiFcCurrentPmValidData':coiFcCurrentPmValidData,'coiFcPmHistoryTable':coiFcPmHistoryTable,'coiFcPmHistoryEntry':coiFcPmHistoryEntry,_J:coiFcPmHistoryIntervalType,_K:coiFcPmIntervalNumber,'coiFcPmHistoryIfInOctets':coiFcPmHistoryIfInOctets,'coiFcPmHistoryRxTotalPkts':coiFcPmHistoryRxTotalPkts,'coiFcPmHistoryIfInErrors':coiFcPmHistoryIfInErrors,'coiFcPmHistoryRxBadFcs':coiFcPmHistoryRxBadFcs,'coiFcPmHistoryRxFramesTooShort':coiFcPmHistoryRxFramesTooShort,'coiFcPmHistoryRxFramesTooLong':coiFcPmHistoryRxFramesTooLong,'coiFcPmHistoryIfOutOctets':coiFcPmHistoryIfOutOctets,'coiFcPmHistoryTxTotalPkts':coiFcPmHistoryTxTotalPkts,'coiFcPmHistoryTxBadFcs':coiFcPmHistoryTxBadFcs,'coiFcPmHistoryTxFramesTooShort':coiFcPmHistoryTxFramesTooShort,'coiFcPmHistoryTxFramesTooLong':coiFcPmHistoryTxFramesTooLong,'coiFcPmHistoryValidData':coiFcPmHistoryValidData,'coiFecPm':coiFecPm,'coiFecPmCurrentTable':coiFecPmCurrentTable,'coiFecPmCurrentEntry':coiFecPmCurrentEntry,_L:coiFecPmCurrentIntervalType,'coiFecPmCorWordErrs':coiFecPmCorWordErrs,'coiFecPmUncorWords':coiFecPmUncorWords,'coiFecPmPreFECMin':coiFecPmPreFECMin,'coiFecPmPreFECMax':coiFecPmPreFECMax,'coiFecPmPreFECAvg':coiFecPmPreFECAvg,'coiFecPmPostFECMin':coiFecPmPostFECMin,'coiFecPmPostFECMax':coiFecPmPostFECMax,'coiFecPmPostFECAvg':coiFecPmPostFECAvg,'coiFecPmQFactorMin':coiFecPmQFactorMin,'coiFecPmQFactorMax':coiFecPmQFactorMax,'coiFecPmQFactorAvg':coiFecPmQFactorAvg,'coiFecPmQMarginMin':coiFecPmQMarginMin,'coiFecPmQMarginMax':coiFecPmQMarginMax,'coiFecPmQMarginAvg':coiFecPmQMarginAvg,'coiFecPmInstQMarginMin':coiFecPmInstQMarginMin,'coiFecPmInstQMarginMax':coiFecPmInstQMarginMax,'coiFecPmInstQMarginAvg':coiFecPmInstQMarginAvg,'coiFecCurrentPmValidData':coiFecCurrentPmValidData,'coiFecPmHistoryTable':coiFecPmHistoryTable,'coiFecPmHistoryEntry':coiFecPmHistoryEntry,_M:coiFecPmHistoryIntervalType,_N:coiFecPmIntervalNumber,'coiFecPmHistoryCorWordErrs':coiFecPmHistoryCorWordErrs,'coiFecPmHistoryUncorWords':coiFecPmHistoryUncorWords,'coiFecPmHistoryPreFECMin':coiFecPmHistoryPreFECMin,'coiFecPmHistoryPreFECMax':coiFecPmHistoryPreFECMax,'coiFecPmHistoryPreFECAvg':coiFecPmHistoryPreFECAvg,'coiFecPmHistoryPostFECMin':coiFecPmHistoryPostFECMin,'coiFecPmHistoryPostFECMax':coiFecPmHistoryPostFECMax,'coiFecPmHistoryPostFECAvg':coiFecPmHistoryPostFECAvg,'coiFecPmHistoryQFactorMin':coiFecPmHistoryQFactorMin,'coiFecPmHistoryQFactorMax':coiFecPmHistoryQFactorMax,'coiFecPmHistoryQFactorAvg':coiFecPmHistoryQFactorAvg,'coiFecPmHistoryQMarginMin':coiFecPmHistoryQMarginMin,'coiFecPmHistoryQMarginMax':coiFecPmHistoryQMarginMax,'coiFecPmHistoryQMarginAvg':coiFecPmHistoryQMarginAvg,'coiFecPmHistoryInstQMarginMin':coiFecPmHistoryInstQMarginMin,'coiFecPmHistoryInstQMarginMax':coiFecPmHistoryInstQMarginMax,'coiFecPmHistoryInstQMarginAvg':coiFecPmHistoryInstQMarginAvg,'coiFecPmHistoryValidData':coiFecPmHistoryValidData,'coiPcsPm':coiPcsPm,'coiPcsPmCurrentTable':coiPcsPmCurrentTable,'coiPcsPmCurrentEntry':coiPcsPmCurrentEntry,_O:coiPcsPmCurrentIntervalType,'coiPcsPmCumBip':coiPcsPmCumBip,'coiPcsPmCumFrmError':coiPcsPmCumFrmError,'coiPcsPmCumBadSh':coiPcsPmCumBadSh,'coiPcsPmEs':coiPcsPmEs,'coiPcsPmSes':coiPcsPmSes,'coiPcsPmUas':coiPcsPmUas,'coiPcsPmFarEndEs':coiPcsPmFarEndEs,'coiPcsPmFarEndSes':coiPcsPmFarEndSes,'coiPcsPmFarEndUas':coiPcsPmFarEndUas,'coiPcsCurrentPmValidData':coiPcsCurrentPmValidData,'coiPcsPmHistoryTable':coiPcsPmHistoryTable,'coiPcsPmHistoryEntry':coiPcsPmHistoryEntry,_P:coiPcsPmHistoryIntervalType,_Q:coiPcsPmIntervalNumber,'coiPcsPmHistoryCumBip':coiPcsPmHistoryCumBip,'coiPcsPmHistoryCumFrmError':coiPcsPmHistoryCumFrmError,'coiPcsPmHistoryCumBadSh':coiPcsPmHistoryCumBadSh,'coiPcsPmHistoryEs':coiPcsPmHistoryEs,'coiPcsPmHistorySes':coiPcsPmHistorySes,'coiPcsPmHistoryUas':coiPcsPmHistoryUas,'coiPcsPmHistoryEsFe':coiPcsPmHistoryEsFe,'coiPcsPmHistorySesFe':coiPcsPmHistorySesFe,'coiPcsPmHistoryUasFe':coiPcsPmHistoryUasFe,'coiPcsPmHistoryValidData':coiPcsPmHistoryValidData,'ciscoFibreChanMIBConformance':ciscoFibreChanMIBConformance,'ciscoFibreChanMIBCompliances':ciscoFibreChanMIBCompliances,'ciscoFibreChanMIBGroups':ciscoFibreChanMIBGroups})