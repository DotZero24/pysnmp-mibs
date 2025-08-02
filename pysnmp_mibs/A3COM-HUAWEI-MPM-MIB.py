_S='h3cHostStaticJoinAddress'
_R='h3cHostStaticJoinAddressType'
_Q='h3cHostStaticJoinVlanID'
_P='h3cMPortConfigVlanID'
_O='h3cMPortGroupAddress'
_N='h3cMPortGroupAddressType'
_M='h3cMPortGroupVlanID'
_L='h3cMPortGroupJoinAddress'
_K='h3cMPortGroupJoinAddressType'
_J='h3cMPortGroupJoinVlanID'
_I='Integer32'
_H='EnabledStatus'
_G='read-only'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='not-accessible'
_B='A3COM-HUAWEI-MPM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cMpm=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,51))
if mibBuilder.loadTexts:h3cMpm.setRevisions(('2005-03-22 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_H3cMPMObject_ObjectIdentity=ObjectIdentity
h3cMPMObject=_H3cMPMObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,51,1))
_H3cMPortGroupLimitMinNumber_Type=Unsigned32
_H3cMPortGroupLimitMinNumber_Object=MibScalar
h3cMPortGroupLimitMinNumber=_H3cMPortGroupLimitMinNumber_Object((1,3,6,1,4,1,43,45,1,10,2,51,1,1),_H3cMPortGroupLimitMinNumber_Type())
h3cMPortGroupLimitMinNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMPortGroupLimitMinNumber.setStatus(_A)
_H3cMPortGroupLimitMaxNumber_Type=Unsigned32
_H3cMPortGroupLimitMaxNumber_Object=MibScalar
h3cMPortGroupLimitMaxNumber=_H3cMPortGroupLimitMaxNumber_Object((1,3,6,1,4,1,43,45,1,10,2,51,1,2),_H3cMPortGroupLimitMaxNumber_Type())
h3cMPortGroupLimitMaxNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMPortGroupLimitMaxNumber.setStatus(_A)
_H3cMPMTable_ObjectIdentity=ObjectIdentity
h3cMPMTable=_H3cMPMTable_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,51,2))
_H3cMPortGroupJoinTable_Object=MibTable
h3cMPortGroupJoinTable=_H3cMPortGroupJoinTable_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,1))
if mibBuilder.loadTexts:h3cMPortGroupJoinTable.setStatus(_A)
_H3cMPortGroupJoinEntry_Object=MibTableRow
h3cMPortGroupJoinEntry=_H3cMPortGroupJoinEntry_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,1,1))
h3cMPortGroupJoinEntry.setIndexNames((0,_E,_F),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:h3cMPortGroupJoinEntry.setStatus(_A)
_H3cMPortGroupJoinVlanID_Type=Integer32
_H3cMPortGroupJoinVlanID_Object=MibTableColumn
h3cMPortGroupJoinVlanID=_H3cMPortGroupJoinVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,1,1,1),_H3cMPortGroupJoinVlanID_Type())
h3cMPortGroupJoinVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMPortGroupJoinVlanID.setStatus(_A)
_H3cMPortGroupJoinAddressType_Type=InetAddressType
_H3cMPortGroupJoinAddressType_Object=MibTableColumn
h3cMPortGroupJoinAddressType=_H3cMPortGroupJoinAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,1,1,2),_H3cMPortGroupJoinAddressType_Type())
h3cMPortGroupJoinAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMPortGroupJoinAddressType.setStatus(_A)
_H3cMPortGroupJoinAddress_Type=InetAddress
_H3cMPortGroupJoinAddress_Object=MibTableColumn
h3cMPortGroupJoinAddress=_H3cMPortGroupJoinAddress_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,1,1,3),_H3cMPortGroupJoinAddress_Type())
h3cMPortGroupJoinAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMPortGroupJoinAddress.setStatus(_A)
_H3cMPortGroupJoinStatus_Type=RowStatus
_H3cMPortGroupJoinStatus_Object=MibTableColumn
h3cMPortGroupJoinStatus=_H3cMPortGroupJoinStatus_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,1,1,4),_H3cMPortGroupJoinStatus_Type())
h3cMPortGroupJoinStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMPortGroupJoinStatus.setStatus(_A)
_H3cMPortGroupTable_Object=MibTable
h3cMPortGroupTable=_H3cMPortGroupTable_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,2))
if mibBuilder.loadTexts:h3cMPortGroupTable.setStatus(_A)
_H3cMPortGroupEntry_Object=MibTableRow
h3cMPortGroupEntry=_H3cMPortGroupEntry_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,2,1))
h3cMPortGroupEntry.setIndexNames((0,_E,_F),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:h3cMPortGroupEntry.setStatus(_A)
_H3cMPortGroupVlanID_Type=Integer32
_H3cMPortGroupVlanID_Object=MibTableColumn
h3cMPortGroupVlanID=_H3cMPortGroupVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,2,1,1),_H3cMPortGroupVlanID_Type())
h3cMPortGroupVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMPortGroupVlanID.setStatus(_A)
_H3cMPortGroupAddressType_Type=InetAddressType
_H3cMPortGroupAddressType_Object=MibTableColumn
h3cMPortGroupAddressType=_H3cMPortGroupAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,2,1,2),_H3cMPortGroupAddressType_Type())
h3cMPortGroupAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMPortGroupAddressType.setStatus(_A)
_H3cMPortGroupAddress_Type=InetAddress
_H3cMPortGroupAddress_Object=MibTableColumn
h3cMPortGroupAddress=_H3cMPortGroupAddress_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,2,1,3),_H3cMPortGroupAddress_Type())
h3cMPortGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMPortGroupAddress.setStatus(_A)
_H3cMPortConfigTable_Object=MibTable
h3cMPortConfigTable=_H3cMPortConfigTable_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3))
if mibBuilder.loadTexts:h3cMPortConfigTable.setStatus(_A)
_H3cMPortConfigEntry_Object=MibTableRow
h3cMPortConfigEntry=_H3cMPortConfigEntry_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3,1))
h3cMPortConfigEntry.setIndexNames((0,_E,_F),(0,_B,_P))
if mibBuilder.loadTexts:h3cMPortConfigEntry.setStatus(_A)
_H3cMPortConfigVlanID_Type=Integer32
_H3cMPortConfigVlanID_Object=MibTableColumn
h3cMPortConfigVlanID=_H3cMPortConfigVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3,1,1),_H3cMPortConfigVlanID_Type())
h3cMPortConfigVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMPortConfigVlanID.setStatus(_A)
_H3cMPortGroupLimitNumber_Type=Unsigned32
_H3cMPortGroupLimitNumber_Object=MibTableColumn
h3cMPortGroupLimitNumber=_H3cMPortGroupLimitNumber_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3,1,2),_H3cMPortGroupLimitNumber_Type())
h3cMPortGroupLimitNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMPortGroupLimitNumber.setStatus(_A)
class _H3cMPortFastLeaveStatus_Type(EnabledStatus):defaultValue=2
_H3cMPortFastLeaveStatus_Type.__name__=_H
_H3cMPortFastLeaveStatus_Object=MibTableColumn
h3cMPortFastLeaveStatus=_H3cMPortFastLeaveStatus_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3,1,3),_H3cMPortFastLeaveStatus_Type())
h3cMPortFastLeaveStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMPortFastLeaveStatus.setStatus(_A)
class _H3cMPortGroupPolicyParameter_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2999))
_H3cMPortGroupPolicyParameter_Type.__name__=_I
_H3cMPortGroupPolicyParameter_Object=MibTableColumn
h3cMPortGroupPolicyParameter=_H3cMPortGroupPolicyParameter_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3,1,4),_H3cMPortGroupPolicyParameter_Type())
h3cMPortGroupPolicyParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMPortGroupPolicyParameter.setStatus(_A)
_H3cMPortConfigRowStatus_Type=RowStatus
_H3cMPortConfigRowStatus_Object=MibTableColumn
h3cMPortConfigRowStatus=_H3cMPortConfigRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3,1,5),_H3cMPortConfigRowStatus_Type())
h3cMPortConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMPortConfigRowStatus.setStatus(_A)
class _H3cMPortGroupLimitReplace_Type(EnabledStatus):defaultValue=2
_H3cMPortGroupLimitReplace_Type.__name__=_H
_H3cMPortGroupLimitReplace_Object=MibTableColumn
h3cMPortGroupLimitReplace=_H3cMPortGroupLimitReplace_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,3,1,6),_H3cMPortGroupLimitReplace_Type())
h3cMPortGroupLimitReplace.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMPortGroupLimitReplace.setStatus(_A)
_H3cHostStaticJoinTable_Object=MibTable
h3cHostStaticJoinTable=_H3cHostStaticJoinTable_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,4))
if mibBuilder.loadTexts:h3cHostStaticJoinTable.setStatus(_A)
_H3cHostStaticJoinEntry_Object=MibTableRow
h3cHostStaticJoinEntry=_H3cHostStaticJoinEntry_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,4,1))
h3cHostStaticJoinEntry.setIndexNames((0,_E,_F),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:h3cHostStaticJoinEntry.setStatus(_A)
_H3cHostStaticJoinVlanID_Type=Integer32
_H3cHostStaticJoinVlanID_Object=MibTableColumn
h3cHostStaticJoinVlanID=_H3cHostStaticJoinVlanID_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,4,1,1),_H3cHostStaticJoinVlanID_Type())
h3cHostStaticJoinVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cHostStaticJoinVlanID.setStatus(_A)
_H3cHostStaticJoinAddressType_Type=InetAddressType
_H3cHostStaticJoinAddressType_Object=MibTableColumn
h3cHostStaticJoinAddressType=_H3cHostStaticJoinAddressType_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,4,1,2),_H3cHostStaticJoinAddressType_Type())
h3cHostStaticJoinAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cHostStaticJoinAddressType.setStatus(_A)
_H3cHostStaticJoinAddress_Type=InetAddress
_H3cHostStaticJoinAddress_Object=MibTableColumn
h3cHostStaticJoinAddress=_H3cHostStaticJoinAddress_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,4,1,3),_H3cHostStaticJoinAddress_Type())
h3cHostStaticJoinAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cHostStaticJoinAddress.setStatus(_A)
_H3cHostStaticJoinStatus_Type=RowStatus
_H3cHostStaticJoinStatus_Object=MibTableColumn
h3cHostStaticJoinStatus=_H3cHostStaticJoinStatus_Object((1,3,6,1,4,1,43,45,1,10,2,51,2,4,1,4),_H3cHostStaticJoinStatus_Type())
h3cHostStaticJoinStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cHostStaticJoinStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:EnabledStatus,'h3cMpm':h3cMpm,'h3cMPMObject':h3cMPMObject,'h3cMPortGroupLimitMinNumber':h3cMPortGroupLimitMinNumber,'h3cMPortGroupLimitMaxNumber':h3cMPortGroupLimitMaxNumber,'h3cMPMTable':h3cMPMTable,'h3cMPortGroupJoinTable':h3cMPortGroupJoinTable,'h3cMPortGroupJoinEntry':h3cMPortGroupJoinEntry,_J:h3cMPortGroupJoinVlanID,_K:h3cMPortGroupJoinAddressType,_L:h3cMPortGroupJoinAddress,'h3cMPortGroupJoinStatus':h3cMPortGroupJoinStatus,'h3cMPortGroupTable':h3cMPortGroupTable,'h3cMPortGroupEntry':h3cMPortGroupEntry,_M:h3cMPortGroupVlanID,_N:h3cMPortGroupAddressType,_O:h3cMPortGroupAddress,'h3cMPortConfigTable':h3cMPortConfigTable,'h3cMPortConfigEntry':h3cMPortConfigEntry,_P:h3cMPortConfigVlanID,'h3cMPortGroupLimitNumber':h3cMPortGroupLimitNumber,'h3cMPortFastLeaveStatus':h3cMPortFastLeaveStatus,'h3cMPortGroupPolicyParameter':h3cMPortGroupPolicyParameter,'h3cMPortConfigRowStatus':h3cMPortConfigRowStatus,'h3cMPortGroupLimitReplace':h3cMPortGroupLimitReplace,'h3cHostStaticJoinTable':h3cHostStaticJoinTable,'h3cHostStaticJoinEntry':h3cHostStaticJoinEntry,_Q:h3cHostStaticJoinVlanID,_R:h3cHostStaticJoinAddressType,_S:h3cHostStaticJoinAddress,'h3cHostStaticJoinStatus':h3cHostStaticJoinStatus})