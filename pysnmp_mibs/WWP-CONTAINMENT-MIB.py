_P='wwpContainmentMulticastState'
_O='wwpContainmentBroadcastState'
_N='wwpContainmentMulticastPortId'
_M='stopping'
_L='engaged'
_K='starting'
_J='throttle'
_I='monitor'
_H='disable'
_G='wwpContainmentBroadcastPortId'
_F='TruthValue'
_E='read-only'
_D='WWP-CONTAINMENT-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
wwpModules,=mibBuilder.importSymbols('WWP-SMI','wwpModules')
wwpContainmentMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,55))
_WwpContainmentMIBObjects_ObjectIdentity=ObjectIdentity
wwpContainmentMIBObjects=_WwpContainmentMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,55,1))
_WwpContainment_ObjectIdentity=ObjectIdentity
wwpContainment=_WwpContainment_ObjectIdentity((1,3,6,1,4,1,6141,2,55,1,1))
_WwpContainmentBroadcastTable_Object=MibTable
wwpContainmentBroadcastTable=_WwpContainmentBroadcastTable_Object((1,3,6,1,4,1,6141,2,55,1,1,1))
if mibBuilder.loadTexts:wwpContainmentBroadcastTable.setStatus(_A)
_WwpContainmentBroadcastEntry_Object=MibTableRow
wwpContainmentBroadcastEntry=_WwpContainmentBroadcastEntry_Object((1,3,6,1,4,1,6141,2,55,1,1,1,1))
wwpContainmentBroadcastEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wwpContainmentBroadcastEntry.setStatus(_A)
class _WwpContainmentBroadcastPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpContainmentBroadcastPortId_Type.__name__=_B
_WwpContainmentBroadcastPortId_Object=MibTableColumn
wwpContainmentBroadcastPortId=_WwpContainmentBroadcastPortId_Object((1,3,6,1,4,1,6141,2,55,1,1,1,1,1),_WwpContainmentBroadcastPortId_Type())
wwpContainmentBroadcastPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpContainmentBroadcastPortId.setStatus(_A)
class _WwpContainmentBroadcastAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_WwpContainmentBroadcastAction_Type.__name__=_B
_WwpContainmentBroadcastAction_Object=MibTableColumn
wwpContainmentBroadcastAction=_WwpContainmentBroadcastAction_Object((1,3,6,1,4,1,6141,2,55,1,1,1,1,2),_WwpContainmentBroadcastAction_Type())
wwpContainmentBroadcastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentBroadcastAction.setStatus(_A)
class _WwpContainmentBroadcastHighMark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpContainmentBroadcastHighMark_Type.__name__=_B
_WwpContainmentBroadcastHighMark_Object=MibTableColumn
wwpContainmentBroadcastHighMark=_WwpContainmentBroadcastHighMark_Object((1,3,6,1,4,1,6141,2,55,1,1,1,1,3),_WwpContainmentBroadcastHighMark_Type())
wwpContainmentBroadcastHighMark.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentBroadcastHighMark.setStatus(_A)
class _WwpContainmentBroadcastLowMark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpContainmentBroadcastLowMark_Type.__name__=_B
_WwpContainmentBroadcastLowMark_Object=MibTableColumn
wwpContainmentBroadcastLowMark=_WwpContainmentBroadcastLowMark_Object((1,3,6,1,4,1,6141,2,55,1,1,1,1,4),_WwpContainmentBroadcastLowMark_Type())
wwpContainmentBroadcastLowMark.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentBroadcastLowMark.setStatus(_A)
class _WwpContainmentBroadcastTrapsEnable_Type(TruthValue):defaultValue=1
_WwpContainmentBroadcastTrapsEnable_Type.__name__=_F
_WwpContainmentBroadcastTrapsEnable_Object=MibTableColumn
wwpContainmentBroadcastTrapsEnable=_WwpContainmentBroadcastTrapsEnable_Object((1,3,6,1,4,1,6141,2,55,1,1,1,1,5),_WwpContainmentBroadcastTrapsEnable_Type())
wwpContainmentBroadcastTrapsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentBroadcastTrapsEnable.setStatus(_A)
class _WwpContainmentBroadcastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),(_K,2),(_L,3),(_M,4)))
_WwpContainmentBroadcastState_Type.__name__=_B
_WwpContainmentBroadcastState_Object=MibTableColumn
wwpContainmentBroadcastState=_WwpContainmentBroadcastState_Object((1,3,6,1,4,1,6141,2,55,1,1,1,1,6),_WwpContainmentBroadcastState_Type())
wwpContainmentBroadcastState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpContainmentBroadcastState.setStatus(_A)
_WwpContainmentMulticastTable_Object=MibTable
wwpContainmentMulticastTable=_WwpContainmentMulticastTable_Object((1,3,6,1,4,1,6141,2,55,1,1,2))
if mibBuilder.loadTexts:wwpContainmentMulticastTable.setStatus(_A)
_WwpContainmentMulticastEntry_Object=MibTableRow
wwpContainmentMulticastEntry=_WwpContainmentMulticastEntry_Object((1,3,6,1,4,1,6141,2,55,1,1,2,1))
wwpContainmentMulticastEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:wwpContainmentMulticastEntry.setStatus(_A)
class _WwpContainmentMulticastPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpContainmentMulticastPortId_Type.__name__=_B
_WwpContainmentMulticastPortId_Object=MibTableColumn
wwpContainmentMulticastPortId=_WwpContainmentMulticastPortId_Object((1,3,6,1,4,1,6141,2,55,1,1,2,1,1),_WwpContainmentMulticastPortId_Type())
wwpContainmentMulticastPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpContainmentMulticastPortId.setStatus(_A)
class _WwpContainmentMulticastAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_WwpContainmentMulticastAction_Type.__name__=_B
_WwpContainmentMulticastAction_Object=MibTableColumn
wwpContainmentMulticastAction=_WwpContainmentMulticastAction_Object((1,3,6,1,4,1,6141,2,55,1,1,2,1,2),_WwpContainmentMulticastAction_Type())
wwpContainmentMulticastAction.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentMulticastAction.setStatus(_A)
class _WwpContainmentMulticastHighMark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpContainmentMulticastHighMark_Type.__name__=_B
_WwpContainmentMulticastHighMark_Object=MibTableColumn
wwpContainmentMulticastHighMark=_WwpContainmentMulticastHighMark_Object((1,3,6,1,4,1,6141,2,55,1,1,2,1,3),_WwpContainmentMulticastHighMark_Type())
wwpContainmentMulticastHighMark.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentMulticastHighMark.setStatus(_A)
class _WwpContainmentMulticastLowMark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpContainmentMulticastLowMark_Type.__name__=_B
_WwpContainmentMulticastLowMark_Object=MibTableColumn
wwpContainmentMulticastLowMark=_WwpContainmentMulticastLowMark_Object((1,3,6,1,4,1,6141,2,55,1,1,2,1,4),_WwpContainmentMulticastLowMark_Type())
wwpContainmentMulticastLowMark.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentMulticastLowMark.setStatus(_A)
class _WwpContainmentMulticastTrapsEnable_Type(TruthValue):defaultValue=1
_WwpContainmentMulticastTrapsEnable_Type.__name__=_F
_WwpContainmentMulticastTrapsEnable_Object=MibTableColumn
wwpContainmentMulticastTrapsEnable=_WwpContainmentMulticastTrapsEnable_Object((1,3,6,1,4,1,6141,2,55,1,1,2,1,5),_WwpContainmentMulticastTrapsEnable_Type())
wwpContainmentMulticastTrapsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpContainmentMulticastTrapsEnable.setStatus(_A)
class _WwpContainmentMulticastState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),(_K,2),(_L,3),(_M,4)))
_WwpContainmentMulticastState_Type.__name__=_B
_WwpContainmentMulticastState_Object=MibTableColumn
wwpContainmentMulticastState=_WwpContainmentMulticastState_Object((1,3,6,1,4,1,6141,2,55,1,1,2,1,6),_WwpContainmentMulticastState_Type())
wwpContainmentMulticastState.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpContainmentMulticastState.setStatus(_A)
_WwpContainmentMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpContainmentMIBNotificationPrefix=_WwpContainmentMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,55,2))
_WwpContainmentMIBNotifications_ObjectIdentity=ObjectIdentity
wwpContainmentMIBNotifications=_WwpContainmentMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,55,2,0))
_WwpContainmentMIBConformance_ObjectIdentity=ObjectIdentity
wwpContainmentMIBConformance=_WwpContainmentMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,55,3))
_WwpContainmentMIBCompliances_ObjectIdentity=ObjectIdentity
wwpContainmentMIBCompliances=_WwpContainmentMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,55,3,1))
_WwpContainmentMIBGroups_ObjectIdentity=ObjectIdentity
wwpContainmentMIBGroups=_WwpContainmentMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,55,3,2))
wwpContainmentNotification=NotificationType((1,3,6,1,4,1,6141,2,55,2,0,1))
wwpContainmentNotification.setObjects(*((_D,_O),(_D,_P)))
if mibBuilder.loadTexts:wwpContainmentNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'wwpContainmentMIB':wwpContainmentMIB,'wwpContainmentMIBObjects':wwpContainmentMIBObjects,'wwpContainment':wwpContainment,'wwpContainmentBroadcastTable':wwpContainmentBroadcastTable,'wwpContainmentBroadcastEntry':wwpContainmentBroadcastEntry,_G:wwpContainmentBroadcastPortId,'wwpContainmentBroadcastAction':wwpContainmentBroadcastAction,'wwpContainmentBroadcastHighMark':wwpContainmentBroadcastHighMark,'wwpContainmentBroadcastLowMark':wwpContainmentBroadcastLowMark,'wwpContainmentBroadcastTrapsEnable':wwpContainmentBroadcastTrapsEnable,_O:wwpContainmentBroadcastState,'wwpContainmentMulticastTable':wwpContainmentMulticastTable,'wwpContainmentMulticastEntry':wwpContainmentMulticastEntry,_N:wwpContainmentMulticastPortId,'wwpContainmentMulticastAction':wwpContainmentMulticastAction,'wwpContainmentMulticastHighMark':wwpContainmentMulticastHighMark,'wwpContainmentMulticastLowMark':wwpContainmentMulticastLowMark,'wwpContainmentMulticastTrapsEnable':wwpContainmentMulticastTrapsEnable,_P:wwpContainmentMulticastState,'wwpContainmentMIBNotificationPrefix':wwpContainmentMIBNotificationPrefix,'wwpContainmentMIBNotifications':wwpContainmentMIBNotifications,'wwpContainmentNotification':wwpContainmentNotification,'wwpContainmentMIBConformance':wwpContainmentMIBConformance,'wwpContainmentMIBCompliances':wwpContainmentMIBCompliances,'wwpContainmentMIBGroups':wwpContainmentMIBGroups})