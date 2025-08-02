_K='read-only'
_J='DisplayString'
_I='ifIndex'
_H='IF-MIB'
_G='dot1qVlanId'
_F='TPLINK-DOT1Q-VLAN-MIB'
_E='read-write'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkDot1qVlanMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,14))
if mibBuilder.loadTexts:tplinkDot1qVlanMIB.setRevisions(('2009-08-03 00:00',))
_TplinkDot1qVlanMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDot1qVlanMIBObjects=_TplinkDot1qVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,14,1))
_VlanPortConfig_ObjectIdentity=ObjectIdentity
vlanPortConfig=_VlanPortConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,14,1,1))
_VlanPortConfigTable_Object=MibTable
vlanPortConfigTable=_VlanPortConfigTable_Object((1,3,6,1,4,1,11863,6,14,1,1,1))
if mibBuilder.loadTexts:vlanPortConfigTable.setStatus(_A)
_VlanPortConifgEntry_Object=MibTableRow
vlanPortConifgEntry=_VlanPortConifgEntry_Object((1,3,6,1,4,1,11863,6,14,1,1,1,1))
vlanPortConifgEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:vlanPortConifgEntry.setStatus(_A)
class _VlanPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_VlanPortNumber_Type.__name__=_D
_VlanPortNumber_Object=MibTableColumn
vlanPortNumber=_VlanPortNumber_Object((1,3,6,1,4,1,11863,6,14,1,1,1,1,1),_VlanPortNumber_Type())
vlanPortNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:vlanPortNumber.setStatus(_A)
class _VlanPortPvid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_VlanPortPvid_Type.__name__=_C
_VlanPortPvid_Object=MibTableColumn
vlanPortPvid=_VlanPortPvid_Object((1,3,6,1,4,1,11863,6,14,1,1,1,1,2),_VlanPortPvid_Type())
vlanPortPvid.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanPortPvid.setStatus(_A)
class _VlanPortIngressCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_VlanPortIngressCheck_Type.__name__=_C
_VlanPortIngressCheck_Object=MibTableColumn
vlanPortIngressCheck=_VlanPortIngressCheck_Object((1,3,6,1,4,1,11863,6,14,1,1,1,1,3),_VlanPortIngressCheck_Type())
vlanPortIngressCheck.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanPortIngressCheck.setStatus(_A)
class _VlanPortAcceptFrameType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('all',0),('tagged-only',1)))
_VlanPortAcceptFrameType_Type.__name__=_C
_VlanPortAcceptFrameType_Object=MibTableColumn
vlanPortAcceptFrameType=_VlanPortAcceptFrameType_Object((1,3,6,1,4,1,11863,6,14,1,1,1,1,4),_VlanPortAcceptFrameType_Type())
vlanPortAcceptFrameType.setMaxAccess(_E)
if mibBuilder.loadTexts:vlanPortAcceptFrameType.setStatus(_A)
class _VlanPortLag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_VlanPortLag_Type.__name__=_J
_VlanPortLag_Object=MibTableColumn
vlanPortLag=_VlanPortLag_Object((1,3,6,1,4,1,11863,6,14,1,1,1,1,5),_VlanPortLag_Type())
vlanPortLag.setMaxAccess(_K)
if mibBuilder.loadTexts:vlanPortLag.setStatus(_A)
_VlanConfig_ObjectIdentity=ObjectIdentity
vlanConfig=_VlanConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,14,1,2))
_VlanConfigTable_Object=MibTable
vlanConfigTable=_VlanConfigTable_Object((1,3,6,1,4,1,11863,6,14,1,2,1))
if mibBuilder.loadTexts:vlanConfigTable.setStatus(_A)
_VlanConfigEntry_Object=MibTableRow
vlanConfigEntry=_VlanConfigEntry_Object((1,3,6,1,4,1,11863,6,14,1,2,1,1))
vlanConfigEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:vlanConfigEntry.setStatus(_A)
class _Dot1qVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Dot1qVlanId_Type.__name__=_C
_Dot1qVlanId_Object=MibTableColumn
dot1qVlanId=_Dot1qVlanId_Object((1,3,6,1,4,1,11863,6,14,1,2,1,1,1),_Dot1qVlanId_Type())
dot1qVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qVlanId.setStatus(_A)
class _Dot1qVlanDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Dot1qVlanDescription_Type.__name__=_D
_Dot1qVlanDescription_Object=MibTableColumn
dot1qVlanDescription=_Dot1qVlanDescription_Object((1,3,6,1,4,1,11863,6,14,1,2,1,1,2),_Dot1qVlanDescription_Type())
dot1qVlanDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qVlanDescription.setStatus(_A)
_VlanTagPortMemberAdd_Type=OctetString
_VlanTagPortMemberAdd_Object=MibTableColumn
vlanTagPortMemberAdd=_VlanTagPortMemberAdd_Object((1,3,6,1,4,1,11863,6,14,1,2,1,1,3),_VlanTagPortMemberAdd_Type())
vlanTagPortMemberAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanTagPortMemberAdd.setStatus(_A)
_VlanUntagPortMemberAdd_Type=OctetString
_VlanUntagPortMemberAdd_Object=MibTableColumn
vlanUntagPortMemberAdd=_VlanUntagPortMemberAdd_Object((1,3,6,1,4,1,11863,6,14,1,2,1,1,4),_VlanUntagPortMemberAdd_Type())
vlanUntagPortMemberAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanUntagPortMemberAdd.setStatus(_A)
_VlanPortMemberRemove_Type=OctetString
_VlanPortMemberRemove_Object=MibTableColumn
vlanPortMemberRemove=_VlanPortMemberRemove_Object((1,3,6,1,4,1,11863,6,14,1,2,1,1,5),_VlanPortMemberRemove_Type())
vlanPortMemberRemove.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanPortMemberRemove.setStatus(_A)
_Dot1qVlanStatus_Type=TPRowStatus
_Dot1qVlanStatus_Object=MibTableColumn
dot1qVlanStatus=_Dot1qVlanStatus_Object((1,3,6,1,4,1,11863,6,14,1,2,1,1,6),_Dot1qVlanStatus_Type())
dot1qVlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1qVlanStatus.setStatus(_A)
_TplinkDot1qVlanNotifications_ObjectIdentity=ObjectIdentity
tplinkDot1qVlanNotifications=_TplinkDot1qVlanNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,14,2))
vlanTableCreate=NotificationType((1,3,6,1,4,1,11863,6,14,2,1))
vlanTableCreate.setObjects((_F,_G))
if mibBuilder.loadTexts:vlanTableCreate.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'tplinkDot1qVlanMIB':tplinkDot1qVlanMIB,'tplinkDot1qVlanMIBObjects':tplinkDot1qVlanMIBObjects,'vlanPortConfig':vlanPortConfig,'vlanPortConfigTable':vlanPortConfigTable,'vlanPortConifgEntry':vlanPortConifgEntry,'vlanPortNumber':vlanPortNumber,'vlanPortPvid':vlanPortPvid,'vlanPortIngressCheck':vlanPortIngressCheck,'vlanPortAcceptFrameType':vlanPortAcceptFrameType,'vlanPortLag':vlanPortLag,'vlanConfig':vlanConfig,'vlanConfigTable':vlanConfigTable,'vlanConfigEntry':vlanConfigEntry,_G:dot1qVlanId,'dot1qVlanDescription':dot1qVlanDescription,'vlanTagPortMemberAdd':vlanTagPortMemberAdd,'vlanUntagPortMemberAdd':vlanUntagPortMemberAdd,'vlanPortMemberRemove':vlanPortMemberRemove,'dot1qVlanStatus':dot1qVlanStatus,'tplinkDot1qVlanNotifications':tplinkDot1qVlanNotifications,'vlanTableCreate':vlanTableCreate})