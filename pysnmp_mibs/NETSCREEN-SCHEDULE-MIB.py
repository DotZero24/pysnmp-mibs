_G='nsSchRecurIndex'
_F='nsSchOnceIndex'
_E='NETSCREEN-SCHEDULE-MIB'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSchedule,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSchedule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
netscreenScheduleMibModule=ModuleIdentity((1,3,6,1,4,1,3224,14,0))
if mibBuilder.loadTexts:netscreenScheduleMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-10 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSchOnceTable_Object=MibTable
nsSchOnceTable=_NsSchOnceTable_Object((1,3,6,1,4,1,3224,14,1))
if mibBuilder.loadTexts:nsSchOnceTable.setStatus(_A)
_NsSchOnceEntry_Object=MibTableRow
nsSchOnceEntry=_NsSchOnceEntry_Object((1,3,6,1,4,1,3224,14,1,1))
nsSchOnceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nsSchOnceEntry.setStatus(_A)
class _NsSchOnceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSchOnceIndex_Type.__name__=_D
_NsSchOnceIndex_Object=MibTableColumn
nsSchOnceIndex=_NsSchOnceIndex_Object((1,3,6,1,4,1,3224,14,1,1,1),_NsSchOnceIndex_Type())
nsSchOnceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchOnceIndex.setStatus(_A)
class _NsSchOnceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchOnceName_Type.__name__=_C
_NsSchOnceName_Object=MibTableColumn
nsSchOnceName=_NsSchOnceName_Object((1,3,6,1,4,1,3224,14,1,1,2),_NsSchOnceName_Type())
nsSchOnceName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchOnceName.setStatus(_A)
class _NsSchOnceStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchOnceStartTime_Type.__name__=_C
_NsSchOnceStartTime_Object=MibTableColumn
nsSchOnceStartTime=_NsSchOnceStartTime_Object((1,3,6,1,4,1,3224,14,1,1,3),_NsSchOnceStartTime_Type())
nsSchOnceStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchOnceStartTime.setStatus(_A)
class _NsSchOnceStopTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchOnceStopTime_Type.__name__=_C
_NsSchOnceStopTime_Object=MibTableColumn
nsSchOnceStopTime=_NsSchOnceStopTime_Object((1,3,6,1,4,1,3224,14,1,1,4),_NsSchOnceStopTime_Type())
nsSchOnceStopTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchOnceStopTime.setStatus(_A)
class _NsSchOnceComments_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchOnceComments_Type.__name__=_C
_NsSchOnceComments_Object=MibTableColumn
nsSchOnceComments=_NsSchOnceComments_Object((1,3,6,1,4,1,3224,14,1,1,5),_NsSchOnceComments_Type())
nsSchOnceComments.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchOnceComments.setStatus(_A)
class _NsSchOnceVsys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSchOnceVsys_Type.__name__=_D
_NsSchOnceVsys_Object=MibTableColumn
nsSchOnceVsys=_NsSchOnceVsys_Object((1,3,6,1,4,1,3224,14,1,1,6),_NsSchOnceVsys_Type())
nsSchOnceVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchOnceVsys.setStatus(_A)
_NsSchRecurTable_Object=MibTable
nsSchRecurTable=_NsSchRecurTable_Object((1,3,6,1,4,1,3224,14,2))
if mibBuilder.loadTexts:nsSchRecurTable.setStatus(_A)
_NsSchRecurEntry_Object=MibTableRow
nsSchRecurEntry=_NsSchRecurEntry_Object((1,3,6,1,4,1,3224,14,2,1))
nsSchRecurEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:nsSchRecurEntry.setStatus(_A)
class _NsSchRecurIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSchRecurIndex_Type.__name__=_D
_NsSchRecurIndex_Object=MibTableColumn
nsSchRecurIndex=_NsSchRecurIndex_Object((1,3,6,1,4,1,3224,14,2,1,1),_NsSchRecurIndex_Type())
nsSchRecurIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurIndex.setStatus(_A)
class _NsSchRecurName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchRecurName_Type.__name__=_C
_NsSchRecurName_Object=MibTableColumn
nsSchRecurName=_NsSchRecurName_Object((1,3,6,1,4,1,3224,14,2,1,2),_NsSchRecurName_Type())
nsSchRecurName.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurName.setStatus(_A)
class _NsSchRecurWeekday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('sun',0),('mon',1),('tue',2),('wed',3),('thu',4),('fri',5),('sat',6)))
_NsSchRecurWeekday_Type.__name__=_D
_NsSchRecurWeekday_Object=MibTableColumn
nsSchRecurWeekday=_NsSchRecurWeekday_Object((1,3,6,1,4,1,3224,14,2,1,3),_NsSchRecurWeekday_Type())
nsSchRecurWeekday.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurWeekday.setStatus(_A)
class _NsSchRecurStartTime1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchRecurStartTime1_Type.__name__=_C
_NsSchRecurStartTime1_Object=MibTableColumn
nsSchRecurStartTime1=_NsSchRecurStartTime1_Object((1,3,6,1,4,1,3224,14,2,1,4),_NsSchRecurStartTime1_Type())
nsSchRecurStartTime1.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurStartTime1.setStatus(_A)
class _NsSchRecurStopTime1_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchRecurStopTime1_Type.__name__=_C
_NsSchRecurStopTime1_Object=MibTableColumn
nsSchRecurStopTime1=_NsSchRecurStopTime1_Object((1,3,6,1,4,1,3224,14,2,1,5),_NsSchRecurStopTime1_Type())
nsSchRecurStopTime1.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurStopTime1.setStatus(_A)
class _NsSchRecurStartTime2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchRecurStartTime2_Type.__name__=_C
_NsSchRecurStartTime2_Object=MibTableColumn
nsSchRecurStartTime2=_NsSchRecurStartTime2_Object((1,3,6,1,4,1,3224,14,2,1,6),_NsSchRecurStartTime2_Type())
nsSchRecurStartTime2.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurStartTime2.setStatus(_A)
class _NsSchRecurStopTime2_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NsSchRecurStopTime2_Type.__name__=_C
_NsSchRecurStopTime2_Object=MibTableColumn
nsSchRecurStopTime2=_NsSchRecurStopTime2_Object((1,3,6,1,4,1,3224,14,2,1,7),_NsSchRecurStopTime2_Type())
nsSchRecurStopTime2.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurStopTime2.setStatus(_A)
class _NsSchRecurComments_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NsSchRecurComments_Type.__name__=_C
_NsSchRecurComments_Object=MibTableColumn
nsSchRecurComments=_NsSchRecurComments_Object((1,3,6,1,4,1,3224,14,2,1,8),_NsSchRecurComments_Type())
nsSchRecurComments.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurComments.setStatus(_A)
class _NsSchRecurVsys_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NsSchRecurVsys_Type.__name__=_D
_NsSchRecurVsys_Object=MibTableColumn
nsSchRecurVsys=_NsSchRecurVsys_Object((1,3,6,1,4,1,3224,14,2,1,9),_NsSchRecurVsys_Type())
nsSchRecurVsys.setMaxAccess(_B)
if mibBuilder.loadTexts:nsSchRecurVsys.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'netscreenScheduleMibModule':netscreenScheduleMibModule,'nsSchOnceTable':nsSchOnceTable,'nsSchOnceEntry':nsSchOnceEntry,_F:nsSchOnceIndex,'nsSchOnceName':nsSchOnceName,'nsSchOnceStartTime':nsSchOnceStartTime,'nsSchOnceStopTime':nsSchOnceStopTime,'nsSchOnceComments':nsSchOnceComments,'nsSchOnceVsys':nsSchOnceVsys,'nsSchRecurTable':nsSchRecurTable,'nsSchRecurEntry':nsSchRecurEntry,_G:nsSchRecurIndex,'nsSchRecurName':nsSchRecurName,'nsSchRecurWeekday':nsSchRecurWeekday,'nsSchRecurStartTime1':nsSchRecurStartTime1,'nsSchRecurStopTime1':nsSchRecurStopTime1,'nsSchRecurStartTime2':nsSchRecurStartTime2,'nsSchRecurStopTime2':nsSchRecurStopTime2,'nsSchRecurComments':nsSchRecurComments,'nsSchRecurVsys':nsSchRecurVsys})