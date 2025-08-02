_H='zxr10vswitchVlanIngressExtVlanid'
_G='zxr10vswitchVlanIngressIfIndex'
_F='zxr10vsiwtchIfIndex'
_E='DisplayString'
_D='ZXR10-VSWITCH-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntryStatus,=mibBuilder.importSymbols('RMON-MIB','EntryStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
zxr10vswitch=ModuleIdentity((1,3,6,1,4,1,3902,3,101,4))
class DisplayString(OctetString):0
class VsiwtchTransMode(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ip',0),('vlan',1),('mix',2)))
class VsiwtchVlanDirection(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('intoout',0),('both',1)))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_Zxr10_ObjectIdentity=ObjectIdentity
zxr10=_Zxr10_ObjectIdentity((1,3,6,1,4,1,3902,3))
_Zxr10protocol_ObjectIdentity=ObjectIdentity
zxr10protocol=_Zxr10protocol_ObjectIdentity((1,3,6,1,4,1,3902,3,101))
_Zxr10vswitchIfTable_Object=MibTable
zxr10vswitchIfTable=_Zxr10vswitchIfTable_Object((1,3,6,1,4,1,3902,3,101,4,1))
if mibBuilder.loadTexts:zxr10vswitchIfTable.setStatus(_A)
_Zxr10vswitchIfEntry_Object=MibTableRow
zxr10vswitchIfEntry=_Zxr10vswitchIfEntry_Object((1,3,6,1,4,1,3902,3,101,4,1,1))
zxr10vswitchIfEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:zxr10vswitchIfEntry.setStatus(_A)
_Zxr10vsiwtchIfIndex_Type=Integer32
_Zxr10vsiwtchIfIndex_Object=MibTableColumn
zxr10vsiwtchIfIndex=_Zxr10vsiwtchIfIndex_Object((1,3,6,1,4,1,3902,3,101,4,1,1,1),_Zxr10vsiwtchIfIndex_Type())
zxr10vsiwtchIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vsiwtchIfIndex.setStatus(_A)
_Zxr10vswitchIfType_Type=Integer32
_Zxr10vswitchIfType_Object=MibTableColumn
zxr10vswitchIfType=_Zxr10vswitchIfType_Object((1,3,6,1,4,1,3902,3,101,4,1,1,2),_Zxr10vswitchIfType_Type())
zxr10vswitchIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchIfType.setStatus(_A)
_Zxr10vswitchIfTransType_Type=VsiwtchTransMode
_Zxr10vswitchIfTransType_Object=MibTableColumn
zxr10vswitchIfTransType=_Zxr10vswitchIfTransType_Object((1,3,6,1,4,1,3902,3,101,4,1,1,3),_Zxr10vswitchIfTransType_Type())
zxr10vswitchIfTransType.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchIfTransType.setStatus(_A)
_Zxr10vswitchIfStatus_Type=Integer32
_Zxr10vswitchIfStatus_Object=MibTableColumn
zxr10vswitchIfStatus=_Zxr10vswitchIfStatus_Object((1,3,6,1,4,1,3902,3,101,4,1,1,4),_Zxr10vswitchIfStatus_Type())
zxr10vswitchIfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchIfStatus.setStatus(_A)
_Zxr10vswitchIfAddr_Type=IpAddress
_Zxr10vswitchIfAddr_Object=MibTableColumn
zxr10vswitchIfAddr=_Zxr10vswitchIfAddr_Object((1,3,6,1,4,1,3902,3,101,4,1,1,5),_Zxr10vswitchIfAddr_Type())
zxr10vswitchIfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchIfAddr.setStatus(_A)
class _Zxr10vswitchIfDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_Zxr10vswitchIfDesc_Type.__name__=_E
_Zxr10vswitchIfDesc_Object=MibTableColumn
zxr10vswitchIfDesc=_Zxr10vswitchIfDesc_Object((1,3,6,1,4,1,3902,3,101,4,1,1,6),_Zxr10vswitchIfDesc_Type())
zxr10vswitchIfDesc.setMaxAccess('read-create')
if mibBuilder.loadTexts:zxr10vswitchIfDesc.setStatus(_A)
_Zxr10vswitchIfTableLastchange_Type=TimeTicks
_Zxr10vswitchIfTableLastchange_Object=MibScalar
zxr10vswitchIfTableLastchange=_Zxr10vswitchIfTableLastchange_Object((1,3,6,1,4,1,3902,3,101,4,2),_Zxr10vswitchIfTableLastchange_Type())
zxr10vswitchIfTableLastchange.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchIfTableLastchange.setStatus(_A)
_Zxr10vswitchVlanTable_Object=MibTable
zxr10vswitchVlanTable=_Zxr10vswitchVlanTable_Object((1,3,6,1,4,1,3902,3,101,4,3))
if mibBuilder.loadTexts:zxr10vswitchVlanTable.setStatus(_A)
_Zxr10vsiwtchVlanEntry_Object=MibTableRow
zxr10vsiwtchVlanEntry=_Zxr10vsiwtchVlanEntry_Object((1,3,6,1,4,1,3902,3,101,4,3,1))
zxr10vsiwtchVlanEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:zxr10vsiwtchVlanEntry.setStatus(_A)
_Zxr10vswitchVlanIngressExtVlanid_Type=Integer32
_Zxr10vswitchVlanIngressExtVlanid_Object=MibTableColumn
zxr10vswitchVlanIngressExtVlanid=_Zxr10vswitchVlanIngressExtVlanid_Object((1,3,6,1,4,1,3902,3,101,4,3,1,1),_Zxr10vswitchVlanIngressExtVlanid_Type())
zxr10vswitchVlanIngressExtVlanid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchVlanIngressExtVlanid.setStatus(_A)
_Zxr10vswitchVlanIngressIfIndex_Type=Integer32
_Zxr10vswitchVlanIngressIfIndex_Object=MibTableColumn
zxr10vswitchVlanIngressIfIndex=_Zxr10vswitchVlanIngressIfIndex_Object((1,3,6,1,4,1,3902,3,101,4,3,1,2),_Zxr10vswitchVlanIngressIfIndex_Type())
zxr10vswitchVlanIngressIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchVlanIngressIfIndex.setStatus(_A)
_Zxr10vswitchVlanIngressIntVlanid_Type=Integer32
_Zxr10vswitchVlanIngressIntVlanid_Object=MibTableColumn
zxr10vswitchVlanIngressIntVlanid=_Zxr10vswitchVlanIngressIntVlanid_Object((1,3,6,1,4,1,3902,3,101,4,3,1,3),_Zxr10vswitchVlanIngressIntVlanid_Type())
zxr10vswitchVlanIngressIntVlanid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchVlanIngressIntVlanid.setStatus(_A)
_Zxr10vswitchVlanEgressExtVlanid_Type=Integer32
_Zxr10vswitchVlanEgressExtVlanid_Object=MibTableColumn
zxr10vswitchVlanEgressExtVlanid=_Zxr10vswitchVlanEgressExtVlanid_Object((1,3,6,1,4,1,3902,3,101,4,3,1,4),_Zxr10vswitchVlanEgressExtVlanid_Type())
zxr10vswitchVlanEgressExtVlanid.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10vswitchVlanEgressExtVlanid.setStatus(_A)
_Zxr10vswitchVlanEgressIfIndex_Type=Integer32
_Zxr10vswitchVlanEgressIfIndex_Object=MibTableColumn
zxr10vswitchVlanEgressIfIndex=_Zxr10vswitchVlanEgressIfIndex_Object((1,3,6,1,4,1,3902,3,101,4,3,1,5),_Zxr10vswitchVlanEgressIfIndex_Type())
zxr10vswitchVlanEgressIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10vswitchVlanEgressIfIndex.setStatus(_A)
_Zxr10vswitchVlanEgressIntVlanid_Type=Integer32
_Zxr10vswitchVlanEgressIntVlanid_Object=MibTableColumn
zxr10vswitchVlanEgressIntVlanid=_Zxr10vswitchVlanEgressIntVlanid_Object((1,3,6,1,4,1,3902,3,101,4,3,1,6),_Zxr10vswitchVlanEgressIntVlanid_Type())
zxr10vswitchVlanEgressIntVlanid.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchVlanEgressIntVlanid.setStatus(_A)
_Zxr10vswitchVlanVlanidRange_Type=Integer32
_Zxr10vswitchVlanVlanidRange_Object=MibTableColumn
zxr10vswitchVlanVlanidRange=_Zxr10vswitchVlanVlanidRange_Object((1,3,6,1,4,1,3902,3,101,4,3,1,7),_Zxr10vswitchVlanVlanidRange_Type())
zxr10vswitchVlanVlanidRange.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10vswitchVlanVlanidRange.setStatus(_A)
_Zxr10vswitchVlandDirection_Type=VsiwtchVlanDirection
_Zxr10vswitchVlandDirection_Object=MibTableColumn
zxr10vswitchVlandDirection=_Zxr10vswitchVlandDirection_Object((1,3,6,1,4,1,3902,3,101,4,3,1,8),_Zxr10vswitchVlandDirection_Type())
zxr10vswitchVlandDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10vswitchVlandDirection.setStatus(_A)
_Zxr10vswitchVlanRowStatus_Type=EntryStatus
_Zxr10vswitchVlanRowStatus_Object=MibTableColumn
zxr10vswitchVlanRowStatus=_Zxr10vswitchVlanRowStatus_Object((1,3,6,1,4,1,3902,3,101,4,3,1,9),_Zxr10vswitchVlanRowStatus_Type())
zxr10vswitchVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10vswitchVlanRowStatus.setStatus(_A)
_Zxr10vswitchVlanDesc_Type=DisplayString
_Zxr10vswitchVlanDesc_Object=MibTableColumn
zxr10vswitchVlanDesc=_Zxr10vswitchVlanDesc_Object((1,3,6,1,4,1,3902,3,101,4,3,1,10),_Zxr10vswitchVlanDesc_Type())
zxr10vswitchVlanDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:zxr10vswitchVlanDesc.setStatus(_A)
_Zxr10vswitchVlanTableLastchange_Type=TimeTicks
_Zxr10vswitchVlanTableLastchange_Object=MibScalar
zxr10vswitchVlanTableLastchange=_Zxr10vswitchVlanTableLastchange_Object((1,3,6,1,4,1,3902,3,101,4,4),_Zxr10vswitchVlanTableLastchange_Type())
zxr10vswitchVlanTableLastchange.setMaxAccess(_B)
if mibBuilder.loadTexts:zxr10vswitchVlanTableLastchange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_E:DisplayString,'VsiwtchTransMode':VsiwtchTransMode,'VsiwtchVlanDirection':VsiwtchVlanDirection,'zte':zte,'zxr10':zxr10,'zxr10protocol':zxr10protocol,'zxr10vswitch':zxr10vswitch,'zxr10vswitchIfTable':zxr10vswitchIfTable,'zxr10vswitchIfEntry':zxr10vswitchIfEntry,_F:zxr10vsiwtchIfIndex,'zxr10vswitchIfType':zxr10vswitchIfType,'zxr10vswitchIfTransType':zxr10vswitchIfTransType,'zxr10vswitchIfStatus':zxr10vswitchIfStatus,'zxr10vswitchIfAddr':zxr10vswitchIfAddr,'zxr10vswitchIfDesc':zxr10vswitchIfDesc,'zxr10vswitchIfTableLastchange':zxr10vswitchIfTableLastchange,'zxr10vswitchVlanTable':zxr10vswitchVlanTable,'zxr10vsiwtchVlanEntry':zxr10vsiwtchVlanEntry,_H:zxr10vswitchVlanIngressExtVlanid,_G:zxr10vswitchVlanIngressIfIndex,'zxr10vswitchVlanIngressIntVlanid':zxr10vswitchVlanIngressIntVlanid,'zxr10vswitchVlanEgressExtVlanid':zxr10vswitchVlanEgressExtVlanid,'zxr10vswitchVlanEgressIfIndex':zxr10vswitchVlanEgressIfIndex,'zxr10vswitchVlanEgressIntVlanid':zxr10vswitchVlanEgressIntVlanid,'zxr10vswitchVlanVlanidRange':zxr10vswitchVlanVlanidRange,'zxr10vswitchVlandDirection':zxr10vswitchVlandDirection,'zxr10vswitchVlanRowStatus':zxr10vswitchVlanRowStatus,'zxr10vswitchVlanDesc':zxr10vswitchVlanDesc,'zxr10vswitchVlanTableLastchange':zxr10vswitchVlanTableLastchange})