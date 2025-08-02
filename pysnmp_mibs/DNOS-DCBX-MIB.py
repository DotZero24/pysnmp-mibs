_L='applicationPriority'
_K='etsRecom'
_J='etsConfig'
_I='DcbxPortRole'
_H='Integer32'
_G='agentDcbxIntfIndex'
_F='DNOS-DCBX-MIB'
_E='Bits'
_D='DcbxVersion'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dnOS,=mibBuilder.importSymbols('DELL-REF-MIB','dnOS')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_E,'Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
fastPathDCBX=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58))
if mibBuilder.loadTexts:fastPathDCBX.setRevisions(('2011-04-20 00:00',))
class DcbxPortRole(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('manual',1),('autoup',2),('autodown',3),('configSource',4)))
class DcbxVersion(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('ieee',2),('cin',3),('cee',4)))
_AgentDcbxGroup_ObjectIdentity=ObjectIdentity
agentDcbxGroup=_AgentDcbxGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1))
_AgentDcbxTable_Object=MibTable
agentDcbxTable=_AgentDcbxTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,1))
if mibBuilder.loadTexts:agentDcbxTable.setStatus(_A)
_AgentDcbxEntry_Object=MibTableRow
agentDcbxEntry=_AgentDcbxEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,1,1))
agentDcbxEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:agentDcbxEntry.setStatus(_A)
_AgentDcbxIntfIndex_Type=InterfaceIndex
_AgentDcbxIntfIndex_Object=MibTableColumn
agentDcbxIntfIndex=_AgentDcbxIntfIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,1,1,1),_AgentDcbxIntfIndex_Type())
agentDcbxIntfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentDcbxIntfIndex.setStatus(_A)
class _AgentDcbxAutoCfgPortRole_Type(DcbxPortRole):defaultValue=1
_AgentDcbxAutoCfgPortRole_Type.__name__=_I
_AgentDcbxAutoCfgPortRole_Object=MibTableColumn
agentDcbxAutoCfgPortRole=_AgentDcbxAutoCfgPortRole_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,1,1,2),_AgentDcbxAutoCfgPortRole_Type())
agentDcbxAutoCfgPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDcbxAutoCfgPortRole.setStatus(_A)
class _AgentDcbxVersion_Type(DcbxVersion):defaultValue=1
_AgentDcbxVersion_Type.__name__=_D
_AgentDcbxVersion_Object=MibTableColumn
agentDcbxVersion=_AgentDcbxVersion_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,1,1,3),_AgentDcbxVersion_Type())
agentDcbxVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDcbxVersion.setStatus('deprecated')
class _AgentDcbxSupportedTLVs_Type(Bits):namedValues=NamedValues(*(('pfc',0),(_J,1),(_K,2),(_L,3)))
_AgentDcbxSupportedTLVs_Type.__name__=_E
_AgentDcbxSupportedTLVs_Object=MibTableColumn
agentDcbxSupportedTLVs=_AgentDcbxSupportedTLVs_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,1,1,4),_AgentDcbxSupportedTLVs_Type())
agentDcbxSupportedTLVs.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxSupportedTLVs.setStatus(_A)
class _AgentDcbxConfigTLVsTxEnable_Type(Bits):namedValues=NamedValues(*(('pfc',0),(_J,1),(_K,2),(_L,3)))
_AgentDcbxConfigTLVsTxEnable_Type.__name__=_E
_AgentDcbxConfigTLVsTxEnable_Object=MibTableColumn
agentDcbxConfigTLVsTxEnable=_AgentDcbxConfigTLVsTxEnable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,1,1,5),_AgentDcbxConfigTLVsTxEnable_Type())
agentDcbxConfigTLVsTxEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDcbxConfigTLVsTxEnable.setStatus(_A)
_AgentDcbxStatusTable_Object=MibTable
agentDcbxStatusTable=_AgentDcbxStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2))
if mibBuilder.loadTexts:agentDcbxStatusTable.setStatus(_A)
_AgentDcbxStatusEntry_Object=MibTableRow
agentDcbxStatusEntry=_AgentDcbxStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1))
agentDcbxStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:agentDcbxStatusEntry.setStatus(_A)
class _AgentDcbxOperVersion_Type(DcbxVersion):defaultValue=1
_AgentDcbxOperVersion_Type.__name__=_D
_AgentDcbxOperVersion_Object=MibTableColumn
agentDcbxOperVersion=_AgentDcbxOperVersion_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,2),_AgentDcbxOperVersion_Type())
agentDcbxOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxOperVersion.setStatus(_A)
_AgentDcbxPeerMACaddress_Type=MacAddress
_AgentDcbxPeerMACaddress_Object=MibTableColumn
agentDcbxPeerMACaddress=_AgentDcbxPeerMACaddress_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,3),_AgentDcbxPeerMACaddress_Type())
agentDcbxPeerMACaddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxPeerMACaddress.setStatus(_A)
class _AgentDcbxCfgSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_AgentDcbxCfgSource_Type.__name__=_H
_AgentDcbxCfgSource_Object=MibTableColumn
agentDcbxCfgSource=_AgentDcbxCfgSource_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,4),_AgentDcbxCfgSource_Type())
agentDcbxCfgSource.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxCfgSource.setStatus(_A)
_AgentDcbxMultiplePeerCount_Type=Unsigned32
_AgentDcbxMultiplePeerCount_Object=MibTableColumn
agentDcbxMultiplePeerCount=_AgentDcbxMultiplePeerCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,5),_AgentDcbxMultiplePeerCount_Type())
agentDcbxMultiplePeerCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxMultiplePeerCount.setStatus(_A)
_AgentDcbxPeerRemovedCount_Type=Unsigned32
_AgentDcbxPeerRemovedCount_Object=MibTableColumn
agentDcbxPeerRemovedCount=_AgentDcbxPeerRemovedCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,6),_AgentDcbxPeerRemovedCount_Type())
agentDcbxPeerRemovedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxPeerRemovedCount.setStatus(_A)
_AgentDcbxPeerOperVersionNum_Type=Unsigned32
_AgentDcbxPeerOperVersionNum_Object=MibTableColumn
agentDcbxPeerOperVersionNum=_AgentDcbxPeerOperVersionNum_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,7),_AgentDcbxPeerOperVersionNum_Type())
agentDcbxPeerOperVersionNum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxPeerOperVersionNum.setStatus(_A)
_AgentDcbxPeerMaxVersion_Type=Unsigned32
_AgentDcbxPeerMaxVersion_Object=MibTableColumn
agentDcbxPeerMaxVersion=_AgentDcbxPeerMaxVersion_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,8),_AgentDcbxPeerMaxVersion_Type())
agentDcbxPeerMaxVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxPeerMaxVersion.setStatus(_A)
_AgentDcbxSeqNum_Type=Unsigned32
_AgentDcbxSeqNum_Object=MibTableColumn
agentDcbxSeqNum=_AgentDcbxSeqNum_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,9),_AgentDcbxSeqNum_Type())
agentDcbxSeqNum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxSeqNum.setStatus(_A)
_AgentDcbxAckNum_Type=Unsigned32
_AgentDcbxAckNum_Object=MibTableColumn
agentDcbxAckNum=_AgentDcbxAckNum_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,10),_AgentDcbxAckNum_Type())
agentDcbxAckNum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxAckNum.setStatus(_A)
_AgentDcbxPeerRcvdAckNum_Type=Unsigned32
_AgentDcbxPeerRcvdAckNum_Object=MibTableColumn
agentDcbxPeerRcvdAckNum=_AgentDcbxPeerRcvdAckNum_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,11),_AgentDcbxPeerRcvdAckNum_Type())
agentDcbxPeerRcvdAckNum.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxPeerRcvdAckNum.setStatus(_A)
_AgentDcbxTxCount_Type=Unsigned32
_AgentDcbxTxCount_Object=MibTableColumn
agentDcbxTxCount=_AgentDcbxTxCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,12),_AgentDcbxTxCount_Type())
agentDcbxTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxTxCount.setStatus(_A)
_AgentDcbxRxCount_Type=Unsigned32
_AgentDcbxRxCount_Object=MibTableColumn
agentDcbxRxCount=_AgentDcbxRxCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,13),_AgentDcbxRxCount_Type())
agentDcbxRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxRxCount.setStatus(_A)
_AgentDcbxErrorFramesCount_Type=Unsigned32
_AgentDcbxErrorFramesCount_Object=MibTableColumn
agentDcbxErrorFramesCount=_AgentDcbxErrorFramesCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,14),_AgentDcbxErrorFramesCount_Type())
agentDcbxErrorFramesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxErrorFramesCount.setStatus(_A)
_AgentDcbxUnknownTLVsCount_Type=Unsigned32
_AgentDcbxUnknownTLVsCount_Object=MibTableColumn
agentDcbxUnknownTLVsCount=_AgentDcbxUnknownTLVsCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,2,1,15),_AgentDcbxUnknownTLVsCount_Type())
agentDcbxUnknownTLVsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDcbxUnknownTLVsCount.setStatus(_A)
_AgentDcbxGroupGlobalConfGroup_ObjectIdentity=ObjectIdentity
agentDcbxGroupGlobalConfGroup=_AgentDcbxGroupGlobalConfGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,3))
class _AgentDcbxGlobalConfVersion_Type(DcbxVersion):defaultValue=1
_AgentDcbxGlobalConfVersion_Type.__name__=_D
_AgentDcbxGlobalConfVersion_Object=MibScalar
agentDcbxGlobalConfVersion=_AgentDcbxGlobalConfVersion_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,58,1,3,1),_AgentDcbxGlobalConfVersion_Type())
agentDcbxGlobalConfVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDcbxGlobalConfVersion.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_I:DcbxPortRole,_D:DcbxVersion,'fastPathDCBX':fastPathDCBX,'agentDcbxGroup':agentDcbxGroup,'agentDcbxTable':agentDcbxTable,'agentDcbxEntry':agentDcbxEntry,_G:agentDcbxIntfIndex,'agentDcbxAutoCfgPortRole':agentDcbxAutoCfgPortRole,'agentDcbxVersion':agentDcbxVersion,'agentDcbxSupportedTLVs':agentDcbxSupportedTLVs,'agentDcbxConfigTLVsTxEnable':agentDcbxConfigTLVsTxEnable,'agentDcbxStatusTable':agentDcbxStatusTable,'agentDcbxStatusEntry':agentDcbxStatusEntry,'agentDcbxOperVersion':agentDcbxOperVersion,'agentDcbxPeerMACaddress':agentDcbxPeerMACaddress,'agentDcbxCfgSource':agentDcbxCfgSource,'agentDcbxMultiplePeerCount':agentDcbxMultiplePeerCount,'agentDcbxPeerRemovedCount':agentDcbxPeerRemovedCount,'agentDcbxPeerOperVersionNum':agentDcbxPeerOperVersionNum,'agentDcbxPeerMaxVersion':agentDcbxPeerMaxVersion,'agentDcbxSeqNum':agentDcbxSeqNum,'agentDcbxAckNum':agentDcbxAckNum,'agentDcbxPeerRcvdAckNum':agentDcbxPeerRcvdAckNum,'agentDcbxTxCount':agentDcbxTxCount,'agentDcbxRxCount':agentDcbxRxCount,'agentDcbxErrorFramesCount':agentDcbxErrorFramesCount,'agentDcbxUnknownTLVsCount':agentDcbxUnknownTLVsCount,'agentDcbxGroupGlobalConfGroup':agentDcbxGroupGlobalConfGroup,'agentDcbxGlobalConfVersion':agentDcbxGlobalConfVersion})