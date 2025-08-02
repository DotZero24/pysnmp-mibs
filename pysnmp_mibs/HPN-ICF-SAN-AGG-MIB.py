_M='hpnicfSanAggGroupCurrentSpeed'
_L='hpnicfSanAggGroupPreviousSpeed'
_K='gigabit bps'
_J='read-create'
_I='Integer32'
_H='accessible-for-notify'
_G='read-only'
_F='ifIndex'
_E='ifDescr'
_D='hpnicfSanAggGroupNumber'
_C='IF-MIB'
_B='HPN-ICF-SAN-AGG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfSan,=mibBuilder.importSymbols('HPN-ICF-VSAN-MIB','hpnicfSan')
ifDescr,ifIndex=mibBuilder.importSymbols(_C,_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfSanAgg=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,2))
if mibBuilder.loadTexts:hpnicfSanAgg.setRevisions(('2013-02-25 09:40',))
class HpnicfMemberList(TextualConvention,OctetString):status=_A
_HpnicfSanAggMibObjects_ObjectIdentity=ObjectIdentity
hpnicfSanAggMibObjects=_HpnicfSanAggMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,2,1))
_HpnicfSanAggMaxMemberNumber_Type=Integer32
_HpnicfSanAggMaxMemberNumber_Object=MibScalar
hpnicfSanAggMaxMemberNumber=_HpnicfSanAggMaxMemberNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,1,1),_HpnicfSanAggMaxMemberNumber_Type())
hpnicfSanAggMaxMemberNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSanAggMaxMemberNumber.setStatus(_A)
_HpnicfSanAggGroupTable_Object=MibTable
hpnicfSanAggGroupTable=_HpnicfSanAggGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,2))
if mibBuilder.loadTexts:hpnicfSanAggGroupTable.setStatus(_A)
_HpnicfSanAggGroupEntry_Object=MibTableRow
hpnicfSanAggGroupEntry=_HpnicfSanAggGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,2,1))
hpnicfSanAggGroupEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:hpnicfSanAggGroupEntry.setStatus(_A)
class _HpnicfSanAggGroupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfSanAggGroupNumber_Type.__name__=_I
_HpnicfSanAggGroupNumber_Object=MibTableColumn
hpnicfSanAggGroupNumber=_HpnicfSanAggGroupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,2,1,1),_HpnicfSanAggGroupNumber_Type())
hpnicfSanAggGroupNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSanAggGroupNumber.setStatus(_A)
_HpnicfSanAggGroupIndex_Type=Integer32
_HpnicfSanAggGroupIndex_Object=MibTableColumn
hpnicfSanAggGroupIndex=_HpnicfSanAggGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,2,1,2),_HpnicfSanAggGroupIndex_Type())
hpnicfSanAggGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSanAggGroupIndex.setStatus(_A)
_HpnicfSanAggMemberList_Type=HpnicfMemberList
_HpnicfSanAggMemberList_Object=MibTableColumn
hpnicfSanAggMemberList=_HpnicfSanAggMemberList_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,2,1,3),_HpnicfSanAggMemberList_Type())
hpnicfSanAggMemberList.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfSanAggMemberList.setStatus(_A)
_HpnicfSanAggMemberStateList_Type=HpnicfMemberList
_HpnicfSanAggMemberStateList_Object=MibTableColumn
hpnicfSanAggMemberStateList=_HpnicfSanAggMemberStateList_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,2,1,4),_HpnicfSanAggMemberStateList_Type())
hpnicfSanAggMemberStateList.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfSanAggMemberStateList.setStatus(_A)
_HpnicfSanAggGroupRowStatus_Type=RowStatus
_HpnicfSanAggGroupRowStatus_Object=MibTableColumn
hpnicfSanAggGroupRowStatus=_HpnicfSanAggGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,2,1,5),_HpnicfSanAggGroupRowStatus_Type())
hpnicfSanAggGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfSanAggGroupRowStatus.setStatus(_A)
_HpnicfSanAggObjForNotification_ObjectIdentity=ObjectIdentity
hpnicfSanAggObjForNotification=_HpnicfSanAggObjForNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,2,3))
_HpnicfSanAggGroupPreviousSpeed_Type=Integer32
_HpnicfSanAggGroupPreviousSpeed_Object=MibScalar
hpnicfSanAggGroupPreviousSpeed=_HpnicfSanAggGroupPreviousSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,3,1),_HpnicfSanAggGroupPreviousSpeed_Type())
hpnicfSanAggGroupPreviousSpeed.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSanAggGroupPreviousSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfSanAggGroupPreviousSpeed.setUnits(_K)
_HpnicfSanAggGroupCurrentSpeed_Type=Integer32
_HpnicfSanAggGroupCurrentSpeed_Object=MibScalar
hpnicfSanAggGroupCurrentSpeed=_HpnicfSanAggGroupCurrentSpeed_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,2,3,2),_HpnicfSanAggGroupCurrentSpeed_Type())
hpnicfSanAggGroupCurrentSpeed.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfSanAggGroupCurrentSpeed.setStatus(_A)
if mibBuilder.loadTexts:hpnicfSanAggGroupCurrentSpeed.setUnits(_K)
_HpnicfSanAggNotifications_ObjectIdentity=ObjectIdentity
hpnicfSanAggNotifications=_HpnicfSanAggNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,2,4))
_HpnicfSanAggNotificationPrefix_ObjectIdentity=ObjectIdentity
hpnicfSanAggNotificationPrefix=_HpnicfSanAggNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,2,4,0))
hpnicfSanAggGroupSpeedChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,2,4,0,1))
hpnicfSanAggGroupSpeedChange.setObjects(*((_B,_D),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:hpnicfSanAggGroupSpeedChange.setStatus(_A)
hpnicfSanAggMemberInactive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,2,4,0,2))
hpnicfSanAggMemberInactive.setObjects(*((_B,_D),(_C,_F),(_C,_E)))
if mibBuilder.loadTexts:hpnicfSanAggMemberInactive.setStatus(_A)
hpnicfSanAggMemberActive=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,127,2,4,0,3))
hpnicfSanAggMemberActive.setObjects(*((_B,_D),(_C,_F),(_C,_E)))
if mibBuilder.loadTexts:hpnicfSanAggMemberActive.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfMemberList':HpnicfMemberList,'hpnicfSanAgg':hpnicfSanAgg,'hpnicfSanAggMibObjects':hpnicfSanAggMibObjects,'hpnicfSanAggMaxMemberNumber':hpnicfSanAggMaxMemberNumber,'hpnicfSanAggGroupTable':hpnicfSanAggGroupTable,'hpnicfSanAggGroupEntry':hpnicfSanAggGroupEntry,_D:hpnicfSanAggGroupNumber,'hpnicfSanAggGroupIndex':hpnicfSanAggGroupIndex,'hpnicfSanAggMemberList':hpnicfSanAggMemberList,'hpnicfSanAggMemberStateList':hpnicfSanAggMemberStateList,'hpnicfSanAggGroupRowStatus':hpnicfSanAggGroupRowStatus,'hpnicfSanAggObjForNotification':hpnicfSanAggObjForNotification,_L:hpnicfSanAggGroupPreviousSpeed,_M:hpnicfSanAggGroupCurrentSpeed,'hpnicfSanAggNotifications':hpnicfSanAggNotifications,'hpnicfSanAggNotificationPrefix':hpnicfSanAggNotificationPrefix,'hpnicfSanAggGroupSpeedChange':hpnicfSanAggGroupSpeedChange,'hpnicfSanAggMemberInactive':hpnicfSanAggMemberInactive,'hpnicfSanAggMemberActive':hpnicfSanAggMemberActive})