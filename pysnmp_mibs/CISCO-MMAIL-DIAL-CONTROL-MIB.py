_AC='cmmFaxGroup'
_AB='cmmIpCallImageGroup'
_AA='cmmIpCallGeneralGroup'
_A9='cmmdcPeerCfgGroup'
_A8='cmmFaxCfgFaxProfile'
_A7='cmmFaxCfgCovergPageComment'
_A6='cmmFaxCfgCovergPageControl'
_A5='cmmFaxCfgLeftHeadingString'
_A4='cmmFaxCfgCenterHeadingString'
_A3='cmmFaxCfgRightHeadingString'
_A2='cmmFaxCfgXmitSubscriberId'
_A1='cmmFaxCfgCalledSubscriberId'
_A0='cmmIpCallHistoryImgResolution'
_z='cmmIpCallHistoryImgEncodingType'
_y='cmmIpCallActiveImgResolution'
_x='cmmIpCallActiveImgEncodingType'
_w='cmmIpCallHistoryNotification'
_v='cmmIpCallHistoryDiscdMimeTypes'
_u='cmmIpCallHistoryAcceptMimeTypes'
_t='cmmIpCallHistoryAccountId'
_s='cmmIpCallHistoryMessageId'
_r='cmmIpCallHistorySessionTarget'
_q='cmmIpCallHistorySessionProtocol'
_p='cmmIpCallHistoryRemoteIPAddress'
_o='cmmIpCallHistoryConnectionId'
_n='cmmIpCallActiveNotification'
_m='cmmIpCallActiveDiscdMimeTypes'
_l='cmmIpCallActiveAcceptMimeTypes'
_k='cmmIpCallActiveAccountId'
_j='cmmIpCallActiveMessageId'
_i='cmmIpCallActiveSessionTarget'
_h='cmmIpCallActiveSessionProtocol'
_g='cmmIpCallActiveRemoteIPAddress'
_f='cmmIpCallActiveConnectionId'
_e='cmmIpPeerCfgDeliStatNotification'
_d='cmmIpPeerCfgMsgDispoNotification'
_c='cmmIpPeerCfgImgResolution'
_b='cmmIpPeerCfgImgEncodingType'
_a='cmmIpPeerCfgSessionTarget'
_Z='cmmIpPeerCfgSessionProtocol'
_Y='dsnMdn'
_X='CmmImgResolutionOrTransparent'
_W='CmmImgEncodingOrTransparent'
_V='modifiedMR'
_U='modifiedREAD'
_T='modifiedHuffman'
_S='transparent'
_R='superFine'
_Q='standard'
_P='TruthValue'
_O='ifIndex'
_N='IF-MIB'
_M='callActiveSetupTime'
_L='callActiveIndex'
_K='cCallHistoryIndex'
_J='CISCO-DIAL-CONTROL-MIB'
_I='smtp'
_H='DIAL-CONTROL-MIB'
_G='DisplayString'
_F='Bits'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='CISCO-MMAIL-DIAL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_J,_K)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CvcGUid,=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB','CvcGUid')
AbsoluteCounter32,callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_H,'AbsoluteCounter32',_L,_M)
ifIndex,=mibBuilder.importSymbols(_N,_O)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_F,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention',_P)
ciscoMediaMailDialControlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,102))
if mibBuilder.loadTexts:ciscoMediaMailDialControlMIB.setRevisions(('2002-02-25 00:00',))
class CmmImgResolution(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_Q,2),('fine',3),(_R,4)))
class CmmImgResolutionOrTransparent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_Q,2),('fine',3),(_R,4)))
class CmmImgEncoding(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_T,2),(_U,3),(_V,4)))
class CmmImgEncodingOrTransparent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3),(_V,4)))
class CmmFaxHeadingString(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CmmdcMIBObjects_ObjectIdentity=ObjectIdentity
cmmdcMIBObjects=_CmmdcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,102,1))
_CmmPeer_ObjectIdentity=ObjectIdentity
cmmPeer=_CmmPeer_ObjectIdentity((1,3,6,1,4,1,9,9,102,1,1))
_CmmIpPeerCfgTable_Object=MibTable
cmmIpPeerCfgTable=_CmmIpPeerCfgTable_Object((1,3,6,1,4,1,9,9,102,1,1,1))
if mibBuilder.loadTexts:cmmIpPeerCfgTable.setStatus(_A)
_CmmIpPeerCfgEntry_Object=MibTableRow
cmmIpPeerCfgEntry=_CmmIpPeerCfgEntry_Object((1,3,6,1,4,1,9,9,102,1,1,1,1))
cmmIpPeerCfgEntry.setIndexNames((0,_N,_O))
if mibBuilder.loadTexts:cmmIpPeerCfgEntry.setStatus(_A)
class _CmmIpPeerCfgSessionProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_CmmIpPeerCfgSessionProtocol_Type.__name__=_E
_CmmIpPeerCfgSessionProtocol_Object=MibTableColumn
cmmIpPeerCfgSessionProtocol=_CmmIpPeerCfgSessionProtocol_Object((1,3,6,1,4,1,9,9,102,1,1,1,1,1),_CmmIpPeerCfgSessionProtocol_Type())
cmmIpPeerCfgSessionProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmIpPeerCfgSessionProtocol.setStatus(_A)
class _CmmIpPeerCfgSessionTarget_Type(DisplayString):defaultValue=OctetString('')
_CmmIpPeerCfgSessionTarget_Type.__name__=_G
_CmmIpPeerCfgSessionTarget_Object=MibTableColumn
cmmIpPeerCfgSessionTarget=_CmmIpPeerCfgSessionTarget_Object((1,3,6,1,4,1,9,9,102,1,1,1,1,2),_CmmIpPeerCfgSessionTarget_Type())
cmmIpPeerCfgSessionTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmIpPeerCfgSessionTarget.setStatus(_A)
class _CmmIpPeerCfgImgEncodingType_Type(CmmImgEncodingOrTransparent):defaultValue=1
_CmmIpPeerCfgImgEncodingType_Type.__name__=_W
_CmmIpPeerCfgImgEncodingType_Object=MibTableColumn
cmmIpPeerCfgImgEncodingType=_CmmIpPeerCfgImgEncodingType_Object((1,3,6,1,4,1,9,9,102,1,1,1,1,3),_CmmIpPeerCfgImgEncodingType_Type())
cmmIpPeerCfgImgEncodingType.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmIpPeerCfgImgEncodingType.setStatus(_A)
class _CmmIpPeerCfgImgResolution_Type(CmmImgResolutionOrTransparent):defaultValue=1
_CmmIpPeerCfgImgResolution_Type.__name__=_X
_CmmIpPeerCfgImgResolution_Object=MibTableColumn
cmmIpPeerCfgImgResolution=_CmmIpPeerCfgImgResolution_Object((1,3,6,1,4,1,9,9,102,1,1,1,1,4),_CmmIpPeerCfgImgResolution_Type())
cmmIpPeerCfgImgResolution.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmIpPeerCfgImgResolution.setStatus(_A)
class _CmmIpPeerCfgMsgDispoNotification_Type(TruthValue):defaultValue=2
_CmmIpPeerCfgMsgDispoNotification_Type.__name__=_P
_CmmIpPeerCfgMsgDispoNotification_Object=MibTableColumn
cmmIpPeerCfgMsgDispoNotification=_CmmIpPeerCfgMsgDispoNotification_Object((1,3,6,1,4,1,9,9,102,1,1,1,1,5),_CmmIpPeerCfgMsgDispoNotification_Type())
cmmIpPeerCfgMsgDispoNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmIpPeerCfgMsgDispoNotification.setStatus(_A)
class _CmmIpPeerCfgDeliStatNotification_Type(Bits):defaultBinValue='0';namedValues=NamedValues(*(('success',0),('failure',1),('delayed',2)))
_CmmIpPeerCfgDeliStatNotification_Type.__name__=_F
_CmmIpPeerCfgDeliStatNotification_Object=MibTableColumn
cmmIpPeerCfgDeliStatNotification=_CmmIpPeerCfgDeliStatNotification_Object((1,3,6,1,4,1,9,9,102,1,1,1,1,6),_CmmIpPeerCfgDeliStatNotification_Type())
cmmIpPeerCfgDeliStatNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmIpPeerCfgDeliStatNotification.setStatus(_A)
_CmmCallActive_ObjectIdentity=ObjectIdentity
cmmCallActive=_CmmCallActive_ObjectIdentity((1,3,6,1,4,1,9,9,102,1,2))
_CmmIpCallActiveTable_Object=MibTable
cmmIpCallActiveTable=_CmmIpCallActiveTable_Object((1,3,6,1,4,1,9,9,102,1,2,1))
if mibBuilder.loadTexts:cmmIpCallActiveTable.setStatus(_A)
_CmmIpCallActiveEntry_Object=MibTableRow
cmmIpCallActiveEntry=_CmmIpCallActiveEntry_Object((1,3,6,1,4,1,9,9,102,1,2,1,1))
cmmIpCallActiveEntry.setIndexNames((0,_H,_M),(0,_H,_L))
if mibBuilder.loadTexts:cmmIpCallActiveEntry.setStatus(_A)
_CmmIpCallActiveConnectionId_Type=CvcGUid
_CmmIpCallActiveConnectionId_Object=MibTableColumn
cmmIpCallActiveConnectionId=_CmmIpCallActiveConnectionId_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,1),_CmmIpCallActiveConnectionId_Type())
cmmIpCallActiveConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveConnectionId.setStatus(_A)
_CmmIpCallActiveRemoteIPAddress_Type=IpAddress
_CmmIpCallActiveRemoteIPAddress_Object=MibTableColumn
cmmIpCallActiveRemoteIPAddress=_CmmIpCallActiveRemoteIPAddress_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,2),_CmmIpCallActiveRemoteIPAddress_Type())
cmmIpCallActiveRemoteIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveRemoteIPAddress.setStatus(_A)
class _CmmIpCallActiveSessionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_CmmIpCallActiveSessionProtocol_Type.__name__=_E
_CmmIpCallActiveSessionProtocol_Object=MibTableColumn
cmmIpCallActiveSessionProtocol=_CmmIpCallActiveSessionProtocol_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,3),_CmmIpCallActiveSessionProtocol_Type())
cmmIpCallActiveSessionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveSessionProtocol.setStatus(_A)
_CmmIpCallActiveSessionTarget_Type=DisplayString
_CmmIpCallActiveSessionTarget_Object=MibTableColumn
cmmIpCallActiveSessionTarget=_CmmIpCallActiveSessionTarget_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,4),_CmmIpCallActiveSessionTarget_Type())
cmmIpCallActiveSessionTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveSessionTarget.setStatus(_A)
_CmmIpCallActiveMessageId_Type=DisplayString
_CmmIpCallActiveMessageId_Object=MibTableColumn
cmmIpCallActiveMessageId=_CmmIpCallActiveMessageId_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,5),_CmmIpCallActiveMessageId_Type())
cmmIpCallActiveMessageId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveMessageId.setStatus(_A)
_CmmIpCallActiveAccountId_Type=DisplayString
_CmmIpCallActiveAccountId_Object=MibTableColumn
cmmIpCallActiveAccountId=_CmmIpCallActiveAccountId_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,6),_CmmIpCallActiveAccountId_Type())
cmmIpCallActiveAccountId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveAccountId.setStatus(_A)
_CmmIpCallActiveImgEncodingType_Type=CmmImgEncoding
_CmmIpCallActiveImgEncodingType_Object=MibTableColumn
cmmIpCallActiveImgEncodingType=_CmmIpCallActiveImgEncodingType_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,7),_CmmIpCallActiveImgEncodingType_Type())
cmmIpCallActiveImgEncodingType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveImgEncodingType.setStatus(_A)
_CmmIpCallActiveImgResolution_Type=CmmImgResolution
_CmmIpCallActiveImgResolution_Object=MibTableColumn
cmmIpCallActiveImgResolution=_CmmIpCallActiveImgResolution_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,8),_CmmIpCallActiveImgResolution_Type())
cmmIpCallActiveImgResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveImgResolution.setStatus(_A)
_CmmIpCallActiveAcceptMimeTypes_Type=AbsoluteCounter32
_CmmIpCallActiveAcceptMimeTypes_Object=MibTableColumn
cmmIpCallActiveAcceptMimeTypes=_CmmIpCallActiveAcceptMimeTypes_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,9),_CmmIpCallActiveAcceptMimeTypes_Type())
cmmIpCallActiveAcceptMimeTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveAcceptMimeTypes.setStatus(_A)
_CmmIpCallActiveDiscdMimeTypes_Type=AbsoluteCounter32
_CmmIpCallActiveDiscdMimeTypes_Object=MibTableColumn
cmmIpCallActiveDiscdMimeTypes=_CmmIpCallActiveDiscdMimeTypes_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,10),_CmmIpCallActiveDiscdMimeTypes_Type())
cmmIpCallActiveDiscdMimeTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveDiscdMimeTypes.setStatus(_A)
class _CmmIpCallActiveNotification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('mdn',2),('dsn',3),(_Y,4)))
_CmmIpCallActiveNotification_Type.__name__=_E
_CmmIpCallActiveNotification_Object=MibTableColumn
cmmIpCallActiveNotification=_CmmIpCallActiveNotification_Object((1,3,6,1,4,1,9,9,102,1,2,1,1,11),_CmmIpCallActiveNotification_Type())
cmmIpCallActiveNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallActiveNotification.setStatus(_A)
_CmmCallHistory_ObjectIdentity=ObjectIdentity
cmmCallHistory=_CmmCallHistory_ObjectIdentity((1,3,6,1,4,1,9,9,102,1,3))
_CmmIpCallHistoryTable_Object=MibTable
cmmIpCallHistoryTable=_CmmIpCallHistoryTable_Object((1,3,6,1,4,1,9,9,102,1,3,1))
if mibBuilder.loadTexts:cmmIpCallHistoryTable.setStatus(_A)
_CmmIpCallHistoryEntry_Object=MibTableRow
cmmIpCallHistoryEntry=_CmmIpCallHistoryEntry_Object((1,3,6,1,4,1,9,9,102,1,3,1,1))
cmmIpCallHistoryEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:cmmIpCallHistoryEntry.setStatus(_A)
_CmmIpCallHistoryConnectionId_Type=CvcGUid
_CmmIpCallHistoryConnectionId_Object=MibTableColumn
cmmIpCallHistoryConnectionId=_CmmIpCallHistoryConnectionId_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,1),_CmmIpCallHistoryConnectionId_Type())
cmmIpCallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryConnectionId.setStatus(_A)
_CmmIpCallHistoryRemoteIPAddress_Type=IpAddress
_CmmIpCallHistoryRemoteIPAddress_Object=MibTableColumn
cmmIpCallHistoryRemoteIPAddress=_CmmIpCallHistoryRemoteIPAddress_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,2),_CmmIpCallHistoryRemoteIPAddress_Type())
cmmIpCallHistoryRemoteIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryRemoteIPAddress.setStatus(_A)
class _CmmIpCallHistorySessionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_I,1))
_CmmIpCallHistorySessionProtocol_Type.__name__=_E
_CmmIpCallHistorySessionProtocol_Object=MibTableColumn
cmmIpCallHistorySessionProtocol=_CmmIpCallHistorySessionProtocol_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,3),_CmmIpCallHistorySessionProtocol_Type())
cmmIpCallHistorySessionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistorySessionProtocol.setStatus(_A)
_CmmIpCallHistorySessionTarget_Type=DisplayString
_CmmIpCallHistorySessionTarget_Object=MibTableColumn
cmmIpCallHistorySessionTarget=_CmmIpCallHistorySessionTarget_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,4),_CmmIpCallHistorySessionTarget_Type())
cmmIpCallHistorySessionTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistorySessionTarget.setStatus(_A)
_CmmIpCallHistoryMessageId_Type=DisplayString
_CmmIpCallHistoryMessageId_Object=MibTableColumn
cmmIpCallHistoryMessageId=_CmmIpCallHistoryMessageId_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,5),_CmmIpCallHistoryMessageId_Type())
cmmIpCallHistoryMessageId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryMessageId.setStatus(_A)
_CmmIpCallHistoryAccountId_Type=DisplayString
_CmmIpCallHistoryAccountId_Object=MibTableColumn
cmmIpCallHistoryAccountId=_CmmIpCallHistoryAccountId_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,6),_CmmIpCallHistoryAccountId_Type())
cmmIpCallHistoryAccountId.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryAccountId.setStatus(_A)
_CmmIpCallHistoryImgEncodingType_Type=CmmImgEncoding
_CmmIpCallHistoryImgEncodingType_Object=MibTableColumn
cmmIpCallHistoryImgEncodingType=_CmmIpCallHistoryImgEncodingType_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,7),_CmmIpCallHistoryImgEncodingType_Type())
cmmIpCallHistoryImgEncodingType.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryImgEncodingType.setStatus(_A)
_CmmIpCallHistoryImgResolution_Type=CmmImgResolution
_CmmIpCallHistoryImgResolution_Object=MibTableColumn
cmmIpCallHistoryImgResolution=_CmmIpCallHistoryImgResolution_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,8),_CmmIpCallHistoryImgResolution_Type())
cmmIpCallHistoryImgResolution.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryImgResolution.setStatus(_A)
_CmmIpCallHistoryAcceptMimeTypes_Type=AbsoluteCounter32
_CmmIpCallHistoryAcceptMimeTypes_Object=MibTableColumn
cmmIpCallHistoryAcceptMimeTypes=_CmmIpCallHistoryAcceptMimeTypes_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,9),_CmmIpCallHistoryAcceptMimeTypes_Type())
cmmIpCallHistoryAcceptMimeTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryAcceptMimeTypes.setStatus(_A)
_CmmIpCallHistoryDiscdMimeTypes_Type=AbsoluteCounter32
_CmmIpCallHistoryDiscdMimeTypes_Object=MibTableColumn
cmmIpCallHistoryDiscdMimeTypes=_CmmIpCallHistoryDiscdMimeTypes_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,10),_CmmIpCallHistoryDiscdMimeTypes_Type())
cmmIpCallHistoryDiscdMimeTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryDiscdMimeTypes.setStatus(_A)
class _CmmIpCallHistoryNotification_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('mdn',2),('dsn',3),(_Y,4)))
_CmmIpCallHistoryNotification_Type.__name__=_E
_CmmIpCallHistoryNotification_Object=MibTableColumn
cmmIpCallHistoryNotification=_CmmIpCallHistoryNotification_Object((1,3,6,1,4,1,9,9,102,1,3,1,1,11),_CmmIpCallHistoryNotification_Type())
cmmIpCallHistoryNotification.setMaxAccess(_C)
if mibBuilder.loadTexts:cmmIpCallHistoryNotification.setStatus(_A)
_CmmFaxGeneralCfg_ObjectIdentity=ObjectIdentity
cmmFaxGeneralCfg=_CmmFaxGeneralCfg_ObjectIdentity((1,3,6,1,4,1,9,9,102,1,4))
class _CmmFaxCfgCalledSubscriberId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CmmFaxCfgCalledSubscriberId_Type.__name__=_G
_CmmFaxCfgCalledSubscriberId_Object=MibScalar
cmmFaxCfgCalledSubscriberId=_CmmFaxCfgCalledSubscriberId_Object((1,3,6,1,4,1,9,9,102,1,4,1),_CmmFaxCfgCalledSubscriberId_Type())
cmmFaxCfgCalledSubscriberId.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgCalledSubscriberId.setStatus(_A)
class _CmmFaxCfgXmitSubscriberId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CmmFaxCfgXmitSubscriberId_Type.__name__=_G
_CmmFaxCfgXmitSubscriberId_Object=MibScalar
cmmFaxCfgXmitSubscriberId=_CmmFaxCfgXmitSubscriberId_Object((1,3,6,1,4,1,9,9,102,1,4,2),_CmmFaxCfgXmitSubscriberId_Type())
cmmFaxCfgXmitSubscriberId.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgXmitSubscriberId.setStatus(_A)
_CmmFaxCfgRightHeadingString_Type=CmmFaxHeadingString
_CmmFaxCfgRightHeadingString_Object=MibScalar
cmmFaxCfgRightHeadingString=_CmmFaxCfgRightHeadingString_Object((1,3,6,1,4,1,9,9,102,1,4,3),_CmmFaxCfgRightHeadingString_Type())
cmmFaxCfgRightHeadingString.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgRightHeadingString.setStatus(_A)
_CmmFaxCfgCenterHeadingString_Type=CmmFaxHeadingString
_CmmFaxCfgCenterHeadingString_Object=MibScalar
cmmFaxCfgCenterHeadingString=_CmmFaxCfgCenterHeadingString_Object((1,3,6,1,4,1,9,9,102,1,4,4),_CmmFaxCfgCenterHeadingString_Type())
cmmFaxCfgCenterHeadingString.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgCenterHeadingString.setStatus(_A)
_CmmFaxCfgLeftHeadingString_Type=CmmFaxHeadingString
_CmmFaxCfgLeftHeadingString_Object=MibScalar
cmmFaxCfgLeftHeadingString=_CmmFaxCfgLeftHeadingString_Object((1,3,6,1,4,1,9,9,102,1,4,5),_CmmFaxCfgLeftHeadingString_Type())
cmmFaxCfgLeftHeadingString.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgLeftHeadingString.setStatus(_A)
class _CmmFaxCfgCovergPageControl_Type(Bits):namedValues=NamedValues(*(('coverPageEnable',0),('coverPageCtlByEmail',1),('coverPageDetailEnable',2)))
_CmmFaxCfgCovergPageControl_Type.__name__=_F
_CmmFaxCfgCovergPageControl_Object=MibScalar
cmmFaxCfgCovergPageControl=_CmmFaxCfgCovergPageControl_Object((1,3,6,1,4,1,9,9,102,1,4,6),_CmmFaxCfgCovergPageControl_Type())
cmmFaxCfgCovergPageControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgCovergPageControl.setStatus(_A)
_CmmFaxCfgCovergPageComment_Type=DisplayString
_CmmFaxCfgCovergPageComment_Object=MibScalar
cmmFaxCfgCovergPageComment=_CmmFaxCfgCovergPageComment_Object((1,3,6,1,4,1,9,9,102,1,4,7),_CmmFaxCfgCovergPageComment_Type())
cmmFaxCfgCovergPageComment.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgCovergPageComment.setStatus(_A)
class _CmmFaxCfgFaxProfile_Type(Bits):namedValues=NamedValues(*(('profileS',0),('profileF',1),('profileJ',2),('profileC',3),('profileL',4),('profileM',5)))
_CmmFaxCfgFaxProfile_Type.__name__=_F
_CmmFaxCfgFaxProfile_Object=MibScalar
cmmFaxCfgFaxProfile=_CmmFaxCfgFaxProfile_Object((1,3,6,1,4,1,9,9,102,1,4,8),_CmmFaxCfgFaxProfile_Type())
cmmFaxCfgFaxProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:cmmFaxCfgFaxProfile.setStatus(_A)
_CmmdcMIBConformance_ObjectIdentity=ObjectIdentity
cmmdcMIBConformance=_CmmdcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,102,3))
_CmmdcMIBCompliances_ObjectIdentity=ObjectIdentity
cmmdcMIBCompliances=_CmmdcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,102,3,1))
_CmmdcMIBGroups_ObjectIdentity=ObjectIdentity
cmmdcMIBGroups=_CmmdcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,102,3,2))
cmmdcPeerCfgGroup=ObjectGroup((1,3,6,1,4,1,9,9,102,3,2,1))
cmmdcPeerCfgGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cmmdcPeerCfgGroup.setStatus(_A)
cmmIpCallGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,102,3,2,2))
cmmIpCallGeneralGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:cmmIpCallGeneralGroup.setStatus(_A)
cmmIpCallImageGroup=ObjectGroup((1,3,6,1,4,1,9,9,102,3,2,3))
cmmIpCallImageGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:cmmIpCallImageGroup.setStatus(_A)
cmmFaxGroup=ObjectGroup((1,3,6,1,4,1,9,9,102,3,2,4))
cmmFaxGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:cmmFaxGroup.setStatus(_A)
cmmdcMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,102,3,1,1))
cmmdcMIBCompliance.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:cmmdcMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CmmImgResolution':CmmImgResolution,_X:CmmImgResolutionOrTransparent,'CmmImgEncoding':CmmImgEncoding,_W:CmmImgEncodingOrTransparent,'CmmFaxHeadingString':CmmFaxHeadingString,'ciscoMediaMailDialControlMIB':ciscoMediaMailDialControlMIB,'cmmdcMIBObjects':cmmdcMIBObjects,'cmmPeer':cmmPeer,'cmmIpPeerCfgTable':cmmIpPeerCfgTable,'cmmIpPeerCfgEntry':cmmIpPeerCfgEntry,_Z:cmmIpPeerCfgSessionProtocol,_a:cmmIpPeerCfgSessionTarget,_b:cmmIpPeerCfgImgEncodingType,_c:cmmIpPeerCfgImgResolution,_d:cmmIpPeerCfgMsgDispoNotification,_e:cmmIpPeerCfgDeliStatNotification,'cmmCallActive':cmmCallActive,'cmmIpCallActiveTable':cmmIpCallActiveTable,'cmmIpCallActiveEntry':cmmIpCallActiveEntry,_f:cmmIpCallActiveConnectionId,_g:cmmIpCallActiveRemoteIPAddress,_h:cmmIpCallActiveSessionProtocol,_i:cmmIpCallActiveSessionTarget,_j:cmmIpCallActiveMessageId,_k:cmmIpCallActiveAccountId,_x:cmmIpCallActiveImgEncodingType,_y:cmmIpCallActiveImgResolution,_l:cmmIpCallActiveAcceptMimeTypes,_m:cmmIpCallActiveDiscdMimeTypes,_n:cmmIpCallActiveNotification,'cmmCallHistory':cmmCallHistory,'cmmIpCallHistoryTable':cmmIpCallHistoryTable,'cmmIpCallHistoryEntry':cmmIpCallHistoryEntry,_o:cmmIpCallHistoryConnectionId,_p:cmmIpCallHistoryRemoteIPAddress,_q:cmmIpCallHistorySessionProtocol,_r:cmmIpCallHistorySessionTarget,_s:cmmIpCallHistoryMessageId,_t:cmmIpCallHistoryAccountId,_z:cmmIpCallHistoryImgEncodingType,_A0:cmmIpCallHistoryImgResolution,_u:cmmIpCallHistoryAcceptMimeTypes,_v:cmmIpCallHistoryDiscdMimeTypes,_w:cmmIpCallHistoryNotification,'cmmFaxGeneralCfg':cmmFaxGeneralCfg,_A1:cmmFaxCfgCalledSubscriberId,_A2:cmmFaxCfgXmitSubscriberId,_A3:cmmFaxCfgRightHeadingString,_A4:cmmFaxCfgCenterHeadingString,_A5:cmmFaxCfgLeftHeadingString,_A6:cmmFaxCfgCovergPageControl,_A7:cmmFaxCfgCovergPageComment,_A8:cmmFaxCfgFaxProfile,'cmmdcMIBConformance':cmmdcMIBConformance,'cmmdcMIBCompliances':cmmdcMIBCompliances,'cmmdcMIBCompliance':cmmdcMIBCompliance,'cmmdcMIBGroups':cmmdcMIBGroups,_A9:cmmdcPeerCfgGroup,_AA:cmmIpCallGeneralGroup,_AB:cmmIpCallImageGroup,_AC:cmmFaxGroup})