_M='fsPIASnpVlanId'
_L='fsPIASnpContextId'
_K='fsPIASnpSessionMacAddress'
_J='fsPIASnpSessionVlanId'
_I='disabled'
_H='enabled'
_G='TruthValue'
_F='not-accessible'
_E='PIA-SNOOPING-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_G)
fspiasnp=ModuleIdentity((1,3,6,1,4,1,29601,2,9))
if mibBuilder.loadTexts:fspiasnp.setRevisions(('2007-11-01 00:00',))
_FsPIASnpSystem_ObjectIdentity=ObjectIdentity
fsPIASnpSystem=_FsPIASnpSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,9,1))
class _FsPIASnoopingSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsPIASnoopingSystemControl_Type.__name__=_B
_FsPIASnoopingSystemControl_Object=MibScalar
fsPIASnoopingSystemControl=_FsPIASnoopingSystemControl_Object((1,3,6,1,4,1,29601,2,9,1,1),_FsPIASnoopingSystemControl_Type())
fsPIASnoopingSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPIASnoopingSystemControl.setStatus(_A)
class _FsPIASnoopingAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsPIASnoopingAdminStatus_Type.__name__=_B
_FsPIASnoopingAdminStatus_Object=MibScalar
fsPIASnoopingAdminStatus=_FsPIASnoopingAdminStatus_Object((1,3,6,1,4,1,29601,2,9,1,2),_FsPIASnoopingAdminStatus_Type())
fsPIASnoopingAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPIASnoopingAdminStatus.setStatus(_A)
class _FsPIATraceOption_Type(Integer32):defaultValue=8
_FsPIATraceOption_Type.__name__=_B
_FsPIATraceOption_Object=MibScalar
fsPIATraceOption=_FsPIATraceOption_Object((1,3,6,1,4,1,29601,2,9,1,3),_FsPIATraceOption_Type())
fsPIATraceOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPIATraceOption.setStatus(_A)
class _FsPIASessionTimeOut_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_FsPIASessionTimeOut_Type.__name__=_B
_FsPIASessionTimeOut_Object=MibScalar
fsPIASessionTimeOut=_FsPIASessionTimeOut_Object((1,3,6,1,4,1,29601,2,9,1,4),_FsPIASessionTimeOut_Type())
fsPIASessionTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPIASessionTimeOut.setStatus(_A)
_FsPIASnpSessionTable_Object=MibTable
fsPIASnpSessionTable=_FsPIASnpSessionTable_Object((1,3,6,1,4,1,29601,2,9,1,5))
if mibBuilder.loadTexts:fsPIASnpSessionTable.setStatus(_A)
_FsPIASnpSessionEntry_Object=MibTableRow
fsPIASnpSessionEntry=_FsPIASnpSessionEntry_Object((1,3,6,1,4,1,29601,2,9,1,5,1))
fsPIASnpSessionEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:fsPIASnpSessionEntry.setStatus(_A)
class _FsPIASnpSessionVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_FsPIASnpSessionVlanId_Type.__name__=_B
_FsPIASnpSessionVlanId_Object=MibTableColumn
fsPIASnpSessionVlanId=_FsPIASnpSessionVlanId_Object((1,3,6,1,4,1,29601,2,9,1,5,1,1),_FsPIASnpSessionVlanId_Type())
fsPIASnpSessionVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPIASnpSessionVlanId.setStatus(_A)
_FsPIASnpSessionMacAddress_Type=MacAddress
_FsPIASnpSessionMacAddress_Object=MibTableColumn
fsPIASnpSessionMacAddress=_FsPIASnpSessionMacAddress_Object((1,3,6,1,4,1,29601,2,9,1,5,1,2),_FsPIASnpSessionMacAddress_Type())
fsPIASnpSessionMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPIASnpSessionMacAddress.setStatus(_A)
_FsPIASnpSessionPortId_Type=InterfaceIndex
_FsPIASnpSessionPortId_Object=MibTableColumn
fsPIASnpSessionPortId=_FsPIASnpSessionPortId_Object((1,3,6,1,4,1,29601,2,9,1,5,1,3),_FsPIASnpSessionPortId_Type())
fsPIASnpSessionPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpSessionPortId.setStatus(_A)
class _FsPIASnpSessionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpSessionId_Type.__name__=_B
_FsPIASnpSessionId_Object=MibTableColumn
fsPIASnpSessionId=_FsPIASnpSessionId_Object((1,3,6,1,4,1,29601,2,9,1,5,1,4),_FsPIASnpSessionId_Type())
fsPIASnpSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpSessionId.setStatus(_A)
_FsPIASnpVlan_ObjectIdentity=ObjectIdentity
fsPIASnpVlan=_FsPIASnpVlan_ObjectIdentity((1,3,6,1,4,1,29601,2,9,2))
_FsPIASnpVlanTable_Object=MibTable
fsPIASnpVlanTable=_FsPIASnpVlanTable_Object((1,3,6,1,4,1,29601,2,9,2,1))
if mibBuilder.loadTexts:fsPIASnpVlanTable.setStatus(_A)
_FsPIASnpVlanEntry_Object=MibTableRow
fsPIASnpVlanEntry=_FsPIASnpVlanEntry_Object((1,3,6,1,4,1,29601,2,9,2,1,1))
fsPIASnpVlanEntry.setIndexNames((0,_E,_L),(0,_E,_M))
if mibBuilder.loadTexts:fsPIASnpVlanEntry.setStatus(_A)
class _FsPIASnpContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPIASnpContextId_Type.__name__=_B
_FsPIASnpContextId_Object=MibTableColumn
fsPIASnpContextId=_FsPIASnpContextId_Object((1,3,6,1,4,1,29601,2,9,2,1,1,1),_FsPIASnpContextId_Type())
fsPIASnpContextId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPIASnpContextId.setStatus(_A)
class _FsPIASnpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsPIASnpVlanId_Type.__name__=_B
_FsPIASnpVlanId_Object=MibTableColumn
fsPIASnpVlanId=_FsPIASnpVlanId_Object((1,3,6,1,4,1,29601,2,9,2,1,1,2),_FsPIASnpVlanId_Type())
fsPIASnpVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsPIASnpVlanId.setStatus(_A)
class _FsPIASnpVlanSnpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsPIASnpVlanSnpStatus_Type.__name__=_B
_FsPIASnpVlanSnpStatus_Object=MibTableColumn
fsPIASnpVlanSnpStatus=_FsPIASnpVlanSnpStatus_Object((1,3,6,1,4,1,29601,2,9,2,1,1,3),_FsPIASnpVlanSnpStatus_Type())
fsPIASnpVlanSnpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPIASnpVlanSnpStatus.setStatus(_A)
class _FsPIASnpVlanStatsRxPADI_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsRxPADI_Type.__name__=_B
_FsPIASnpVlanStatsRxPADI_Object=MibTableColumn
fsPIASnpVlanStatsRxPADI=_FsPIASnpVlanStatsRxPADI_Object((1,3,6,1,4,1,29601,2,9,2,1,1,4),_FsPIASnpVlanStatsRxPADI_Type())
fsPIASnpVlanStatsRxPADI.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsRxPADI.setStatus(_A)
class _FsPIASnpVlanStatsRxPADO_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsRxPADO_Type.__name__=_B
_FsPIASnpVlanStatsRxPADO_Object=MibTableColumn
fsPIASnpVlanStatsRxPADO=_FsPIASnpVlanStatsRxPADO_Object((1,3,6,1,4,1,29601,2,9,2,1,1,5),_FsPIASnpVlanStatsRxPADO_Type())
fsPIASnpVlanStatsRxPADO.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsRxPADO.setStatus(_A)
class _FsPIASnpVlanStatsRxPADR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsRxPADR_Type.__name__=_B
_FsPIASnpVlanStatsRxPADR_Object=MibTableColumn
fsPIASnpVlanStatsRxPADR=_FsPIASnpVlanStatsRxPADR_Object((1,3,6,1,4,1,29601,2,9,2,1,1,6),_FsPIASnpVlanStatsRxPADR_Type())
fsPIASnpVlanStatsRxPADR.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsRxPADR.setStatus(_A)
class _FsPIASnpVlanStatsRxPADS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsRxPADS_Type.__name__=_B
_FsPIASnpVlanStatsRxPADS_Object=MibTableColumn
fsPIASnpVlanStatsRxPADS=_FsPIASnpVlanStatsRxPADS_Object((1,3,6,1,4,1,29601,2,9,2,1,1,7),_FsPIASnpVlanStatsRxPADS_Type())
fsPIASnpVlanStatsRxPADS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsRxPADS.setStatus(_A)
class _FsPIASnpVlanStatsRxPADT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsRxPADT_Type.__name__=_B
_FsPIASnpVlanStatsRxPADT_Object=MibTableColumn
fsPIASnpVlanStatsRxPADT=_FsPIASnpVlanStatsRxPADT_Object((1,3,6,1,4,1,29601,2,9,2,1,1,8),_FsPIASnpVlanStatsRxPADT_Type())
fsPIASnpVlanStatsRxPADT.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsRxPADT.setStatus(_A)
class _FsPIASnpVlanStatsTxPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsTxPkt_Type.__name__=_B
_FsPIASnpVlanStatsTxPkt_Object=MibTableColumn
fsPIASnpVlanStatsTxPkt=_FsPIASnpVlanStatsTxPkt_Object((1,3,6,1,4,1,29601,2,9,2,1,1,9),_FsPIASnpVlanStatsTxPkt_Type())
fsPIASnpVlanStatsTxPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsTxPkt.setStatus(_A)
class _FsPIASnpVlanStatsTxGenError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsTxGenError_Type.__name__=_B
_FsPIASnpVlanStatsTxGenError_Object=MibTableColumn
fsPIASnpVlanStatsTxGenError=_FsPIASnpVlanStatsTxGenError_Object((1,3,6,1,4,1,29601,2,9,2,1,1,10),_FsPIASnpVlanStatsTxGenError_Type())
fsPIASnpVlanStatsTxGenError.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsTxGenError.setStatus(_A)
class _FsPIASnpVlanStatsDroppedResUntrusted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsDroppedResUntrusted_Type.__name__=_B
_FsPIASnpVlanStatsDroppedResUntrusted_Object=MibTableColumn
fsPIASnpVlanStatsDroppedResUntrusted=_FsPIASnpVlanStatsDroppedResUntrusted_Object((1,3,6,1,4,1,29601,2,9,2,1,1,11),_FsPIASnpVlanStatsDroppedResUntrusted_Type())
fsPIASnpVlanStatsDroppedResUntrusted.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsDroppedResUntrusted.setStatus(_A)
class _FsPIASnpVlanStatsDroppedReqTrusted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsPIASnpVlanStatsDroppedReqTrusted_Type.__name__=_B
_FsPIASnpVlanStatsDroppedReqTrusted_Object=MibTableColumn
fsPIASnpVlanStatsDroppedReqTrusted=_FsPIASnpVlanStatsDroppedReqTrusted_Object((1,3,6,1,4,1,29601,2,9,2,1,1,12),_FsPIASnpVlanStatsDroppedReqTrusted_Type())
fsPIASnpVlanStatsDroppedReqTrusted.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsDroppedReqTrusted.setStatus(_A)
class _FsPIASnpVlanStatsDroppedPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPIASnpVlanStatsDroppedPkt_Type.__name__=_B
_FsPIASnpVlanStatsDroppedPkt_Object=MibTableColumn
fsPIASnpVlanStatsDroppedPkt=_FsPIASnpVlanStatsDroppedPkt_Object((1,3,6,1,4,1,29601,2,9,2,1,1,13),_FsPIASnpVlanStatsDroppedPkt_Type())
fsPIASnpVlanStatsDroppedPkt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsPIASnpVlanStatsDroppedPkt.setStatus(_A)
class _FsPIASnpVlanStatsClear_Type(TruthValue):subtypeSpec=TruthValue.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPIASnpVlanStatsClear_Type.__name__=_G
_FsPIASnpVlanStatsClear_Object=MibTableColumn
fsPIASnpVlanStatsClear=_FsPIASnpVlanStatsClear_Object((1,3,6,1,4,1,29601,2,9,2,1,1,14),_FsPIASnpVlanStatsClear_Type())
fsPIASnpVlanStatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPIASnpVlanStatsClear.setStatus(_A)
_FsPIASnpRowStatus_Type=RowStatus
_FsPIASnpRowStatus_Object=MibTableColumn
fsPIASnpRowStatus=_FsPIASnpRowStatus_Object((1,3,6,1,4,1,29601,2,9,2,1,1,15),_FsPIASnpRowStatus_Type())
fsPIASnpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPIASnpRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fspiasnp':fspiasnp,'fsPIASnpSystem':fsPIASnpSystem,'fsPIASnoopingSystemControl':fsPIASnoopingSystemControl,'fsPIASnoopingAdminStatus':fsPIASnoopingAdminStatus,'fsPIATraceOption':fsPIATraceOption,'fsPIASessionTimeOut':fsPIASessionTimeOut,'fsPIASnpSessionTable':fsPIASnpSessionTable,'fsPIASnpSessionEntry':fsPIASnpSessionEntry,_J:fsPIASnpSessionVlanId,_K:fsPIASnpSessionMacAddress,'fsPIASnpSessionPortId':fsPIASnpSessionPortId,'fsPIASnpSessionId':fsPIASnpSessionId,'fsPIASnpVlan':fsPIASnpVlan,'fsPIASnpVlanTable':fsPIASnpVlanTable,'fsPIASnpVlanEntry':fsPIASnpVlanEntry,_L:fsPIASnpContextId,_M:fsPIASnpVlanId,'fsPIASnpVlanSnpStatus':fsPIASnpVlanSnpStatus,'fsPIASnpVlanStatsRxPADI':fsPIASnpVlanStatsRxPADI,'fsPIASnpVlanStatsRxPADO':fsPIASnpVlanStatsRxPADO,'fsPIASnpVlanStatsRxPADR':fsPIASnpVlanStatsRxPADR,'fsPIASnpVlanStatsRxPADS':fsPIASnpVlanStatsRxPADS,'fsPIASnpVlanStatsRxPADT':fsPIASnpVlanStatsRxPADT,'fsPIASnpVlanStatsTxPkt':fsPIASnpVlanStatsTxPkt,'fsPIASnpVlanStatsTxGenError':fsPIASnpVlanStatsTxGenError,'fsPIASnpVlanStatsDroppedResUntrusted':fsPIASnpVlanStatsDroppedResUntrusted,'fsPIASnpVlanStatsDroppedReqTrusted':fsPIASnpVlanStatsDroppedReqTrusted,'fsPIASnpVlanStatsDroppedPkt':fsPIASnpVlanStatsDroppedPkt,'fsPIASnpVlanStatsClear':fsPIASnpVlanStatsClear,'fsPIASnpRowStatus':fsPIASnpRowStatus})