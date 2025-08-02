_S='hpnicfHostStaticJoinAddress'
_R='hpnicfHostStaticJoinAddressType'
_Q='hpnicfHostStaticJoinVlanID'
_P='hpnicfMPortConfigVlanID'
_O='hpnicfMPortGroupAddress'
_N='hpnicfMPortGroupAddressType'
_M='hpnicfMPortGroupVlanID'
_L='hpnicfMPortGroupJoinAddress'
_K='hpnicfMPortGroupJoinAddressType'
_J='hpnicfMPortGroupJoinVlanID'
_I='Integer32'
_H='EnabledStatus'
_G='read-only'
_F='ifIndex'
_E='IF-MIB'
_D='read-create'
_C='not-accessible'
_B='HPN-ICF-MPM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfMpm=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,51))
if mibBuilder.loadTexts:hpnicfMpm.setRevisions(('2005-03-22 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfMPMObject_ObjectIdentity=ObjectIdentity
hpnicfMPMObject=_HpnicfMPMObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,51,1))
_HpnicfMPortGroupLimitMinNumber_Type=Unsigned32
_HpnicfMPortGroupLimitMinNumber_Object=MibScalar
hpnicfMPortGroupLimitMinNumber=_HpnicfMPortGroupLimitMinNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,1,1),_HpnicfMPortGroupLimitMinNumber_Type())
hpnicfMPortGroupLimitMinNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMPortGroupLimitMinNumber.setStatus(_A)
_HpnicfMPortGroupLimitMaxNumber_Type=Unsigned32
_HpnicfMPortGroupLimitMaxNumber_Object=MibScalar
hpnicfMPortGroupLimitMaxNumber=_HpnicfMPortGroupLimitMaxNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,1,2),_HpnicfMPortGroupLimitMaxNumber_Type())
hpnicfMPortGroupLimitMaxNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMPortGroupLimitMaxNumber.setStatus(_A)
_HpnicfMPMTable_ObjectIdentity=ObjectIdentity
hpnicfMPMTable=_HpnicfMPMTable_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,51,2))
_HpnicfMPortGroupJoinTable_Object=MibTable
hpnicfMPortGroupJoinTable=_HpnicfMPortGroupJoinTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,1))
if mibBuilder.loadTexts:hpnicfMPortGroupJoinTable.setStatus(_A)
_HpnicfMPortGroupJoinEntry_Object=MibTableRow
hpnicfMPortGroupJoinEntry=_HpnicfMPortGroupJoinEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,1,1))
hpnicfMPortGroupJoinEntry.setIndexNames((0,_E,_F),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfMPortGroupJoinEntry.setStatus(_A)
_HpnicfMPortGroupJoinVlanID_Type=Integer32
_HpnicfMPortGroupJoinVlanID_Object=MibTableColumn
hpnicfMPortGroupJoinVlanID=_HpnicfMPortGroupJoinVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,1,1,1),_HpnicfMPortGroupJoinVlanID_Type())
hpnicfMPortGroupJoinVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMPortGroupJoinVlanID.setStatus(_A)
_HpnicfMPortGroupJoinAddressType_Type=InetAddressType
_HpnicfMPortGroupJoinAddressType_Object=MibTableColumn
hpnicfMPortGroupJoinAddressType=_HpnicfMPortGroupJoinAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,1,1,2),_HpnicfMPortGroupJoinAddressType_Type())
hpnicfMPortGroupJoinAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMPortGroupJoinAddressType.setStatus(_A)
_HpnicfMPortGroupJoinAddress_Type=InetAddress
_HpnicfMPortGroupJoinAddress_Object=MibTableColumn
hpnicfMPortGroupJoinAddress=_HpnicfMPortGroupJoinAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,1,1,3),_HpnicfMPortGroupJoinAddress_Type())
hpnicfMPortGroupJoinAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMPortGroupJoinAddress.setStatus(_A)
_HpnicfMPortGroupJoinStatus_Type=RowStatus
_HpnicfMPortGroupJoinStatus_Object=MibTableColumn
hpnicfMPortGroupJoinStatus=_HpnicfMPortGroupJoinStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,1,1,4),_HpnicfMPortGroupJoinStatus_Type())
hpnicfMPortGroupJoinStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMPortGroupJoinStatus.setStatus(_A)
_HpnicfMPortGroupTable_Object=MibTable
hpnicfMPortGroupTable=_HpnicfMPortGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,2))
if mibBuilder.loadTexts:hpnicfMPortGroupTable.setStatus(_A)
_HpnicfMPortGroupEntry_Object=MibTableRow
hpnicfMPortGroupEntry=_HpnicfMPortGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,2,1))
hpnicfMPortGroupEntry.setIndexNames((0,_E,_F),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:hpnicfMPortGroupEntry.setStatus(_A)
_HpnicfMPortGroupVlanID_Type=Integer32
_HpnicfMPortGroupVlanID_Object=MibTableColumn
hpnicfMPortGroupVlanID=_HpnicfMPortGroupVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,2,1,1),_HpnicfMPortGroupVlanID_Type())
hpnicfMPortGroupVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMPortGroupVlanID.setStatus(_A)
_HpnicfMPortGroupAddressType_Type=InetAddressType
_HpnicfMPortGroupAddressType_Object=MibTableColumn
hpnicfMPortGroupAddressType=_HpnicfMPortGroupAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,2,1,2),_HpnicfMPortGroupAddressType_Type())
hpnicfMPortGroupAddressType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMPortGroupAddressType.setStatus(_A)
_HpnicfMPortGroupAddress_Type=InetAddress
_HpnicfMPortGroupAddress_Object=MibTableColumn
hpnicfMPortGroupAddress=_HpnicfMPortGroupAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,2,1,3),_HpnicfMPortGroupAddress_Type())
hpnicfMPortGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMPortGroupAddress.setStatus(_A)
_HpnicfMPortConfigTable_Object=MibTable
hpnicfMPortConfigTable=_HpnicfMPortConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3))
if mibBuilder.loadTexts:hpnicfMPortConfigTable.setStatus(_A)
_HpnicfMPortConfigEntry_Object=MibTableRow
hpnicfMPortConfigEntry=_HpnicfMPortConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3,1))
hpnicfMPortConfigEntry.setIndexNames((0,_E,_F),(0,_B,_P))
if mibBuilder.loadTexts:hpnicfMPortConfigEntry.setStatus(_A)
_HpnicfMPortConfigVlanID_Type=Integer32
_HpnicfMPortConfigVlanID_Object=MibTableColumn
hpnicfMPortConfigVlanID=_HpnicfMPortConfigVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3,1,1),_HpnicfMPortConfigVlanID_Type())
hpnicfMPortConfigVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMPortConfigVlanID.setStatus(_A)
_HpnicfMPortGroupLimitNumber_Type=Unsigned32
_HpnicfMPortGroupLimitNumber_Object=MibTableColumn
hpnicfMPortGroupLimitNumber=_HpnicfMPortGroupLimitNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3,1,2),_HpnicfMPortGroupLimitNumber_Type())
hpnicfMPortGroupLimitNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMPortGroupLimitNumber.setStatus(_A)
class _HpnicfMPortFastLeaveStatus_Type(EnabledStatus):defaultValue=2
_HpnicfMPortFastLeaveStatus_Type.__name__=_H
_HpnicfMPortFastLeaveStatus_Object=MibTableColumn
hpnicfMPortFastLeaveStatus=_HpnicfMPortFastLeaveStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3,1,3),_HpnicfMPortFastLeaveStatus_Type())
hpnicfMPortFastLeaveStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMPortFastLeaveStatus.setStatus(_A)
class _HpnicfMPortGroupPolicyParameter_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,2999))
_HpnicfMPortGroupPolicyParameter_Type.__name__=_I
_HpnicfMPortGroupPolicyParameter_Object=MibTableColumn
hpnicfMPortGroupPolicyParameter=_HpnicfMPortGroupPolicyParameter_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3,1,4),_HpnicfMPortGroupPolicyParameter_Type())
hpnicfMPortGroupPolicyParameter.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMPortGroupPolicyParameter.setStatus(_A)
_HpnicfMPortConfigRowStatus_Type=RowStatus
_HpnicfMPortConfigRowStatus_Object=MibTableColumn
hpnicfMPortConfigRowStatus=_HpnicfMPortConfigRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3,1,5),_HpnicfMPortConfigRowStatus_Type())
hpnicfMPortConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMPortConfigRowStatus.setStatus(_A)
class _HpnicfMPortGroupLimitReplace_Type(EnabledStatus):defaultValue=2
_HpnicfMPortGroupLimitReplace_Type.__name__=_H
_HpnicfMPortGroupLimitReplace_Object=MibTableColumn
hpnicfMPortGroupLimitReplace=_HpnicfMPortGroupLimitReplace_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,3,1,6),_HpnicfMPortGroupLimitReplace_Type())
hpnicfMPortGroupLimitReplace.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfMPortGroupLimitReplace.setStatus(_A)
_HpnicfHostStaticJoinTable_Object=MibTable
hpnicfHostStaticJoinTable=_HpnicfHostStaticJoinTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,4))
if mibBuilder.loadTexts:hpnicfHostStaticJoinTable.setStatus(_A)
_HpnicfHostStaticJoinEntry_Object=MibTableRow
hpnicfHostStaticJoinEntry=_HpnicfHostStaticJoinEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,4,1))
hpnicfHostStaticJoinEntry.setIndexNames((0,_E,_F),(0,_B,_Q),(0,_B,_R),(0,_B,_S))
if mibBuilder.loadTexts:hpnicfHostStaticJoinEntry.setStatus(_A)
_HpnicfHostStaticJoinVlanID_Type=Integer32
_HpnicfHostStaticJoinVlanID_Object=MibTableColumn
hpnicfHostStaticJoinVlanID=_HpnicfHostStaticJoinVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,4,1,1),_HpnicfHostStaticJoinVlanID_Type())
hpnicfHostStaticJoinVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfHostStaticJoinVlanID.setStatus(_A)
_HpnicfHostStaticJoinAddressType_Type=InetAddressType
_HpnicfHostStaticJoinAddressType_Object=MibTableColumn
hpnicfHostStaticJoinAddressType=_HpnicfHostStaticJoinAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,4,1,2),_HpnicfHostStaticJoinAddressType_Type())
hpnicfHostStaticJoinAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfHostStaticJoinAddressType.setStatus(_A)
_HpnicfHostStaticJoinAddress_Type=InetAddress
_HpnicfHostStaticJoinAddress_Object=MibTableColumn
hpnicfHostStaticJoinAddress=_HpnicfHostStaticJoinAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,4,1,3),_HpnicfHostStaticJoinAddress_Type())
hpnicfHostStaticJoinAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfHostStaticJoinAddress.setStatus(_A)
_HpnicfHostStaticJoinStatus_Type=RowStatus
_HpnicfHostStaticJoinStatus_Object=MibTableColumn
hpnicfHostStaticJoinStatus=_HpnicfHostStaticJoinStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,51,2,4,1,4),_HpnicfHostStaticJoinStatus_Type())
hpnicfHostStaticJoinStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfHostStaticJoinStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:EnabledStatus,'hpnicfMpm':hpnicfMpm,'hpnicfMPMObject':hpnicfMPMObject,'hpnicfMPortGroupLimitMinNumber':hpnicfMPortGroupLimitMinNumber,'hpnicfMPortGroupLimitMaxNumber':hpnicfMPortGroupLimitMaxNumber,'hpnicfMPMTable':hpnicfMPMTable,'hpnicfMPortGroupJoinTable':hpnicfMPortGroupJoinTable,'hpnicfMPortGroupJoinEntry':hpnicfMPortGroupJoinEntry,_J:hpnicfMPortGroupJoinVlanID,_K:hpnicfMPortGroupJoinAddressType,_L:hpnicfMPortGroupJoinAddress,'hpnicfMPortGroupJoinStatus':hpnicfMPortGroupJoinStatus,'hpnicfMPortGroupTable':hpnicfMPortGroupTable,'hpnicfMPortGroupEntry':hpnicfMPortGroupEntry,_M:hpnicfMPortGroupVlanID,_N:hpnicfMPortGroupAddressType,_O:hpnicfMPortGroupAddress,'hpnicfMPortConfigTable':hpnicfMPortConfigTable,'hpnicfMPortConfigEntry':hpnicfMPortConfigEntry,_P:hpnicfMPortConfigVlanID,'hpnicfMPortGroupLimitNumber':hpnicfMPortGroupLimitNumber,'hpnicfMPortFastLeaveStatus':hpnicfMPortFastLeaveStatus,'hpnicfMPortGroupPolicyParameter':hpnicfMPortGroupPolicyParameter,'hpnicfMPortConfigRowStatus':hpnicfMPortConfigRowStatus,'hpnicfMPortGroupLimitReplace':hpnicfMPortGroupLimitReplace,'hpnicfHostStaticJoinTable':hpnicfHostStaticJoinTable,'hpnicfHostStaticJoinEntry':hpnicfHostStaticJoinEntry,_Q:hpnicfHostStaticJoinVlanID,_R:hpnicfHostStaticJoinAddressType,_S:hpnicfHostStaticJoinAddress,'hpnicfHostStaticJoinStatus':hpnicfHostStaticJoinStatus})