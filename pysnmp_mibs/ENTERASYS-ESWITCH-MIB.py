_f='etsysESwitchProtocolGroup'
_e='etsysESwitchEtherTypeGroup'
_d='etsysESwitchBaseGroup'
_c='etsysESwitchProtocolPreempted'
_b='etsysESwitchProtocolStatus'
_a='etsysESwitchProtocolVlanId'
_Z='etsysESwitchProtocolAllowedToGoTo'
_Y='etsysESwitchProtocolConstraint'
_X='etsysESwitchEtherTypePreempted'
_W='etsysESwitchEtherTypeStatus'
_V='etsysESwitchEtherTypeValue'
_U='etsysESwitchAddressFilter'
_T='etsysESwitchRateLimit'
_S='etsysESwitchRateLimitSwitch'
_R='etsysESwitchAdminStatus'
_Q='etsysESwitchProtocolIndex'
_P='etsysESwitchProtocolType'
_O='etsysESwitchProtocolReceivePort'
_N='read-only'
_M='deleteOnReset'
_L='permanent'
_K='invalid'
_J='etsysESwitchEtherTypeIndex'
_I='OctetString'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='read-write'
_D='read-create'
_C='Integer32'
_B='ENTERASYS-ESWITCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ifIndex,=mibBuilder.importSymbols(_G,_H)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
enterasysESwitchMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,10))
if mibBuilder.loadTexts:enterasysESwitchMIB.setRevisions(('2002-03-07 19:50','2001-02-13 11:00'))
_EtsysESwitchObjects_ObjectIdentity=ObjectIdentity
etsysESwitchObjects=_EtsysESwitchObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,1))
_EtsysESwitchParams_ObjectIdentity=ObjectIdentity
etsysESwitchParams=_EtsysESwitchParams_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,1,1))
_EtsysESwitchAdminStatus_Type=EnabledStatus
_EtsysESwitchAdminStatus_Object=MibScalar
etsysESwitchAdminStatus=_EtsysESwitchAdminStatus_Object((1,3,6,1,4,1,5624,1,2,10,1,1,1),_EtsysESwitchAdminStatus_Type())
etsysESwitchAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysESwitchAdminStatus.setStatus(_A)
_EtsysESwitchRateLimiting_ObjectIdentity=ObjectIdentity
etsysESwitchRateLimiting=_EtsysESwitchRateLimiting_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,1,2))
_EtsysESwitchRateLimitingTable_Object=MibTable
etsysESwitchRateLimitingTable=_EtsysESwitchRateLimitingTable_Object((1,3,6,1,4,1,5624,1,2,10,1,2,1))
if mibBuilder.loadTexts:etsysESwitchRateLimitingTable.setStatus(_A)
_EtsysESwitchRateLimitingEntry_Object=MibTableRow
etsysESwitchRateLimitingEntry=_EtsysESwitchRateLimitingEntry_Object((1,3,6,1,4,1,5624,1,2,10,1,2,1,1))
etsysESwitchRateLimitingEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysESwitchRateLimitingEntry.setStatus(_A)
_EtsysESwitchRateLimitSwitch_Type=TruthValue
_EtsysESwitchRateLimitSwitch_Object=MibTableColumn
etsysESwitchRateLimitSwitch=_EtsysESwitchRateLimitSwitch_Object((1,3,6,1,4,1,5624,1,2,10,1,2,1,1,1),_EtsysESwitchRateLimitSwitch_Type())
etsysESwitchRateLimitSwitch.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysESwitchRateLimitSwitch.setStatus(_A)
_EtsysESwitchRateLimit_Type=Unsigned32
_EtsysESwitchRateLimit_Object=MibTableColumn
etsysESwitchRateLimit=_EtsysESwitchRateLimit_Object((1,3,6,1,4,1,5624,1,2,10,1,2,1,1,2),_EtsysESwitchRateLimit_Type())
etsysESwitchRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysESwitchRateLimit.setStatus(_A)
_EtsysESwitchFilter_ObjectIdentity=ObjectIdentity
etsysESwitchFilter=_EtsysESwitchFilter_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,1,3))
_EtsysESwitchAddrFilterTable_Object=MibTable
etsysESwitchAddrFilterTable=_EtsysESwitchAddrFilterTable_Object((1,3,6,1,4,1,5624,1,2,10,1,3,1))
if mibBuilder.loadTexts:etsysESwitchAddrFilterTable.setStatus(_A)
_EtsysESwitchAddrFilterEntry_Object=MibTableRow
etsysESwitchAddrFilterEntry=_EtsysESwitchAddrFilterEntry_Object((1,3,6,1,4,1,5624,1,2,10,1,3,1,1))
etsysESwitchAddrFilterEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:etsysESwitchAddrFilterEntry.setStatus(_A)
_EtsysESwitchAddressFilter_Type=TruthValue
_EtsysESwitchAddressFilter_Object=MibTableColumn
etsysESwitchAddressFilter=_EtsysESwitchAddressFilter_Object((1,3,6,1,4,1,5624,1,2,10,1,3,1,1,1),_EtsysESwitchAddressFilter_Type())
etsysESwitchAddressFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysESwitchAddressFilter.setStatus(_A)
_EtsysESwitchProtocolObjects_ObjectIdentity=ObjectIdentity
etsysESwitchProtocolObjects=_EtsysESwitchProtocolObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,1,4))
_EtsysESwitchEtherTypeTable_Object=MibTable
etsysESwitchEtherTypeTable=_EtsysESwitchEtherTypeTable_Object((1,3,6,1,4,1,5624,1,2,10,1,4,1))
if mibBuilder.loadTexts:etsysESwitchEtherTypeTable.setStatus(_A)
_EtsysESwitchEtherTypeEntry_Object=MibTableRow
etsysESwitchEtherTypeEntry=_EtsysESwitchEtherTypeEntry_Object((1,3,6,1,4,1,5624,1,2,10,1,4,1,1))
etsysESwitchEtherTypeEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:etsysESwitchEtherTypeEntry.setStatus(_A)
class _EtsysESwitchEtherTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_EtsysESwitchEtherTypeIndex_Type.__name__=_C
_EtsysESwitchEtherTypeIndex_Object=MibTableColumn
etsysESwitchEtherTypeIndex=_EtsysESwitchEtherTypeIndex_Object((1,3,6,1,4,1,5624,1,2,10,1,4,1,1,1),_EtsysESwitchEtherTypeIndex_Type())
etsysESwitchEtherTypeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysESwitchEtherTypeIndex.setStatus(_A)
class _EtsysESwitchEtherTypeValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_EtsysESwitchEtherTypeValue_Type.__name__=_I
_EtsysESwitchEtherTypeValue_Object=MibTableColumn
etsysESwitchEtherTypeValue=_EtsysESwitchEtherTypeValue_Object((1,3,6,1,4,1,5624,1,2,10,1,4,1,1,2),_EtsysESwitchEtherTypeValue_Type())
etsysESwitchEtherTypeValue.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysESwitchEtherTypeValue.setStatus(_A)
class _EtsysESwitchEtherTypeStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_K,2),(_L,3),(_M,4)))
_EtsysESwitchEtherTypeStatus_Type.__name__=_C
_EtsysESwitchEtherTypeStatus_Object=MibTableColumn
etsysESwitchEtherTypeStatus=_EtsysESwitchEtherTypeStatus_Object((1,3,6,1,4,1,5624,1,2,10,1,4,1,1,3),_EtsysESwitchEtherTypeStatus_Type())
etsysESwitchEtherTypeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysESwitchEtherTypeStatus.setStatus(_A)
_EtsysESwitchEtherTypePreempted_Type=TruthValue
_EtsysESwitchEtherTypePreempted_Object=MibTableColumn
etsysESwitchEtherTypePreempted=_EtsysESwitchEtherTypePreempted_Object((1,3,6,1,4,1,5624,1,2,10,1,4,1,1,4),_EtsysESwitchEtherTypePreempted_Type())
etsysESwitchEtherTypePreempted.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysESwitchEtherTypePreempted.setStatus(_A)
_EtsysESwitchProtocolTable_Object=MibTable
etsysESwitchProtocolTable=_EtsysESwitchProtocolTable_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2))
if mibBuilder.loadTexts:etsysESwitchProtocolTable.setStatus(_A)
_EtsysESwitchProtocolEntry_Object=MibTableRow
etsysESwitchProtocolEntry=_EtsysESwitchProtocolEntry_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1))
etsysESwitchProtocolEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:etsysESwitchProtocolEntry.setStatus(_A)
class _EtsysESwitchProtocolReceivePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EtsysESwitchProtocolReceivePort_Type.__name__=_C
_EtsysESwitchProtocolReceivePort_Object=MibTableColumn
etsysESwitchProtocolReceivePort=_EtsysESwitchProtocolReceivePort_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,1),_EtsysESwitchProtocolReceivePort_Type())
etsysESwitchProtocolReceivePort.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysESwitchProtocolReceivePort.setStatus(_A)
class _EtsysESwitchProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('userEtherType',1),('ipv4',2),('ipxEthernet',3),('ipxRaw',4),('ipxLlc',5),('ipxSnap',6),('sna',7),('netBios',8),('decnet',9),('ipv6',10)))
_EtsysESwitchProtocolType_Type.__name__=_C
_EtsysESwitchProtocolType_Object=MibTableColumn
etsysESwitchProtocolType=_EtsysESwitchProtocolType_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,2),_EtsysESwitchProtocolType_Type())
etsysESwitchProtocolType.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysESwitchProtocolType.setStatus(_A)
class _EtsysESwitchProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_EtsysESwitchProtocolIndex_Type.__name__=_C
_EtsysESwitchProtocolIndex_Object=MibTableColumn
etsysESwitchProtocolIndex=_EtsysESwitchProtocolIndex_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,3),_EtsysESwitchProtocolIndex_Type())
etsysESwitchProtocolIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:etsysESwitchProtocolIndex.setStatus(_A)
class _EtsysESwitchProtocolConstraint_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('portMask',1),('vlan',2)))
_EtsysESwitchProtocolConstraint_Type.__name__=_C
_EtsysESwitchProtocolConstraint_Object=MibTableColumn
etsysESwitchProtocolConstraint=_EtsysESwitchProtocolConstraint_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,4),_EtsysESwitchProtocolConstraint_Type())
etsysESwitchProtocolConstraint.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysESwitchProtocolConstraint.setStatus(_A)
_EtsysESwitchProtocolAllowedToGoTo_Type=PortList
_EtsysESwitchProtocolAllowedToGoTo_Object=MibTableColumn
etsysESwitchProtocolAllowedToGoTo=_EtsysESwitchProtocolAllowedToGoTo_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,5),_EtsysESwitchProtocolAllowedToGoTo_Type())
etsysESwitchProtocolAllowedToGoTo.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysESwitchProtocolAllowedToGoTo.setStatus(_A)
class _EtsysESwitchProtocolVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EtsysESwitchProtocolVlanId_Type.__name__=_C
_EtsysESwitchProtocolVlanId_Object=MibTableColumn
etsysESwitchProtocolVlanId=_EtsysESwitchProtocolVlanId_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,6),_EtsysESwitchProtocolVlanId_Type())
etsysESwitchProtocolVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysESwitchProtocolVlanId.setStatus(_A)
class _EtsysESwitchProtocolStatus_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_K,2),(_L,3),(_M,4)))
_EtsysESwitchProtocolStatus_Type.__name__=_C
_EtsysESwitchProtocolStatus_Object=MibTableColumn
etsysESwitchProtocolStatus=_EtsysESwitchProtocolStatus_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,7),_EtsysESwitchProtocolStatus_Type())
etsysESwitchProtocolStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysESwitchProtocolStatus.setStatus(_A)
_EtsysESwitchProtocolPreempted_Type=TruthValue
_EtsysESwitchProtocolPreempted_Object=MibTableColumn
etsysESwitchProtocolPreempted=_EtsysESwitchProtocolPreempted_Object((1,3,6,1,4,1,5624,1,2,10,1,4,2,1,8),_EtsysESwitchProtocolPreempted_Type())
etsysESwitchProtocolPreempted.setMaxAccess(_N)
if mibBuilder.loadTexts:etsysESwitchProtocolPreempted.setStatus(_A)
_EtsysESwitchConformance_ObjectIdentity=ObjectIdentity
etsysESwitchConformance=_EtsysESwitchConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,2))
_EtsysESwitchGroups_ObjectIdentity=ObjectIdentity
etsysESwitchGroups=_EtsysESwitchGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,2,1))
_EtsysESwitchCompliances_ObjectIdentity=ObjectIdentity
etsysESwitchCompliances=_EtsysESwitchCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,10,2,2))
etsysESwitchBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,10,2,1,1))
etsysESwitchBaseGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:etsysESwitchBaseGroup.setStatus(_A)
etsysESwitchEtherTypeGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,10,2,1,2))
etsysESwitchEtherTypeGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:etsysESwitchEtherTypeGroup.setStatus(_A)
etsysESwitchProtocolGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,10,2,1,3))
etsysESwitchProtocolGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:etsysESwitchProtocolGroup.setStatus(_A)
etsysESwitchCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,10,2,2,1))
etsysESwitchCompliance.setObjects(*((_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:etsysESwitchCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'enterasysESwitchMIB':enterasysESwitchMIB,'etsysESwitchObjects':etsysESwitchObjects,'etsysESwitchParams':etsysESwitchParams,_R:etsysESwitchAdminStatus,'etsysESwitchRateLimiting':etsysESwitchRateLimiting,'etsysESwitchRateLimitingTable':etsysESwitchRateLimitingTable,'etsysESwitchRateLimitingEntry':etsysESwitchRateLimitingEntry,_S:etsysESwitchRateLimitSwitch,_T:etsysESwitchRateLimit,'etsysESwitchFilter':etsysESwitchFilter,'etsysESwitchAddrFilterTable':etsysESwitchAddrFilterTable,'etsysESwitchAddrFilterEntry':etsysESwitchAddrFilterEntry,_U:etsysESwitchAddressFilter,'etsysESwitchProtocolObjects':etsysESwitchProtocolObjects,'etsysESwitchEtherTypeTable':etsysESwitchEtherTypeTable,'etsysESwitchEtherTypeEntry':etsysESwitchEtherTypeEntry,_J:etsysESwitchEtherTypeIndex,_V:etsysESwitchEtherTypeValue,_W:etsysESwitchEtherTypeStatus,_X:etsysESwitchEtherTypePreempted,'etsysESwitchProtocolTable':etsysESwitchProtocolTable,'etsysESwitchProtocolEntry':etsysESwitchProtocolEntry,_O:etsysESwitchProtocolReceivePort,_P:etsysESwitchProtocolType,_Q:etsysESwitchProtocolIndex,_Y:etsysESwitchProtocolConstraint,_Z:etsysESwitchProtocolAllowedToGoTo,_a:etsysESwitchProtocolVlanId,_b:etsysESwitchProtocolStatus,_c:etsysESwitchProtocolPreempted,'etsysESwitchConformance':etsysESwitchConformance,'etsysESwitchGroups':etsysESwitchGroups,_d:etsysESwitchBaseGroup,_e:etsysESwitchEtherTypeGroup,_f:etsysESwitchProtocolGroup,'etsysESwitchCompliances':etsysESwitchCompliances,'etsysESwitchCompliance':etsysESwitchCompliance})