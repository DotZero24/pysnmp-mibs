_T='telephonyAttributesIpAddressCallVer1'
_S='telephonyAttributesFeaturesTableVer1'
_R='telephonyAttributesIpAddressCallEnable'
_Q='telephonyAttributesAutomaticRejection'
_P='telephonyAttributesDelayedHotLineTargetAddress'
_O='telephonyAttributesDelayedHotLineExtension'
_N='telephonyAttributesDelayedHotLineEnable'
_M='telephonyAttributesHookFlashProcessing'
_L='telephonyAttributesCallDirectionRestriction'
_K='telephonyAttributesAutomaticCallTargetAddress'
_J='telephonyAttributesAutomaticCallEnable'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='Integer32'
_E='OctetString'
_D='MxEnableState'
_C='read-write'
_B='MX-TELEPHONY-ATTRIBUTES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
mediatrixConfig,=mibBuilder.importSymbols('MX-SMI','mediatrixConfig')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
telephonyAttributesMIB=ModuleIdentity((1,3,6,1,4,1,4935,15,70))
if mibBuilder.loadTexts:telephonyAttributesMIB.setRevisions(('2010-10-05 00:00','2006-11-27 00:00','2005-07-04 00:00','2003-05-16 00:00','2003-04-30 00:00','2003-03-18 00:00','2003-03-03 00:00'))
_TelephonyAttributesMIBObjects_ObjectIdentity=ObjectIdentity
telephonyAttributesMIBObjects=_TelephonyAttributesMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,15,70,1))
_TelephonyAttributesIfFeaturesTable_Object=MibTable
telephonyAttributesIfFeaturesTable=_TelephonyAttributesIfFeaturesTable_Object((1,3,6,1,4,1,4935,15,70,1,10))
if mibBuilder.loadTexts:telephonyAttributesIfFeaturesTable.setStatus(_A)
_TelephonyAttributesIfFeaturesEntry_Object=MibTableRow
telephonyAttributesIfFeaturesEntry=_TelephonyAttributesIfFeaturesEntry_Object((1,3,6,1,4,1,4935,15,70,1,10,1))
telephonyAttributesIfFeaturesEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:telephonyAttributesIfFeaturesEntry.setStatus(_A)
class _TelephonyAttributesAutomaticCallEnable_Type(MxEnableState):defaultValue=0
_TelephonyAttributesAutomaticCallEnable_Type.__name__=_D
_TelephonyAttributesAutomaticCallEnable_Object=MibTableColumn
telephonyAttributesAutomaticCallEnable=_TelephonyAttributesAutomaticCallEnable_Object((1,3,6,1,4,1,4935,15,70,1,10,1,5),_TelephonyAttributesAutomaticCallEnable_Type())
telephonyAttributesAutomaticCallEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesAutomaticCallEnable.setStatus(_A)
class _TelephonyAttributesAutomaticCallTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TelephonyAttributesAutomaticCallTargetAddress_Type.__name__=_E
_TelephonyAttributesAutomaticCallTargetAddress_Object=MibTableColumn
telephonyAttributesAutomaticCallTargetAddress=_TelephonyAttributesAutomaticCallTargetAddress_Object((1,3,6,1,4,1,4935,15,70,1,10,1,10),_TelephonyAttributesAutomaticCallTargetAddress_Type())
telephonyAttributesAutomaticCallTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesAutomaticCallTargetAddress.setStatus(_A)
class _TelephonyAttributesCallDirectionRestriction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noRestriction',0),('scnToIpOnly',1),('ipToScnOnly',2)))
_TelephonyAttributesCallDirectionRestriction_Type.__name__=_F
_TelephonyAttributesCallDirectionRestriction_Object=MibTableColumn
telephonyAttributesCallDirectionRestriction=_TelephonyAttributesCallDirectionRestriction_Object((1,3,6,1,4,1,4935,15,70,1,10,1,15),_TelephonyAttributesCallDirectionRestriction_Type())
telephonyAttributesCallDirectionRestriction.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesCallDirectionRestriction.setStatus(_A)
class _TelephonyAttributesHookFlashProcessing_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('processLocally',0),('transmitUsingSignalingProtocol',1),('outOfBandUsingRtp',2)))
_TelephonyAttributesHookFlashProcessing_Type.__name__=_F
_TelephonyAttributesHookFlashProcessing_Object=MibTableColumn
telephonyAttributesHookFlashProcessing=_TelephonyAttributesHookFlashProcessing_Object((1,3,6,1,4,1,4935,15,70,1,10,1,20),_TelephonyAttributesHookFlashProcessing_Type())
telephonyAttributesHookFlashProcessing.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesHookFlashProcessing.setStatus(_A)
class _TelephonyAttributesDelayedHotLineEnable_Type(MxEnableState):defaultValue=0
_TelephonyAttributesDelayedHotLineEnable_Type.__name__=_D
_TelephonyAttributesDelayedHotLineEnable_Object=MibTableColumn
telephonyAttributesDelayedHotLineEnable=_TelephonyAttributesDelayedHotLineEnable_Object((1,3,6,1,4,1,4935,15,70,1,10,1,70),_TelephonyAttributesDelayedHotLineEnable_Type())
telephonyAttributesDelayedHotLineEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesDelayedHotLineEnable.setStatus(_A)
class _TelephonyAttributesDelayedHotLineExtension_Type(MxEnableState):defaultValue=0
_TelephonyAttributesDelayedHotLineExtension_Type.__name__=_D
_TelephonyAttributesDelayedHotLineExtension_Object=MibTableColumn
telephonyAttributesDelayedHotLineExtension=_TelephonyAttributesDelayedHotLineExtension_Object((1,3,6,1,4,1,4935,15,70,1,10,1,120),_TelephonyAttributesDelayedHotLineExtension_Type())
telephonyAttributesDelayedHotLineExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesDelayedHotLineExtension.setStatus(_A)
class _TelephonyAttributesDelayedHotLineTargetAddress_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_TelephonyAttributesDelayedHotLineTargetAddress_Type.__name__=_E
_TelephonyAttributesDelayedHotLineTargetAddress_Object=MibTableColumn
telephonyAttributesDelayedHotLineTargetAddress=_TelephonyAttributesDelayedHotLineTargetAddress_Object((1,3,6,1,4,1,4935,15,70,1,10,1,170),_TelephonyAttributesDelayedHotLineTargetAddress_Type())
telephonyAttributesDelayedHotLineTargetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesDelayedHotLineTargetAddress.setStatus(_A)
class _TelephonyAttributesAutomaticRejection_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_TelephonyAttributesAutomaticRejection_Type.__name__=_I
_TelephonyAttributesAutomaticRejection_Object=MibScalar
telephonyAttributesAutomaticRejection=_TelephonyAttributesAutomaticRejection_Object((1,3,6,1,4,1,4935,15,70,1,10,1,220),_TelephonyAttributesAutomaticRejection_Type())
telephonyAttributesAutomaticRejection.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesAutomaticRejection.setStatus(_A)
_TelephonyAttributesIpAddressCallCustomization_ObjectIdentity=ObjectIdentity
telephonyAttributesIpAddressCallCustomization=_TelephonyAttributesIpAddressCallCustomization_ObjectIdentity((1,3,6,1,4,1,4935,15,70,1,30))
class _TelephonyAttributesIpAddressCallEnable_Type(MxEnableState):defaultValue=0
_TelephonyAttributesIpAddressCallEnable_Type.__name__=_D
_TelephonyAttributesIpAddressCallEnable_Object=MibScalar
telephonyAttributesIpAddressCallEnable=_TelephonyAttributesIpAddressCallEnable_Object((1,3,6,1,4,1,4935,15,70,1,30,5),_TelephonyAttributesIpAddressCallEnable_Type())
telephonyAttributesIpAddressCallEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:telephonyAttributesIpAddressCallEnable.setStatus(_A)
_TelephonyAttributesConformance_ObjectIdentity=ObjectIdentity
telephonyAttributesConformance=_TelephonyAttributesConformance_ObjectIdentity((1,3,6,1,4,1,4935,15,70,2))
_TelephonyAttributesCompliances_ObjectIdentity=ObjectIdentity
telephonyAttributesCompliances=_TelephonyAttributesCompliances_ObjectIdentity((1,3,6,1,4,1,4935,15,70,2,1))
_TelephonyAttributesGroups_ObjectIdentity=ObjectIdentity
telephonyAttributesGroups=_TelephonyAttributesGroups_ObjectIdentity((1,3,6,1,4,1,4935,15,70,2,5))
telephonyAttributesFeaturesTableVer1=ObjectGroup((1,3,6,1,4,1,4935,15,70,2,5,10))
telephonyAttributesFeaturesTableVer1.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:telephonyAttributesFeaturesTableVer1.setStatus(_A)
telephonyAttributesIpAddressCallVer1=ObjectGroup((1,3,6,1,4,1,4935,15,70,2,5,15))
telephonyAttributesIpAddressCallVer1.setObjects((_B,_R))
if mibBuilder.loadTexts:telephonyAttributesIpAddressCallVer1.setStatus(_A)
telephonyAttributesComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,15,70,2,1,1))
telephonyAttributesComplVer1.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:telephonyAttributesComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'telephonyAttributesMIB':telephonyAttributesMIB,'telephonyAttributesMIBObjects':telephonyAttributesMIBObjects,'telephonyAttributesIfFeaturesTable':telephonyAttributesIfFeaturesTable,'telephonyAttributesIfFeaturesEntry':telephonyAttributesIfFeaturesEntry,_J:telephonyAttributesAutomaticCallEnable,_K:telephonyAttributesAutomaticCallTargetAddress,_L:telephonyAttributesCallDirectionRestriction,_M:telephonyAttributesHookFlashProcessing,_N:telephonyAttributesDelayedHotLineEnable,_O:telephonyAttributesDelayedHotLineExtension,_P:telephonyAttributesDelayedHotLineTargetAddress,_Q:telephonyAttributesAutomaticRejection,'telephonyAttributesIpAddressCallCustomization':telephonyAttributesIpAddressCallCustomization,_R:telephonyAttributesIpAddressCallEnable,'telephonyAttributesConformance':telephonyAttributesConformance,'telephonyAttributesCompliances':telephonyAttributesCompliances,'telephonyAttributesComplVer1':telephonyAttributesComplVer1,'telephonyAttributesGroups':telephonyAttributesGroups,_S:telephonyAttributesFeaturesTableVer1,_T:telephonyAttributesIpAddressCallVer1})