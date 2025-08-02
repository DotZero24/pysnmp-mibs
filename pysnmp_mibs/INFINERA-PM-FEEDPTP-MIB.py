_T='feedPtpPmRealGroup'
_S='feedPtpPmGroup'
_R='feedPtpPmRealInputCurrent'
_Q='feedPtpPmRealInputVoltage'
_P='feedPtpPmInputCurrentAve'
_O='feedPtpPmInputCurrentMax'
_N='feedPtpPmInputCurrentMin'
_M='feedPtpPmInputVoltageAve'
_L='feedPtpPmInputVoltageMax'
_K='feedPtpPmInputVoltageMin'
_J='feedPtpPmValidity'
_I='not-accessible'
_H='feedPtpPmTimestamp'
_G='feedPtpPmSampleDuration'
_F='Integer32'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-PM-FEEDPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
perfMon,=mibBuilder.importSymbols('INFINERA-REG-MIB','perfMon')
FloatHundredths,=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
feedPtpPmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,3,46))
if mibBuilder.loadTexts:feedPtpPmMIB.setRevisions(('2013-10-08 00:00',))
_FeedPtpPmRealTable_Object=MibTable
feedPtpPmRealTable=_FeedPtpPmRealTable_Object((1,3,6,1,4,1,21296,2,2,2,3,46,1))
if mibBuilder.loadTexts:feedPtpPmRealTable.setStatus(_A)
_FeedPtpPmRealEntry_Object=MibTableRow
feedPtpPmRealEntry=_FeedPtpPmRealEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,46,1,1))
feedPtpPmRealEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:feedPtpPmRealEntry.setStatus(_A)
_FeedPtpPmRealInputVoltage_Type=FloatHundredths
_FeedPtpPmRealInputVoltage_Object=MibTableColumn
feedPtpPmRealInputVoltage=_FeedPtpPmRealInputVoltage_Object((1,3,6,1,4,1,21296,2,2,2,3,46,1,1,1),_FeedPtpPmRealInputVoltage_Type())
feedPtpPmRealInputVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmRealInputVoltage.setStatus(_A)
_FeedPtpPmRealInputCurrent_Type=FloatHundredths
_FeedPtpPmRealInputCurrent_Object=MibTableColumn
feedPtpPmRealInputCurrent=_FeedPtpPmRealInputCurrent_Object((1,3,6,1,4,1,21296,2,2,2,3,46,1,1,2),_FeedPtpPmRealInputCurrent_Type())
feedPtpPmRealInputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmRealInputCurrent.setStatus(_A)
_FeedPtpPmTable_Object=MibTable
feedPtpPmTable=_FeedPtpPmTable_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2))
if mibBuilder.loadTexts:feedPtpPmTable.setStatus(_A)
_FeedPtpPmEntry_Object=MibTableRow
feedPtpPmEntry=_FeedPtpPmEntry_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1))
feedPtpPmEntry.setIndexNames((0,_D,_E),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:feedPtpPmEntry.setStatus(_A)
class _FeedPtpPmTimestamp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FeedPtpPmTimestamp_Type.__name__=_F
_FeedPtpPmTimestamp_Object=MibTableColumn
feedPtpPmTimestamp=_FeedPtpPmTimestamp_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,1),_FeedPtpPmTimestamp_Type())
feedPtpPmTimestamp.setMaxAccess(_I)
if mibBuilder.loadTexts:feedPtpPmTimestamp.setStatus(_A)
class _FeedPtpPmSampleDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteenMinutes',1),('day',2)))
_FeedPtpPmSampleDuration_Type.__name__=_F
_FeedPtpPmSampleDuration_Object=MibTableColumn
feedPtpPmSampleDuration=_FeedPtpPmSampleDuration_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,2),_FeedPtpPmSampleDuration_Type())
feedPtpPmSampleDuration.setMaxAccess(_I)
if mibBuilder.loadTexts:feedPtpPmSampleDuration.setStatus(_A)
_FeedPtpPmValidity_Type=TruthValue
_FeedPtpPmValidity_Object=MibTableColumn
feedPtpPmValidity=_FeedPtpPmValidity_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,3),_FeedPtpPmValidity_Type())
feedPtpPmValidity.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmValidity.setStatus(_A)
_FeedPtpPmInputVoltageMin_Type=FloatHundredths
_FeedPtpPmInputVoltageMin_Object=MibTableColumn
feedPtpPmInputVoltageMin=_FeedPtpPmInputVoltageMin_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,4),_FeedPtpPmInputVoltageMin_Type())
feedPtpPmInputVoltageMin.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmInputVoltageMin.setStatus(_A)
_FeedPtpPmInputVoltageMax_Type=FloatHundredths
_FeedPtpPmInputVoltageMax_Object=MibTableColumn
feedPtpPmInputVoltageMax=_FeedPtpPmInputVoltageMax_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,5),_FeedPtpPmInputVoltageMax_Type())
feedPtpPmInputVoltageMax.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmInputVoltageMax.setStatus(_A)
_FeedPtpPmInputVoltageAve_Type=FloatHundredths
_FeedPtpPmInputVoltageAve_Object=MibTableColumn
feedPtpPmInputVoltageAve=_FeedPtpPmInputVoltageAve_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,6),_FeedPtpPmInputVoltageAve_Type())
feedPtpPmInputVoltageAve.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmInputVoltageAve.setStatus(_A)
_FeedPtpPmInputCurrentMin_Type=FloatHundredths
_FeedPtpPmInputCurrentMin_Object=MibTableColumn
feedPtpPmInputCurrentMin=_FeedPtpPmInputCurrentMin_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,7),_FeedPtpPmInputCurrentMin_Type())
feedPtpPmInputCurrentMin.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmInputCurrentMin.setStatus(_A)
_FeedPtpPmInputCurrentMax_Type=FloatHundredths
_FeedPtpPmInputCurrentMax_Object=MibTableColumn
feedPtpPmInputCurrentMax=_FeedPtpPmInputCurrentMax_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,8),_FeedPtpPmInputCurrentMax_Type())
feedPtpPmInputCurrentMax.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmInputCurrentMax.setStatus(_A)
_FeedPtpPmInputCurrentAve_Type=FloatHundredths
_FeedPtpPmInputCurrentAve_Object=MibTableColumn
feedPtpPmInputCurrentAve=_FeedPtpPmInputCurrentAve_Object((1,3,6,1,4,1,21296,2,2,2,3,46,2,1,9),_FeedPtpPmInputCurrentAve_Type())
feedPtpPmInputCurrentAve.setMaxAccess(_C)
if mibBuilder.loadTexts:feedPtpPmInputCurrentAve.setStatus(_A)
_FeedPtpPmConformance_ObjectIdentity=ObjectIdentity
feedPtpPmConformance=_FeedPtpPmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,46,3))
_FeedPtpPmCompliances_ObjectIdentity=ObjectIdentity
feedPtpPmCompliances=_FeedPtpPmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,46,3,1))
_FeedPtpPmGroups_ObjectIdentity=ObjectIdentity
feedPtpPmGroups=_FeedPtpPmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,3,46,3,2))
feedPtpPmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,46,3,2,1))
feedPtpPmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:feedPtpPmGroup.setStatus(_A)
feedPtpPmRealGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,3,46,3,2,2))
feedPtpPmRealGroup.setObjects(*((_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:feedPtpPmRealGroup.setStatus(_A)
feedPtpPmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,46,3,1,1))
feedPtpPmCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:feedPtpPmCompliance.setStatus(_A)
feedPtpPmRealCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,3,46,3,1,2))
feedPtpPmRealCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:feedPtpPmRealCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'feedPtpPmMIB':feedPtpPmMIB,'feedPtpPmRealTable':feedPtpPmRealTable,'feedPtpPmRealEntry':feedPtpPmRealEntry,_Q:feedPtpPmRealInputVoltage,_R:feedPtpPmRealInputCurrent,'feedPtpPmTable':feedPtpPmTable,'feedPtpPmEntry':feedPtpPmEntry,_H:feedPtpPmTimestamp,_G:feedPtpPmSampleDuration,_J:feedPtpPmValidity,_K:feedPtpPmInputVoltageMin,_L:feedPtpPmInputVoltageMax,_M:feedPtpPmInputVoltageAve,_N:feedPtpPmInputCurrentMin,_O:feedPtpPmInputCurrentMax,_P:feedPtpPmInputCurrentAve,'feedPtpPmConformance':feedPtpPmConformance,'feedPtpPmCompliances':feedPtpPmCompliances,'feedPtpPmCompliance':feedPtpPmCompliance,'feedPtpPmRealCompliance':feedPtpPmRealCompliance,'feedPtpPmGroups':feedPtpPmGroups,_S:feedPtpPmGroup,_T:feedPtpPmRealGroup})