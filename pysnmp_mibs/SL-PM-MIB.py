_O='slPmL2IntervalNumber'
_N='slPmL2IntervalType'
_M='slPmL2CounterType'
_L='read-write'
_K='slPmIntervalNumber'
_J='slPmIntervalType'
_I='slPmDirectionType'
_H='slPmType'
_G='Integer32'
_F='ifIndex'
_E='IF-MIB'
_D='not-accessible'
_C='SL-PM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
XpdrServiceType,=mibBuilder.importSymbols('SL-XPDR-MIB','XpdrServiceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
slPmMib=ModuleIdentity((1,3,6,1,4,1,4515,1,3,25))
class SlPmType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('native',1))
class SlPmL2Type(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('crc',1),('rxPackets',2),('txPackets',3),('rxBytes',4),('txBytes',5)))
class SlPmDirectionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('near',1),('far',2)))
class SlPmIntervalType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fifteen',1),('day',2)))
_SlPmIntervals_ObjectIdentity=ObjectIdentity
slPmIntervals=_SlPmIntervals_ObjectIdentity((1,3,6,1,4,1,4515,1,3,25,1))
_SlPmIntervalTable_Object=MibTable
slPmIntervalTable=_SlPmIntervalTable_Object((1,3,6,1,4,1,4515,1,3,25,1,1))
if mibBuilder.loadTexts:slPmIntervalTable.setStatus(_A)
_SlPmIntervalEntry_Object=MibTableRow
slPmIntervalEntry=_SlPmIntervalEntry_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1))
slPmIntervalEntry.setIndexNames((0,_E,_F),(0,_C,_H),(0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:slPmIntervalEntry.setStatus(_A)
_SlPmType_Type=SlPmType
_SlPmType_Object=MibTableColumn
slPmType=_SlPmType_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,1),_SlPmType_Type())
slPmType.setMaxAccess(_D)
if mibBuilder.loadTexts:slPmType.setStatus(_A)
_SlPmDirectionType_Type=SlPmDirectionType
_SlPmDirectionType_Object=MibTableColumn
slPmDirectionType=_SlPmDirectionType_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,2),_SlPmDirectionType_Type())
slPmDirectionType.setMaxAccess(_D)
if mibBuilder.loadTexts:slPmDirectionType.setStatus(_A)
_SlPmIntervalType_Type=SlPmIntervalType
_SlPmIntervalType_Object=MibTableColumn
slPmIntervalType=_SlPmIntervalType_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,3),_SlPmIntervalType_Type())
slPmIntervalType.setMaxAccess(_D)
if mibBuilder.loadTexts:slPmIntervalType.setStatus(_A)
class _SlPmIntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_SlPmIntervalNumber_Type.__name__=_G
_SlPmIntervalNumber_Object=MibTableColumn
slPmIntervalNumber=_SlPmIntervalNumber_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,4),_SlPmIntervalNumber_Type())
slPmIntervalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:slPmIntervalNumber.setStatus(_A)
_SlPmIntervalCVs_Type=PerfIntervalCount
_SlPmIntervalCVs_Object=MibTableColumn
slPmIntervalCVs=_SlPmIntervalCVs_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,5),_SlPmIntervalCVs_Type())
slPmIntervalCVs.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalCVs.setStatus(_A)
_SlPmIntervalESs_Type=PerfIntervalCount
_SlPmIntervalESs_Object=MibTableColumn
slPmIntervalESs=_SlPmIntervalESs_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,6),_SlPmIntervalESs_Type())
slPmIntervalESs.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalESs.setStatus(_A)
_SlPmIntervalSESs_Type=PerfIntervalCount
_SlPmIntervalSESs_Object=MibTableColumn
slPmIntervalSESs=_SlPmIntervalSESs_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,7),_SlPmIntervalSESs_Type())
slPmIntervalSESs.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalSESs.setStatus(_A)
_SlPmIntervalSEFSs_Type=PerfIntervalCount
_SlPmIntervalSEFSs_Object=MibTableColumn
slPmIntervalSEFSs=_SlPmIntervalSEFSs_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,8),_SlPmIntervalSEFSs_Type())
slPmIntervalSEFSs.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalSEFSs.setStatus(_A)
_SlPmIntervalUASs_Type=PerfIntervalCount
_SlPmIntervalUASs_Object=MibTableColumn
slPmIntervalUASs=_SlPmIntervalUASs_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,9),_SlPmIntervalUASs_Type())
slPmIntervalUASs.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalUASs.setStatus(_A)
_SlPmIntervalValidData_Type=TruthValue
_SlPmIntervalValidData_Object=MibTableColumn
slPmIntervalValidData=_SlPmIntervalValidData_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,10),_SlPmIntervalValidData_Type())
slPmIntervalValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalValidData.setStatus(_A)
_SlPmIntervalTcaFlag_Type=TruthValue
_SlPmIntervalTcaFlag_Object=MibTableColumn
slPmIntervalTcaFlag=_SlPmIntervalTcaFlag_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,11),_SlPmIntervalTcaFlag_Type())
slPmIntervalTcaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalTcaFlag.setStatus(_A)
_SlPmIntervalReset_Type=Integer32
_SlPmIntervalReset_Object=MibTableColumn
slPmIntervalReset=_SlPmIntervalReset_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,12),_SlPmIntervalReset_Type())
slPmIntervalReset.setMaxAccess(_L)
if mibBuilder.loadTexts:slPmIntervalReset.setStatus(_A)
_SlPmIntervalStartTime_Type=DateAndTime
_SlPmIntervalStartTime_Object=MibTableColumn
slPmIntervalStartTime=_SlPmIntervalStartTime_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,13),_SlPmIntervalStartTime_Type())
slPmIntervalStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmIntervalStartTime.setStatus(_A)
_SlPmServiceType_Type=XpdrServiceType
_SlPmServiceType_Object=MibTableColumn
slPmServiceType=_SlPmServiceType_Object((1,3,6,1,4,1,4515,1,3,25,1,1,1,14),_SlPmServiceType_Type())
slPmServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmServiceType.setStatus(_A)
_SlPmL2Intervals_ObjectIdentity=ObjectIdentity
slPmL2Intervals=_SlPmL2Intervals_ObjectIdentity((1,3,6,1,4,1,4515,1,3,25,2))
_SlPmL2Table_Object=MibTable
slPmL2Table=_SlPmL2Table_Object((1,3,6,1,4,1,4515,1,3,25,2,1))
if mibBuilder.loadTexts:slPmL2Table.setStatus(_A)
_SlPmL2Entry_Object=MibTableRow
slPmL2Entry=_SlPmL2Entry_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1))
slPmL2Entry.setIndexNames((0,_E,_F),(0,_C,_M),(0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:slPmL2Entry.setStatus(_A)
_SlPmL2CounterType_Type=SlPmL2Type
_SlPmL2CounterType_Object=MibTableColumn
slPmL2CounterType=_SlPmL2CounterType_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,1),_SlPmL2CounterType_Type())
slPmL2CounterType.setMaxAccess(_D)
if mibBuilder.loadTexts:slPmL2CounterType.setStatus(_A)
_SlPmL2IntervalType_Type=SlPmIntervalType
_SlPmL2IntervalType_Object=MibTableColumn
slPmL2IntervalType=_SlPmL2IntervalType_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,2),_SlPmL2IntervalType_Type())
slPmL2IntervalType.setMaxAccess(_D)
if mibBuilder.loadTexts:slPmL2IntervalType.setStatus(_A)
class _SlPmL2IntervalNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,96))
_SlPmL2IntervalNumber_Type.__name__=_G
_SlPmL2IntervalNumber_Object=MibTableColumn
slPmL2IntervalNumber=_SlPmL2IntervalNumber_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,3),_SlPmL2IntervalNumber_Type())
slPmL2IntervalNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:slPmL2IntervalNumber.setStatus(_A)
_SlPmL2Count_Type=Counter64
_SlPmL2Count_Object=MibTableColumn
slPmL2Count=_SlPmL2Count_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,4),_SlPmL2Count_Type())
slPmL2Count.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmL2Count.setStatus(_A)
_SlPmL2ValidData_Type=TruthValue
_SlPmL2ValidData_Object=MibTableColumn
slPmL2ValidData=_SlPmL2ValidData_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,5),_SlPmL2ValidData_Type())
slPmL2ValidData.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmL2ValidData.setStatus(_A)
_SlPmL2Reset_Type=Integer32
_SlPmL2Reset_Object=MibTableColumn
slPmL2Reset=_SlPmL2Reset_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,6),_SlPmL2Reset_Type())
slPmL2Reset.setMaxAccess(_L)
if mibBuilder.loadTexts:slPmL2Reset.setStatus(_A)
_SlPmL2StartTime_Type=DateAndTime
_SlPmL2StartTime_Object=MibTableColumn
slPmL2StartTime=_SlPmL2StartTime_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,7),_SlPmL2StartTime_Type())
slPmL2StartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmL2StartTime.setStatus(_A)
_SlPmL2ServiceType_Type=XpdrServiceType
_SlPmL2ServiceType_Object=MibTableColumn
slPmL2ServiceType=_SlPmL2ServiceType_Object((1,3,6,1,4,1,4515,1,3,25,2,1,1,8),_SlPmL2ServiceType_Type())
slPmL2ServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:slPmL2ServiceType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'SlPmType':SlPmType,'SlPmL2Type':SlPmL2Type,'SlPmDirectionType':SlPmDirectionType,'SlPmIntervalType':SlPmIntervalType,'slPmMib':slPmMib,'slPmIntervals':slPmIntervals,'slPmIntervalTable':slPmIntervalTable,'slPmIntervalEntry':slPmIntervalEntry,_H:slPmType,_I:slPmDirectionType,_J:slPmIntervalType,_K:slPmIntervalNumber,'slPmIntervalCVs':slPmIntervalCVs,'slPmIntervalESs':slPmIntervalESs,'slPmIntervalSESs':slPmIntervalSESs,'slPmIntervalSEFSs':slPmIntervalSEFSs,'slPmIntervalUASs':slPmIntervalUASs,'slPmIntervalValidData':slPmIntervalValidData,'slPmIntervalTcaFlag':slPmIntervalTcaFlag,'slPmIntervalReset':slPmIntervalReset,'slPmIntervalStartTime':slPmIntervalStartTime,'slPmServiceType':slPmServiceType,'slPmL2Intervals':slPmL2Intervals,'slPmL2Table':slPmL2Table,'slPmL2Entry':slPmL2Entry,_M:slPmL2CounterType,_N:slPmL2IntervalType,_O:slPmL2IntervalNumber,'slPmL2Count':slPmL2Count,'slPmL2ValidData':slPmL2ValidData,'slPmL2Reset':slPmL2Reset,'slPmL2StartTime':slPmL2StartTime,'slPmL2ServiceType':slPmL2ServiceType})