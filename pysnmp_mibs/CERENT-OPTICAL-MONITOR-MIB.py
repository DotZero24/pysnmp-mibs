_j='cerentOpticalMIBPMGroup'
_i='cerentOpticalMIBThresholdGroup'
_h='cerentOpticalMIBMonGroup'
_g='cOpticalParamHighDegradeThresh'
_f='cOpticalParamLowDegradeThresh'
_e='cOpticalPMIntervalValidData'
_d='cOpticalPMIntervalMeanParam'
_c='cOpticalPMIntervalMinParam'
_b='cOpticalPMIntervalMaxParam'
_a='cOpticalPMCurrentMeanParam'
_Z='cOpticalPMCurrentMinParam'
_Y='cOpticalPMCurrentMaxParam'
_X='cOpticalParameterValue'
_W='cOpticalPMIntervalNumber'
_V='cOpticalPMIntervalPeriod'
_U='cOpticalPMIntervalParamType'
_T='cOpticalPMIntervalDirection'
_S='cOpticalPMCurrentPeriod'
_R='cOpticalPMCurrentParamType'
_Q='cOpticalPMCurrentDirection'
_P='cOpticalMonParameterType'
_O='cOpticalMonDirection'
_N='Integer32'
_M='cOpticalParamLowWarning1DayThresh'
_L='cOpticalParamLowWarning15MinThresh'
_K='cOpticalParamLowAlarmThresh'
_J='cOpticalParamHighWarning1DayThresh'
_I='cOpticalParamHighWarning15MinThresh'
_H='cOpticalParamHighAlarmThresh'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='read-only'
_C='not-accessible'
_B='CERENT-OPTICAL-MONITOR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cerentGeneric,cerentModules,cerentRequirements=mibBuilder.importSymbols('CERENT-GLOBAL-REGISTRY','cerentGeneric','cerentModules','cerentRequirements')
CerentPeriod,=mibBuilder.importSymbols('CERENT-TC','CerentPeriod')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cerentOpticalMonitorMIB=ModuleIdentity((1,3,6,1,4,1,3607,1,10,70))
if mibBuilder.loadTexts:cerentOpticalMonitorMIB.setRevisions(('1902-11-11 00:00',))
class OpticalParameterType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('power',1),('acPower',2),('apdTemp',3),('laserTemp',4),('biasCurrent',5),('peltierCurrent',6),('xcvrVoltage',7),('voa',8),('gain',9),('oscPower',10),('addPower',11)))
class OpticalParameterValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000,1000000))
class OpticalIfDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('receive',1),('transmit',2),('notApplicable',3)))
_CerentOpticalMonitorMIBObjects_ObjectIdentity=ObjectIdentity
cerentOpticalMonitorMIBObjects=_CerentOpticalMonitorMIBObjects_ObjectIdentity((1,3,6,1,4,1,3607,2,30))
_CerentOpticalMonGroup_ObjectIdentity=ObjectIdentity
cerentOpticalMonGroup=_CerentOpticalMonGroup_ObjectIdentity((1,3,6,1,4,1,3607,2,30,1))
_COpticalMonTable_Object=MibTable
cOpticalMonTable=_COpticalMonTable_Object((1,3,6,1,4,1,3607,2,30,1,1))
if mibBuilder.loadTexts:cOpticalMonTable.setStatus(_A)
_COpticalMonEntry_Object=MibTableRow
cOpticalMonEntry=_COpticalMonEntry_Object((1,3,6,1,4,1,3607,2,30,1,1,1))
cOpticalMonEntry.setIndexNames((0,_F,_G),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:cOpticalMonEntry.setStatus(_A)
_COpticalMonDirection_Type=OpticalIfDirection
_COpticalMonDirection_Object=MibTableColumn
cOpticalMonDirection=_COpticalMonDirection_Object((1,3,6,1,4,1,3607,2,30,1,1,1,1),_COpticalMonDirection_Type())
cOpticalMonDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalMonDirection.setStatus(_A)
_COpticalMonParameterType_Type=OpticalParameterType
_COpticalMonParameterType_Object=MibTableColumn
cOpticalMonParameterType=_COpticalMonParameterType_Object((1,3,6,1,4,1,3607,2,30,1,1,1,2),_COpticalMonParameterType_Type())
cOpticalMonParameterType.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalMonParameterType.setStatus(_A)
_COpticalParameterValue_Type=OpticalParameterValue
_COpticalParameterValue_Object=MibTableColumn
cOpticalParameterValue=_COpticalParameterValue_Object((1,3,6,1,4,1,3607,2,30,1,1,1,3),_COpticalParameterValue_Type())
cOpticalParameterValue.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalParameterValue.setStatus(_A)
_COpticalParamHighAlarmThresh_Type=OpticalParameterValue
_COpticalParamHighAlarmThresh_Object=MibTableColumn
cOpticalParamHighAlarmThresh=_COpticalParamHighAlarmThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,4),_COpticalParamHighAlarmThresh_Type())
cOpticalParamHighAlarmThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighAlarmThresh.setStatus(_A)
_COpticalParamHighWarning15MinThresh_Type=OpticalParameterValue
_COpticalParamHighWarning15MinThresh_Object=MibTableColumn
cOpticalParamHighWarning15MinThresh=_COpticalParamHighWarning15MinThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,5),_COpticalParamHighWarning15MinThresh_Type())
cOpticalParamHighWarning15MinThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighWarning15MinThresh.setStatus(_A)
_COpticalParamHighWarning1DayThresh_Type=OpticalParameterValue
_COpticalParamHighWarning1DayThresh_Object=MibTableColumn
cOpticalParamHighWarning1DayThresh=_COpticalParamHighWarning1DayThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,6),_COpticalParamHighWarning1DayThresh_Type())
cOpticalParamHighWarning1DayThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighWarning1DayThresh.setStatus(_A)
_COpticalParamLowAlarmThresh_Type=OpticalParameterValue
_COpticalParamLowAlarmThresh_Object=MibTableColumn
cOpticalParamLowAlarmThresh=_COpticalParamLowAlarmThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,7),_COpticalParamLowAlarmThresh_Type())
cOpticalParamLowAlarmThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowAlarmThresh.setStatus(_A)
_COpticalParamLowWarning15MinThresh_Type=OpticalParameterValue
_COpticalParamLowWarning15MinThresh_Object=MibTableColumn
cOpticalParamLowWarning15MinThresh=_COpticalParamLowWarning15MinThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,8),_COpticalParamLowWarning15MinThresh_Type())
cOpticalParamLowWarning15MinThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowWarning15MinThresh.setStatus(_A)
_COpticalParamLowWarning1DayThresh_Type=OpticalParameterValue
_COpticalParamLowWarning1DayThresh_Object=MibTableColumn
cOpticalParamLowWarning1DayThresh=_COpticalParamLowWarning1DayThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,9),_COpticalParamLowWarning1DayThresh_Type())
cOpticalParamLowWarning1DayThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowWarning1DayThresh.setStatus(_A)
_COpticalParamLowDegradeThresh_Type=OpticalParameterValue
_COpticalParamLowDegradeThresh_Object=MibTableColumn
cOpticalParamLowDegradeThresh=_COpticalParamLowDegradeThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,10),_COpticalParamLowDegradeThresh_Type())
cOpticalParamLowDegradeThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamLowDegradeThresh.setStatus(_A)
_COpticalParamHighDegradeThresh_Type=OpticalParameterValue
_COpticalParamHighDegradeThresh_Object=MibTableColumn
cOpticalParamHighDegradeThresh=_COpticalParamHighDegradeThresh_Object((1,3,6,1,4,1,3607,2,30,1,1,1,11),_COpticalParamHighDegradeThresh_Type())
cOpticalParamHighDegradeThresh.setMaxAccess(_E)
if mibBuilder.loadTexts:cOpticalParamHighDegradeThresh.setStatus(_A)
_CerentOpticalPMGroup_ObjectIdentity=ObjectIdentity
cerentOpticalPMGroup=_CerentOpticalPMGroup_ObjectIdentity((1,3,6,1,4,1,3607,2,30,2))
_COpticalPMCurrentTable_Object=MibTable
cOpticalPMCurrentTable=_COpticalPMCurrentTable_Object((1,3,6,1,4,1,3607,2,30,2,1))
if mibBuilder.loadTexts:cOpticalPMCurrentTable.setStatus(_A)
_COpticalPMCurrentEntry_Object=MibTableRow
cOpticalPMCurrentEntry=_COpticalPMCurrentEntry_Object((1,3,6,1,4,1,3607,2,30,2,1,1))
cOpticalPMCurrentEntry.setIndexNames((0,_F,_G),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:cOpticalPMCurrentEntry.setStatus(_A)
_COpticalPMCurrentDirection_Type=OpticalIfDirection
_COpticalPMCurrentDirection_Object=MibTableColumn
cOpticalPMCurrentDirection=_COpticalPMCurrentDirection_Object((1,3,6,1,4,1,3607,2,30,2,1,1,1),_COpticalPMCurrentDirection_Type())
cOpticalPMCurrentDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMCurrentDirection.setStatus(_A)
_COpticalPMCurrentParamType_Type=OpticalParameterType
_COpticalPMCurrentParamType_Object=MibTableColumn
cOpticalPMCurrentParamType=_COpticalPMCurrentParamType_Object((1,3,6,1,4,1,3607,2,30,2,1,1,2),_COpticalPMCurrentParamType_Type())
cOpticalPMCurrentParamType.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMCurrentParamType.setStatus(_A)
_COpticalPMCurrentPeriod_Type=CerentPeriod
_COpticalPMCurrentPeriod_Object=MibTableColumn
cOpticalPMCurrentPeriod=_COpticalPMCurrentPeriod_Object((1,3,6,1,4,1,3607,2,30,2,1,1,3),_COpticalPMCurrentPeriod_Type())
cOpticalPMCurrentPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMCurrentPeriod.setStatus(_A)
_COpticalPMCurrentMaxParam_Type=OpticalParameterValue
_COpticalPMCurrentMaxParam_Object=MibTableColumn
cOpticalPMCurrentMaxParam=_COpticalPMCurrentMaxParam_Object((1,3,6,1,4,1,3607,2,30,2,1,1,4),_COpticalPMCurrentMaxParam_Type())
cOpticalPMCurrentMaxParam.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMCurrentMaxParam.setStatus(_A)
_COpticalPMCurrentMinParam_Type=OpticalParameterValue
_COpticalPMCurrentMinParam_Object=MibTableColumn
cOpticalPMCurrentMinParam=_COpticalPMCurrentMinParam_Object((1,3,6,1,4,1,3607,2,30,2,1,1,5),_COpticalPMCurrentMinParam_Type())
cOpticalPMCurrentMinParam.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMCurrentMinParam.setStatus(_A)
_COpticalPMCurrentMeanParam_Type=OpticalParameterValue
_COpticalPMCurrentMeanParam_Object=MibTableColumn
cOpticalPMCurrentMeanParam=_COpticalPMCurrentMeanParam_Object((1,3,6,1,4,1,3607,2,30,2,1,1,6),_COpticalPMCurrentMeanParam_Type())
cOpticalPMCurrentMeanParam.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMCurrentMeanParam.setStatus(_A)
_COpticalPMIntervalTable_Object=MibTable
cOpticalPMIntervalTable=_COpticalPMIntervalTable_Object((1,3,6,1,4,1,3607,2,30,2,2))
if mibBuilder.loadTexts:cOpticalPMIntervalTable.setStatus(_A)
_COpticalPMIntervalEntry_Object=MibTableRow
cOpticalPMIntervalEntry=_COpticalPMIntervalEntry_Object((1,3,6,1,4,1,3607,2,30,2,2,1))
cOpticalPMIntervalEntry.setIndexNames((0,_F,_G),(0,_B,_T),(0,_B,_U),(0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:cOpticalPMIntervalEntry.setStatus(_A)
_COpticalPMIntervalDirection_Type=OpticalIfDirection
_COpticalPMIntervalDirection_Object=MibTableColumn
cOpticalPMIntervalDirection=_COpticalPMIntervalDirection_Object((1,3,6,1,4,1,3607,2,30,2,2,1,1),_COpticalPMIntervalDirection_Type())
cOpticalPMIntervalDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalDirection.setStatus(_A)
_COpticalPMIntervalParamType_Type=OpticalParameterType
_COpticalPMIntervalParamType_Object=MibTableColumn
cOpticalPMIntervalParamType=_COpticalPMIntervalParamType_Object((1,3,6,1,4,1,3607,2,30,2,2,1,2),_COpticalPMIntervalParamType_Type())
cOpticalPMIntervalParamType.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalParamType.setStatus(_A)
_COpticalPMIntervalPeriod_Type=CerentPeriod
_COpticalPMIntervalPeriod_Object=MibTableColumn
cOpticalPMIntervalPeriod=_COpticalPMIntervalPeriod_Object((1,3,6,1,4,1,3607,2,30,2,2,1,3),_COpticalPMIntervalPeriod_Type())
cOpticalPMIntervalPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalPeriod.setStatus(_A)
class _COpticalPMIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_COpticalPMIntervalNumber_Type.__name__=_N
_COpticalPMIntervalNumber_Object=MibTableColumn
cOpticalPMIntervalNumber=_COpticalPMIntervalNumber_Object((1,3,6,1,4,1,3607,2,30,2,2,1,4),_COpticalPMIntervalNumber_Type())
cOpticalPMIntervalNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cOpticalPMIntervalNumber.setStatus(_A)
_COpticalPMIntervalMaxParam_Type=OpticalParameterValue
_COpticalPMIntervalMaxParam_Object=MibTableColumn
cOpticalPMIntervalMaxParam=_COpticalPMIntervalMaxParam_Object((1,3,6,1,4,1,3607,2,30,2,2,1,5),_COpticalPMIntervalMaxParam_Type())
cOpticalPMIntervalMaxParam.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalMaxParam.setStatus(_A)
_COpticalPMIntervalMinParam_Type=OpticalParameterValue
_COpticalPMIntervalMinParam_Object=MibTableColumn
cOpticalPMIntervalMinParam=_COpticalPMIntervalMinParam_Object((1,3,6,1,4,1,3607,2,30,2,2,1,6),_COpticalPMIntervalMinParam_Type())
cOpticalPMIntervalMinParam.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalMinParam.setStatus(_A)
_COpticalPMIntervalMeanParam_Type=OpticalParameterValue
_COpticalPMIntervalMeanParam_Object=MibTableColumn
cOpticalPMIntervalMeanParam=_COpticalPMIntervalMeanParam_Object((1,3,6,1,4,1,3607,2,30,2,2,1,7),_COpticalPMIntervalMeanParam_Type())
cOpticalPMIntervalMeanParam.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalMeanParam.setStatus(_A)
_COpticalPMIntervalValidData_Type=TruthValue
_COpticalPMIntervalValidData_Object=MibTableColumn
cOpticalPMIntervalValidData=_COpticalPMIntervalValidData_Object((1,3,6,1,4,1,3607,2,30,2,2,1,8),_COpticalPMIntervalValidData_Type())
cOpticalPMIntervalValidData.setMaxAccess(_D)
if mibBuilder.loadTexts:cOpticalPMIntervalValidData.setStatus(_A)
_CerentOpticalMonitorMIBConformance_ObjectIdentity=ObjectIdentity
cerentOpticalMonitorMIBConformance=_CerentOpticalMonitorMIBConformance_ObjectIdentity((1,3,6,1,4,1,3607,5,20))
_CerentOpticalMonitorMIBCompliances_ObjectIdentity=ObjectIdentity
cerentOpticalMonitorMIBCompliances=_CerentOpticalMonitorMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3607,5,20,1))
_CerentOpticalMonitorMIBGroups_ObjectIdentity=ObjectIdentity
cerentOpticalMonitorMIBGroups=_CerentOpticalMonitorMIBGroups_ObjectIdentity((1,3,6,1,4,1,3607,5,20,2))
cerentOpticalMIBMonGroup=ObjectGroup((1,3,6,1,4,1,3607,5,20,2,1))
cerentOpticalMIBMonGroup.setObjects((_B,_X))
if mibBuilder.loadTexts:cerentOpticalMIBMonGroup.setStatus(_A)
cerentOpticalMIBThresholdGroup=ObjectGroup((1,3,6,1,4,1,3607,5,20,2,2))
cerentOpticalMIBThresholdGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:cerentOpticalMIBThresholdGroup.setStatus(_A)
cerentOpticalMIBPMGroup=ObjectGroup((1,3,6,1,4,1,3607,5,20,2,3))
cerentOpticalMIBPMGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cerentOpticalMIBPMGroup.setStatus(_A)
cerentOpticalDwdmNetworkMIBThresholdGroup=ObjectGroup((1,3,6,1,4,1,3607,5,20,2,4))
cerentOpticalDwdmNetworkMIBThresholdGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:cerentOpticalDwdmNetworkMIBThresholdGroup.setStatus(_A)
cerentOpticalMonitorMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3607,5,20,1,1))
cerentOpticalMonitorMIBCompliance.setObjects(*((_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:cerentOpticalMonitorMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'OpticalParameterType':OpticalParameterType,'OpticalParameterValue':OpticalParameterValue,'OpticalIfDirection':OpticalIfDirection,'cerentOpticalMonitorMIB':cerentOpticalMonitorMIB,'cerentOpticalMonitorMIBObjects':cerentOpticalMonitorMIBObjects,'cerentOpticalMonGroup':cerentOpticalMonGroup,'cOpticalMonTable':cOpticalMonTable,'cOpticalMonEntry':cOpticalMonEntry,_O:cOpticalMonDirection,_P:cOpticalMonParameterType,_X:cOpticalParameterValue,_H:cOpticalParamHighAlarmThresh,_I:cOpticalParamHighWarning15MinThresh,_J:cOpticalParamHighWarning1DayThresh,_K:cOpticalParamLowAlarmThresh,_L:cOpticalParamLowWarning15MinThresh,_M:cOpticalParamLowWarning1DayThresh,_f:cOpticalParamLowDegradeThresh,_g:cOpticalParamHighDegradeThresh,'cerentOpticalPMGroup':cerentOpticalPMGroup,'cOpticalPMCurrentTable':cOpticalPMCurrentTable,'cOpticalPMCurrentEntry':cOpticalPMCurrentEntry,_Q:cOpticalPMCurrentDirection,_R:cOpticalPMCurrentParamType,_S:cOpticalPMCurrentPeriod,_Y:cOpticalPMCurrentMaxParam,_Z:cOpticalPMCurrentMinParam,_a:cOpticalPMCurrentMeanParam,'cOpticalPMIntervalTable':cOpticalPMIntervalTable,'cOpticalPMIntervalEntry':cOpticalPMIntervalEntry,_T:cOpticalPMIntervalDirection,_U:cOpticalPMIntervalParamType,_V:cOpticalPMIntervalPeriod,_W:cOpticalPMIntervalNumber,_b:cOpticalPMIntervalMaxParam,_c:cOpticalPMIntervalMinParam,_d:cOpticalPMIntervalMeanParam,_e:cOpticalPMIntervalValidData,'cerentOpticalMonitorMIBConformance':cerentOpticalMonitorMIBConformance,'cerentOpticalMonitorMIBCompliances':cerentOpticalMonitorMIBCompliances,'cerentOpticalMonitorMIBCompliance':cerentOpticalMonitorMIBCompliance,'cerentOpticalMonitorMIBGroups':cerentOpticalMonitorMIBGroups,_h:cerentOpticalMIBMonGroup,_i:cerentOpticalMIBThresholdGroup,_j:cerentOpticalMIBPMGroup,'cerentOpticalDwdmNetworkMIBThresholdGroup':cerentOpticalDwdmNetworkMIBThresholdGroup})