_l='sunHwCtrlTpmForceClear'
_k='sunHwCtrlTpmActivate'
_j='sunHwCtrlTpmEnable'
_i='sunHwCtrlPowerMgmtSamplingAveragePower'
_h='sunHwCtrlPowerMgmtSamplingMaximumPower'
_g='sunHwCtrlPowerMgmtSamplingMinimumPower'
_f='sunHwCtrlPowerMgmtSamplingTimestamp'
_e='sunHwCtrlPowerMgmtSamplingPeriod'
_d='sunHwCtrlPowerMgmtConsumptionThreshold2'
_c='sunHwCtrlPowerMgmtConsumptionThreshold1'
_b='sunHwCtrlPowerMgmtBudgetPendingTimelimitActions'
_a='sunHwCtrlPowerMgmtBudgetPendingTimelimit'
_Z='sunHwCtrlPowerMgmtBudgetPendingPowerlimit'
_Y='sunHwCtrlPowerMgmtBudgetCommitPending'
_X='sunHwCtrlPowerMgmtBudgetOK'
_W='sunHwCtrlPowerMgmtBudgetTimelimitActions'
_V='sunHwCtrlPowerMgmtBudgetTimelimit'
_U='sunHwCtrlPowerMgmtBudgetPowerlimit'
_T='sunHwCtrlPowerMgmtBudgetMinPowerlimit'
_S='sunHwCtrlPowerMgmtBudget'
_R='sunHwCtrlPowerMgmtPolicy'
_Q='sunHwCtrlPowerMgmtAvailablePower'
_P='sunHwCtrlPowerMgmtPermittedPower'
_O='sunHwCtrlPowerMgmtActualPower'
_N='sunHwCtrlPowerMgmtValue'
_M='sunHwCtrlPowerMgmtUnits'
_L='sunHwCtrlPowerMgmtName'
_K='sunHwCtrlTotalPSU'
_J='sunHwCtrlReservedPSU'
_I='milliseconds'
_H='sunHwCtrlPowerMgmtID'
_G='unknown'
_F='watts'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='SUN-HW-CTRL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
sunHwCtrlMIB=ModuleIdentity((1,3,6,1,4,1,42,2,175,104))
if mibBuilder.loadTexts:sunHwCtrlMIB.setRevisions(('2010-01-04 00:00','2009-08-20 00:00','2009-07-28 00:00','2009-03-01 00:00','2008-09-01 00:00'))
class SunHwCtrlPowerMgmtID(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class SunHwCtrlPowerMgmtPolicy(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notsupported',1),(_G,2),('performance',3),('elastic',4)))
class SunHwCtrlPowerMgmtBudgetTimelimitActions(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('none',0),('hardPowerOff',1)))
_Sun_ObjectIdentity=ObjectIdentity
sun=_Sun_ObjectIdentity((1,3,6,1,4,1,42))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,42,2))
_Ilom_ObjectIdentity=ObjectIdentity
ilom=_Ilom_ObjectIdentity((1,3,6,1,4,1,42,2,175))
_SunHwCtrlMIBObjects_ObjectIdentity=ObjectIdentity
sunHwCtrlMIBObjects=_SunHwCtrlMIBObjects_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,1))
_SunHwCtrlPowerMgmt_ObjectIdentity=ObjectIdentity
sunHwCtrlPowerMgmt=_SunHwCtrlPowerMgmt_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,1,6))
_SunHwCtrlReservedPSU_Type=Integer32
_SunHwCtrlReservedPSU_Object=MibScalar
sunHwCtrlReservedPSU=_SunHwCtrlReservedPSU_Object((1,3,6,1,4,1,42,2,175,104,1,6,1),_SunHwCtrlReservedPSU_Type())
sunHwCtrlReservedPSU.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlReservedPSU.setStatus(_A)
_SunHwCtrlTotalPSU_Type=Integer32
_SunHwCtrlTotalPSU_Object=MibScalar
sunHwCtrlTotalPSU=_SunHwCtrlTotalPSU_Object((1,3,6,1,4,1,42,2,175,104,1,6,2),_SunHwCtrlTotalPSU_Type())
sunHwCtrlTotalPSU.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlTotalPSU.setStatus(_A)
_SunHwCtrlPowerMgmtTable_Object=MibTable
sunHwCtrlPowerMgmtTable=_SunHwCtrlPowerMgmtTable_Object((1,3,6,1,4,1,42,2,175,104,1,6,3))
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtTable.setStatus(_A)
_SunHwCtrlPowerMgmtEntry_Object=MibTableRow
sunHwCtrlPowerMgmtEntry=_SunHwCtrlPowerMgmtEntry_Object((1,3,6,1,4,1,42,2,175,104,1,6,3,1))
sunHwCtrlPowerMgmtEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtEntry.setStatus(_A)
_SunHwCtrlPowerMgmtID_Type=SunHwCtrlPowerMgmtID
_SunHwCtrlPowerMgmtID_Object=MibTableColumn
sunHwCtrlPowerMgmtID=_SunHwCtrlPowerMgmtID_Object((1,3,6,1,4,1,42,2,175,104,1,6,3,1,1),_SunHwCtrlPowerMgmtID_Type())
sunHwCtrlPowerMgmtID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtID.setStatus(_A)
_SunHwCtrlPowerMgmtName_Type=SnmpAdminString
_SunHwCtrlPowerMgmtName_Object=MibTableColumn
sunHwCtrlPowerMgmtName=_SunHwCtrlPowerMgmtName_Object((1,3,6,1,4,1,42,2,175,104,1,6,3,1,2),_SunHwCtrlPowerMgmtName_Type())
sunHwCtrlPowerMgmtName.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtName.setStatus(_A)
_SunHwCtrlPowerMgmtUnits_Type=SnmpAdminString
_SunHwCtrlPowerMgmtUnits_Object=MibTableColumn
sunHwCtrlPowerMgmtUnits=_SunHwCtrlPowerMgmtUnits_Object((1,3,6,1,4,1,42,2,175,104,1,6,3,1,3),_SunHwCtrlPowerMgmtUnits_Type())
sunHwCtrlPowerMgmtUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtUnits.setStatus(_A)
_SunHwCtrlPowerMgmtValue_Type=SnmpAdminString
_SunHwCtrlPowerMgmtValue_Object=MibTableColumn
sunHwCtrlPowerMgmtValue=_SunHwCtrlPowerMgmtValue_Object((1,3,6,1,4,1,42,2,175,104,1,6,3,1,4),_SunHwCtrlPowerMgmtValue_Type())
sunHwCtrlPowerMgmtValue.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtValue.setStatus(_A)
_SunHwCtrlPowerMgmtActualPower_Type=Integer32
_SunHwCtrlPowerMgmtActualPower_Object=MibScalar
sunHwCtrlPowerMgmtActualPower=_SunHwCtrlPowerMgmtActualPower_Object((1,3,6,1,4,1,42,2,175,104,1,6,4),_SunHwCtrlPowerMgmtActualPower_Type())
sunHwCtrlPowerMgmtActualPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtActualPower.setStatus(_A)
_SunHwCtrlPowerMgmtPermittedPower_Type=Integer32
_SunHwCtrlPowerMgmtPermittedPower_Object=MibScalar
sunHwCtrlPowerMgmtPermittedPower=_SunHwCtrlPowerMgmtPermittedPower_Object((1,3,6,1,4,1,42,2,175,104,1,6,5),_SunHwCtrlPowerMgmtPermittedPower_Type())
sunHwCtrlPowerMgmtPermittedPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtPermittedPower.setStatus(_A)
_SunHwCtrlPowerMgmtAvailablePower_Type=Integer32
_SunHwCtrlPowerMgmtAvailablePower_Object=MibScalar
sunHwCtrlPowerMgmtAvailablePower=_SunHwCtrlPowerMgmtAvailablePower_Object((1,3,6,1,4,1,42,2,175,104,1,6,6),_SunHwCtrlPowerMgmtAvailablePower_Type())
sunHwCtrlPowerMgmtAvailablePower.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtAvailablePower.setStatus(_A)
_SunHwCtrlPowerMgmtPolicy_Type=SunHwCtrlPowerMgmtPolicy
_SunHwCtrlPowerMgmtPolicy_Object=MibScalar
sunHwCtrlPowerMgmtPolicy=_SunHwCtrlPowerMgmtPolicy_Object((1,3,6,1,4,1,42,2,175,104,1,6,7),_SunHwCtrlPowerMgmtPolicy_Type())
sunHwCtrlPowerMgmtPolicy.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtPolicy.setStatus(_A)
_SunHwCtrlPowerMgmtBudgetSettings_ObjectIdentity=ObjectIdentity
sunHwCtrlPowerMgmtBudgetSettings=_SunHwCtrlPowerMgmtBudgetSettings_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,1,6,9))
class _SunHwCtrlPowerMgmtBudget_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('disabled',2),('enabled',3),('enabledPostPoweron',4)))
_SunHwCtrlPowerMgmtBudget_Type.__name__=_D
_SunHwCtrlPowerMgmtBudget_Object=MibScalar
sunHwCtrlPowerMgmtBudget=_SunHwCtrlPowerMgmtBudget_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,1),_SunHwCtrlPowerMgmtBudget_Type())
sunHwCtrlPowerMgmtBudget.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudget.setStatus(_A)
class _SunHwCtrlPowerMgmtBudgetMinPowerlimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtBudgetMinPowerlimit_Type.__name__=_D
_SunHwCtrlPowerMgmtBudgetMinPowerlimit_Object=MibScalar
sunHwCtrlPowerMgmtBudgetMinPowerlimit=_SunHwCtrlPowerMgmtBudgetMinPowerlimit_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,2),_SunHwCtrlPowerMgmtBudgetMinPowerlimit_Type())
sunHwCtrlPowerMgmtBudgetMinPowerlimit.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetMinPowerlimit.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetMinPowerlimit.setUnits(_F)
class _SunHwCtrlPowerMgmtBudgetPowerlimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtBudgetPowerlimit_Type.__name__=_D
_SunHwCtrlPowerMgmtBudgetPowerlimit_Object=MibScalar
sunHwCtrlPowerMgmtBudgetPowerlimit=_SunHwCtrlPowerMgmtBudgetPowerlimit_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,3),_SunHwCtrlPowerMgmtBudgetPowerlimit_Type())
sunHwCtrlPowerMgmtBudgetPowerlimit.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetPowerlimit.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetPowerlimit.setUnits(_F)
class _SunHwCtrlPowerMgmtBudgetTimelimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtBudgetTimelimit_Type.__name__=_D
_SunHwCtrlPowerMgmtBudgetTimelimit_Object=MibScalar
sunHwCtrlPowerMgmtBudgetTimelimit=_SunHwCtrlPowerMgmtBudgetTimelimit_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,5),_SunHwCtrlPowerMgmtBudgetTimelimit_Type())
sunHwCtrlPowerMgmtBudgetTimelimit.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetTimelimit.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetTimelimit.setUnits(_I)
_SunHwCtrlPowerMgmtBudgetTimelimitActions_Type=SunHwCtrlPowerMgmtBudgetTimelimitActions
_SunHwCtrlPowerMgmtBudgetTimelimitActions_Object=MibScalar
sunHwCtrlPowerMgmtBudgetTimelimitActions=_SunHwCtrlPowerMgmtBudgetTimelimitActions_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,6),_SunHwCtrlPowerMgmtBudgetTimelimitActions_Type())
sunHwCtrlPowerMgmtBudgetTimelimitActions.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetTimelimitActions.setStatus(_A)
_SunHwCtrlPowerMgmtBudgetOK_Type=TruthValue
_SunHwCtrlPowerMgmtBudgetOK_Object=MibScalar
sunHwCtrlPowerMgmtBudgetOK=_SunHwCtrlPowerMgmtBudgetOK_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,7),_SunHwCtrlPowerMgmtBudgetOK_Type())
sunHwCtrlPowerMgmtBudgetOK.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetOK.setStatus(_A)
_SunHwCtrlPowerMgmtBudgetCommitPending_Type=TruthValue
_SunHwCtrlPowerMgmtBudgetCommitPending_Object=MibScalar
sunHwCtrlPowerMgmtBudgetCommitPending=_SunHwCtrlPowerMgmtBudgetCommitPending_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,100),_SunHwCtrlPowerMgmtBudgetCommitPending_Type())
sunHwCtrlPowerMgmtBudgetCommitPending.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetCommitPending.setStatus(_A)
class _SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Type.__name__=_D
_SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Object=MibScalar
sunHwCtrlPowerMgmtBudgetPendingPowerlimit=_SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,103),_SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Type())
sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setUnits(_F)
class _SunHwCtrlPowerMgmtBudgetPendingTimelimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_SunHwCtrlPowerMgmtBudgetPendingTimelimit_Type.__name__=_D
_SunHwCtrlPowerMgmtBudgetPendingTimelimit_Object=MibScalar
sunHwCtrlPowerMgmtBudgetPendingTimelimit=_SunHwCtrlPowerMgmtBudgetPendingTimelimit_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,105),_SunHwCtrlPowerMgmtBudgetPendingTimelimit_Type())
sunHwCtrlPowerMgmtBudgetPendingTimelimit.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetPendingTimelimit.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetPendingTimelimit.setUnits(_I)
_SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Type=SunHwCtrlPowerMgmtBudgetTimelimitActions
_SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Object=MibScalar
sunHwCtrlPowerMgmtBudgetPendingTimelimitActions=_SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Object((1,3,6,1,4,1,42,2,175,104,1,6,9,106),_SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Type())
sunHwCtrlPowerMgmtBudgetPendingTimelimitActions.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtBudgetPendingTimelimitActions.setStatus(_A)
_SunHwCtrlPowerMgmtConsumptionThresholds_ObjectIdentity=ObjectIdentity
sunHwCtrlPowerMgmtConsumptionThresholds=_SunHwCtrlPowerMgmtConsumptionThresholds_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,1,6,10))
class _SunHwCtrlPowerMgmtConsumptionThreshold1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SunHwCtrlPowerMgmtConsumptionThreshold1_Type.__name__=_D
_SunHwCtrlPowerMgmtConsumptionThreshold1_Object=MibScalar
sunHwCtrlPowerMgmtConsumptionThreshold1=_SunHwCtrlPowerMgmtConsumptionThreshold1_Object((1,3,6,1,4,1,42,2,175,104,1,6,10,1),_SunHwCtrlPowerMgmtConsumptionThreshold1_Type())
sunHwCtrlPowerMgmtConsumptionThreshold1.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtConsumptionThreshold1.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtConsumptionThreshold1.setUnits(_F)
class _SunHwCtrlPowerMgmtConsumptionThreshold2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_SunHwCtrlPowerMgmtConsumptionThreshold2_Type.__name__=_D
_SunHwCtrlPowerMgmtConsumptionThreshold2_Object=MibScalar
sunHwCtrlPowerMgmtConsumptionThreshold2=_SunHwCtrlPowerMgmtConsumptionThreshold2_Object((1,3,6,1,4,1,42,2,175,104,1,6,10,2),_SunHwCtrlPowerMgmtConsumptionThreshold2_Type())
sunHwCtrlPowerMgmtConsumptionThreshold2.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtConsumptionThreshold2.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtConsumptionThreshold2.setUnits(_F)
_SunHwCtrlPowerMgmtSampling_ObjectIdentity=ObjectIdentity
sunHwCtrlPowerMgmtSampling=_SunHwCtrlPowerMgmtSampling_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,1,6,11))
class _SunHwCtrlPowerMgmtSamplingPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtSamplingPeriod_Type.__name__=_D
_SunHwCtrlPowerMgmtSamplingPeriod_Object=MibScalar
sunHwCtrlPowerMgmtSamplingPeriod=_SunHwCtrlPowerMgmtSamplingPeriod_Object((1,3,6,1,4,1,42,2,175,104,1,6,11,1),_SunHwCtrlPowerMgmtSamplingPeriod_Type())
sunHwCtrlPowerMgmtSamplingPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingPeriod.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingPeriod.setUnits('seconds')
_SunHwCtrlPowerMgmtSamplingTimestamp_Type=DateAndTime
_SunHwCtrlPowerMgmtSamplingTimestamp_Object=MibScalar
sunHwCtrlPowerMgmtSamplingTimestamp=_SunHwCtrlPowerMgmtSamplingTimestamp_Object((1,3,6,1,4,1,42,2,175,104,1,6,11,2),_SunHwCtrlPowerMgmtSamplingTimestamp_Type())
sunHwCtrlPowerMgmtSamplingTimestamp.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingTimestamp.setStatus(_A)
class _SunHwCtrlPowerMgmtSamplingMinimumPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtSamplingMinimumPower_Type.__name__=_D
_SunHwCtrlPowerMgmtSamplingMinimumPower_Object=MibScalar
sunHwCtrlPowerMgmtSamplingMinimumPower=_SunHwCtrlPowerMgmtSamplingMinimumPower_Object((1,3,6,1,4,1,42,2,175,104,1,6,11,3),_SunHwCtrlPowerMgmtSamplingMinimumPower_Type())
sunHwCtrlPowerMgmtSamplingMinimumPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingMinimumPower.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingMinimumPower.setUnits(_F)
class _SunHwCtrlPowerMgmtSamplingMaximumPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtSamplingMaximumPower_Type.__name__=_D
_SunHwCtrlPowerMgmtSamplingMaximumPower_Object=MibScalar
sunHwCtrlPowerMgmtSamplingMaximumPower=_SunHwCtrlPowerMgmtSamplingMaximumPower_Object((1,3,6,1,4,1,42,2,175,104,1,6,11,4),_SunHwCtrlPowerMgmtSamplingMaximumPower_Type())
sunHwCtrlPowerMgmtSamplingMaximumPower.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingMaximumPower.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingMaximumPower.setUnits(_F)
class _SunHwCtrlPowerMgmtSamplingAveragePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SunHwCtrlPowerMgmtSamplingAveragePower_Type.__name__=_D
_SunHwCtrlPowerMgmtSamplingAveragePower_Object=MibScalar
sunHwCtrlPowerMgmtSamplingAveragePower=_SunHwCtrlPowerMgmtSamplingAveragePower_Object((1,3,6,1,4,1,42,2,175,104,1,6,11,5),_SunHwCtrlPowerMgmtSamplingAveragePower_Type())
sunHwCtrlPowerMgmtSamplingAveragePower.setMaxAccess(_C)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingAveragePower.setStatus(_A)
if mibBuilder.loadTexts:sunHwCtrlPowerMgmtSamplingAveragePower.setUnits(_F)
_SunHwCtrlTPM_ObjectIdentity=ObjectIdentity
sunHwCtrlTPM=_SunHwCtrlTPM_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,1,7))
_SunHwCtrlTpmEnable_Type=TruthValue
_SunHwCtrlTpmEnable_Object=MibScalar
sunHwCtrlTpmEnable=_SunHwCtrlTpmEnable_Object((1,3,6,1,4,1,42,2,175,104,1,7,1),_SunHwCtrlTpmEnable_Type())
sunHwCtrlTpmEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlTpmEnable.setStatus(_A)
_SunHwCtrlTpmActivate_Type=TruthValue
_SunHwCtrlTpmActivate_Object=MibScalar
sunHwCtrlTpmActivate=_SunHwCtrlTpmActivate_Object((1,3,6,1,4,1,42,2,175,104,1,7,2),_SunHwCtrlTpmActivate_Type())
sunHwCtrlTpmActivate.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlTpmActivate.setStatus(_A)
_SunHwCtrlTpmForceClear_Type=TruthValue
_SunHwCtrlTpmForceClear_Object=MibScalar
sunHwCtrlTpmForceClear=_SunHwCtrlTpmForceClear_Object((1,3,6,1,4,1,42,2,175,104,1,7,3),_SunHwCtrlTpmForceClear_Type())
sunHwCtrlTpmForceClear.setMaxAccess(_E)
if mibBuilder.loadTexts:sunHwCtrlTpmForceClear.setStatus(_A)
_SunHwCtrlMIBConformances_ObjectIdentity=ObjectIdentity
sunHwCtrlMIBConformances=_SunHwCtrlMIBConformances_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,2))
_SunHwCtrlCompliances_ObjectIdentity=ObjectIdentity
sunHwCtrlCompliances=_SunHwCtrlCompliances_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,2,1))
_SunHwCtrlGroups_ObjectIdentity=ObjectIdentity
sunHwCtrlGroups=_SunHwCtrlGroups_ObjectIdentity((1,3,6,1,4,1,42,2,175,104,2,2))
sunHwCtrlObjectsGroup=ObjectGroup((1,3,6,1,4,1,42,2,175,104,2,2,1))
sunHwCtrlObjectsGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:sunHwCtrlObjectsGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SunHwCtrlPowerMgmtID':SunHwCtrlPowerMgmtID,'SunHwCtrlPowerMgmtPolicy':SunHwCtrlPowerMgmtPolicy,'SunHwCtrlPowerMgmtBudgetTimelimitActions':SunHwCtrlPowerMgmtBudgetTimelimitActions,'sun':sun,'products':products,'ilom':ilom,'sunHwCtrlMIB':sunHwCtrlMIB,'sunHwCtrlMIBObjects':sunHwCtrlMIBObjects,'sunHwCtrlPowerMgmt':sunHwCtrlPowerMgmt,_J:sunHwCtrlReservedPSU,_K:sunHwCtrlTotalPSU,'sunHwCtrlPowerMgmtTable':sunHwCtrlPowerMgmtTable,'sunHwCtrlPowerMgmtEntry':sunHwCtrlPowerMgmtEntry,_H:sunHwCtrlPowerMgmtID,_L:sunHwCtrlPowerMgmtName,_M:sunHwCtrlPowerMgmtUnits,_N:sunHwCtrlPowerMgmtValue,_O:sunHwCtrlPowerMgmtActualPower,_P:sunHwCtrlPowerMgmtPermittedPower,_Q:sunHwCtrlPowerMgmtAvailablePower,_R:sunHwCtrlPowerMgmtPolicy,'sunHwCtrlPowerMgmtBudgetSettings':sunHwCtrlPowerMgmtBudgetSettings,_S:sunHwCtrlPowerMgmtBudget,_T:sunHwCtrlPowerMgmtBudgetMinPowerlimit,_U:sunHwCtrlPowerMgmtBudgetPowerlimit,_V:sunHwCtrlPowerMgmtBudgetTimelimit,_W:sunHwCtrlPowerMgmtBudgetTimelimitActions,_X:sunHwCtrlPowerMgmtBudgetOK,_Y:sunHwCtrlPowerMgmtBudgetCommitPending,_Z:sunHwCtrlPowerMgmtBudgetPendingPowerlimit,_a:sunHwCtrlPowerMgmtBudgetPendingTimelimit,_b:sunHwCtrlPowerMgmtBudgetPendingTimelimitActions,'sunHwCtrlPowerMgmtConsumptionThresholds':sunHwCtrlPowerMgmtConsumptionThresholds,_c:sunHwCtrlPowerMgmtConsumptionThreshold1,_d:sunHwCtrlPowerMgmtConsumptionThreshold2,'sunHwCtrlPowerMgmtSampling':sunHwCtrlPowerMgmtSampling,_e:sunHwCtrlPowerMgmtSamplingPeriod,_f:sunHwCtrlPowerMgmtSamplingTimestamp,_g:sunHwCtrlPowerMgmtSamplingMinimumPower,_h:sunHwCtrlPowerMgmtSamplingMaximumPower,_i:sunHwCtrlPowerMgmtSamplingAveragePower,'sunHwCtrlTPM':sunHwCtrlTPM,_j:sunHwCtrlTpmEnable,_k:sunHwCtrlTpmActivate,_l:sunHwCtrlTpmForceClear,'sunHwCtrlMIBConformances':sunHwCtrlMIBConformances,'sunHwCtrlCompliances':sunHwCtrlCompliances,'sunHwCtrlGroups':sunHwCtrlGroups,'sunHwCtrlObjectsGroup':sunHwCtrlObjectsGroup})