_T='ntcAupcCtrlConfGrpV1Standard'
_S='ntcAupcCtrlCurModulatorPower'
_R='ntcAupcCtrlReqModulatorPower'
_Q='ntcAupcCtrlPowerRequestCounter'
_P='ntcAupcCtrlClientFeedbackCounter'
_O='ntcAupcCtrlForwardConfigCounter'
_N='ntcAupcCtrlRefTerm'
_M='ntcAupcCtrlMaximumPowerStepDown'
_L='ntcAupcCtrlMaximumPowerStepUp'
_K='ntcAupcCtrlMaximumModPower'
_J='ntcAupcCtrlNominalModPower'
_I='ntcAupcCtrlEnable'
_H='Unsigned32'
_G='NtcEnable'
_F='dBm'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='NEWTEC-AUPCCONTROLLER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcAupcController=ModuleIdentity((1,3,6,1,4,1,5835,5,2,4200))
if mibBuilder.loadTexts:ntcAupcController.setRevisions(('2017-10-16 12:00','2014-02-03 12:00','2013-05-22 06:00'))
_NtcAupcCtrlObjects_ObjectIdentity=ObjectIdentity
ntcAupcCtrlObjects=_NtcAupcCtrlObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4200,1))
if mibBuilder.loadTexts:ntcAupcCtrlObjects.setStatus(_A)
class _NtcAupcCtrlEnable_Type(NtcEnable):defaultValue=0
_NtcAupcCtrlEnable_Type.__name__=_G
_NtcAupcCtrlEnable_Object=MibScalar
ntcAupcCtrlEnable=_NtcAupcCtrlEnable_Object((1,3,6,1,4,1,5835,5,2,4200,1,1),_NtcAupcCtrlEnable_Type())
ntcAupcCtrlEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcCtrlEnable.setStatus(_A)
class _NtcAupcCtrlNominalModPower_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,100))
_NtcAupcCtrlNominalModPower_Type.__name__=_C
_NtcAupcCtrlNominalModPower_Object=MibScalar
ntcAupcCtrlNominalModPower=_NtcAupcCtrlNominalModPower_Object((1,3,6,1,4,1,5835,5,2,4200,1,2),_NtcAupcCtrlNominalModPower_Type())
ntcAupcCtrlNominalModPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcCtrlNominalModPower.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcCtrlNominalModPower.setUnits(_F)
class _NtcAupcCtrlMaximumModPower_Type(Integer32):defaultValue=-150;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,100))
_NtcAupcCtrlMaximumModPower_Type.__name__=_C
_NtcAupcCtrlMaximumModPower_Object=MibScalar
ntcAupcCtrlMaximumModPower=_NtcAupcCtrlMaximumModPower_Object((1,3,6,1,4,1,5835,5,2,4200,1,3),_NtcAupcCtrlMaximumModPower_Type())
ntcAupcCtrlMaximumModPower.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcCtrlMaximumModPower.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcCtrlMaximumModPower.setUnits(_F)
class _NtcAupcCtrlMaximumPowerStepUp_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NtcAupcCtrlMaximumPowerStepUp_Type.__name__=_C
_NtcAupcCtrlMaximumPowerStepUp_Object=MibScalar
ntcAupcCtrlMaximumPowerStepUp=_NtcAupcCtrlMaximumPowerStepUp_Object((1,3,6,1,4,1,5835,5,2,4200,1,4),_NtcAupcCtrlMaximumPowerStepUp_Type())
ntcAupcCtrlMaximumPowerStepUp.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcCtrlMaximumPowerStepUp.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcCtrlMaximumPowerStepUp.setUnits('dBm/s')
class _NtcAupcCtrlMaximumPowerStepDown_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_NtcAupcCtrlMaximumPowerStepDown_Type.__name__=_C
_NtcAupcCtrlMaximumPowerStepDown_Object=MibScalar
ntcAupcCtrlMaximumPowerStepDown=_NtcAupcCtrlMaximumPowerStepDown_Object((1,3,6,1,4,1,5835,5,2,4200,1,5),_NtcAupcCtrlMaximumPowerStepDown_Type())
ntcAupcCtrlMaximumPowerStepDown.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcCtrlMaximumPowerStepDown.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcCtrlMaximumPowerStepDown.setUnits('dBm/s')
class _NtcAupcCtrlRefTerm_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65277))
_NtcAupcCtrlRefTerm_Type.__name__=_H
_NtcAupcCtrlRefTerm_Object=MibScalar
ntcAupcCtrlRefTerm=_NtcAupcCtrlRefTerm_Object((1,3,6,1,4,1,5835,5,2,4200,1,6),_NtcAupcCtrlRefTerm_Type())
ntcAupcCtrlRefTerm.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcAupcCtrlRefTerm.setStatus(_A)
_NtcAupcCtrlMonitoring_ObjectIdentity=ObjectIdentity
ntcAupcCtrlMonitoring=_NtcAupcCtrlMonitoring_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4200,1,7))
if mibBuilder.loadTexts:ntcAupcCtrlMonitoring.setStatus(_A)
_NtcAupcCtrlForwardConfigCounter_Type=Counter64
_NtcAupcCtrlForwardConfigCounter_Object=MibScalar
ntcAupcCtrlForwardConfigCounter=_NtcAupcCtrlForwardConfigCounter_Object((1,3,6,1,4,1,5835,5,2,4200,1,7,1),_NtcAupcCtrlForwardConfigCounter_Type())
ntcAupcCtrlForwardConfigCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAupcCtrlForwardConfigCounter.setStatus(_A)
_NtcAupcCtrlClientFeedbackCounter_Type=Counter64
_NtcAupcCtrlClientFeedbackCounter_Object=MibScalar
ntcAupcCtrlClientFeedbackCounter=_NtcAupcCtrlClientFeedbackCounter_Object((1,3,6,1,4,1,5835,5,2,4200,1,7,2),_NtcAupcCtrlClientFeedbackCounter_Type())
ntcAupcCtrlClientFeedbackCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAupcCtrlClientFeedbackCounter.setStatus(_A)
_NtcAupcCtrlPowerRequestCounter_Type=Counter64
_NtcAupcCtrlPowerRequestCounter_Object=MibScalar
ntcAupcCtrlPowerRequestCounter=_NtcAupcCtrlPowerRequestCounter_Object((1,3,6,1,4,1,5835,5,2,4200,1,7,3),_NtcAupcCtrlPowerRequestCounter_Type())
ntcAupcCtrlPowerRequestCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAupcCtrlPowerRequestCounter.setStatus(_A)
class _NtcAupcCtrlReqModulatorPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,100))
_NtcAupcCtrlReqModulatorPower_Type.__name__=_C
_NtcAupcCtrlReqModulatorPower_Object=MibScalar
ntcAupcCtrlReqModulatorPower=_NtcAupcCtrlReqModulatorPower_Object((1,3,6,1,4,1,5835,5,2,4200,1,7,4),_NtcAupcCtrlReqModulatorPower_Type())
ntcAupcCtrlReqModulatorPower.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAupcCtrlReqModulatorPower.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcCtrlReqModulatorPower.setUnits(_F)
class _NtcAupcCtrlCurModulatorPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,100))
_NtcAupcCtrlCurModulatorPower_Type.__name__=_C
_NtcAupcCtrlCurModulatorPower_Object=MibScalar
ntcAupcCtrlCurModulatorPower=_NtcAupcCtrlCurModulatorPower_Object((1,3,6,1,4,1,5835,5,2,4200,1,7,5),_NtcAupcCtrlCurModulatorPower_Type())
ntcAupcCtrlCurModulatorPower.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAupcCtrlCurModulatorPower.setStatus(_A)
if mibBuilder.loadTexts:ntcAupcCtrlCurModulatorPower.setUnits(_F)
_NtcAupcCtrlConformance_ObjectIdentity=ObjectIdentity
ntcAupcCtrlConformance=_NtcAupcCtrlConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4200,2))
if mibBuilder.loadTexts:ntcAupcCtrlConformance.setStatus(_A)
_NtcAupcCtrlConfCompliance_ObjectIdentity=ObjectIdentity
ntcAupcCtrlConfCompliance=_NtcAupcCtrlConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4200,2,1))
if mibBuilder.loadTexts:ntcAupcCtrlConfCompliance.setStatus(_A)
_NtcAupcCtrlConfGroup_ObjectIdentity=ObjectIdentity
ntcAupcCtrlConfGroup=_NtcAupcCtrlConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,4200,2,2))
if mibBuilder.loadTexts:ntcAupcCtrlConfGroup.setStatus(_A)
ntcAupcCtrlConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,4200,2,2,1))
ntcAupcCtrlConfGrpV1Standard.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ntcAupcCtrlConfGrpV1Standard.setStatus(_A)
ntcAupcCtrlConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,4200,2,1,1))
ntcAupcCtrlConfCompV1Standard.setObjects((_B,_T))
if mibBuilder.loadTexts:ntcAupcCtrlConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcAupcController':ntcAupcController,'ntcAupcCtrlObjects':ntcAupcCtrlObjects,_I:ntcAupcCtrlEnable,_J:ntcAupcCtrlNominalModPower,_K:ntcAupcCtrlMaximumModPower,_L:ntcAupcCtrlMaximumPowerStepUp,_M:ntcAupcCtrlMaximumPowerStepDown,_N:ntcAupcCtrlRefTerm,'ntcAupcCtrlMonitoring':ntcAupcCtrlMonitoring,_O:ntcAupcCtrlForwardConfigCounter,_P:ntcAupcCtrlClientFeedbackCounter,_Q:ntcAupcCtrlPowerRequestCounter,_R:ntcAupcCtrlReqModulatorPower,_S:ntcAupcCtrlCurModulatorPower,'ntcAupcCtrlConformance':ntcAupcCtrlConformance,'ntcAupcCtrlConfCompliance':ntcAupcCtrlConfCompliance,'ntcAupcCtrlConfCompV1Standard':ntcAupcCtrlConfCompV1Standard,'ntcAupcCtrlConfGroup':ntcAupcCtrlConfGroup,_T:ntcAupcCtrlConfGrpV1Standard})