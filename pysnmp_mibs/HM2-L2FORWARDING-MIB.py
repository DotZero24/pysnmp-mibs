_I='hm2CosMapIpDscpValue'
_H='not-accessible'
_G='hm2TrafficClassPriority'
_F='HmEnabledStatus'
_E='HM2-L2FORWARDING-MIB'
_D='read-write'
_C='Unsigned32'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_F,'hm2ConfigurationMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2L2ForwardingMib=ModuleIdentity((1,3,6,1,4,1,248,11,30))
if mibBuilder.loadTexts:hm2L2ForwardingMib.setRevisions(('2011-03-16 00:00',))
_Hm2L2ForwardingMibNotifications_ObjectIdentity=ObjectIdentity
hm2L2ForwardingMibNotifications=_Hm2L2ForwardingMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,30,0))
_Hm2L2ForwardingMibObjects_ObjectIdentity=ObjectIdentity
hm2L2ForwardingMibObjects=_Hm2L2ForwardingMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,30,1))
_Hm2L2ForwGeneralGroup_ObjectIdentity=ObjectIdentity
hm2L2ForwGeneralGroup=_Hm2L2ForwGeneralGroup_ObjectIdentity((1,3,6,1,4,1,248,11,30,1,1))
class _Hm2L2VlanUnawareModeAdminStatus_Type(HmEnabledStatus):defaultValue=2
_Hm2L2VlanUnawareModeAdminStatus_Type.__name__=_F
_Hm2L2VlanUnawareModeAdminStatus_Object=MibScalar
hm2L2VlanUnawareModeAdminStatus=_Hm2L2VlanUnawareModeAdminStatus_Object((1,3,6,1,4,1,248,11,30,1,1,1),_Hm2L2VlanUnawareModeAdminStatus_Type())
hm2L2VlanUnawareModeAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2L2VlanUnawareModeAdminStatus.setStatus(_A)
_Hm2L2VlanUnawareModeOperStatus_Type=HmEnabledStatus
_Hm2L2VlanUnawareModeOperStatus_Object=MibScalar
hm2L2VlanUnawareModeOperStatus=_Hm2L2VlanUnawareModeOperStatus_Object((1,3,6,1,4,1,248,11,30,1,1,2),_Hm2L2VlanUnawareModeOperStatus_Type())
hm2L2VlanUnawareModeOperStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:hm2L2VlanUnawareModeOperStatus.setStatus(_A)
_Hm2L2ForwClassOfServiceGroup_ObjectIdentity=ObjectIdentity
hm2L2ForwClassOfServiceGroup=_Hm2L2ForwClassOfServiceGroup_ObjectIdentity((1,3,6,1,4,1,248,11,30,1,2))
_Hm2TrafficClassTable_Object=MibTable
hm2TrafficClassTable=_Hm2TrafficClassTable_Object((1,3,6,1,4,1,248,11,30,1,2,1))
if mibBuilder.loadTexts:hm2TrafficClassTable.setStatus(_A)
_Hm2TrafficClassEntry_Object=MibTableRow
hm2TrafficClassEntry=_Hm2TrafficClassEntry_Object((1,3,6,1,4,1,248,11,30,1,2,1,1))
hm2TrafficClassEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:hm2TrafficClassEntry.setStatus(_A)
class _Hm2TrafficClassPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2TrafficClassPriority_Type.__name__=_B
_Hm2TrafficClassPriority_Object=MibTableColumn
hm2TrafficClassPriority=_Hm2TrafficClassPriority_Object((1,3,6,1,4,1,248,11,30,1,2,1,1,1),_Hm2TrafficClassPriority_Type())
hm2TrafficClassPriority.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2TrafficClassPriority.setStatus(_A)
class _Hm2TrafficClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2TrafficClass_Type.__name__=_B
_Hm2TrafficClass_Object=MibTableColumn
hm2TrafficClass=_Hm2TrafficClass_Object((1,3,6,1,4,1,248,11,30,1,2,1,1,2),_Hm2TrafficClass_Type())
hm2TrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2TrafficClass.setStatus(_A)
_Hm2CosMapIpDscpTable_Object=MibTable
hm2CosMapIpDscpTable=_Hm2CosMapIpDscpTable_Object((1,3,6,1,4,1,248,11,30,1,2,2))
if mibBuilder.loadTexts:hm2CosMapIpDscpTable.setStatus(_A)
_Hm2CosMapIpDscpEntry_Object=MibTableRow
hm2CosMapIpDscpEntry=_Hm2CosMapIpDscpEntry_Object((1,3,6,1,4,1,248,11,30,1,2,2,1))
hm2CosMapIpDscpEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:hm2CosMapIpDscpEntry.setStatus(_A)
class _Hm2CosMapIpDscpValue_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_Hm2CosMapIpDscpValue_Type.__name__=_C
_Hm2CosMapIpDscpValue_Object=MibTableColumn
hm2CosMapIpDscpValue=_Hm2CosMapIpDscpValue_Object((1,3,6,1,4,1,248,11,30,1,2,2,1,1),_Hm2CosMapIpDscpValue_Type())
hm2CosMapIpDscpValue.setMaxAccess(_H)
if mibBuilder.loadTexts:hm2CosMapIpDscpValue.setStatus(_A)
class _Hm2CosMapIpDscpTrafficClass_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Hm2CosMapIpDscpTrafficClass_Type.__name__=_C
_Hm2CosMapIpDscpTrafficClass_Object=MibTableColumn
hm2CosMapIpDscpTrafficClass=_Hm2CosMapIpDscpTrafficClass_Object((1,3,6,1,4,1,248,11,30,1,2,2,1,2),_Hm2CosMapIpDscpTrafficClass_Type())
hm2CosMapIpDscpTrafficClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hm2CosMapIpDscpTrafficClass.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hm2L2ForwardingMib':hm2L2ForwardingMib,'hm2L2ForwardingMibNotifications':hm2L2ForwardingMibNotifications,'hm2L2ForwardingMibObjects':hm2L2ForwardingMibObjects,'hm2L2ForwGeneralGroup':hm2L2ForwGeneralGroup,'hm2L2VlanUnawareModeAdminStatus':hm2L2VlanUnawareModeAdminStatus,'hm2L2VlanUnawareModeOperStatus':hm2L2VlanUnawareModeOperStatus,'hm2L2ForwClassOfServiceGroup':hm2L2ForwClassOfServiceGroup,'hm2TrafficClassTable':hm2TrafficClassTable,'hm2TrafficClassEntry':hm2TrafficClassEntry,_G:hm2TrafficClassPriority,'hm2TrafficClass':hm2TrafficClass,'hm2CosMapIpDscpTable':hm2CosMapIpDscpTable,'hm2CosMapIpDscpEntry':hm2CosMapIpDscpEntry,_I:hm2CosMapIpDscpValue,'hm2CosMapIpDscpTrafficClass':hm2CosMapIpDscpTrafficClass})