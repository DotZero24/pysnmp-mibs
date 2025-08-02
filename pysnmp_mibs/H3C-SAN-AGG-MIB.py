_M='h3cSanAggGroupCurrentSpeed'
_L='h3cSanAggGroupPreviousSpeed'
_K='gigabit bps'
_J='read-create'
_I='Integer32'
_H='accessible-for-notify'
_G='read-only'
_F='ifIndex'
_E='ifDescr'
_D='h3cSanAggGroupNumber'
_C='IF-MIB'
_B='H3C-SAN-AGG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cSan,=mibBuilder.importSymbols('H3C-VSAN-MIB','h3cSan')
ifDescr,ifIndex=mibBuilder.importSymbols(_C,_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cSanAgg=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,2))
if mibBuilder.loadTexts:h3cSanAgg.setRevisions(('2013-02-25 09:40',))
class H3cMemberList(TextualConvention,OctetString):status=_A
_H3cSanAggMibObjects_ObjectIdentity=ObjectIdentity
h3cSanAggMibObjects=_H3cSanAggMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,2,1))
_H3cSanAggMaxMemberNumber_Type=Integer32
_H3cSanAggMaxMemberNumber_Object=MibScalar
h3cSanAggMaxMemberNumber=_H3cSanAggMaxMemberNumber_Object((1,3,6,1,4,1,2011,10,2,127,2,1,1),_H3cSanAggMaxMemberNumber_Type())
h3cSanAggMaxMemberNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSanAggMaxMemberNumber.setStatus(_A)
_H3cSanAggGroupTable_Object=MibTable
h3cSanAggGroupTable=_H3cSanAggGroupTable_Object((1,3,6,1,4,1,2011,10,2,127,2,2))
if mibBuilder.loadTexts:h3cSanAggGroupTable.setStatus(_A)
_H3cSanAggGroupEntry_Object=MibTableRow
h3cSanAggGroupEntry=_H3cSanAggGroupEntry_Object((1,3,6,1,4,1,2011,10,2,127,2,2,1))
h3cSanAggGroupEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:h3cSanAggGroupEntry.setStatus(_A)
class _H3cSanAggGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cSanAggGroupNumber_Type.__name__=_I
_H3cSanAggGroupNumber_Object=MibTableColumn
h3cSanAggGroupNumber=_H3cSanAggGroupNumber_Object((1,3,6,1,4,1,2011,10,2,127,2,2,1,1),_H3cSanAggGroupNumber_Type())
h3cSanAggGroupNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSanAggGroupNumber.setStatus(_A)
_H3cSanAggGroupIndex_Type=Integer32
_H3cSanAggGroupIndex_Object=MibTableColumn
h3cSanAggGroupIndex=_H3cSanAggGroupIndex_Object((1,3,6,1,4,1,2011,10,2,127,2,2,1,2),_H3cSanAggGroupIndex_Type())
h3cSanAggGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSanAggGroupIndex.setStatus(_A)
_H3cSanAggMemberList_Type=H3cMemberList
_H3cSanAggMemberList_Object=MibTableColumn
h3cSanAggMemberList=_H3cSanAggMemberList_Object((1,3,6,1,4,1,2011,10,2,127,2,2,1,3),_H3cSanAggMemberList_Type())
h3cSanAggMemberList.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSanAggMemberList.setStatus(_A)
_H3cSanAggMemberStateList_Type=H3cMemberList
_H3cSanAggMemberStateList_Object=MibTableColumn
h3cSanAggMemberStateList=_H3cSanAggMemberStateList_Object((1,3,6,1,4,1,2011,10,2,127,2,2,1,4),_H3cSanAggMemberStateList_Type())
h3cSanAggMemberStateList.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cSanAggMemberStateList.setStatus(_A)
_H3cSanAggGroupRowStatus_Type=RowStatus
_H3cSanAggGroupRowStatus_Object=MibTableColumn
h3cSanAggGroupRowStatus=_H3cSanAggGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,127,2,2,1,5),_H3cSanAggGroupRowStatus_Type())
h3cSanAggGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cSanAggGroupRowStatus.setStatus(_A)
_H3cSanAggObjForNotification_ObjectIdentity=ObjectIdentity
h3cSanAggObjForNotification=_H3cSanAggObjForNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,2,3))
_H3cSanAggGroupPreviousSpeed_Type=Integer32
_H3cSanAggGroupPreviousSpeed_Object=MibScalar
h3cSanAggGroupPreviousSpeed=_H3cSanAggGroupPreviousSpeed_Object((1,3,6,1,4,1,2011,10,2,127,2,3,1),_H3cSanAggGroupPreviousSpeed_Type())
h3cSanAggGroupPreviousSpeed.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSanAggGroupPreviousSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cSanAggGroupPreviousSpeed.setUnits(_K)
_H3cSanAggGroupCurrentSpeed_Type=Integer32
_H3cSanAggGroupCurrentSpeed_Object=MibScalar
h3cSanAggGroupCurrentSpeed=_H3cSanAggGroupCurrentSpeed_Object((1,3,6,1,4,1,2011,10,2,127,2,3,2),_H3cSanAggGroupCurrentSpeed_Type())
h3cSanAggGroupCurrentSpeed.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cSanAggGroupCurrentSpeed.setStatus(_A)
if mibBuilder.loadTexts:h3cSanAggGroupCurrentSpeed.setUnits(_K)
_H3cSanAggNotifications_ObjectIdentity=ObjectIdentity
h3cSanAggNotifications=_H3cSanAggNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,2,4))
_H3cSanAggNotificationPrefix_ObjectIdentity=ObjectIdentity
h3cSanAggNotificationPrefix=_H3cSanAggNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,2,4,0))
h3cSanAggGroupSpeedChange=NotificationType((1,3,6,1,4,1,2011,10,2,127,2,4,0,1))
h3cSanAggGroupSpeedChange.setObjects(*((_B,_D),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:h3cSanAggGroupSpeedChange.setStatus(_A)
h3cSanAggMemberInactive=NotificationType((1,3,6,1,4,1,2011,10,2,127,2,4,0,2))
h3cSanAggMemberInactive.setObjects(*((_B,_D),(_C,_F),(_C,_E)))
if mibBuilder.loadTexts:h3cSanAggMemberInactive.setStatus(_A)
h3cSanAggMemberActive=NotificationType((1,3,6,1,4,1,2011,10,2,127,2,4,0,3))
h3cSanAggMemberActive.setObjects(*((_B,_D),(_C,_F),(_C,_E)))
if mibBuilder.loadTexts:h3cSanAggMemberActive.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cMemberList':H3cMemberList,'h3cSanAgg':h3cSanAgg,'h3cSanAggMibObjects':h3cSanAggMibObjects,'h3cSanAggMaxMemberNumber':h3cSanAggMaxMemberNumber,'h3cSanAggGroupTable':h3cSanAggGroupTable,'h3cSanAggGroupEntry':h3cSanAggGroupEntry,_D:h3cSanAggGroupNumber,'h3cSanAggGroupIndex':h3cSanAggGroupIndex,'h3cSanAggMemberList':h3cSanAggMemberList,'h3cSanAggMemberStateList':h3cSanAggMemberStateList,'h3cSanAggGroupRowStatus':h3cSanAggGroupRowStatus,'h3cSanAggObjForNotification':h3cSanAggObjForNotification,_L:h3cSanAggGroupPreviousSpeed,_M:h3cSanAggGroupCurrentSpeed,'h3cSanAggNotifications':h3cSanAggNotifications,'h3cSanAggNotificationPrefix':h3cSanAggNotificationPrefix,'h3cSanAggGroupSpeedChange':h3cSanAggGroupSpeedChange,'h3cSanAggMemberInactive':h3cSanAggMemberInactive,'h3cSanAggMemberActive':h3cSanAggMemberActive})