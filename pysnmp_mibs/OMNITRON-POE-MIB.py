_c='ostPoeGroup'
_b='ostPoEPortHeartbeatDeferTime'
_a='ostPoEPortHeartbeatStatus'
_Z='ostPoePortHeartbeatNumberRestarts'
_Y='ostPoePortHeartbeatErrorAction'
_X='ostPoePortHeartbeatErrorDetection'
_W='ostPoePortHeartbeatInterval'
_V='ostPoePortHeartbeatIpAddress'
_U='ostPoePortHeartbeatEnable'
_T='ostPoePortPseStatus'
_S='ostPoePortPseCurrentSupplied'
_R='ostPoePortPseVoltageSupplied'
_Q='ostPoePortPdMode'
_P='ostPoePortPse60wMode'
_O='ostPoePortPseEnable'
_N='ostPoeGlobalCfgTotalPwr'
_M='ostPoeGlobalCfgPwrLimitationEnable'
_L='heartbeatDisabled'
_K='ostPoePortCfgIndex'
_J='TruthValue'
_I='IpAddress'
_H='0.0'
_G='OstFloatValue'
_F='read-only'
_E='Unsigned32'
_D='Integer32'
_C='read-write'
_B='OMNITRON-POE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
OstFloatValue,OstPortSingleIndex,omnitron=mibBuilder.importSymbols('OMNITRON-TC-MIB',_G,'OstPortSingleIndex','omnitron')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,_I,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_J)
omnitronPoeMib=ModuleIdentity((1,3,6,1,4,1,7342,15))
if mibBuilder.loadTexts:omnitronPoeMib.setRevisions(('2015-01-19 12:00',))
_OstPoeGlobalCfgTable_ObjectIdentity=ObjectIdentity
ostPoeGlobalCfgTable=_OstPoeGlobalCfgTable_ObjectIdentity((1,3,6,1,4,1,7342,15,1))
class _OstPoeGlobalCfgPwrLimitationEnable_Type(TruthValue):defaultValue=2
_OstPoeGlobalCfgPwrLimitationEnable_Type.__name__=_J
_OstPoeGlobalCfgPwrLimitationEnable_Object=MibScalar
ostPoeGlobalCfgPwrLimitationEnable=_OstPoeGlobalCfgPwrLimitationEnable_Object((1,3,6,1,4,1,7342,15,1,1),_OstPoeGlobalCfgPwrLimitationEnable_Type())
ostPoeGlobalCfgPwrLimitationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoeGlobalCfgPwrLimitationEnable.setStatus(_A)
class _OstPoeGlobalCfgTotalPwr_Type(OstFloatValue):defaultValue=OctetString(_H)
_OstPoeGlobalCfgTotalPwr_Type.__name__=_G
_OstPoeGlobalCfgTotalPwr_Object=MibScalar
ostPoeGlobalCfgTotalPwr=_OstPoeGlobalCfgTotalPwr_Object((1,3,6,1,4,1,7342,15,1,2),_OstPoeGlobalCfgTotalPwr_Type())
ostPoeGlobalCfgTotalPwr.setMaxAccess(_F)
if mibBuilder.loadTexts:ostPoeGlobalCfgTotalPwr.setStatus(_A)
_OstPoePortCfgTable_Object=MibTable
ostPoePortCfgTable=_OstPoePortCfgTable_Object((1,3,6,1,4,1,7342,15,2))
if mibBuilder.loadTexts:ostPoePortCfgTable.setStatus(_A)
_OstPoePortCfgEntry_Object=MibTableRow
ostPoePortCfgEntry=_OstPoePortCfgEntry_Object((1,3,6,1,4,1,7342,15,2,1))
ostPoePortCfgEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:ostPoePortCfgEntry.setStatus(_A)
_OstPoePortCfgIndex_Type=OstPortSingleIndex
_OstPoePortCfgIndex_Object=MibTableColumn
ostPoePortCfgIndex=_OstPoePortCfgIndex_Object((1,3,6,1,4,1,7342,15,2,1,1),_OstPoePortCfgIndex_Type())
ostPoePortCfgIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ostPoePortCfgIndex.setStatus(_A)
class _OstPoePortPseEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pseDisabled',1),('pseEnabled',2)))
_OstPoePortPseEnable_Type.__name__=_D
_OstPoePortPseEnable_Object=MibTableColumn
ostPoePortPseEnable=_OstPoePortPseEnable_Object((1,3,6,1,4,1,7342,15,2,1,2),_OstPoePortPseEnable_Type())
ostPoePortPseEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortPseEnable.setStatus(_A)
class _OstPoePortPse60wMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('pse60wNotAvail',0),('pse60wAuto',1),('pse60wForce',2)))
_OstPoePortPse60wMode_Type.__name__=_D
_OstPoePortPse60wMode_Object=MibTableColumn
ostPoePortPse60wMode=_OstPoePortPse60wMode_Object((1,3,6,1,4,1,7342,15,2,1,3),_OstPoePortPse60wMode_Type())
ostPoePortPse60wMode.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortPse60wMode.setStatus(_A)
class _OstPoePortPdMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('pdModeNotDetected',1),('pdModeNotClassified',2),('pdModeFailure',3),('pdModeClass0',4),('pdModeClass1',5),('pdModeClass2',6),('pdModeClass3',7),('pdModeClass4',8),('pdMode60W',9)))
_OstPoePortPdMode_Type.__name__=_D
_OstPoePortPdMode_Object=MibTableColumn
ostPoePortPdMode=_OstPoePortPdMode_Object((1,3,6,1,4,1,7342,15,2,1,4),_OstPoePortPdMode_Type())
ostPoePortPdMode.setMaxAccess(_F)
if mibBuilder.loadTexts:ostPoePortPdMode.setStatus(_A)
class _OstPoePortPseVoltageSupplied_Type(OstFloatValue):defaultValue=OctetString(_H)
_OstPoePortPseVoltageSupplied_Type.__name__=_G
_OstPoePortPseVoltageSupplied_Object=MibTableColumn
ostPoePortPseVoltageSupplied=_OstPoePortPseVoltageSupplied_Object((1,3,6,1,4,1,7342,15,2,1,5),_OstPoePortPseVoltageSupplied_Type())
ostPoePortPseVoltageSupplied.setMaxAccess(_F)
if mibBuilder.loadTexts:ostPoePortPseVoltageSupplied.setStatus(_A)
class _OstPoePortPseCurrentSupplied_Type(OstFloatValue):defaultValue=OctetString(_H)
_OstPoePortPseCurrentSupplied_Type.__name__=_G
_OstPoePortPseCurrentSupplied_Object=MibTableColumn
ostPoePortPseCurrentSupplied=_OstPoePortPseCurrentSupplied_Object((1,3,6,1,4,1,7342,15,2,1,6),_OstPoePortPseCurrentSupplied_Type())
ostPoePortPseCurrentSupplied.setMaxAccess(_F)
if mibBuilder.loadTexts:ostPoePortPseCurrentSupplied.setStatus(_A)
class _OstPoePortPseStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notApplicable',1),('pdNormal',2),('pdOverCurrent',3),('pdBrownOut',4),('pdInsufficientPower',5)))
_OstPoePortPseStatus_Type.__name__=_D
_OstPoePortPseStatus_Object=MibTableColumn
ostPoePortPseStatus=_OstPoePortPseStatus_Object((1,3,6,1,4,1,7342,15,2,1,7),_OstPoePortPseStatus_Type())
ostPoePortPseStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortPseStatus.setStatus(_A)
class _OstPoePortHeartbeatEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('heartbeatEnabled',2)))
_OstPoePortHeartbeatEnable_Type.__name__=_D
_OstPoePortHeartbeatEnable_Object=MibTableColumn
ostPoePortHeartbeatEnable=_OstPoePortHeartbeatEnable_Object((1,3,6,1,4,1,7342,15,2,1,8),_OstPoePortHeartbeatEnable_Type())
ostPoePortHeartbeatEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortHeartbeatEnable.setStatus(_A)
class _OstPoePortHeartbeatIpAddress_Type(IpAddress):defaultHexValue='00000000'
_OstPoePortHeartbeatIpAddress_Type.__name__=_I
_OstPoePortHeartbeatIpAddress_Object=MibTableColumn
ostPoePortHeartbeatIpAddress=_OstPoePortHeartbeatIpAddress_Object((1,3,6,1,4,1,7342,15,2,1,9),_OstPoePortHeartbeatIpAddress_Type())
ostPoePortHeartbeatIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortHeartbeatIpAddress.setStatus(_A)
class _OstPoePortHeartbeatInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_OstPoePortHeartbeatInterval_Type.__name__=_E
_OstPoePortHeartbeatInterval_Object=MibTableColumn
ostPoePortHeartbeatInterval=_OstPoePortHeartbeatInterval_Object((1,3,6,1,4,1,7342,15,2,1,10),_OstPoePortHeartbeatInterval_Type())
ostPoePortHeartbeatInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortHeartbeatInterval.setStatus(_A)
class _OstPoePortHeartbeatErrorDetection_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_OstPoePortHeartbeatErrorDetection_Type.__name__=_E
_OstPoePortHeartbeatErrorDetection_Object=MibTableColumn
ostPoePortHeartbeatErrorDetection=_OstPoePortHeartbeatErrorDetection_Object((1,3,6,1,4,1,7342,15,2,1,11),_OstPoePortHeartbeatErrorDetection_Type())
ostPoePortHeartbeatErrorDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortHeartbeatErrorDetection.setStatus(_A)
class _OstPoePortHeartbeatErrorAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('errorLostIgnored',1),('errorRestart',2),('errorShutdown',3)))
_OstPoePortHeartbeatErrorAction_Type.__name__=_D
_OstPoePortHeartbeatErrorAction_Object=MibTableColumn
ostPoePortHeartbeatErrorAction=_OstPoePortHeartbeatErrorAction_Object((1,3,6,1,4,1,7342,15,2,1,12),_OstPoePortHeartbeatErrorAction_Type())
ostPoePortHeartbeatErrorAction.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortHeartbeatErrorAction.setStatus(_A)
class _OstPoePortHeartbeatNumberRestarts_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_OstPoePortHeartbeatNumberRestarts_Type.__name__=_E
_OstPoePortHeartbeatNumberRestarts_Object=MibTableColumn
ostPoePortHeartbeatNumberRestarts=_OstPoePortHeartbeatNumberRestarts_Object((1,3,6,1,4,1,7342,15,2,1,13),_OstPoePortHeartbeatNumberRestarts_Type())
ostPoePortHeartbeatNumberRestarts.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoePortHeartbeatNumberRestarts.setStatus(_A)
class _OstPoEPortHeartbeatStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),('heartbeatAvailable',2),('heartbeatErrored',3),('heartbeatRestart',4),('heartbeatShutdown',5)))
_OstPoEPortHeartbeatStatus_Type.__name__=_D
_OstPoEPortHeartbeatStatus_Object=MibTableColumn
ostPoEPortHeartbeatStatus=_OstPoEPortHeartbeatStatus_Object((1,3,6,1,4,1,7342,15,2,1,14),_OstPoEPortHeartbeatStatus_Type())
ostPoEPortHeartbeatStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ostPoEPortHeartbeatStatus.setStatus(_A)
class _OstPoEPortHeartbeatDeferTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_OstPoEPortHeartbeatDeferTime_Type.__name__=_E
_OstPoEPortHeartbeatDeferTime_Object=MibTableColumn
ostPoEPortHeartbeatDeferTime=_OstPoEPortHeartbeatDeferTime_Object((1,3,6,1,4,1,7342,15,2,1,15),_OstPoEPortHeartbeatDeferTime_Type())
ostPoEPortHeartbeatDeferTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ostPoEPortHeartbeatDeferTime.setStatus(_A)
_OstPoeCompliances_ObjectIdentity=ObjectIdentity
ostPoeCompliances=_OstPoeCompliances_ObjectIdentity((1,3,6,1,4,1,7342,15,3))
_OstPoeGroups_ObjectIdentity=ObjectIdentity
ostPoeGroups=_OstPoeGroups_ObjectIdentity((1,3,6,1,4,1,7342,15,4))
ostPoeGroup=ObjectGroup((1,3,6,1,4,1,7342,15,4,1))
ostPoeGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ostPoeGroup.setStatus(_A)
ostPoeCompliance=ModuleCompliance((1,3,6,1,4,1,7342,15,3,2))
ostPoeCompliance.setObjects((_B,_c))
if mibBuilder.loadTexts:ostPoeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'omnitronPoeMib':omnitronPoeMib,'ostPoeGlobalCfgTable':ostPoeGlobalCfgTable,_M:ostPoeGlobalCfgPwrLimitationEnable,_N:ostPoeGlobalCfgTotalPwr,'ostPoePortCfgTable':ostPoePortCfgTable,'ostPoePortCfgEntry':ostPoePortCfgEntry,_K:ostPoePortCfgIndex,_O:ostPoePortPseEnable,_P:ostPoePortPse60wMode,_Q:ostPoePortPdMode,_R:ostPoePortPseVoltageSupplied,_S:ostPoePortPseCurrentSupplied,_T:ostPoePortPseStatus,_U:ostPoePortHeartbeatEnable,_V:ostPoePortHeartbeatIpAddress,_W:ostPoePortHeartbeatInterval,_X:ostPoePortHeartbeatErrorDetection,_Y:ostPoePortHeartbeatErrorAction,_Z:ostPoePortHeartbeatNumberRestarts,_a:ostPoEPortHeartbeatStatus,_b:ostPoEPortHeartbeatDeferTime,'ostPoeCompliances':ostPoeCompliances,'ostPoeCompliance':ostPoeCompliance,'ostPoeGroups':ostPoeGroups,_c:ostPoeGroup})