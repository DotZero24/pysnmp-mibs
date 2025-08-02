_A1='cvAtmPeerCfgGroup'
_A0='cvAtmCallActiveGroup'
_z='cvAtmCallHistoryGroup'
_y='cvAtmPeerCfgDtmfRelay'
_x='cvAtmPeerCfgUseSeqNumbers'
_w='cvAtmPeerCfgVADEnable'
_v='cvAtmPeerCfgInBandSignaling'
_u='cvAtmPeerCfgFaxBytes'
_t='cvAtmPeerCfgFaxRate'
_s='cvAtmPeerCfgCodecBytes'
_r='cvAtmPeerCfgCoderRate'
_q='cvAtmPeerCfgVcName'
_p='cvAtmPeerCfgVci'
_o='cvAtmPeerCfgVpi'
_n='cvAtmPeerCfgInterfaceName'
_m='cvAtmPeerCfgSessionProtocol'
_l='cvAtmCallActiveUseSeqNumbers'
_k='cvAtmCallActiveDtmfRelay'
_j='cvAtmCallActiveCalledNumber'
_i='cvAtmCallActiveSessionProtocol'
_h='cvAtmCallActiveSubchannelID'
_g='cvAtmCallActiveSessionTarget'
_f='cvAtmCallActiveLowerIfName'
_e='cvAtmCallActiveVci'
_d='cvAtmCallActiveVpi'
_c='cvAtmCallActiveConnectionId'
_b='cvAtmCallHistoryUseSeqNumbers'
_a='cvAtmCallHistoryDtmfRelay'
_Z='cvAtmCallHistoryCalledNumber'
_Y='cvAtmCallHistorySessionProtocol'
_X='cvAtmCallHistorySubchannelID'
_W='cvAtmCallHistorySessionTarget'
_V='cvAtmCallHistoryLowerIfName'
_U='cvAtmCallHistoryVci'
_T='cvAtmCallHistoryVpi'
_S='cvAtmCallHistoryConnectionId'
_R='CvAtmSessionProtocol'
_Q='ifIndex'
_P='IF-MIB'
_O='callActiveSetupTime'
_N='callActiveIndex'
_M='CvcSpeechCoderRate'
_L='CvcInBandSignaling'
_K='CvcFaxTransmitRate'
_J='cCallHistoryIndex'
_I='CISCO-DIAL-CONTROL-MIB'
_H='DisplayString'
_G='DIAL-CONTROL-MIB'
_F='TruthValue'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='CISCO-VOICE-ATM-DIAL-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cCallHistoryIndex,=mibBuilder.importSymbols(_I,_J)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
CvcFaxTransmitRate,CvcGUid,CvcInBandSignaling,CvcSpeechCoderRate=mibBuilder.importSymbols('CISCO-VOICE-COMMON-DIAL-CONTROL-MIB',_K,'CvcGUid',_L,_M)
callActiveIndex,callActiveSetupTime=mibBuilder.importSymbols(_G,_N,_O)
ifIndex,=mibBuilder.importSymbols(_P,_Q)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention',_F)
ciscoVoiceAtmDialControlMIB=ModuleIdentity((1,3,6,1,4,1,9,10,35))
if mibBuilder.loadTexts:ciscoVoiceAtmDialControlMIB.setRevisions(('2002-11-17 00:00','1999-03-20 00:00'))
class CvAtmSessionProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('ciscoSwitched',2),('aal2Trunk',3)))
_CiscoVoiceAtmDialControlMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVoiceAtmDialControlMIBObjects=_CiscoVoiceAtmDialControlMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,35,1))
_CvAtmCallHistory_ObjectIdentity=ObjectIdentity
cvAtmCallHistory=_CvAtmCallHistory_ObjectIdentity((1,3,6,1,4,1,9,10,35,1,1))
_CvAtmCallHistoryTable_Object=MibTable
cvAtmCallHistoryTable=_CvAtmCallHistoryTable_Object((1,3,6,1,4,1,9,10,35,1,1,1))
if mibBuilder.loadTexts:cvAtmCallHistoryTable.setStatus(_A)
_CvAtmCallHistoryEntry_Object=MibTableRow
cvAtmCallHistoryEntry=_CvAtmCallHistoryEntry_Object((1,3,6,1,4,1,9,10,35,1,1,1,1))
cvAtmCallHistoryEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:cvAtmCallHistoryEntry.setStatus(_A)
_CvAtmCallHistoryConnectionId_Type=CvcGUid
_CvAtmCallHistoryConnectionId_Object=MibTableColumn
cvAtmCallHistoryConnectionId=_CvAtmCallHistoryConnectionId_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,1),_CvAtmCallHistoryConnectionId_Type())
cvAtmCallHistoryConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistoryConnectionId.setStatus(_A)
class _CvAtmCallHistoryVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CvAtmCallHistoryVpi_Type.__name__=_E
_CvAtmCallHistoryVpi_Object=MibTableColumn
cvAtmCallHistoryVpi=_CvAtmCallHistoryVpi_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,2),_CvAtmCallHistoryVpi_Type())
cvAtmCallHistoryVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistoryVpi.setStatus(_A)
class _CvAtmCallHistoryVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CvAtmCallHistoryVci_Type.__name__=_E
_CvAtmCallHistoryVci_Object=MibTableColumn
cvAtmCallHistoryVci=_CvAtmCallHistoryVci_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,3),_CvAtmCallHistoryVci_Type())
cvAtmCallHistoryVci.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistoryVci.setStatus(_A)
_CvAtmCallHistoryLowerIfName_Type=DisplayString
_CvAtmCallHistoryLowerIfName_Object=MibTableColumn
cvAtmCallHistoryLowerIfName=_CvAtmCallHistoryLowerIfName_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,4),_CvAtmCallHistoryLowerIfName_Type())
cvAtmCallHistoryLowerIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistoryLowerIfName.setStatus(_A)
_CvAtmCallHistorySessionTarget_Type=DisplayString
_CvAtmCallHistorySessionTarget_Object=MibTableColumn
cvAtmCallHistorySessionTarget=_CvAtmCallHistorySessionTarget_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,5),_CvAtmCallHistorySessionTarget_Type())
cvAtmCallHistorySessionTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistorySessionTarget.setStatus(_A)
class _CvAtmCallHistorySubchannelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CvAtmCallHistorySubchannelID_Type.__name__=_E
_CvAtmCallHistorySubchannelID_Object=MibTableColumn
cvAtmCallHistorySubchannelID=_CvAtmCallHistorySubchannelID_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,6),_CvAtmCallHistorySubchannelID_Type())
cvAtmCallHistorySubchannelID.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistorySubchannelID.setStatus(_A)
_CvAtmCallHistorySessionProtocol_Type=CvAtmSessionProtocol
_CvAtmCallHistorySessionProtocol_Object=MibTableColumn
cvAtmCallHistorySessionProtocol=_CvAtmCallHistorySessionProtocol_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,7),_CvAtmCallHistorySessionProtocol_Type())
cvAtmCallHistorySessionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistorySessionProtocol.setStatus(_A)
_CvAtmCallHistoryCalledNumber_Type=DisplayString
_CvAtmCallHistoryCalledNumber_Object=MibTableColumn
cvAtmCallHistoryCalledNumber=_CvAtmCallHistoryCalledNumber_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,8),_CvAtmCallHistoryCalledNumber_Type())
cvAtmCallHistoryCalledNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistoryCalledNumber.setStatus(_A)
_CvAtmCallHistoryDtmfRelay_Type=TruthValue
_CvAtmCallHistoryDtmfRelay_Object=MibTableColumn
cvAtmCallHistoryDtmfRelay=_CvAtmCallHistoryDtmfRelay_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,9),_CvAtmCallHistoryDtmfRelay_Type())
cvAtmCallHistoryDtmfRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistoryDtmfRelay.setStatus(_A)
_CvAtmCallHistoryUseSeqNumbers_Type=TruthValue
_CvAtmCallHistoryUseSeqNumbers_Object=MibTableColumn
cvAtmCallHistoryUseSeqNumbers=_CvAtmCallHistoryUseSeqNumbers_Object((1,3,6,1,4,1,9,10,35,1,1,1,1,10),_CvAtmCallHistoryUseSeqNumbers_Type())
cvAtmCallHistoryUseSeqNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallHistoryUseSeqNumbers.setStatus(_A)
_CvAtmCallActive_ObjectIdentity=ObjectIdentity
cvAtmCallActive=_CvAtmCallActive_ObjectIdentity((1,3,6,1,4,1,9,10,35,1,2))
_CvAtmCallActiveTable_Object=MibTable
cvAtmCallActiveTable=_CvAtmCallActiveTable_Object((1,3,6,1,4,1,9,10,35,1,2,1))
if mibBuilder.loadTexts:cvAtmCallActiveTable.setStatus(_A)
_CvAtmCallActiveEntry_Object=MibTableRow
cvAtmCallActiveEntry=_CvAtmCallActiveEntry_Object((1,3,6,1,4,1,9,10,35,1,2,1,1))
cvAtmCallActiveEntry.setIndexNames((0,_G,_O),(0,_G,_N))
if mibBuilder.loadTexts:cvAtmCallActiveEntry.setStatus(_A)
_CvAtmCallActiveConnectionId_Type=CvcGUid
_CvAtmCallActiveConnectionId_Object=MibTableColumn
cvAtmCallActiveConnectionId=_CvAtmCallActiveConnectionId_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,1),_CvAtmCallActiveConnectionId_Type())
cvAtmCallActiveConnectionId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveConnectionId.setStatus(_A)
class _CvAtmCallActiveVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CvAtmCallActiveVpi_Type.__name__=_E
_CvAtmCallActiveVpi_Object=MibTableColumn
cvAtmCallActiveVpi=_CvAtmCallActiveVpi_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,2),_CvAtmCallActiveVpi_Type())
cvAtmCallActiveVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveVpi.setStatus(_A)
class _CvAtmCallActiveVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CvAtmCallActiveVci_Type.__name__=_E
_CvAtmCallActiveVci_Object=MibTableColumn
cvAtmCallActiveVci=_CvAtmCallActiveVci_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,3),_CvAtmCallActiveVci_Type())
cvAtmCallActiveVci.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveVci.setStatus(_A)
_CvAtmCallActiveLowerIfName_Type=DisplayString
_CvAtmCallActiveLowerIfName_Object=MibTableColumn
cvAtmCallActiveLowerIfName=_CvAtmCallActiveLowerIfName_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,4),_CvAtmCallActiveLowerIfName_Type())
cvAtmCallActiveLowerIfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveLowerIfName.setStatus(_A)
_CvAtmCallActiveSessionTarget_Type=DisplayString
_CvAtmCallActiveSessionTarget_Object=MibTableColumn
cvAtmCallActiveSessionTarget=_CvAtmCallActiveSessionTarget_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,5),_CvAtmCallActiveSessionTarget_Type())
cvAtmCallActiveSessionTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveSessionTarget.setStatus(_A)
class _CvAtmCallActiveSubchannelID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CvAtmCallActiveSubchannelID_Type.__name__=_E
_CvAtmCallActiveSubchannelID_Object=MibTableColumn
cvAtmCallActiveSubchannelID=_CvAtmCallActiveSubchannelID_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,6),_CvAtmCallActiveSubchannelID_Type())
cvAtmCallActiveSubchannelID.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveSubchannelID.setStatus(_A)
_CvAtmCallActiveSessionProtocol_Type=CvAtmSessionProtocol
_CvAtmCallActiveSessionProtocol_Object=MibTableColumn
cvAtmCallActiveSessionProtocol=_CvAtmCallActiveSessionProtocol_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,7),_CvAtmCallActiveSessionProtocol_Type())
cvAtmCallActiveSessionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveSessionProtocol.setStatus(_A)
_CvAtmCallActiveCalledNumber_Type=DisplayString
_CvAtmCallActiveCalledNumber_Object=MibTableColumn
cvAtmCallActiveCalledNumber=_CvAtmCallActiveCalledNumber_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,8),_CvAtmCallActiveCalledNumber_Type())
cvAtmCallActiveCalledNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveCalledNumber.setStatus(_A)
_CvAtmCallActiveDtmfRelay_Type=TruthValue
_CvAtmCallActiveDtmfRelay_Object=MibTableColumn
cvAtmCallActiveDtmfRelay=_CvAtmCallActiveDtmfRelay_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,9),_CvAtmCallActiveDtmfRelay_Type())
cvAtmCallActiveDtmfRelay.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveDtmfRelay.setStatus(_A)
_CvAtmCallActiveUseSeqNumbers_Type=TruthValue
_CvAtmCallActiveUseSeqNumbers_Object=MibTableColumn
cvAtmCallActiveUseSeqNumbers=_CvAtmCallActiveUseSeqNumbers_Object((1,3,6,1,4,1,9,10,35,1,2,1,1,10),_CvAtmCallActiveUseSeqNumbers_Type())
cvAtmCallActiveUseSeqNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:cvAtmCallActiveUseSeqNumbers.setStatus(_A)
_CvAtmDialPeer_ObjectIdentity=ObjectIdentity
cvAtmDialPeer=_CvAtmDialPeer_ObjectIdentity((1,3,6,1,4,1,9,10,35,1,3))
_CvAtmPeerCfgTable_Object=MibTable
cvAtmPeerCfgTable=_CvAtmPeerCfgTable_Object((1,3,6,1,4,1,9,10,35,1,3,1))
if mibBuilder.loadTexts:cvAtmPeerCfgTable.setStatus(_A)
_CvAtmPeerCfgEntry_Object=MibTableRow
cvAtmPeerCfgEntry=_CvAtmPeerCfgEntry_Object((1,3,6,1,4,1,9,10,35,1,3,1,1))
cvAtmPeerCfgEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:cvAtmPeerCfgEntry.setStatus(_A)
class _CvAtmPeerCfgSessionProtocol_Type(CvAtmSessionProtocol):defaultValue=2
_CvAtmPeerCfgSessionProtocol_Type.__name__=_R
_CvAtmPeerCfgSessionProtocol_Object=MibTableColumn
cvAtmPeerCfgSessionProtocol=_CvAtmPeerCfgSessionProtocol_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,1),_CvAtmPeerCfgSessionProtocol_Type())
cvAtmPeerCfgSessionProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgSessionProtocol.setStatus(_A)
class _CvAtmPeerCfgInterfaceName_Type(DisplayString):defaultValue=OctetString('')
_CvAtmPeerCfgInterfaceName_Type.__name__=_H
_CvAtmPeerCfgInterfaceName_Object=MibTableColumn
cvAtmPeerCfgInterfaceName=_CvAtmPeerCfgInterfaceName_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,2),_CvAtmPeerCfgInterfaceName_Type())
cvAtmPeerCfgInterfaceName.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgInterfaceName.setStatus(_A)
class _CvAtmPeerCfgVpi_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CvAtmPeerCfgVpi_Type.__name__=_E
_CvAtmPeerCfgVpi_Object=MibTableColumn
cvAtmPeerCfgVpi=_CvAtmPeerCfgVpi_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,3),_CvAtmPeerCfgVpi_Type())
cvAtmPeerCfgVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgVpi.setStatus(_A)
class _CvAtmPeerCfgVci_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CvAtmPeerCfgVci_Type.__name__=_E
_CvAtmPeerCfgVci_Object=MibTableColumn
cvAtmPeerCfgVci=_CvAtmPeerCfgVci_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,4),_CvAtmPeerCfgVci_Type())
cvAtmPeerCfgVci.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgVci.setStatus(_A)
class _CvAtmPeerCfgVcName_Type(DisplayString):defaultValue=OctetString('')
_CvAtmPeerCfgVcName_Type.__name__=_H
_CvAtmPeerCfgVcName_Object=MibTableColumn
cvAtmPeerCfgVcName=_CvAtmPeerCfgVcName_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,5),_CvAtmPeerCfgVcName_Type())
cvAtmPeerCfgVcName.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgVcName.setStatus(_A)
class _CvAtmPeerCfgCoderRate_Type(CvcSpeechCoderRate):defaultValue=2
_CvAtmPeerCfgCoderRate_Type.__name__=_M
_CvAtmPeerCfgCoderRate_Object=MibTableColumn
cvAtmPeerCfgCoderRate=_CvAtmPeerCfgCoderRate_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,6),_CvAtmPeerCfgCoderRate_Type())
cvAtmPeerCfgCoderRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgCoderRate.setStatus(_A)
class _CvAtmPeerCfgCodecBytes_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_CvAtmPeerCfgCodecBytes_Type.__name__=_E
_CvAtmPeerCfgCodecBytes_Object=MibTableColumn
cvAtmPeerCfgCodecBytes=_CvAtmPeerCfgCodecBytes_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,7),_CvAtmPeerCfgCodecBytes_Type())
cvAtmPeerCfgCodecBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgCodecBytes.setStatus(_A)
class _CvAtmPeerCfgFaxRate_Type(CvcFaxTransmitRate):defaultValue=2
_CvAtmPeerCfgFaxRate_Type.__name__=_K
_CvAtmPeerCfgFaxRate_Object=MibTableColumn
cvAtmPeerCfgFaxRate=_CvAtmPeerCfgFaxRate_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,8),_CvAtmPeerCfgFaxRate_Type())
cvAtmPeerCfgFaxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgFaxRate.setStatus(_A)
class _CvAtmPeerCfgFaxBytes_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_CvAtmPeerCfgFaxBytes_Type.__name__=_E
_CvAtmPeerCfgFaxBytes_Object=MibTableColumn
cvAtmPeerCfgFaxBytes=_CvAtmPeerCfgFaxBytes_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,9),_CvAtmPeerCfgFaxBytes_Type())
cvAtmPeerCfgFaxBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgFaxBytes.setStatus(_A)
class _CvAtmPeerCfgInBandSignaling_Type(CvcInBandSignaling):defaultValue=1
_CvAtmPeerCfgInBandSignaling_Type.__name__=_L
_CvAtmPeerCfgInBandSignaling_Object=MibTableColumn
cvAtmPeerCfgInBandSignaling=_CvAtmPeerCfgInBandSignaling_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,10),_CvAtmPeerCfgInBandSignaling_Type())
cvAtmPeerCfgInBandSignaling.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgInBandSignaling.setStatus(_A)
class _CvAtmPeerCfgVADEnable_Type(TruthValue):defaultValue=1
_CvAtmPeerCfgVADEnable_Type.__name__=_F
_CvAtmPeerCfgVADEnable_Object=MibTableColumn
cvAtmPeerCfgVADEnable=_CvAtmPeerCfgVADEnable_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,11),_CvAtmPeerCfgVADEnable_Type())
cvAtmPeerCfgVADEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgVADEnable.setStatus(_A)
class _CvAtmPeerCfgUseSeqNumbers_Type(TruthValue):defaultValue=2
_CvAtmPeerCfgUseSeqNumbers_Type.__name__=_F
_CvAtmPeerCfgUseSeqNumbers_Object=MibTableColumn
cvAtmPeerCfgUseSeqNumbers=_CvAtmPeerCfgUseSeqNumbers_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,12),_CvAtmPeerCfgUseSeqNumbers_Type())
cvAtmPeerCfgUseSeqNumbers.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgUseSeqNumbers.setStatus(_A)
class _CvAtmPeerCfgDtmfRelay_Type(TruthValue):defaultValue=2
_CvAtmPeerCfgDtmfRelay_Type.__name__=_F
_CvAtmPeerCfgDtmfRelay_Object=MibTableColumn
cvAtmPeerCfgDtmfRelay=_CvAtmPeerCfgDtmfRelay_Object((1,3,6,1,4,1,9,10,35,1,3,1,1,13),_CvAtmPeerCfgDtmfRelay_Type())
cvAtmPeerCfgDtmfRelay.setMaxAccess(_D)
if mibBuilder.loadTexts:cvAtmPeerCfgDtmfRelay.setStatus(_A)
_CiscoVoiceAtmDialControlMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoVoiceAtmDialControlMIBNotificationPrefix=_CiscoVoiceAtmDialControlMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,10,35,2))
_CiscoVoiceAtmDialControlMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoVoiceAtmDialControlMIBNotifications=_CiscoVoiceAtmDialControlMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,35,2,0))
_CiscoVoiceAtmDialControlMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVoiceAtmDialControlMIBConformance=_CiscoVoiceAtmDialControlMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,35,3))
_CiscoVoiceAtmDialControlMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVoiceAtmDialControlMIBCompliances=_CiscoVoiceAtmDialControlMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,35,3,1))
_CiscoVoiceAtmDialControlMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVoiceAtmDialControlMIBGroups=_CiscoVoiceAtmDialControlMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,35,3,2))
cvAtmCallHistoryGroup=ObjectGroup((1,3,6,1,4,1,9,10,35,3,2,1))
cvAtmCallHistoryGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:cvAtmCallHistoryGroup.setStatus(_A)
cvAtmCallActiveGroup=ObjectGroup((1,3,6,1,4,1,9,10,35,3,2,2))
cvAtmCallActiveGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:cvAtmCallActiveGroup.setStatus(_A)
cvAtmPeerCfgGroup=ObjectGroup((1,3,6,1,4,1,9,10,35,3,2,3))
cvAtmPeerCfgGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cvAtmPeerCfgGroup.setStatus(_A)
ciscoVoiceAtmDialControlMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,35,3,1,1))
ciscoVoiceAtmDialControlMIBCompliance.setObjects(*((_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoVoiceAtmDialControlMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_R:CvAtmSessionProtocol,'ciscoVoiceAtmDialControlMIB':ciscoVoiceAtmDialControlMIB,'ciscoVoiceAtmDialControlMIBObjects':ciscoVoiceAtmDialControlMIBObjects,'cvAtmCallHistory':cvAtmCallHistory,'cvAtmCallHistoryTable':cvAtmCallHistoryTable,'cvAtmCallHistoryEntry':cvAtmCallHistoryEntry,_S:cvAtmCallHistoryConnectionId,_T:cvAtmCallHistoryVpi,_U:cvAtmCallHistoryVci,_V:cvAtmCallHistoryLowerIfName,_W:cvAtmCallHistorySessionTarget,_X:cvAtmCallHistorySubchannelID,_Y:cvAtmCallHistorySessionProtocol,_Z:cvAtmCallHistoryCalledNumber,_a:cvAtmCallHistoryDtmfRelay,_b:cvAtmCallHistoryUseSeqNumbers,'cvAtmCallActive':cvAtmCallActive,'cvAtmCallActiveTable':cvAtmCallActiveTable,'cvAtmCallActiveEntry':cvAtmCallActiveEntry,_c:cvAtmCallActiveConnectionId,_d:cvAtmCallActiveVpi,_e:cvAtmCallActiveVci,_f:cvAtmCallActiveLowerIfName,_g:cvAtmCallActiveSessionTarget,_h:cvAtmCallActiveSubchannelID,_i:cvAtmCallActiveSessionProtocol,_j:cvAtmCallActiveCalledNumber,_k:cvAtmCallActiveDtmfRelay,_l:cvAtmCallActiveUseSeqNumbers,'cvAtmDialPeer':cvAtmDialPeer,'cvAtmPeerCfgTable':cvAtmPeerCfgTable,'cvAtmPeerCfgEntry':cvAtmPeerCfgEntry,_m:cvAtmPeerCfgSessionProtocol,_n:cvAtmPeerCfgInterfaceName,_o:cvAtmPeerCfgVpi,_p:cvAtmPeerCfgVci,_q:cvAtmPeerCfgVcName,_r:cvAtmPeerCfgCoderRate,_s:cvAtmPeerCfgCodecBytes,_t:cvAtmPeerCfgFaxRate,_u:cvAtmPeerCfgFaxBytes,_v:cvAtmPeerCfgInBandSignaling,_w:cvAtmPeerCfgVADEnable,_x:cvAtmPeerCfgUseSeqNumbers,_y:cvAtmPeerCfgDtmfRelay,'ciscoVoiceAtmDialControlMIBNotificationPrefix':ciscoVoiceAtmDialControlMIBNotificationPrefix,'ciscoVoiceAtmDialControlMIBNotifications':ciscoVoiceAtmDialControlMIBNotifications,'ciscoVoiceAtmDialControlMIBConformance':ciscoVoiceAtmDialControlMIBConformance,'ciscoVoiceAtmDialControlMIBCompliances':ciscoVoiceAtmDialControlMIBCompliances,'ciscoVoiceAtmDialControlMIBCompliance':ciscoVoiceAtmDialControlMIBCompliance,'ciscoVoiceAtmDialControlMIBGroups':ciscoVoiceAtmDialControlMIBGroups,_z:cvAtmCallHistoryGroup,_A0:cvAtmCallActiveGroup,_A1:cvAtmPeerCfgGroup})