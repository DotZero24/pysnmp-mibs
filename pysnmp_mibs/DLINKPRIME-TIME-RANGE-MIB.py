_X='dpTimeRangeProfileCfgGroup'
_W='dpTimeRangeProfileRowStatus'
_V='notApplicable'
_U='saturday'
_T='friday'
_S='thursday'
_R='wednesday'
_Q='tuesday'
_P='monday'
_O='sunday'
_N='dpTimeRangeProfileEndMinute'
_M='dpTimeRangeProfileEndHour'
_L='dpTimeRangeProfileEndDayOfWeek'
_K='dpTimeRangeProfileStartMinute'
_J='dpTimeRangeProfileStartHour'
_I='dpTimeRangeProfileStartDayOfWeek'
_H='dpTimeRangeProfilePeriodType'
_G='dpTimeRangeProfileName'
_F='DisplayString'
_E='Integer32'
_D='Unsigned32'
_C='not-accessible'
_B='DLINKPRIME-TIME-RANGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlinkPrimeCommon,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlinkPrimeCommon')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
dlinkPrimeTimeRangeMIB=ModuleIdentity((1,3,6,1,4,1,171,15,24))
if mibBuilder.loadTexts:dlinkPrimeTimeRangeMIB.setRevisions(('2014-04-26 00:00',))
_DpTimeRangeMIBNotifications_ObjectIdentity=ObjectIdentity
dpTimeRangeMIBNotifications=_DpTimeRangeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,171,15,24,0))
_DpTimeRangeMIBObjects_ObjectIdentity=ObjectIdentity
dpTimeRangeMIBObjects=_DpTimeRangeMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,15,24,1))
_DpTimeRangeProfileTable_Object=MibTable
dpTimeRangeProfileTable=_DpTimeRangeProfileTable_Object((1,3,6,1,4,1,171,15,24,1,1))
if mibBuilder.loadTexts:dpTimeRangeProfileTable.setStatus(_A)
_DpTimeRangeProfileEntry_Object=MibTableRow
dpTimeRangeProfileEntry=_DpTimeRangeProfileEntry_Object((1,3,6,1,4,1,171,15,24,1,1,1))
dpTimeRangeProfileEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:dpTimeRangeProfileEntry.setStatus(_A)
class _DpTimeRangeProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_DpTimeRangeProfileName_Type.__name__=_F
_DpTimeRangeProfileName_Object=MibTableColumn
dpTimeRangeProfileName=_DpTimeRangeProfileName_Object((1,3,6,1,4,1,171,15,24,1,1,1,1),_DpTimeRangeProfileName_Type())
dpTimeRangeProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfileName.setStatus(_A)
class _DpTimeRangeProfilePeriodType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('daily',1),('weekly',2)))
_DpTimeRangeProfilePeriodType_Type.__name__=_E
_DpTimeRangeProfilePeriodType_Object=MibTableColumn
dpTimeRangeProfilePeriodType=_DpTimeRangeProfilePeriodType_Object((1,3,6,1,4,1,171,15,24,1,1,1,2),_DpTimeRangeProfilePeriodType_Type())
dpTimeRangeProfilePeriodType.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfilePeriodType.setStatus(_A)
class _DpTimeRangeProfileStartDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8)))
_DpTimeRangeProfileStartDayOfWeek_Type.__name__=_E
_DpTimeRangeProfileStartDayOfWeek_Object=MibTableColumn
dpTimeRangeProfileStartDayOfWeek=_DpTimeRangeProfileStartDayOfWeek_Object((1,3,6,1,4,1,171,15,24,1,1,1,3),_DpTimeRangeProfileStartDayOfWeek_Type())
dpTimeRangeProfileStartDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfileStartDayOfWeek.setStatus(_A)
class _DpTimeRangeProfileStartHour_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_DpTimeRangeProfileStartHour_Type.__name__=_D
_DpTimeRangeProfileStartHour_Object=MibTableColumn
dpTimeRangeProfileStartHour=_DpTimeRangeProfileStartHour_Object((1,3,6,1,4,1,171,15,24,1,1,1,4),_DpTimeRangeProfileStartHour_Type())
dpTimeRangeProfileStartHour.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfileStartHour.setStatus(_A)
class _DpTimeRangeProfileStartMinute_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_DpTimeRangeProfileStartMinute_Type.__name__=_D
_DpTimeRangeProfileStartMinute_Object=MibTableColumn
dpTimeRangeProfileStartMinute=_DpTimeRangeProfileStartMinute_Object((1,3,6,1,4,1,171,15,24,1,1,1,5),_DpTimeRangeProfileStartMinute_Type())
dpTimeRangeProfileStartMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfileStartMinute.setStatus(_A)
class _DpTimeRangeProfileEndDayOfWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6),(_U,7),(_V,8)))
_DpTimeRangeProfileEndDayOfWeek_Type.__name__=_E
_DpTimeRangeProfileEndDayOfWeek_Object=MibTableColumn
dpTimeRangeProfileEndDayOfWeek=_DpTimeRangeProfileEndDayOfWeek_Object((1,3,6,1,4,1,171,15,24,1,1,1,6),_DpTimeRangeProfileEndDayOfWeek_Type())
dpTimeRangeProfileEndDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfileEndDayOfWeek.setStatus(_A)
class _DpTimeRangeProfileEndHour_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_DpTimeRangeProfileEndHour_Type.__name__=_D
_DpTimeRangeProfileEndHour_Object=MibTableColumn
dpTimeRangeProfileEndHour=_DpTimeRangeProfileEndHour_Object((1,3,6,1,4,1,171,15,24,1,1,1,7),_DpTimeRangeProfileEndHour_Type())
dpTimeRangeProfileEndHour.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfileEndHour.setStatus(_A)
class _DpTimeRangeProfileEndMinute_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_DpTimeRangeProfileEndMinute_Type.__name__=_D
_DpTimeRangeProfileEndMinute_Object=MibTableColumn
dpTimeRangeProfileEndMinute=_DpTimeRangeProfileEndMinute_Object((1,3,6,1,4,1,171,15,24,1,1,1,8),_DpTimeRangeProfileEndMinute_Type())
dpTimeRangeProfileEndMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:dpTimeRangeProfileEndMinute.setStatus(_A)
_DpTimeRangeProfileRowStatus_Type=RowStatus
_DpTimeRangeProfileRowStatus_Object=MibTableColumn
dpTimeRangeProfileRowStatus=_DpTimeRangeProfileRowStatus_Object((1,3,6,1,4,1,171,15,24,1,1,1,9),_DpTimeRangeProfileRowStatus_Type())
dpTimeRangeProfileRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:dpTimeRangeProfileRowStatus.setStatus(_A)
_DpTimeRangeMIBConformance_ObjectIdentity=ObjectIdentity
dpTimeRangeMIBConformance=_DpTimeRangeMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,15,24,2))
_DpTimeRangeCompliances_ObjectIdentity=ObjectIdentity
dpTimeRangeCompliances=_DpTimeRangeCompliances_ObjectIdentity((1,3,6,1,4,1,171,15,24,2,1))
_DpTimeRangeGroups_ObjectIdentity=ObjectIdentity
dpTimeRangeGroups=_DpTimeRangeGroups_ObjectIdentity((1,3,6,1,4,1,171,15,24,2,2))
dpTimeRangeProfileCfgGroup=ObjectGroup((1,3,6,1,4,1,171,15,24,2,2,1))
dpTimeRangeProfileCfgGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:dpTimeRangeProfileCfgGroup.setStatus(_A)
dpTimeRangeCompliance=ModuleCompliance((1,3,6,1,4,1,171,15,24,2,1,1))
dpTimeRangeCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:dpTimeRangeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dlinkPrimeTimeRangeMIB':dlinkPrimeTimeRangeMIB,'dpTimeRangeMIBNotifications':dpTimeRangeMIBNotifications,'dpTimeRangeMIBObjects':dpTimeRangeMIBObjects,'dpTimeRangeProfileTable':dpTimeRangeProfileTable,'dpTimeRangeProfileEntry':dpTimeRangeProfileEntry,_G:dpTimeRangeProfileName,_H:dpTimeRangeProfilePeriodType,_I:dpTimeRangeProfileStartDayOfWeek,_J:dpTimeRangeProfileStartHour,_K:dpTimeRangeProfileStartMinute,_L:dpTimeRangeProfileEndDayOfWeek,_M:dpTimeRangeProfileEndHour,_N:dpTimeRangeProfileEndMinute,_W:dpTimeRangeProfileRowStatus,'dpTimeRangeMIBConformance':dpTimeRangeMIBConformance,'dpTimeRangeCompliances':dpTimeRangeCompliances,'dpTimeRangeCompliance':dpTimeRangeCompliance,'dpTimeRangeGroups':dpTimeRangeGroups,_X:dpTimeRangeProfileCfgGroup})