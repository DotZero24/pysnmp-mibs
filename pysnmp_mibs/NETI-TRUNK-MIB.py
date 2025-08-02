_G='dppipIndex'
_F='NETI-TRUNK-MIB'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netiGeneric,=mibBuilder.importSymbols('NETI-COMMON-MIB','netiGeneric')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowPointer,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TimeStamp','TruthValue')
netiTrunkMIB=ModuleIdentity((1,3,6,1,4,1,2928,2,3))
if mibBuilder.loadTexts:netiTrunkMIB.setRevisions(('2014-03-14 08:00','2013-08-29 16:00','2013-01-24 15:00','2009-08-26 15:00'))
class FecMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fecNone',1),('fec1D',2),('fec2D',3)))
class DppipSupport(TextualConvention,OctetString):status=_A;displayHint='1d.1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_TrunkObjects_ObjectIdentity=ObjectIdentity
trunkObjects=_TrunkObjects_ObjectIdentity((1,3,6,1,4,1,2928,2,3,1))
_DppipGroup_ObjectIdentity=ObjectIdentity
dppipGroup=_DppipGroup_ObjectIdentity((1,3,6,1,4,1,2928,2,3,1,1))
_DppipNumber_Type=Integer32
_DppipNumber_Object=MibScalar
dppipNumber=_DppipNumber_Object((1,3,6,1,4,1,2928,2,3,1,1,1),_DppipNumber_Type())
dppipNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipNumber.setStatus(_A)
_DppipLastChange_Type=TimeStamp
_DppipLastChange_Object=MibScalar
dppipLastChange=_DppipLastChange_Object((1,3,6,1,4,1,2928,2,3,1,1,2),_DppipLastChange_Type())
dppipLastChange.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipLastChange.setStatus(_A)
_DppipTable_Object=MibTable
dppipTable=_DppipTable_Object((1,3,6,1,4,1,2928,2,3,1,1,3))
if mibBuilder.loadTexts:dppipTable.setStatus(_A)
_DppipEntry_Object=MibTableRow
dppipEntry=_DppipEntry_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1))
dppipEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dppipEntry.setStatus(_A)
_DppipIndex_Type=Unsigned32
_DppipIndex_Object=MibTableColumn
dppipIndex=_DppipIndex_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,1),_DppipIndex_Type())
dppipIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dppipIndex.setStatus(_A)
_DppipName_Type=SnmpAdminString
_DppipName_Object=MibTableColumn
dppipName=_DppipName_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,2),_DppipName_Type())
dppipName.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipName.setStatus(_A)
_DppipAddress_Type=IpAddress
_DppipAddress_Object=MibTableColumn
dppipAddress=_DppipAddress_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,3),_DppipAddress_Type())
dppipAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipAddress.setStatus(_A)
_DppipNetMask_Type=IpAddress
_DppipNetMask_Object=MibTableColumn
dppipNetMask=_DppipNetMask_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,4),_DppipNetMask_Type())
dppipNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipNetMask.setStatus(_A)
_DppipDefaultGateway_Type=IpAddress
_DppipDefaultGateway_Object=MibTableColumn
dppipDefaultGateway=_DppipDefaultGateway_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,5),_DppipDefaultGateway_Type())
dppipDefaultGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipDefaultGateway.setStatus(_A)
_DppipPeerAddress_Type=IpAddress
_DppipPeerAddress_Object=MibTableColumn
dppipPeerAddress=_DppipPeerAddress_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,6),_DppipPeerAddress_Type())
dppipPeerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipPeerAddress.setStatus(_A)
_DppipTxSlots_Type=Unsigned32
_DppipTxSlots_Object=MibTableColumn
dppipTxSlots=_DppipTxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,7),_DppipTxSlots_Type())
dppipTxSlots.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipTxSlots.setStatus(_A)
_DppipTxUsedCapacity_Type=Gauge32
_DppipTxUsedCapacity_Object=MibTableColumn
dppipTxUsedCapacity=_DppipTxUsedCapacity_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,8),_DppipTxUsedCapacity_Type())
dppipTxUsedCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipTxUsedCapacity.setStatus(_A)
_DppipRxSlots_Type=Gauge32
_DppipRxSlots_Object=MibTableColumn
dppipRxSlots=_DppipRxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,9),_DppipRxSlots_Type())
dppipRxSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRxSlots.setStatus(_A)
_DppipRxUsedCapacity_Type=Gauge32
_DppipRxUsedCapacity_Object=MibTableColumn
dppipRxUsedCapacity=_DppipRxUsedCapacity_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,10),_DppipRxUsedCapacity_Type())
dppipRxUsedCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRxUsedCapacity.setStatus(_A)
_DppipDelayVariation_Type=Unsigned32
_DppipDelayVariation_Object=MibTableColumn
dppipDelayVariation=_DppipDelayVariation_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,11),_DppipDelayVariation_Type())
dppipDelayVariation.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDelayVariation.setStatus(_A)
class _DppipOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3),('unknown',4),('dormant',5),('notPresent',6),('lowerLayerDown',7)))
_DppipOperStatus_Type.__name__=_E
_DppipOperStatus_Object=MibTableColumn
dppipOperStatus=_DppipOperStatus_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,12),_DppipOperStatus_Type())
dppipOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipOperStatus.setStatus(_A)
_DppipFailure_Type=SnmpAdminString
_DppipFailure_Object=MibTableColumn
dppipFailure=_DppipFailure_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,13),_DppipFailure_Type())
dppipFailure.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipFailure.setStatus(_A)
_DppipReceivedFrames_Type=Counter64
_DppipReceivedFrames_Object=MibTableColumn
dppipReceivedFrames=_DppipReceivedFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,14),_DppipReceivedFrames_Type())
dppipReceivedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipReceivedFrames.setStatus(_A)
_DppipMissingFrames_Type=Counter64
_DppipMissingFrames_Object=MibTableColumn
dppipMissingFrames=_DppipMissingFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,15),_DppipMissingFrames_Type())
dppipMissingFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMissingFrames.setStatus(_A)
_DppipDeliveredFrames_Type=Counter64
_DppipDeliveredFrames_Object=MibTableColumn
dppipDeliveredFrames=_DppipDeliveredFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,16),_DppipDeliveredFrames_Type())
dppipDeliveredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDeliveredFrames.setStatus(_A)
_DppipDroppedFrames_Type=Counter64
_DppipDroppedFrames_Object=MibTableColumn
dppipDroppedFrames=_DppipDroppedFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,17),_DppipDroppedFrames_Type())
dppipDroppedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDroppedFrames.setStatus(_A)
_DppipDuplicateFrames_Type=Counter64
_DppipDuplicateFrames_Object=MibTableColumn
dppipDuplicateFrames=_DppipDuplicateFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,18),_DppipDuplicateFrames_Type())
dppipDuplicateFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDuplicateFrames.setStatus(_A)
_DppipReorderedFrames_Type=Counter64
_DppipReorderedFrames_Object=MibTableColumn
dppipReorderedFrames=_DppipReorderedFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,19),_DppipReorderedFrames_Type())
dppipReorderedFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipReorderedFrames.setStatus(_A)
_DppipLostFrames_Type=Counter64
_DppipLostFrames_Object=MibTableColumn
dppipLostFrames=_DppipLostFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,20),_DppipLostFrames_Type())
dppipLostFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipLostFrames.setStatus(_A)
_DppipRecoveredFrames_Type=Counter64
_DppipRecoveredFrames_Object=MibTableColumn
dppipRecoveredFrames=_DppipRecoveredFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,21),_DppipRecoveredFrames_Type())
dppipRecoveredFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRecoveredFrames.setStatus(_A)
_DppipSentFrames_Type=Counter64
_DppipSentFrames_Object=MibTableColumn
dppipSentFrames=_DppipSentFrames_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,22),_DppipSentFrames_Type())
dppipSentFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipSentFrames.setStatus(_A)
_DppipDelayVarPtp_Type=Unsigned32
_DppipDelayVarPtp_Object=MibTableColumn
dppipDelayVarPtp=_DppipDelayVarPtp_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,23),_DppipDelayVarPtp_Type())
dppipDelayVarPtp.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDelayVarPtp.setStatus(_A)
_DppipDelayVar999_Type=Unsigned32
_DppipDelayVar999_Object=MibTableColumn
dppipDelayVar999=_DppipDelayVar999_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,24),_DppipDelayVar999_Type())
dppipDelayVar999.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDelayVar999.setStatus(_A)
class _DppipAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_DppipAdminStatus_Type.__name__=_E
_DppipAdminStatus_Object=MibTableColumn
dppipAdminStatus=_DppipAdminStatus_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,25),_DppipAdminStatus_Type())
dppipAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipAdminStatus.setStatus(_A)
class _DppipVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,4095))
_DppipVlan_Type.__name__=_E
_DppipVlan_Object=MibTableColumn
dppipVlan=_DppipVlan_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,26),_DppipVlan_Type())
dppipVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipVlan.setStatus(_A)
_DppipDelayVar01_Type=Unsigned32
_DppipDelayVar01_Object=MibTableColumn
dppipDelayVar01=_DppipDelayVar01_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,27),_DppipDelayVar01_Type())
dppipDelayVar01.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDelayVar01.setStatus(_A)
class _DppipPrio_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_DppipPrio_Type.__name__=_D
_DppipPrio_Object=MibTableColumn
dppipPrio=_DppipPrio_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,28),_DppipPrio_Type())
dppipPrio.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipPrio.setStatus(_A)
_DppipPhysIf_Type=RowPointer
_DppipPhysIf_Object=MibTableColumn
dppipPhysIf=_DppipPhysIf_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,29),_DppipPhysIf_Type())
dppipPhysIf.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPhysIf.setStatus(_A)
class _DppipMtu_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1500))
_DppipMtu_Type.__name__=_D
_DppipMtu_Object=MibTableColumn
dppipMtu=_DppipMtu_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,30),_DppipMtu_Type())
dppipMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipMtu.setStatus(_A)
class _DppipTtl_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_DppipTtl_Type.__name__=_D
_DppipTtl_Object=MibTableColumn
dppipTtl=_DppipTtl_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,31),_DppipTtl_Type())
dppipTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipTtl.setStatus(_A)
class _DppipDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_DppipDscp_Type.__name__=_D
_DppipDscp_Object=MibTableColumn
dppipDscp=_DppipDscp_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,32),_DppipDscp_Type())
dppipDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipDscp.setStatus(_A)
_DppipRxSlotsPerFrame_Type=Unsigned32
_DppipRxSlotsPerFrame_Object=MibTableColumn
dppipRxSlotsPerFrame=_DppipRxSlotsPerFrame_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,33),_DppipRxSlotsPerFrame_Type())
dppipRxSlotsPerFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRxSlotsPerFrame.setStatus(_A)
_DppipAvailTxSlots_Type=Gauge32
_DppipAvailTxSlots_Object=MibTableColumn
dppipAvailTxSlots=_DppipAvailTxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,34),_DppipAvailTxSlots_Type())
dppipAvailTxSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipAvailTxSlots.setStatus(_A)
_DppipAvailRxSlots_Type=Gauge32
_DppipAvailRxSlots_Object=MibTableColumn
dppipAvailRxSlots=_DppipAvailRxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,35),_DppipAvailRxSlots_Type())
dppipAvailRxSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipAvailRxSlots.setStatus(_A)
_DppipMinUsageRatio_Type=Unsigned32
_DppipMinUsageRatio_Object=MibTableColumn
dppipMinUsageRatio=_DppipMinUsageRatio_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,36),_DppipMinUsageRatio_Type())
dppipMinUsageRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipMinUsageRatio.setStatus(_A)
_DppipTxTranspSlots_Type=Gauge32
_DppipTxTranspSlots_Object=MibTableColumn
dppipTxTranspSlots=_DppipTxTranspSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,37),_DppipTxTranspSlots_Type())
dppipTxTranspSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipTxTranspSlots.setStatus(_A)
_DppipRxTranspSlots_Type=Gauge32
_DppipRxTranspSlots_Object=MibTableColumn
dppipRxTranspSlots=_DppipRxTranspSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,38),_DppipRxTranspSlots_Type())
dppipRxTranspSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRxTranspSlots.setStatus(_A)
_DppipNomDTDelay_Type=Unsigned32
_DppipNomDTDelay_Object=MibTableColumn
dppipNomDTDelay=_DppipNomDTDelay_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,39),_DppipNomDTDelay_Type())
dppipNomDTDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipNomDTDelay.setStatus(_A)
_DppipTxFecMode_Type=FecMode
_DppipTxFecMode_Object=MibTableColumn
dppipTxFecMode=_DppipTxFecMode_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,40),_DppipTxFecMode_Type())
dppipTxFecMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipTxFecMode.setStatus(_A)
_DppipTxFecRows_Type=Unsigned32
_DppipTxFecRows_Object=MibTableColumn
dppipTxFecRows=_DppipTxFecRows_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,41),_DppipTxFecRows_Type())
dppipTxFecRows.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipTxFecRows.setStatus(_A)
_DppipTxFecCols_Type=Unsigned32
_DppipTxFecCols_Object=MibTableColumn
dppipTxFecCols=_DppipTxFecCols_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,42),_DppipTxFecCols_Type())
dppipTxFecCols.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipTxFecCols.setStatus(_A)
_DppipRxFecMode_Type=FecMode
_DppipRxFecMode_Object=MibTableColumn
dppipRxFecMode=_DppipRxFecMode_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,43),_DppipRxFecMode_Type())
dppipRxFecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRxFecMode.setStatus(_A)
_DppipRxFecRows_Type=Unsigned32
_DppipRxFecRows_Object=MibTableColumn
dppipRxFecRows=_DppipRxFecRows_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,44),_DppipRxFecRows_Type())
dppipRxFecRows.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRxFecRows.setStatus(_A)
_DppipRxFecCols_Type=Unsigned32
_DppipRxFecCols_Object=MibTableColumn
dppipRxFecCols=_DppipRxFecCols_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,45),_DppipRxFecCols_Type())
dppipRxFecCols.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipRxFecCols.setStatus(_A)
class _DppipCntControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_DppipCntControl_Type.__name__=_E
_DppipCntControl_Object=MibTableColumn
dppipCntControl=_DppipCntControl_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,46),_DppipCntControl_Type())
dppipCntControl.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipCntControl.setStatus(_A)
_DppipSuppressAlarms_Type=TruthValue
_DppipSuppressAlarms_Object=MibTableColumn
dppipSuppressAlarms=_DppipSuppressAlarms_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,47),_DppipSuppressAlarms_Type())
dppipSuppressAlarms.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipSuppressAlarms.setStatus(_A)
class _DppipSigFailFilter_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000))
_DppipSigFailFilter_Type.__name__=_D
_DppipSigFailFilter_Object=MibTableColumn
dppipSigFailFilter=_DppipSigFailFilter_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,48),_DppipSigFailFilter_Type())
dppipSigFailFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipSigFailFilter.setStatus(_A)
class _DppipDegThreshold_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8000))
_DppipDegThreshold_Type.__name__=_D
_DppipDegThreshold_Object=MibTableColumn
dppipDegThreshold=_DppipDegThreshold_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,49),_DppipDegThreshold_Type())
dppipDegThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipDegThreshold.setStatus(_A)
class _DppipDegPeriod_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_DppipDegPeriod_Type.__name__=_D
_DppipDegPeriod_Object=MibTableColumn
dppipDegPeriod=_DppipDegPeriod_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,50),_DppipDegPeriod_Type())
dppipDegPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipDegPeriod.setStatus(_A)
_DppipTolJitter_Type=Unsigned32
_DppipTolJitter_Object=MibTableColumn
dppipTolJitter=_DppipTolJitter_Object((1,3,6,1,4,1,2928,2,3,1,1,3,1,51),_DppipTolJitter_Type())
dppipTolJitter.setMaxAccess(_C)
if mibBuilder.loadTexts:dppipTolJitter.setStatus(_A)
_DppipLimitsTable_Object=MibTable
dppipLimitsTable=_DppipLimitsTable_Object((1,3,6,1,4,1,2928,2,3,1,1,4))
if mibBuilder.loadTexts:dppipLimitsTable.setStatus(_A)
_DppipLimitsEntry_Object=MibTableRow
dppipLimitsEntry=_DppipLimitsEntry_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1))
dppipLimitsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dppipLimitsEntry.setStatus(_A)
_DppipMaxFecMode_Type=FecMode
_DppipMaxFecMode_Object=MibTableColumn
dppipMaxFecMode=_DppipMaxFecMode_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,1),_DppipMaxFecMode_Type())
dppipMaxFecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMaxFecMode.setStatus(_A)
_DppipMaxFecRows_Type=Unsigned32
_DppipMaxFecRows_Object=MibTableColumn
dppipMaxFecRows=_DppipMaxFecRows_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,2),_DppipMaxFecRows_Type())
dppipMaxFecRows.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMaxFecRows.setStatus(_A)
_DppipMinFecRows_Type=Unsigned32
_DppipMinFecRows_Object=MibTableColumn
dppipMinFecRows=_DppipMinFecRows_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,3),_DppipMinFecRows_Type())
dppipMinFecRows.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMinFecRows.setStatus(_A)
_DppipMaxFecCols_Type=Unsigned32
_DppipMaxFecCols_Object=MibTableColumn
dppipMaxFecCols=_DppipMaxFecCols_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,4),_DppipMaxFecCols_Type())
dppipMaxFecCols.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMaxFecCols.setStatus(_A)
_DppipMinFecCols_Type=Unsigned32
_DppipMinFecCols_Object=MibTableColumn
dppipMinFecCols=_DppipMinFecCols_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,5),_DppipMinFecCols_Type())
dppipMinFecCols.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMinFecCols.setStatus(_A)
_DppipMaxFecElems_Type=Unsigned32
_DppipMaxFecElems_Object=MibTableColumn
dppipMaxFecElems=_DppipMaxFecElems_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,6),_DppipMaxFecElems_Type())
dppipMaxFecElems.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMaxFecElems.setStatus(_A)
_DppipMaxTxSlots_Type=Unsigned32
_DppipMaxTxSlots_Object=MibTableColumn
dppipMaxTxSlots=_DppipMaxTxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,7),_DppipMaxTxSlots_Type())
dppipMaxTxSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMaxTxSlots.setStatus(_A)
_DppipMinTxSlots_Type=Unsigned32
_DppipMinTxSlots_Object=MibTableColumn
dppipMinTxSlots=_DppipMinTxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,8),_DppipMinTxSlots_Type())
dppipMinTxSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMinTxSlots.setStatus(_A)
_DppipMaxTolJitter_Type=Unsigned32
_DppipMaxTolJitter_Object=MibTableColumn
dppipMaxTolJitter=_DppipMaxTolJitter_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,9),_DppipMaxTolJitter_Type())
dppipMaxTolJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMaxTolJitter.setStatus(_A)
_DppipMinTolJitter_Type=Unsigned32
_DppipMinTolJitter_Object=MibTableColumn
dppipMinTolJitter=_DppipMinTolJitter_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,10),_DppipMinTolJitter_Type())
dppipMinTolJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipMinTolJitter.setStatus(_A)
_DppipDTSupport_Type=DppipSupport
_DppipDTSupport_Object=MibTableColumn
dppipDTSupport=_DppipDTSupport_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,11),_DppipDTSupport_Type())
dppipDTSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipDTSupport.setStatus(_A)
_DppipTTSupport_Type=DppipSupport
_DppipTTSupport_Object=MibTableColumn
dppipTTSupport=_DppipTTSupport_Object((1,3,6,1,4,1,2928,2,3,1,1,4,1,12),_DppipTTSupport_Type())
dppipTTSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipTTSupport.setStatus(_A)
_DppipPeerLimitsTable_Object=MibTable
dppipPeerLimitsTable=_DppipPeerLimitsTable_Object((1,3,6,1,4,1,2928,2,3,1,1,5))
if mibBuilder.loadTexts:dppipPeerLimitsTable.setStatus(_A)
_DppipPeerLimitsEntry_Object=MibTableRow
dppipPeerLimitsEntry=_DppipPeerLimitsEntry_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1))
dppipPeerLimitsEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:dppipPeerLimitsEntry.setStatus(_A)
_DppipPeerMaxFecMode_Type=FecMode
_DppipPeerMaxFecMode_Object=MibTableColumn
dppipPeerMaxFecMode=_DppipPeerMaxFecMode_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,1),_DppipPeerMaxFecMode_Type())
dppipPeerMaxFecMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMaxFecMode.setStatus(_A)
_DppipPeerMaxFecRows_Type=Unsigned32
_DppipPeerMaxFecRows_Object=MibTableColumn
dppipPeerMaxFecRows=_DppipPeerMaxFecRows_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,2),_DppipPeerMaxFecRows_Type())
dppipPeerMaxFecRows.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMaxFecRows.setStatus(_A)
_DppipPeerMinFecRows_Type=Unsigned32
_DppipPeerMinFecRows_Object=MibTableColumn
dppipPeerMinFecRows=_DppipPeerMinFecRows_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,3),_DppipPeerMinFecRows_Type())
dppipPeerMinFecRows.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMinFecRows.setStatus(_A)
_DppipPeerMaxFecCols_Type=Unsigned32
_DppipPeerMaxFecCols_Object=MibTableColumn
dppipPeerMaxFecCols=_DppipPeerMaxFecCols_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,4),_DppipPeerMaxFecCols_Type())
dppipPeerMaxFecCols.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMaxFecCols.setStatus(_A)
_DppipPeerMinFecCols_Type=Unsigned32
_DppipPeerMinFecCols_Object=MibTableColumn
dppipPeerMinFecCols=_DppipPeerMinFecCols_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,5),_DppipPeerMinFecCols_Type())
dppipPeerMinFecCols.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMinFecCols.setStatus(_A)
_DppipPeerMaxFecElems_Type=Unsigned32
_DppipPeerMaxFecElems_Object=MibTableColumn
dppipPeerMaxFecElems=_DppipPeerMaxFecElems_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,6),_DppipPeerMaxFecElems_Type())
dppipPeerMaxFecElems.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMaxFecElems.setStatus(_A)
_DppipPeerMaxRxSlots_Type=Unsigned32
_DppipPeerMaxRxSlots_Object=MibTableColumn
dppipPeerMaxRxSlots=_DppipPeerMaxRxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,7),_DppipPeerMaxRxSlots_Type())
dppipPeerMaxRxSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMaxRxSlots.setStatus(_A)
_DppipPeerMinRxSlots_Type=Unsigned32
_DppipPeerMinRxSlots_Object=MibTableColumn
dppipPeerMinRxSlots=_DppipPeerMinRxSlots_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,8),_DppipPeerMinRxSlots_Type())
dppipPeerMinRxSlots.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerMinRxSlots.setStatus(_A)
_DppipPeerDTSupport_Type=DppipSupport
_DppipPeerDTSupport_Object=MibTableColumn
dppipPeerDTSupport=_DppipPeerDTSupport_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,9),_DppipPeerDTSupport_Type())
dppipPeerDTSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerDTSupport.setStatus(_A)
_DppipPeerTTSupport_Type=DppipSupport
_DppipPeerTTSupport_Object=MibTableColumn
dppipPeerTTSupport=_DppipPeerTTSupport_Object((1,3,6,1,4,1,2928,2,3,1,1,5,1,10),_DppipPeerTTSupport_Type())
dppipPeerTTSupport.setMaxAccess(_B)
if mibBuilder.loadTexts:dppipPeerTTSupport.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'FecMode':FecMode,'DppipSupport':DppipSupport,'netiTrunkMIB':netiTrunkMIB,'trunkObjects':trunkObjects,'dppipGroup':dppipGroup,'dppipNumber':dppipNumber,'dppipLastChange':dppipLastChange,'dppipTable':dppipTable,'dppipEntry':dppipEntry,_G:dppipIndex,'dppipName':dppipName,'dppipAddress':dppipAddress,'dppipNetMask':dppipNetMask,'dppipDefaultGateway':dppipDefaultGateway,'dppipPeerAddress':dppipPeerAddress,'dppipTxSlots':dppipTxSlots,'dppipTxUsedCapacity':dppipTxUsedCapacity,'dppipRxSlots':dppipRxSlots,'dppipRxUsedCapacity':dppipRxUsedCapacity,'dppipDelayVariation':dppipDelayVariation,'dppipOperStatus':dppipOperStatus,'dppipFailure':dppipFailure,'dppipReceivedFrames':dppipReceivedFrames,'dppipMissingFrames':dppipMissingFrames,'dppipDeliveredFrames':dppipDeliveredFrames,'dppipDroppedFrames':dppipDroppedFrames,'dppipDuplicateFrames':dppipDuplicateFrames,'dppipReorderedFrames':dppipReorderedFrames,'dppipLostFrames':dppipLostFrames,'dppipRecoveredFrames':dppipRecoveredFrames,'dppipSentFrames':dppipSentFrames,'dppipDelayVarPtp':dppipDelayVarPtp,'dppipDelayVar999':dppipDelayVar999,'dppipAdminStatus':dppipAdminStatus,'dppipVlan':dppipVlan,'dppipDelayVar01':dppipDelayVar01,'dppipPrio':dppipPrio,'dppipPhysIf':dppipPhysIf,'dppipMtu':dppipMtu,'dppipTtl':dppipTtl,'dppipDscp':dppipDscp,'dppipRxSlotsPerFrame':dppipRxSlotsPerFrame,'dppipAvailTxSlots':dppipAvailTxSlots,'dppipAvailRxSlots':dppipAvailRxSlots,'dppipMinUsageRatio':dppipMinUsageRatio,'dppipTxTranspSlots':dppipTxTranspSlots,'dppipRxTranspSlots':dppipRxTranspSlots,'dppipNomDTDelay':dppipNomDTDelay,'dppipTxFecMode':dppipTxFecMode,'dppipTxFecRows':dppipTxFecRows,'dppipTxFecCols':dppipTxFecCols,'dppipRxFecMode':dppipRxFecMode,'dppipRxFecRows':dppipRxFecRows,'dppipRxFecCols':dppipRxFecCols,'dppipCntControl':dppipCntControl,'dppipSuppressAlarms':dppipSuppressAlarms,'dppipSigFailFilter':dppipSigFailFilter,'dppipDegThreshold':dppipDegThreshold,'dppipDegPeriod':dppipDegPeriod,'dppipTolJitter':dppipTolJitter,'dppipLimitsTable':dppipLimitsTable,'dppipLimitsEntry':dppipLimitsEntry,'dppipMaxFecMode':dppipMaxFecMode,'dppipMaxFecRows':dppipMaxFecRows,'dppipMinFecRows':dppipMinFecRows,'dppipMaxFecCols':dppipMaxFecCols,'dppipMinFecCols':dppipMinFecCols,'dppipMaxFecElems':dppipMaxFecElems,'dppipMaxTxSlots':dppipMaxTxSlots,'dppipMinTxSlots':dppipMinTxSlots,'dppipMaxTolJitter':dppipMaxTolJitter,'dppipMinTolJitter':dppipMinTolJitter,'dppipDTSupport':dppipDTSupport,'dppipTTSupport':dppipTTSupport,'dppipPeerLimitsTable':dppipPeerLimitsTable,'dppipPeerLimitsEntry':dppipPeerLimitsEntry,'dppipPeerMaxFecMode':dppipPeerMaxFecMode,'dppipPeerMaxFecRows':dppipPeerMaxFecRows,'dppipPeerMinFecRows':dppipPeerMinFecRows,'dppipPeerMaxFecCols':dppipPeerMaxFecCols,'dppipPeerMinFecCols':dppipPeerMinFecCols,'dppipPeerMaxFecElems':dppipPeerMaxFecElems,'dppipPeerMaxRxSlots':dppipPeerMaxRxSlots,'dppipPeerMinRxSlots':dppipPeerMinRxSlots,'dppipPeerDTSupport':dppipPeerDTSupport,'dppipPeerTTSupport':dppipPeerTTSupport})