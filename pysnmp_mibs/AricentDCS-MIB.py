_L='not-accessible'
_K='fsDcsPortCtrlVlanId'
_J='fsDcsPortCtrlIndex'
_I='disabled'
_H='enabled'
_G='EnabledStatus'
_F='AricentDCS-MIB'
_E='NULL'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
fsDcsMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,1))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsDcsSystem_ObjectIdentity=ObjectIdentity
fsDcsSystem=_FsDcsSystem_ObjectIdentity((1,3,6,1,4,1,29601,2,1,1))
class _FsDcsDefCircuitIDFormatConfig_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_FsDcsDefCircuitIDFormatConfig_Type.__name__=_C
_FsDcsDefCircuitIDFormatConfig_Object=MibScalar
fsDcsDefCircuitIDFormatConfig=_FsDcsDefCircuitIDFormatConfig_Object((1,3,6,1,4,1,29601,2,1,1,1),_FsDcsDefCircuitIDFormatConfig_Type())
fsDcsDefCircuitIDFormatConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsDefCircuitIDFormatConfig.setStatus(_A)
class _FsDcsDefCircuitIDFormatString_Type(DisplayString):defaultValue=OctetString(_E);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_FsDcsDefCircuitIDFormatString_Type.__name__=_D
_FsDcsDefCircuitIDFormatString_Object=MibScalar
fsDcsDefCircuitIDFormatString=_FsDcsDefCircuitIDFormatString_Object((1,3,6,1,4,1,29601,2,1,1,2),_FsDcsDefCircuitIDFormatString_Type())
fsDcsDefCircuitIDFormatString.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsDefCircuitIDFormatString.setStatus(_A)
class _FsDcsDefCircuitIDFormatOption_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('sp',1),('sv',2),('pv',3),('spv',4)))
_FsDcsDefCircuitIDFormatOption_Type.__name__=_C
_FsDcsDefCircuitIDFormatOption_Object=MibScalar
fsDcsDefCircuitIDFormatOption=_FsDcsDefCircuitIDFormatOption_Object((1,3,6,1,4,1,29601,2,1,1,3),_FsDcsDefCircuitIDFormatOption_Type())
fsDcsDefCircuitIDFormatOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsDefCircuitIDFormatOption.setStatus(_A)
class _FsDcsDefCircuitIDFormatDelimiter_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('hash',1),('dot',2),('comma',3),('semicolon',4),('rightslash',5),('space',6)))
_FsDcsDefCircuitIDFormatDelimiter_Type.__name__=_C
_FsDcsDefCircuitIDFormatDelimiter_Object=MibScalar
fsDcsDefCircuitIDFormatDelimiter=_FsDcsDefCircuitIDFormatDelimiter_Object((1,3,6,1,4,1,29601,2,1,1,4),_FsDcsDefCircuitIDFormatDelimiter_Type())
fsDcsDefCircuitIDFormatDelimiter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsDefCircuitIDFormatDelimiter.setStatus(_A)
_FsDcsConfigControl_ObjectIdentity=ObjectIdentity
fsDcsConfigControl=_FsDcsConfigControl_ObjectIdentity((1,3,6,1,4,1,29601,2,1,2))
_FsDcsPortCtrlTable_Object=MibTable
fsDcsPortCtrlTable=_FsDcsPortCtrlTable_Object((1,3,6,1,4,1,29601,2,1,2,1))
if mibBuilder.loadTexts:fsDcsPortCtrlTable.setStatus(_A)
_FsDcsPortCtrlEntry_Object=MibTableRow
fsDcsPortCtrlEntry=_FsDcsPortCtrlEntry_Object((1,3,6,1,4,1,29601,2,1,2,1,1))
fsDcsPortCtrlEntry.setIndexNames((0,_F,_J),(0,_F,_K))
if mibBuilder.loadTexts:fsDcsPortCtrlEntry.setStatus(_A)
_FsDcsPortCtrlIndex_Type=InterfaceIndex
_FsDcsPortCtrlIndex_Object=MibTableColumn
fsDcsPortCtrlIndex=_FsDcsPortCtrlIndex_Object((1,3,6,1,4,1,29601,2,1,2,1,1,1),_FsDcsPortCtrlIndex_Type())
fsDcsPortCtrlIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:fsDcsPortCtrlIndex.setStatus(_A)
class _FsDcsPortCtrlVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_FsDcsPortCtrlVlanId_Type.__name__=_C
_FsDcsPortCtrlVlanId_Object=MibTableColumn
fsDcsPortCtrlVlanId=_FsDcsPortCtrlVlanId_Object((1,3,6,1,4,1,29601,2,1,2,1,1,2),_FsDcsPortCtrlVlanId_Type())
fsDcsPortCtrlVlanId.setMaxAccess(_L)
if mibBuilder.loadTexts:fsDcsPortCtrlVlanId.setStatus(_A)
class _FsDcsPortCtrlRemoteAgentIdentifier_Type(DisplayString):defaultValue=OctetString(_E);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FsDcsPortCtrlRemoteAgentIdentifier_Type.__name__=_D
_FsDcsPortCtrlRemoteAgentIdentifier_Object=MibTableColumn
fsDcsPortCtrlRemoteAgentIdentifier=_FsDcsPortCtrlRemoteAgentIdentifier_Object((1,3,6,1,4,1,29601,2,1,2,1,1,3),_FsDcsPortCtrlRemoteAgentIdentifier_Type())
fsDcsPortCtrlRemoteAgentIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsPortCtrlRemoteAgentIdentifier.setStatus(_A)
class _FsDcsPortCtrlRemoteAgentIDStatus_Type(EnabledStatus):defaultValue=2
_FsDcsPortCtrlRemoteAgentIDStatus_Type.__name__=_G
_FsDcsPortCtrlRemoteAgentIDStatus_Object=MibTableColumn
fsDcsPortCtrlRemoteAgentIDStatus=_FsDcsPortCtrlRemoteAgentIDStatus_Object((1,3,6,1,4,1,29601,2,1,2,1,1,4),_FsDcsPortCtrlRemoteAgentIDStatus_Type())
fsDcsPortCtrlRemoteAgentIDStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsPortCtrlRemoteAgentIDStatus.setStatus(_A)
class _FsDcsPortCtrlAccessLoopStatus_Type(EnabledStatus):defaultValue=2
_FsDcsPortCtrlAccessLoopStatus_Type.__name__=_G
_FsDcsPortCtrlAccessLoopStatus_Object=MibTableColumn
fsDcsPortCtrlAccessLoopStatus=_FsDcsPortCtrlAccessLoopStatus_Object((1,3,6,1,4,1,29601,2,1,2,1,1,5),_FsDcsPortCtrlAccessLoopStatus_Type())
fsDcsPortCtrlAccessLoopStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsPortCtrlAccessLoopStatus.setStatus(_A)
class _FsDcsPortCtrlAgentCircuitID_Type(DisplayString):defaultValue=OctetString(_E);subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FsDcsPortCtrlAgentCircuitID_Type.__name__=_D
_FsDcsPortCtrlAgentCircuitID_Object=MibTableColumn
fsDcsPortCtrlAgentCircuitID=_FsDcsPortCtrlAgentCircuitID_Object((1,3,6,1,4,1,29601,2,1,2,1,1,6),_FsDcsPortCtrlAgentCircuitID_Type())
fsDcsPortCtrlAgentCircuitID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDcsPortCtrlAgentCircuitID.setStatus(_A)
_FsDcsPortCtrlVlanRowStatus_Type=RowStatus
_FsDcsPortCtrlVlanRowStatus_Object=MibTableColumn
fsDcsPortCtrlVlanRowStatus=_FsDcsPortCtrlVlanRowStatus_Object((1,3,6,1,4,1,29601,2,1,2,1,1,7),_FsDcsPortCtrlVlanRowStatus_Type())
fsDcsPortCtrlVlanRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsDcsPortCtrlVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_G:EnabledStatus,'fsDcsMIB':fsDcsMIB,'fsDcsSystem':fsDcsSystem,'fsDcsDefCircuitIDFormatConfig':fsDcsDefCircuitIDFormatConfig,'fsDcsDefCircuitIDFormatString':fsDcsDefCircuitIDFormatString,'fsDcsDefCircuitIDFormatOption':fsDcsDefCircuitIDFormatOption,'fsDcsDefCircuitIDFormatDelimiter':fsDcsDefCircuitIDFormatDelimiter,'fsDcsConfigControl':fsDcsConfigControl,'fsDcsPortCtrlTable':fsDcsPortCtrlTable,'fsDcsPortCtrlEntry':fsDcsPortCtrlEntry,_J:fsDcsPortCtrlIndex,_K:fsDcsPortCtrlVlanId,'fsDcsPortCtrlRemoteAgentIdentifier':fsDcsPortCtrlRemoteAgentIdentifier,'fsDcsPortCtrlRemoteAgentIDStatus':fsDcsPortCtrlRemoteAgentIDStatus,'fsDcsPortCtrlAccessLoopStatus':fsDcsPortCtrlAccessLoopStatus,'fsDcsPortCtrlAgentCircuitID':fsDcsPortCtrlAgentCircuitID,'fsDcsPortCtrlVlanRowStatus':fsDcsPortCtrlVlanRowStatus})