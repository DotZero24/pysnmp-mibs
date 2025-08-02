_a='hwLAGMibNotificationGroup'
_Z='hwLAGMibObjectGroup'
_Y='hwAggPortActiveNotification'
_X='hwAggPortInactiveNotification2'
_W='hwAggPortInactiveNotification'
_V='hwAggSpeedChangedNotification'
_U='hwAggResourceAllocationValue'
_T='hwAggPortNotAttachedString'
_S='hwAggPortLacpState'
_R='hwAggPortNotAttachedReason'
_Q='hwAggPortListSamePartnerPorts'
_P='hwAggPortListSelectedPorts'
_O='hwAggLinkState'
_N='hwAggLinkPortList'
_M='hwAggLinkMode'
_L='hwAggLinkName'
_K='accessible-for-notify'
_J='PortList'
_I='read-write'
_H='read-only'
_G='DisplayString'
_F='Integer32'
_E='hwAggPortIndex'
_D='read-create'
_C='hwAggLinkNumber'
_B='current'
_A='HUAWEI-LAG-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
huaweiDatacomm,huaweiMgmt=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','huaweiDatacomm','huaweiMgmt')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hwLAG=ModuleIdentity((1,3,6,1,4,1,2011,5,25,25))
_HwLAGMibObjects_ObjectIdentity=ObjectIdentity
hwLAGMibObjects=_HwLAGMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,5,25,25,1))
_HwAggLinkTable_Object=MibTable
hwAggLinkTable=_HwAggLinkTable_Object((1,3,6,1,4,1,2011,5,25,25,1,1))
if mibBuilder.loadTexts:hwAggLinkTable.setStatus(_B)
_HwAggLinkEntry_Object=MibTableRow
hwAggLinkEntry=_HwAggLinkEntry_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1))
hwAggLinkEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:hwAggLinkEntry.setStatus(_B)
_HwAggLinkNumber_Type=Integer32
_HwAggLinkNumber_Object=MibTableColumn
hwAggLinkNumber=_HwAggLinkNumber_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1,1),_HwAggLinkNumber_Type())
hwAggLinkNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:hwAggLinkNumber.setStatus(_B)
class _HwAggLinkName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HwAggLinkName_Type.__name__=_G
_HwAggLinkName_Object=MibTableColumn
hwAggLinkName=_HwAggLinkName_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1,2),_HwAggLinkName_Type())
hwAggLinkName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwAggLinkName.setStatus(_B)
class _HwAggLinkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('static',2),('dynamic',3)))
_HwAggLinkMode_Type.__name__=_F
_HwAggLinkMode_Object=MibTableColumn
hwAggLinkMode=_HwAggLinkMode_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1,3),_HwAggLinkMode_Type())
hwAggLinkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwAggLinkMode.setStatus(_B)
_HwAggLinkPortList_Type=PortList
_HwAggLinkPortList_Object=MibTableColumn
hwAggLinkPortList=_HwAggLinkPortList_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1,4),_HwAggLinkPortList_Type())
hwAggLinkPortList.setMaxAccess(_D)
if mibBuilder.loadTexts:hwAggLinkPortList.setStatus(_B)
_HwAggLinkState_Type=RowStatus
_HwAggLinkState_Object=MibTableColumn
hwAggLinkState=_HwAggLinkState_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1,5),_HwAggLinkState_Type())
hwAggLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:hwAggLinkState.setStatus(_B)
_HwAggPortListSelectedPorts_Type=PortList
_HwAggPortListSelectedPorts_Object=MibTableColumn
hwAggPortListSelectedPorts=_HwAggPortListSelectedPorts_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1,6),_HwAggPortListSelectedPorts_Type())
hwAggPortListSelectedPorts.setMaxAccess(_H)
if mibBuilder.loadTexts:hwAggPortListSelectedPorts.setStatus(_B)
_HwAggPortListSamePartnerPorts_Type=PortList
_HwAggPortListSamePartnerPorts_Object=MibTableColumn
hwAggPortListSamePartnerPorts=_HwAggPortListSamePartnerPorts_Object((1,3,6,1,4,1,2011,5,25,25,1,1,1,7),_HwAggPortListSamePartnerPorts_Type())
hwAggPortListSamePartnerPorts.setMaxAccess(_H)
if mibBuilder.loadTexts:hwAggPortListSamePartnerPorts.setStatus(_B)
_HwAggPortTable_Object=MibTable
hwAggPortTable=_HwAggPortTable_Object((1,3,6,1,4,1,2011,5,25,25,1,2))
if mibBuilder.loadTexts:hwAggPortTable.setStatus(_B)
_HwAggPortEntry_Object=MibTableRow
hwAggPortEntry=_HwAggPortEntry_Object((1,3,6,1,4,1,2011,5,25,25,1,2,1))
hwAggPortEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:hwAggPortEntry.setStatus(_B)
_HwAggPortIndex_Type=Gauge32
_HwAggPortIndex_Object=MibTableColumn
hwAggPortIndex=_HwAggPortIndex_Object((1,3,6,1,4,1,2011,5,25,25,1,2,1,1),_HwAggPortIndex_Type())
hwAggPortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:hwAggPortIndex.setStatus(_B)
class _HwAggPortNotAttachedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HwAggPortNotAttachedReason_Type.__name__=_F
_HwAggPortNotAttachedReason_Object=MibTableColumn
hwAggPortNotAttachedReason=_HwAggPortNotAttachedReason_Object((1,3,6,1,4,1,2011,5,25,25,1,2,1,2),_HwAggPortNotAttachedReason_Type())
hwAggPortNotAttachedReason.setMaxAccess(_I)
if mibBuilder.loadTexts:hwAggPortNotAttachedReason.setStatus(_B)
_HwAggPortLacpState_Type=TruthValue
_HwAggPortLacpState_Object=MibTableColumn
hwAggPortLacpState=_HwAggPortLacpState_Object((1,3,6,1,4,1,2011,5,25,25,1,2,1,3),_HwAggPortLacpState_Type())
hwAggPortLacpState.setMaxAccess(_I)
if mibBuilder.loadTexts:hwAggPortLacpState.setStatus(_B)
class _HwAggPortNotAttachedString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwAggPortNotAttachedString_Type.__name__=_G
_HwAggPortNotAttachedString_Object=MibTableColumn
hwAggPortNotAttachedString=_HwAggPortNotAttachedString_Object((1,3,6,1,4,1,2011,5,25,25,1,2,1,4),_HwAggPortNotAttachedString_Type())
hwAggPortNotAttachedString.setMaxAccess(_I)
if mibBuilder.loadTexts:hwAggPortNotAttachedString.setStatus(_B)
class _HwAggResourceAllocationValue_Type(PortList):defaultValue=OctetString('0')
_HwAggResourceAllocationValue_Type.__name__=_J
_HwAggResourceAllocationValue_Object=MibScalar
hwAggResourceAllocationValue=_HwAggResourceAllocationValue_Object((1,3,6,1,4,1,2011,5,25,25,1,3),_HwAggResourceAllocationValue_Type())
hwAggResourceAllocationValue.setMaxAccess(_H)
if mibBuilder.loadTexts:hwAggResourceAllocationValue.setStatus(_B)
_HwLAGMibNotifications_ObjectIdentity=ObjectIdentity
hwLAGMibNotifications=_HwLAGMibNotifications_ObjectIdentity((1,3,6,1,4,1,2011,5,25,25,2))
_HwLAGMibConformance_ObjectIdentity=ObjectIdentity
hwLAGMibConformance=_HwLAGMibConformance_ObjectIdentity((1,3,6,1,4,1,2011,5,25,25,3))
_HwLAGMibCompliances_ObjectIdentity=ObjectIdentity
hwLAGMibCompliances=_HwLAGMibCompliances_ObjectIdentity((1,3,6,1,4,1,2011,5,25,25,3,1))
_HwLAGMibGroup_ObjectIdentity=ObjectIdentity
hwLAGMibGroup=_HwLAGMibGroup_ObjectIdentity((1,3,6,1,4,1,2011,5,25,25,3,2))
hwLAGMibObjectGroup=ObjectGroup((1,3,6,1,4,1,2011,5,25,25,3,2,1))
hwLAGMibObjectGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:hwLAGMibObjectGroup.setStatus(_B)
hwAggSpeedChangedNotification=NotificationType((1,3,6,1,4,1,2011,5,25,25,2,1))
hwAggSpeedChangedNotification.setObjects((_A,_C))
if mibBuilder.loadTexts:hwAggSpeedChangedNotification.setStatus(_B)
hwAggPortInactiveNotification=NotificationType((1,3,6,1,4,1,2011,5,25,25,2,2))
hwAggPortInactiveNotification.setObjects((_A,_C))
if mibBuilder.loadTexts:hwAggPortInactiveNotification.setStatus(_B)
hwAggPortInactiveNotification2=NotificationType((1,3,6,1,4,1,2011,5,25,25,2,3))
hwAggPortInactiveNotification2.setObjects(*((_A,_C),(_A,_E)))
if mibBuilder.loadTexts:hwAggPortInactiveNotification2.setStatus(_B)
hwAggPortActiveNotification=NotificationType((1,3,6,1,4,1,2011,5,25,25,2,4))
hwAggPortActiveNotification.setObjects(*((_A,_C),(_A,_E)))
if mibBuilder.loadTexts:hwAggPortActiveNotification.setStatus(_B)
hwLAGMibNotificationGroup=NotificationGroup((1,3,6,1,4,1,2011,5,25,25,3,2,2))
hwLAGMibNotificationGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:hwLAGMibNotificationGroup.setStatus(_B)
hwLAGMibCompliance=ModuleCompliance((1,3,6,1,4,1,2011,5,25,25,3,1,1))
hwLAGMibCompliance.setObjects(*((_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:hwLAGMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hwLAG':hwLAG,'hwLAGMibObjects':hwLAGMibObjects,'hwAggLinkTable':hwAggLinkTable,'hwAggLinkEntry':hwAggLinkEntry,_C:hwAggLinkNumber,_L:hwAggLinkName,_M:hwAggLinkMode,_N:hwAggLinkPortList,_O:hwAggLinkState,_P:hwAggPortListSelectedPorts,_Q:hwAggPortListSamePartnerPorts,'hwAggPortTable':hwAggPortTable,'hwAggPortEntry':hwAggPortEntry,_E:hwAggPortIndex,_R:hwAggPortNotAttachedReason,_S:hwAggPortLacpState,_T:hwAggPortNotAttachedString,_U:hwAggResourceAllocationValue,'hwLAGMibNotifications':hwLAGMibNotifications,_V:hwAggSpeedChangedNotification,_W:hwAggPortInactiveNotification,_X:hwAggPortInactiveNotification2,_Y:hwAggPortActiveNotification,'hwLAGMibConformance':hwLAGMibConformance,'hwLAGMibCompliances':hwLAGMibCompliances,'hwLAGMibCompliance':hwLAGMibCompliance,'hwLAGMibGroup':hwLAGMibGroup,_Z:hwLAGMibObjectGroup,_a:hwLAGMibNotificationGroup})