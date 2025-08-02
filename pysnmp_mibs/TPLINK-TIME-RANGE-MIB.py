_H='tpHolidayName'
_G='tpTimeRangeName'
_F='Integer32'
_E='TPLINK-TIME-RANGE-MIB'
_D='read-only'
_C='read-create'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkTimeRangeMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,55))
if mibBuilder.loadTexts:tplinkTimeRangeMIB.setRevisions(('2013-07-03 00:00',))
_TplinkTimeRangeMIBObjects_ObjectIdentity=ObjectIdentity
tplinkTimeRangeMIBObjects=_TplinkTimeRangeMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,55,1))
_TpTimeRangeConfig_ObjectIdentity=ObjectIdentity
tpTimeRangeConfig=_TpTimeRangeConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,55,1,1))
_TpTimeRangeConfigTable_Object=MibTable
tpTimeRangeConfigTable=_TpTimeRangeConfigTable_Object((1,3,6,1,4,1,11863,6,55,1,1,1))
if mibBuilder.loadTexts:tpTimeRangeConfigTable.setStatus(_A)
_TpTimeRangeConfigEntry_Object=MibTableRow
tpTimeRangeConfigEntry=_TpTimeRangeConfigEntry_Object((1,3,6,1,4,1,11863,6,55,1,1,1,1))
tpTimeRangeConfigEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:tpTimeRangeConfigEntry.setStatus(_A)
_TpTimeRangeIndex_Type=Integer32
_TpTimeRangeIndex_Object=MibTableColumn
tpTimeRangeIndex=_TpTimeRangeIndex_Object((1,3,6,1,4,1,11863,6,55,1,1,1,1,1),_TpTimeRangeIndex_Type())
tpTimeRangeIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpTimeRangeIndex.setStatus(_A)
class _TpTimeRangeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpTimeRangeName_Type.__name__=_B
_TpTimeRangeName_Object=MibTableColumn
tpTimeRangeName=_TpTimeRangeName_Object((1,3,6,1,4,1,11863,6,55,1,1,1,1,2),_TpTimeRangeName_Type())
tpTimeRangeName.setMaxAccess(_D)
if mibBuilder.loadTexts:tpTimeRangeName.setStatus(_A)
class _TpTimeRangeExcludeHoliday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('include',0),('exclude',1)))
_TpTimeRangeExcludeHoliday_Type.__name__=_F
_TpTimeRangeExcludeHoliday_Object=MibTableColumn
tpTimeRangeExcludeHoliday=_TpTimeRangeExcludeHoliday_Object((1,3,6,1,4,1,11863,6,55,1,1,1,1,3),_TpTimeRangeExcludeHoliday_Type())
tpTimeRangeExcludeHoliday.setMaxAccess(_C)
if mibBuilder.loadTexts:tpTimeRangeExcludeHoliday.setStatus(_A)
class _TpTimeRangeAbsoluteTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_TpTimeRangeAbsoluteTime_Type.__name__=_B
_TpTimeRangeAbsoluteTime_Object=MibTableColumn
tpTimeRangeAbsoluteTime=_TpTimeRangeAbsoluteTime_Object((1,3,6,1,4,1,11863,6,55,1,1,1,1,4),_TpTimeRangeAbsoluteTime_Type())
tpTimeRangeAbsoluteTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpTimeRangeAbsoluteTime.setStatus(_A)
class _TpTimeRangePeriodicTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,511))
_TpTimeRangePeriodicTime_Type.__name__=_B
_TpTimeRangePeriodicTime_Object=MibTableColumn
tpTimeRangePeriodicTime=_TpTimeRangePeriodicTime_Object((1,3,6,1,4,1,11863,6,55,1,1,1,1,5),_TpTimeRangePeriodicTime_Type())
tpTimeRangePeriodicTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpTimeRangePeriodicTime.setStatus(_A)
_TpTimeRangeStatus_Type=TPRowStatus
_TpTimeRangeStatus_Object=MibTableColumn
tpTimeRangeStatus=_TpTimeRangeStatus_Object((1,3,6,1,4,1,11863,6,55,1,1,1,1,6),_TpTimeRangeStatus_Type())
tpTimeRangeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpTimeRangeStatus.setStatus(_A)
_TpHolidayConfig_ObjectIdentity=ObjectIdentity
tpHolidayConfig=_TpHolidayConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,55,1,2))
_TpHolidayConfigTable_Object=MibTable
tpHolidayConfigTable=_TpHolidayConfigTable_Object((1,3,6,1,4,1,11863,6,55,1,2,1))
if mibBuilder.loadTexts:tpHolidayConfigTable.setStatus(_A)
_TpHolidayConfigEntry_Object=MibTableRow
tpHolidayConfigEntry=_TpHolidayConfigEntry_Object((1,3,6,1,4,1,11863,6,55,1,2,1,1))
tpHolidayConfigEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:tpHolidayConfigEntry.setStatus(_A)
_TpHolidayIndex_Type=Integer32
_TpHolidayIndex_Object=MibTableColumn
tpHolidayIndex=_TpHolidayIndex_Object((1,3,6,1,4,1,11863,6,55,1,2,1,1,1),_TpHolidayIndex_Type())
tpHolidayIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tpHolidayIndex.setStatus(_A)
class _TpHolidayName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpHolidayName_Type.__name__=_B
_TpHolidayName_Object=MibTableColumn
tpHolidayName=_TpHolidayName_Object((1,3,6,1,4,1,11863,6,55,1,2,1,1,2),_TpHolidayName_Type())
tpHolidayName.setMaxAccess(_D)
if mibBuilder.loadTexts:tpHolidayName.setStatus(_A)
class _TpHolidayStartDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpHolidayStartDate_Type.__name__=_B
_TpHolidayStartDate_Object=MibTableColumn
tpHolidayStartDate=_TpHolidayStartDate_Object((1,3,6,1,4,1,11863,6,55,1,2,1,1,3),_TpHolidayStartDate_Type())
tpHolidayStartDate.setMaxAccess(_C)
if mibBuilder.loadTexts:tpHolidayStartDate.setStatus(_A)
class _TpHolidayEndDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpHolidayEndDate_Type.__name__=_B
_TpHolidayEndDate_Object=MibTableColumn
tpHolidayEndDate=_TpHolidayEndDate_Object((1,3,6,1,4,1,11863,6,55,1,2,1,1,4),_TpHolidayEndDate_Type())
tpHolidayEndDate.setMaxAccess(_C)
if mibBuilder.loadTexts:tpHolidayEndDate.setStatus(_A)
_TpHolidayStatus_Type=TPRowStatus
_TpHolidayStatus_Object=MibTableColumn
tpHolidayStatus=_TpHolidayStatus_Object((1,3,6,1,4,1,11863,6,55,1,2,1,1,5),_TpHolidayStatus_Type())
tpHolidayStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpHolidayStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'tplinkTimeRangeMIB':tplinkTimeRangeMIB,'tplinkTimeRangeMIBObjects':tplinkTimeRangeMIBObjects,'tpTimeRangeConfig':tpTimeRangeConfig,'tpTimeRangeConfigTable':tpTimeRangeConfigTable,'tpTimeRangeConfigEntry':tpTimeRangeConfigEntry,'tpTimeRangeIndex':tpTimeRangeIndex,_G:tpTimeRangeName,'tpTimeRangeExcludeHoliday':tpTimeRangeExcludeHoliday,'tpTimeRangeAbsoluteTime':tpTimeRangeAbsoluteTime,'tpTimeRangePeriodicTime':tpTimeRangePeriodicTime,'tpTimeRangeStatus':tpTimeRangeStatus,'tpHolidayConfig':tpHolidayConfig,'tpHolidayConfigTable':tpHolidayConfigTable,'tpHolidayConfigEntry':tpHolidayConfigEntry,'tpHolidayIndex':tpHolidayIndex,_H:tpHolidayName,'tpHolidayStartDate':tpHolidayStartDate,'tpHolidayEndDate':tpHolidayEndDate,'tpHolidayStatus':tpHolidayStatus})