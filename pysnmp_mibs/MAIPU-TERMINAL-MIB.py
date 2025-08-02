_H='mpTermRHStateRHIndex'
_G='mpTermRHStateInterface'
_F='mpTermStateInterface'
_E='MAIPU-TERMINAL-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
mpTerminalMib=ModuleIdentity((1,3,6,1,4,1,5651,3,602))
if mibBuilder.loadTexts:mpTerminalMib.setRevisions(('2007-03-14 15:07',))
_MpTermMIBObjects_ObjectIdentity=ObjectIdentity
mpTermMIBObjects=_MpTermMIBObjects_ObjectIdentity((1,3,6,1,4,1,5651,3,602,1))
_MpTermConfigs_ObjectIdentity=ObjectIdentity
mpTermConfigs=_MpTermConfigs_ObjectIdentity((1,3,6,1,4,1,5651,3,602,1,1))
_MpTermInfo_ObjectIdentity=ObjectIdentity
mpTermInfo=_MpTermInfo_ObjectIdentity((1,3,6,1,4,1,5651,3,602,1,2))
_MpTermStateTable_Object=MibTable
mpTermStateTable=_MpTermStateTable_Object((1,3,6,1,4,1,5651,3,602,1,2,1))
if mibBuilder.loadTexts:mpTermStateTable.setStatus(_A)
_MpTermStateEntry_Object=MibTableRow
mpTermStateEntry=_MpTermStateEntry_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1))
mpTermStateEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mpTermStateEntry.setStatus(_A)
class _MpTermStateInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,59))
_MpTermStateInterface_Type.__name__=_D
_MpTermStateInterface_Object=MibTableColumn
mpTermStateInterface=_MpTermStateInterface_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,1),_MpTermStateInterface_Type())
mpTermStateInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateInterface.setStatus(_A)
class _MpTermStateTermType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('terminal',1),('mpdlc',2),('pad',3)))
_MpTermStateTermType_Type.__name__=_C
_MpTermStateTermType_Object=MibTableColumn
mpTermStateTermType=_MpTermStateTermType_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,2),_MpTermStateTermType_Type())
mpTermStateTermType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateTermType.setStatus(_A)
_MpTermStateCOM_Type=Integer32
_MpTermStateCOM_Object=MibTableColumn
mpTermStateCOM=_MpTermStateCOM_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,3),_MpTermStateCOM_Type())
mpTermStateCOM.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateCOM.setStatus(_A)
_MpTermStateTERM_Type=Integer32
_MpTermStateTERM_Object=MibTableColumn
mpTermStateTERM=_MpTermStateTERM_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,4),_MpTermStateTERM_Type())
mpTermStateTERM.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateTERM.setStatus(_A)
class _MpTermStateTcpServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpTermStateTcpServerPort_Type.__name__=_C
_MpTermStateTcpServerPort_Object=MibTableColumn
mpTermStateTcpServerPort=_MpTermStateTcpServerPort_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,5),_MpTermStateTcpServerPort_Type())
mpTermStateTcpServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateTcpServerPort.setStatus(_A)
class _MpTermStateTerminalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('closed',1),('initial',2),('prompt',3),('running',4),('waiting',5)))
_MpTermStateTerminalState_Type.__name__=_C
_MpTermStateTerminalState_Object=MibTableColumn
mpTermStateTerminalState=_MpTermStateTerminalState_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,6),_MpTermStateTerminalState_Type())
mpTermStateTerminalState.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateTerminalState.setStatus(_A)
class _MpTermStateTemplateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpTermStateTemplateName_Type.__name__=_D
_MpTermStateTemplateName_Object=MibTableColumn
mpTermStateTemplateName=_MpTermStateTemplateName_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,7),_MpTermStateTemplateName_Type())
mpTermStateTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateTemplateName.setStatus(_A)
class _MpTermStateActiveRHIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,9))
_MpTermStateActiveRHIndex_Type.__name__=_C
_MpTermStateActiveRHIndex_Object=MibTableColumn
mpTermStateActiveRHIndex=_MpTermStateActiveRHIndex_Object((1,3,6,1,4,1,5651,3,602,1,2,1,1,8),_MpTermStateActiveRHIndex_Type())
mpTermStateActiveRHIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermStateActiveRHIndex.setStatus(_A)
_MpTermRHStateTable_Object=MibTable
mpTermRHStateTable=_MpTermRHStateTable_Object((1,3,6,1,4,1,5651,3,602,1,2,2))
if mibBuilder.loadTexts:mpTermRHStateTable.setStatus(_A)
_MpTermRHStateEntry_Object=MibTableRow
mpTermRHStateEntry=_MpTermRHStateEntry_Object((1,3,6,1,4,1,5651,3,602,1,2,2,1))
mpTermRHStateEntry.setIndexNames((0,_E,_G),(0,_E,_H))
if mibBuilder.loadTexts:mpTermRHStateEntry.setStatus(_A)
class _MpTermRHStateInterface_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,59))
_MpTermRHStateInterface_Type.__name__=_D
_MpTermRHStateInterface_Object=MibTableColumn
mpTermRHStateInterface=_MpTermRHStateInterface_Object((1,3,6,1,4,1,5651,3,602,1,2,2,1,1),_MpTermRHStateInterface_Type())
mpTermRHStateInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermRHStateInterface.setStatus(_A)
class _MpTermRHStateRHIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_MpTermRHStateRHIndex_Type.__name__=_C
_MpTermRHStateRHIndex_Object=MibTableColumn
mpTermRHStateRHIndex=_MpTermRHStateRHIndex_Object((1,3,6,1,4,1,5651,3,602,1,2,2,1,2),_MpTermRHStateRHIndex_Type())
mpTermRHStateRHIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermRHStateRHIndex.setStatus(_A)
class _MpTermRHStateTemplateName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpTermRHStateTemplateName_Type.__name__=_D
_MpTermRHStateTemplateName_Object=MibTableColumn
mpTermRHStateTemplateName=_MpTermRHStateTemplateName_Object((1,3,6,1,4,1,5651,3,602,1,2,2,1,3),_MpTermRHStateTemplateName_Type())
mpTermRHStateTemplateName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermRHStateTemplateName.setStatus(_A)
class _MpTermRHStateRemoteState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disconnect',1),('connecting',2),('connected',3)))
_MpTermRHStateRemoteState_Type.__name__=_C
_MpTermRHStateRemoteState_Object=MibTableColumn
mpTermRHStateRemoteState=_MpTermRHStateRemoteState_Object((1,3,6,1,4,1,5651,3,602,1,2,2,1,4),_MpTermRHStateRemoteState_Type())
mpTermRHStateRemoteState.setMaxAccess(_B)
if mibBuilder.loadTexts:mpTermRHStateRemoteState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mpTerminalMib':mpTerminalMib,'mpTermMIBObjects':mpTermMIBObjects,'mpTermConfigs':mpTermConfigs,'mpTermInfo':mpTermInfo,'mpTermStateTable':mpTermStateTable,'mpTermStateEntry':mpTermStateEntry,_F:mpTermStateInterface,'mpTermStateTermType':mpTermStateTermType,'mpTermStateCOM':mpTermStateCOM,'mpTermStateTERM':mpTermStateTERM,'mpTermStateTcpServerPort':mpTermStateTcpServerPort,'mpTermStateTerminalState':mpTermStateTerminalState,'mpTermStateTemplateName':mpTermStateTemplateName,'mpTermStateActiveRHIndex':mpTermStateActiveRHIndex,'mpTermRHStateTable':mpTermRHStateTable,'mpTermRHStateEntry':mpTermRHStateEntry,_G:mpTermRHStateInterface,_H:mpTermRHStateRHIndex,'mpTermRHStateTemplateName':mpTermRHStateTemplateName,'mpTermRHStateRemoteState':mpTermRHStateRemoteState})