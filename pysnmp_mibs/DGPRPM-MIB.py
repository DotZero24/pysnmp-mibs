_S='accessNo'
_R='cpsIDIndex'
_Q='normal'
_P='rpmScheduleIndex'
_O='NotificationType'
_N='outletH'
_M='outletG'
_L='outletF'
_K='outletE'
_J='outletD'
_I='outletC'
_H='outletB'
_G='outletA'
_F='none'
_E='DGPRPM-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_O,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_O,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Dgp_ObjectIdentity=ObjectIdentity
dgp=_Dgp_ObjectIdentity((1,3,6,1,4,1,17420))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,17420,1))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,17420,1,1))
class _Protocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('ups01',0),('ups02',1),('rpm',2),('cps',3),('ats',4)))
_Protocol_Type.__name__=_C
_Protocol_Object=MibScalar
protocol=_Protocol_Object((1,3,6,1,4,1,17420,1,1,1),_Protocol_Type())
protocol.setMaxAccess(_B)
if mibBuilder.loadTexts:protocol.setStatus(_A)
_Rpm_ObjectIdentity=ObjectIdentity
rpm=_Rpm_ObjectIdentity((1,3,6,1,4,1,17420,1,1,3))
_RpmNumber_Type=Integer32
_RpmNumber_Object=MibScalar
rpmNumber=_RpmNumber_Object((1,3,6,1,4,1,17420,1,1,3,1),_RpmNumber_Type())
rpmNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmNumber.setStatus(_A)
_RpmTable_Object=MibTable
rpmTable=_RpmTable_Object((1,3,6,1,4,1,17420,1,1,3,2))
if mibBuilder.loadTexts:rpmTable.setStatus(_A)
_RpmEntry_Object=MibTableRow
rpmEntry=_RpmEntry_Object((1,3,6,1,4,1,17420,1,1,3,2,1))
rpmEntry.setIndexNames((0,_E,'rpmID'))
if mibBuilder.loadTexts:rpmEntry.setStatus(_A)
class _RpmID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RpmID_Type.__name__=_C
_RpmID_Object=MibTableColumn
rpmID=_RpmID_Object((1,3,6,1,4,1,17420,1,1,3,2,1,1),_RpmID_Type())
rpmID.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmID.setStatus(_A)
_RpmOutletNumber_Type=Integer32
_RpmOutletNumber_Object=MibTableColumn
rpmOutletNumber=_RpmOutletNumber_Object((1,3,6,1,4,1,17420,1,1,3,2,1,2),_RpmOutletNumber_Type())
rpmOutletNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmOutletNumber.setStatus(_A)
_RpmOutletState_Type=DisplayString
_RpmOutletState_Object=MibTableColumn
rpmOutletState=_RpmOutletState_Object((1,3,6,1,4,1,17420,1,1,3,2,1,3),_RpmOutletState_Type())
rpmOutletState.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmOutletState.setStatus(_A)
_RpmControlType_Type=DisplayString
_RpmControlType_Object=MibTableColumn
rpmControlType=_RpmControlType_Object((1,3,6,1,4,1,17420,1,1,3,2,1,4),_RpmControlType_Type())
rpmControlType.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmControlType.setStatus(_A)
_RpmInternetLocal_Type=DisplayString
_RpmInternetLocal_Object=MibTableColumn
rpmInternetLocal=_RpmInternetLocal_Object((1,3,6,1,4,1,17420,1,1,3,2,1,5),_RpmInternetLocal_Type())
rpmInternetLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmInternetLocal.setStatus(_A)
_RpmName_Type=DisplayString
_RpmName_Object=MibTableColumn
rpmName=_RpmName_Object((1,3,6,1,4,1,17420,1,1,3,2,1,6),_RpmName_Type())
rpmName.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmName.setStatus(_A)
_RpmOutletA_Type=DisplayString
_RpmOutletA_Object=MibTableColumn
rpmOutletA=_RpmOutletA_Object((1,3,6,1,4,1,17420,1,1,3,2,1,7),_RpmOutletA_Type())
rpmOutletA.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletA.setStatus(_A)
_RpmOutletB_Type=DisplayString
_RpmOutletB_Object=MibTableColumn
rpmOutletB=_RpmOutletB_Object((1,3,6,1,4,1,17420,1,1,3,2,1,8),_RpmOutletB_Type())
rpmOutletB.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletB.setStatus(_A)
_RpmOutletC_Type=DisplayString
_RpmOutletC_Object=MibTableColumn
rpmOutletC=_RpmOutletC_Object((1,3,6,1,4,1,17420,1,1,3,2,1,9),_RpmOutletC_Type())
rpmOutletC.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletC.setStatus(_A)
_RpmOutletD_Type=DisplayString
_RpmOutletD_Object=MibTableColumn
rpmOutletD=_RpmOutletD_Object((1,3,6,1,4,1,17420,1,1,3,2,1,10),_RpmOutletD_Type())
rpmOutletD.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletD.setStatus(_A)
_RpmOutletE_Type=DisplayString
_RpmOutletE_Object=MibTableColumn
rpmOutletE=_RpmOutletE_Object((1,3,6,1,4,1,17420,1,1,3,2,1,11),_RpmOutletE_Type())
rpmOutletE.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletE.setStatus(_A)
_RpmOutletF_Type=DisplayString
_RpmOutletF_Object=MibTableColumn
rpmOutletF=_RpmOutletF_Object((1,3,6,1,4,1,17420,1,1,3,2,1,12),_RpmOutletF_Type())
rpmOutletF.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletF.setStatus(_A)
_RpmOutletG_Type=DisplayString
_RpmOutletG_Object=MibTableColumn
rpmOutletG=_RpmOutletG_Object((1,3,6,1,4,1,17420,1,1,3,2,1,13),_RpmOutletG_Type())
rpmOutletG.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletG.setStatus(_A)
_RpmOutletH_Type=DisplayString
_RpmOutletH_Object=MibTableColumn
rpmOutletH=_RpmOutletH_Object((1,3,6,1,4,1,17420,1,1,3,2,1,14),_RpmOutletH_Type())
rpmOutletH.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletH.setStatus(_A)
_RpmDelayA_Type=Integer32
_RpmDelayA_Object=MibTableColumn
rpmDelayA=_RpmDelayA_Object((1,3,6,1,4,1,17420,1,1,3,2,1,15),_RpmDelayA_Type())
rpmDelayA.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayA.setStatus(_A)
_RpmDelayB_Type=Integer32
_RpmDelayB_Object=MibTableColumn
rpmDelayB=_RpmDelayB_Object((1,3,6,1,4,1,17420,1,1,3,2,1,16),_RpmDelayB_Type())
rpmDelayB.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayB.setStatus(_A)
_RpmDelayC_Type=Integer32
_RpmDelayC_Object=MibTableColumn
rpmDelayC=_RpmDelayC_Object((1,3,6,1,4,1,17420,1,1,3,2,1,17),_RpmDelayC_Type())
rpmDelayC.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayC.setStatus(_A)
_RpmDelayD_Type=Integer32
_RpmDelayD_Object=MibTableColumn
rpmDelayD=_RpmDelayD_Object((1,3,6,1,4,1,17420,1,1,3,2,1,18),_RpmDelayD_Type())
rpmDelayD.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayD.setStatus(_A)
_RpmDelayE_Type=Integer32
_RpmDelayE_Object=MibTableColumn
rpmDelayE=_RpmDelayE_Object((1,3,6,1,4,1,17420,1,1,3,2,1,19),_RpmDelayE_Type())
rpmDelayE.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayE.setStatus(_A)
_RpmDelayF_Type=Integer32
_RpmDelayF_Object=MibTableColumn
rpmDelayF=_RpmDelayF_Object((1,3,6,1,4,1,17420,1,1,3,2,1,20),_RpmDelayF_Type())
rpmDelayF.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayF.setStatus(_A)
_RpmDelayG_Type=Integer32
_RpmDelayG_Object=MibTableColumn
rpmDelayG=_RpmDelayG_Object((1,3,6,1,4,1,17420,1,1,3,2,1,21),_RpmDelayG_Type())
rpmDelayG.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayG.setStatus(_A)
_RpmDelayH_Type=Integer32
_RpmDelayH_Object=MibTableColumn
rpmDelayH=_RpmDelayH_Object((1,3,6,1,4,1,17420,1,1,3,2,1,22),_RpmDelayH_Type())
rpmDelayH.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDelayH.setStatus(_A)
_RpmResumeDelayA_Type=Integer32
_RpmResumeDelayA_Object=MibTableColumn
rpmResumeDelayA=_RpmResumeDelayA_Object((1,3,6,1,4,1,17420,1,1,3,2,1,23),_RpmResumeDelayA_Type())
rpmResumeDelayA.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayA.setStatus(_A)
_RpmResumeDelayB_Type=Integer32
_RpmResumeDelayB_Object=MibTableColumn
rpmResumeDelayB=_RpmResumeDelayB_Object((1,3,6,1,4,1,17420,1,1,3,2,1,24),_RpmResumeDelayB_Type())
rpmResumeDelayB.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayB.setStatus(_A)
_RpmResumeDelayC_Type=Integer32
_RpmResumeDelayC_Object=MibTableColumn
rpmResumeDelayC=_RpmResumeDelayC_Object((1,3,6,1,4,1,17420,1,1,3,2,1,25),_RpmResumeDelayC_Type())
rpmResumeDelayC.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayC.setStatus(_A)
_RpmResumeDelayD_Type=Integer32
_RpmResumeDelayD_Object=MibTableColumn
rpmResumeDelayD=_RpmResumeDelayD_Object((1,3,6,1,4,1,17420,1,1,3,2,1,26),_RpmResumeDelayD_Type())
rpmResumeDelayD.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayD.setStatus(_A)
_RpmResumeDelayE_Type=Integer32
_RpmResumeDelayE_Object=MibTableColumn
rpmResumeDelayE=_RpmResumeDelayE_Object((1,3,6,1,4,1,17420,1,1,3,2,1,27),_RpmResumeDelayE_Type())
rpmResumeDelayE.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayE.setStatus(_A)
_RpmResumeDelayF_Type=Integer32
_RpmResumeDelayF_Object=MibTableColumn
rpmResumeDelayF=_RpmResumeDelayF_Object((1,3,6,1,4,1,17420,1,1,3,2,1,28),_RpmResumeDelayF_Type())
rpmResumeDelayF.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayF.setStatus(_A)
_RpmResumeDelayG_Type=Integer32
_RpmResumeDelayG_Object=MibTableColumn
rpmResumeDelayG=_RpmResumeDelayG_Object((1,3,6,1,4,1,17420,1,1,3,2,1,29),_RpmResumeDelayG_Type())
rpmResumeDelayG.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayG.setStatus(_A)
_RpmResumeDelayH_Type=Integer32
_RpmResumeDelayH_Object=MibTableColumn
rpmResumeDelayH=_RpmResumeDelayH_Object((1,3,6,1,4,1,17420,1,1,3,2,1,30),_RpmResumeDelayH_Type())
rpmResumeDelayH.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmResumeDelayH.setStatus(_A)
_RpmSetEntry_ObjectIdentity=ObjectIdentity
rpmSetEntry=_RpmSetEntry_ObjectIdentity((1,3,6,1,4,1,17420,1,1,3,3))
class _RpmSetID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RpmSetID_Type.__name__=_C
_RpmSetID_Object=MibScalar
rpmSetID=_RpmSetID_Object((1,3,6,1,4,1,17420,1,1,3,3,1),_RpmSetID_Type())
rpmSetID.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmSetID.setStatus(_A)
class _RpmOnNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8)))
_RpmOnNumber_Type.__name__=_C
_RpmOnNumber_Object=MibScalar
rpmOnNumber=_RpmOnNumber_Object((1,3,6,1,4,1,17420,1,1,3,3,2),_RpmOnNumber_Type())
rpmOnNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOnNumber.setStatus(_A)
class _RpmOffNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8)))
_RpmOffNumber_Type.__name__=_C
_RpmOffNumber_Object=MibScalar
rpmOffNumber=_RpmOffNumber_Object((1,3,6,1,4,1,17420,1,1,3,3,3),_RpmOffNumber_Type())
rpmOffNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOffNumber.setStatus(_A)
class _RpmAllOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('on',1),('off',2)))
_RpmAllOnOff_Type.__name__=_C
_RpmAllOnOff_Object=MibScalar
rpmAllOnOff=_RpmAllOnOff_Object((1,3,6,1,4,1,17420,1,1,3,3,4),_RpmAllOnOff_Type())
rpmAllOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmAllOnOff.setStatus(_A)
_RpmScheduleTable_Object=MibTable
rpmScheduleTable=_RpmScheduleTable_Object((1,3,6,1,4,1,17420,1,1,3,4))
if mibBuilder.loadTexts:rpmScheduleTable.setStatus(_A)
_RpmScheduleEntry_Object=MibTableRow
rpmScheduleEntry=_RpmScheduleEntry_Object((1,3,6,1,4,1,17420,1,1,3,4,1))
rpmScheduleEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:rpmScheduleEntry.setStatus(_A)
_RpmScheduleIndex_Type=Integer32
_RpmScheduleIndex_Object=MibTableColumn
rpmScheduleIndex=_RpmScheduleIndex_Object((1,3,6,1,4,1,17420,1,1,3,4,1,1),_RpmScheduleIndex_Type())
rpmScheduleIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:rpmScheduleIndex.setStatus(_A)
class _RpmScheduleID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_RpmScheduleID_Type.__name__=_C
_RpmScheduleID_Object=MibTableColumn
rpmScheduleID=_RpmScheduleID_Object((1,3,6,1,4,1,17420,1,1,3,4,1,2),_RpmScheduleID_Type())
rpmScheduleID.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmScheduleID.setStatus(_A)
class _RpmOutlet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8)))
_RpmOutlet_Type.__name__=_C
_RpmOutlet_Object=MibTableColumn
rpmOutlet=_RpmOutlet_Object((1,3,6,1,4,1,17420,1,1,3,4,1,3),_RpmOutlet_Type())
rpmOutlet.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutlet.setStatus(_A)
class _RpmOutletAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_RpmOutletAction_Type.__name__=_C
_RpmOutletAction_Object=MibTableColumn
rpmOutletAction=_RpmOutletAction_Object((1,3,6,1,4,1,17420,1,1,3,4,1,4),_RpmOutletAction_Type())
rpmOutletAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmOutletAction.setStatus(_A)
class _RpmPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('once',1),('everySunday',2),('everyMonday',3),('everyTuesday',4),('everyWednesday',5),('everyThursday',6),('everyFriday',7),('everySaturday',8),('everyDay',9)))
_RpmPeriod_Type.__name__=_C
_RpmPeriod_Object=MibTableColumn
rpmPeriod=_RpmPeriod_Object((1,3,6,1,4,1,17420,1,1,3,4,1,5),_RpmPeriod_Type())
rpmPeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmPeriod.setStatus(_A)
_RpmDate_Type=DisplayString
_RpmDate_Object=MibTableColumn
rpmDate=_RpmDate_Object((1,3,6,1,4,1,17420,1,1,3,4,1,6),_RpmDate_Type())
rpmDate.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmDate.setStatus(_A)
_RpmTime_Type=DisplayString
_RpmTime_Object=MibTableColumn
rpmTime=_RpmTime_Object((1,3,6,1,4,1,17420,1,1,3,4,1,7),_RpmTime_Type())
rpmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmTime.setStatus(_A)
class _RpmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('clear',0),('accept',1)))
_RpmStatus_Type.__name__=_C
_RpmStatus_Object=MibTableColumn
rpmStatus=_RpmStatus_Object((1,3,6,1,4,1,17420,1,1,3,4,1,8),_RpmStatus_Type())
rpmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rpmStatus.setStatus(_A)
_Cps_ObjectIdentity=ObjectIdentity
cps=_Cps_ObjectIdentity((1,3,6,1,4,1,17420,1,1,4))
_CpsNumber_Type=Integer32
_CpsNumber_Object=MibScalar
cpsNumber=_CpsNumber_Object((1,3,6,1,4,1,17420,1,1,4,1),_CpsNumber_Type())
cpsNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cpsNumber.setStatus(_A)
_CpsTable_Object=MibTable
cpsTable=_CpsTable_Object((1,3,6,1,4,1,17420,1,1,4,2))
if mibBuilder.loadTexts:cpsTable.setStatus(_A)
_CpsEntry_Object=MibTableRow
cpsEntry=_CpsEntry_Object((1,3,6,1,4,1,17420,1,1,4,2,1))
cpsEntry.setIndexNames((0,_E,'cpsID'))
if mibBuilder.loadTexts:cpsEntry.setStatus(_A)
class _CpsID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CpsID_Type.__name__=_C
_CpsID_Object=MibTableColumn
cpsID=_CpsID_Object((1,3,6,1,4,1,17420,1,1,4,2,1,1),_CpsID_Type())
cpsID.setMaxAccess(_D)
if mibBuilder.loadTexts:cpsID.setStatus(_A)
_CpsValue_Type=Integer32
_CpsValue_Object=MibTableColumn
cpsValue=_CpsValue_Object((1,3,6,1,4,1,17420,1,1,4,2,1,2),_CpsValue_Type())
cpsValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cpsValue.setStatus(_A)
class _CpsThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('alarm',0),(_Q,1)))
_CpsThreshold1_Type.__name__=_C
_CpsThreshold1_Object=MibTableColumn
cpsThreshold1=_CpsThreshold1_Object((1,3,6,1,4,1,17420,1,1,4,2,1,3),_CpsThreshold1_Type())
cpsThreshold1.setMaxAccess(_D)
if mibBuilder.loadTexts:cpsThreshold1.setStatus(_A)
class _CpsThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('alarm',0),(_Q,1)))
_CpsThreshold2_Type.__name__=_C
_CpsThreshold2_Object=MibTableColumn
cpsThreshold2=_CpsThreshold2_Object((1,3,6,1,4,1,17420,1,1,4,2,1,4),_CpsThreshold2_Type())
cpsThreshold2.setMaxAccess(_D)
if mibBuilder.loadTexts:cpsThreshold2.setStatus(_A)
_CpsSetTable_Object=MibTable
cpsSetTable=_CpsSetTable_Object((1,3,6,1,4,1,17420,1,1,4,3))
if mibBuilder.loadTexts:cpsSetTable.setStatus(_A)
_CpsSetEntry_Object=MibTableRow
cpsSetEntry=_CpsSetEntry_Object((1,3,6,1,4,1,17420,1,1,4,3,1))
cpsSetEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:cpsSetEntry.setStatus(_A)
class _CpsIDIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_CpsIDIndex_Type.__name__=_C
_CpsIDIndex_Object=MibTableColumn
cpsIDIndex=_CpsIDIndex_Object((1,3,6,1,4,1,17420,1,1,4,3,1,1),_CpsIDIndex_Type())
cpsIDIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cpsIDIndex.setStatus(_A)
class _CpsSetThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_CpsSetThreshold1_Type.__name__=_C
_CpsSetThreshold1_Object=MibTableColumn
cpsSetThreshold1=_CpsSetThreshold1_Object((1,3,6,1,4,1,17420,1,1,4,3,1,2),_CpsSetThreshold1_Type())
cpsSetThreshold1.setMaxAccess(_B)
if mibBuilder.loadTexts:cpsSetThreshold1.setStatus(_A)
class _CpsSetThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9999))
_CpsSetThreshold2_Type.__name__=_C
_CpsSetThreshold2_Object=MibTableColumn
cpsSetThreshold2=_CpsSetThreshold2_Object((1,3,6,1,4,1,17420,1,1,4,3,1,3),_CpsSetThreshold2_Type())
cpsSetThreshold2.setMaxAccess(_B)
if mibBuilder.loadTexts:cpsSetThreshold2.setStatus(_A)
_Ats_ObjectIdentity=ObjectIdentity
ats=_Ats_ObjectIdentity((1,3,6,1,4,1,17420,1,1,5))
_AtsIdentification_Type=DisplayString
_AtsIdentification_Object=MibScalar
atsIdentification=_AtsIdentification_Object((1,3,6,1,4,1,17420,1,1,5,1),_AtsIdentification_Type())
atsIdentification.setMaxAccess(_B)
if mibBuilder.loadTexts:atsIdentification.setStatus(_A)
_AtsInputPowerSourceA_Type=DisplayString
_AtsInputPowerSourceA_Object=MibScalar
atsInputPowerSourceA=_AtsInputPowerSourceA_Object((1,3,6,1,4,1,17420,1,1,5,2),_AtsInputPowerSourceA_Type())
atsInputPowerSourceA.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputPowerSourceA.setStatus(_A)
_AtsInputPowerSourceB_Type=DisplayString
_AtsInputPowerSourceB_Object=MibScalar
atsInputPowerSourceB=_AtsInputPowerSourceB_Object((1,3,6,1,4,1,17420,1,1,5,3),_AtsInputPowerSourceB_Type())
atsInputPowerSourceB.setMaxAccess(_B)
if mibBuilder.loadTexts:atsInputPowerSourceB.setStatus(_A)
class _AtsAutomaticTransferSwitch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),('transfer',1)))
_AtsAutomaticTransferSwitch_Type.__name__=_C
_AtsAutomaticTransferSwitch_Object=MibScalar
atsAutomaticTransferSwitch=_AtsAutomaticTransferSwitch_Object((1,3,6,1,4,1,17420,1,1,5,4),_AtsAutomaticTransferSwitch_Type())
atsAutomaticTransferSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:atsAutomaticTransferSwitch.setStatus(_A)
class _AtsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),('a',1),('b',2)))
_AtsStatus_Type.__name__=_C
_AtsStatus_Object=MibScalar
atsStatus=_AtsStatus_Object((1,3,6,1,4,1,17420,1,1,5,5),_AtsStatus_Type())
atsStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:atsStatus.setStatus(_A)
_Mgmt_ObjectIdentity=ObjectIdentity
mgmt=_Mgmt_ObjectIdentity((1,3,6,1,4,1,17420,1,1,999))
_Snmp_ObjectIdentity=ObjectIdentity
snmp=_Snmp_ObjectIdentity((1,3,6,1,4,1,17420,1,1,999,1))
_AccessTable_Object=MibTable
accessTable=_AccessTable_Object((1,3,6,1,4,1,17420,1,1,999,1,1))
if mibBuilder.loadTexts:accessTable.setStatus(_A)
_AccessEntry_Object=MibTableRow
accessEntry=_AccessEntry_Object((1,3,6,1,4,1,17420,1,1,999,1,1,1))
accessEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:accessEntry.setStatus(_A)
class _AccessNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_AccessNo_Type.__name__=_C
_AccessNo_Object=MibTableColumn
accessNo=_AccessNo_Object((1,3,6,1,4,1,17420,1,1,999,1,1,1,1),_AccessNo_Type())
accessNo.setMaxAccess(_D)
if mibBuilder.loadTexts:accessNo.setStatus(_A)
_Community_Type=DisplayString
_Community_Object=MibTableColumn
community=_Community_Object((1,3,6,1,4,1,17420,1,1,999,1,1,1,2),_Community_Type())
community.setMaxAccess(_B)
if mibBuilder.loadTexts:community.setStatus(_A)
class _Permission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noAccess',0),('read',1),('readWrite',2)))
_Permission_Type.__name__=_C
_Permission_Object=MibTableColumn
permission=_Permission_Object((1,3,6,1,4,1,17420,1,1,999,1,1,1,3),_Permission_Type())
permission.setMaxAccess(_B)
if mibBuilder.loadTexts:permission.setStatus(_A)
rpmOutletOn=NotificationType((1,3,6,1,4,1,17420,0,100))
if mibBuilder.loadTexts:rpmOutletOn.setStatus('')
rpmOutletOff=NotificationType((1,3,6,1,4,1,17420,0,101))
if mibBuilder.loadTexts:rpmOutletOff.setStatus('')
rpmOutletReboot=NotificationType((1,3,6,1,4,1,17420,0,102))
if mibBuilder.loadTexts:rpmOutletReboot.setStatus('')
rpmOutletfault=NotificationType((1,3,6,1,4,1,17420,0,103))
if mibBuilder.loadTexts:rpmOutletfault.setStatus('')
rpmCommunicationLost=NotificationType((1,3,6,1,4,1,17420,0,104))
if mibBuilder.loadTexts:rpmCommunicationLost.setStatus('')
cpsOutOfThreshold1=NotificationType((1,3,6,1,4,1,17420,0,105))
if mibBuilder.loadTexts:cpsOutOfThreshold1.setStatus('')
cpsOutOfThreshold2=NotificationType((1,3,6,1,4,1,17420,0,106))
if mibBuilder.loadTexts:cpsOutOfThreshold2.setStatus('')
cpsCommunicationLost=NotificationType((1,3,6,1,4,1,17420,0,107))
if mibBuilder.loadTexts:cpsCommunicationLost.setStatus('')
mibBuilder.exportSymbols(_E,**{'dgp':dgp,'rpmOutletOn':rpmOutletOn,'rpmOutletOff':rpmOutletOff,'rpmOutletReboot':rpmOutletReboot,'rpmOutletfault':rpmOutletfault,'rpmCommunicationLost':rpmCommunicationLost,'cpsOutOfThreshold1':cpsOutOfThreshold1,'cpsOutOfThreshold2':cpsOutOfThreshold2,'cpsCommunicationLost':cpsCommunicationLost,'products':products,'hardware':hardware,'protocol':protocol,'rpm':rpm,'rpmNumber':rpmNumber,'rpmTable':rpmTable,'rpmEntry':rpmEntry,'rpmID':rpmID,'rpmOutletNumber':rpmOutletNumber,'rpmOutletState':rpmOutletState,'rpmControlType':rpmControlType,'rpmInternetLocal':rpmInternetLocal,'rpmName':rpmName,'rpmOutletA':rpmOutletA,'rpmOutletB':rpmOutletB,'rpmOutletC':rpmOutletC,'rpmOutletD':rpmOutletD,'rpmOutletE':rpmOutletE,'rpmOutletF':rpmOutletF,'rpmOutletG':rpmOutletG,'rpmOutletH':rpmOutletH,'rpmDelayA':rpmDelayA,'rpmDelayB':rpmDelayB,'rpmDelayC':rpmDelayC,'rpmDelayD':rpmDelayD,'rpmDelayE':rpmDelayE,'rpmDelayF':rpmDelayF,'rpmDelayG':rpmDelayG,'rpmDelayH':rpmDelayH,'rpmResumeDelayA':rpmResumeDelayA,'rpmResumeDelayB':rpmResumeDelayB,'rpmResumeDelayC':rpmResumeDelayC,'rpmResumeDelayD':rpmResumeDelayD,'rpmResumeDelayE':rpmResumeDelayE,'rpmResumeDelayF':rpmResumeDelayF,'rpmResumeDelayG':rpmResumeDelayG,'rpmResumeDelayH':rpmResumeDelayH,'rpmSetEntry':rpmSetEntry,'rpmSetID':rpmSetID,'rpmOnNumber':rpmOnNumber,'rpmOffNumber':rpmOffNumber,'rpmAllOnOff':rpmAllOnOff,'rpmScheduleTable':rpmScheduleTable,'rpmScheduleEntry':rpmScheduleEntry,_P:rpmScheduleIndex,'rpmScheduleID':rpmScheduleID,'rpmOutlet':rpmOutlet,'rpmOutletAction':rpmOutletAction,'rpmPeriod':rpmPeriod,'rpmDate':rpmDate,'rpmTime':rpmTime,'rpmStatus':rpmStatus,'cps':cps,'cpsNumber':cpsNumber,'cpsTable':cpsTable,'cpsEntry':cpsEntry,'cpsID':cpsID,'cpsValue':cpsValue,'cpsThreshold1':cpsThreshold1,'cpsThreshold2':cpsThreshold2,'cpsSetTable':cpsSetTable,'cpsSetEntry':cpsSetEntry,_R:cpsIDIndex,'cpsSetThreshold1':cpsSetThreshold1,'cpsSetThreshold2':cpsSetThreshold2,'ats':ats,'atsIdentification':atsIdentification,'atsInputPowerSourceA':atsInputPowerSourceA,'atsInputPowerSourceB':atsInputPowerSourceB,'atsAutomaticTransferSwitch':atsAutomaticTransferSwitch,'atsStatus':atsStatus,'mgmt':mgmt,'snmp':snmp,'accessTable':accessTable,'accessEntry':accessEntry,_S:accessNo,'community':community,'permission':permission})