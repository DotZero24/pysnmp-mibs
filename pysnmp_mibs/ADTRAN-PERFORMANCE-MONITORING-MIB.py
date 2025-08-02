_O='read-write'
_N='adGenPmStatsAttribute'
_M='adGenPm24HrIntervalStatsInterval'
_L='adGenPm24HrIntervalStatsAttribute'
_K='adGenPm24HrCurrentStatsAttribute'
_J='adGenPm15MinIntervalStatsInterval'
_I='adGenPm15MinIntervalStatsAttribute'
_H='adGenPm15MinCurrentIntervalStatsAttribute'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='ADTRAN-PERFORMANCE-MONITORING-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPerformanceMonitoring,adGenPerformanceMonitoringID=mibBuilder.importSymbols('ADTRAN-SHARED-CND-SYSTEM-MIB','adGenPerformanceMonitoring','adGenPerformanceMonitoringID')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_E,'InterfaceIndex',_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
adGenPerformanceMonitoringMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,70,23,1))
if mibBuilder.loadTexts:adGenPerformanceMonitoringMIB.setRevisions(('2012-02-06 00:00','2010-03-31 00:00'))
class AdGenPmAttributeName(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class AdGenPmFunctionName(TextualConvention,OctetString):status=_A;displayHint='32a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AdGenPmStats_ObjectIdentity=ObjectIdentity
adGenPmStats=_AdGenPmStats_ObjectIdentity((1,3,6,1,4,1,664,5,70,23,1))
_AdGenPm15MinCurrentIntervalStatsTable_Object=MibTable
adGenPm15MinCurrentIntervalStatsTable=_AdGenPm15MinCurrentIntervalStatsTable_Object((1,3,6,1,4,1,664,5,70,23,1,1))
if mibBuilder.loadTexts:adGenPm15MinCurrentIntervalStatsTable.setStatus(_A)
_AdGenPm15MinCurrentIntervalStatsEntry_Object=MibTableRow
adGenPm15MinCurrentIntervalStatsEntry=_AdGenPm15MinCurrentIntervalStatsEntry_Object((1,3,6,1,4,1,664,5,70,23,1,1,1))
adGenPm15MinCurrentIntervalStatsEntry.setIndexNames((0,_E,_F),(0,_C,_H))
if mibBuilder.loadTexts:adGenPm15MinCurrentIntervalStatsEntry.setStatus(_A)
_AdGenPm15MinCurrentIntervalStatsAttribute_Type=AdGenPmAttributeName
_AdGenPm15MinCurrentIntervalStatsAttribute_Object=MibTableColumn
adGenPm15MinCurrentIntervalStatsAttribute=_AdGenPm15MinCurrentIntervalStatsAttribute_Object((1,3,6,1,4,1,664,5,70,23,1,1,1,1),_AdGenPm15MinCurrentIntervalStatsAttribute_Type())
adGenPm15MinCurrentIntervalStatsAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPm15MinCurrentIntervalStatsAttribute.setStatus(_A)
_AdGenPm15MinCurrentIntervalStatsValue_Type=Counter32
_AdGenPm15MinCurrentIntervalStatsValue_Object=MibTableColumn
adGenPm15MinCurrentIntervalStatsValue=_AdGenPm15MinCurrentIntervalStatsValue_Object((1,3,6,1,4,1,664,5,70,23,1,1,1,2),_AdGenPm15MinCurrentIntervalStatsValue_Type())
adGenPm15MinCurrentIntervalStatsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm15MinCurrentIntervalStatsValue.setStatus(_A)
_AdGenPm15MinCurrentIntervalStatsHCValue_Type=Counter64
_AdGenPm15MinCurrentIntervalStatsHCValue_Object=MibTableColumn
adGenPm15MinCurrentIntervalStatsHCValue=_AdGenPm15MinCurrentIntervalStatsHCValue_Object((1,3,6,1,4,1,664,5,70,23,1,1,1,3),_AdGenPm15MinCurrentIntervalStatsHCValue_Type())
adGenPm15MinCurrentIntervalStatsHCValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm15MinCurrentIntervalStatsHCValue.setStatus(_A)
_AdGenPm15MinCurrentIntervalStatsValid_Type=TruthValue
_AdGenPm15MinCurrentIntervalStatsValid_Object=MibTableColumn
adGenPm15MinCurrentIntervalStatsValid=_AdGenPm15MinCurrentIntervalStatsValid_Object((1,3,6,1,4,1,664,5,70,23,1,1,1,4),_AdGenPm15MinCurrentIntervalStatsValid_Type())
adGenPm15MinCurrentIntervalStatsValid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm15MinCurrentIntervalStatsValid.setStatus(_A)
_AdGenPm15MinIntervalStatsTable_Object=MibTable
adGenPm15MinIntervalStatsTable=_AdGenPm15MinIntervalStatsTable_Object((1,3,6,1,4,1,664,5,70,23,1,2))
if mibBuilder.loadTexts:adGenPm15MinIntervalStatsTable.setStatus(_A)
_AdGenPm15MinIntervalStatsEntry_Object=MibTableRow
adGenPm15MinIntervalStatsEntry=_AdGenPm15MinIntervalStatsEntry_Object((1,3,6,1,4,1,664,5,70,23,1,2,1))
adGenPm15MinIntervalStatsEntry.setIndexNames((0,_E,_F),(0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:adGenPm15MinIntervalStatsEntry.setStatus(_A)
class _AdGenPm15MinIntervalStatsInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,96))
_AdGenPm15MinIntervalStatsInterval_Type.__name__=_G
_AdGenPm15MinIntervalStatsInterval_Object=MibTableColumn
adGenPm15MinIntervalStatsInterval=_AdGenPm15MinIntervalStatsInterval_Object((1,3,6,1,4,1,664,5,70,23,1,2,1,1),_AdGenPm15MinIntervalStatsInterval_Type())
adGenPm15MinIntervalStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPm15MinIntervalStatsInterval.setStatus(_A)
_AdGenPm15MinIntervalStatsAttribute_Type=AdGenPmAttributeName
_AdGenPm15MinIntervalStatsAttribute_Object=MibTableColumn
adGenPm15MinIntervalStatsAttribute=_AdGenPm15MinIntervalStatsAttribute_Object((1,3,6,1,4,1,664,5,70,23,1,2,1,2),_AdGenPm15MinIntervalStatsAttribute_Type())
adGenPm15MinIntervalStatsAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPm15MinIntervalStatsAttribute.setStatus(_A)
_AdGenPm15MinIntervalStatsValue_Type=Counter32
_AdGenPm15MinIntervalStatsValue_Object=MibTableColumn
adGenPm15MinIntervalStatsValue=_AdGenPm15MinIntervalStatsValue_Object((1,3,6,1,4,1,664,5,70,23,1,2,1,3),_AdGenPm15MinIntervalStatsValue_Type())
adGenPm15MinIntervalStatsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm15MinIntervalStatsValue.setStatus(_A)
_AdGenPm15MinIntervalStatsHCValue_Type=Counter64
_AdGenPm15MinIntervalStatsHCValue_Object=MibTableColumn
adGenPm15MinIntervalStatsHCValue=_AdGenPm15MinIntervalStatsHCValue_Object((1,3,6,1,4,1,664,5,70,23,1,2,1,4),_AdGenPm15MinIntervalStatsHCValue_Type())
adGenPm15MinIntervalStatsHCValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm15MinIntervalStatsHCValue.setStatus(_A)
_AdGenPm15MinIntervalStatsValid_Type=TruthValue
_AdGenPm15MinIntervalStatsValid_Object=MibTableColumn
adGenPm15MinIntervalStatsValid=_AdGenPm15MinIntervalStatsValid_Object((1,3,6,1,4,1,664,5,70,23,1,2,1,5),_AdGenPm15MinIntervalStatsValid_Type())
adGenPm15MinIntervalStatsValid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm15MinIntervalStatsValid.setStatus(_A)
_AdGenPm24HrCurrentStatsTable_Object=MibTable
adGenPm24HrCurrentStatsTable=_AdGenPm24HrCurrentStatsTable_Object((1,3,6,1,4,1,664,5,70,23,1,3))
if mibBuilder.loadTexts:adGenPm24HrCurrentStatsTable.setStatus(_A)
_AdGenPm24HrCurrentStatsEntry_Object=MibTableRow
adGenPm24HrCurrentStatsEntry=_AdGenPm24HrCurrentStatsEntry_Object((1,3,6,1,4,1,664,5,70,23,1,3,1))
adGenPm24HrCurrentStatsEntry.setIndexNames((0,_E,_F),(0,_C,_K))
if mibBuilder.loadTexts:adGenPm24HrCurrentStatsEntry.setStatus(_A)
_AdGenPm24HrCurrentStatsAttribute_Type=AdGenPmAttributeName
_AdGenPm24HrCurrentStatsAttribute_Object=MibTableColumn
adGenPm24HrCurrentStatsAttribute=_AdGenPm24HrCurrentStatsAttribute_Object((1,3,6,1,4,1,664,5,70,23,1,3,1,1),_AdGenPm24HrCurrentStatsAttribute_Type())
adGenPm24HrCurrentStatsAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPm24HrCurrentStatsAttribute.setStatus(_A)
_AdGenPm24HrCurrentStatsValue_Type=Counter32
_AdGenPm24HrCurrentStatsValue_Object=MibTableColumn
adGenPm24HrCurrentStatsValue=_AdGenPm24HrCurrentStatsValue_Object((1,3,6,1,4,1,664,5,70,23,1,3,1,2),_AdGenPm24HrCurrentStatsValue_Type())
adGenPm24HrCurrentStatsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm24HrCurrentStatsValue.setStatus(_A)
_AdGenPm24HrCurrentStatsHCValue_Type=Counter64
_AdGenPm24HrCurrentStatsHCValue_Object=MibTableColumn
adGenPm24HrCurrentStatsHCValue=_AdGenPm24HrCurrentStatsHCValue_Object((1,3,6,1,4,1,664,5,70,23,1,3,1,3),_AdGenPm24HrCurrentStatsHCValue_Type())
adGenPm24HrCurrentStatsHCValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm24HrCurrentStatsHCValue.setStatus(_A)
_AdGenPm24HrCurrentStatsValid_Type=TruthValue
_AdGenPm24HrCurrentStatsValid_Object=MibTableColumn
adGenPm24HrCurrentStatsValid=_AdGenPm24HrCurrentStatsValid_Object((1,3,6,1,4,1,664,5,70,23,1,3,1,4),_AdGenPm24HrCurrentStatsValid_Type())
adGenPm24HrCurrentStatsValid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm24HrCurrentStatsValid.setStatus(_A)
_AdGenPm24HrIntervalStatsTable_Object=MibTable
adGenPm24HrIntervalStatsTable=_AdGenPm24HrIntervalStatsTable_Object((1,3,6,1,4,1,664,5,70,23,1,4))
if mibBuilder.loadTexts:adGenPm24HrIntervalStatsTable.setStatus(_A)
_AdGenPm24HrIntervalStatsEntry_Object=MibTableRow
adGenPm24HrIntervalStatsEntry=_AdGenPm24HrIntervalStatsEntry_Object((1,3,6,1,4,1,664,5,70,23,1,4,1))
adGenPm24HrIntervalStatsEntry.setIndexNames((0,_E,_F),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:adGenPm24HrIntervalStatsEntry.setStatus(_A)
_AdGenPm24HrIntervalStatsAttribute_Type=AdGenPmAttributeName
_AdGenPm24HrIntervalStatsAttribute_Object=MibTableColumn
adGenPm24HrIntervalStatsAttribute=_AdGenPm24HrIntervalStatsAttribute_Object((1,3,6,1,4,1,664,5,70,23,1,4,1,1),_AdGenPm24HrIntervalStatsAttribute_Type())
adGenPm24HrIntervalStatsAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPm24HrIntervalStatsAttribute.setStatus(_A)
class _AdGenPm24HrIntervalStatsInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_AdGenPm24HrIntervalStatsInterval_Type.__name__=_G
_AdGenPm24HrIntervalStatsInterval_Object=MibTableColumn
adGenPm24HrIntervalStatsInterval=_AdGenPm24HrIntervalStatsInterval_Object((1,3,6,1,4,1,664,5,70,23,1,4,1,2),_AdGenPm24HrIntervalStatsInterval_Type())
adGenPm24HrIntervalStatsInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPm24HrIntervalStatsInterval.setStatus(_A)
_AdGenPm24HrIntervalStatsValue_Type=Counter32
_AdGenPm24HrIntervalStatsValue_Object=MibTableColumn
adGenPm24HrIntervalStatsValue=_AdGenPm24HrIntervalStatsValue_Object((1,3,6,1,4,1,664,5,70,23,1,4,1,3),_AdGenPm24HrIntervalStatsValue_Type())
adGenPm24HrIntervalStatsValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm24HrIntervalStatsValue.setStatus(_A)
_AdGenPm24HrIntervalStatsHCValue_Type=Counter64
_AdGenPm24HrIntervalStatsHCValue_Object=MibTableColumn
adGenPm24HrIntervalStatsHCValue=_AdGenPm24HrIntervalStatsHCValue_Object((1,3,6,1,4,1,664,5,70,23,1,4,1,4),_AdGenPm24HrIntervalStatsHCValue_Type())
adGenPm24HrIntervalStatsHCValue.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm24HrIntervalStatsHCValue.setStatus(_A)
_AdGenPm24HrIntervalStatsValid_Type=TruthValue
_AdGenPm24HrIntervalStatsValid_Object=MibTableColumn
adGenPm24HrIntervalStatsValid=_AdGenPm24HrIntervalStatsValid_Object((1,3,6,1,4,1,664,5,70,23,1,4,1,5),_AdGenPm24HrIntervalStatsValid_Type())
adGenPm24HrIntervalStatsValid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenPm24HrIntervalStatsValid.setStatus(_A)
_AdGenPmProvisioning_ObjectIdentity=ObjectIdentity
adGenPmProvisioning=_AdGenPmProvisioning_ObjectIdentity((1,3,6,1,4,1,664,5,70,23,2))
_AdGenPmStatsResetTable_Object=MibTable
adGenPmStatsResetTable=_AdGenPmStatsResetTable_Object((1,3,6,1,4,1,664,5,70,23,2,1))
if mibBuilder.loadTexts:adGenPmStatsResetTable.setStatus(_A)
_AdGenPmStatsResetEntry_Object=MibTableRow
adGenPmStatsResetEntry=_AdGenPmStatsResetEntry_Object((1,3,6,1,4,1,664,5,70,23,2,1,1))
adGenPmStatsResetEntry.setIndexNames((0,_E,_F),(0,_C,_N))
if mibBuilder.loadTexts:adGenPmStatsResetEntry.setStatus(_A)
_AdGenPmStatsAttribute_Type=AdGenPmAttributeName
_AdGenPmStatsAttribute_Object=MibTableColumn
adGenPmStatsAttribute=_AdGenPmStatsAttribute_Object((1,3,6,1,4,1,664,5,70,23,2,1,1,1),_AdGenPmStatsAttribute_Type())
adGenPmStatsAttribute.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenPmStatsAttribute.setStatus(_A)
_AdGenPmStats15MinReset_Type=Integer32
_AdGenPmStats15MinReset_Object=MibTableColumn
adGenPmStats15MinReset=_AdGenPmStats15MinReset_Object((1,3,6,1,4,1,664,5,70,23,2,1,1,2),_AdGenPmStats15MinReset_Type())
adGenPmStats15MinReset.setMaxAccess(_O)
if mibBuilder.loadTexts:adGenPmStats15MinReset.setStatus(_A)
_AdGenPmStats24HrReset_Type=Integer32
_AdGenPmStats24HrReset_Object=MibTableColumn
adGenPmStats24HrReset=_AdGenPmStats24HrReset_Object((1,3,6,1,4,1,664,5,70,23,2,1,1,3),_AdGenPmStats24HrReset_Type())
adGenPmStats24HrReset.setMaxAccess(_O)
if mibBuilder.loadTexts:adGenPmStats24HrReset.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'AdGenPmAttributeName':AdGenPmAttributeName,'AdGenPmFunctionName':AdGenPmFunctionName,'adGenPmStats':adGenPmStats,'adGenPm15MinCurrentIntervalStatsTable':adGenPm15MinCurrentIntervalStatsTable,'adGenPm15MinCurrentIntervalStatsEntry':adGenPm15MinCurrentIntervalStatsEntry,_H:adGenPm15MinCurrentIntervalStatsAttribute,'adGenPm15MinCurrentIntervalStatsValue':adGenPm15MinCurrentIntervalStatsValue,'adGenPm15MinCurrentIntervalStatsHCValue':adGenPm15MinCurrentIntervalStatsHCValue,'adGenPm15MinCurrentIntervalStatsValid':adGenPm15MinCurrentIntervalStatsValid,'adGenPm15MinIntervalStatsTable':adGenPm15MinIntervalStatsTable,'adGenPm15MinIntervalStatsEntry':adGenPm15MinIntervalStatsEntry,_J:adGenPm15MinIntervalStatsInterval,_I:adGenPm15MinIntervalStatsAttribute,'adGenPm15MinIntervalStatsValue':adGenPm15MinIntervalStatsValue,'adGenPm15MinIntervalStatsHCValue':adGenPm15MinIntervalStatsHCValue,'adGenPm15MinIntervalStatsValid':adGenPm15MinIntervalStatsValid,'adGenPm24HrCurrentStatsTable':adGenPm24HrCurrentStatsTable,'adGenPm24HrCurrentStatsEntry':adGenPm24HrCurrentStatsEntry,_K:adGenPm24HrCurrentStatsAttribute,'adGenPm24HrCurrentStatsValue':adGenPm24HrCurrentStatsValue,'adGenPm24HrCurrentStatsHCValue':adGenPm24HrCurrentStatsHCValue,'adGenPm24HrCurrentStatsValid':adGenPm24HrCurrentStatsValid,'adGenPm24HrIntervalStatsTable':adGenPm24HrIntervalStatsTable,'adGenPm24HrIntervalStatsEntry':adGenPm24HrIntervalStatsEntry,_L:adGenPm24HrIntervalStatsAttribute,_M:adGenPm24HrIntervalStatsInterval,'adGenPm24HrIntervalStatsValue':adGenPm24HrIntervalStatsValue,'adGenPm24HrIntervalStatsHCValue':adGenPm24HrIntervalStatsHCValue,'adGenPm24HrIntervalStatsValid':adGenPm24HrIntervalStatsValid,'adGenPmProvisioning':adGenPmProvisioning,'adGenPmStatsResetTable':adGenPmStatsResetTable,'adGenPmStatsResetEntry':adGenPmStatsResetEntry,_N:adGenPmStatsAttribute,'adGenPmStats15MinReset':adGenPmStats15MinReset,'adGenPmStats24HrReset':adGenPmStats24HrReset,'adGenPerformanceMonitoringMIB':adGenPerformanceMonitoringMIB})