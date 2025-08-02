_I='dot1dPortPairHighPort'
_H='dot1dPortPairLowPort'
_G='disabled'
_F='dot1dSrPort'
_E='SOURCE-ROUTING-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBridge,dot1dSr=mibBuilder.importSymbols('BRIDGE-MIB','dot1dBridge','dot1dSr')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Dot1dSrPortTable_Object=MibTable
dot1dSrPortTable=_Dot1dSrPortTable_Object((1,3,6,1,2,1,17,3,1))
if mibBuilder.loadTexts:dot1dSrPortTable.setStatus(_A)
_Dot1dSrPortEntry_Object=MibTableRow
dot1dSrPortEntry=_Dot1dSrPortEntry_Object((1,3,6,1,2,1,17,3,1,1))
dot1dSrPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:dot1dSrPortEntry.setStatus(_A)
class _Dot1dSrPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1dSrPort_Type.__name__=_D
_Dot1dSrPort_Object=MibTableColumn
dot1dSrPort=_Dot1dSrPort_Object((1,3,6,1,2,1,17,3,1,1,1),_Dot1dSrPort_Type())
dot1dSrPort.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPort.setStatus(_A)
_Dot1dSrPortHopCount_Type=Integer32
_Dot1dSrPortHopCount_Object=MibTableColumn
dot1dSrPortHopCount=_Dot1dSrPortHopCount_Object((1,3,6,1,2,1,17,3,1,1,2),_Dot1dSrPortHopCount_Type())
dot1dSrPortHopCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dSrPortHopCount.setStatus(_A)
_Dot1dSrPortLocalSegment_Type=Integer32
_Dot1dSrPortLocalSegment_Object=MibTableColumn
dot1dSrPortLocalSegment=_Dot1dSrPortLocalSegment_Object((1,3,6,1,2,1,17,3,1,1,3),_Dot1dSrPortLocalSegment_Type())
dot1dSrPortLocalSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dSrPortLocalSegment.setStatus(_A)
_Dot1dSrPortBridgeNum_Type=Integer32
_Dot1dSrPortBridgeNum_Object=MibTableColumn
dot1dSrPortBridgeNum=_Dot1dSrPortBridgeNum_Object((1,3,6,1,2,1,17,3,1,1,4),_Dot1dSrPortBridgeNum_Type())
dot1dSrPortBridgeNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dSrPortBridgeNum.setStatus(_A)
_Dot1dSrPortTargetSegment_Type=Integer32
_Dot1dSrPortTargetSegment_Object=MibTableColumn
dot1dSrPortTargetSegment=_Dot1dSrPortTargetSegment_Object((1,3,6,1,2,1,17,3,1,1,5),_Dot1dSrPortTargetSegment_Type())
dot1dSrPortTargetSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dSrPortTargetSegment.setStatus(_A)
_Dot1dSrPortLargestFrame_Type=Integer32
_Dot1dSrPortLargestFrame_Object=MibTableColumn
dot1dSrPortLargestFrame=_Dot1dSrPortLargestFrame_Object((1,3,6,1,2,1,17,3,1,1,6),_Dot1dSrPortLargestFrame_Type())
dot1dSrPortLargestFrame.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dSrPortLargestFrame.setStatus(_A)
class _Dot1dSrPortSTESpanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto-span',1),(_G,2),('forced',3)))
_Dot1dSrPortSTESpanMode_Type.__name__=_D
_Dot1dSrPortSTESpanMode_Object=MibTableColumn
dot1dSrPortSTESpanMode=_Dot1dSrPortSTESpanMode_Object((1,3,6,1,2,1,17,3,1,1,7),_Dot1dSrPortSTESpanMode_Type())
dot1dSrPortSTESpanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dSrPortSTESpanMode.setStatus(_A)
_Dot1dSrPortSpecInFrames_Type=Counter32
_Dot1dSrPortSpecInFrames_Object=MibTableColumn
dot1dSrPortSpecInFrames=_Dot1dSrPortSpecInFrames_Object((1,3,6,1,2,1,17,3,1,1,8),_Dot1dSrPortSpecInFrames_Type())
dot1dSrPortSpecInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortSpecInFrames.setStatus(_A)
_Dot1dSrPortSpecOutFrames_Type=Counter32
_Dot1dSrPortSpecOutFrames_Object=MibTableColumn
dot1dSrPortSpecOutFrames=_Dot1dSrPortSpecOutFrames_Object((1,3,6,1,2,1,17,3,1,1,9),_Dot1dSrPortSpecOutFrames_Type())
dot1dSrPortSpecOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortSpecOutFrames.setStatus(_A)
_Dot1dSrPortApeInFrames_Type=Counter32
_Dot1dSrPortApeInFrames_Object=MibTableColumn
dot1dSrPortApeInFrames=_Dot1dSrPortApeInFrames_Object((1,3,6,1,2,1,17,3,1,1,10),_Dot1dSrPortApeInFrames_Type())
dot1dSrPortApeInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortApeInFrames.setStatus(_A)
_Dot1dSrPortApeOutFrames_Type=Counter32
_Dot1dSrPortApeOutFrames_Object=MibTableColumn
dot1dSrPortApeOutFrames=_Dot1dSrPortApeOutFrames_Object((1,3,6,1,2,1,17,3,1,1,11),_Dot1dSrPortApeOutFrames_Type())
dot1dSrPortApeOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortApeOutFrames.setStatus(_A)
_Dot1dSrPortSteInFrames_Type=Counter32
_Dot1dSrPortSteInFrames_Object=MibTableColumn
dot1dSrPortSteInFrames=_Dot1dSrPortSteInFrames_Object((1,3,6,1,2,1,17,3,1,1,12),_Dot1dSrPortSteInFrames_Type())
dot1dSrPortSteInFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortSteInFrames.setStatus(_A)
_Dot1dSrPortSteOutFrames_Type=Counter32
_Dot1dSrPortSteOutFrames_Object=MibTableColumn
dot1dSrPortSteOutFrames=_Dot1dSrPortSteOutFrames_Object((1,3,6,1,2,1,17,3,1,1,13),_Dot1dSrPortSteOutFrames_Type())
dot1dSrPortSteOutFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortSteOutFrames.setStatus(_A)
_Dot1dSrPortSegmentMismatchDiscards_Type=Counter32
_Dot1dSrPortSegmentMismatchDiscards_Object=MibTableColumn
dot1dSrPortSegmentMismatchDiscards=_Dot1dSrPortSegmentMismatchDiscards_Object((1,3,6,1,2,1,17,3,1,1,14),_Dot1dSrPortSegmentMismatchDiscards_Type())
dot1dSrPortSegmentMismatchDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortSegmentMismatchDiscards.setStatus(_A)
_Dot1dSrPortDuplicateSegmentDiscards_Type=Counter32
_Dot1dSrPortDuplicateSegmentDiscards_Object=MibTableColumn
dot1dSrPortDuplicateSegmentDiscards=_Dot1dSrPortDuplicateSegmentDiscards_Object((1,3,6,1,2,1,17,3,1,1,15),_Dot1dSrPortDuplicateSegmentDiscards_Type())
dot1dSrPortDuplicateSegmentDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortDuplicateSegmentDiscards.setStatus(_A)
_Dot1dSrPortHopCountExceededDiscards_Type=Counter32
_Dot1dSrPortHopCountExceededDiscards_Object=MibTableColumn
dot1dSrPortHopCountExceededDiscards=_Dot1dSrPortHopCountExceededDiscards_Object((1,3,6,1,2,1,17,3,1,1,16),_Dot1dSrPortHopCountExceededDiscards_Type())
dot1dSrPortHopCountExceededDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortHopCountExceededDiscards.setStatus(_A)
_Dot1dSrPortDupLanIdOrTreeErrors_Type=Counter32
_Dot1dSrPortDupLanIdOrTreeErrors_Object=MibTableColumn
dot1dSrPortDupLanIdOrTreeErrors=_Dot1dSrPortDupLanIdOrTreeErrors_Object((1,3,6,1,2,1,17,3,1,1,17),_Dot1dSrPortDupLanIdOrTreeErrors_Type())
dot1dSrPortDupLanIdOrTreeErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortDupLanIdOrTreeErrors.setStatus(_A)
_Dot1dSrPortLanIdMismatches_Type=Counter32
_Dot1dSrPortLanIdMismatches_Object=MibTableColumn
dot1dSrPortLanIdMismatches=_Dot1dSrPortLanIdMismatches_Object((1,3,6,1,2,1,17,3,1,1,18),_Dot1dSrPortLanIdMismatches_Type())
dot1dSrPortLanIdMismatches.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dSrPortLanIdMismatches.setStatus(_A)
class _Dot1dSrBridgeLfMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mode3',1),('mode6',2)))
_Dot1dSrBridgeLfMode_Type.__name__=_D
_Dot1dSrBridgeLfMode_Object=MibScalar
dot1dSrBridgeLfMode=_Dot1dSrBridgeLfMode_Object((1,3,6,1,2,1,17,3,2),_Dot1dSrBridgeLfMode_Type())
dot1dSrBridgeLfMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dSrBridgeLfMode.setStatus(_A)
_Dot1dPortPair_ObjectIdentity=ObjectIdentity
dot1dPortPair=_Dot1dPortPair_ObjectIdentity((1,3,6,1,2,1,17,10))
_Dot1dPortPairTableSize_Type=Gauge32
_Dot1dPortPairTableSize_Object=MibScalar
dot1dPortPairTableSize=_Dot1dPortPairTableSize_Object((1,3,6,1,2,1,17,10,1),_Dot1dPortPairTableSize_Type())
dot1dPortPairTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dot1dPortPairTableSize.setStatus(_A)
_Dot1dPortPairTable_Object=MibTable
dot1dPortPairTable=_Dot1dPortPairTable_Object((1,3,6,1,2,1,17,10,2))
if mibBuilder.loadTexts:dot1dPortPairTable.setStatus(_A)
_Dot1dPortPairEntry_Object=MibTableRow
dot1dPortPairEntry=_Dot1dPortPairEntry_Object((1,3,6,1,2,1,17,10,2,1))
dot1dPortPairEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:dot1dPortPairEntry.setStatus(_A)
class _Dot1dPortPairLowPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1dPortPairLowPort_Type.__name__=_D
_Dot1dPortPairLowPort_Object=MibTableColumn
dot1dPortPairLowPort=_Dot1dPortPairLowPort_Object((1,3,6,1,2,1,17,10,2,1,1),_Dot1dPortPairLowPort_Type())
dot1dPortPairLowPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortPairLowPort.setStatus(_A)
class _Dot1dPortPairHighPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot1dPortPairHighPort_Type.__name__=_D
_Dot1dPortPairHighPort_Object=MibTableColumn
dot1dPortPairHighPort=_Dot1dPortPairHighPort_Object((1,3,6,1,2,1,17,10,2,1,2),_Dot1dPortPairHighPort_Type())
dot1dPortPairHighPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortPairHighPort.setStatus(_A)
_Dot1dPortPairBridgeNum_Type=Integer32
_Dot1dPortPairBridgeNum_Object=MibTableColumn
dot1dPortPairBridgeNum=_Dot1dPortPairBridgeNum_Object((1,3,6,1,2,1,17,10,2,1,3),_Dot1dPortPairBridgeNum_Type())
dot1dPortPairBridgeNum.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortPairBridgeNum.setStatus(_A)
class _Dot1dPortPairBridgeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enabled',1),(_G,2),('invalid',3)))
_Dot1dPortPairBridgeState_Type.__name__=_D
_Dot1dPortPairBridgeState_Object=MibTableColumn
dot1dPortPairBridgeState=_Dot1dPortPairBridgeState_Object((1,3,6,1,2,1,17,10,2,1,4),_Dot1dPortPairBridgeState_Type())
dot1dPortPairBridgeState.setMaxAccess(_C)
if mibBuilder.loadTexts:dot1dPortPairBridgeState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'dot1dSrPortTable':dot1dSrPortTable,'dot1dSrPortEntry':dot1dSrPortEntry,_F:dot1dSrPort,'dot1dSrPortHopCount':dot1dSrPortHopCount,'dot1dSrPortLocalSegment':dot1dSrPortLocalSegment,'dot1dSrPortBridgeNum':dot1dSrPortBridgeNum,'dot1dSrPortTargetSegment':dot1dSrPortTargetSegment,'dot1dSrPortLargestFrame':dot1dSrPortLargestFrame,'dot1dSrPortSTESpanMode':dot1dSrPortSTESpanMode,'dot1dSrPortSpecInFrames':dot1dSrPortSpecInFrames,'dot1dSrPortSpecOutFrames':dot1dSrPortSpecOutFrames,'dot1dSrPortApeInFrames':dot1dSrPortApeInFrames,'dot1dSrPortApeOutFrames':dot1dSrPortApeOutFrames,'dot1dSrPortSteInFrames':dot1dSrPortSteInFrames,'dot1dSrPortSteOutFrames':dot1dSrPortSteOutFrames,'dot1dSrPortSegmentMismatchDiscards':dot1dSrPortSegmentMismatchDiscards,'dot1dSrPortDuplicateSegmentDiscards':dot1dSrPortDuplicateSegmentDiscards,'dot1dSrPortHopCountExceededDiscards':dot1dSrPortHopCountExceededDiscards,'dot1dSrPortDupLanIdOrTreeErrors':dot1dSrPortDupLanIdOrTreeErrors,'dot1dSrPortLanIdMismatches':dot1dSrPortLanIdMismatches,'dot1dSrBridgeLfMode':dot1dSrBridgeLfMode,'dot1dPortPair':dot1dPortPair,'dot1dPortPairTableSize':dot1dPortPairTableSize,'dot1dPortPairTable':dot1dPortPairTable,'dot1dPortPairEntry':dot1dPortPairEntry,_H:dot1dPortPairLowPort,_I:dot1dPortPairHighPort,'dot1dPortPairBridgeNum':dot1dPortPairBridgeNum,'dot1dPortPairBridgeState':dot1dPortPairBridgeState})