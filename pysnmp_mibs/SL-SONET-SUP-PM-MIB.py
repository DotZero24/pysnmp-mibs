_f='sonetCounterValue'
_e='sonetCounterId'
_d='sonetVTThresholdEntry'
_c='sonetSectionThresholdEntry'
_b='sonetFarEndVTDayNumber'
_a='sonetVTDayNumber'
_Z='not-accessible'
_Y='sonetVTDefaultThresholdRate'
_X='sonetVTDefaultThresholdDirection'
_W='sonetFarEndPathDayNumber'
_V='sonetPathDayNumber'
_U='sonetPathThresholdDirection'
_T='sonetPathDefaultThresholdRate'
_S='sonetPathDefaultThresholdDirection'
_R='accessible-for-notify'
_Q='sonetFarEndLineDayNumber'
_P='sonetLineDayNumber'
_O='sonetLineThresholdDirection'
_N='vt1dot5'
_M='sonetLineDefaultThresholdRate'
_L='sonetLineDefaultThresholdDirection'
_K='sonetSectionDayNumber'
_J='sonetSectionDefaultThresholdRate'
_I='farEnd'
_H='nearEnd'
_G='ifIndex'
_F='IF-MIB'
_E='SL-SONET-SUP-PM-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slSonetMib,=mibBuilder.importSymbols('SL-SONET-MIB','slSonetMib')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
sonetFarEndLineCurrentEntry,sonetFarEndLineIntervalEntry,sonetFarEndPathCurrentEntry,sonetFarEndPathIntervalEntry,sonetFarEndVTCurrentEntry,sonetFarEndVTIntervalEntry,sonetLineCurrentEntry,sonetLineIntervalEntry,sonetMediumEntry,sonetPathCurrentEntry,sonetPathIntervalEntry,sonetSectionCurrentEntry,sonetSectionIntervalEntry,sonetVTCurrentEntry,sonetVTIntervalEntry=mibBuilder.importSymbols('SONET-MIB','sonetFarEndLineCurrentEntry','sonetFarEndLineIntervalEntry','sonetFarEndPathCurrentEntry','sonetFarEndPathIntervalEntry','sonetFarEndVTCurrentEntry','sonetFarEndVTIntervalEntry','sonetLineCurrentEntry','sonetLineIntervalEntry','sonetMediumEntry','sonetPathCurrentEntry','sonetPathIntervalEntry','sonetSectionCurrentEntry','sonetSectionIntervalEntry','sonetVTCurrentEntry','sonetVTIntervalEntry')
sonetSupPmMIB=ModuleIdentity((1,3,6,1,4,1,4515,1,6,3))
_SonetSupObjects_ObjectIdentity=ObjectIdentity
sonetSupObjects=_SonetSupObjects_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,1))
_SonetSupConfig_ObjectIdentity=ObjectIdentity
sonetSupConfig=_SonetSupConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,1,1))
_SonetSupMedium_ObjectIdentity=ObjectIdentity
sonetSupMedium=_SonetSupMedium_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,1,2))
_SonetSupSection_ObjectIdentity=ObjectIdentity
sonetSupSection=_SonetSupSection_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,1,3))
_SonetSectionDefaultThresholdTable_Object=MibTable
sonetSectionDefaultThresholdTable=_SonetSectionDefaultThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1))
if mibBuilder.loadTexts:sonetSectionDefaultThresholdTable.setStatus(_A)
_SonetSectionDefaultThresholdEntry_Object=MibTableRow
sonetSectionDefaultThresholdEntry=_SonetSectionDefaultThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1))
sonetSectionDefaultThresholdEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:sonetSectionDefaultThresholdEntry.setStatus(_A)
class _SonetSectionDefaultThresholdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('oc1',1),('oc3',2),('oc12',3),('oc24',4),('oc48',5),('oc192',6)))
_SonetSectionDefaultThresholdRate_Type.__name__=_D
_SonetSectionDefaultThresholdRate_Object=MibTableColumn
sonetSectionDefaultThresholdRate=_SonetSectionDefaultThresholdRate_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,1),_SonetSectionDefaultThresholdRate_Type())
sonetSectionDefaultThresholdRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDefaultThresholdRate.setStatus(_A)
_SonetSectionDefaultCVThreshold_Type=Integer32
_SonetSectionDefaultCVThreshold_Object=MibTableColumn
sonetSectionDefaultCVThreshold=_SonetSectionDefaultCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,2),_SonetSectionDefaultCVThreshold_Type())
sonetSectionDefaultCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultCVThreshold.setStatus(_A)
_SonetSectionDefaultESThreshold_Type=Integer32
_SonetSectionDefaultESThreshold_Object=MibTableColumn
sonetSectionDefaultESThreshold=_SonetSectionDefaultESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,3),_SonetSectionDefaultESThreshold_Type())
sonetSectionDefaultESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultESThreshold.setStatus(_A)
_SonetSectionDefaultSESThreshold_Type=Integer32
_SonetSectionDefaultSESThreshold_Object=MibTableColumn
sonetSectionDefaultSESThreshold=_SonetSectionDefaultSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,6),_SonetSectionDefaultSESThreshold_Type())
sonetSectionDefaultSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultSESThreshold.setStatus(_A)
_SonetSectionDefaultSEFSThreshold_Type=Integer32
_SonetSectionDefaultSEFSThreshold_Object=MibTableColumn
sonetSectionDefaultSEFSThreshold=_SonetSectionDefaultSEFSThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,7),_SonetSectionDefaultSEFSThreshold_Type())
sonetSectionDefaultSEFSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultSEFSThreshold.setStatus(_A)
_SonetSectionDefaultDayCVThreshold_Type=Integer32
_SonetSectionDefaultDayCVThreshold_Object=MibTableColumn
sonetSectionDefaultDayCVThreshold=_SonetSectionDefaultDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,8),_SonetSectionDefaultDayCVThreshold_Type())
sonetSectionDefaultDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultDayCVThreshold.setStatus(_A)
_SonetSectionDefaultDayESThreshold_Type=Integer32
_SonetSectionDefaultDayESThreshold_Object=MibTableColumn
sonetSectionDefaultDayESThreshold=_SonetSectionDefaultDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,9),_SonetSectionDefaultDayESThreshold_Type())
sonetSectionDefaultDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultDayESThreshold.setStatus(_A)
_SonetSectionDefaultDaySESThreshold_Type=Integer32
_SonetSectionDefaultDaySESThreshold_Object=MibTableColumn
sonetSectionDefaultDaySESThreshold=_SonetSectionDefaultDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,12),_SonetSectionDefaultDaySESThreshold_Type())
sonetSectionDefaultDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultDaySESThreshold.setStatus(_A)
_SonetSectionDefaultDaySEFSThreshold_Type=Integer32
_SonetSectionDefaultDaySEFSThreshold_Object=MibTableColumn
sonetSectionDefaultDaySEFSThreshold=_SonetSectionDefaultDaySEFSThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,1,1,13),_SonetSectionDefaultDaySEFSThreshold_Type())
sonetSectionDefaultDaySEFSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDefaultDaySEFSThreshold.setStatus(_A)
_SonetSectionThresholdTable_Object=MibTable
sonetSectionThresholdTable=_SonetSectionThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2))
if mibBuilder.loadTexts:sonetSectionThresholdTable.setStatus(_A)
_SonetSectionThresholdEntry_Object=MibTableRow
sonetSectionThresholdEntry=_SonetSectionThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1))
if mibBuilder.loadTexts:sonetSectionThresholdEntry.setStatus(_A)
class _SonetSectionCurrentCVThreshold_Type(Integer32):defaultValue=0
_SonetSectionCurrentCVThreshold_Type.__name__=_D
_SonetSectionCurrentCVThreshold_Object=MibTableColumn
sonetSectionCurrentCVThreshold=_SonetSectionCurrentCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,1),_SonetSectionCurrentCVThreshold_Type())
sonetSectionCurrentCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentCVThreshold.setStatus(_A)
class _SonetSectionCurrentESThreshold_Type(Integer32):defaultValue=0
_SonetSectionCurrentESThreshold_Type.__name__=_D
_SonetSectionCurrentESThreshold_Object=MibTableColumn
sonetSectionCurrentESThreshold=_SonetSectionCurrentESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,2),_SonetSectionCurrentESThreshold_Type())
sonetSectionCurrentESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentESThreshold.setStatus(_A)
class _SonetSectionCurrentSESThreshold_Type(Integer32):defaultValue=0
_SonetSectionCurrentSESThreshold_Type.__name__=_D
_SonetSectionCurrentSESThreshold_Object=MibTableColumn
sonetSectionCurrentSESThreshold=_SonetSectionCurrentSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,5),_SonetSectionCurrentSESThreshold_Type())
sonetSectionCurrentSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentSESThreshold.setStatus(_A)
class _SonetSectionCurrentSEFSThreshold_Type(Integer32):defaultValue=0
_SonetSectionCurrentSEFSThreshold_Type.__name__=_D
_SonetSectionCurrentSEFSThreshold_Object=MibTableColumn
sonetSectionCurrentSEFSThreshold=_SonetSectionCurrentSEFSThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,6),_SonetSectionCurrentSEFSThreshold_Type())
sonetSectionCurrentSEFSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionCurrentSEFSThreshold.setStatus(_A)
class _SonetSectionDayCVThreshold_Type(Integer32):defaultValue=0
_SonetSectionDayCVThreshold_Type.__name__=_D
_SonetSectionDayCVThreshold_Object=MibTableColumn
sonetSectionDayCVThreshold=_SonetSectionDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,7),_SonetSectionDayCVThreshold_Type())
sonetSectionDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDayCVThreshold.setStatus(_A)
class _SonetSectionDayESThreshold_Type(Integer32):defaultValue=0
_SonetSectionDayESThreshold_Type.__name__=_D
_SonetSectionDayESThreshold_Object=MibTableColumn
sonetSectionDayESThreshold=_SonetSectionDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,8),_SonetSectionDayESThreshold_Type())
sonetSectionDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDayESThreshold.setStatus(_A)
class _SonetSectionDaySESThreshold_Type(Integer32):defaultValue=0
_SonetSectionDaySESThreshold_Type.__name__=_D
_SonetSectionDaySESThreshold_Object=MibTableColumn
sonetSectionDaySESThreshold=_SonetSectionDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,11),_SonetSectionDaySESThreshold_Type())
sonetSectionDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDaySESThreshold.setStatus(_A)
class _SonetSectionDaySEFSThreshold_Type(Integer32):defaultValue=0
_SonetSectionDaySEFSThreshold_Type.__name__=_D
_SonetSectionDaySEFSThreshold_Object=MibTableColumn
sonetSectionDaySEFSThreshold=_SonetSectionDaySEFSThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,3,2,1,12),_SonetSectionDaySEFSThreshold_Type())
sonetSectionDaySEFSThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDaySEFSThreshold.setStatus(_A)
_SonetSectionDayTable_Object=MibTable
sonetSectionDayTable=_SonetSectionDayTable_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15))
if mibBuilder.loadTexts:sonetSectionDayTable.setStatus(_A)
_SonetSectionDayEntry_Object=MibTableRow
sonetSectionDayEntry=_SonetSectionDayEntry_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1))
sonetSectionDayEntry.setIndexNames((0,_F,_G),(0,_E,_K))
if mibBuilder.loadTexts:sonetSectionDayEntry.setStatus(_A)
class _SonetSectionDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33))
_SonetSectionDayNumber_Type.__name__=_D
_SonetSectionDayNumber_Object=MibTableColumn
sonetSectionDayNumber=_SonetSectionDayNumber_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,1),_SonetSectionDayNumber_Type())
sonetSectionDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDayNumber.setStatus(_A)
_SonetSectionDayStartTime_Type=DateAndTime
_SonetSectionDayStartTime_Object=MibTableColumn
sonetSectionDayStartTime=_SonetSectionDayStartTime_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,2),_SonetSectionDayStartTime_Type())
sonetSectionDayStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDayStartTime.setStatus(_A)
_SonetSectionDayValidData_Type=TruthValue
_SonetSectionDayValidData_Object=MibTableColumn
sonetSectionDayValidData=_SonetSectionDayValidData_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,3),_SonetSectionDayValidData_Type())
sonetSectionDayValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDayValidData.setStatus(_A)
_SonetSectionDayCVs_Type=PerfTotalCount
_SonetSectionDayCVs_Object=MibTableColumn
sonetSectionDayCVs=_SonetSectionDayCVs_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,4),_SonetSectionDayCVs_Type())
sonetSectionDayCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDayCVs.setStatus(_A)
_SonetSectionDayESs_Type=PerfTotalCount
_SonetSectionDayESs_Object=MibTableColumn
sonetSectionDayESs=_SonetSectionDayESs_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,5),_SonetSectionDayESs_Type())
sonetSectionDayESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDayESs.setStatus(_A)
_SonetSectionDaySESs_Type=PerfTotalCount
_SonetSectionDaySESs_Object=MibTableColumn
sonetSectionDaySESs=_SonetSectionDaySESs_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,8),_SonetSectionDaySESs_Type())
sonetSectionDaySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDaySESs.setStatus(_A)
_SonetSectionDaySEFSs_Type=PerfTotalCount
_SonetSectionDaySEFSs_Object=MibTableColumn
sonetSectionDaySEFSs=_SonetSectionDaySEFSs_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,9),_SonetSectionDaySEFSs_Type())
sonetSectionDaySEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDaySEFSs.setStatus(_A)
_SonetSectionDayTcaFlag_Type=TruthValue
_SonetSectionDayTcaFlag_Object=MibTableColumn
sonetSectionDayTcaFlag=_SonetSectionDayTcaFlag_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,10),_SonetSectionDayTcaFlag_Type())
sonetSectionDayTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetSectionDayTcaFlag.setStatus(_A)
_SonetSectionDayReset_Type=Integer32
_SonetSectionDayReset_Object=MibTableColumn
sonetSectionDayReset=_SonetSectionDayReset_Object((1,3,6,1,4,1,4515,1,6,3,1,3,15,1,11),_SonetSectionDayReset_Type())
sonetSectionDayReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetSectionDayReset.setStatus(_A)
_SonetSupLine_ObjectIdentity=ObjectIdentity
sonetSupLine=_SonetSupLine_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,1,4))
_SonetLineDefaultThresholdTable_Object=MibTable
sonetLineDefaultThresholdTable=_SonetLineDefaultThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1))
if mibBuilder.loadTexts:sonetLineDefaultThresholdTable.setStatus(_A)
_SonetLineDefaultThresholdEntry_Object=MibTableRow
sonetLineDefaultThresholdEntry=_SonetLineDefaultThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1))
sonetLineDefaultThresholdEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:sonetLineDefaultThresholdEntry.setStatus(_A)
class _SonetLineDefaultThresholdDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SonetLineDefaultThresholdDirection_Type.__name__=_D
_SonetLineDefaultThresholdDirection_Object=MibTableColumn
sonetLineDefaultThresholdDirection=_SonetLineDefaultThresholdDirection_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,1),_SonetLineDefaultThresholdDirection_Type())
sonetLineDefaultThresholdDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDefaultThresholdDirection.setStatus(_A)
class _SonetLineDefaultThresholdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_N,1),('vtg',2),('oc1',3),('oc3',4),('oc12',5),('oc24',6),('oc48',7),('oc192',8)))
_SonetLineDefaultThresholdRate_Type.__name__=_D
_SonetLineDefaultThresholdRate_Object=MibTableColumn
sonetLineDefaultThresholdRate=_SonetLineDefaultThresholdRate_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,2),_SonetLineDefaultThresholdRate_Type())
sonetLineDefaultThresholdRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDefaultThresholdRate.setStatus(_A)
_SonetLineDefaultCVThreshold_Type=Integer32
_SonetLineDefaultCVThreshold_Object=MibTableColumn
sonetLineDefaultCVThreshold=_SonetLineDefaultCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,3),_SonetLineDefaultCVThreshold_Type())
sonetLineDefaultCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultCVThreshold.setStatus(_A)
_SonetLineDefaultESThreshold_Type=Integer32
_SonetLineDefaultESThreshold_Object=MibTableColumn
sonetLineDefaultESThreshold=_SonetLineDefaultESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,4),_SonetLineDefaultESThreshold_Type())
sonetLineDefaultESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultESThreshold.setStatus(_A)
_SonetLineDefaultSESThreshold_Type=Integer32
_SonetLineDefaultSESThreshold_Object=MibTableColumn
sonetLineDefaultSESThreshold=_SonetLineDefaultSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,7),_SonetLineDefaultSESThreshold_Type())
sonetLineDefaultSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultSESThreshold.setStatus(_A)
_SonetLineDefaultUASThreshold_Type=Integer32
_SonetLineDefaultUASThreshold_Object=MibTableColumn
sonetLineDefaultUASThreshold=_SonetLineDefaultUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,9),_SonetLineDefaultUASThreshold_Type())
sonetLineDefaultUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultUASThreshold.setStatus(_A)
_SonetLineDefaultDayCVThreshold_Type=Integer32
_SonetLineDefaultDayCVThreshold_Object=MibTableColumn
sonetLineDefaultDayCVThreshold=_SonetLineDefaultDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,10),_SonetLineDefaultDayCVThreshold_Type())
sonetLineDefaultDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultDayCVThreshold.setStatus(_A)
_SonetLineDefaultDayESThreshold_Type=Integer32
_SonetLineDefaultDayESThreshold_Object=MibTableColumn
sonetLineDefaultDayESThreshold=_SonetLineDefaultDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,11),_SonetLineDefaultDayESThreshold_Type())
sonetLineDefaultDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultDayESThreshold.setStatus(_A)
_SonetLineDefaultDaySESThreshold_Type=Integer32
_SonetLineDefaultDaySESThreshold_Object=MibTableColumn
sonetLineDefaultDaySESThreshold=_SonetLineDefaultDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,14),_SonetLineDefaultDaySESThreshold_Type())
sonetLineDefaultDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultDaySESThreshold.setStatus(_A)
_SonetLineDefaultDayUASThreshold_Type=Integer32
_SonetLineDefaultDayUASThreshold_Object=MibTableColumn
sonetLineDefaultDayUASThreshold=_SonetLineDefaultDayUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,1,1,16),_SonetLineDefaultDayUASThreshold_Type())
sonetLineDefaultDayUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDefaultDayUASThreshold.setStatus(_A)
_SonetLineThresholdTable_Object=MibTable
sonetLineThresholdTable=_SonetLineThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2))
if mibBuilder.loadTexts:sonetLineThresholdTable.setStatus(_A)
_SonetLineThresholdEntry_Object=MibTableRow
sonetLineThresholdEntry=_SonetLineThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1))
sonetLineThresholdEntry.setIndexNames((0,_F,_G),(0,_E,_O))
if mibBuilder.loadTexts:sonetLineThresholdEntry.setStatus(_A)
class _SonetLineThresholdDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SonetLineThresholdDirection_Type.__name__=_D
_SonetLineThresholdDirection_Object=MibTableColumn
sonetLineThresholdDirection=_SonetLineThresholdDirection_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,1),_SonetLineThresholdDirection_Type())
sonetLineThresholdDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineThresholdDirection.setStatus(_A)
class _SonetLineCurrentCVThreshold_Type(Integer32):defaultValue=0
_SonetLineCurrentCVThreshold_Type.__name__=_D
_SonetLineCurrentCVThreshold_Object=MibTableColumn
sonetLineCurrentCVThreshold=_SonetLineCurrentCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,2),_SonetLineCurrentCVThreshold_Type())
sonetLineCurrentCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentCVThreshold.setStatus(_A)
class _SonetLineCurrentESThreshold_Type(Integer32):defaultValue=0
_SonetLineCurrentESThreshold_Type.__name__=_D
_SonetLineCurrentESThreshold_Object=MibTableColumn
sonetLineCurrentESThreshold=_SonetLineCurrentESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,3),_SonetLineCurrentESThreshold_Type())
sonetLineCurrentESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentESThreshold.setStatus(_A)
class _SonetLineCurrentSESThreshold_Type(Integer32):defaultValue=0
_SonetLineCurrentSESThreshold_Type.__name__=_D
_SonetLineCurrentSESThreshold_Object=MibTableColumn
sonetLineCurrentSESThreshold=_SonetLineCurrentSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,4),_SonetLineCurrentSESThreshold_Type())
sonetLineCurrentSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentSESThreshold.setStatus(_A)
class _SonetLineCurrentUASThreshold_Type(Integer32):defaultValue=0
_SonetLineCurrentUASThreshold_Type.__name__=_D
_SonetLineCurrentUASThreshold_Object=MibTableColumn
sonetLineCurrentUASThreshold=_SonetLineCurrentUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,5),_SonetLineCurrentUASThreshold_Type())
sonetLineCurrentUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineCurrentUASThreshold.setStatus(_A)
class _SonetLineDayCVThreshold_Type(Integer32):defaultValue=0
_SonetLineDayCVThreshold_Type.__name__=_D
_SonetLineDayCVThreshold_Object=MibTableColumn
sonetLineDayCVThreshold=_SonetLineDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,6),_SonetLineDayCVThreshold_Type())
sonetLineDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDayCVThreshold.setStatus(_A)
class _SonetLineDayESThreshold_Type(Integer32):defaultValue=0
_SonetLineDayESThreshold_Type.__name__=_D
_SonetLineDayESThreshold_Object=MibTableColumn
sonetLineDayESThreshold=_SonetLineDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,7),_SonetLineDayESThreshold_Type())
sonetLineDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDayESThreshold.setStatus(_A)
class _SonetLineDaySESThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SonetLineDaySESThreshold_Type.__name__=_D
_SonetLineDaySESThreshold_Object=MibTableColumn
sonetLineDaySESThreshold=_SonetLineDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,8),_SonetLineDaySESThreshold_Type())
sonetLineDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDaySESThreshold.setStatus(_A)
class _SonetLineDayUASThreshold_Type(Integer32):defaultValue=0
_SonetLineDayUASThreshold_Type.__name__=_D
_SonetLineDayUASThreshold_Object=MibTableColumn
sonetLineDayUASThreshold=_SonetLineDayUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,1,4,2,1,9),_SonetLineDayUASThreshold_Type())
sonetLineDayUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDayUASThreshold.setStatus(_A)
_SonetLineDayTable_Object=MibTable
sonetLineDayTable=_SonetLineDayTable_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5))
if mibBuilder.loadTexts:sonetLineDayTable.setStatus(_A)
_SonetLineDayEntry_Object=MibTableRow
sonetLineDayEntry=_SonetLineDayEntry_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1))
sonetLineDayEntry.setIndexNames((0,_F,_G),(0,_E,_P))
if mibBuilder.loadTexts:sonetLineDayEntry.setStatus(_A)
class _SonetLineDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,33))
_SonetLineDayNumber_Type.__name__=_D
_SonetLineDayNumber_Object=MibTableColumn
sonetLineDayNumber=_SonetLineDayNumber_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,1),_SonetLineDayNumber_Type())
sonetLineDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayNumber.setStatus(_A)
_SonetLineDayStartTime_Type=DateAndTime
_SonetLineDayStartTime_Object=MibTableColumn
sonetLineDayStartTime=_SonetLineDayStartTime_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,2),_SonetLineDayStartTime_Type())
sonetLineDayStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayStartTime.setStatus(_A)
_SonetLineDayValidData_Type=TruthValue
_SonetLineDayValidData_Object=MibTableColumn
sonetLineDayValidData=_SonetLineDayValidData_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,3),_SonetLineDayValidData_Type())
sonetLineDayValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayValidData.setStatus(_A)
_SonetLineDayCVs_Type=PerfTotalCount
_SonetLineDayCVs_Object=MibTableColumn
sonetLineDayCVs=_SonetLineDayCVs_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,5),_SonetLineDayCVs_Type())
sonetLineDayCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayCVs.setStatus(_A)
_SonetLineDayESs_Type=PerfTotalCount
_SonetLineDayESs_Object=MibTableColumn
sonetLineDayESs=_SonetLineDayESs_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,6),_SonetLineDayESs_Type())
sonetLineDayESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayESs.setStatus(_A)
_SonetLineDaySESs_Type=PerfTotalCount
_SonetLineDaySESs_Object=MibTableColumn
sonetLineDaySESs=_SonetLineDaySESs_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,9),_SonetLineDaySESs_Type())
sonetLineDaySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDaySESs.setStatus(_A)
_SonetLineDayUASs_Type=PerfTotalCount
_SonetLineDayUASs_Object=MibTableColumn
sonetLineDayUASs=_SonetLineDayUASs_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,10),_SonetLineDayUASs_Type())
sonetLineDayUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayUASs.setStatus(_A)
_SonetLineDayPSC_Type=PerfTotalCount
_SonetLineDayPSC_Object=MibTableColumn
sonetLineDayPSC=_SonetLineDayPSC_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,11),_SonetLineDayPSC_Type())
sonetLineDayPSC.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayPSC.setStatus(_A)
_SonetLineDayPSD_Type=PerfTotalCount
_SonetLineDayPSD_Object=MibTableColumn
sonetLineDayPSD=_SonetLineDayPSD_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,12),_SonetLineDayPSD_Type())
sonetLineDayPSD.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayPSD.setStatus(_A)
_SonetLineDayFCs_Type=PerfTotalCount
_SonetLineDayFCs_Object=MibTableColumn
sonetLineDayFCs=_SonetLineDayFCs_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,13),_SonetLineDayFCs_Type())
sonetLineDayFCs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayFCs.setStatus(_A)
_SonetLineDayTcaFlag_Type=TruthValue
_SonetLineDayTcaFlag_Object=MibTableColumn
sonetLineDayTcaFlag=_SonetLineDayTcaFlag_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,14),_SonetLineDayTcaFlag_Type())
sonetLineDayTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetLineDayTcaFlag.setStatus(_A)
_SonetLineDayReset_Type=Integer32
_SonetLineDayReset_Object=MibTableColumn
sonetLineDayReset=_SonetLineDayReset_Object((1,3,6,1,4,1,4515,1,6,3,1,4,5,1,15),_SonetLineDayReset_Type())
sonetLineDayReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetLineDayReset.setStatus(_A)
_SonetSupFarEndLine_ObjectIdentity=ObjectIdentity
sonetSupFarEndLine=_SonetSupFarEndLine_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,1,5))
_SonetFarEndLineDayTable_Object=MibTable
sonetFarEndLineDayTable=_SonetFarEndLineDayTable_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3))
if mibBuilder.loadTexts:sonetFarEndLineDayTable.setStatus(_A)
_SonetFarEndLineDayEntry_Object=MibTableRow
sonetFarEndLineDayEntry=_SonetFarEndLineDayEntry_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1))
sonetFarEndLineDayEntry.setIndexNames((0,_F,_G),(0,_E,_Q))
if mibBuilder.loadTexts:sonetFarEndLineDayEntry.setStatus(_A)
class _SonetFarEndLineDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_SonetFarEndLineDayNumber_Type.__name__=_D
_SonetFarEndLineDayNumber_Object=MibTableColumn
sonetFarEndLineDayNumber=_SonetFarEndLineDayNumber_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,1),_SonetFarEndLineDayNumber_Type())
sonetFarEndLineDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayNumber.setStatus(_A)
_SonetFarEndLineDayStartTime_Type=DateAndTime
_SonetFarEndLineDayStartTime_Object=MibTableColumn
sonetFarEndLineDayStartTime=_SonetFarEndLineDayStartTime_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,2),_SonetFarEndLineDayStartTime_Type())
sonetFarEndLineDayStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayStartTime.setStatus(_A)
_SonetFarEndLineDayValidData_Type=TruthValue
_SonetFarEndLineDayValidData_Object=MibTableColumn
sonetFarEndLineDayValidData=_SonetFarEndLineDayValidData_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,3),_SonetFarEndLineDayValidData_Type())
sonetFarEndLineDayValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayValidData.setStatus(_A)
_SonetFarEndLineDayCVs_Type=PerfTotalCount
_SonetFarEndLineDayCVs_Object=MibTableColumn
sonetFarEndLineDayCVs=_SonetFarEndLineDayCVs_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,5),_SonetFarEndLineDayCVs_Type())
sonetFarEndLineDayCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayCVs.setStatus(_A)
_SonetFarEndLineDayESs_Type=PerfTotalCount
_SonetFarEndLineDayESs_Object=MibTableColumn
sonetFarEndLineDayESs=_SonetFarEndLineDayESs_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,6),_SonetFarEndLineDayESs_Type())
sonetFarEndLineDayESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayESs.setStatus(_A)
_SonetFarEndLineDaySESs_Type=PerfTotalCount
_SonetFarEndLineDaySESs_Object=MibTableColumn
sonetFarEndLineDaySESs=_SonetFarEndLineDaySESs_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,9),_SonetFarEndLineDaySESs_Type())
sonetFarEndLineDaySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDaySESs.setStatus(_A)
_SonetFarEndLineDayUASs_Type=PerfTotalCount
_SonetFarEndLineDayUASs_Object=MibTableColumn
sonetFarEndLineDayUASs=_SonetFarEndLineDayUASs_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,10),_SonetFarEndLineDayUASs_Type())
sonetFarEndLineDayUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayUASs.setStatus(_A)
_SonetFarEndLineDayFCs_Type=PerfTotalCount
_SonetFarEndLineDayFCs_Object=MibTableColumn
sonetFarEndLineDayFCs=_SonetFarEndLineDayFCs_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,11),_SonetFarEndLineDayFCs_Type())
sonetFarEndLineDayFCs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayFCs.setStatus(_A)
_SonetFarEndLineDayTcaFlag_Type=TruthValue
_SonetFarEndLineDayTcaFlag_Object=MibTableColumn
sonetFarEndLineDayTcaFlag=_SonetFarEndLineDayTcaFlag_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,12),_SonetFarEndLineDayTcaFlag_Type())
sonetFarEndLineDayTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndLineDayTcaFlag.setStatus(_A)
_SonetFarEndLineDayReset_Type=Integer32
_SonetFarEndLineDayReset_Object=MibTableColumn
sonetFarEndLineDayReset=_SonetFarEndLineDayReset_Object((1,3,6,1,4,1,4515,1,6,3,1,5,3,1,13),_SonetFarEndLineDayReset_Type())
sonetFarEndLineDayReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndLineDayReset.setStatus(_A)
_SonetTrap_ObjectIdentity=ObjectIdentity
sonetTrap=_SonetTrap_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,1,6))
_SonetCounterId_Type=ObjectIdentifier
_SonetCounterId_Object=MibScalar
sonetCounterId=_SonetCounterId_Object((1,3,6,1,4,1,4515,1,6,3,1,6,1),_SonetCounterId_Type())
sonetCounterId.setMaxAccess(_R)
if mibBuilder.loadTexts:sonetCounterId.setStatus(_A)
_SonetCounterValue_Type=Integer32
_SonetCounterValue_Object=MibScalar
sonetCounterValue=_SonetCounterValue_Object((1,3,6,1,4,1,4515,1,6,3,1,6,2),_SonetCounterValue_Type())
sonetCounterValue.setMaxAccess(_R)
if mibBuilder.loadTexts:sonetCounterValue.setStatus(_A)
_SonetSupObjectsPath_ObjectIdentity=ObjectIdentity
sonetSupObjectsPath=_SonetSupObjectsPath_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,2))
_SonetSupPath_ObjectIdentity=ObjectIdentity
sonetSupPath=_SonetSupPath_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,2,1))
_SonetPathDefaultThresholdTable_Object=MibTable
sonetPathDefaultThresholdTable=_SonetPathDefaultThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1))
if mibBuilder.loadTexts:sonetPathDefaultThresholdTable.setStatus(_A)
_SonetPathDefaultThresholdEntry_Object=MibTableRow
sonetPathDefaultThresholdEntry=_SonetPathDefaultThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1))
sonetPathDefaultThresholdEntry.setIndexNames((0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:sonetPathDefaultThresholdEntry.setStatus(_A)
class _SonetPathDefaultThresholdDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SonetPathDefaultThresholdDirection_Type.__name__=_D
_SonetPathDefaultThresholdDirection_Object=MibTableColumn
sonetPathDefaultThresholdDirection=_SonetPathDefaultThresholdDirection_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,1),_SonetPathDefaultThresholdDirection_Type())
sonetPathDefaultThresholdDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDefaultThresholdDirection.setStatus(_A)
class _SonetPathDefaultThresholdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('sts1',1),('sts3',2),('sts12',3),('sts24',4),('sts48',5),('sts192',6)))
_SonetPathDefaultThresholdRate_Type.__name__=_D
_SonetPathDefaultThresholdRate_Object=MibTableColumn
sonetPathDefaultThresholdRate=_SonetPathDefaultThresholdRate_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,2),_SonetPathDefaultThresholdRate_Type())
sonetPathDefaultThresholdRate.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDefaultThresholdRate.setStatus(_A)
_SonetPathDefaultCVThreshold_Type=Integer32
_SonetPathDefaultCVThreshold_Object=MibTableColumn
sonetPathDefaultCVThreshold=_SonetPathDefaultCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,3),_SonetPathDefaultCVThreshold_Type())
sonetPathDefaultCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultCVThreshold.setStatus(_A)
_SonetPathDefaultESThreshold_Type=Integer32
_SonetPathDefaultESThreshold_Object=MibTableColumn
sonetPathDefaultESThreshold=_SonetPathDefaultESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,4),_SonetPathDefaultESThreshold_Type())
sonetPathDefaultESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultESThreshold.setStatus(_A)
_SonetPathDefaultSESThreshold_Type=Integer32
_SonetPathDefaultSESThreshold_Object=MibTableColumn
sonetPathDefaultSESThreshold=_SonetPathDefaultSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,7),_SonetPathDefaultSESThreshold_Type())
sonetPathDefaultSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultSESThreshold.setStatus(_A)
_SonetPathDefaultUASThreshold_Type=Integer32
_SonetPathDefaultUASThreshold_Object=MibTableColumn
sonetPathDefaultUASThreshold=_SonetPathDefaultUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,8),_SonetPathDefaultUASThreshold_Type())
sonetPathDefaultUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultUASThreshold.setStatus(_A)
_SonetPathDefaultDayCVThreshold_Type=Integer32
_SonetPathDefaultDayCVThreshold_Object=MibTableColumn
sonetPathDefaultDayCVThreshold=_SonetPathDefaultDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,16),_SonetPathDefaultDayCVThreshold_Type())
sonetPathDefaultDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultDayCVThreshold.setStatus(_A)
_SonetPathDefaultDayESThreshold_Type=Integer32
_SonetPathDefaultDayESThreshold_Object=MibTableColumn
sonetPathDefaultDayESThreshold=_SonetPathDefaultDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,17),_SonetPathDefaultDayESThreshold_Type())
sonetPathDefaultDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultDayESThreshold.setStatus(_A)
_SonetPathDefaultDaySESThreshold_Type=Integer32
_SonetPathDefaultDaySESThreshold_Object=MibTableColumn
sonetPathDefaultDaySESThreshold=_SonetPathDefaultDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,20),_SonetPathDefaultDaySESThreshold_Type())
sonetPathDefaultDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultDaySESThreshold.setStatus(_A)
_SonetPathDefaultDayUASThreshold_Type=Integer32
_SonetPathDefaultDayUASThreshold_Object=MibTableColumn
sonetPathDefaultDayUASThreshold=_SonetPathDefaultDayUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,1,1,21),_SonetPathDefaultDayUASThreshold_Type())
sonetPathDefaultDayUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDefaultDayUASThreshold.setStatus(_A)
_SonetPathThresholdTable_Object=MibTable
sonetPathThresholdTable=_SonetPathThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2))
if mibBuilder.loadTexts:sonetPathThresholdTable.setStatus(_A)
_SonetPathThresholdEntry_Object=MibTableRow
sonetPathThresholdEntry=_SonetPathThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1))
sonetPathThresholdEntry.setIndexNames((0,_F,_G),(0,_E,_U))
if mibBuilder.loadTexts:sonetPathThresholdEntry.setStatus(_A)
class _SonetPathThresholdDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SonetPathThresholdDirection_Type.__name__=_D
_SonetPathThresholdDirection_Object=MibTableColumn
sonetPathThresholdDirection=_SonetPathThresholdDirection_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,1),_SonetPathThresholdDirection_Type())
sonetPathThresholdDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathThresholdDirection.setStatus(_A)
class _SonetPathCurrentCVThreshold_Type(Integer32):defaultValue=0
_SonetPathCurrentCVThreshold_Type.__name__=_D
_SonetPathCurrentCVThreshold_Object=MibTableColumn
sonetPathCurrentCVThreshold=_SonetPathCurrentCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,2),_SonetPathCurrentCVThreshold_Type())
sonetPathCurrentCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentCVThreshold.setStatus(_A)
class _SonetPathCurrentESThreshold_Type(Integer32):defaultValue=0
_SonetPathCurrentESThreshold_Type.__name__=_D
_SonetPathCurrentESThreshold_Object=MibTableColumn
sonetPathCurrentESThreshold=_SonetPathCurrentESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,3),_SonetPathCurrentESThreshold_Type())
sonetPathCurrentESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentESThreshold.setStatus(_A)
class _SonetPathCurrentSESThreshold_Type(Integer32):defaultValue=0
_SonetPathCurrentSESThreshold_Type.__name__=_D
_SonetPathCurrentSESThreshold_Object=MibTableColumn
sonetPathCurrentSESThreshold=_SonetPathCurrentSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,4),_SonetPathCurrentSESThreshold_Type())
sonetPathCurrentSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentSESThreshold.setStatus(_A)
class _SonetPathCurrentUASThreshold_Type(Integer32):defaultValue=0
_SonetPathCurrentUASThreshold_Type.__name__=_D
_SonetPathCurrentUASThreshold_Object=MibTableColumn
sonetPathCurrentUASThreshold=_SonetPathCurrentUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,5),_SonetPathCurrentUASThreshold_Type())
sonetPathCurrentUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathCurrentUASThreshold.setStatus(_A)
class _SonetPathDayCVThreshold_Type(Integer32):defaultValue=0
_SonetPathDayCVThreshold_Type.__name__=_D
_SonetPathDayCVThreshold_Object=MibTableColumn
sonetPathDayCVThreshold=_SonetPathDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,6),_SonetPathDayCVThreshold_Type())
sonetPathDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDayCVThreshold.setStatus(_A)
class _SonetPathDayESThreshold_Type(Integer32):defaultValue=0
_SonetPathDayESThreshold_Type.__name__=_D
_SonetPathDayESThreshold_Object=MibTableColumn
sonetPathDayESThreshold=_SonetPathDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,7),_SonetPathDayESThreshold_Type())
sonetPathDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDayESThreshold.setStatus(_A)
class _SonetPathDaySESThreshold_Type(Integer32):defaultValue=0
_SonetPathDaySESThreshold_Type.__name__=_D
_SonetPathDaySESThreshold_Object=MibTableColumn
sonetPathDaySESThreshold=_SonetPathDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,8),_SonetPathDaySESThreshold_Type())
sonetPathDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDaySESThreshold.setStatus(_A)
class _SonetPathDayUASThreshold_Type(Integer32):defaultValue=0
_SonetPathDayUASThreshold_Type.__name__=_D
_SonetPathDayUASThreshold_Object=MibTableColumn
sonetPathDayUASThreshold=_SonetPathDayUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,2,1,2,1,9),_SonetPathDayUASThreshold_Type())
sonetPathDayUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDayUASThreshold.setStatus(_A)
_SonetPathDayTable_Object=MibTable
sonetPathDayTable=_SonetPathDayTable_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17))
if mibBuilder.loadTexts:sonetPathDayTable.setStatus(_A)
_SonetPathDayEntry_Object=MibTableRow
sonetPathDayEntry=_SonetPathDayEntry_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1))
sonetPathDayEntry.setIndexNames((0,_F,_G),(0,_E,_V))
if mibBuilder.loadTexts:sonetPathDayEntry.setStatus(_A)
class _SonetPathDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_SonetPathDayNumber_Type.__name__=_D
_SonetPathDayNumber_Object=MibTableColumn
sonetPathDayNumber=_SonetPathDayNumber_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,1),_SonetPathDayNumber_Type())
sonetPathDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayNumber.setStatus(_A)
_SonetPathDayStartTime_Type=DateAndTime
_SonetPathDayStartTime_Object=MibTableColumn
sonetPathDayStartTime=_SonetPathDayStartTime_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,2),_SonetPathDayStartTime_Type())
sonetPathDayStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayStartTime.setStatus(_A)
_SonetPathDayValidData_Type=TruthValue
_SonetPathDayValidData_Object=MibTableColumn
sonetPathDayValidData=_SonetPathDayValidData_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,3),_SonetPathDayValidData_Type())
sonetPathDayValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayValidData.setStatus(_A)
_SonetPathDayCVs_Type=PerfTotalCount
_SonetPathDayCVs_Object=MibTableColumn
sonetPathDayCVs=_SonetPathDayCVs_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,5),_SonetPathDayCVs_Type())
sonetPathDayCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayCVs.setStatus(_A)
_SonetPathDayESs_Type=PerfTotalCount
_SonetPathDayESs_Object=MibTableColumn
sonetPathDayESs=_SonetPathDayESs_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,6),_SonetPathDayESs_Type())
sonetPathDayESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayESs.setStatus(_A)
_SonetPathDaySESs_Type=PerfTotalCount
_SonetPathDaySESs_Object=MibTableColumn
sonetPathDaySESs=_SonetPathDaySESs_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,9),_SonetPathDaySESs_Type())
sonetPathDaySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDaySESs.setStatus(_A)
_SonetPathDayUASs_Type=PerfTotalCount
_SonetPathDayUASs_Object=MibTableColumn
sonetPathDayUASs=_SonetPathDayUASs_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,10),_SonetPathDayUASs_Type())
sonetPathDayUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayUASs.setStatus(_A)
_SonetPathDayFCs_Type=PerfTotalCount
_SonetPathDayFCs_Object=MibTableColumn
sonetPathDayFCs=_SonetPathDayFCs_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,11),_SonetPathDayFCs_Type())
sonetPathDayFCs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayFCs.setStatus(_A)
_SonetPathDayTcaFlag_Type=TruthValue
_SonetPathDayTcaFlag_Object=MibTableColumn
sonetPathDayTcaFlag=_SonetPathDayTcaFlag_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,12),_SonetPathDayTcaFlag_Type())
sonetPathDayTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayTcaFlag.setStatus(_A)
_SonetPathDayEBs_Type=PerfTotalCount
_SonetPathDayEBs_Object=MibTableColumn
sonetPathDayEBs=_SonetPathDayEBs_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,13),_SonetPathDayEBs_Type())
sonetPathDayEBs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetPathDayEBs.setStatus(_A)
_SonetPathDayReset_Type=Integer32
_SonetPathDayReset_Object=MibTableColumn
sonetPathDayReset=_SonetPathDayReset_Object((1,3,6,1,4,1,4515,1,6,3,2,1,17,1,14),_SonetPathDayReset_Type())
sonetPathDayReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetPathDayReset.setStatus(_A)
_SonetSupFarEndPath_ObjectIdentity=ObjectIdentity
sonetSupFarEndPath=_SonetSupFarEndPath_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,2,2))
_SonetFarEndPathDayTable_Object=MibTable
sonetFarEndPathDayTable=_SonetFarEndPathDayTable_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3))
if mibBuilder.loadTexts:sonetFarEndPathDayTable.setStatus(_A)
_SonetFarEndPathDayEntry_Object=MibTableRow
sonetFarEndPathDayEntry=_SonetFarEndPathDayEntry_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1))
sonetFarEndPathDayEntry.setIndexNames((0,_F,_G),(0,_E,_W))
if mibBuilder.loadTexts:sonetFarEndPathDayEntry.setStatus(_A)
class _SonetFarEndPathDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SonetFarEndPathDayNumber_Type.__name__=_D
_SonetFarEndPathDayNumber_Object=MibTableColumn
sonetFarEndPathDayNumber=_SonetFarEndPathDayNumber_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,1),_SonetFarEndPathDayNumber_Type())
sonetFarEndPathDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayNumber.setStatus(_A)
_SonetFarEndPathDayStartTime_Type=DateAndTime
_SonetFarEndPathDayStartTime_Object=MibTableColumn
sonetFarEndPathDayStartTime=_SonetFarEndPathDayStartTime_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,2),_SonetFarEndPathDayStartTime_Type())
sonetFarEndPathDayStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayStartTime.setStatus(_A)
_SonetFarEndPathDayValidData_Type=TruthValue
_SonetFarEndPathDayValidData_Object=MibTableColumn
sonetFarEndPathDayValidData=_SonetFarEndPathDayValidData_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,3),_SonetFarEndPathDayValidData_Type())
sonetFarEndPathDayValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayValidData.setStatus(_A)
_SonetFarEndPathDayCVs_Type=PerfTotalCount
_SonetFarEndPathDayCVs_Object=MibTableColumn
sonetFarEndPathDayCVs=_SonetFarEndPathDayCVs_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,5),_SonetFarEndPathDayCVs_Type())
sonetFarEndPathDayCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayCVs.setStatus(_A)
_SonetFarEndPathDayESs_Type=PerfTotalCount
_SonetFarEndPathDayESs_Object=MibTableColumn
sonetFarEndPathDayESs=_SonetFarEndPathDayESs_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,6),_SonetFarEndPathDayESs_Type())
sonetFarEndPathDayESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayESs.setStatus(_A)
_SonetFarEndPathDaySESs_Type=PerfTotalCount
_SonetFarEndPathDaySESs_Object=MibTableColumn
sonetFarEndPathDaySESs=_SonetFarEndPathDaySESs_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,9),_SonetFarEndPathDaySESs_Type())
sonetFarEndPathDaySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDaySESs.setStatus(_A)
_SonetFarEndPathDayUASs_Type=PerfTotalCount
_SonetFarEndPathDayUASs_Object=MibTableColumn
sonetFarEndPathDayUASs=_SonetFarEndPathDayUASs_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,10),_SonetFarEndPathDayUASs_Type())
sonetFarEndPathDayUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayUASs.setStatus(_A)
_SonetFarEndPathDayFCs_Type=PerfTotalCount
_SonetFarEndPathDayFCs_Object=MibTableColumn
sonetFarEndPathDayFCs=_SonetFarEndPathDayFCs_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,11),_SonetFarEndPathDayFCs_Type())
sonetFarEndPathDayFCs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayFCs.setStatus(_A)
_SonetFarEndPathDayTcaFlag_Type=TruthValue
_SonetFarEndPathDayTcaFlag_Object=MibTableColumn
sonetFarEndPathDayTcaFlag=_SonetFarEndPathDayTcaFlag_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,12),_SonetFarEndPathDayTcaFlag_Type())
sonetFarEndPathDayTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayTcaFlag.setStatus(_A)
_SonetFarEndPathDayEBs_Type=PerfTotalCount
_SonetFarEndPathDayEBs_Object=MibTableColumn
sonetFarEndPathDayEBs=_SonetFarEndPathDayEBs_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,13),_SonetFarEndPathDayEBs_Type())
sonetFarEndPathDayEBs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndPathDayEBs.setStatus(_A)
_SonetFarEndPathDayReset_Type=Integer32
_SonetFarEndPathDayReset_Object=MibTableColumn
sonetFarEndPathDayReset=_SonetFarEndPathDayReset_Object((1,3,6,1,4,1,4515,1,6,3,2,2,3,1,14),_SonetFarEndPathDayReset_Type())
sonetFarEndPathDayReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndPathDayReset.setStatus(_A)
_SonetSupObjectsVT_ObjectIdentity=ObjectIdentity
sonetSupObjectsVT=_SonetSupObjectsVT_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,3))
_SonetSupVT_ObjectIdentity=ObjectIdentity
sonetSupVT=_SonetSupVT_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,3,1))
_SonetVTDefaultThresholdTable_Object=MibTable
sonetVTDefaultThresholdTable=_SonetVTDefaultThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1))
if mibBuilder.loadTexts:sonetVTDefaultThresholdTable.setStatus(_A)
_SonetVTDefaultThresholdEntry_Object=MibTableRow
sonetVTDefaultThresholdEntry=_SonetVTDefaultThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1))
sonetVTDefaultThresholdEntry.setIndexNames((0,_E,_X),(0,_E,_Y))
if mibBuilder.loadTexts:sonetVTDefaultThresholdEntry.setStatus(_A)
class _SonetVTDefaultThresholdDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_SonetVTDefaultThresholdDirection_Type.__name__=_D
_SonetVTDefaultThresholdDirection_Object=MibTableColumn
sonetVTDefaultThresholdDirection=_SonetVTDefaultThresholdDirection_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,1),_SonetVTDefaultThresholdDirection_Type())
sonetVTDefaultThresholdDirection.setMaxAccess(_Z)
if mibBuilder.loadTexts:sonetVTDefaultThresholdDirection.setStatus(_A)
class _SonetVTDefaultThresholdRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),('vtg',2)))
_SonetVTDefaultThresholdRate_Type.__name__=_D
_SonetVTDefaultThresholdRate_Object=MibTableColumn
sonetVTDefaultThresholdRate=_SonetVTDefaultThresholdRate_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,2),_SonetVTDefaultThresholdRate_Type())
sonetVTDefaultThresholdRate.setMaxAccess(_Z)
if mibBuilder.loadTexts:sonetVTDefaultThresholdRate.setStatus(_A)
class _SonetVTDefaultCVThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16383))
_SonetVTDefaultCVThreshold_Type.__name__=_D
_SonetVTDefaultCVThreshold_Object=MibTableColumn
sonetVTDefaultCVThreshold=_SonetVTDefaultCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,3),_SonetVTDefaultCVThreshold_Type())
sonetVTDefaultCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultCVThreshold.setStatus(_A)
class _SonetVTDefaultESThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_SonetVTDefaultESThreshold_Type.__name__=_D
_SonetVTDefaultESThreshold_Object=MibTableColumn
sonetVTDefaultESThreshold=_SonetVTDefaultESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,4),_SonetVTDefaultESThreshold_Type())
sonetVTDefaultESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultESThreshold.setStatus(_A)
class _SonetVTDefaultSESThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_SonetVTDefaultSESThreshold_Type.__name__=_D
_SonetVTDefaultSESThreshold_Object=MibTableColumn
sonetVTDefaultSESThreshold=_SonetVTDefaultSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,5),_SonetVTDefaultSESThreshold_Type())
sonetVTDefaultSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultSESThreshold.setStatus(_A)
class _SonetVTDefaultUASThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,900))
_SonetVTDefaultUASThreshold_Type.__name__=_D
_SonetVTDefaultUASThreshold_Object=MibTableColumn
sonetVTDefaultUASThreshold=_SonetVTDefaultUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,6),_SonetVTDefaultUASThreshold_Type())
sonetVTDefaultUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultUASThreshold.setStatus(_A)
class _SonetVTDefaultDayCVThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1048575))
_SonetVTDefaultDayCVThreshold_Type.__name__=_D
_SonetVTDefaultDayCVThreshold_Object=MibTableColumn
sonetVTDefaultDayCVThreshold=_SonetVTDefaultDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,7),_SonetVTDefaultDayCVThreshold_Type())
sonetVTDefaultDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultDayCVThreshold.setStatus(_A)
class _SonetVTDefaultDayESThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SonetVTDefaultDayESThreshold_Type.__name__=_D
_SonetVTDefaultDayESThreshold_Object=MibTableColumn
sonetVTDefaultDayESThreshold=_SonetVTDefaultDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,8),_SonetVTDefaultDayESThreshold_Type())
sonetVTDefaultDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultDayESThreshold.setStatus(_A)
class _SonetVTDefaultDaySESThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SonetVTDefaultDaySESThreshold_Type.__name__=_D
_SonetVTDefaultDaySESThreshold_Object=MibTableColumn
sonetVTDefaultDaySESThreshold=_SonetVTDefaultDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,9),_SonetVTDefaultDaySESThreshold_Type())
sonetVTDefaultDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultDaySESThreshold.setStatus(_A)
class _SonetVTDefaultDayUASThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_SonetVTDefaultDayUASThreshold_Type.__name__=_D
_SonetVTDefaultDayUASThreshold_Object=MibTableColumn
sonetVTDefaultDayUASThreshold=_SonetVTDefaultDayUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,1,1,10),_SonetVTDefaultDayUASThreshold_Type())
sonetVTDefaultDayUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDefaultDayUASThreshold.setStatus(_A)
_SonetVTThresholdTable_Object=MibTable
sonetVTThresholdTable=_SonetVTThresholdTable_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2))
if mibBuilder.loadTexts:sonetVTThresholdTable.setStatus(_A)
_SonetVTThresholdEntry_Object=MibTableRow
sonetVTThresholdEntry=_SonetVTThresholdEntry_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1))
if mibBuilder.loadTexts:sonetVTThresholdEntry.setStatus(_A)
class _SonetVTCurrentCVThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_SonetVTCurrentCVThreshold_Type.__name__=_D
_SonetVTCurrentCVThreshold_Object=MibTableColumn
sonetVTCurrentCVThreshold=_SonetVTCurrentCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,1),_SonetVTCurrentCVThreshold_Type())
sonetVTCurrentCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentCVThreshold.setStatus(_A)
class _SonetVTCurrentESThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_SonetVTCurrentESThreshold_Type.__name__=_D
_SonetVTCurrentESThreshold_Object=MibTableColumn
sonetVTCurrentESThreshold=_SonetVTCurrentESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,2),_SonetVTCurrentESThreshold_Type())
sonetVTCurrentESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentESThreshold.setStatus(_A)
class _SonetVTCurrentSESThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_SonetVTCurrentSESThreshold_Type.__name__=_D
_SonetVTCurrentSESThreshold_Object=MibTableColumn
sonetVTCurrentSESThreshold=_SonetVTCurrentSESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,3),_SonetVTCurrentSESThreshold_Type())
sonetVTCurrentSESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentSESThreshold.setStatus(_A)
class _SonetVTCurrentUASThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,900))
_SonetVTCurrentUASThreshold_Type.__name__=_D
_SonetVTCurrentUASThreshold_Object=MibTableColumn
sonetVTCurrentUASThreshold=_SonetVTCurrentUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,4),_SonetVTCurrentUASThreshold_Type())
sonetVTCurrentUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTCurrentUASThreshold.setStatus(_A)
class _SonetVTDayCVThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SonetVTDayCVThreshold_Type.__name__=_D
_SonetVTDayCVThreshold_Object=MibTableColumn
sonetVTDayCVThreshold=_SonetVTDayCVThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,5),_SonetVTDayCVThreshold_Type())
sonetVTDayCVThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDayCVThreshold.setStatus(_A)
class _SonetVTDayESThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SonetVTDayESThreshold_Type.__name__=_D
_SonetVTDayESThreshold_Object=MibTableColumn
sonetVTDayESThreshold=_SonetVTDayESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,6),_SonetVTDayESThreshold_Type())
sonetVTDayESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDayESThreshold.setStatus(_A)
class _SonetVTDaySESThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SonetVTDaySESThreshold_Type.__name__=_D
_SonetVTDaySESThreshold_Object=MibTableColumn
sonetVTDaySESThreshold=_SonetVTDaySESThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,7),_SonetVTDaySESThreshold_Type())
sonetVTDaySESThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDaySESThreshold.setStatus(_A)
class _SonetVTDayUASThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SonetVTDayUASThreshold_Type.__name__=_D
_SonetVTDayUASThreshold_Object=MibTableColumn
sonetVTDayUASThreshold=_SonetVTDayUASThreshold_Object((1,3,6,1,4,1,4515,1,6,3,3,1,2,1,8),_SonetVTDayUASThreshold_Type())
sonetVTDayUASThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDayUASThreshold.setStatus(_A)
_SonetVTDayTable_Object=MibTable
sonetVTDayTable=_SonetVTDayTable_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17))
if mibBuilder.loadTexts:sonetVTDayTable.setStatus(_A)
_SonetVTDayEntry_Object=MibTableRow
sonetVTDayEntry=_SonetVTDayEntry_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1))
sonetVTDayEntry.setIndexNames((0,_F,_G),(0,_E,_a))
if mibBuilder.loadTexts:sonetVTDayEntry.setStatus(_A)
class _SonetVTDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,33))
_SonetVTDayNumber_Type.__name__=_D
_SonetVTDayNumber_Object=MibTableColumn
sonetVTDayNumber=_SonetVTDayNumber_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,1),_SonetVTDayNumber_Type())
sonetVTDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayNumber.setStatus(_A)
_SonetVTDayStartTime_Type=DateAndTime
_SonetVTDayStartTime_Object=MibTableColumn
sonetVTDayStartTime=_SonetVTDayStartTime_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,2),_SonetVTDayStartTime_Type())
sonetVTDayStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayStartTime.setStatus(_A)
_SonetVTDayValidData_Type=TruthValue
_SonetVTDayValidData_Object=MibTableColumn
sonetVTDayValidData=_SonetVTDayValidData_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,3),_SonetVTDayValidData_Type())
sonetVTDayValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayValidData.setStatus(_A)
_SonetVTDayFCs_Type=PerfTotalCount
_SonetVTDayFCs_Object=MibTableColumn
sonetVTDayFCs=_SonetVTDayFCs_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,4),_SonetVTDayFCs_Type())
sonetVTDayFCs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayFCs.setStatus(_A)
_SonetVTDayCVs_Type=PerfTotalCount
_SonetVTDayCVs_Object=MibTableColumn
sonetVTDayCVs=_SonetVTDayCVs_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,5),_SonetVTDayCVs_Type())
sonetVTDayCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayCVs.setStatus(_A)
_SonetVTDayESs_Type=PerfTotalCount
_SonetVTDayESs_Object=MibTableColumn
sonetVTDayESs=_SonetVTDayESs_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,6),_SonetVTDayESs_Type())
sonetVTDayESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayESs.setStatus(_A)
_SonetVTDaySESs_Type=PerfTotalCount
_SonetVTDaySESs_Object=MibTableColumn
sonetVTDaySESs=_SonetVTDaySESs_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,7),_SonetVTDaySESs_Type())
sonetVTDaySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDaySESs.setStatus(_A)
_SonetVTDayUASs_Type=PerfTotalCount
_SonetVTDayUASs_Object=MibTableColumn
sonetVTDayUASs=_SonetVTDayUASs_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,8),_SonetVTDayUASs_Type())
sonetVTDayUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayUASs.setStatus(_A)
_SonetVTDayEBs_Type=PerfTotalCount
_SonetVTDayEBs_Object=MibTableColumn
sonetVTDayEBs=_SonetVTDayEBs_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,9),_SonetVTDayEBs_Type())
sonetVTDayEBs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayEBs.setStatus(_A)
_SonetVTDayTcaFlag_Type=TruthValue
_SonetVTDayTcaFlag_Object=MibTableColumn
sonetVTDayTcaFlag=_SonetVTDayTcaFlag_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,10),_SonetVTDayTcaFlag_Type())
sonetVTDayTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetVTDayTcaFlag.setStatus(_A)
_SonetVTDayReset_Type=Integer32
_SonetVTDayReset_Object=MibTableColumn
sonetVTDayReset=_SonetVTDayReset_Object((1,3,6,1,4,1,4515,1,6,3,3,1,17,1,11),_SonetVTDayReset_Type())
sonetVTDayReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetVTDayReset.setStatus(_A)
_SonetSupFarEndVT_ObjectIdentity=ObjectIdentity
sonetSupFarEndVT=_SonetSupFarEndVT_ObjectIdentity((1,3,6,1,4,1,4515,1,6,3,3,2))
_SonetFarEndVTDayTable_Object=MibTable
sonetFarEndVTDayTable=_SonetFarEndVTDayTable_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3))
if mibBuilder.loadTexts:sonetFarEndVTDayTable.setStatus(_A)
_SonetFarEndVTDayEntry_Object=MibTableRow
sonetFarEndVTDayEntry=_SonetFarEndVTDayEntry_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1))
sonetFarEndVTDayEntry.setIndexNames((0,_F,_G),(0,_E,_b))
if mibBuilder.loadTexts:sonetFarEndVTDayEntry.setStatus(_A)
class _SonetFarEndVTDayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_SonetFarEndVTDayNumber_Type.__name__=_D
_SonetFarEndVTDayNumber_Object=MibTableColumn
sonetFarEndVTDayNumber=_SonetFarEndVTDayNumber_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,1),_SonetFarEndVTDayNumber_Type())
sonetFarEndVTDayNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayNumber.setStatus(_A)
_SonetFarEndVTDayStartTime_Type=DateAndTime
_SonetFarEndVTDayStartTime_Object=MibTableColumn
sonetFarEndVTDayStartTime=_SonetFarEndVTDayStartTime_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,2),_SonetFarEndVTDayStartTime_Type())
sonetFarEndVTDayStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayStartTime.setStatus(_A)
_SonetFarEndVTDayValidData_Type=TruthValue
_SonetFarEndVTDayValidData_Object=MibTableColumn
sonetFarEndVTDayValidData=_SonetFarEndVTDayValidData_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,3),_SonetFarEndVTDayValidData_Type())
sonetFarEndVTDayValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayValidData.setStatus(_A)
_SonetFarEndVTDayFCs_Type=PerfTotalCount
_SonetFarEndVTDayFCs_Object=MibTableColumn
sonetFarEndVTDayFCs=_SonetFarEndVTDayFCs_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,4),_SonetFarEndVTDayFCs_Type())
sonetFarEndVTDayFCs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayFCs.setStatus(_A)
_SonetFarEndVTDayCVs_Type=PerfTotalCount
_SonetFarEndVTDayCVs_Object=MibTableColumn
sonetFarEndVTDayCVs=_SonetFarEndVTDayCVs_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,5),_SonetFarEndVTDayCVs_Type())
sonetFarEndVTDayCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayCVs.setStatus(_A)
_SonetFarEndVTDayESs_Type=PerfTotalCount
_SonetFarEndVTDayESs_Object=MibTableColumn
sonetFarEndVTDayESs=_SonetFarEndVTDayESs_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,6),_SonetFarEndVTDayESs_Type())
sonetFarEndVTDayESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayESs.setStatus(_A)
_SonetFarEndVTDaySESs_Type=PerfTotalCount
_SonetFarEndVTDaySESs_Object=MibTableColumn
sonetFarEndVTDaySESs=_SonetFarEndVTDaySESs_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,7),_SonetFarEndVTDaySESs_Type())
sonetFarEndVTDaySESs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDaySESs.setStatus(_A)
_SonetFarEndVTDayUASs_Type=PerfTotalCount
_SonetFarEndVTDayUASs_Object=MibTableColumn
sonetFarEndVTDayUASs=_SonetFarEndVTDayUASs_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,8),_SonetFarEndVTDayUASs_Type())
sonetFarEndVTDayUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayUASs.setStatus(_A)
_SonetFarEndVTDayEBs_Type=PerfTotalCount
_SonetFarEndVTDayEBs_Object=MibTableColumn
sonetFarEndVTDayEBs=_SonetFarEndVTDayEBs_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,9),_SonetFarEndVTDayEBs_Type())
sonetFarEndVTDayEBs.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayEBs.setStatus(_A)
_SonetFarEndVTDayTcaFlag_Type=TruthValue
_SonetFarEndVTDayTcaFlag_Object=MibTableColumn
sonetFarEndVTDayTcaFlag=_SonetFarEndVTDayTcaFlag_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,10),_SonetFarEndVTDayTcaFlag_Type())
sonetFarEndVTDayTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:sonetFarEndVTDayTcaFlag.setStatus(_A)
_SonetFarEndVTDayReset_Type=Integer32
_SonetFarEndVTDayReset_Object=MibTableColumn
sonetFarEndVTDayReset=_SonetFarEndVTDayReset_Object((1,3,6,1,4,1,4515,1,6,3,3,2,3,1,11),_SonetFarEndVTDayReset_Type())
sonetFarEndVTDayReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sonetFarEndVTDayReset.setStatus(_A)
sonetSectionCurrentEntry.registerAugmentions((_E,_c))
sonetSectionThresholdEntry.setIndexNames(*sonetSectionCurrentEntry.getIndexNames())
sonetVTCurrentEntry.registerAugmentions((_E,_d))
sonetVTThresholdEntry.setIndexNames(*sonetVTCurrentEntry.getIndexNames())
sonetThresholdCrossing=NotificationType((1,3,6,1,4,1,4515,1,6,3,1,6,3))
sonetThresholdCrossing.setObjects(*((_E,_e),(_E,_f)))
if mibBuilder.loadTexts:sonetThresholdCrossing.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'sonetSupPmMIB':sonetSupPmMIB,'sonetSupObjects':sonetSupObjects,'sonetSupConfig':sonetSupConfig,'sonetSupMedium':sonetSupMedium,'sonetSupSection':sonetSupSection,'sonetSectionDefaultThresholdTable':sonetSectionDefaultThresholdTable,'sonetSectionDefaultThresholdEntry':sonetSectionDefaultThresholdEntry,_J:sonetSectionDefaultThresholdRate,'sonetSectionDefaultCVThreshold':sonetSectionDefaultCVThreshold,'sonetSectionDefaultESThreshold':sonetSectionDefaultESThreshold,'sonetSectionDefaultSESThreshold':sonetSectionDefaultSESThreshold,'sonetSectionDefaultSEFSThreshold':sonetSectionDefaultSEFSThreshold,'sonetSectionDefaultDayCVThreshold':sonetSectionDefaultDayCVThreshold,'sonetSectionDefaultDayESThreshold':sonetSectionDefaultDayESThreshold,'sonetSectionDefaultDaySESThreshold':sonetSectionDefaultDaySESThreshold,'sonetSectionDefaultDaySEFSThreshold':sonetSectionDefaultDaySEFSThreshold,'sonetSectionThresholdTable':sonetSectionThresholdTable,_c:sonetSectionThresholdEntry,'sonetSectionCurrentCVThreshold':sonetSectionCurrentCVThreshold,'sonetSectionCurrentESThreshold':sonetSectionCurrentESThreshold,'sonetSectionCurrentSESThreshold':sonetSectionCurrentSESThreshold,'sonetSectionCurrentSEFSThreshold':sonetSectionCurrentSEFSThreshold,'sonetSectionDayCVThreshold':sonetSectionDayCVThreshold,'sonetSectionDayESThreshold':sonetSectionDayESThreshold,'sonetSectionDaySESThreshold':sonetSectionDaySESThreshold,'sonetSectionDaySEFSThreshold':sonetSectionDaySEFSThreshold,'sonetSectionDayTable':sonetSectionDayTable,'sonetSectionDayEntry':sonetSectionDayEntry,_K:sonetSectionDayNumber,'sonetSectionDayStartTime':sonetSectionDayStartTime,'sonetSectionDayValidData':sonetSectionDayValidData,'sonetSectionDayCVs':sonetSectionDayCVs,'sonetSectionDayESs':sonetSectionDayESs,'sonetSectionDaySESs':sonetSectionDaySESs,'sonetSectionDaySEFSs':sonetSectionDaySEFSs,'sonetSectionDayTcaFlag':sonetSectionDayTcaFlag,'sonetSectionDayReset':sonetSectionDayReset,'sonetSupLine':sonetSupLine,'sonetLineDefaultThresholdTable':sonetLineDefaultThresholdTable,'sonetLineDefaultThresholdEntry':sonetLineDefaultThresholdEntry,_L:sonetLineDefaultThresholdDirection,_M:sonetLineDefaultThresholdRate,'sonetLineDefaultCVThreshold':sonetLineDefaultCVThreshold,'sonetLineDefaultESThreshold':sonetLineDefaultESThreshold,'sonetLineDefaultSESThreshold':sonetLineDefaultSESThreshold,'sonetLineDefaultUASThreshold':sonetLineDefaultUASThreshold,'sonetLineDefaultDayCVThreshold':sonetLineDefaultDayCVThreshold,'sonetLineDefaultDayESThreshold':sonetLineDefaultDayESThreshold,'sonetLineDefaultDaySESThreshold':sonetLineDefaultDaySESThreshold,'sonetLineDefaultDayUASThreshold':sonetLineDefaultDayUASThreshold,'sonetLineThresholdTable':sonetLineThresholdTable,'sonetLineThresholdEntry':sonetLineThresholdEntry,_O:sonetLineThresholdDirection,'sonetLineCurrentCVThreshold':sonetLineCurrentCVThreshold,'sonetLineCurrentESThreshold':sonetLineCurrentESThreshold,'sonetLineCurrentSESThreshold':sonetLineCurrentSESThreshold,'sonetLineCurrentUASThreshold':sonetLineCurrentUASThreshold,'sonetLineDayCVThreshold':sonetLineDayCVThreshold,'sonetLineDayESThreshold':sonetLineDayESThreshold,'sonetLineDaySESThreshold':sonetLineDaySESThreshold,'sonetLineDayUASThreshold':sonetLineDayUASThreshold,'sonetLineDayTable':sonetLineDayTable,'sonetLineDayEntry':sonetLineDayEntry,_P:sonetLineDayNumber,'sonetLineDayStartTime':sonetLineDayStartTime,'sonetLineDayValidData':sonetLineDayValidData,'sonetLineDayCVs':sonetLineDayCVs,'sonetLineDayESs':sonetLineDayESs,'sonetLineDaySESs':sonetLineDaySESs,'sonetLineDayUASs':sonetLineDayUASs,'sonetLineDayPSC':sonetLineDayPSC,'sonetLineDayPSD':sonetLineDayPSD,'sonetLineDayFCs':sonetLineDayFCs,'sonetLineDayTcaFlag':sonetLineDayTcaFlag,'sonetLineDayReset':sonetLineDayReset,'sonetSupFarEndLine':sonetSupFarEndLine,'sonetFarEndLineDayTable':sonetFarEndLineDayTable,'sonetFarEndLineDayEntry':sonetFarEndLineDayEntry,_Q:sonetFarEndLineDayNumber,'sonetFarEndLineDayStartTime':sonetFarEndLineDayStartTime,'sonetFarEndLineDayValidData':sonetFarEndLineDayValidData,'sonetFarEndLineDayCVs':sonetFarEndLineDayCVs,'sonetFarEndLineDayESs':sonetFarEndLineDayESs,'sonetFarEndLineDaySESs':sonetFarEndLineDaySESs,'sonetFarEndLineDayUASs':sonetFarEndLineDayUASs,'sonetFarEndLineDayFCs':sonetFarEndLineDayFCs,'sonetFarEndLineDayTcaFlag':sonetFarEndLineDayTcaFlag,'sonetFarEndLineDayReset':sonetFarEndLineDayReset,'sonetTrap':sonetTrap,_e:sonetCounterId,_f:sonetCounterValue,'sonetThresholdCrossing':sonetThresholdCrossing,'sonetSupObjectsPath':sonetSupObjectsPath,'sonetSupPath':sonetSupPath,'sonetPathDefaultThresholdTable':sonetPathDefaultThresholdTable,'sonetPathDefaultThresholdEntry':sonetPathDefaultThresholdEntry,_S:sonetPathDefaultThresholdDirection,_T:sonetPathDefaultThresholdRate,'sonetPathDefaultCVThreshold':sonetPathDefaultCVThreshold,'sonetPathDefaultESThreshold':sonetPathDefaultESThreshold,'sonetPathDefaultSESThreshold':sonetPathDefaultSESThreshold,'sonetPathDefaultUASThreshold':sonetPathDefaultUASThreshold,'sonetPathDefaultDayCVThreshold':sonetPathDefaultDayCVThreshold,'sonetPathDefaultDayESThreshold':sonetPathDefaultDayESThreshold,'sonetPathDefaultDaySESThreshold':sonetPathDefaultDaySESThreshold,'sonetPathDefaultDayUASThreshold':sonetPathDefaultDayUASThreshold,'sonetPathThresholdTable':sonetPathThresholdTable,'sonetPathThresholdEntry':sonetPathThresholdEntry,_U:sonetPathThresholdDirection,'sonetPathCurrentCVThreshold':sonetPathCurrentCVThreshold,'sonetPathCurrentESThreshold':sonetPathCurrentESThreshold,'sonetPathCurrentSESThreshold':sonetPathCurrentSESThreshold,'sonetPathCurrentUASThreshold':sonetPathCurrentUASThreshold,'sonetPathDayCVThreshold':sonetPathDayCVThreshold,'sonetPathDayESThreshold':sonetPathDayESThreshold,'sonetPathDaySESThreshold':sonetPathDaySESThreshold,'sonetPathDayUASThreshold':sonetPathDayUASThreshold,'sonetPathDayTable':sonetPathDayTable,'sonetPathDayEntry':sonetPathDayEntry,_V:sonetPathDayNumber,'sonetPathDayStartTime':sonetPathDayStartTime,'sonetPathDayValidData':sonetPathDayValidData,'sonetPathDayCVs':sonetPathDayCVs,'sonetPathDayESs':sonetPathDayESs,'sonetPathDaySESs':sonetPathDaySESs,'sonetPathDayUASs':sonetPathDayUASs,'sonetPathDayFCs':sonetPathDayFCs,'sonetPathDayTcaFlag':sonetPathDayTcaFlag,'sonetPathDayEBs':sonetPathDayEBs,'sonetPathDayReset':sonetPathDayReset,'sonetSupFarEndPath':sonetSupFarEndPath,'sonetFarEndPathDayTable':sonetFarEndPathDayTable,'sonetFarEndPathDayEntry':sonetFarEndPathDayEntry,_W:sonetFarEndPathDayNumber,'sonetFarEndPathDayStartTime':sonetFarEndPathDayStartTime,'sonetFarEndPathDayValidData':sonetFarEndPathDayValidData,'sonetFarEndPathDayCVs':sonetFarEndPathDayCVs,'sonetFarEndPathDayESs':sonetFarEndPathDayESs,'sonetFarEndPathDaySESs':sonetFarEndPathDaySESs,'sonetFarEndPathDayUASs':sonetFarEndPathDayUASs,'sonetFarEndPathDayFCs':sonetFarEndPathDayFCs,'sonetFarEndPathDayTcaFlag':sonetFarEndPathDayTcaFlag,'sonetFarEndPathDayEBs':sonetFarEndPathDayEBs,'sonetFarEndPathDayReset':sonetFarEndPathDayReset,'sonetSupObjectsVT':sonetSupObjectsVT,'sonetSupVT':sonetSupVT,'sonetVTDefaultThresholdTable':sonetVTDefaultThresholdTable,'sonetVTDefaultThresholdEntry':sonetVTDefaultThresholdEntry,_X:sonetVTDefaultThresholdDirection,_Y:sonetVTDefaultThresholdRate,'sonetVTDefaultCVThreshold':sonetVTDefaultCVThreshold,'sonetVTDefaultESThreshold':sonetVTDefaultESThreshold,'sonetVTDefaultSESThreshold':sonetVTDefaultSESThreshold,'sonetVTDefaultUASThreshold':sonetVTDefaultUASThreshold,'sonetVTDefaultDayCVThreshold':sonetVTDefaultDayCVThreshold,'sonetVTDefaultDayESThreshold':sonetVTDefaultDayESThreshold,'sonetVTDefaultDaySESThreshold':sonetVTDefaultDaySESThreshold,'sonetVTDefaultDayUASThreshold':sonetVTDefaultDayUASThreshold,'sonetVTThresholdTable':sonetVTThresholdTable,_d:sonetVTThresholdEntry,'sonetVTCurrentCVThreshold':sonetVTCurrentCVThreshold,'sonetVTCurrentESThreshold':sonetVTCurrentESThreshold,'sonetVTCurrentSESThreshold':sonetVTCurrentSESThreshold,'sonetVTCurrentUASThreshold':sonetVTCurrentUASThreshold,'sonetVTDayCVThreshold':sonetVTDayCVThreshold,'sonetVTDayESThreshold':sonetVTDayESThreshold,'sonetVTDaySESThreshold':sonetVTDaySESThreshold,'sonetVTDayUASThreshold':sonetVTDayUASThreshold,'sonetVTDayTable':sonetVTDayTable,'sonetVTDayEntry':sonetVTDayEntry,_a:sonetVTDayNumber,'sonetVTDayStartTime':sonetVTDayStartTime,'sonetVTDayValidData':sonetVTDayValidData,'sonetVTDayFCs':sonetVTDayFCs,'sonetVTDayCVs':sonetVTDayCVs,'sonetVTDayESs':sonetVTDayESs,'sonetVTDaySESs':sonetVTDaySESs,'sonetVTDayUASs':sonetVTDayUASs,'sonetVTDayEBs':sonetVTDayEBs,'sonetVTDayTcaFlag':sonetVTDayTcaFlag,'sonetVTDayReset':sonetVTDayReset,'sonetSupFarEndVT':sonetSupFarEndVT,'sonetFarEndVTDayTable':sonetFarEndVTDayTable,'sonetFarEndVTDayEntry':sonetFarEndVTDayEntry,_b:sonetFarEndVTDayNumber,'sonetFarEndVTDayStartTime':sonetFarEndVTDayStartTime,'sonetFarEndVTDayValidData':sonetFarEndVTDayValidData,'sonetFarEndVTDayFCs':sonetFarEndVTDayFCs,'sonetFarEndVTDayCVs':sonetFarEndVTDayCVs,'sonetFarEndVTDayESs':sonetFarEndVTDayESs,'sonetFarEndVTDaySESs':sonetFarEndVTDaySESs,'sonetFarEndVTDayUASs':sonetFarEndVTDayUASs,'sonetFarEndVTDayEBs':sonetFarEndVTDayEBs,'sonetFarEndVTDayTcaFlag':sonetFarEndVTDayTcaFlag,'sonetFarEndVTDayReset':sonetFarEndVTDayReset})