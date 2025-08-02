_b='zxAnVoiceDigitMapName'
_a='zxAnVoiceCtrlPortId'
_Z='zxAnVoiceToneCategory'
_Y='zxAnVoiceToneArea'
_X='zxAnVoiceFirstRingingMgId'
_W='srilanka'
_V='europe'
_U='russia'
_T='singapore'
_S='hongkong'
_R='mainland'
_Q='zxAnDsx1LinkNo'
_P='zxAnDsx1Slot'
_O='zxAnDsx1Shelf'
_N='zxAnDsx1Rack'
_M='msagRPId'
_L='msagRPRingProfile'
_K='0.1dBov'
_J='DisplayString'
_I='Bits'
_H='10ms'
_G='read-only'
_F='not-accessible'
_E='ZTE-AN-VOICE-GLOBAL-MIB'
_D='read-create'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAnVoiceGlobalMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,5200))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxAn_ObjectIdentity=ObjectIdentity
zxAn=_ZxAn_ObjectIdentity((1,3,6,1,4,1,3902,1015))
_ZxAnVoiceMgmt_ObjectIdentity=ObjectIdentity
zxAnVoiceMgmt=_ZxAnVoiceMgmt_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3))
_ZxAnVoiceGlobalConfig_ObjectIdentity=ObjectIdentity
zxAnVoiceGlobalConfig=_ZxAnVoiceGlobalConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1))
_MsagRingProfileTable_Object=MibTable
msagRingProfileTable=_MsagRingProfileTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6))
if mibBuilder.loadTexts:msagRingProfileTable.setStatus(_A)
_MsagRingProfileEntry_Object=MibTableRow
msagRingProfileEntry=_MsagRingProfileEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1))
msagRingProfileEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:msagRingProfileEntry.setStatus(_A)
class _MsagRPRingProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,12,15)));namedValues=NamedValues(*(('profMainLand',1),('profHongkong',2),('profSingapore',3),('profRussia',4),('profEurope',5),('profBELGIUM',12),('profSrilanka',15)))
_MsagRPRingProfile_Type.__name__=_B
_MsagRPRingProfile_Object=MibTableColumn
msagRPRingProfile=_MsagRPRingProfile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,1),_MsagRPRingProfile_Type())
msagRPRingProfile.setMaxAccess(_F)
if mibBuilder.loadTexts:msagRPRingProfile.setStatus(_A)
class _MsagRPId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_MsagRPId_Type.__name__=_B
_MsagRPId_Object=MibTableColumn
msagRPId=_MsagRPId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,2),_MsagRPId_Type())
msagRPId.setMaxAccess(_F)
if mibBuilder.loadTexts:msagRPId.setStatus(_A)
class _MsagRPTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPTime_Type.__name__=_B
_MsagRPTime_Object=MibTableColumn
msagRPTime=_MsagRPTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,3),_MsagRPTime_Type())
msagRPTime.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPTime.setStatus(_A)
class _MsagRPOn1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOn1_Type.__name__=_B
_MsagRPOn1_Object=MibTableColumn
msagRPOn1=_MsagRPOn1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,4),_MsagRPOn1_Type())
msagRPOn1.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOn1.setStatus(_A)
class _MsagRPOff1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOff1_Type.__name__=_B
_MsagRPOff1_Object=MibTableColumn
msagRPOff1=_MsagRPOff1_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,5),_MsagRPOff1_Type())
msagRPOff1.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOff1.setStatus(_A)
class _MsagRPOn2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOn2_Type.__name__=_B
_MsagRPOn2_Object=MibTableColumn
msagRPOn2=_MsagRPOn2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,6),_MsagRPOn2_Type())
msagRPOn2.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOn2.setStatus(_A)
class _MsagRPOff2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOff2_Type.__name__=_B
_MsagRPOff2_Object=MibTableColumn
msagRPOff2=_MsagRPOff2_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,7),_MsagRPOff2_Type())
msagRPOff2.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOff2.setStatus(_A)
class _MsagRPOn3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOn3_Type.__name__=_B
_MsagRPOn3_Object=MibTableColumn
msagRPOn3=_MsagRPOn3_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,8),_MsagRPOn3_Type())
msagRPOn3.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOn3.setStatus(_A)
class _MsagRPOff3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOff3_Type.__name__=_B
_MsagRPOff3_Object=MibTableColumn
msagRPOff3=_MsagRPOff3_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,9),_MsagRPOff3_Type())
msagRPOff3.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOff3.setStatus(_A)
class _MsagRPOn4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOn4_Type.__name__=_B
_MsagRPOn4_Object=MibTableColumn
msagRPOn4=_MsagRPOn4_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,10),_MsagRPOn4_Type())
msagRPOn4.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOn4.setStatus(_A)
class _MsagRPOff4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOff4_Type.__name__=_B
_MsagRPOff4_Object=MibTableColumn
msagRPOff4=_MsagRPOff4_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,11),_MsagRPOff4_Type())
msagRPOff4.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOff4.setStatus(_A)
class _MsagRPOn5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOn5_Type.__name__=_B
_MsagRPOn5_Object=MibTableColumn
msagRPOn5=_MsagRPOn5_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,12),_MsagRPOn5_Type())
msagRPOn5.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOn5.setStatus(_A)
class _MsagRPOff5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsagRPOff5_Type.__name__=_B
_MsagRPOff5_Object=MibTableColumn
msagRPOff5=_MsagRPOff5_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,13),_MsagRPOff5_Type())
msagRPOff5.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPOff5.setStatus(_A)
_MsagRPRowStatus_Type=RowStatus
_MsagRPRowStatus_Object=MibTableColumn
msagRPRowStatus=_MsagRPRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,6,1,14),_MsagRPRowStatus_Type())
msagRPRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:msagRPRowStatus.setStatus(_A)
_ZxAnDsx1Table_Object=MibTable
zxAnDsx1Table=_ZxAnDsx1Table_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16))
if mibBuilder.loadTexts:zxAnDsx1Table.setStatus(_A)
_ZxAnDsx1Entry_Object=MibTableRow
zxAnDsx1Entry=_ZxAnDsx1Entry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16,1))
zxAnDsx1Entry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:zxAnDsx1Entry.setStatus(_A)
class _ZxAnDsx1Rack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3))
_ZxAnDsx1Rack_Type.__name__=_B
_ZxAnDsx1Rack_Object=MibTableColumn
zxAnDsx1Rack=_ZxAnDsx1Rack_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16,1,1),_ZxAnDsx1Rack_Type())
zxAnDsx1Rack.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDsx1Rack.setStatus(_A)
class _ZxAnDsx1Shelf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_ZxAnDsx1Shelf_Type.__name__=_B
_ZxAnDsx1Shelf_Object=MibTableColumn
zxAnDsx1Shelf=_ZxAnDsx1Shelf_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16,1,2),_ZxAnDsx1Shelf_Type())
zxAnDsx1Shelf.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDsx1Shelf.setStatus(_A)
class _ZxAnDsx1Slot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_ZxAnDsx1Slot_Type.__name__=_B
_ZxAnDsx1Slot_Object=MibTableColumn
zxAnDsx1Slot=_ZxAnDsx1Slot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16,1,3),_ZxAnDsx1Slot_Type())
zxAnDsx1Slot.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDsx1Slot.setStatus(_A)
class _ZxAnDsx1LinkNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_ZxAnDsx1LinkNo_Type.__name__=_B
_ZxAnDsx1LinkNo_Object=MibTableColumn
zxAnDsx1LinkNo=_ZxAnDsx1LinkNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16,1,4),_ZxAnDsx1LinkNo_Type())
zxAnDsx1LinkNo.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnDsx1LinkNo.setStatus(_A)
class _ZxAnDsx1Loopback_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLoopback',1),('localLoopback',2),('remoteLineLoopback',3)))
_ZxAnDsx1Loopback_Type.__name__=_B
_ZxAnDsx1Loopback_Object=MibTableColumn
zxAnDsx1Loopback=_ZxAnDsx1Loopback_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16,1,5),_ZxAnDsx1Loopback_Type())
zxAnDsx1Loopback.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDsx1Loopback.setStatus(_A)
class _ZxAnDsx1FramingMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('withoutCrc',1),('withCrc',2),('sameAsPeers',3)))
_ZxAnDsx1FramingMode_Type.__name__=_B
_ZxAnDsx1FramingMode_Object=MibTableColumn
zxAnDsx1FramingMode=_ZxAnDsx1FramingMode_Object((1,3,6,1,4,1,3902,1015,5200,3,1,16,1,6),_ZxAnDsx1FramingMode_Type())
zxAnDsx1FramingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnDsx1FramingMode.setStatus(_A)
_ZxAnVoiceGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnVoiceGlobalObjects=_ZxAnVoiceGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,1000))
class _ZxAnVoiceGlobalMgmtCapabilities_Type(Bits):namedValues=NamedValues(('nbPlatform',0))
_ZxAnVoiceGlobalMgmtCapabilities_Type.__name__=_I
_ZxAnVoiceGlobalMgmtCapabilities_Object=MibScalar
zxAnVoiceGlobalMgmtCapabilities=_ZxAnVoiceGlobalMgmtCapabilities_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1000,1),_ZxAnVoiceGlobalMgmtCapabilities_Type())
zxAnVoiceGlobalMgmtCapabilities.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceGlobalMgmtCapabilities.setStatus(_A)
class _ZxAnVoiceServiceLicense_Type(Bits):namedValues=NamedValues(*(('h248',0),('mgcp',1),('v5',2),('voipIsdn',3),('reserved1',4),('reserved2',5),('sip',6)))
_ZxAnVoiceServiceLicense_Type.__name__=_I
_ZxAnVoiceServiceLicense_Object=MibScalar
zxAnVoiceServiceLicense=_ZxAnVoiceServiceLicense_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1000,2),_ZxAnVoiceServiceLicense_Type())
zxAnVoiceServiceLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceServiceLicense.setStatus(_A)
_ZxAnVoiceSysMgmtObjects_ObjectIdentity=ObjectIdentity
zxAnVoiceSysMgmtObjects=_ZxAnVoiceSysMgmtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,1000,10))
class _ZxAnVoiceSysArea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,15)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,15)))
_ZxAnVoiceSysArea_Type.__name__=_B
_ZxAnVoiceSysArea_Object=MibScalar
zxAnVoiceSysArea=_ZxAnVoiceSysArea_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1000,10,1),_ZxAnVoiceSysArea_Type())
zxAnVoiceSysArea.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceSysArea.setStatus(_A)
class _ZxAnVoiceSysCallMatchType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('longMatch',1),('shortMatch',2)))
_ZxAnVoiceSysCallMatchType_Type.__name__=_B
_ZxAnVoiceSysCallMatchType_Object=MibScalar
zxAnVoiceSysCallMatchType=_ZxAnVoiceSysCallMatchType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1000,10,2),_ZxAnVoiceSysCallMatchType_Type())
zxAnVoiceSysCallMatchType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceSysCallMatchType.setStatus(_A)
class _ZxAnVoiceSysLoadDftRingProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('load',1))
_ZxAnVoiceSysLoadDftRingProfile_Type.__name__=_B
_ZxAnVoiceSysLoadDftRingProfile_Object=MibScalar
zxAnVoiceSysLoadDftRingProfile=_ZxAnVoiceSysLoadDftRingProfile_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1000,10,3),_ZxAnVoiceSysLoadDftRingProfile_Type())
zxAnVoiceSysLoadDftRingProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceSysLoadDftRingProfile.setStatus(_A)
_ZxAnVoiceFirstRingingTable_Object=MibTable
zxAnVoiceFirstRingingTable=_ZxAnVoiceFirstRingingTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1002))
if mibBuilder.loadTexts:zxAnVoiceFirstRingingTable.setStatus(_A)
_ZxAnVoiceFirstRingingEntry_Object=MibTableRow
zxAnVoiceFirstRingingEntry=_ZxAnVoiceFirstRingingEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1002,1))
zxAnVoiceFirstRingingEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:zxAnVoiceFirstRingingEntry.setStatus(_A)
_ZxAnVoiceFirstRingingMgId_Type=Integer32
_ZxAnVoiceFirstRingingMgId_Object=MibTableColumn
zxAnVoiceFirstRingingMgId=_ZxAnVoiceFirstRingingMgId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1002,1,1),_ZxAnVoiceFirstRingingMgId_Type())
zxAnVoiceFirstRingingMgId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoiceFirstRingingMgId.setStatus(_A)
class _ZxAnVoiceFirstRingingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('accordingToCid',1),('differentFromOtherRings',2),('sameWithOtherRings',3)))
_ZxAnVoiceFirstRingingType_Type.__name__=_B
_ZxAnVoiceFirstRingingType_Object=MibTableColumn
zxAnVoiceFirstRingingType=_ZxAnVoiceFirstRingingType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1002,1,2),_ZxAnVoiceFirstRingingType_Type())
zxAnVoiceFirstRingingType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceFirstRingingType.setStatus(_A)
class _ZxAnVoiceFirstRingingTime_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,120))
_ZxAnVoiceFirstRingingTime_Type.__name__=_B
_ZxAnVoiceFirstRingingTime_Object=MibTableColumn
zxAnVoiceFirstRingingTime=_ZxAnVoiceFirstRingingTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1002,1,3),_ZxAnVoiceFirstRingingTime_Type())
zxAnVoiceFirstRingingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceFirstRingingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceFirstRingingTime.setUnits(_H)
class _ZxAnVoiceFirstRingingInterval_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,400))
_ZxAnVoiceFirstRingingInterval_Type.__name__=_B
_ZxAnVoiceFirstRingingInterval_Object=MibTableColumn
zxAnVoiceFirstRingingInterval=_ZxAnVoiceFirstRingingInterval_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1002,1,4),_ZxAnVoiceFirstRingingInterval_Type())
zxAnVoiceFirstRingingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceFirstRingingInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceFirstRingingInterval.setUnits(_H)
_ZxAnVoiceToneProfileTable_Object=MibTable
zxAnVoiceToneProfileTable=_ZxAnVoiceToneProfileTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003))
if mibBuilder.loadTexts:zxAnVoiceToneProfileTable.setStatus(_A)
_ZxAnVoiceToneProfileEntry_Object=MibTableRow
zxAnVoiceToneProfileEntry=_ZxAnVoiceToneProfileEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1))
zxAnVoiceToneProfileEntry.setIndexNames((0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:zxAnVoiceToneProfileEntry.setStatus(_A)
class _ZxAnVoiceToneArea_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,15)));namedValues=NamedValues(*((_R,1),(_S,2),(_T,3),(_U,4),(_V,5),(_W,15)))
_ZxAnVoiceToneArea_Type.__name__=_B
_ZxAnVoiceToneArea_Object=MibTableColumn
zxAnVoiceToneArea=_ZxAnVoiceToneArea_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,1),_ZxAnVoiceToneArea_Type())
zxAnVoiceToneArea.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoiceToneArea.setStatus(_A)
class _ZxAnVoiceToneCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,10013,10014,10015,10016,10017,10018,10019,10020,10021,10025,10031,10032,10033,10035,10036,10037,10038,10039)));namedValues=NamedValues(*(('dialTone',1),('ringbackTone',2),('busyTone',3),('congestionTone',4),('specialDialTone',5),('howlerTone',6),('verificationTone',7),('callWaitingTone',8),('stutterDialTone',9),('numberUnobtainableTone',10),('recallDialTone',11),('holdingTone',12),('callWaitingToneA',10013),('callWaitingToneB',10014),('callWaitingToneC',10015),('callWaitingToneD',10016),('callWaitingToneE',10017),('expensiveRouteWarningTone',10018),('bargeInTone',10019),('testNumberTone',10020),('intrusionTone',10021),('sitTone',10025),('busyHowlerTone',10031),('conferenceNoReadyTone',10032),('conferenceExitTone',10033),('advancedSpecialInfoTone',10035),('trunkBusyTone',10036),('advancedHoldingTone',10037),('interventionTone',10038),('wrongDialTone',10039)))
_ZxAnVoiceToneCategory_Type.__name__=_B
_ZxAnVoiceToneCategory_Object=MibTableColumn
zxAnVoiceToneCategory=_ZxAnVoiceToneCategory_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,2),_ZxAnVoiceToneCategory_Type())
zxAnVoiceToneCategory.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoiceToneCategory.setStatus(_A)
class _ZxAnVoiceToneDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnVoiceToneDuration_Type.__name__=_B
_ZxAnVoiceToneDuration_Object=MibTableColumn
zxAnVoiceToneDuration=_ZxAnVoiceToneDuration_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,3),_ZxAnVoiceToneDuration_Type())
zxAnVoiceToneDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceToneDuration.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceToneDuration.setUnits('100ms')
class _ZxAnVoiceToneFirstWaveFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceToneFirstWaveFrequency_Type.__name__=_B
_ZxAnVoiceToneFirstWaveFrequency_Object=MibTableColumn
zxAnVoiceToneFirstWaveFrequency=_ZxAnVoiceToneFirstWaveFrequency_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,4),_ZxAnVoiceToneFirstWaveFrequency_Type())
zxAnVoiceToneFirstWaveFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceToneFirstWaveFrequency.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceToneFirstWaveFrequency.setUnits('Hz')
class _ZxAnVoiceToneFirstWaveAmplitude_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_ZxAnVoiceToneFirstWaveAmplitude_Type.__name__=_B
_ZxAnVoiceToneFirstWaveAmplitude_Object=MibTableColumn
zxAnVoiceToneFirstWaveAmplitude=_ZxAnVoiceToneFirstWaveAmplitude_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,5),_ZxAnVoiceToneFirstWaveAmplitude_Type())
zxAnVoiceToneFirstWaveAmplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceToneFirstWaveAmplitude.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceToneFirstWaveAmplitude.setUnits(_K)
class _ZxAnVoiceToneSecondWaveFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceToneSecondWaveFrequency_Type.__name__=_B
_ZxAnVoiceToneSecondWaveFrequency_Object=MibTableColumn
zxAnVoiceToneSecondWaveFrequency=_ZxAnVoiceToneSecondWaveFrequency_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,6),_ZxAnVoiceToneSecondWaveFrequency_Type())
zxAnVoiceToneSecondWaveFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceToneSecondWaveFrequency.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceToneSecondWaveFrequency.setUnits('Hz')
class _ZxAnVoiceToneSecondWaveAmplitude_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_ZxAnVoiceToneSecondWaveAmplitude_Type.__name__=_B
_ZxAnVoiceToneSecondWaveAmplitude_Object=MibTableColumn
zxAnVoiceToneSecondWaveAmplitude=_ZxAnVoiceToneSecondWaveAmplitude_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,7),_ZxAnVoiceToneSecondWaveAmplitude_Type())
zxAnVoiceToneSecondWaveAmplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceToneSecondWaveAmplitude.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceToneSecondWaveAmplitude.setUnits(_K)
class _ZxAnVoiceToneThirdWaveFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceToneThirdWaveFrequency_Type.__name__=_B
_ZxAnVoiceToneThirdWaveFrequency_Object=MibTableColumn
zxAnVoiceToneThirdWaveFrequency=_ZxAnVoiceToneThirdWaveFrequency_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,8),_ZxAnVoiceToneThirdWaveFrequency_Type())
zxAnVoiceToneThirdWaveFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceToneThirdWaveFrequency.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceToneThirdWaveFrequency.setUnits('Hz')
class _ZxAnVoiceToneThirdWaveAmplitude_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_ZxAnVoiceToneThirdWaveAmplitude_Type.__name__=_B
_ZxAnVoiceToneThirdWaveAmplitude_Object=MibTableColumn
zxAnVoiceToneThirdWaveAmplitude=_ZxAnVoiceToneThirdWaveAmplitude_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,9),_ZxAnVoiceToneThirdWaveAmplitude_Type())
zxAnVoiceToneThirdWaveAmplitude.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceToneThirdWaveAmplitude.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceToneThirdWaveAmplitude.setUnits(_K)
class _ZxAnVoicFirstWaveTimeSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnVoicFirstWaveTimeSlot_Type.__name__=_B
_ZxAnVoicFirstWaveTimeSlot_Object=MibTableColumn
zxAnVoicFirstWaveTimeSlot=_ZxAnVoicFirstWaveTimeSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,10),_ZxAnVoicFirstWaveTimeSlot_Type())
zxAnVoicFirstWaveTimeSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoicFirstWaveTimeSlot.setStatus(_A)
class _ZxAnVoicSecondWaveTimeSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnVoicSecondWaveTimeSlot_Type.__name__=_B
_ZxAnVoicSecondWaveTimeSlot_Object=MibTableColumn
zxAnVoicSecondWaveTimeSlot=_ZxAnVoicSecondWaveTimeSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,11),_ZxAnVoicSecondWaveTimeSlot_Type())
zxAnVoicSecondWaveTimeSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoicSecondWaveTimeSlot.setStatus(_A)
class _ZxAnVoicThirdWaveTimeSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnVoicThirdWaveTimeSlot_Type.__name__=_B
_ZxAnVoicThirdWaveTimeSlot_Object=MibTableColumn
zxAnVoicThirdWaveTimeSlot=_ZxAnVoicThirdWaveTimeSlot_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,12),_ZxAnVoicThirdWaveTimeSlot_Type())
zxAnVoicThirdWaveTimeSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoicThirdWaveTimeSlot.setStatus(_A)
class _ZxAnVoiceFirstToneSendingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceFirstToneSendingTime_Type.__name__=_B
_ZxAnVoiceFirstToneSendingTime_Object=MibTableColumn
zxAnVoiceFirstToneSendingTime=_ZxAnVoiceFirstToneSendingTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,13),_ZxAnVoiceFirstToneSendingTime_Type())
zxAnVoiceFirstToneSendingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceFirstToneSendingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceFirstToneSendingTime.setUnits(_H)
class _ZxAnVoiceFirstToneBreakTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceFirstToneBreakTime_Type.__name__=_B
_ZxAnVoiceFirstToneBreakTime_Object=MibTableColumn
zxAnVoiceFirstToneBreakTime=_ZxAnVoiceFirstToneBreakTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,14),_ZxAnVoiceFirstToneBreakTime_Type())
zxAnVoiceFirstToneBreakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceFirstToneBreakTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceFirstToneBreakTime.setUnits(_H)
class _ZxAnVoiceSecondToneSendingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceSecondToneSendingTime_Type.__name__=_B
_ZxAnVoiceSecondToneSendingTime_Object=MibTableColumn
zxAnVoiceSecondToneSendingTime=_ZxAnVoiceSecondToneSendingTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,15),_ZxAnVoiceSecondToneSendingTime_Type())
zxAnVoiceSecondToneSendingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceSecondToneSendingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceSecondToneSendingTime.setUnits(_H)
class _ZxAnVoiceSecondToneBreakTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceSecondToneBreakTime_Type.__name__=_B
_ZxAnVoiceSecondToneBreakTime_Object=MibTableColumn
zxAnVoiceSecondToneBreakTime=_ZxAnVoiceSecondToneBreakTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,16),_ZxAnVoiceSecondToneBreakTime_Type())
zxAnVoiceSecondToneBreakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceSecondToneBreakTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceSecondToneBreakTime.setUnits(_H)
class _ZxAnVoiceThirdToneSendingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceThirdToneSendingTime_Type.__name__=_B
_ZxAnVoiceThirdToneSendingTime_Object=MibTableColumn
zxAnVoiceThirdToneSendingTime=_ZxAnVoiceThirdToneSendingTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,17),_ZxAnVoiceThirdToneSendingTime_Type())
zxAnVoiceThirdToneSendingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceThirdToneSendingTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceThirdToneSendingTime.setUnits(_H)
class _ZxAnVoiceThirdToneBreakTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceThirdToneBreakTime_Type.__name__=_B
_ZxAnVoiceThirdToneBreakTime_Object=MibTableColumn
zxAnVoiceThirdToneBreakTime=_ZxAnVoiceThirdToneBreakTime_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1003,1,18),_ZxAnVoiceThirdToneBreakTime_Type())
zxAnVoiceThirdToneBreakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnVoiceThirdToneBreakTime.setStatus(_A)
if mibBuilder.loadTexts:zxAnVoiceThirdToneBreakTime.setUnits(_H)
_ZxAnVoiceCtrlPortTable_Object=MibTable
zxAnVoiceCtrlPortTable=_ZxAnVoiceCtrlPortTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1004))
if mibBuilder.loadTexts:zxAnVoiceCtrlPortTable.setStatus(_A)
_ZxAnVoiceCtrlPortEntry_Object=MibTableRow
zxAnVoiceCtrlPortEntry=_ZxAnVoiceCtrlPortEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1004,1))
zxAnVoiceCtrlPortEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:zxAnVoiceCtrlPortEntry.setStatus(_A)
class _ZxAnVoiceCtrlPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,40))
_ZxAnVoiceCtrlPortId_Type.__name__=_B
_ZxAnVoiceCtrlPortId_Object=MibTableColumn
zxAnVoiceCtrlPortId=_ZxAnVoiceCtrlPortId_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1004,1,1),_ZxAnVoiceCtrlPortId_Type())
zxAnVoiceCtrlPortId.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoiceCtrlPortId.setStatus(_A)
class _ZxAnVoiceCtrlPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('udp',1),('tcp',2)))
_ZxAnVoiceCtrlPortType_Type.__name__=_B
_ZxAnVoiceCtrlPortType_Object=MibTableColumn
zxAnVoiceCtrlPortType=_ZxAnVoiceCtrlPortType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1004,1,2),_ZxAnVoiceCtrlPortType_Type())
zxAnVoiceCtrlPortType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoiceCtrlPortType.setStatus(_A)
class _ZxAnVoiceCtrlPortNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ZxAnVoiceCtrlPortNo_Type.__name__=_B
_ZxAnVoiceCtrlPortNo_Object=MibTableColumn
zxAnVoiceCtrlPortNo=_ZxAnVoiceCtrlPortNo_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1004,1,3),_ZxAnVoiceCtrlPortNo_Type())
zxAnVoiceCtrlPortNo.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoiceCtrlPortNo.setStatus(_A)
_ZxAnVoiceCtrlPortRowStatus_Type=RowStatus
_ZxAnVoiceCtrlPortRowStatus_Object=MibTableColumn
zxAnVoiceCtrlPortRowStatus=_ZxAnVoiceCtrlPortRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1004,1,20),_ZxAnVoiceCtrlPortRowStatus_Type())
zxAnVoiceCtrlPortRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoiceCtrlPortRowStatus.setStatus(_A)
_ZxAnVoiceDigitMapTable_Object=MibTable
zxAnVoiceDigitMapTable=_ZxAnVoiceDigitMapTable_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1005))
if mibBuilder.loadTexts:zxAnVoiceDigitMapTable.setStatus(_A)
_ZxAnVoiceDigitMapEntry_Object=MibTableRow
zxAnVoiceDigitMapEntry=_ZxAnVoiceDigitMapEntry_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1005,1))
zxAnVoiceDigitMapEntry.setIndexNames((0,_E,_b))
if mibBuilder.loadTexts:zxAnVoiceDigitMapEntry.setStatus(_A)
class _ZxAnVoiceDigitMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_ZxAnVoiceDigitMapName_Type.__name__=_J
_ZxAnVoiceDigitMapName_Object=MibTableColumn
zxAnVoiceDigitMapName=_ZxAnVoiceDigitMapName_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1005,1,1),_ZxAnVoiceDigitMapName_Type())
zxAnVoiceDigitMapName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnVoiceDigitMapName.setStatus(_A)
class _ZxAnVoiceDigitMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('selfSwitch',1),('sip',2),('emergencyCall',3)))
_ZxAnVoiceDigitMapType_Type.__name__=_B
_ZxAnVoiceDigitMapType_Object=MibTableColumn
zxAnVoiceDigitMapType=_ZxAnVoiceDigitMapType_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1005,1,2),_ZxAnVoiceDigitMapType_Type())
zxAnVoiceDigitMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoiceDigitMapType.setStatus(_A)
class _ZxAnVoiceDigitMapBody_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,4095))
_ZxAnVoiceDigitMapBody_Type.__name__=_J
_ZxAnVoiceDigitMapBody_Object=MibTableColumn
zxAnVoiceDigitMapBody=_ZxAnVoiceDigitMapBody_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1005,1,3),_ZxAnVoiceDigitMapBody_Type())
zxAnVoiceDigitMapBody.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoiceDigitMapBody.setStatus(_A)
_ZxAnVoiceDigitMapRowStatus_Type=RowStatus
_ZxAnVoiceDigitMapRowStatus_Object=MibTableColumn
zxAnVoiceDigitMapRowStatus=_ZxAnVoiceDigitMapRowStatus_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1005,1,30),_ZxAnVoiceDigitMapRowStatus_Type())
zxAnVoiceDigitMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnVoiceDigitMapRowStatus.setStatus(_A)
_ZxAnVoicePortNumberStatsObjects_ObjectIdentity=ObjectIdentity
zxAnVoicePortNumberStatsObjects=_ZxAnVoicePortNumberStatsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,1050))
_ZxAnVoiceActivePortStatsObjects_ObjectIdentity=ObjectIdentity
zxAnVoiceActivePortStatsObjects=_ZxAnVoiceActivePortStatsObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1))
_ZxAnVoiceActiveV5PotsPorts_Type=Integer32
_ZxAnVoiceActiveV5PotsPorts_Object=MibScalar
zxAnVoiceActiveV5PotsPorts=_ZxAnVoiceActiveV5PotsPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,1),_ZxAnVoiceActiveV5PotsPorts_Type())
zxAnVoiceActiveV5PotsPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveV5PotsPorts.setStatus(_A)
_ZxAnVoiceActiveV5BriPorts_Type=Integer32
_ZxAnVoiceActiveV5BriPorts_Object=MibScalar
zxAnVoiceActiveV5BriPorts=_ZxAnVoiceActiveV5BriPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,2),_ZxAnVoiceActiveV5BriPorts_Type())
zxAnVoiceActiveV5BriPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveV5BriPorts.setStatus(_A)
_ZxAnVoiceActiveV5PriPorts_Type=Integer32
_ZxAnVoiceActiveV5PriPorts_Object=MibScalar
zxAnVoiceActiveV5PriPorts=_ZxAnVoiceActiveV5PriPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,3),_ZxAnVoiceActiveV5PriPorts_Type())
zxAnVoiceActiveV5PriPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveV5PriPorts.setStatus(_A)
_ZxAnVoiceActiveH248PotsPorts_Type=Integer32
_ZxAnVoiceActiveH248PotsPorts_Object=MibScalar
zxAnVoiceActiveH248PotsPorts=_ZxAnVoiceActiveH248PotsPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,4),_ZxAnVoiceActiveH248PotsPorts_Type())
zxAnVoiceActiveH248PotsPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveH248PotsPorts.setStatus(_A)
_ZxAnVoiceActiveH248BriPorts_Type=Integer32
_ZxAnVoiceActiveH248BriPorts_Object=MibScalar
zxAnVoiceActiveH248BriPorts=_ZxAnVoiceActiveH248BriPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,5),_ZxAnVoiceActiveH248BriPorts_Type())
zxAnVoiceActiveH248BriPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveH248BriPorts.setStatus(_A)
_ZxAnVoiceActiveH248PriPorts_Type=Integer32
_ZxAnVoiceActiveH248PriPorts_Object=MibScalar
zxAnVoiceActiveH248PriPorts=_ZxAnVoiceActiveH248PriPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,6),_ZxAnVoiceActiveH248PriPorts_Type())
zxAnVoiceActiveH248PriPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveH248PriPorts.setStatus(_A)
_ZxAnVoiceActiveSipPotsPorts_Type=Integer32
_ZxAnVoiceActiveSipPotsPorts_Object=MibScalar
zxAnVoiceActiveSipPotsPorts=_ZxAnVoiceActiveSipPotsPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,7),_ZxAnVoiceActiveSipPotsPorts_Type())
zxAnVoiceActiveSipPotsPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveSipPotsPorts.setStatus(_A)
_ZxAnVoiceActiveSipBriPorts_Type=Integer32
_ZxAnVoiceActiveSipBriPorts_Object=MibScalar
zxAnVoiceActiveSipBriPorts=_ZxAnVoiceActiveSipBriPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,8),_ZxAnVoiceActiveSipBriPorts_Type())
zxAnVoiceActiveSipBriPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveSipBriPorts.setStatus(_A)
_ZxAnVoiceActiveSipPriPorts_Type=Integer32
_ZxAnVoiceActiveSipPriPorts_Object=MibScalar
zxAnVoiceActiveSipPriPorts=_ZxAnVoiceActiveSipPriPorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,9),_ZxAnVoiceActiveSipPriPorts_Type())
zxAnVoiceActiveSipPriPorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveSipPriPorts.setStatus(_A)
_ZxAnVoiceActiveLeasedLinePorts_Type=Integer32
_ZxAnVoiceActiveLeasedLinePorts_Object=MibScalar
zxAnVoiceActiveLeasedLinePorts=_ZxAnVoiceActiveLeasedLinePorts_Object((1,3,6,1,4,1,3902,1015,5200,3,1,1050,1,10),_ZxAnVoiceActiveLeasedLinePorts_Type())
zxAnVoiceActiveLeasedLinePorts.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnVoiceActiveLeasedLinePorts.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zte':zte,'zxAn':zxAn,'zxAnVoiceGlobalMib':zxAnVoiceGlobalMib,'zxAnVoiceMgmt':zxAnVoiceMgmt,'zxAnVoiceGlobalConfig':zxAnVoiceGlobalConfig,'msagRingProfileTable':msagRingProfileTable,'msagRingProfileEntry':msagRingProfileEntry,_L:msagRPRingProfile,_M:msagRPId,'msagRPTime':msagRPTime,'msagRPOn1':msagRPOn1,'msagRPOff1':msagRPOff1,'msagRPOn2':msagRPOn2,'msagRPOff2':msagRPOff2,'msagRPOn3':msagRPOn3,'msagRPOff3':msagRPOff3,'msagRPOn4':msagRPOn4,'msagRPOff4':msagRPOff4,'msagRPOn5':msagRPOn5,'msagRPOff5':msagRPOff5,'msagRPRowStatus':msagRPRowStatus,'zxAnDsx1Table':zxAnDsx1Table,'zxAnDsx1Entry':zxAnDsx1Entry,_N:zxAnDsx1Rack,_O:zxAnDsx1Shelf,_P:zxAnDsx1Slot,_Q:zxAnDsx1LinkNo,'zxAnDsx1Loopback':zxAnDsx1Loopback,'zxAnDsx1FramingMode':zxAnDsx1FramingMode,'zxAnVoiceGlobalObjects':zxAnVoiceGlobalObjects,'zxAnVoiceGlobalMgmtCapabilities':zxAnVoiceGlobalMgmtCapabilities,'zxAnVoiceServiceLicense':zxAnVoiceServiceLicense,'zxAnVoiceSysMgmtObjects':zxAnVoiceSysMgmtObjects,'zxAnVoiceSysArea':zxAnVoiceSysArea,'zxAnVoiceSysCallMatchType':zxAnVoiceSysCallMatchType,'zxAnVoiceSysLoadDftRingProfile':zxAnVoiceSysLoadDftRingProfile,'zxAnVoiceFirstRingingTable':zxAnVoiceFirstRingingTable,'zxAnVoiceFirstRingingEntry':zxAnVoiceFirstRingingEntry,_X:zxAnVoiceFirstRingingMgId,'zxAnVoiceFirstRingingType':zxAnVoiceFirstRingingType,'zxAnVoiceFirstRingingTime':zxAnVoiceFirstRingingTime,'zxAnVoiceFirstRingingInterval':zxAnVoiceFirstRingingInterval,'zxAnVoiceToneProfileTable':zxAnVoiceToneProfileTable,'zxAnVoiceToneProfileEntry':zxAnVoiceToneProfileEntry,_Y:zxAnVoiceToneArea,_Z:zxAnVoiceToneCategory,'zxAnVoiceToneDuration':zxAnVoiceToneDuration,'zxAnVoiceToneFirstWaveFrequency':zxAnVoiceToneFirstWaveFrequency,'zxAnVoiceToneFirstWaveAmplitude':zxAnVoiceToneFirstWaveAmplitude,'zxAnVoiceToneSecondWaveFrequency':zxAnVoiceToneSecondWaveFrequency,'zxAnVoiceToneSecondWaveAmplitude':zxAnVoiceToneSecondWaveAmplitude,'zxAnVoiceToneThirdWaveFrequency':zxAnVoiceToneThirdWaveFrequency,'zxAnVoiceToneThirdWaveAmplitude':zxAnVoiceToneThirdWaveAmplitude,'zxAnVoicFirstWaveTimeSlot':zxAnVoicFirstWaveTimeSlot,'zxAnVoicSecondWaveTimeSlot':zxAnVoicSecondWaveTimeSlot,'zxAnVoicThirdWaveTimeSlot':zxAnVoicThirdWaveTimeSlot,'zxAnVoiceFirstToneSendingTime':zxAnVoiceFirstToneSendingTime,'zxAnVoiceFirstToneBreakTime':zxAnVoiceFirstToneBreakTime,'zxAnVoiceSecondToneSendingTime':zxAnVoiceSecondToneSendingTime,'zxAnVoiceSecondToneBreakTime':zxAnVoiceSecondToneBreakTime,'zxAnVoiceThirdToneSendingTime':zxAnVoiceThirdToneSendingTime,'zxAnVoiceThirdToneBreakTime':zxAnVoiceThirdToneBreakTime,'zxAnVoiceCtrlPortTable':zxAnVoiceCtrlPortTable,'zxAnVoiceCtrlPortEntry':zxAnVoiceCtrlPortEntry,_a:zxAnVoiceCtrlPortId,'zxAnVoiceCtrlPortType':zxAnVoiceCtrlPortType,'zxAnVoiceCtrlPortNo':zxAnVoiceCtrlPortNo,'zxAnVoiceCtrlPortRowStatus':zxAnVoiceCtrlPortRowStatus,'zxAnVoiceDigitMapTable':zxAnVoiceDigitMapTable,'zxAnVoiceDigitMapEntry':zxAnVoiceDigitMapEntry,_b:zxAnVoiceDigitMapName,'zxAnVoiceDigitMapType':zxAnVoiceDigitMapType,'zxAnVoiceDigitMapBody':zxAnVoiceDigitMapBody,'zxAnVoiceDigitMapRowStatus':zxAnVoiceDigitMapRowStatus,'zxAnVoicePortNumberStatsObjects':zxAnVoicePortNumberStatsObjects,'zxAnVoiceActivePortStatsObjects':zxAnVoiceActivePortStatsObjects,'zxAnVoiceActiveV5PotsPorts':zxAnVoiceActiveV5PotsPorts,'zxAnVoiceActiveV5BriPorts':zxAnVoiceActiveV5BriPorts,'zxAnVoiceActiveV5PriPorts':zxAnVoiceActiveV5PriPorts,'zxAnVoiceActiveH248PotsPorts':zxAnVoiceActiveH248PotsPorts,'zxAnVoiceActiveH248BriPorts':zxAnVoiceActiveH248BriPorts,'zxAnVoiceActiveH248PriPorts':zxAnVoiceActiveH248PriPorts,'zxAnVoiceActiveSipPotsPorts':zxAnVoiceActiveSipPotsPorts,'zxAnVoiceActiveSipBriPorts':zxAnVoiceActiveSipBriPorts,'zxAnVoiceActiveSipPriPorts':zxAnVoiceActiveSipPriPorts,'zxAnVoiceActiveLeasedLinePorts':zxAnVoiceActiveLeasedLinePorts})