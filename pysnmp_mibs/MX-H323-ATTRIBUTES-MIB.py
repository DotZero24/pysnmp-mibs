_X='h323AttributesQ931GroupVer1'
_W='h323AttributesTelephonyGroupVer1'
_V='h323AttributesSignalingGroupVer1'
_U='h323AttributesCalledPartyNumberTypeOfNumber'
_T='h323AttributesCalledPartyNumberDigitMap'
_S='h323AttributesCalledPartyNumberEnable'
_R='h323AttributesInformationTransferCapability'
_Q='h323AttributesDirectGatewayCallHost'
_P='h323AttributesDirectGatewayCallEnable'
_O='h323AttributesVoiceCapabilitySendingMethod'
_N='h323AttributesParallelH245Enable'
_M='h323AttributesFastConnectEnable'
_L='h323AttributesH245TunnelingEnable'
_K='h323AttributesEarlyH245Enable'
_J='MxIpAddress'
_I='OctetString'
_H='h323AttributesCalledPartyNumberIndex'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='MxEnableState'
_C='read-write'
_B='MX-H323-ATTRIBUTES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
h323,ipAddressConfigH323Dhcp,ipAddressConfigH323Static,ipAddressStatusH323=mibBuilder.importSymbols('MX-H323-MIB','h323','ipAddressConfigH323Dhcp','ipAddressConfigH323Static','ipAddressStatusH323')
MxEnableState,MxIpAddress,MxIpDhcpSiteSpecificCode,MxIpPort=mibBuilder.importSymbols('MX-TC',_D,_J,'MxIpDhcpSiteSpecificCode','MxIpPort')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h323AttributesMIB=ModuleIdentity((1,3,6,1,4,1,4935,20,30,5))
if mibBuilder.loadTexts:h323AttributesMIB.setRevisions(('2008-08-25 00:00','2008-03-05 00:00','2005-01-18 00:00','2004-10-15 00:00','2004-07-14 00:00','2004-01-21 00:00','2003-11-05 00:00','2003-05-05 00:00','2003-03-04 00:00'))
_H323AttributesMIBObjects_ObjectIdentity=ObjectIdentity
h323AttributesMIBObjects=_H323AttributesMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,20,30,5,1))
_H323AttributesQ931_ObjectIdentity=ObjectIdentity
h323AttributesQ931=_H323AttributesQ931_ObjectIdentity((1,3,6,1,4,1,4935,20,30,5,1,1))
_H323AttributesQ931BearerCapability_ObjectIdentity=ObjectIdentity
h323AttributesQ931BearerCapability=_H323AttributesQ931BearerCapability_ObjectIdentity((1,3,6,1,4,1,4935,20,30,5,1,1,5))
class _H323AttributesInformationTransferCapability_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('speech',0),('unrestrictedDigitalInformation',1),('restrictedDigitalInformation',2),('audio31kHz',3),('udita',4),('video',5)))
_H323AttributesInformationTransferCapability_Type.__name__=_E
_H323AttributesInformationTransferCapability_Object=MibScalar
h323AttributesInformationTransferCapability=_H323AttributesInformationTransferCapability_Object((1,3,6,1,4,1,4935,20,30,5,1,1,5,5),_H323AttributesInformationTransferCapability_Type())
h323AttributesInformationTransferCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesInformationTransferCapability.setStatus(_A)
_H323AttributesQ931CalledPartyNumberTable_Object=MibTable
h323AttributesQ931CalledPartyNumberTable=_H323AttributesQ931CalledPartyNumberTable_Object((1,3,6,1,4,1,4935,20,30,5,1,1,15))
if mibBuilder.loadTexts:h323AttributesQ931CalledPartyNumberTable.setStatus(_A)
_H323AttributesQ931CalledPartyNumberEntry_Object=MibTableRow
h323AttributesQ931CalledPartyNumberEntry=_H323AttributesQ931CalledPartyNumberEntry_Object((1,3,6,1,4,1,4935,20,30,5,1,1,15,1))
h323AttributesQ931CalledPartyNumberEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:h323AttributesQ931CalledPartyNumberEntry.setStatus(_A)
_H323AttributesCalledPartyNumberIndex_Type=Unsigned32
_H323AttributesCalledPartyNumberIndex_Object=MibTableColumn
h323AttributesCalledPartyNumberIndex=_H323AttributesCalledPartyNumberIndex_Object((1,3,6,1,4,1,4935,20,30,5,1,1,15,1,1),_H323AttributesCalledPartyNumberIndex_Type())
h323AttributesCalledPartyNumberIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:h323AttributesCalledPartyNumberIndex.setStatus(_A)
class _H323AttributesCalledPartyNumberEnable_Type(MxEnableState):defaultValue=0
_H323AttributesCalledPartyNumberEnable_Type.__name__=_D
_H323AttributesCalledPartyNumberEnable_Object=MibTableColumn
h323AttributesCalledPartyNumberEnable=_H323AttributesCalledPartyNumberEnable_Object((1,3,6,1,4,1,4935,20,30,5,1,1,15,1,5),_H323AttributesCalledPartyNumberEnable_Type())
h323AttributesCalledPartyNumberEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesCalledPartyNumberEnable.setStatus(_A)
class _H323AttributesCalledPartyNumberDigitMap_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H323AttributesCalledPartyNumberDigitMap_Type.__name__=_I
_H323AttributesCalledPartyNumberDigitMap_Object=MibTableColumn
h323AttributesCalledPartyNumberDigitMap=_H323AttributesCalledPartyNumberDigitMap_Object((1,3,6,1,4,1,4935,20,30,5,1,1,15,1,10),_H323AttributesCalledPartyNumberDigitMap_Type())
h323AttributesCalledPartyNumberDigitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesCalledPartyNumberDigitMap.setStatus(_A)
class _H323AttributesCalledPartyNumberTypeOfNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('internationalNumber',0),('nationalNumber',1),('subscriberNumber',2),('privateNumber',3),('unknown',4)))
_H323AttributesCalledPartyNumberTypeOfNumber_Type.__name__=_E
_H323AttributesCalledPartyNumberTypeOfNumber_Object=MibTableColumn
h323AttributesCalledPartyNumberTypeOfNumber=_H323AttributesCalledPartyNumberTypeOfNumber_Object((1,3,6,1,4,1,4935,20,30,5,1,1,15,1,15),_H323AttributesCalledPartyNumberTypeOfNumber_Type())
h323AttributesCalledPartyNumberTypeOfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesCalledPartyNumberTypeOfNumber.setStatus(_A)
_H323IfSignalingAttributesTable_Object=MibTable
h323IfSignalingAttributesTable=_H323IfSignalingAttributesTable_Object((1,3,6,1,4,1,4935,20,30,5,1,5))
if mibBuilder.loadTexts:h323IfSignalingAttributesTable.setStatus(_A)
_H323IfSignalingAttributesEntry_Object=MibTableRow
h323IfSignalingAttributesEntry=_H323IfSignalingAttributesEntry_Object((1,3,6,1,4,1,4935,20,30,5,1,5,1))
h323IfSignalingAttributesEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h323IfSignalingAttributesEntry.setStatus(_A)
class _H323AttributesEarlyH245Enable_Type(MxEnableState):defaultValue=1
_H323AttributesEarlyH245Enable_Type.__name__=_D
_H323AttributesEarlyH245Enable_Object=MibTableColumn
h323AttributesEarlyH245Enable=_H323AttributesEarlyH245Enable_Object((1,3,6,1,4,1,4935,20,30,5,1,5,1,5),_H323AttributesEarlyH245Enable_Type())
h323AttributesEarlyH245Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesEarlyH245Enable.setStatus(_A)
class _H323AttributesH245TunnelingEnable_Type(MxEnableState):defaultValue=0
_H323AttributesH245TunnelingEnable_Type.__name__=_D
_H323AttributesH245TunnelingEnable_Object=MibTableColumn
h323AttributesH245TunnelingEnable=_H323AttributesH245TunnelingEnable_Object((1,3,6,1,4,1,4935,20,30,5,1,5,1,10),_H323AttributesH245TunnelingEnable_Type())
h323AttributesH245TunnelingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesH245TunnelingEnable.setStatus(_A)
class _H323AttributesFastConnectEnable_Type(MxEnableState):defaultValue=1
_H323AttributesFastConnectEnable_Type.__name__=_D
_H323AttributesFastConnectEnable_Object=MibTableColumn
h323AttributesFastConnectEnable=_H323AttributesFastConnectEnable_Object((1,3,6,1,4,1,4935,20,30,5,1,5,1,15),_H323AttributesFastConnectEnable_Type())
h323AttributesFastConnectEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesFastConnectEnable.setStatus(_A)
class _H323AttributesParallelH245Enable_Type(MxEnableState):defaultValue=0
_H323AttributesParallelH245Enable_Type.__name__=_D
_H323AttributesParallelH245Enable_Object=MibTableColumn
h323AttributesParallelH245Enable=_H323AttributesParallelH245Enable_Object((1,3,6,1,4,1,4935,20,30,5,1,5,1,20),_H323AttributesParallelH245Enable_Type())
h323AttributesParallelH245Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesParallelH245Enable.setStatus(_A)
class _H323AttributesVoiceCapabilitySendingMethod_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('abbreviated',0),('detailed',1)))
_H323AttributesVoiceCapabilitySendingMethod_Type.__name__=_E
_H323AttributesVoiceCapabilitySendingMethod_Object=MibTableColumn
h323AttributesVoiceCapabilitySendingMethod=_H323AttributesVoiceCapabilitySendingMethod_Object((1,3,6,1,4,1,4935,20,30,5,1,5,1,25),_H323AttributesVoiceCapabilitySendingMethod_Type())
h323AttributesVoiceCapabilitySendingMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesVoiceCapabilitySendingMethod.setStatus(_A)
_H323IfTelephonyAttributesTable_Object=MibTable
h323IfTelephonyAttributesTable=_H323IfTelephonyAttributesTable_Object((1,3,6,1,4,1,4935,20,30,5,1,10))
if mibBuilder.loadTexts:h323IfTelephonyAttributesTable.setStatus(_A)
_H323IfTelephonyAttributesEntry_Object=MibTableRow
h323IfTelephonyAttributesEntry=_H323IfTelephonyAttributesEntry_Object((1,3,6,1,4,1,4935,20,30,5,1,10,1))
h323IfTelephonyAttributesEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h323IfTelephonyAttributesEntry.setStatus(_A)
class _H323AttributesDirectGatewayCallEnable_Type(MxEnableState):defaultValue=0
_H323AttributesDirectGatewayCallEnable_Type.__name__=_D
_H323AttributesDirectGatewayCallEnable_Object=MibTableColumn
h323AttributesDirectGatewayCallEnable=_H323AttributesDirectGatewayCallEnable_Object((1,3,6,1,4,1,4935,20,30,5,1,10,1,5),_H323AttributesDirectGatewayCallEnable_Type())
h323AttributesDirectGatewayCallEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesDirectGatewayCallEnable.setStatus(_A)
class _H323AttributesDirectGatewayCallHost_Type(MxIpAddress):defaultValue=OctetString('')
_H323AttributesDirectGatewayCallHost_Type.__name__=_J
_H323AttributesDirectGatewayCallHost_Object=MibTableColumn
h323AttributesDirectGatewayCallHost=_H323AttributesDirectGatewayCallHost_Object((1,3,6,1,4,1,4935,20,30,5,1,10,1,10),_H323AttributesDirectGatewayCallHost_Type())
h323AttributesDirectGatewayCallHost.setMaxAccess(_C)
if mibBuilder.loadTexts:h323AttributesDirectGatewayCallHost.setStatus(_A)
_H323AttributesConformance_ObjectIdentity=ObjectIdentity
h323AttributesConformance=_H323AttributesConformance_ObjectIdentity((1,3,6,1,4,1,4935,20,30,5,2))
_H323AttributesCompliances_ObjectIdentity=ObjectIdentity
h323AttributesCompliances=_H323AttributesCompliances_ObjectIdentity((1,3,6,1,4,1,4935,20,30,5,2,1))
_H323AttributesGroups_ObjectIdentity=ObjectIdentity
h323AttributesGroups=_H323AttributesGroups_ObjectIdentity((1,3,6,1,4,1,4935,20,30,5,2,2))
h323AttributesSignalingGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,5,2,2,5))
h323AttributesSignalingGroupVer1.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:h323AttributesSignalingGroupVer1.setStatus(_A)
h323AttributesTelephonyGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,5,2,2,10))
h323AttributesTelephonyGroupVer1.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:h323AttributesTelephonyGroupVer1.setStatus(_A)
h323AttributesQ931GroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,5,2,2,15))
h323AttributesQ931GroupVer1.setObjects(*((_B,_R),(_B,_H),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:h323AttributesQ931GroupVer1.setStatus(_A)
h323AttributesBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,20,30,5,2,1,5))
h323AttributesBasicComplVer1.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:h323AttributesBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h323AttributesMIB':h323AttributesMIB,'h323AttributesMIBObjects':h323AttributesMIBObjects,'h323AttributesQ931':h323AttributesQ931,'h323AttributesQ931BearerCapability':h323AttributesQ931BearerCapability,_R:h323AttributesInformationTransferCapability,'h323AttributesQ931CalledPartyNumberTable':h323AttributesQ931CalledPartyNumberTable,'h323AttributesQ931CalledPartyNumberEntry':h323AttributesQ931CalledPartyNumberEntry,_H:h323AttributesCalledPartyNumberIndex,_S:h323AttributesCalledPartyNumberEnable,_T:h323AttributesCalledPartyNumberDigitMap,_U:h323AttributesCalledPartyNumberTypeOfNumber,'h323IfSignalingAttributesTable':h323IfSignalingAttributesTable,'h323IfSignalingAttributesEntry':h323IfSignalingAttributesEntry,_K:h323AttributesEarlyH245Enable,_L:h323AttributesH245TunnelingEnable,_M:h323AttributesFastConnectEnable,_N:h323AttributesParallelH245Enable,_O:h323AttributesVoiceCapabilitySendingMethod,'h323IfTelephonyAttributesTable':h323IfTelephonyAttributesTable,'h323IfTelephonyAttributesEntry':h323IfTelephonyAttributesEntry,_P:h323AttributesDirectGatewayCallEnable,_Q:h323AttributesDirectGatewayCallHost,'h323AttributesConformance':h323AttributesConformance,'h323AttributesCompliances':h323AttributesCompliances,'h323AttributesBasicComplVer1':h323AttributesBasicComplVer1,'h323AttributesGroups':h323AttributesGroups,_V:h323AttributesSignalingGroupVer1,_W:h323AttributesTelephonyGroupVer1,_X:h323AttributesQ931GroupVer1})