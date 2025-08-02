_l='cerentGenericPmStatsIntervalGroup'
_k='cerentGenericPmStatsCurrentGroup'
_j='cerentGenericPmThresholdGroup'
_i='cerentGenericPmAlarmThresholdHCValue'
_h='cerentGenericPmAlarmThresholdOverFlowValue'
_g='cerentGenericPmAlarmThresholdValue'
_f='cerentGenericPmStatsIntervalValidData'
_e='cerentGenericPmStatsIntervalHCValue'
_d='cerentGenericPmStatsIntervalOverFlowValue'
_c='cerentGenericPmStatsIntervalValue'
_b='cerentGenericPmStatsCurrentValidIntervals'
_a='cerentGenericPmStatsCurrentValidData'
_Z='cerentGenericPmStatsCurrentHCValue'
_Y='cerentGenericPmStatsCurrentOverFlowValue'
_X='cerentGenericPmStatsCurrentValue'
_W='cerentGenericPmThresholdHCValue'
_V='cerentGenericPmThresholdOverFlowValue'
_U='cerentGenericPmThresholdValue'
_T='cerentGenericPmAlarmThresholdMonitorType'
_S='cerentGenericPmAlarmThresholdIndex'
_R='cerentGenericPmStatsIntervalNumber'
_Q='cerentGenericPmStatsIntervalPeriod'
_P='cerentGenericPmStatsIntervalLocation'
_O='cerentGenericPmStatsIntervalType'
_N='cerentGenericPmStatsIntervalIndex'
_M='cerentGenericPmStatsCurrentPeriod'
_L='cerentGenericPmStatsCurrentLocation'
_K='cerentGenericPmStatsCurrentType'
_J='cerentGenericPmStatsCurrentIndex'
_I='cerentGenericPmThresholdPeriod'
_H='cerentGenericPmThresholdLocation'
_G='cerentGenericPmThresholdMonitorType'
_F='cerentGenericPmThresholdIndex'
_E='Integer32'
_D='read-only'
_C='not-accessible'
_B='CERENT-GENERIC-PM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cerentGeneric,cerentModules,cerentRequirements=mibBuilder.importSymbols('CERENT-GLOBAL-REGISTRY','cerentGeneric','cerentModules','cerentRequirements')
CerentAlarmThresholdMonitorType,CerentLocation,CerentMonitorType,CerentPeriod=mibBuilder.importSymbols('CERENT-TC','CerentAlarmThresholdMonitorType','CerentLocation','CerentMonitorType','CerentPeriod')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cerentGenericPmMIB=ModuleIdentity((1,3,6,1,4,1,3607,1,10,130))
if mibBuilder.loadTexts:cerentGenericPmMIB.setRevisions(('2004-10-13 00:00',))
_CerentGenericPmMIBObjects_ObjectIdentity=ObjectIdentity
cerentGenericPmMIBObjects=_CerentGenericPmMIBObjects_ObjectIdentity((1,3,6,1,4,1,3607,2,90))
_CerentGenericPmThresholdTable_Object=MibTable
cerentGenericPmThresholdTable=_CerentGenericPmThresholdTable_Object((1,3,6,1,4,1,3607,2,90,10))
if mibBuilder.loadTexts:cerentGenericPmThresholdTable.setStatus(_A)
_CerentGenericPmThresholdEntry_Object=MibTableRow
cerentGenericPmThresholdEntry=_CerentGenericPmThresholdEntry_Object((1,3,6,1,4,1,3607,2,90,10,1))
cerentGenericPmThresholdEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cerentGenericPmThresholdEntry.setStatus(_A)
class _CerentGenericPmThresholdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CerentGenericPmThresholdIndex_Type.__name__=_E
_CerentGenericPmThresholdIndex_Object=MibTableColumn
cerentGenericPmThresholdIndex=_CerentGenericPmThresholdIndex_Object((1,3,6,1,4,1,3607,2,90,10,1,10),_CerentGenericPmThresholdIndex_Type())
cerentGenericPmThresholdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmThresholdIndex.setStatus(_A)
_CerentGenericPmThresholdMonitorType_Type=CerentMonitorType
_CerentGenericPmThresholdMonitorType_Object=MibTableColumn
cerentGenericPmThresholdMonitorType=_CerentGenericPmThresholdMonitorType_Object((1,3,6,1,4,1,3607,2,90,10,1,20),_CerentGenericPmThresholdMonitorType_Type())
cerentGenericPmThresholdMonitorType.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmThresholdMonitorType.setStatus(_A)
_CerentGenericPmThresholdLocation_Type=CerentLocation
_CerentGenericPmThresholdLocation_Object=MibTableColumn
cerentGenericPmThresholdLocation=_CerentGenericPmThresholdLocation_Object((1,3,6,1,4,1,3607,2,90,10,1,30),_CerentGenericPmThresholdLocation_Type())
cerentGenericPmThresholdLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmThresholdLocation.setStatus(_A)
_CerentGenericPmThresholdPeriod_Type=CerentPeriod
_CerentGenericPmThresholdPeriod_Object=MibTableColumn
cerentGenericPmThresholdPeriod=_CerentGenericPmThresholdPeriod_Object((1,3,6,1,4,1,3607,2,90,10,1,40),_CerentGenericPmThresholdPeriod_Type())
cerentGenericPmThresholdPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmThresholdPeriod.setStatus(_A)
_CerentGenericPmThresholdValue_Type=Integer32
_CerentGenericPmThresholdValue_Object=MibTableColumn
cerentGenericPmThresholdValue=_CerentGenericPmThresholdValue_Object((1,3,6,1,4,1,3607,2,90,10,1,50),_CerentGenericPmThresholdValue_Type())
cerentGenericPmThresholdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmThresholdValue.setStatus(_A)
_CerentGenericPmThresholdOverFlowValue_Type=Integer32
_CerentGenericPmThresholdOverFlowValue_Object=MibTableColumn
cerentGenericPmThresholdOverFlowValue=_CerentGenericPmThresholdOverFlowValue_Object((1,3,6,1,4,1,3607,2,90,10,1,60),_CerentGenericPmThresholdOverFlowValue_Type())
cerentGenericPmThresholdOverFlowValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmThresholdOverFlowValue.setStatus(_A)
_CerentGenericPmThresholdHCValue_Type=Counter64
_CerentGenericPmThresholdHCValue_Object=MibTableColumn
cerentGenericPmThresholdHCValue=_CerentGenericPmThresholdHCValue_Object((1,3,6,1,4,1,3607,2,90,10,1,70),_CerentGenericPmThresholdHCValue_Type())
cerentGenericPmThresholdHCValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmThresholdHCValue.setStatus(_A)
_CerentGenericPmStatsCurrentTable_Object=MibTable
cerentGenericPmStatsCurrentTable=_CerentGenericPmStatsCurrentTable_Object((1,3,6,1,4,1,3607,2,90,20))
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentTable.setStatus(_A)
_CerentGenericPmStatsCurrentEntry_Object=MibTableRow
cerentGenericPmStatsCurrentEntry=_CerentGenericPmStatsCurrentEntry_Object((1,3,6,1,4,1,3607,2,90,20,1))
cerentGenericPmStatsCurrentEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentEntry.setStatus(_A)
class _CerentGenericPmStatsCurrentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CerentGenericPmStatsCurrentIndex_Type.__name__=_E
_CerentGenericPmStatsCurrentIndex_Object=MibTableColumn
cerentGenericPmStatsCurrentIndex=_CerentGenericPmStatsCurrentIndex_Object((1,3,6,1,4,1,3607,2,90,20,1,10),_CerentGenericPmStatsCurrentIndex_Type())
cerentGenericPmStatsCurrentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentIndex.setStatus(_A)
_CerentGenericPmStatsCurrentType_Type=CerentMonitorType
_CerentGenericPmStatsCurrentType_Object=MibTableColumn
cerentGenericPmStatsCurrentType=_CerentGenericPmStatsCurrentType_Object((1,3,6,1,4,1,3607,2,90,20,1,20),_CerentGenericPmStatsCurrentType_Type())
cerentGenericPmStatsCurrentType.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentType.setStatus(_A)
_CerentGenericPmStatsCurrentLocation_Type=CerentLocation
_CerentGenericPmStatsCurrentLocation_Object=MibTableColumn
cerentGenericPmStatsCurrentLocation=_CerentGenericPmStatsCurrentLocation_Object((1,3,6,1,4,1,3607,2,90,20,1,30),_CerentGenericPmStatsCurrentLocation_Type())
cerentGenericPmStatsCurrentLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentLocation.setStatus(_A)
_CerentGenericPmStatsCurrentPeriod_Type=CerentPeriod
_CerentGenericPmStatsCurrentPeriod_Object=MibTableColumn
cerentGenericPmStatsCurrentPeriod=_CerentGenericPmStatsCurrentPeriod_Object((1,3,6,1,4,1,3607,2,90,20,1,40),_CerentGenericPmStatsCurrentPeriod_Type())
cerentGenericPmStatsCurrentPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentPeriod.setStatus(_A)
_CerentGenericPmStatsCurrentValue_Type=Integer32
_CerentGenericPmStatsCurrentValue_Object=MibTableColumn
cerentGenericPmStatsCurrentValue=_CerentGenericPmStatsCurrentValue_Object((1,3,6,1,4,1,3607,2,90,20,1,50),_CerentGenericPmStatsCurrentValue_Type())
cerentGenericPmStatsCurrentValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentValue.setStatus(_A)
_CerentGenericPmStatsCurrentOverFlowValue_Type=Integer32
_CerentGenericPmStatsCurrentOverFlowValue_Object=MibTableColumn
cerentGenericPmStatsCurrentOverFlowValue=_CerentGenericPmStatsCurrentOverFlowValue_Object((1,3,6,1,4,1,3607,2,90,20,1,60),_CerentGenericPmStatsCurrentOverFlowValue_Type())
cerentGenericPmStatsCurrentOverFlowValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentOverFlowValue.setStatus(_A)
_CerentGenericPmStatsCurrentHCValue_Type=Counter64
_CerentGenericPmStatsCurrentHCValue_Object=MibTableColumn
cerentGenericPmStatsCurrentHCValue=_CerentGenericPmStatsCurrentHCValue_Object((1,3,6,1,4,1,3607,2,90,20,1,70),_CerentGenericPmStatsCurrentHCValue_Type())
cerentGenericPmStatsCurrentHCValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentHCValue.setStatus(_A)
_CerentGenericPmStatsCurrentValidData_Type=TruthValue
_CerentGenericPmStatsCurrentValidData_Object=MibTableColumn
cerentGenericPmStatsCurrentValidData=_CerentGenericPmStatsCurrentValidData_Object((1,3,6,1,4,1,3607,2,90,20,1,80),_CerentGenericPmStatsCurrentValidData_Type())
cerentGenericPmStatsCurrentValidData.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentValidData.setStatus(_A)
class _CerentGenericPmStatsCurrentValidIntervals_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CerentGenericPmStatsCurrentValidIntervals_Type.__name__=_E
_CerentGenericPmStatsCurrentValidIntervals_Object=MibTableColumn
cerentGenericPmStatsCurrentValidIntervals=_CerentGenericPmStatsCurrentValidIntervals_Object((1,3,6,1,4,1,3607,2,90,20,1,90),_CerentGenericPmStatsCurrentValidIntervals_Type())
cerentGenericPmStatsCurrentValidIntervals.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentValidIntervals.setStatus(_A)
_CerentGenericPmStatsIntervalTable_Object=MibTable
cerentGenericPmStatsIntervalTable=_CerentGenericPmStatsIntervalTable_Object((1,3,6,1,4,1,3607,2,90,30))
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalTable.setStatus(_A)
_CerentGenericPmStatsIntervalEntry_Object=MibTableRow
cerentGenericPmStatsIntervalEntry=_CerentGenericPmStatsIntervalEntry_Object((1,3,6,1,4,1,3607,2,90,30,1))
cerentGenericPmStatsIntervalEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalEntry.setStatus(_A)
class _CerentGenericPmStatsIntervalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CerentGenericPmStatsIntervalIndex_Type.__name__=_E
_CerentGenericPmStatsIntervalIndex_Object=MibTableColumn
cerentGenericPmStatsIntervalIndex=_CerentGenericPmStatsIntervalIndex_Object((1,3,6,1,4,1,3607,2,90,30,1,10),_CerentGenericPmStatsIntervalIndex_Type())
cerentGenericPmStatsIntervalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalIndex.setStatus(_A)
_CerentGenericPmStatsIntervalType_Type=CerentMonitorType
_CerentGenericPmStatsIntervalType_Object=MibTableColumn
cerentGenericPmStatsIntervalType=_CerentGenericPmStatsIntervalType_Object((1,3,6,1,4,1,3607,2,90,30,1,20),_CerentGenericPmStatsIntervalType_Type())
cerentGenericPmStatsIntervalType.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalType.setStatus(_A)
_CerentGenericPmStatsIntervalLocation_Type=CerentLocation
_CerentGenericPmStatsIntervalLocation_Object=MibTableColumn
cerentGenericPmStatsIntervalLocation=_CerentGenericPmStatsIntervalLocation_Object((1,3,6,1,4,1,3607,2,90,30,1,30),_CerentGenericPmStatsIntervalLocation_Type())
cerentGenericPmStatsIntervalLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalLocation.setStatus(_A)
_CerentGenericPmStatsIntervalPeriod_Type=CerentPeriod
_CerentGenericPmStatsIntervalPeriod_Object=MibTableColumn
cerentGenericPmStatsIntervalPeriod=_CerentGenericPmStatsIntervalPeriod_Object((1,3,6,1,4,1,3607,2,90,30,1,40),_CerentGenericPmStatsIntervalPeriod_Type())
cerentGenericPmStatsIntervalPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalPeriod.setStatus(_A)
class _CerentGenericPmStatsIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_CerentGenericPmStatsIntervalNumber_Type.__name__=_E
_CerentGenericPmStatsIntervalNumber_Object=MibTableColumn
cerentGenericPmStatsIntervalNumber=_CerentGenericPmStatsIntervalNumber_Object((1,3,6,1,4,1,3607,2,90,30,1,50),_CerentGenericPmStatsIntervalNumber_Type())
cerentGenericPmStatsIntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalNumber.setStatus(_A)
_CerentGenericPmStatsIntervalValue_Type=Integer32
_CerentGenericPmStatsIntervalValue_Object=MibTableColumn
cerentGenericPmStatsIntervalValue=_CerentGenericPmStatsIntervalValue_Object((1,3,6,1,4,1,3607,2,90,30,1,60),_CerentGenericPmStatsIntervalValue_Type())
cerentGenericPmStatsIntervalValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalValue.setStatus(_A)
_CerentGenericPmStatsIntervalOverFlowValue_Type=Integer32
_CerentGenericPmStatsIntervalOverFlowValue_Object=MibTableColumn
cerentGenericPmStatsIntervalOverFlowValue=_CerentGenericPmStatsIntervalOverFlowValue_Object((1,3,6,1,4,1,3607,2,90,30,1,70),_CerentGenericPmStatsIntervalOverFlowValue_Type())
cerentGenericPmStatsIntervalOverFlowValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalOverFlowValue.setStatus(_A)
_CerentGenericPmStatsIntervalHCValue_Type=Counter64
_CerentGenericPmStatsIntervalHCValue_Object=MibTableColumn
cerentGenericPmStatsIntervalHCValue=_CerentGenericPmStatsIntervalHCValue_Object((1,3,6,1,4,1,3607,2,90,30,1,80),_CerentGenericPmStatsIntervalHCValue_Type())
cerentGenericPmStatsIntervalHCValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalHCValue.setStatus(_A)
_CerentGenericPmStatsIntervalValidData_Type=TruthValue
_CerentGenericPmStatsIntervalValidData_Object=MibTableColumn
cerentGenericPmStatsIntervalValidData=_CerentGenericPmStatsIntervalValidData_Object((1,3,6,1,4,1,3607,2,90,30,1,90),_CerentGenericPmStatsIntervalValidData_Type())
cerentGenericPmStatsIntervalValidData.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalValidData.setStatus(_A)
_CerentGenericPmAlarmThresholdTable_Object=MibTable
cerentGenericPmAlarmThresholdTable=_CerentGenericPmAlarmThresholdTable_Object((1,3,6,1,4,1,3607,2,90,40))
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdTable.setStatus(_A)
_CerentGenericPmAlarmThresholdEntry_Object=MibTableRow
cerentGenericPmAlarmThresholdEntry=_CerentGenericPmAlarmThresholdEntry_Object((1,3,6,1,4,1,3607,2,90,40,1))
cerentGenericPmAlarmThresholdEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdEntry.setStatus(_A)
class _CerentGenericPmAlarmThresholdIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CerentGenericPmAlarmThresholdIndex_Type.__name__=_E
_CerentGenericPmAlarmThresholdIndex_Object=MibTableColumn
cerentGenericPmAlarmThresholdIndex=_CerentGenericPmAlarmThresholdIndex_Object((1,3,6,1,4,1,3607,2,90,40,1,10),_CerentGenericPmAlarmThresholdIndex_Type())
cerentGenericPmAlarmThresholdIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdIndex.setStatus(_A)
_CerentGenericPmAlarmThresholdMonitorType_Type=CerentAlarmThresholdMonitorType
_CerentGenericPmAlarmThresholdMonitorType_Object=MibTableColumn
cerentGenericPmAlarmThresholdMonitorType=_CerentGenericPmAlarmThresholdMonitorType_Object((1,3,6,1,4,1,3607,2,90,40,1,20),_CerentGenericPmAlarmThresholdMonitorType_Type())
cerentGenericPmAlarmThresholdMonitorType.setMaxAccess(_C)
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdMonitorType.setStatus(_A)
_CerentGenericPmAlarmThresholdValue_Type=Integer32
_CerentGenericPmAlarmThresholdValue_Object=MibTableColumn
cerentGenericPmAlarmThresholdValue=_CerentGenericPmAlarmThresholdValue_Object((1,3,6,1,4,1,3607,2,90,40,1,30),_CerentGenericPmAlarmThresholdValue_Type())
cerentGenericPmAlarmThresholdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdValue.setStatus(_A)
_CerentGenericPmAlarmThresholdOverFlowValue_Type=Integer32
_CerentGenericPmAlarmThresholdOverFlowValue_Object=MibTableColumn
cerentGenericPmAlarmThresholdOverFlowValue=_CerentGenericPmAlarmThresholdOverFlowValue_Object((1,3,6,1,4,1,3607,2,90,40,1,40),_CerentGenericPmAlarmThresholdOverFlowValue_Type())
cerentGenericPmAlarmThresholdOverFlowValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdOverFlowValue.setStatus(_A)
_CerentGenericPmAlarmThresholdHCValue_Type=Counter64
_CerentGenericPmAlarmThresholdHCValue_Object=MibTableColumn
cerentGenericPmAlarmThresholdHCValue=_CerentGenericPmAlarmThresholdHCValue_Object((1,3,6,1,4,1,3607,2,90,40,1,50),_CerentGenericPmAlarmThresholdHCValue_Type())
cerentGenericPmAlarmThresholdHCValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdHCValue.setStatus(_A)
_CerentGenericPmMIBConformance_ObjectIdentity=ObjectIdentity
cerentGenericPmMIBConformance=_CerentGenericPmMIBConformance_ObjectIdentity((1,3,6,1,4,1,3607,5,80))
_CerentGenericPmMIBCompliances_ObjectIdentity=ObjectIdentity
cerentGenericPmMIBCompliances=_CerentGenericPmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3607,5,80,1))
_CerentGenericPmMIBGroups_ObjectIdentity=ObjectIdentity
cerentGenericPmMIBGroups=_CerentGenericPmMIBGroups_ObjectIdentity((1,3,6,1,4,1,3607,5,80,2))
cerentGenericPmThresholdGroup=ObjectGroup((1,3,6,1,4,1,3607,5,80,2,10))
cerentGenericPmThresholdGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cerentGenericPmThresholdGroup.setStatus(_A)
cerentGenericPmStatsCurrentGroup=ObjectGroup((1,3,6,1,4,1,3607,5,80,2,20))
cerentGenericPmStatsCurrentGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:cerentGenericPmStatsCurrentGroup.setStatus(_A)
cerentGenericPmStatsIntervalGroup=ObjectGroup((1,3,6,1,4,1,3607,5,80,2,30))
cerentGenericPmStatsIntervalGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:cerentGenericPmStatsIntervalGroup.setStatus(_A)
cerentGenericPmAlarmThresholdGroup=ObjectGroup((1,3,6,1,4,1,3607,5,80,2,40))
cerentGenericPmAlarmThresholdGroup.setObjects(*((_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:cerentGenericPmAlarmThresholdGroup.setStatus(_A)
cerentGenericPmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3607,5,80,1,1))
cerentGenericPmMIBCompliance.setObjects(*((_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cerentGenericPmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cerentGenericPmMIB':cerentGenericPmMIB,'cerentGenericPmMIBObjects':cerentGenericPmMIBObjects,'cerentGenericPmThresholdTable':cerentGenericPmThresholdTable,'cerentGenericPmThresholdEntry':cerentGenericPmThresholdEntry,_F:cerentGenericPmThresholdIndex,_G:cerentGenericPmThresholdMonitorType,_H:cerentGenericPmThresholdLocation,_I:cerentGenericPmThresholdPeriod,_U:cerentGenericPmThresholdValue,_V:cerentGenericPmThresholdOverFlowValue,_W:cerentGenericPmThresholdHCValue,'cerentGenericPmStatsCurrentTable':cerentGenericPmStatsCurrentTable,'cerentGenericPmStatsCurrentEntry':cerentGenericPmStatsCurrentEntry,_J:cerentGenericPmStatsCurrentIndex,_K:cerentGenericPmStatsCurrentType,_L:cerentGenericPmStatsCurrentLocation,_M:cerentGenericPmStatsCurrentPeriod,_X:cerentGenericPmStatsCurrentValue,_Y:cerentGenericPmStatsCurrentOverFlowValue,_Z:cerentGenericPmStatsCurrentHCValue,_a:cerentGenericPmStatsCurrentValidData,_b:cerentGenericPmStatsCurrentValidIntervals,'cerentGenericPmStatsIntervalTable':cerentGenericPmStatsIntervalTable,'cerentGenericPmStatsIntervalEntry':cerentGenericPmStatsIntervalEntry,_N:cerentGenericPmStatsIntervalIndex,_O:cerentGenericPmStatsIntervalType,_P:cerentGenericPmStatsIntervalLocation,_Q:cerentGenericPmStatsIntervalPeriod,_R:cerentGenericPmStatsIntervalNumber,_c:cerentGenericPmStatsIntervalValue,_d:cerentGenericPmStatsIntervalOverFlowValue,_e:cerentGenericPmStatsIntervalHCValue,_f:cerentGenericPmStatsIntervalValidData,'cerentGenericPmAlarmThresholdTable':cerentGenericPmAlarmThresholdTable,'cerentGenericPmAlarmThresholdEntry':cerentGenericPmAlarmThresholdEntry,_S:cerentGenericPmAlarmThresholdIndex,_T:cerentGenericPmAlarmThresholdMonitorType,_g:cerentGenericPmAlarmThresholdValue,_h:cerentGenericPmAlarmThresholdOverFlowValue,_i:cerentGenericPmAlarmThresholdHCValue,'cerentGenericPmMIBConformance':cerentGenericPmMIBConformance,'cerentGenericPmMIBCompliances':cerentGenericPmMIBCompliances,'cerentGenericPmMIBCompliance':cerentGenericPmMIBCompliance,'cerentGenericPmMIBGroups':cerentGenericPmMIBGroups,_j:cerentGenericPmThresholdGroup,_k:cerentGenericPmStatsCurrentGroup,_l:cerentGenericPmStatsIntervalGroup,'cerentGenericPmAlarmThresholdGroup':cerentGenericPmAlarmThresholdGroup})