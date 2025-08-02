_W='oacEthOamExtMepEntry'
_V='oacEthOamLbrNotRespMepId'
_U='oacEthOamLbrReceiveOrder'
_T='EthOamExtMepMode'
_S='read-create'
_R='EthOamExtMipMode'
_Q='oacEthOamMipVlanIndex'
_P='oacEthOamMipMegLevel'
_O='oacEthOamMipIfIndex'
_N='mode8021ag'
_M='modey1731'
_L='Unsigned32'
_K='TruthValue'
_J='dot1agCfmMepIdentifier'
_I='dot1agCfmMdIndex'
_H='dot1agCfmMaIndex'
_G='Dot1agCfmCcmInterval'
_F='not-accessible'
_E='ONEACCESS-ETHOAM-EXT-MIB'
_D='IEEE8021-CFM-MIB'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmCcmInterval,Dot1agCfmConfigErrors,Dot1agCfmIdPermission,Dot1agCfmMDLevel,Dot1agCfmMDLevelOrNone,Dot1agCfmMepIdOrZero,Dot1agCfmMhfCreation,Dot1agCfmMpDirection,dot1agCfmConfigErrorList,dot1agCfmDefaultMd,dot1agCfmMa,dot1agCfmMaIndex,dot1agCfmMaMepListRowStatus,dot1agCfmMaNetRowStatus,dot1agCfmMdIndex,dot1agCfmMdRowStatus,dot1agCfmMepEntry,dot1agCfmMepIdentifier,dot1agCfmMepLbrBadMsdu,dot1agCfmMepRowStatus,dot1agCfmStack,dot1agCfmVlan=mibBuilder.importSymbols(_D,_G,'Dot1agCfmConfigErrors','Dot1agCfmIdPermission','Dot1agCfmMDLevel','Dot1agCfmMDLevelOrNone','Dot1agCfmMepIdOrZero','Dot1agCfmMhfCreation','Dot1agCfmMpDirection','dot1agCfmConfigErrorList','dot1agCfmDefaultMd','dot1agCfmMa',_H,'dot1agCfmMaMepListRowStatus','dot1agCfmMaNetRowStatus',_I,'dot1agCfmMdRowStatus','dot1agCfmMepEntry',_J,'dot1agCfmMepLbrBadMsdu','dot1agCfmMepRowStatus','dot1agCfmStack','dot1agCfmVlan')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
oacExpIMEthernet,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMEthernet','oacMIBModules')
VlanIdOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIdOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
oacEthOamExtMib=ModuleIdentity((1,3,6,1,4,1,13191,1,100,689))
if mibBuilder.loadTexts:oacEthOamExtMib.setRevisions(('2011-07-29 00:00','2011-06-15 00:00','2011-01-05 00:01','2010-08-12 00:01'))
class EthOamExtMipMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
class EthOamExtMepMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),(_N,2),('modehybrid',3)))
class EthOamEfdState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('efdDisabled',1),('efdIdle',2),('efdTriggered',3)))
_OacEthOamExtMIBObjects_ObjectIdentity=ObjectIdentity
oacEthOamExtMIBObjects=_OacEthOamExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,10,2))
_OacEthOamExtIfObjects_ObjectIdentity=ObjectIdentity
oacEthOamExtIfObjects=_OacEthOamExtIfObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,10,2,1))
_OacEthOamExtMipTable_Object=MibTable
oacEthOamExtMipTable=_OacEthOamExtMipTable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,1))
if mibBuilder.loadTexts:oacEthOamExtMipTable.setStatus(_A)
_OacEthOamExtMipEntry_Object=MibTableRow
oacEthOamExtMipEntry=_OacEthOamExtMipEntry_Object((1,3,6,1,4,1,13191,10,3,10,2,1,1,1))
oacEthOamExtMipEntry.setIndexNames((0,_E,_O),(0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:oacEthOamExtMipEntry.setStatus(_A)
_OacEthOamMipIfIndex_Type=InterfaceIndex
_OacEthOamMipIfIndex_Object=MibTableColumn
oacEthOamMipIfIndex=_OacEthOamMipIfIndex_Object((1,3,6,1,4,1,13191,10,3,10,2,1,1,1,1),_OacEthOamMipIfIndex_Type())
oacEthOamMipIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacEthOamMipIfIndex.setStatus(_A)
_OacEthOamMipMegLevel_Type=Unsigned32
_OacEthOamMipMegLevel_Object=MibTableColumn
oacEthOamMipMegLevel=_OacEthOamMipMegLevel_Object((1,3,6,1,4,1,13191,10,3,10,2,1,1,1,2),_OacEthOamMipMegLevel_Type())
oacEthOamMipMegLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:oacEthOamMipMegLevel.setStatus(_A)
_OacEthOamMipVlanIndex_Type=VlanIdOrNone
_OacEthOamMipVlanIndex_Object=MibTableColumn
oacEthOamMipVlanIndex=_OacEthOamMipVlanIndex_Object((1,3,6,1,4,1,13191,10,3,10,2,1,1,1,3),_OacEthOamMipVlanIndex_Type())
oacEthOamMipVlanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:oacEthOamMipVlanIndex.setStatus(_A)
class _OacEthOamMipMode_Type(EthOamExtMipMode):defaultValue=1
_OacEthOamMipMode_Type.__name__=_R
_OacEthOamMipMode_Object=MibTableColumn
oacEthOamMipMode=_OacEthOamMipMode_Object((1,3,6,1,4,1,13191,10,3,10,2,1,1,1,4),_OacEthOamMipMode_Type())
oacEthOamMipMode.setMaxAccess(_S)
if mibBuilder.loadTexts:oacEthOamMipMode.setStatus(_A)
_OacEthOamMipRowStatus_Type=RowStatus
_OacEthOamMipRowStatus_Object=MibTableColumn
oacEthOamMipRowStatus=_OacEthOamMipRowStatus_Object((1,3,6,1,4,1,13191,10,3,10,2,1,1,1,5),_OacEthOamMipRowStatus_Type())
oacEthOamMipRowStatus.setMaxAccess(_S)
if mibBuilder.loadTexts:oacEthOamMipRowStatus.setStatus(_A)
_OacEthOamExtMepTable_Object=MibTable
oacEthOamExtMepTable=_OacEthOamExtMepTable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2))
if mibBuilder.loadTexts:oacEthOamExtMepTable.setStatus(_A)
_OacEthOamExtMepEntry_Object=MibTableRow
oacEthOamExtMepEntry=_OacEthOamExtMepEntry_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1))
if mibBuilder.loadTexts:oacEthOamExtMepEntry.setStatus(_A)
class _OacEthOamMepMode_Type(EthOamExtMepMode):defaultValue=3
_OacEthOamMepMode_Type.__name__=_T
_OacEthOamMepMode_Object=MibTableColumn
oacEthOamMepMode=_OacEthOamMepMode_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,1),_OacEthOamMepMode_Type())
oacEthOamMepMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepMode.setStatus(_A)
_OacEthOamMepLossDestMacAddress_Type=MacAddress
_OacEthOamMepLossDestMacAddress_Object=MibTableColumn
oacEthOamMepLossDestMacAddress=_OacEthOamMepLossDestMacAddress_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,10),_OacEthOamMepLossDestMacAddress_Type())
oacEthOamMepLossDestMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepLossDestMacAddress.setStatus(_A)
_OacEthOamMepLossDestMepId_Type=Dot1agCfmMepIdOrZero
_OacEthOamMepLossDestMepId_Object=MibTableColumn
oacEthOamMepLossDestMepId=_OacEthOamMepLossDestMepId_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,11),_OacEthOamMepLossDestMepId_Type())
oacEthOamMepLossDestMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepLossDestMepId.setStatus(_A)
_OacEthOamMepLossDestIsMepId_Type=TruthValue
_OacEthOamMepLossDestIsMepId_Object=MibTableColumn
oacEthOamMepLossDestIsMepId=_OacEthOamMepLossDestIsMepId_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,12),_OacEthOamMepLossDestIsMepId_Type())
oacEthOamMepLossDestIsMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepLossDestIsMepId.setStatus(_A)
_OacEthOamMepLossVlanPriority_Type=Unsigned32
_OacEthOamMepLossVlanPriority_Object=MibTableColumn
oacEthOamMepLossVlanPriority=_OacEthOamMepLossVlanPriority_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,13),_OacEthOamMepLossVlanPriority_Type())
oacEthOamMepLossVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepLossVlanPriority.setStatus(_A)
class _OacEthOamMepLossInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_OacEthOamMepLossInterval_Type.__name__=_G
_OacEthOamMepLossInterval_Object=MibTableColumn
oacEthOamMepLossInterval=_OacEthOamMepLossInterval_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,14),_OacEthOamMepLossInterval_Type())
oacEthOamMepLossInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepLossInterval.setStatus(_A)
class _OacEthOamMepLossStatus_Type(TruthValue):defaultValue=2
_OacEthOamMepLossStatus_Type.__name__=_K
_OacEthOamMepLossStatus_Object=MibTableColumn
oacEthOamMepLossStatus=_OacEthOamMepLossStatus_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,15),_OacEthOamMepLossStatus_Type())
oacEthOamMepLossStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepLossStatus.setStatus(_A)
_OacEthOamMepLossMessagesStart_Type=TruthValue
_OacEthOamMepLossMessagesStart_Object=MibTableColumn
oacEthOamMepLossMessagesStart=_OacEthOamMepLossMessagesStart_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,16),_OacEthOamMepLossMessagesStart_Type())
oacEthOamMepLossMessagesStart.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepLossMessagesStart.setStatus(_A)
_OacEthOamMepLossResultOK_Type=TruthValue
_OacEthOamMepLossResultOK_Object=MibTableColumn
oacEthOamMepLossResultOK=_OacEthOamMepLossResultOK_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,17),_OacEthOamMepLossResultOK_Type())
oacEthOamMepLossResultOK.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepLossResultOK.setStatus(_A)
_OacEthOamMepLossNbrOfTxFrames_Type=Counter32
_OacEthOamMepLossNbrOfTxFrames_Object=MibTableColumn
oacEthOamMepLossNbrOfTxFrames=_OacEthOamMepLossNbrOfTxFrames_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,18),_OacEthOamMepLossNbrOfTxFrames_Type())
oacEthOamMepLossNbrOfTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepLossNbrOfTxFrames.setStatus(_A)
_OacEthOamMepLossNbrOfRxFrames_Type=Counter32
_OacEthOamMepLossNbrOfRxFrames_Object=MibTableColumn
oacEthOamMepLossNbrOfRxFrames=_OacEthOamMepLossNbrOfRxFrames_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,19),_OacEthOamMepLossNbrOfRxFrames_Type())
oacEthOamMepLossNbrOfRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepLossNbrOfRxFrames.setStatus(_A)
_OacEthOamMepLossReplyLoss_Type=Counter32
_OacEthOamMepLossReplyLoss_Object=MibTableColumn
oacEthOamMepLossReplyLoss=_OacEthOamMepLossReplyLoss_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,20),_OacEthOamMepLossReplyLoss_Type())
oacEthOamMepLossReplyLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepLossReplyLoss.setStatus(_A)
_OacEthOamMepLossNearEndDrops_Type=Counter32
_OacEthOamMepLossNearEndDrops_Object=MibTableColumn
oacEthOamMepLossNearEndDrops=_OacEthOamMepLossNearEndDrops_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,21),_OacEthOamMepLossNearEndDrops_Type())
oacEthOamMepLossNearEndDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepLossNearEndDrops.setStatus(_A)
_OacEthOamMepLossFarEndDrops_Type=Counter32
_OacEthOamMepLossFarEndDrops_Object=MibTableColumn
oacEthOamMepLossFarEndDrops=_OacEthOamMepLossFarEndDrops_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,22),_OacEthOamMepLossFarEndDrops_Type())
oacEthOamMepLossFarEndDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepLossFarEndDrops.setStatus(_A)
_OacEthOamMepDelayDestMacAddress_Type=MacAddress
_OacEthOamMepDelayDestMacAddress_Object=MibTableColumn
oacEthOamMepDelayDestMacAddress=_OacEthOamMepDelayDestMacAddress_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,30),_OacEthOamMepDelayDestMacAddress_Type())
oacEthOamMepDelayDestMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayDestMacAddress.setStatus(_A)
_OacEthOamMepDelayDestMepId_Type=Dot1agCfmMepIdOrZero
_OacEthOamMepDelayDestMepId_Object=MibTableColumn
oacEthOamMepDelayDestMepId=_OacEthOamMepDelayDestMepId_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,31),_OacEthOamMepDelayDestMepId_Type())
oacEthOamMepDelayDestMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayDestMepId.setStatus(_A)
_OacEthOamMepDelayDestIsMepId_Type=TruthValue
_OacEthOamMepDelayDestIsMepId_Object=MibTableColumn
oacEthOamMepDelayDestIsMepId=_OacEthOamMepDelayDestIsMepId_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,32),_OacEthOamMepDelayDestIsMepId_Type())
oacEthOamMepDelayDestIsMepId.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayDestIsMepId.setStatus(_A)
_OacEthOamMepDelayVlanPriority_Type=Unsigned32
_OacEthOamMepDelayVlanPriority_Object=MibTableColumn
oacEthOamMepDelayVlanPriority=_OacEthOamMepDelayVlanPriority_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,33),_OacEthOamMepDelayVlanPriority_Type())
oacEthOamMepDelayVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayVlanPriority.setStatus(_A)
class _OacEthOamMepDelayInterval_Type(Dot1agCfmCcmInterval):defaultValue=4
_OacEthOamMepDelayInterval_Type.__name__=_G
_OacEthOamMepDelayInterval_Object=MibTableColumn
oacEthOamMepDelayInterval=_OacEthOamMepDelayInterval_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,34),_OacEthOamMepDelayInterval_Type())
oacEthOamMepDelayInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayInterval.setStatus(_A)
class _OacEthOamMepDelayStatus_Type(TruthValue):defaultValue=2
_OacEthOamMepDelayStatus_Type.__name__=_K
_OacEthOamMepDelayStatus_Object=MibTableColumn
oacEthOamMepDelayStatus=_OacEthOamMepDelayStatus_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,35),_OacEthOamMepDelayStatus_Type())
oacEthOamMepDelayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayStatus.setStatus(_A)
_OacEthOamMepDelayTimeOut_Type=Unsigned32
_OacEthOamMepDelayTimeOut_Object=MibTableColumn
oacEthOamMepDelayTimeOut=_OacEthOamMepDelayTimeOut_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,36),_OacEthOamMepDelayTimeOut_Type())
oacEthOamMepDelayTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayTimeOut.setStatus(_A)
_OacEthOamMepDelayMessagesStart_Type=TruthValue
_OacEthOamMepDelayMessagesStart_Object=MibTableColumn
oacEthOamMepDelayMessagesStart=_OacEthOamMepDelayMessagesStart_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,37),_OacEthOamMepDelayMessagesStart_Type())
oacEthOamMepDelayMessagesStart.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepDelayMessagesStart.setStatus(_A)
_OacEthOamMepDelayResultOK_Type=TruthValue
_OacEthOamMepDelayResultOK_Object=MibTableColumn
oacEthOamMepDelayResultOK=_OacEthOamMepDelayResultOK_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,38),_OacEthOamMepDelayResultOK_Type())
oacEthOamMepDelayResultOK.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayResultOK.setStatus(_A)
_OacEthOamMepDelayNbrOfTxFrames_Type=Counter32
_OacEthOamMepDelayNbrOfTxFrames_Object=MibTableColumn
oacEthOamMepDelayNbrOfTxFrames=_OacEthOamMepDelayNbrOfTxFrames_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,39),_OacEthOamMepDelayNbrOfTxFrames_Type())
oacEthOamMepDelayNbrOfTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayNbrOfTxFrames.setStatus(_A)
_OacEthOamMepDelayNbrOfRxFrames_Type=Counter32
_OacEthOamMepDelayNbrOfRxFrames_Object=MibTableColumn
oacEthOamMepDelayNbrOfRxFrames=_OacEthOamMepDelayNbrOfRxFrames_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,40),_OacEthOamMepDelayNbrOfRxFrames_Type())
oacEthOamMepDelayNbrOfRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayNbrOfRxFrames.setStatus(_A)
_OacEthOamMepDelayLoss_Type=Counter32
_OacEthOamMepDelayLoss_Object=MibTableColumn
oacEthOamMepDelayLoss=_OacEthOamMepDelayLoss_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,41),_OacEthOamMepDelayLoss_Type())
oacEthOamMepDelayLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayLoss.setStatus(_A)
_OacEthOamMepDelayMin_Type=Unsigned32
_OacEthOamMepDelayMin_Object=MibTableColumn
oacEthOamMepDelayMin=_OacEthOamMepDelayMin_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,42),_OacEthOamMepDelayMin_Type())
oacEthOamMepDelayMin.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayMin.setStatus(_A)
_OacEthOamMepDelayMax_Type=Unsigned32
_OacEthOamMepDelayMax_Object=MibTableColumn
oacEthOamMepDelayMax=_OacEthOamMepDelayMax_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,43),_OacEthOamMepDelayMax_Type())
oacEthOamMepDelayMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayMax.setStatus(_A)
_OacEthOamMepDelayAvrg_Type=Unsigned32
_OacEthOamMepDelayAvrg_Object=MibTableColumn
oacEthOamMepDelayAvrg=_OacEthOamMepDelayAvrg_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,44),_OacEthOamMepDelayAvrg_Type())
oacEthOamMepDelayAvrg.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayAvrg.setStatus(_A)
_OacEthOamMepDelayJitterNegMax_Type=Unsigned32
_OacEthOamMepDelayJitterNegMax_Object=MibTableColumn
oacEthOamMepDelayJitterNegMax=_OacEthOamMepDelayJitterNegMax_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,45),_OacEthOamMepDelayJitterNegMax_Type())
oacEthOamMepDelayJitterNegMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayJitterNegMax.setStatus(_A)
_OacEthOamMepDelayJitterAvrgMax_Type=Unsigned32
_OacEthOamMepDelayJitterAvrgMax_Object=MibTableColumn
oacEthOamMepDelayJitterAvrgMax=_OacEthOamMepDelayJitterAvrgMax_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,46),_OacEthOamMepDelayJitterAvrgMax_Type())
oacEthOamMepDelayJitterAvrgMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayJitterAvrgMax.setStatus(_A)
_OacEthOamMepDelayJitterPosMax_Type=Unsigned32
_OacEthOamMepDelayJitterPosMax_Object=MibTableColumn
oacEthOamMepDelayJitterPosMax=_OacEthOamMepDelayJitterPosMax_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,47),_OacEthOamMepDelayJitterPosMax_Type())
oacEthOamMepDelayJitterPosMax.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepDelayJitterPosMax.setStatus(_A)
_OacEthOamMepRdiTxEnable_Type=TruthValue
_OacEthOamMepRdiTxEnable_Object=MibTableColumn
oacEthOamMepRdiTxEnable=_OacEthOamMepRdiTxEnable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,60),_OacEthOamMepRdiTxEnable_Type())
oacEthOamMepRdiTxEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepRdiTxEnable.setStatus(_A)
_OacEthOamMepMcastLbmStatus_Type=TruthValue
_OacEthOamMepMcastLbmStatus_Object=MibTableColumn
oacEthOamMepMcastLbmStatus=_OacEthOamMepMcastLbmStatus_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,70),_OacEthOamMepMcastLbmStatus_Type())
oacEthOamMepMcastLbmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepMcastLbmStatus.setStatus(_A)
_OacEthOamMepMcastLbmResult_Type=TruthValue
_OacEthOamMepMcastLbmResult_Object=MibTableColumn
oacEthOamMepMcastLbmResult=_OacEthOamMepMcastLbmResult_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,71),_OacEthOamMepMcastLbmResult_Type())
oacEthOamMepMcastLbmResult.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepMcastLbmResult.setStatus(_A)
_OacEthOamMepMcastLbmSeqNumber_Type=Unsigned32
_OacEthOamMepMcastLbmSeqNumber_Object=MibTableColumn
oacEthOamMepMcastLbmSeqNumber=_OacEthOamMepMcastLbmSeqNumber_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,72),_OacEthOamMepMcastLbmSeqNumber_Type())
oacEthOamMepMcastLbmSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepMcastLbmSeqNumber.setStatus(_A)
_OacEthOamMepMcastLbmDataTlv_Type=OctetString
_OacEthOamMepMcastLbmDataTlv_Object=MibTableColumn
oacEthOamMepMcastLbmDataTlv=_OacEthOamMepMcastLbmDataTlv_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,73),_OacEthOamMepMcastLbmDataTlv_Type())
oacEthOamMepMcastLbmDataTlv.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepMcastLbmDataTlv.setStatus(_A)
_OacEthOamMepAisInterval_Type=Unsigned32
_OacEthOamMepAisInterval_Object=MibTableColumn
oacEthOamMepAisInterval=_OacEthOamMepAisInterval_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,80),_OacEthOamMepAisInterval_Type())
oacEthOamMepAisInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepAisInterval.setStatus(_A)
_OacEthOamMepAisVlanPriority_Type=Unsigned32
_OacEthOamMepAisVlanPriority_Object=MibTableColumn
oacEthOamMepAisVlanPriority=_OacEthOamMepAisVlanPriority_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,81),_OacEthOamMepAisVlanPriority_Type())
oacEthOamMepAisVlanPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepAisVlanPriority.setStatus(_A)
_OacEthOamMepAisTxEnable_Type=TruthValue
_OacEthOamMepAisTxEnable_Object=MibTableColumn
oacEthOamMepAisTxEnable=_OacEthOamMepAisTxEnable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,82),_OacEthOamMepAisTxEnable_Type())
oacEthOamMepAisTxEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepAisTxEnable.setStatus(_A)
_OacEthOamMepAisClientMegLevel_Type=Unsigned32
_OacEthOamMepAisClientMegLevel_Object=MibTableColumn
oacEthOamMepAisClientMegLevel=_OacEthOamMepAisClientMegLevel_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,83),_OacEthOamMepAisClientMegLevel_Type())
oacEthOamMepAisClientMegLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepAisClientMegLevel.setStatus(_A)
_OacEthOamMepEfdEnable_Type=TruthValue
_OacEthOamMepEfdEnable_Object=MibTableColumn
oacEthOamMepEfdEnable=_OacEthOamMepEfdEnable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,90),_OacEthOamMepEfdEnable_Type())
oacEthOamMepEfdEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamMepEfdEnable.setStatus(_A)
_OacEthOamMepEfdState_Type=EthOamEfdState
_OacEthOamMepEfdState_Object=MibTableColumn
oacEthOamMepEfdState=_OacEthOamMepEfdState_Object((1,3,6,1,4,1,13191,10,3,10,2,1,2,1,91),_OacEthOamMepEfdState_Type())
oacEthOamMepEfdState.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamMepEfdState.setStatus(_A)
_OacEthOamExtGlobal_ObjectIdentity=ObjectIdentity
oacEthOamExtGlobal=_OacEthOamExtGlobal_ObjectIdentity((1,3,6,1,4,1,13191,10,3,10,2,1,3))
_OacEthOamExtEnable_Type=TruthValue
_OacEthOamExtEnable_Object=MibScalar
oacEthOamExtEnable=_OacEthOamExtEnable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,3,1),_OacEthOamExtEnable_Type())
oacEthOamExtEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:oacEthOamExtEnable.setStatus(_A)
_OacEthOamExtLbrTable_Object=MibTable
oacEthOamExtLbrTable=_OacEthOamExtLbrTable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,4))
if mibBuilder.loadTexts:oacEthOamExtLbrTable.setStatus(_A)
_OacEthOamExtLbrEntry_Object=MibTableRow
oacEthOamExtLbrEntry=_OacEthOamExtLbrEntry_Object((1,3,6,1,4,1,13191,10,3,10,2,1,4,1))
oacEthOamExtLbrEntry.setIndexNames((0,_D,_I),(0,_D,_H),(0,_D,_J),(0,_E,_U))
if mibBuilder.loadTexts:oacEthOamExtLbrEntry.setStatus(_A)
class _OacEthOamLbrReceiveOrder_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_OacEthOamLbrReceiveOrder_Type.__name__=_L
_OacEthOamLbrReceiveOrder_Object=MibTableColumn
oacEthOamLbrReceiveOrder=_OacEthOamLbrReceiveOrder_Object((1,3,6,1,4,1,13191,10,3,10,2,1,4,1,1),_OacEthOamLbrReceiveOrder_Type())
oacEthOamLbrReceiveOrder.setMaxAccess(_F)
if mibBuilder.loadTexts:oacEthOamLbrReceiveOrder.setStatus(_A)
_OacEthOamLbrPeerMacAddress_Type=MacAddress
_OacEthOamLbrPeerMacAddress_Object=MibTableColumn
oacEthOamLbrPeerMacAddress=_OacEthOamLbrPeerMacAddress_Object((1,3,6,1,4,1,13191,10,3,10,2,1,4,1,2),_OacEthOamLbrPeerMacAddress_Type())
oacEthOamLbrPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamLbrPeerMacAddress.setStatus(_A)
_OacEthOamLbrMepId_Type=Dot1agCfmMepIdOrZero
_OacEthOamLbrMepId_Object=MibTableColumn
oacEthOamLbrMepId=_OacEthOamLbrMepId_Object((1,3,6,1,4,1,13191,10,3,10,2,1,4,1,3),_OacEthOamLbrMepId_Type())
oacEthOamLbrMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamLbrMepId.setStatus(_A)
_OacEthOamLbrNotRespTable_Object=MibTable
oacEthOamLbrNotRespTable=_OacEthOamLbrNotRespTable_Object((1,3,6,1,4,1,13191,10,3,10,2,1,5))
if mibBuilder.loadTexts:oacEthOamLbrNotRespTable.setStatus(_A)
_OacEthOamLbrNotRespEntry_Object=MibTableRow
oacEthOamLbrNotRespEntry=_OacEthOamLbrNotRespEntry_Object((1,3,6,1,4,1,13191,10,3,10,2,1,5,1))
oacEthOamLbrNotRespEntry.setIndexNames((0,_D,_I),(0,_D,_H),(0,_D,_J),(0,_E,_V))
if mibBuilder.loadTexts:oacEthOamLbrNotRespEntry.setStatus(_A)
_OacEthOamLbrNotRespMepId_Type=Dot1agCfmMepIdOrZero
_OacEthOamLbrNotRespMepId_Object=MibTableColumn
oacEthOamLbrNotRespMepId=_OacEthOamLbrNotRespMepId_Object((1,3,6,1,4,1,13191,10,3,10,2,1,5,1,1),_OacEthOamLbrNotRespMepId_Type())
oacEthOamLbrNotRespMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamLbrNotRespMepId.setStatus(_A)
_OacEthOamLbrNotRespPeerMacAddress_Type=MacAddress
_OacEthOamLbrNotRespPeerMacAddress_Object=MibTableColumn
oacEthOamLbrNotRespPeerMacAddress=_OacEthOamLbrNotRespPeerMacAddress_Object((1,3,6,1,4,1,13191,10,3,10,2,1,5,1,2),_OacEthOamLbrNotRespPeerMacAddress_Type())
oacEthOamLbrNotRespPeerMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:oacEthOamLbrNotRespPeerMacAddress.setStatus(_A)
dot1agCfmMepEntry.registerAugmentions((_E,_W))
oacEthOamExtMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{_R:EthOamExtMipMode,_T:EthOamExtMepMode,'EthOamEfdState':EthOamEfdState,'oacEthOamExtMib':oacEthOamExtMib,'oacEthOamExtMIBObjects':oacEthOamExtMIBObjects,'oacEthOamExtIfObjects':oacEthOamExtIfObjects,'oacEthOamExtMipTable':oacEthOamExtMipTable,'oacEthOamExtMipEntry':oacEthOamExtMipEntry,_O:oacEthOamMipIfIndex,_P:oacEthOamMipMegLevel,_Q:oacEthOamMipVlanIndex,'oacEthOamMipMode':oacEthOamMipMode,'oacEthOamMipRowStatus':oacEthOamMipRowStatus,'oacEthOamExtMepTable':oacEthOamExtMepTable,_W:oacEthOamExtMepEntry,'oacEthOamMepMode':oacEthOamMepMode,'oacEthOamMepLossDestMacAddress':oacEthOamMepLossDestMacAddress,'oacEthOamMepLossDestMepId':oacEthOamMepLossDestMepId,'oacEthOamMepLossDestIsMepId':oacEthOamMepLossDestIsMepId,'oacEthOamMepLossVlanPriority':oacEthOamMepLossVlanPriority,'oacEthOamMepLossInterval':oacEthOamMepLossInterval,'oacEthOamMepLossStatus':oacEthOamMepLossStatus,'oacEthOamMepLossMessagesStart':oacEthOamMepLossMessagesStart,'oacEthOamMepLossResultOK':oacEthOamMepLossResultOK,'oacEthOamMepLossNbrOfTxFrames':oacEthOamMepLossNbrOfTxFrames,'oacEthOamMepLossNbrOfRxFrames':oacEthOamMepLossNbrOfRxFrames,'oacEthOamMepLossReplyLoss':oacEthOamMepLossReplyLoss,'oacEthOamMepLossNearEndDrops':oacEthOamMepLossNearEndDrops,'oacEthOamMepLossFarEndDrops':oacEthOamMepLossFarEndDrops,'oacEthOamMepDelayDestMacAddress':oacEthOamMepDelayDestMacAddress,'oacEthOamMepDelayDestMepId':oacEthOamMepDelayDestMepId,'oacEthOamMepDelayDestIsMepId':oacEthOamMepDelayDestIsMepId,'oacEthOamMepDelayVlanPriority':oacEthOamMepDelayVlanPriority,'oacEthOamMepDelayInterval':oacEthOamMepDelayInterval,'oacEthOamMepDelayStatus':oacEthOamMepDelayStatus,'oacEthOamMepDelayTimeOut':oacEthOamMepDelayTimeOut,'oacEthOamMepDelayMessagesStart':oacEthOamMepDelayMessagesStart,'oacEthOamMepDelayResultOK':oacEthOamMepDelayResultOK,'oacEthOamMepDelayNbrOfTxFrames':oacEthOamMepDelayNbrOfTxFrames,'oacEthOamMepDelayNbrOfRxFrames':oacEthOamMepDelayNbrOfRxFrames,'oacEthOamMepDelayLoss':oacEthOamMepDelayLoss,'oacEthOamMepDelayMin':oacEthOamMepDelayMin,'oacEthOamMepDelayMax':oacEthOamMepDelayMax,'oacEthOamMepDelayAvrg':oacEthOamMepDelayAvrg,'oacEthOamMepDelayJitterNegMax':oacEthOamMepDelayJitterNegMax,'oacEthOamMepDelayJitterAvrgMax':oacEthOamMepDelayJitterAvrgMax,'oacEthOamMepDelayJitterPosMax':oacEthOamMepDelayJitterPosMax,'oacEthOamMepRdiTxEnable':oacEthOamMepRdiTxEnable,'oacEthOamMepMcastLbmStatus':oacEthOamMepMcastLbmStatus,'oacEthOamMepMcastLbmResult':oacEthOamMepMcastLbmResult,'oacEthOamMepMcastLbmSeqNumber':oacEthOamMepMcastLbmSeqNumber,'oacEthOamMepMcastLbmDataTlv':oacEthOamMepMcastLbmDataTlv,'oacEthOamMepAisInterval':oacEthOamMepAisInterval,'oacEthOamMepAisVlanPriority':oacEthOamMepAisVlanPriority,'oacEthOamMepAisTxEnable':oacEthOamMepAisTxEnable,'oacEthOamMepAisClientMegLevel':oacEthOamMepAisClientMegLevel,'oacEthOamMepEfdEnable':oacEthOamMepEfdEnable,'oacEthOamMepEfdState':oacEthOamMepEfdState,'oacEthOamExtGlobal':oacEthOamExtGlobal,'oacEthOamExtEnable':oacEthOamExtEnable,'oacEthOamExtLbrTable':oacEthOamExtLbrTable,'oacEthOamExtLbrEntry':oacEthOamExtLbrEntry,_U:oacEthOamLbrReceiveOrder,'oacEthOamLbrPeerMacAddress':oacEthOamLbrPeerMacAddress,'oacEthOamLbrMepId':oacEthOamLbrMepId,'oacEthOamLbrNotRespTable':oacEthOamLbrNotRespTable,'oacEthOamLbrNotRespEntry':oacEthOamLbrNotRespEntry,_V:oacEthOamLbrNotRespMepId,'oacEthOamLbrNotRespPeerMacAddress':oacEthOamLbrNotRespPeerMacAddress})