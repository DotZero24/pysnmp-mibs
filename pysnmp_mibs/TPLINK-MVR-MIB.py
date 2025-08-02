_L='read-create'
_K='tpMvrGroupIPAddress'
_J='TPLINK-MVR-MIB'
_I='ifIndex'
_H='IF-MIB'
_G='enable'
_F='disable'
_E='OctetString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkMvrMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,99))
if mibBuilder.loadTexts:tplinkMvrMIB.setRevisions(('2012-12-14 14:32',))
_TplinkMvrMIBObjects_ObjectIdentity=ObjectIdentity
tplinkMvrMIBObjects=_TplinkMvrMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,99,1))
_TpMvrGlobalConfig_ObjectIdentity=ObjectIdentity
tpMvrGlobalConfig=_TpMvrGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,99,1,1))
class _TpMvrAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpMvrAdminMode_Type.__name__=_B
_TpMvrAdminMode_Object=MibScalar
tpMvrAdminMode=_TpMvrAdminMode_Object((1,3,6,1,4,1,11863,6,99,1,1,1),_TpMvrAdminMode_Type())
tpMvrAdminMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrAdminMode.setStatus(_A)
class _TpMvrModeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('compatible',1),('dynamic',2)))
_TpMvrModeType_Type.__name__=_B
_TpMvrModeType_Object=MibScalar
tpMvrModeType=_TpMvrModeType_Object((1,3,6,1,4,1,11863,6,99,1,1,2),_TpMvrModeType_Type())
tpMvrModeType.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrModeType.setStatus(_A)
class _TpMvrMulticastVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_TpMvrMulticastVlanId_Type.__name__=_B
_TpMvrMulticastVlanId_Object=MibScalar
tpMvrMulticastVlanId=_TpMvrMulticastVlanId_Object((1,3,6,1,4,1,11863,6,99,1,1,3),_TpMvrMulticastVlanId_Type())
tpMvrMulticastVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrMulticastVlanId.setStatus(_A)
_TpMvrMaxMulticastGroupsCount_Type=Integer32
_TpMvrMaxMulticastGroupsCount_Object=MibScalar
tpMvrMaxMulticastGroupsCount=_TpMvrMaxMulticastGroupsCount_Object((1,3,6,1,4,1,11863,6,99,1,1,4),_TpMvrMaxMulticastGroupsCount_Type())
tpMvrMaxMulticastGroupsCount.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMvrMaxMulticastGroupsCount.setStatus(_A)
_TpMvrCurrentMulticastGroupsCount_Type=Integer32
_TpMvrCurrentMulticastGroupsCount_Object=MibScalar
tpMvrCurrentMulticastGroupsCount=_TpMvrCurrentMulticastGroupsCount_Object((1,3,6,1,4,1,11863,6,99,1,1,5),_TpMvrCurrentMulticastGroupsCount_Type())
tpMvrCurrentMulticastGroupsCount.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMvrCurrentMulticastGroupsCount.setStatus(_A)
class _TpMvrQueryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_TpMvrQueryTime_Type.__name__=_B
_TpMvrQueryTime_Object=MibScalar
tpMvrQueryTime=_TpMvrQueryTime_Object((1,3,6,1,4,1,11863,6,99,1,1,6),_TpMvrQueryTime_Type())
tpMvrQueryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrQueryTime.setStatus(_A)
_TpMvrPortConfig_ObjectIdentity=ObjectIdentity
tpMvrPortConfig=_TpMvrPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,99,1,2))
_TpMvrPortTable_Object=MibTable
tpMvrPortTable=_TpMvrPortTable_Object((1,3,6,1,4,1,11863,6,99,1,2,1))
if mibBuilder.loadTexts:tpMvrPortTable.setStatus(_A)
_TpMvrPortEntry_Object=MibTableRow
tpMvrPortEntry=_TpMvrPortEntry_Object((1,3,6,1,4,1,11863,6,99,1,2,1,1))
tpMvrPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:tpMvrPortEntry.setStatus(_A)
class _TpMvrPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpMvrPortEnable_Type.__name__=_B
_TpMvrPortEnable_Object=MibTableColumn
tpMvrPortEnable=_TpMvrPortEnable_Object((1,3,6,1,4,1,11863,6,99,1,2,1,1,2),_TpMvrPortEnable_Type())
tpMvrPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrPortEnable.setStatus(_A)
class _TpMvrPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('source',1),('receiver',2)))
_TpMvrPortType_Type.__name__=_B
_TpMvrPortType_Object=MibTableColumn
tpMvrPortType=_TpMvrPortType_Object((1,3,6,1,4,1,11863,6,99,1,2,1,1,3),_TpMvrPortType_Type())
tpMvrPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrPortType.setStatus(_A)
class _TpMvrPortImmediateLeaveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_TpMvrPortImmediateLeaveMode_Type.__name__=_B
_TpMvrPortImmediateLeaveMode_Object=MibTableColumn
tpMvrPortImmediateLeaveMode=_TpMvrPortImmediateLeaveMode_Object((1,3,6,1,4,1,11863,6,99,1,2,1,1,4),_TpMvrPortImmediateLeaveMode_Type())
tpMvrPortImmediateLeaveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrPortImmediateLeaveMode.setStatus(_A)
class _TpMvrPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('activeInVlan',1),('activeNotInVlan',2),('inactiveInVlan',3),('inactiveNotInVlan',4)))
_TpMvrPortStatus_Type.__name__=_B
_TpMvrPortStatus_Object=MibTableColumn
tpMvrPortStatus=_TpMvrPortStatus_Object((1,3,6,1,4,1,11863,6,99,1,2,1,1,5),_TpMvrPortStatus_Type())
tpMvrPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMvrPortStatus.setStatus(_A)
_TpMvrGroupConfig_ObjectIdentity=ObjectIdentity
tpMvrGroupConfig=_TpMvrGroupConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,99,1,3))
_TpMvrGroupTable_Object=MibTable
tpMvrGroupTable=_TpMvrGroupTable_Object((1,3,6,1,4,1,11863,6,99,1,3,1))
if mibBuilder.loadTexts:tpMvrGroupTable.setStatus(_A)
_TpMvrGroupEntry_Object=MibTableRow
tpMvrGroupEntry=_TpMvrGroupEntry_Object((1,3,6,1,4,1,11863,6,99,1,3,1,1))
tpMvrGroupEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:tpMvrGroupEntry.setStatus(_A)
_TpMvrGroupIPAddress_Type=IpAddress
_TpMvrGroupIPAddress_Object=MibTableColumn
tpMvrGroupIPAddress=_TpMvrGroupIPAddress_Object((1,3,6,1,4,1,11863,6,99,1,3,1,1,1),_TpMvrGroupIPAddress_Type())
tpMvrGroupIPAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:tpMvrGroupIPAddress.setStatus(_A)
class _TpMvrGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_TpMvrGroupStatus_Type.__name__=_B
_TpMvrGroupStatus_Object=MibTableColumn
tpMvrGroupStatus=_TpMvrGroupStatus_Object((1,3,6,1,4,1,11863,6,99,1,3,1,1,2),_TpMvrGroupStatus_Type())
tpMvrGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMvrGroupStatus.setStatus(_A)
class _TpMvrGroupForwardPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMvrGroupForwardPorts_Type.__name__=_E
_TpMvrGroupForwardPorts_Object=MibTableColumn
tpMvrGroupForwardPorts=_TpMvrGroupForwardPorts_Object((1,3,6,1,4,1,11863,6,99,1,3,1,1,3),_TpMvrGroupForwardPorts_Type())
tpMvrGroupForwardPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMvrGroupForwardPorts.setStatus(_A)
class _TpMvrGroupAddForwardPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMvrGroupAddForwardPorts_Type.__name__=_E
_TpMvrGroupAddForwardPorts_Object=MibTableColumn
tpMvrGroupAddForwardPorts=_TpMvrGroupAddForwardPorts_Object((1,3,6,1,4,1,11863,6,99,1,3,1,1,4),_TpMvrGroupAddForwardPorts_Type())
tpMvrGroupAddForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrGroupAddForwardPorts.setStatus(_A)
class _TpMvrGroupDelForwardPorts_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMvrGroupDelForwardPorts_Type.__name__=_E
_TpMvrGroupDelForwardPorts_Object=MibTableColumn
tpMvrGroupDelForwardPorts=_TpMvrGroupDelForwardPorts_Object((1,3,6,1,4,1,11863,6,99,1,3,1,1,5),_TpMvrGroupDelForwardPorts_Type())
tpMvrGroupDelForwardPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMvrGroupDelForwardPorts.setStatus(_A)
_TpMvrGroupRowStatus_Type=TPRowStatus
_TpMvrGroupRowStatus_Object=MibTableColumn
tpMvrGroupRowStatus=_TpMvrGroupRowStatus_Object((1,3,6,1,4,1,11863,6,99,1,3,1,1,6),_TpMvrGroupRowStatus_Type())
tpMvrGroupRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:tpMvrGroupRowStatus.setStatus(_A)
_TplinkMvrNotifications_ObjectIdentity=ObjectIdentity
tplinkMvrNotifications=_TplinkMvrNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,99,2))
mibBuilder.exportSymbols(_J,**{'tplinkMvrMIB':tplinkMvrMIB,'tplinkMvrMIBObjects':tplinkMvrMIBObjects,'tpMvrGlobalConfig':tpMvrGlobalConfig,'tpMvrAdminMode':tpMvrAdminMode,'tpMvrModeType':tpMvrModeType,'tpMvrMulticastVlanId':tpMvrMulticastVlanId,'tpMvrMaxMulticastGroupsCount':tpMvrMaxMulticastGroupsCount,'tpMvrCurrentMulticastGroupsCount':tpMvrCurrentMulticastGroupsCount,'tpMvrQueryTime':tpMvrQueryTime,'tpMvrPortConfig':tpMvrPortConfig,'tpMvrPortTable':tpMvrPortTable,'tpMvrPortEntry':tpMvrPortEntry,'tpMvrPortEnable':tpMvrPortEnable,'tpMvrPortType':tpMvrPortType,'tpMvrPortImmediateLeaveMode':tpMvrPortImmediateLeaveMode,'tpMvrPortStatus':tpMvrPortStatus,'tpMvrGroupConfig':tpMvrGroupConfig,'tpMvrGroupTable':tpMvrGroupTable,'tpMvrGroupEntry':tpMvrGroupEntry,_K:tpMvrGroupIPAddress,'tpMvrGroupStatus':tpMvrGroupStatus,'tpMvrGroupForwardPorts':tpMvrGroupForwardPorts,'tpMvrGroupAddForwardPorts':tpMvrGroupAddForwardPorts,'tpMvrGroupDelForwardPorts':tpMvrGroupDelForwardPorts,'tpMvrGroupRowStatus':tpMvrGroupRowStatus,'tplinkMvrNotifications':tplinkMvrNotifications})