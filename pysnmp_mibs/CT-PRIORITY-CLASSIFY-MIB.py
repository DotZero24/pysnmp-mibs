_H='pClassifyUDPPortNumber'
_G='pClassifyRTPInterfaceNumber'
_F='enabled'
_E='disabled'
_D='CT-PRIORITY-CLASSIFY-MIB'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctPriorityExt,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctPriorityExt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtPriorityExtClassifyConfig_ObjectIdentity=ObjectIdentity
ctPriorityExtClassifyConfig=_CtPriorityExtClassifyConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,5))
_PClassifyRTP_ObjectIdentity=ObjectIdentity
pClassifyRTP=_PClassifyRTP_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,5,1))
class _PClassifyRTPLowDelayQueuePreference_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PClassifyRTPLowDelayQueuePreference_Type.__name__=_B
_PClassifyRTPLowDelayQueuePreference_Object=MibScalar
pClassifyRTPLowDelayQueuePreference=_PClassifyRTPLowDelayQueuePreference_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,1),_PClassifyRTPLowDelayQueuePreference_Type())
pClassifyRTPLowDelayQueuePreference.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyRTPLowDelayQueuePreference.setStatus(_A)
class _PClassifyRTCPParsing_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_PClassifyRTCPParsing_Type.__name__=_B
_PClassifyRTCPParsing_Object=MibScalar
pClassifyRTCPParsing=_PClassifyRTCPParsing_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,2),_PClassifyRTCPParsing_Type())
pClassifyRTCPParsing.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyRTCPParsing.setStatus(_A)
_PClassifyRTPTable_Object=MibTable
pClassifyRTPTable=_PClassifyRTPTable_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,3))
if mibBuilder.loadTexts:pClassifyRTPTable.setStatus(_A)
_PClassifyRTPEntry_Object=MibTableRow
pClassifyRTPEntry=_PClassifyRTPEntry_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,3,1))
pClassifyRTPEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:pClassifyRTPEntry.setStatus(_A)
_PClassifyRTPInterfaceNumber_Type=Integer32
_PClassifyRTPInterfaceNumber_Object=MibTableColumn
pClassifyRTPInterfaceNumber=_PClassifyRTPInterfaceNumber_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,3,1,1),_PClassifyRTPInterfaceNumber_Type())
pClassifyRTPInterfaceNumber.setMaxAccess('read-only')
if mibBuilder.loadTexts:pClassifyRTPInterfaceNumber.setStatus(_A)
class _PClassifyRTPState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noModification',1),('onlyQTag',2),('onlyQTOS',3),('qTagAndQTOS',4)))
_PClassifyRTPState_Type.__name__=_B
_PClassifyRTPState_Object=MibTableColumn
pClassifyRTPState=_PClassifyRTPState_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,3,1,2),_PClassifyRTPState_Type())
pClassifyRTPState.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyRTPState.setStatus(_A)
class _PClassifyRTPTOSPrecedence_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PClassifyRTPTOSPrecedence_Type.__name__=_B
_PClassifyRTPTOSPrecedence_Object=MibTableColumn
pClassifyRTPTOSPrecedence=_PClassifyRTPTOSPrecedence_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,3,1,3),_PClassifyRTPTOSPrecedence_Type())
pClassifyRTPTOSPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyRTPTOSPrecedence.setStatus(_A)
class _PClassifyRTPTagPriority_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PClassifyRTPTagPriority_Type.__name__=_B
_PClassifyRTPTagPriority_Object=MibTableColumn
pClassifyRTPTagPriority=_PClassifyRTPTagPriority_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,3,1,4),_PClassifyRTPTagPriority_Type())
pClassifyRTPTagPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyRTPTagPriority.setStatus(_A)
class _PClassifyRTPTagVID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_PClassifyRTPTagVID_Type.__name__=_B
_PClassifyRTPTagVID_Object=MibTableColumn
pClassifyRTPTagVID=_PClassifyRTPTagVID_Object((1,3,6,1,4,1,52,4,1,2,14,5,1,3,1,5),_PClassifyRTPTagVID_Type())
pClassifyRTPTagVID.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyRTPTagVID.setStatus(_A)
_PClassifyUDP_ObjectIdentity=ObjectIdentity
pClassifyUDP=_PClassifyUDP_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,14,5,2))
_PClassifyUDPTable_Object=MibTable
pClassifyUDPTable=_PClassifyUDPTable_Object((1,3,6,1,4,1,52,4,1,2,14,5,2,1))
if mibBuilder.loadTexts:pClassifyUDPTable.setStatus(_A)
_PClassifyUDPEntry_Object=MibTableRow
pClassifyUDPEntry=_PClassifyUDPEntry_Object((1,3,6,1,4,1,52,4,1,2,14,5,2,1,1))
pClassifyUDPEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:pClassifyUDPEntry.setStatus(_A)
_PClassifyUDPPortNumber_Type=Integer32
_PClassifyUDPPortNumber_Object=MibTableColumn
pClassifyUDPPortNumber=_PClassifyUDPPortNumber_Object((1,3,6,1,4,1,52,4,1,2,14,5,2,1,1,1),_PClassifyUDPPortNumber_Type())
pClassifyUDPPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyUDPPortNumber.setStatus(_A)
class _PClassifyUDPState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),('remove',3)))
_PClassifyUDPState_Type.__name__=_B
_PClassifyUDPState_Object=MibTableColumn
pClassifyUDPState=_PClassifyUDPState_Object((1,3,6,1,4,1,52,4,1,2,14,5,2,1,1,2),_PClassifyUDPState_Type())
pClassifyUDPState.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyUDPState.setStatus(_A)
class _PClassifyUDPLowDelayQueuePreference_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_PClassifyUDPLowDelayQueuePreference_Type.__name__=_B
_PClassifyUDPLowDelayQueuePreference_Object=MibTableColumn
pClassifyUDPLowDelayQueuePreference=_PClassifyUDPLowDelayQueuePreference_Object((1,3,6,1,4,1,52,4,1,2,14,5,2,1,1,3),_PClassifyUDPLowDelayQueuePreference_Type())
pClassifyUDPLowDelayQueuePreference.setMaxAccess(_C)
if mibBuilder.loadTexts:pClassifyUDPLowDelayQueuePreference.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ctPriorityExtClassifyConfig':ctPriorityExtClassifyConfig,'pClassifyRTP':pClassifyRTP,'pClassifyRTPLowDelayQueuePreference':pClassifyRTPLowDelayQueuePreference,'pClassifyRTCPParsing':pClassifyRTCPParsing,'pClassifyRTPTable':pClassifyRTPTable,'pClassifyRTPEntry':pClassifyRTPEntry,_G:pClassifyRTPInterfaceNumber,'pClassifyRTPState':pClassifyRTPState,'pClassifyRTPTOSPrecedence':pClassifyRTPTOSPrecedence,'pClassifyRTPTagPriority':pClassifyRTPTagPriority,'pClassifyRTPTagVID':pClassifyRTPTagVID,'pClassifyUDP':pClassifyUDP,'pClassifyUDPTable':pClassifyUDPTable,'pClassifyUDPEntry':pClassifyUDPEntry,_H:pClassifyUDPPortNumber,'pClassifyUDPState':pClassifyUDPState,'pClassifyUDPLowDelayQueuePreference':pClassifyUDPLowDelayQueuePreference})