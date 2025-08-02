_I='fsLbdPortId'
_H='ARICENT-LBD-MIB'
_G='disabled'
_F='enabled'
_E='TruthValue'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_E)
futureLbdMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,123))
_FsLbdSystems_ObjectIdentity=ObjectIdentity
fsLbdSystems=_FsLbdSystems_ObjectIdentity((1,3,6,1,4,1,29601,2,123,1))
class _FsLbdSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsLbdSystemControl_Type.__name__=_C
_FsLbdSystemControl_Object=MibScalar
fsLbdSystemControl=_FsLbdSystemControl_Object((1,3,6,1,4,1,29601,2,123,1,1),_FsLbdSystemControl_Type())
fsLbdSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdSystemControl.setStatus(_A)
class _FsLbdModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsLbdModuleStatus_Type.__name__=_C
_FsLbdModuleStatus_Object=MibScalar
fsLbdModuleStatus=_FsLbdModuleStatus_Object((1,3,6,1,4,1,29601,2,123,1,2),_FsLbdModuleStatus_Type())
fsLbdModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdModuleStatus.setStatus(_A)
class _FsLbdTransmitInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_FsLbdTransmitInterval_Type.__name__=_C
_FsLbdTransmitInterval_Object=MibScalar
fsLbdTransmitInterval=_FsLbdTransmitInterval_Object((1,3,6,1,4,1,29601,2,123,1,3),_FsLbdTransmitInterval_Type())
fsLbdTransmitInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdTransmitInterval.setStatus(_A)
_FsLbdDestMacAddress_Type=MacAddress
_FsLbdDestMacAddress_Object=MibScalar
fsLbdDestMacAddress=_FsLbdDestMacAddress_Object((1,3,6,1,4,1,29601,2,123,1,4),_FsLbdDestMacAddress_Type())
fsLbdDestMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdDestMacAddress.setStatus(_A)
class _FsLbdTraceOption_Type(Integer32):defaultValue=8
_FsLbdTraceOption_Type.__name__=_C
_FsLbdTraceOption_Object=MibScalar
fsLbdTraceOption=_FsLbdTraceOption_Object((1,3,6,1,4,1,29601,2,123,1,5),_FsLbdTraceOption_Type())
fsLbdTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdTraceOption.setStatus(_A)
_FsLbdConfig_ObjectIdentity=ObjectIdentity
fsLbdConfig=_FsLbdConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,123,2))
_FsLbdPortTable_Object=MibTable
fsLbdPortTable=_FsLbdPortTable_Object((1,3,6,1,4,1,29601,2,123,2,1))
if mibBuilder.loadTexts:fsLbdPortTable.setStatus(_A)
_FsLbdPortEntry_Object=MibTableRow
fsLbdPortEntry=_FsLbdPortEntry_Object((1,3,6,1,4,1,29601,2,123,2,1,1))
fsLbdPortEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:fsLbdPortEntry.setStatus(_A)
_FsLbdPortId_Type=Integer32
_FsLbdPortId_Object=MibTableColumn
fsLbdPortId=_FsLbdPortId_Object((1,3,6,1,4,1,29601,2,123,2,1,1,1),_FsLbdPortId_Type())
fsLbdPortId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsLbdPortId.setStatus(_A)
class _FsLbdLoopDetectStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_FsLbdLoopDetectStatus_Type.__name__=_C
_FsLbdLoopDetectStatus_Object=MibTableColumn
fsLbdLoopDetectStatus=_FsLbdLoopDetectStatus_Object((1,3,6,1,4,1,29601,2,123,2,1,1,2),_FsLbdLoopDetectStatus_Type())
fsLbdLoopDetectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdLoopDetectStatus.setStatus(_A)
_FsLbdTxCount_Type=Counter32
_FsLbdTxCount_Object=MibTableColumn
fsLbdTxCount=_FsLbdTxCount_Object((1,3,6,1,4,1,29601,2,123,2,1,1,3),_FsLbdTxCount_Type())
fsLbdTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLbdTxCount.setStatus(_A)
_FsLbdRxCount_Type=Counter32
_FsLbdRxCount_Object=MibTableColumn
fsLbdRxCount=_FsLbdRxCount_Object((1,3,6,1,4,1,29601,2,123,2,1,1,4),_FsLbdRxCount_Type())
fsLbdRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLbdRxCount.setStatus(_A)
class _FsLbdPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noloopback',0),('loopback',1)))
_FsLbdPortStatus_Type.__name__=_C
_FsLbdPortStatus_Object=MibTableColumn
fsLbdPortStatus=_FsLbdPortStatus_Object((1,3,6,1,4,1,29601,2,123,2,1,1,5),_FsLbdPortStatus_Type())
fsLbdPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLbdPortStatus.setStatus(_A)
_FsLbdPktTxFromPort_Type=Integer32
_FsLbdPktTxFromPort_Object=MibTableColumn
fsLbdPktTxFromPort=_FsLbdPktTxFromPort_Object((1,3,6,1,4,1,29601,2,123,2,1,1,6),_FsLbdPktTxFromPort_Type())
fsLbdPktTxFromPort.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLbdPktTxFromPort.setStatus(_A)
_FsLbdPortRowStatus_Type=RowStatus
_FsLbdPortRowStatus_Object=MibTableColumn
fsLbdPortRowStatus=_FsLbdPortRowStatus_Object((1,3,6,1,4,1,29601,2,123,2,1,1,7),_FsLbdPortRowStatus_Type())
fsLbdPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdPortRowStatus.setStatus(_A)
class _FsLbdClearStats_Type(TruthValue):defaultValue=2
_FsLbdClearStats_Type.__name__=_E
_FsLbdClearStats_Object=MibTableColumn
fsLbdClearStats=_FsLbdClearStats_Object((1,3,6,1,4,1,29601,2,123,2,1,1,8),_FsLbdClearStats_Type())
fsLbdClearStats.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLbdClearStats.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'futureLbdMIB':futureLbdMIB,'fsLbdSystems':fsLbdSystems,'fsLbdSystemControl':fsLbdSystemControl,'fsLbdModuleStatus':fsLbdModuleStatus,'fsLbdTransmitInterval':fsLbdTransmitInterval,'fsLbdDestMacAddress':fsLbdDestMacAddress,'fsLbdTraceOption':fsLbdTraceOption,'fsLbdConfig':fsLbdConfig,'fsLbdPortTable':fsLbdPortTable,'fsLbdPortEntry':fsLbdPortEntry,_I:fsLbdPortId,'fsLbdLoopDetectStatus':fsLbdLoopDetectStatus,'fsLbdTxCount':fsLbdTxCount,'fsLbdRxCount':fsLbdRxCount,'fsLbdPortStatus':fsLbdPortStatus,'fsLbdPktTxFromPort':fsLbdPktTxFromPort,'fsLbdPortRowStatus':fsLbdPortRowStatus,'fsLbdClearStats':fsLbdClearStats})