_e='bnLogMsgBufferNonVolCurSize'
_d='bnLogMsgBufferCurSize'
_c='connectionTypeTCPSecure'
_b='connectionTypeTCP'
_a='connectionTypeUDP'
_Z='msgTypeDebug'
_Y='msgTypeNotice'
_X='msgTypeError'
_W='msgTypeAlert'
_V='msgTypeEmergency'
_U='bnLogMsgRemoteServerAddress'
_T='bnLogMsgRemoteServerAddressType'
_S='bnLogMsgBufferMsgIndex'
_R='bnLogMsgBufferMsgTime'
_Q='bnLogMsgBufferMsgOrig'
_P='deprecated'
_O='IpAddress'
_N='TruthValue'
_M='InetAddressType'
_L='read-create'
_K='InetAddress'
_J='not-accessible'
_I='msgTypeNone'
_H='BN-LOG-MESSAGE-MIB'
_G='msgTypeInformational'
_F='msgTypeSerious'
_E='msgTypeCritical'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,_M)
bnLogMsg,=mibBuilder.importSymbols('S5-ROOT-MIB','bnLogMsg')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_O,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention',_N)
bnLogMsgMIB=ModuleIdentity((1,3,6,1,4,1,45,1,6,16,1))
if mibBuilder.loadTexts:bnLogMsgMIB.setRevisions(('2016-02-01 00:00','2015-11-02 00:00','2013-10-10 00:00','2012-04-10 00:00','2012-03-26 00:00','2011-04-20 00:00','2010-06-29 00:00','2009-04-15 00:00','2009-04-14 00:00','2009-03-31 00:00','2009-03-23 00:00','2007-09-04 00:00','2005-05-04 00:00','2005-04-27 00:00','2003-02-24 12:00'))
_BnLogMsgMIBObjects_ObjectIdentity=ObjectIdentity
bnLogMsgMIBObjects=_BnLogMsgMIBObjects_ObjectIdentity((1,3,6,1,4,1,45,1,6,16,1,1))
class _BnLogMsgBufferOperaton_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_BnLogMsgBufferOperaton_Type.__name__=_B
_BnLogMsgBufferOperaton_Object=MibScalar
bnLogMsgBufferOperaton=_BnLogMsgBufferOperaton_Object((1,3,6,1,4,1,45,1,6,16,1,1,1),_BnLogMsgBufferOperaton_Type())
bnLogMsgBufferOperaton.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgBufferOperaton.setStatus(_A)
class _BnLogMsgBufferMaxSize_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(50,100,200,400,1500)));namedValues=NamedValues(*(('msgBufferSizeSmall',50),('msgBufferSizeMedium',100),('msgBufferSizeLarge',200),('msgBufferSizeVeryLarge',400),('msgBufferSizeExtraLarge',1500)))
_BnLogMsgBufferMaxSize_Type.__name__=_B
_BnLogMsgBufferMaxSize_Object=MibScalar
bnLogMsgBufferMaxSize=_BnLogMsgBufferMaxSize_Object((1,3,6,1,4,1,45,1,6,16,1,1,2),_BnLogMsgBufferMaxSize_Type())
bnLogMsgBufferMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgBufferMaxSize.setStatus(_A)
class _BnLogMsgBufferCurSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_BnLogMsgBufferCurSize_Type.__name__=_B
_BnLogMsgBufferCurSize_Object=MibScalar
bnLogMsgBufferCurSize=_BnLogMsgBufferCurSize_Object((1,3,6,1,4,1,45,1,6,16,1,1,3),_BnLogMsgBufferCurSize_Type())
bnLogMsgBufferCurSize.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferCurSize.setStatus(_A)
class _BnLogMsgBufferFullAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('overwrite',1),('latch',2)))
_BnLogMsgBufferFullAction_Type.__name__=_B
_BnLogMsgBufferFullAction_Object=MibScalar
bnLogMsgBufferFullAction=_BnLogMsgBufferFullAction_Object((1,3,6,1,4,1,45,1,6,16,1,1,4),_BnLogMsgBufferFullAction_Type())
bnLogMsgBufferFullAction.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgBufferFullAction.setStatus(_A)
class _BnLogMsgBufferSaveTargets_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_I,4)))
_BnLogMsgBufferSaveTargets_Type.__name__=_B
_BnLogMsgBufferSaveTargets_Object=MibScalar
bnLogMsgBufferSaveTargets=_BnLogMsgBufferSaveTargets_Object((1,3,6,1,4,1,45,1,6,16,1,1,5),_BnLogMsgBufferSaveTargets_Type())
bnLogMsgBufferSaveTargets.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgBufferSaveTargets.setStatus(_A)
class _BnLogMsgBufferClearTargets_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),('msgTypeAllVolatile',4),('msgTypeNonVolatile',5)))
_BnLogMsgBufferClearTargets_Type.__name__=_B
_BnLogMsgBufferClearTargets_Object=MibScalar
bnLogMsgBufferClearTargets=_BnLogMsgBufferClearTargets_Object((1,3,6,1,4,1,45,1,6,16,1,1,6),_BnLogMsgBufferClearTargets_Type())
bnLogMsgBufferClearTargets.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgBufferClearTargets.setStatus(_P)
class _BnLogMsgBufferClearMsgs_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clearMsgs',1),('savingMsgs',2)))
_BnLogMsgBufferClearMsgs_Type.__name__=_B
_BnLogMsgBufferClearMsgs_Object=MibScalar
bnLogMsgBufferClearMsgs=_BnLogMsgBufferClearMsgs_Object((1,3,6,1,4,1,45,1,6,16,1,1,7),_BnLogMsgBufferClearMsgs_Type())
bnLogMsgBufferClearMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgBufferClearMsgs.setStatus(_P)
class _BnLogMsgBufferNonVolCurSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_BnLogMsgBufferNonVolCurSize_Type.__name__=_B
_BnLogMsgBufferNonVolCurSize_Object=MibScalar
bnLogMsgBufferNonVolCurSize=_BnLogMsgBufferNonVolCurSize_Object((1,3,6,1,4,1,45,1,6,16,1,1,8),_BnLogMsgBufferNonVolCurSize_Type())
bnLogMsgBufferNonVolCurSize.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferNonVolCurSize.setStatus(_A)
class _BnLogMsgBufferNonVolSaveTargets_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_I,4)))
_BnLogMsgBufferNonVolSaveTargets_Type.__name__=_B
_BnLogMsgBufferNonVolSaveTargets_Object=MibScalar
bnLogMsgBufferNonVolSaveTargets=_BnLogMsgBufferNonVolSaveTargets_Object((1,3,6,1,4,1,45,1,6,16,1,1,9),_BnLogMsgBufferNonVolSaveTargets_Type())
bnLogMsgBufferNonVolSaveTargets.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgBufferNonVolSaveTargets.setStatus(_A)
_BnLogMsgBufferTable_Object=MibTable
bnLogMsgBufferTable=_BnLogMsgBufferTable_Object((1,3,6,1,4,1,45,1,6,16,1,1,10))
if mibBuilder.loadTexts:bnLogMsgBufferTable.setStatus(_A)
_BnLogMsgBufferEntry_Object=MibTableRow
bnLogMsgBufferEntry=_BnLogMsgBufferEntry_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1))
bnLogMsgBufferEntry.setIndexNames((0,_H,_Q),(0,_H,_R),(0,_H,_S))
if mibBuilder.loadTexts:bnLogMsgBufferEntry.setStatus(_A)
class _BnLogMsgBufferMsgIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BnLogMsgBufferMsgIndex_Type.__name__=_B
_BnLogMsgBufferMsgIndex_Object=MibTableColumn
bnLogMsgBufferMsgIndex=_BnLogMsgBufferMsgIndex_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,1),_BnLogMsgBufferMsgIndex_Type())
bnLogMsgBufferMsgIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:bnLogMsgBufferMsgIndex.setStatus(_A)
class _BnLogMsgBufferMsgOrig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_BnLogMsgBufferMsgOrig_Type.__name__=_B
_BnLogMsgBufferMsgOrig_Object=MibTableColumn
bnLogMsgBufferMsgOrig=_BnLogMsgBufferMsgOrig_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,2),_BnLogMsgBufferMsgOrig_Type())
bnLogMsgBufferMsgOrig.setMaxAccess(_J)
if mibBuilder.loadTexts:bnLogMsgBufferMsgOrig.setStatus(_A)
_BnLogMsgBufferMsgTime_Type=TimeTicks
_BnLogMsgBufferMsgTime_Object=MibTableColumn
bnLogMsgBufferMsgTime=_BnLogMsgBufferMsgTime_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,3),_BnLogMsgBufferMsgTime_Type())
bnLogMsgBufferMsgTime.setMaxAccess(_J)
if mibBuilder.loadTexts:bnLogMsgBufferMsgTime.setStatus(_A)
class _BnLogMsgBufferMsgSrc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('msgSrcRunning',1),('msgSrcNonVol',2)))
_BnLogMsgBufferMsgSrc_Type.__name__=_B
_BnLogMsgBufferMsgSrc_Object=MibTableColumn
bnLogMsgBufferMsgSrc=_BnLogMsgBufferMsgSrc_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,4),_BnLogMsgBufferMsgSrc_Type())
bnLogMsgBufferMsgSrc.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgSrc.setStatus(_A)
_BnLogMsgBufferMsgCode_Type=Integer32
_BnLogMsgBufferMsgCode_Object=MibTableColumn
bnLogMsgBufferMsgCode=_BnLogMsgBufferMsgCode_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,5),_BnLogMsgBufferMsgCode_Type())
bnLogMsgBufferMsgCode.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgCode.setStatus(_A)
_BnLogMsgBufferMsgString_Type=DisplayString
_BnLogMsgBufferMsgString_Object=MibTableColumn
bnLogMsgBufferMsgString=_BnLogMsgBufferMsgString_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,6),_BnLogMsgBufferMsgString_Type())
bnLogMsgBufferMsgString.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgString.setStatus(_A)
_BnLogMsgBufferMsgParam1_Type=Integer32
_BnLogMsgBufferMsgParam1_Object=MibTableColumn
bnLogMsgBufferMsgParam1=_BnLogMsgBufferMsgParam1_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,7),_BnLogMsgBufferMsgParam1_Type())
bnLogMsgBufferMsgParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgParam1.setStatus(_A)
_BnLogMsgBufferMsgParam2_Type=Integer32
_BnLogMsgBufferMsgParam2_Object=MibTableColumn
bnLogMsgBufferMsgParam2=_BnLogMsgBufferMsgParam2_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,8),_BnLogMsgBufferMsgParam2_Type())
bnLogMsgBufferMsgParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgParam2.setStatus(_A)
_BnLogMsgBufferMsgParam3_Type=Integer32
_BnLogMsgBufferMsgParam3_Object=MibTableColumn
bnLogMsgBufferMsgParam3=_BnLogMsgBufferMsgParam3_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,9),_BnLogMsgBufferMsgParam3_Type())
bnLogMsgBufferMsgParam3.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgParam3.setStatus(_A)
_BnLogMsgBufferMsgUtcTime_Type=DateAndTime
_BnLogMsgBufferMsgUtcTime_Object=MibTableColumn
bnLogMsgBufferMsgUtcTime=_BnLogMsgBufferMsgUtcTime_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,10),_BnLogMsgBufferMsgUtcTime_Type())
bnLogMsgBufferMsgUtcTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgUtcTime.setStatus(_A)
class _BnLogMsgBufferMsgType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_I,4)))
_BnLogMsgBufferMsgType_Type.__name__=_B
_BnLogMsgBufferMsgType_Object=MibTableColumn
bnLogMsgBufferMsgType=_BnLogMsgBufferMsgType_Object((1,3,6,1,4,1,45,1,6,16,1,1,10,1,11),_BnLogMsgBufferMsgType_Type())
bnLogMsgBufferMsgType.setMaxAccess(_D)
if mibBuilder.loadTexts:bnLogMsgBufferMsgType.setStatus(_A)
class _BnLogMsgRemoteSyslogEnabled_Type(TruthValue):defaultValue=2
_BnLogMsgRemoteSyslogEnabled_Type.__name__=_N
_BnLogMsgRemoteSyslogEnabled_Object=MibScalar
bnLogMsgRemoteSyslogEnabled=_BnLogMsgRemoteSyslogEnabled_Object((1,3,6,1,4,1,45,1,6,16,1,1,11),_BnLogMsgRemoteSyslogEnabled_Type())
bnLogMsgRemoteSyslogEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogEnabled.setStatus(_A)
class _BnLogMsgRemoteSyslogAddress_Type(IpAddress):defaultHexValue='00000000'
_BnLogMsgRemoteSyslogAddress_Type.__name__=_O
_BnLogMsgRemoteSyslogAddress_Object=MibScalar
bnLogMsgRemoteSyslogAddress=_BnLogMsgRemoteSyslogAddress_Object((1,3,6,1,4,1,45,1,6,16,1,1,12),_BnLogMsgRemoteSyslogAddress_Type())
bnLogMsgRemoteSyslogAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogAddress.setStatus(_A)
class _BnLogMsgRemoteSyslogSaveTargets_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_I,4)))
_BnLogMsgRemoteSyslogSaveTargets_Type.__name__=_B
_BnLogMsgRemoteSyslogSaveTargets_Object=MibScalar
bnLogMsgRemoteSyslogSaveTargets=_BnLogMsgRemoteSyslogSaveTargets_Object((1,3,6,1,4,1,45,1,6,16,1,1,13),_BnLogMsgRemoteSyslogSaveTargets_Type())
bnLogMsgRemoteSyslogSaveTargets.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogSaveTargets.setStatus(_A)
class _BnLogMsgClearMessageBuffers_Type(Bits):namedValues=NamedValues(*(('none',0),('volCritical',1),('volSerious',2),('volInformational',3),('nonVolCritical',4),('nonVolSerious',5),('nonVolInformational',6)))
_BnLogMsgClearMessageBuffers_Type.__name__='Bits'
_BnLogMsgClearMessageBuffers_Object=MibScalar
bnLogMsgClearMessageBuffers=_BnLogMsgClearMessageBuffers_Object((1,3,6,1,4,1,45,1,6,16,1,1,14),_BnLogMsgClearMessageBuffers_Type())
bnLogMsgClearMessageBuffers.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgClearMessageBuffers.setStatus(_A)
class _BnLogMsgRemoteSyslogInetAddressType_Type(InetAddressType):defaultValue=0
_BnLogMsgRemoteSyslogInetAddressType_Type.__name__=_M
_BnLogMsgRemoteSyslogInetAddressType_Object=MibScalar
bnLogMsgRemoteSyslogInetAddressType=_BnLogMsgRemoteSyslogInetAddressType_Object((1,3,6,1,4,1,45,1,6,16,1,1,15),_BnLogMsgRemoteSyslogInetAddressType_Type())
bnLogMsgRemoteSyslogInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogInetAddressType.setStatus(_A)
class _BnLogMsgRemoteSyslogInetAddress_Type(InetAddress):defaultHexValue=''
_BnLogMsgRemoteSyslogInetAddress_Type.__name__=_K
_BnLogMsgRemoteSyslogInetAddress_Object=MibScalar
bnLogMsgRemoteSyslogInetAddress=_BnLogMsgRemoteSyslogInetAddress_Object((1,3,6,1,4,1,45,1,6,16,1,1,16),_BnLogMsgRemoteSyslogInetAddress_Type())
bnLogMsgRemoteSyslogInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogInetAddress.setStatus(_A)
class _BnLogMsgRemoteSyslogSecondaryInetAddressType_Type(InetAddressType):defaultValue=0
_BnLogMsgRemoteSyslogSecondaryInetAddressType_Type.__name__=_M
_BnLogMsgRemoteSyslogSecondaryInetAddressType_Object=MibScalar
bnLogMsgRemoteSyslogSecondaryInetAddressType=_BnLogMsgRemoteSyslogSecondaryInetAddressType_Object((1,3,6,1,4,1,45,1,6,16,1,1,17),_BnLogMsgRemoteSyslogSecondaryInetAddressType_Type())
bnLogMsgRemoteSyslogSecondaryInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogSecondaryInetAddressType.setStatus(_A)
class _BnLogMsgRemoteSyslogSecondaryInetAddress_Type(InetAddress):defaultHexValue=''
_BnLogMsgRemoteSyslogSecondaryInetAddress_Type.__name__=_K
_BnLogMsgRemoteSyslogSecondaryInetAddress_Object=MibScalar
bnLogMsgRemoteSyslogSecondaryInetAddress=_BnLogMsgRemoteSyslogSecondaryInetAddress_Object((1,3,6,1,4,1,45,1,6,16,1,1,18),_BnLogMsgRemoteSyslogSecondaryInetAddress_Type())
bnLogMsgRemoteSyslogSecondaryInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogSecondaryInetAddress.setStatus(_A)
_BnLogMsgRemoteServerTable_Object=MibTable
bnLogMsgRemoteServerTable=_BnLogMsgRemoteServerTable_Object((1,3,6,1,4,1,45,1,6,16,1,1,19))
if mibBuilder.loadTexts:bnLogMsgRemoteServerTable.setStatus(_A)
_BnLogMsgRemoteServerEntry_Object=MibTableRow
bnLogMsgRemoteServerEntry=_BnLogMsgRemoteServerEntry_Object((1,3,6,1,4,1,45,1,6,16,1,1,19,1))
bnLogMsgRemoteServerEntry.setIndexNames((0,_H,_T),(0,_H,_U))
if mibBuilder.loadTexts:bnLogMsgRemoteServerEntry.setStatus(_A)
_BnLogMsgRemoteServerAddressType_Type=InetAddressType
_BnLogMsgRemoteServerAddressType_Object=MibTableColumn
bnLogMsgRemoteServerAddressType=_BnLogMsgRemoteServerAddressType_Object((1,3,6,1,4,1,45,1,6,16,1,1,19,1,1),_BnLogMsgRemoteServerAddressType_Type())
bnLogMsgRemoteServerAddressType.setMaxAccess(_J)
if mibBuilder.loadTexts:bnLogMsgRemoteServerAddressType.setStatus(_A)
class _BnLogMsgRemoteServerAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_BnLogMsgRemoteServerAddress_Type.__name__=_K
_BnLogMsgRemoteServerAddress_Object=MibTableColumn
bnLogMsgRemoteServerAddress=_BnLogMsgRemoteServerAddress_Object((1,3,6,1,4,1,45,1,6,16,1,1,19,1,2),_BnLogMsgRemoteServerAddress_Type())
bnLogMsgRemoteServerAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:bnLogMsgRemoteServerAddress.setStatus(_A)
class _BnLogMsgRemoteServerEnabled_Type(TruthValue):defaultValue=1
_BnLogMsgRemoteServerEnabled_Type.__name__=_N
_BnLogMsgRemoteServerEnabled_Object=MibTableColumn
bnLogMsgRemoteServerEnabled=_BnLogMsgRemoteServerEnabled_Object((1,3,6,1,4,1,45,1,6,16,1,1,19,1,3),_BnLogMsgRemoteServerEnabled_Type())
bnLogMsgRemoteServerEnabled.setMaxAccess(_L)
if mibBuilder.loadTexts:bnLogMsgRemoteServerEnabled.setStatus(_A)
class _BnLogMsgRemoteServerSaveTargets_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_I,4)))
_BnLogMsgRemoteServerSaveTargets_Type.__name__=_B
_BnLogMsgRemoteServerSaveTargets_Object=MibTableColumn
bnLogMsgRemoteServerSaveTargets=_BnLogMsgRemoteServerSaveTargets_Object((1,3,6,1,4,1,45,1,6,16,1,1,19,1,4),_BnLogMsgRemoteServerSaveTargets_Type())
bnLogMsgRemoteServerSaveTargets.setMaxAccess(_L)
if mibBuilder.loadTexts:bnLogMsgRemoteServerSaveTargets.setStatus(_A)
_BnLogMsgRemoteServerRowStatus_Type=RowStatus
_BnLogMsgRemoteServerRowStatus_Object=MibTableColumn
bnLogMsgRemoteServerRowStatus=_BnLogMsgRemoteServerRowStatus_Object((1,3,6,1,4,1,45,1,6,16,1,1,19,1,5),_BnLogMsgRemoteServerRowStatus_Type())
bnLogMsgRemoteServerRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:bnLogMsgRemoteServerRowStatus.setStatus(_A)
class _BnLogMsgRemoteServerStandardSaveTargets_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_V,0),(_W,1),(_E,2),(_X,3),(_F,4),(_Y,5),(_G,6),(_Z,7),(_I,8)))
_BnLogMsgRemoteServerStandardSaveTargets_Type.__name__=_B
_BnLogMsgRemoteServerStandardSaveTargets_Object=MibTableColumn
bnLogMsgRemoteServerStandardSaveTargets=_BnLogMsgRemoteServerStandardSaveTargets_Object((1,3,6,1,4,1,45,1,6,16,1,1,19,1,6),_BnLogMsgRemoteServerStandardSaveTargets_Type())
bnLogMsgRemoteServerStandardSaveTargets.setMaxAccess(_L)
if mibBuilder.loadTexts:bnLogMsgRemoteServerStandardSaveTargets.setStatus(_A)
class _BnLogMsgRemoteSyslogFacility_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('fltKernel',1),('fltUserLevel',2),('fltMailSystem',3),('fltDaemon',4),('fltSecAuthor',5),('fltMsgGenInt',6),('fltLinePrinter',7),('fltNetNews',8),('fltUUCP',9),('fltClockDaemon',10),('fltSecAuthor2',11),('fltFTPDaemon',12),('fltNTP',13),('fltLogAudit',14),('fltLogAlert',15),('fltClockDaemon2',16),('fltLocal0',17),('fltLocal1',18),('fltLocal2',19),('fltLocal3',20),('fltLocal4',21),('fltLocal5',22),('fltLocal6',23),('fltLocal7',24),('fltNone',25)))
_BnLogMsgRemoteSyslogFacility_Type.__name__=_B
_BnLogMsgRemoteSyslogFacility_Object=MibScalar
bnLogMsgRemoteSyslogFacility=_BnLogMsgRemoteSyslogFacility_Object((1,3,6,1,4,1,45,1,6,16,1,1,20),_BnLogMsgRemoteSyslogFacility_Type())
bnLogMsgRemoteSyslogFacility.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogFacility.setStatus(_A)
class _BnLogMsgRemoteSyslogStandardSaveTargets_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_V,0),(_W,1),(_E,2),(_X,3),(_F,4),(_Y,5),(_G,6),(_Z,7),(_I,8)))
_BnLogMsgRemoteSyslogStandardSaveTargets_Type.__name__=_B
_BnLogMsgRemoteSyslogStandardSaveTargets_Object=MibScalar
bnLogMsgRemoteSyslogStandardSaveTargets=_BnLogMsgRemoteSyslogStandardSaveTargets_Object((1,3,6,1,4,1,45,1,6,16,1,1,21),_BnLogMsgRemoteSyslogStandardSaveTargets_Type())
bnLogMsgRemoteSyslogStandardSaveTargets.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogStandardSaveTargets.setStatus(_A)
class _BnLogMsgRemoteSyslogPrimaryTcpPort_Type(Integer32):defaultValue=601;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(601,601),ValueRangeConstraint(1024,65535))
_BnLogMsgRemoteSyslogPrimaryTcpPort_Type.__name__=_B
_BnLogMsgRemoteSyslogPrimaryTcpPort_Object=MibScalar
bnLogMsgRemoteSyslogPrimaryTcpPort=_BnLogMsgRemoteSyslogPrimaryTcpPort_Object((1,3,6,1,4,1,45,1,6,16,1,1,22),_BnLogMsgRemoteSyslogPrimaryTcpPort_Type())
bnLogMsgRemoteSyslogPrimaryTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogPrimaryTcpPort.setStatus(_A)
class _BnLogMsgRemoteSyslogSecondaryTcpPort_Type(Integer32):defaultValue=601;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(601,601),ValueRangeConstraint(1024,65535))
_BnLogMsgRemoteSyslogSecondaryTcpPort_Type.__name__=_B
_BnLogMsgRemoteSyslogSecondaryTcpPort_Object=MibScalar
bnLogMsgRemoteSyslogSecondaryTcpPort=_BnLogMsgRemoteSyslogSecondaryTcpPort_Object((1,3,6,1,4,1,45,1,6,16,1,1,23),_BnLogMsgRemoteSyslogSecondaryTcpPort_Type())
bnLogMsgRemoteSyslogSecondaryTcpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogSecondaryTcpPort.setStatus(_A)
class _BnLogMsgRemoteSyslogPrimaryConnectionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3)))
_BnLogMsgRemoteSyslogPrimaryConnectionType_Type.__name__=_B
_BnLogMsgRemoteSyslogPrimaryConnectionType_Object=MibScalar
bnLogMsgRemoteSyslogPrimaryConnectionType=_BnLogMsgRemoteSyslogPrimaryConnectionType_Object((1,3,6,1,4,1,45,1,6,16,1,1,24),_BnLogMsgRemoteSyslogPrimaryConnectionType_Type())
bnLogMsgRemoteSyslogPrimaryConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogPrimaryConnectionType.setStatus(_A)
class _BnLogMsgRemoteSyslogSecondaryConnectionType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_a,1),(_b,2),(_c,3)))
_BnLogMsgRemoteSyslogSecondaryConnectionType_Type.__name__=_B
_BnLogMsgRemoteSyslogSecondaryConnectionType_Object=MibScalar
bnLogMsgRemoteSyslogSecondaryConnectionType=_BnLogMsgRemoteSyslogSecondaryConnectionType_Object((1,3,6,1,4,1,45,1,6,16,1,1,25),_BnLogMsgRemoteSyslogSecondaryConnectionType_Type())
bnLogMsgRemoteSyslogSecondaryConnectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:bnLogMsgRemoteSyslogSecondaryConnectionType.setStatus(_A)
_BnLogMsgMIBTraps_ObjectIdentity=ObjectIdentity
bnLogMsgMIBTraps=_BnLogMsgMIBTraps_ObjectIdentity((1,3,6,1,4,1,45,1,6,16,1,2))
_BnLogMsgMIBTrapPrefix_ObjectIdentity=ObjectIdentity
bnLogMsgMIBTrapPrefix=_BnLogMsgMIBTrapPrefix_ObjectIdentity((1,3,6,1,4,1,45,1,6,16,1,2,0))
_BnLogMsgMIBConformance_ObjectIdentity=ObjectIdentity
bnLogMsgMIBConformance=_BnLogMsgMIBConformance_ObjectIdentity((1,3,6,1,4,1,45,1,6,16,1,3))
bnLogMsgBufferFull=NotificationType((1,3,6,1,4,1,45,1,6,16,1,2,0,1))
bnLogMsgBufferFull.setObjects(*((_H,_d),(_H,_e)))
if mibBuilder.loadTexts:bnLogMsgBufferFull.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'bnLogMsgMIB':bnLogMsgMIB,'bnLogMsgMIBObjects':bnLogMsgMIBObjects,'bnLogMsgBufferOperaton':bnLogMsgBufferOperaton,'bnLogMsgBufferMaxSize':bnLogMsgBufferMaxSize,_d:bnLogMsgBufferCurSize,'bnLogMsgBufferFullAction':bnLogMsgBufferFullAction,'bnLogMsgBufferSaveTargets':bnLogMsgBufferSaveTargets,'bnLogMsgBufferClearTargets':bnLogMsgBufferClearTargets,'bnLogMsgBufferClearMsgs':bnLogMsgBufferClearMsgs,_e:bnLogMsgBufferNonVolCurSize,'bnLogMsgBufferNonVolSaveTargets':bnLogMsgBufferNonVolSaveTargets,'bnLogMsgBufferTable':bnLogMsgBufferTable,'bnLogMsgBufferEntry':bnLogMsgBufferEntry,_S:bnLogMsgBufferMsgIndex,_Q:bnLogMsgBufferMsgOrig,_R:bnLogMsgBufferMsgTime,'bnLogMsgBufferMsgSrc':bnLogMsgBufferMsgSrc,'bnLogMsgBufferMsgCode':bnLogMsgBufferMsgCode,'bnLogMsgBufferMsgString':bnLogMsgBufferMsgString,'bnLogMsgBufferMsgParam1':bnLogMsgBufferMsgParam1,'bnLogMsgBufferMsgParam2':bnLogMsgBufferMsgParam2,'bnLogMsgBufferMsgParam3':bnLogMsgBufferMsgParam3,'bnLogMsgBufferMsgUtcTime':bnLogMsgBufferMsgUtcTime,'bnLogMsgBufferMsgType':bnLogMsgBufferMsgType,'bnLogMsgRemoteSyslogEnabled':bnLogMsgRemoteSyslogEnabled,'bnLogMsgRemoteSyslogAddress':bnLogMsgRemoteSyslogAddress,'bnLogMsgRemoteSyslogSaveTargets':bnLogMsgRemoteSyslogSaveTargets,'bnLogMsgClearMessageBuffers':bnLogMsgClearMessageBuffers,'bnLogMsgRemoteSyslogInetAddressType':bnLogMsgRemoteSyslogInetAddressType,'bnLogMsgRemoteSyslogInetAddress':bnLogMsgRemoteSyslogInetAddress,'bnLogMsgRemoteSyslogSecondaryInetAddressType':bnLogMsgRemoteSyslogSecondaryInetAddressType,'bnLogMsgRemoteSyslogSecondaryInetAddress':bnLogMsgRemoteSyslogSecondaryInetAddress,'bnLogMsgRemoteServerTable':bnLogMsgRemoteServerTable,'bnLogMsgRemoteServerEntry':bnLogMsgRemoteServerEntry,_T:bnLogMsgRemoteServerAddressType,_U:bnLogMsgRemoteServerAddress,'bnLogMsgRemoteServerEnabled':bnLogMsgRemoteServerEnabled,'bnLogMsgRemoteServerSaveTargets':bnLogMsgRemoteServerSaveTargets,'bnLogMsgRemoteServerRowStatus':bnLogMsgRemoteServerRowStatus,'bnLogMsgRemoteServerStandardSaveTargets':bnLogMsgRemoteServerStandardSaveTargets,'bnLogMsgRemoteSyslogFacility':bnLogMsgRemoteSyslogFacility,'bnLogMsgRemoteSyslogStandardSaveTargets':bnLogMsgRemoteSyslogStandardSaveTargets,'bnLogMsgRemoteSyslogPrimaryTcpPort':bnLogMsgRemoteSyslogPrimaryTcpPort,'bnLogMsgRemoteSyslogSecondaryTcpPort':bnLogMsgRemoteSyslogSecondaryTcpPort,'bnLogMsgRemoteSyslogPrimaryConnectionType':bnLogMsgRemoteSyslogPrimaryConnectionType,'bnLogMsgRemoteSyslogSecondaryConnectionType':bnLogMsgRemoteSyslogSecondaryConnectionType,'bnLogMsgMIBTraps':bnLogMsgMIBTraps,'bnLogMsgMIBTrapPrefix':bnLogMsgMIBTrapPrefix,'bnLogMsgBufferFull':bnLogMsgBufferFull,'bnLogMsgMIBConformance':bnLogMsgMIBConformance})