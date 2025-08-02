_O='sanEventDesc'
_N='sanEventGroup'
_M='sanEventCategory'
_L='sanEventEventCode'
_K='NotificationType'
_J='sanEventURL'
_I='sanEventSourceSubtype'
_H='sanEventSourceType'
_G='sanEventSeverity'
_F='sanEventIPAddress'
_E='mandatory'
_D='optional'
_C='OctetString'
_B='read-only'
_A='CPQSANEVENT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
Compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqSanAppliance_ObjectIdentity=ObjectIdentity
cpqSanAppliance=_CpqSanAppliance_ObjectIdentity((1,3,6,1,4,1,232,151))
_SanEvent_ObjectIdentity=ObjectIdentity
sanEvent=_SanEvent_ObjectIdentity((1,3,6,1,4,1,232,151,101))
_SanEventObj_ObjectIdentity=ObjectIdentity
sanEventObj=_SanEventObj_ObjectIdentity((1,3,6,1,4,1,232,151,101,100))
class _SanEventEventCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_SanEventEventCode_Type.__name__=_C
_SanEventEventCode_Object=MibScalar
sanEventEventCode=_SanEventEventCode_Object((1,3,6,1,4,1,232,151,101,100,1),_SanEventEventCode_Type())
sanEventEventCode.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventEventCode.setStatus(_E)
class _SanEventIPAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_SanEventIPAddress_Type.__name__=_C
_SanEventIPAddress_Object=MibScalar
sanEventIPAddress=_SanEventIPAddress_Object((1,3,6,1,4,1,232,151,101,100,2),_SanEventIPAddress_Type())
sanEventIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventIPAddress.setStatus(_E)
_SanEventSeverity_Type=Integer32
_SanEventSeverity_Object=MibScalar
sanEventSeverity=_SanEventSeverity_Object((1,3,6,1,4,1,232,151,101,100,3),_SanEventSeverity_Type())
sanEventSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventSeverity.setStatus(_E)
_SanEventCategory_Type=Integer32
_SanEventCategory_Object=MibScalar
sanEventCategory=_SanEventCategory_Object((1,3,6,1,4,1,232,151,101,100,4),_SanEventCategory_Type())
sanEventCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventCategory.setStatus(_E)
class _SanEventGroup_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_SanEventGroup_Type.__name__=_C
_SanEventGroup_Object=MibScalar
sanEventGroup=_SanEventGroup_Object((1,3,6,1,4,1,232,151,101,100,5),_SanEventGroup_Type())
sanEventGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventGroup.setStatus(_D)
class _SanEventSourceType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_SanEventSourceType_Type.__name__=_C
_SanEventSourceType_Object=MibScalar
sanEventSourceType=_SanEventSourceType_Object((1,3,6,1,4,1,232,151,101,100,6),_SanEventSourceType_Type())
sanEventSourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventSourceType.setStatus(_D)
class _SanEventSourceSubtype_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_SanEventSourceSubtype_Type.__name__=_C
_SanEventSourceSubtype_Object=MibScalar
sanEventSourceSubtype=_SanEventSourceSubtype_Object((1,3,6,1,4,1,232,151,101,100,7),_SanEventSourceSubtype_Type())
sanEventSourceSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventSourceSubtype.setStatus(_D)
class _SanEventURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_SanEventURL_Type.__name__=_C
_SanEventURL_Object=MibScalar
sanEventURL=_SanEventURL_Object((1,3,6,1,4,1,232,151,101,100,8),_SanEventURL_Type())
sanEventURL.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventURL.setStatus(_D)
class _SanEventDesc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_SanEventDesc_Type.__name__=_C
_SanEventDesc_Object=MibScalar
sanEventDesc=_SanEventDesc_Object((1,3,6,1,4,1,232,151,101,100,9),_SanEventDesc_Type())
sanEventDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:sanEventDesc.setStatus(_D)
sanEventTrap=NotificationType((1,3,6,1,4,1,232,151,101,0,1))
sanEventTrap.setObjects(*((_A,_L),(_A,_F),(_A,_G),(_A,_M),(_A,_N),(_A,_H),(_A,_I),(_A,_J),(_A,_O)))
if mibBuilder.loadTexts:sanEventTrap.setStatus('')
sanTestTrap=NotificationType((1,3,6,1,4,1,232,151,101,0,2))
sanTestTrap.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:sanTestTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{'Compaq':Compaq,'cpqSanAppliance':cpqSanAppliance,'sanEvent':sanEvent,'sanEventTrap':sanEventTrap,'sanTestTrap':sanTestTrap,'sanEventObj':sanEventObj,_L:sanEventEventCode,_F:sanEventIPAddress,_G:sanEventSeverity,_M:sanEventCategory,_N:sanEventGroup,_H:sanEventSourceType,_I:sanEventSourceSubtype,_J:sanEventURL,_O:sanEventDesc})