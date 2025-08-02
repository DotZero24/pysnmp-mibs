_a='hpnicfLAGMibNotificationGroup'
_Z='hpnicfLAGMibObjectGroup'
_Y='hpnicfAggPortActiveNotification'
_X='hpnicfAggPortInactiveNotification2'
_W='hpnicfAggPortInactiveNotification'
_V='hpnicfAggSpeedChangedNotification'
_U='hpnicfAggResourceAllocationValue'
_T='hpnicfAggPortNotAttachedString'
_S='hpnicfAggPortLacpState'
_R='hpnicfAggPortNotAttachedReason'
_Q='hpnicfAggPortListSamePartnerPorts'
_P='hpnicfAggPortListSelectedPorts'
_O='hpnicfAggLinkState'
_N='hpnicfAggLinkPortList'
_M='hpnicfAggLinkMode'
_L='hpnicfAggLinkName'
_K='accessible-for-notify'
_J='PortList'
_I='read-write'
_H='read-only'
_G='DisplayString'
_F='Integer32'
_E='hpnicfAggPortIndex'
_D='read-create'
_C='hpnicfAggLinkNumber'
_B='current'
_A='HPN-ICF-LAG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfLAG=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,25))
_HpnicfLAGMibObjects_ObjectIdentity=ObjectIdentity
hpnicfLAGMibObjects=_HpnicfLAGMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,25,1))
_HpnicfAggLinkTable_Object=MibTable
hpnicfAggLinkTable=_HpnicfAggLinkTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1))
if mibBuilder.loadTexts:hpnicfAggLinkTable.setStatus(_B)
_HpnicfAggLinkEntry_Object=MibTableRow
hpnicfAggLinkEntry=_HpnicfAggLinkEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1))
hpnicfAggLinkEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:hpnicfAggLinkEntry.setStatus(_B)
_HpnicfAggLinkNumber_Type=Integer32
_HpnicfAggLinkNumber_Object=MibTableColumn
hpnicfAggLinkNumber=_HpnicfAggLinkNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1,1),_HpnicfAggLinkNumber_Type())
hpnicfAggLinkNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfAggLinkNumber.setStatus(_B)
class _HpnicfAggLinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfAggLinkName_Type.__name__=_G
_HpnicfAggLinkName_Object=MibTableColumn
hpnicfAggLinkName=_HpnicfAggLinkName_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1,2),_HpnicfAggLinkName_Type())
hpnicfAggLinkName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAggLinkName.setStatus(_B)
class _HpnicfAggLinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('static',2),('dynamic',3)))
_HpnicfAggLinkMode_Type.__name__=_F
_HpnicfAggLinkMode_Object=MibTableColumn
hpnicfAggLinkMode=_HpnicfAggLinkMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1,3),_HpnicfAggLinkMode_Type())
hpnicfAggLinkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAggLinkMode.setStatus(_B)
_HpnicfAggLinkPortList_Type=PortList
_HpnicfAggLinkPortList_Object=MibTableColumn
hpnicfAggLinkPortList=_HpnicfAggLinkPortList_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1,4),_HpnicfAggLinkPortList_Type())
hpnicfAggLinkPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAggLinkPortList.setStatus(_B)
_HpnicfAggLinkState_Type=RowStatus
_HpnicfAggLinkState_Object=MibTableColumn
hpnicfAggLinkState=_HpnicfAggLinkState_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1,5),_HpnicfAggLinkState_Type())
hpnicfAggLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfAggLinkState.setStatus(_B)
_HpnicfAggPortListSelectedPorts_Type=PortList
_HpnicfAggPortListSelectedPorts_Object=MibTableColumn
hpnicfAggPortListSelectedPorts=_HpnicfAggPortListSelectedPorts_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1,6),_HpnicfAggPortListSelectedPorts_Type())
hpnicfAggPortListSelectedPorts.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfAggPortListSelectedPorts.setStatus(_B)
_HpnicfAggPortListSamePartnerPorts_Type=PortList
_HpnicfAggPortListSamePartnerPorts_Object=MibTableColumn
hpnicfAggPortListSamePartnerPorts=_HpnicfAggPortListSamePartnerPorts_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,1,1,7),_HpnicfAggPortListSamePartnerPorts_Type())
hpnicfAggPortListSamePartnerPorts.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfAggPortListSamePartnerPorts.setStatus(_B)
_HpnicfAggPortTable_Object=MibTable
hpnicfAggPortTable=_HpnicfAggPortTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,2))
if mibBuilder.loadTexts:hpnicfAggPortTable.setStatus(_B)
_HpnicfAggPortEntry_Object=MibTableRow
hpnicfAggPortEntry=_HpnicfAggPortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,2,1))
hpnicfAggPortEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:hpnicfAggPortEntry.setStatus(_B)
_HpnicfAggPortIndex_Type=Gauge32
_HpnicfAggPortIndex_Object=MibTableColumn
hpnicfAggPortIndex=_HpnicfAggPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,2,1,1),_HpnicfAggPortIndex_Type())
hpnicfAggPortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfAggPortIndex.setStatus(_B)
class _HpnicfAggPortNotAttachedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HpnicfAggPortNotAttachedReason_Type.__name__=_F
_HpnicfAggPortNotAttachedReason_Object=MibTableColumn
hpnicfAggPortNotAttachedReason=_HpnicfAggPortNotAttachedReason_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,2,1,2),_HpnicfAggPortNotAttachedReason_Type())
hpnicfAggPortNotAttachedReason.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfAggPortNotAttachedReason.setStatus(_B)
_HpnicfAggPortLacpState_Type=TruthValue
_HpnicfAggPortLacpState_Object=MibTableColumn
hpnicfAggPortLacpState=_HpnicfAggPortLacpState_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,2,1,3),_HpnicfAggPortLacpState_Type())
hpnicfAggPortLacpState.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfAggPortLacpState.setStatus(_B)
class _HpnicfAggPortNotAttachedString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfAggPortNotAttachedString_Type.__name__=_G
_HpnicfAggPortNotAttachedString_Object=MibTableColumn
hpnicfAggPortNotAttachedString=_HpnicfAggPortNotAttachedString_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,2,1,4),_HpnicfAggPortNotAttachedString_Type())
hpnicfAggPortNotAttachedString.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfAggPortNotAttachedString.setStatus(_B)
class _HpnicfAggResourceAllocationValue_Type(PortList):defaultValue=OctetString('0')
_HpnicfAggResourceAllocationValue_Type.__name__=_J
_HpnicfAggResourceAllocationValue_Object=MibScalar
hpnicfAggResourceAllocationValue=_HpnicfAggResourceAllocationValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,25,1,3),_HpnicfAggResourceAllocationValue_Type())
hpnicfAggResourceAllocationValue.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfAggResourceAllocationValue.setStatus(_B)
_HpnicfLAGMibNotifications_ObjectIdentity=ObjectIdentity
hpnicfLAGMibNotifications=_HpnicfLAGMibNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,25,2))
_HpnicfLAGMibConformance_ObjectIdentity=ObjectIdentity
hpnicfLAGMibConformance=_HpnicfLAGMibConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,25,3))
_HpnicfLAGMibCompliances_ObjectIdentity=ObjectIdentity
hpnicfLAGMibCompliances=_HpnicfLAGMibCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,25,3,1))
_HpnicfLAGMibGroup_ObjectIdentity=ObjectIdentity
hpnicfLAGMibGroup=_HpnicfLAGMibGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,25,3,2))
hpnicfLAGMibObjectGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,25,3,2,1))
hpnicfLAGMibObjectGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:hpnicfLAGMibObjectGroup.setStatus(_B)
hpnicfAggSpeedChangedNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,25,2,1))
hpnicfAggSpeedChangedNotification.setObjects((_A,_C))
if mibBuilder.loadTexts:hpnicfAggSpeedChangedNotification.setStatus(_B)
hpnicfAggPortInactiveNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,25,2,2))
hpnicfAggPortInactiveNotification.setObjects((_A,_C))
if mibBuilder.loadTexts:hpnicfAggPortInactiveNotification.setStatus(_B)
hpnicfAggPortInactiveNotification2=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,25,2,3))
hpnicfAggPortInactiveNotification2.setObjects(*((_A,_C),(_A,_E)))
if mibBuilder.loadTexts:hpnicfAggPortInactiveNotification2.setStatus(_B)
hpnicfAggPortActiveNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,25,2,4))
hpnicfAggPortActiveNotification.setObjects(*((_A,_C),(_A,_E)))
if mibBuilder.loadTexts:hpnicfAggPortActiveNotification.setStatus(_B)
hpnicfLAGMibNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,8,25,3,2,2))
hpnicfLAGMibNotificationGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:hpnicfLAGMibNotificationGroup.setStatus(_B)
hpnicfLAGMibCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,8,25,3,1,1))
hpnicfLAGMibCompliance.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hpnicfLAGMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpnicfLAG':hpnicfLAG,'hpnicfLAGMibObjects':hpnicfLAGMibObjects,'hpnicfAggLinkTable':hpnicfAggLinkTable,'hpnicfAggLinkEntry':hpnicfAggLinkEntry,_C:hpnicfAggLinkNumber,_L:hpnicfAggLinkName,_M:hpnicfAggLinkMode,_N:hpnicfAggLinkPortList,_O:hpnicfAggLinkState,_P:hpnicfAggPortListSelectedPorts,_Q:hpnicfAggPortListSamePartnerPorts,'hpnicfAggPortTable':hpnicfAggPortTable,'hpnicfAggPortEntry':hpnicfAggPortEntry,_E:hpnicfAggPortIndex,_R:hpnicfAggPortNotAttachedReason,_S:hpnicfAggPortLacpState,_T:hpnicfAggPortNotAttachedString,_U:hpnicfAggResourceAllocationValue,'hpnicfLAGMibNotifications':hpnicfLAGMibNotifications,_V:hpnicfAggSpeedChangedNotification,_W:hpnicfAggPortInactiveNotification,_X:hpnicfAggPortInactiveNotification2,_Y:hpnicfAggPortActiveNotification,'hpnicfLAGMibConformance':hpnicfLAGMibConformance,'hpnicfLAGMibCompliances':hpnicfLAGMibCompliances,'hpnicfLAGMibCompliance':hpnicfLAGMibCompliance,'hpnicfLAGMibGroup':hpnicfLAGMibGroup,_Z:hpnicfLAGMibObjectGroup,_a:hpnicfLAGMibNotificationGroup})