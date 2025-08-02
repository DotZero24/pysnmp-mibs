_g='devConfigChangeKeysDbType'
_f='dslNAM'
_e='t3NniNAM'
_d='dualDsxNniNAM'
_c='ddsNAM'
_b='failedAPM'
_a='acceptingAPM'
_Z='pktVoiceAPM'
_Y='ocu4APM'
_X='sruAPM'
_W='dce6APM'
_V='ocu6APM'
_U='ocu2APM'
_T='t1NoDsxNAM'
_S='voiceFxoAPM'
_R='voiceEmAPM'
_Q='voiceFxsAPM'
_P='syncDataAPM'
_O='unsupportedAPM'
_N='emptySlot'
_M='devCfgCardSlot'
_L='devCfgClkWhichSrc'
_K='enable'
_J='disable'
_I='NotificationType'
_H='ifIndex'
_G='IF-MIB'
_F='noOp'
_E='PDN-CONFIG-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
pdn_devConfig,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-devConfig')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
_DevConfigArea_ObjectIdentity=ObjectIdentity
devConfigArea=_DevConfigArea_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,1))
class _DevConfigAreaCopy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*((_F,1),('active-to-customer1',2),('active-to-customer2',3),('customer1-to-active',4),('customer1-to-customer2',5),('customer2-to-active',6),('customer2-to-customer1',7),('factory1-to-active',8),('factory1-to-customer1',9),('factory1-to-customer2',10),('factory2-to-active',11),('factory2-to-customer1',12),('factory2-to-customer2',13),('factory3-to-active',14),('factory3-to-customer1',15),('factory3-to-customer2',16),('factory4-to-active',17),('factory4-to-customer1',18),('factory4-to-customer2',19),('factory5-to-active',20),('factory5-to-customer1',21),('factory5-to-customer2',22),('factory6-to-active',23),('factory6-to-customer1',24),('factory6-to-customer2',25),('factory7-to-active',26),('factory7-to-customer1',27),('factory7-to-customer2',28),('factory8-to-active',29),('factory8-to-customer1',30),('factory8-to-customer2',31),('factory9-to-active',32),('factory9-to-customer1',33),('factory9-to-customer2',34)))
_DevConfigAreaCopy_Type.__name__=_C
_DevConfigAreaCopy_Object=MibScalar
devConfigAreaCopy=_DevConfigAreaCopy_Object((1,3,6,1,4,1,1795,2,24,2,7,1,1),_DevConfigAreaCopy_Type())
devConfigAreaCopy.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigAreaCopy.setStatus(_A)
_DevConfigTestTimer_ObjectIdentity=ObjectIdentity
devConfigTestTimer=_DevConfigTestTimer_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,2))
class _DevConfigTestTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_DevConfigTestTimeout_Type.__name__=_C
_DevConfigTestTimeout_Object=MibScalar
devConfigTestTimeout=_DevConfigTestTimeout_Object((1,3,6,1,4,1,1795,2,24,2,7,2,1),_DevConfigTestTimeout_Type())
devConfigTestTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigTestTimeout.setStatus(_A)
_DevConfigTestDuration_Type=Integer32
_DevConfigTestDuration_Object=MibScalar
devConfigTestDuration=_DevConfigTestDuration_Object((1,3,6,1,4,1,1795,2,24,2,7,2,2),_DevConfigTestDuration_Type())
devConfigTestDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigTestDuration.setStatus(_A)
_DevConfigClockSrc_ObjectIdentity=ObjectIdentity
devConfigClockSrc=_DevConfigClockSrc_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,3))
_DevConfigClockSrcTable_Object=MibTable
devConfigClockSrcTable=_DevConfigClockSrcTable_Object((1,3,6,1,4,1,1795,2,24,2,7,3,1))
if mibBuilder.loadTexts:devConfigClockSrcTable.setStatus(_A)
_DevConfigClockSrcEntry_Object=MibTableRow
devConfigClockSrcEntry=_DevConfigClockSrcEntry_Object((1,3,6,1,4,1,1795,2,24,2,7,3,1,1))
devConfigClockSrcEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:devConfigClockSrcEntry.setStatus(_A)
class _DevCfgClkWhichSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_DevCfgClkWhichSrc_Type.__name__=_C
_DevCfgClkWhichSrc_Object=MibTableColumn
devCfgClkWhichSrc=_DevCfgClkWhichSrc_Object((1,3,6,1,4,1,1795,2,24,2,7,3,1,1,1),_DevCfgClkWhichSrc_Type())
devCfgClkWhichSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:devCfgClkWhichSrc.setStatus(_A)
class _DevCfgClkSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('internal',1),('external',2),('interface',3),('dbm',4),('external2',5)))
_DevCfgClkSource_Type.__name__=_C
_DevCfgClkSource_Object=MibTableColumn
devCfgClkSource=_DevCfgClkSource_Object((1,3,6,1,4,1,1795,2,24,2,7,3,1,1,2),_DevCfgClkSource_Type())
devCfgClkSource.setMaxAccess(_B)
if mibBuilder.loadTexts:devCfgClkSource.setStatus(_A)
_DevCfgClkIfIndex_Type=Integer32
_DevCfgClkIfIndex_Object=MibTableColumn
devCfgClkIfIndex=_DevCfgClkIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,7,3,1,1,3),_DevCfgClkIfIndex_Type())
devCfgClkIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:devCfgClkIfIndex.setStatus(_A)
class _DevCfgClkRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('rate400Hz',1),('rate8KHz',2),('rate64KHz',3),('rate1544KHz',4),('rate2048KHz',5)))
_DevCfgClkRate_Type.__name__=_C
_DevCfgClkRate_Object=MibTableColumn
devCfgClkRate=_DevCfgClkRate_Object((1,3,6,1,4,1,1795,2,24,2,7,3,1,1,4),_DevCfgClkRate_Type())
devCfgClkRate.setMaxAccess(_B)
if mibBuilder.loadTexts:devCfgClkRate.setStatus(_A)
_DevConfigTrap_ObjectIdentity=ObjectIdentity
devConfigTrap=_DevConfigTrap_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,4))
_DevConfigTrapEnable_Type=Integer32
_DevConfigTrapEnable_Object=MibScalar
devConfigTrapEnable=_DevConfigTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,7,4,1),_DevConfigTrapEnable_Type())
devConfigTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigTrapEnable.setStatus(_A)
_CCNTrapEnable_Type=Integer32
_CCNTrapEnable_Object=MibScalar
cCNTrapEnable=_CCNTrapEnable_Object((1,3,6,1,4,1,1795,2,24,2,7,4,2),_CCNTrapEnable_Type())
cCNTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cCNTrapEnable.setStatus(_A)
_DevConfigAlarm_ObjectIdentity=ObjectIdentity
devConfigAlarm=_DevConfigAlarm_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,5))
class _DevConfigAlarmRelayCutoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('off',2)))
_DevConfigAlarmRelayCutoff_Type.__name__=_C
_DevConfigAlarmRelayCutoff_Object=MibScalar
devConfigAlarmRelayCutoff=_DevConfigAlarmRelayCutoff_Object((1,3,6,1,4,1,1795,2,24,2,7,5,6),_DevConfigAlarmRelayCutoff_Type())
devConfigAlarmRelayCutoff.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigAlarmRelayCutoff.setStatus(_A)
_DevConfigCardType_ObjectIdentity=ObjectIdentity
devConfigCardType=_DevConfigCardType_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,6))
_DevConfigCardTypeTable_Object=MibTable
devConfigCardTypeTable=_DevConfigCardTypeTable_Object((1,3,6,1,4,1,1795,2,24,2,7,6,7))
if mibBuilder.loadTexts:devConfigCardTypeTable.setStatus(_A)
_DevConfigCardTypeEntry_Object=MibTableRow
devConfigCardTypeEntry=_DevConfigCardTypeEntry_Object((1,3,6,1,4,1,1795,2,24,2,7,6,7,1))
devConfigCardTypeEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:devConfigCardTypeEntry.setStatus(_A)
_DevCfgCardSlot_Type=Integer32
_DevCfgCardSlot_Object=MibTableColumn
devCfgCardSlot=_DevCfgCardSlot_Object((1,3,6,1,4,1,1795,2,24,2,7,6,7,1,1),_DevCfgCardSlot_Type())
devCfgCardSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:devCfgCardSlot.setStatus(_A)
class _DevCfgCardConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_N,1),(_O,2),('t1NAM',3),(_P,4),(_Q,5),(_R,6),(_S,7),('dsxAPM',8),(_T,9),('misconfiguredAPM',10),(_U,11),(_V,12),(_W,13),(_X,14),(_Y,15),(_Z,16),(_a,17),(_b,18),('dpNAM',19),('stNAM',20),(_c,21),(_d,22),(_e,23),('t3NAM',24),(_f,25)))
_DevCfgCardConfig_Type.__name__=_C
_DevCfgCardConfig_Object=MibTableColumn
devCfgCardConfig=_DevCfgCardConfig_Object((1,3,6,1,4,1,1795,2,24,2,7,6,7,1,2),_DevCfgCardConfig_Type())
devCfgCardConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:devCfgCardConfig.setStatus(_A)
class _DevCfgCardActual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*((_N,1),(_O,2),('t1NAM',3),(_P,4),(_Q,5),(_R,6),(_S,7),('voiceDsxAPM',8),(_T,9),('misconfigured',10),(_U,11),(_V,12),(_W,13),(_X,14),(_Y,15),(_Z,16),(_a,17),(_b,18),('dpNAM',19),('stNAM',20),(_c,21),(_d,22),(_e,23),('t3NAM',24),(_f,25)))
_DevCfgCardActual_Type.__name__=_C
_DevCfgCardActual_Object=MibTableColumn
devCfgCardActual=_DevCfgCardActual_Object((1,3,6,1,4,1,1795,2,24,2,7,6,7,1,3),_DevCfgCardActual_Type())
devCfgCardActual.setMaxAccess(_D)
if mibBuilder.loadTexts:devCfgCardActual.setStatus(_A)
class _DevCfgCardAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('accept',2)))
_DevCfgCardAction_Type.__name__=_C
_DevCfgCardAction_Object=MibTableColumn
devCfgCardAction=_DevCfgCardAction_Object((1,3,6,1,4,1,1795,2,24,2,7,6,7,1,4),_DevCfgCardAction_Type())
devCfgCardAction.setMaxAccess(_B)
if mibBuilder.loadTexts:devCfgCardAction.setStatus(_A)
_DevConfigNetSync_ObjectIdentity=ObjectIdentity
devConfigNetSync=_DevConfigNetSync_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,7))
class _DevConfigNetSyncRole_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('tributary',2),('controller',3)))
_DevConfigNetSyncRole_Type.__name__=_C
_DevConfigNetSyncRole_Object=MibScalar
devConfigNetSyncRole=_DevConfigNetSyncRole_Object((1,3,6,1,4,1,1795,2,24,2,7,7,1),_DevConfigNetSyncRole_Type())
devConfigNetSyncRole.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigNetSyncRole.setStatus(_A)
_DevConfigTime_ObjectIdentity=ObjectIdentity
devConfigTime=_DevConfigTime_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,8))
_DevConfigTimeOfDay_Type=DateAndTime
_DevConfigTimeOfDay_Object=MibScalar
devConfigTimeOfDay=_DevConfigTimeOfDay_Object((1,3,6,1,4,1,1795,2,24,2,7,8,1),_DevConfigTimeOfDay_Type())
devConfigTimeOfDay.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigTimeOfDay.setStatus(_A)
_DevConfigChangeKeys_ObjectIdentity=ObjectIdentity
devConfigChangeKeys=_DevConfigChangeKeys_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,9))
_DevConfigChangeKeysTable_Object=MibTable
devConfigChangeKeysTable=_DevConfigChangeKeysTable_Object((1,3,6,1,4,1,1795,2,24,2,7,9,1))
if mibBuilder.loadTexts:devConfigChangeKeysTable.setStatus(_A)
_DevConfigChangeKeysEntry_Object=MibTableRow
devConfigChangeKeysEntry=_DevConfigChangeKeysEntry_Object((1,3,6,1,4,1,1795,2,24,2,7,9,1,1))
devConfigChangeKeysEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:devConfigChangeKeysEntry.setStatus(_A)
class _DevConfigChangeKeysDbType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('generalConfig',1),('rmonAlarm',2),('rmonUserHistory',3),('routerConfig',4)))
_DevConfigChangeKeysDbType_Type.__name__=_C
_DevConfigChangeKeysDbType_Object=MibTableColumn
devConfigChangeKeysDbType=_DevConfigChangeKeysDbType_Object((1,3,6,1,4,1,1795,2,24,2,7,9,1,1,1),_DevConfigChangeKeysDbType_Type())
devConfigChangeKeysDbType.setMaxAccess(_D)
if mibBuilder.loadTexts:devConfigChangeKeysDbType.setStatus(_A)
_DevConfigChangeKeysDbKey_Type=Gauge32
_DevConfigChangeKeysDbKey_Object=MibTableColumn
devConfigChangeKeysDbKey=_DevConfigChangeKeysDbKey_Object((1,3,6,1,4,1,1795,2,24,2,7,9,1,1,2),_DevConfigChangeKeysDbKey_Type())
devConfigChangeKeysDbKey.setMaxAccess(_D)
if mibBuilder.loadTexts:devConfigChangeKeysDbKey.setStatus(_A)
_DevConfiguration_ObjectIdentity=ObjectIdentity
devConfiguration=_DevConfiguration_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,7,10))
_DevConfigComDiscTime_Type=Integer32
_DevConfigComDiscTime_Object=MibScalar
devConfigComDiscTime=_DevConfigComDiscTime_Object((1,3,6,1,4,1,1795,2,24,2,7,10,1),_DevConfigComDiscTime_Type())
devConfigComDiscTime.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigComDiscTime.setStatus(_A)
class _DevConfigPortNumDisplayFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sle',1),('unitport',2),('name',3)))
_DevConfigPortNumDisplayFormat_Type.__name__=_C
_DevConfigPortNumDisplayFormat_Object=MibScalar
devConfigPortNumDisplayFormat=_DevConfigPortNumDisplayFormat_Object((1,3,6,1,4,1,1795,2,24,2,7,10,2),_DevConfigPortNumDisplayFormat_Type())
devConfigPortNumDisplayFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigPortNumDisplayFormat.setStatus(_A)
class _DevConfigDateDisplayFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ddmmyy',1),('mmddyy',2)))
_DevConfigDateDisplayFormat_Type.__name__=_C
_DevConfigDateDisplayFormat_Object=MibScalar
devConfigDateDisplayFormat=_DevConfigDateDisplayFormat_Object((1,3,6,1,4,1,1795,2,24,2,7,10,3),_DevConfigDateDisplayFormat_Type())
devConfigDateDisplayFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:devConfigDateDisplayFormat.setStatus(_A)
class _DevAcceptRemoteResetFrame_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_DevAcceptRemoteResetFrame_Type.__name__=_C
_DevAcceptRemoteResetFrame_Object=MibScalar
devAcceptRemoteResetFrame=_DevAcceptRemoteResetFrame_Object((1,3,6,1,4,1,1795,2,24,2,7,10,4),_DevAcceptRemoteResetFrame_Type())
devAcceptRemoteResetFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:devAcceptRemoteResetFrame.setStatus(_A)
cCN=NotificationType((1,3,6,1,4,1,1795,2,24,2,7,4,0,7))
cCN.setObjects((_G,_H))
if mibBuilder.loadTexts:cCN.setStatus('')
mibBuilder.exportSymbols(_E,**{'devConfigArea':devConfigArea,'devConfigAreaCopy':devConfigAreaCopy,'devConfigTestTimer':devConfigTestTimer,'devConfigTestTimeout':devConfigTestTimeout,'devConfigTestDuration':devConfigTestDuration,'devConfigClockSrc':devConfigClockSrc,'devConfigClockSrcTable':devConfigClockSrcTable,'devConfigClockSrcEntry':devConfigClockSrcEntry,_L:devCfgClkWhichSrc,'devCfgClkSource':devCfgClkSource,'devCfgClkIfIndex':devCfgClkIfIndex,'devCfgClkRate':devCfgClkRate,'devConfigTrap':devConfigTrap,'cCN':cCN,'devConfigTrapEnable':devConfigTrapEnable,'cCNTrapEnable':cCNTrapEnable,'devConfigAlarm':devConfigAlarm,'devConfigAlarmRelayCutoff':devConfigAlarmRelayCutoff,'devConfigCardType':devConfigCardType,'devConfigCardTypeTable':devConfigCardTypeTable,'devConfigCardTypeEntry':devConfigCardTypeEntry,_M:devCfgCardSlot,'devCfgCardConfig':devCfgCardConfig,'devCfgCardActual':devCfgCardActual,'devCfgCardAction':devCfgCardAction,'devConfigNetSync':devConfigNetSync,'devConfigNetSyncRole':devConfigNetSyncRole,'devConfigTime':devConfigTime,'devConfigTimeOfDay':devConfigTimeOfDay,'devConfigChangeKeys':devConfigChangeKeys,'devConfigChangeKeysTable':devConfigChangeKeysTable,'devConfigChangeKeysEntry':devConfigChangeKeysEntry,_g:devConfigChangeKeysDbType,'devConfigChangeKeysDbKey':devConfigChangeKeysDbKey,'devConfiguration':devConfiguration,'devConfigComDiscTime':devConfigComDiscTime,'devConfigPortNumDisplayFormat':devConfigPortNumDisplayFormat,'devConfigDateDisplayFormat':devConfigDateDisplayFormat,'devAcceptRemoteResetFrame':devAcceptRemoteResetFrame})