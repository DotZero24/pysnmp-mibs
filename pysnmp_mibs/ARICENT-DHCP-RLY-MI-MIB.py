_L='fsMIDhcpRelaySrvIpAddress'
_K='not-accessible'
_J='ifIndex'
_I='IF-MIB'
_H='fsMIDhcpContextId'
_G='ARICENT-DHCP-RLY-MI-MIB'
_F='read-only'
_E='disable'
_D='enable'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futureMIDhcpRelay=ModuleIdentity((1,3,6,1,4,1,29601,2,92))
if mibBuilder.loadTexts:futureMIDhcpRelay.setRevisions(('2014-10-28 00:00',))
_FsMIDhcpRelay_ObjectIdentity=ObjectIdentity
fsMIDhcpRelay=_FsMIDhcpRelay_ObjectIdentity((1,3,6,1,4,1,29601,2,92,1))
class _FsMIDhcpConfigGblTraceLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIDhcpConfigGblTraceLevel_Type.__name__=_C
_FsMIDhcpConfigGblTraceLevel_Object=MibScalar
fsMIDhcpConfigGblTraceLevel=_FsMIDhcpConfigGblTraceLevel_Object((1,3,6,1,4,1,29601,2,92,1,1),_FsMIDhcpConfigGblTraceLevel_Type())
fsMIDhcpConfigGblTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpConfigGblTraceLevel.setStatus(_A)
_FsMIDhcpRelayTable_ObjectIdentity=ObjectIdentity
fsMIDhcpRelayTable=_FsMIDhcpRelayTable_ObjectIdentity((1,3,6,1,4,1,29601,2,92,2))
_FsMIDhcpContextTable_Object=MibTable
fsMIDhcpContextTable=_FsMIDhcpContextTable_Object((1,3,6,1,4,1,29601,2,92,2,1))
if mibBuilder.loadTexts:fsMIDhcpContextTable.setStatus(_A)
_FsMIDhcpContextEntry_Object=MibTableRow
fsMIDhcpContextEntry=_FsMIDhcpContextEntry_Object((1,3,6,1,4,1,29601,2,92,2,1,1))
fsMIDhcpContextEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fsMIDhcpContextEntry.setStatus(_A)
class _FsMIDhcpContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDhcpContextId_Type.__name__=_C
_FsMIDhcpContextId_Object=MibTableColumn
fsMIDhcpContextId=_FsMIDhcpContextId_Object((1,3,6,1,4,1,29601,2,92,2,1,1,1),_FsMIDhcpContextId_Type())
fsMIDhcpContextId.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIDhcpContextId.setStatus(_A)
class _FsMIDhcpRelaying_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsMIDhcpRelaying_Type.__name__=_C
_FsMIDhcpRelaying_Object=MibTableColumn
fsMIDhcpRelaying=_FsMIDhcpRelaying_Object((1,3,6,1,4,1,29601,2,92,2,1,1,2),_FsMIDhcpRelaying_Type())
fsMIDhcpRelaying.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelaying.setStatus(_A)
class _FsMIDhcpRelayServersOnly_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsMIDhcpRelayServersOnly_Type.__name__=_C
_FsMIDhcpRelayServersOnly_Object=MibTableColumn
fsMIDhcpRelayServersOnly=_FsMIDhcpRelayServersOnly_Object((1,3,6,1,4,1,29601,2,92,2,1,1,3),_FsMIDhcpRelayServersOnly_Type())
fsMIDhcpRelayServersOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayServersOnly.setStatus(_A)
class _FsMIDhcpRelaySecsThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDhcpRelaySecsThreshold_Type.__name__=_C
_FsMIDhcpRelaySecsThreshold_Object=MibTableColumn
fsMIDhcpRelaySecsThreshold=_FsMIDhcpRelaySecsThreshold_Object((1,3,6,1,4,1,29601,2,92,2,1,1,4),_FsMIDhcpRelaySecsThreshold_Type())
fsMIDhcpRelaySecsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelaySecsThreshold.setStatus(_A)
class _FsMIDhcpRelayHopsThreshold_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_FsMIDhcpRelayHopsThreshold_Type.__name__=_C
_FsMIDhcpRelayHopsThreshold_Object=MibTableColumn
fsMIDhcpRelayHopsThreshold=_FsMIDhcpRelayHopsThreshold_Object((1,3,6,1,4,1,29601,2,92,2,1,1,5),_FsMIDhcpRelayHopsThreshold_Type())
fsMIDhcpRelayHopsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayHopsThreshold.setStatus(_A)
class _FsMIDhcpRelayRAIOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsMIDhcpRelayRAIOptionControl_Type.__name__=_C
_FsMIDhcpRelayRAIOptionControl_Object=MibTableColumn
fsMIDhcpRelayRAIOptionControl=_FsMIDhcpRelayRAIOptionControl_Object((1,3,6,1,4,1,29601,2,92,2,1,1,6),_FsMIDhcpRelayRAIOptionControl_Type())
fsMIDhcpRelayRAIOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayRAIOptionControl.setStatus(_A)
class _FsMIDhcpRelayRAICircuitIDSubOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsMIDhcpRelayRAICircuitIDSubOptionControl_Type.__name__=_C
_FsMIDhcpRelayRAICircuitIDSubOptionControl_Object=MibTableColumn
fsMIDhcpRelayRAICircuitIDSubOptionControl=_FsMIDhcpRelayRAICircuitIDSubOptionControl_Object((1,3,6,1,4,1,29601,2,92,2,1,1,7),_FsMIDhcpRelayRAICircuitIDSubOptionControl_Type())
fsMIDhcpRelayRAICircuitIDSubOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayRAICircuitIDSubOptionControl.setStatus(_A)
class _FsMIDhcpRelayRAIRemoteIDSubOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsMIDhcpRelayRAIRemoteIDSubOptionControl_Type.__name__=_C
_FsMIDhcpRelayRAIRemoteIDSubOptionControl_Object=MibTableColumn
fsMIDhcpRelayRAIRemoteIDSubOptionControl=_FsMIDhcpRelayRAIRemoteIDSubOptionControl_Object((1,3,6,1,4,1,29601,2,92,2,1,1,8),_FsMIDhcpRelayRAIRemoteIDSubOptionControl_Type())
fsMIDhcpRelayRAIRemoteIDSubOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayRAIRemoteIDSubOptionControl.setStatus(_A)
class _FsMIDhcpRelayRAISubnetMaskSubOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_FsMIDhcpRelayRAISubnetMaskSubOptionControl_Type.__name__=_C
_FsMIDhcpRelayRAISubnetMaskSubOptionControl_Object=MibTableColumn
fsMIDhcpRelayRAISubnetMaskSubOptionControl=_FsMIDhcpRelayRAISubnetMaskSubOptionControl_Object((1,3,6,1,4,1,29601,2,92,2,1,1,9),_FsMIDhcpRelayRAISubnetMaskSubOptionControl_Type())
fsMIDhcpRelayRAISubnetMaskSubOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayRAISubnetMaskSubOptionControl.setStatus(_A)
_FsMIDhcpRelayRAIOptionInserted_Type=Counter32
_FsMIDhcpRelayRAIOptionInserted_Object=MibTableColumn
fsMIDhcpRelayRAIOptionInserted=_FsMIDhcpRelayRAIOptionInserted_Object((1,3,6,1,4,1,29601,2,92,2,1,1,10),_FsMIDhcpRelayRAIOptionInserted_Type())
fsMIDhcpRelayRAIOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIDhcpRelayRAIOptionInserted.setStatus(_A)
_FsMIDhcpRelayRAICircuitIDSubOptionInserted_Type=Counter32
_FsMIDhcpRelayRAICircuitIDSubOptionInserted_Object=MibTableColumn
fsMIDhcpRelayRAICircuitIDSubOptionInserted=_FsMIDhcpRelayRAICircuitIDSubOptionInserted_Object((1,3,6,1,4,1,29601,2,92,2,1,1,11),_FsMIDhcpRelayRAICircuitIDSubOptionInserted_Type())
fsMIDhcpRelayRAICircuitIDSubOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIDhcpRelayRAICircuitIDSubOptionInserted.setStatus(_A)
_FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Type=Counter32
_FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Object=MibTableColumn
fsMIDhcpRelayRAIRemoteIDSubOptionInserted=_FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Object((1,3,6,1,4,1,29601,2,92,2,1,1,12),_FsMIDhcpRelayRAIRemoteIDSubOptionInserted_Type())
fsMIDhcpRelayRAIRemoteIDSubOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIDhcpRelayRAIRemoteIDSubOptionInserted.setStatus(_A)
_FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Type=Counter32
_FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Object=MibTableColumn
fsMIDhcpRelayRAISubnetMaskSubOptionInserted=_FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Object((1,3,6,1,4,1,29601,2,92,2,1,1,13),_FsMIDhcpRelayRAISubnetMaskSubOptionInserted_Type())
fsMIDhcpRelayRAISubnetMaskSubOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIDhcpRelayRAISubnetMaskSubOptionInserted.setStatus(_A)
_FsMIDhcpRelayRAIOptionWronglySet_Type=Counter32
_FsMIDhcpRelayRAIOptionWronglySet_Object=MibTableColumn
fsMIDhcpRelayRAIOptionWronglySet=_FsMIDhcpRelayRAIOptionWronglySet_Object((1,3,6,1,4,1,29601,2,92,2,1,1,14),_FsMIDhcpRelayRAIOptionWronglySet_Type())
fsMIDhcpRelayRAIOptionWronglySet.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIDhcpRelayRAIOptionWronglySet.setStatus(_A)
_FsMIDhcpRelayRAISpaceConstraint_Type=Counter32
_FsMIDhcpRelayRAISpaceConstraint_Object=MibTableColumn
fsMIDhcpRelayRAISpaceConstraint=_FsMIDhcpRelayRAISpaceConstraint_Object((1,3,6,1,4,1,29601,2,92,2,1,1,15),_FsMIDhcpRelayRAISpaceConstraint_Type())
fsMIDhcpRelayRAISpaceConstraint.setMaxAccess(_F)
if mibBuilder.loadTexts:fsMIDhcpRelayRAISpaceConstraint.setStatus(_A)
class _FsMIDhcpConfigTraceLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIDhcpConfigTraceLevel_Type.__name__=_C
_FsMIDhcpConfigTraceLevel_Object=MibTableColumn
fsMIDhcpConfigTraceLevel=_FsMIDhcpConfigTraceLevel_Object((1,3,6,1,4,1,29601,2,92,2,1,1,16),_FsMIDhcpConfigTraceLevel_Type())
fsMIDhcpConfigTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpConfigTraceLevel.setStatus(_A)
class _FsMIDhcpConfigDhcpCircuitOption_Type(Bits):defaultHexValue='01';namedValues=NamedValues(*(('routerindex',0),('vlanid',1),('recvport',2)))
_FsMIDhcpConfigDhcpCircuitOption_Type.__name__='Bits'
_FsMIDhcpConfigDhcpCircuitOption_Object=MibTableColumn
fsMIDhcpConfigDhcpCircuitOption=_FsMIDhcpConfigDhcpCircuitOption_Object((1,3,6,1,4,1,29601,2,92,2,1,1,17),_FsMIDhcpConfigDhcpCircuitOption_Type())
fsMIDhcpConfigDhcpCircuitOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpConfigDhcpCircuitOption.setStatus(_A)
class _FsMIDhcpRelayCounterReset_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('notset',2)))
_FsMIDhcpRelayCounterReset_Type.__name__=_C
_FsMIDhcpRelayCounterReset_Object=MibTableColumn
fsMIDhcpRelayCounterReset=_FsMIDhcpRelayCounterReset_Object((1,3,6,1,4,1,29601,2,92,2,1,1,18),_FsMIDhcpRelayCounterReset_Type())
fsMIDhcpRelayCounterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayCounterReset.setStatus(_A)
_FsMIDhcpRelayContextRowStatus_Type=RowStatus
_FsMIDhcpRelayContextRowStatus_Object=MibTableColumn
fsMIDhcpRelayContextRowStatus=_FsMIDhcpRelayContextRowStatus_Object((1,3,6,1,4,1,29601,2,92,2,1,1,19),_FsMIDhcpRelayContextRowStatus_Type())
fsMIDhcpRelayContextRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayContextRowStatus.setStatus(_A)
_FsMIDhcpRelaySrvAddressTable_Object=MibTable
fsMIDhcpRelaySrvAddressTable=_FsMIDhcpRelaySrvAddressTable_Object((1,3,6,1,4,1,29601,2,92,2,2))
if mibBuilder.loadTexts:fsMIDhcpRelaySrvAddressTable.setStatus(_A)
_FsMIDhcpRelaySrvAddressEntry_Object=MibTableRow
fsMIDhcpRelaySrvAddressEntry=_FsMIDhcpRelaySrvAddressEntry_Object((1,3,6,1,4,1,29601,2,92,2,2,1))
fsMIDhcpRelaySrvAddressEntry.setIndexNames((0,_G,_H),(0,_G,_L))
if mibBuilder.loadTexts:fsMIDhcpRelaySrvAddressEntry.setStatus(_A)
_FsMIDhcpRelaySrvIpAddress_Type=IpAddress
_FsMIDhcpRelaySrvIpAddress_Object=MibTableColumn
fsMIDhcpRelaySrvIpAddress=_FsMIDhcpRelaySrvIpAddress_Object((1,3,6,1,4,1,29601,2,92,2,2,1,1),_FsMIDhcpRelaySrvIpAddress_Type())
fsMIDhcpRelaySrvIpAddress.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIDhcpRelaySrvIpAddress.setStatus(_A)
_FsMIDhcpRelaySrvAddressRowStatus_Type=RowStatus
_FsMIDhcpRelaySrvAddressRowStatus_Object=MibTableColumn
fsMIDhcpRelaySrvAddressRowStatus=_FsMIDhcpRelaySrvAddressRowStatus_Object((1,3,6,1,4,1,29601,2,92,2,2,1,2),_FsMIDhcpRelaySrvAddressRowStatus_Type())
fsMIDhcpRelaySrvAddressRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelaySrvAddressRowStatus.setStatus(_A)
_FsMIDhcpRelayIfTable_Object=MibTable
fsMIDhcpRelayIfTable=_FsMIDhcpRelayIfTable_Object((1,3,6,1,4,1,29601,2,92,2,3))
if mibBuilder.loadTexts:fsMIDhcpRelayIfTable.setStatus(_A)
_FsMIDhcpRelayIfEntry_Object=MibTableRow
fsMIDhcpRelayIfEntry=_FsMIDhcpRelayIfEntry_Object((1,3,6,1,4,1,29601,2,92,2,3,1))
fsMIDhcpRelayIfEntry.setIndexNames((0,_G,_H),(0,_I,_J))
if mibBuilder.loadTexts:fsMIDhcpRelayIfEntry.setStatus(_A)
_FsMIDhcpRelayIfCircuitId_Type=Unsigned32
_FsMIDhcpRelayIfCircuitId_Object=MibTableColumn
fsMIDhcpRelayIfCircuitId=_FsMIDhcpRelayIfCircuitId_Object((1,3,6,1,4,1,29601,2,92,2,3,1,1),_FsMIDhcpRelayIfCircuitId_Type())
fsMIDhcpRelayIfCircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayIfCircuitId.setStatus(_A)
_FsMIDhcpRelayIfRemoteId_Type=DisplayString
_FsMIDhcpRelayIfRemoteId_Object=MibTableColumn
fsMIDhcpRelayIfRemoteId=_FsMIDhcpRelayIfRemoteId_Object((1,3,6,1,4,1,29601,2,92,2,3,1,2),_FsMIDhcpRelayIfRemoteId_Type())
fsMIDhcpRelayIfRemoteId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayIfRemoteId.setStatus(_A)
_FsMIDhcpRelayIfRowStatus_Type=RowStatus
_FsMIDhcpRelayIfRowStatus_Object=MibTableColumn
fsMIDhcpRelayIfRowStatus=_FsMIDhcpRelayIfRowStatus_Object((1,3,6,1,4,1,29601,2,92,2,3,1,3),_FsMIDhcpRelayIfRowStatus_Type())
fsMIDhcpRelayIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpRelayIfRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'futureMIDhcpRelay':futureMIDhcpRelay,'fsMIDhcpRelay':fsMIDhcpRelay,'fsMIDhcpConfigGblTraceLevel':fsMIDhcpConfigGblTraceLevel,'fsMIDhcpRelayTable':fsMIDhcpRelayTable,'fsMIDhcpContextTable':fsMIDhcpContextTable,'fsMIDhcpContextEntry':fsMIDhcpContextEntry,_H:fsMIDhcpContextId,'fsMIDhcpRelaying':fsMIDhcpRelaying,'fsMIDhcpRelayServersOnly':fsMIDhcpRelayServersOnly,'fsMIDhcpRelaySecsThreshold':fsMIDhcpRelaySecsThreshold,'fsMIDhcpRelayHopsThreshold':fsMIDhcpRelayHopsThreshold,'fsMIDhcpRelayRAIOptionControl':fsMIDhcpRelayRAIOptionControl,'fsMIDhcpRelayRAICircuitIDSubOptionControl':fsMIDhcpRelayRAICircuitIDSubOptionControl,'fsMIDhcpRelayRAIRemoteIDSubOptionControl':fsMIDhcpRelayRAIRemoteIDSubOptionControl,'fsMIDhcpRelayRAISubnetMaskSubOptionControl':fsMIDhcpRelayRAISubnetMaskSubOptionControl,'fsMIDhcpRelayRAIOptionInserted':fsMIDhcpRelayRAIOptionInserted,'fsMIDhcpRelayRAICircuitIDSubOptionInserted':fsMIDhcpRelayRAICircuitIDSubOptionInserted,'fsMIDhcpRelayRAIRemoteIDSubOptionInserted':fsMIDhcpRelayRAIRemoteIDSubOptionInserted,'fsMIDhcpRelayRAISubnetMaskSubOptionInserted':fsMIDhcpRelayRAISubnetMaskSubOptionInserted,'fsMIDhcpRelayRAIOptionWronglySet':fsMIDhcpRelayRAIOptionWronglySet,'fsMIDhcpRelayRAISpaceConstraint':fsMIDhcpRelayRAISpaceConstraint,'fsMIDhcpConfigTraceLevel':fsMIDhcpConfigTraceLevel,'fsMIDhcpConfigDhcpCircuitOption':fsMIDhcpConfigDhcpCircuitOption,'fsMIDhcpRelayCounterReset':fsMIDhcpRelayCounterReset,'fsMIDhcpRelayContextRowStatus':fsMIDhcpRelayContextRowStatus,'fsMIDhcpRelaySrvAddressTable':fsMIDhcpRelaySrvAddressTable,'fsMIDhcpRelaySrvAddressEntry':fsMIDhcpRelaySrvAddressEntry,_L:fsMIDhcpRelaySrvIpAddress,'fsMIDhcpRelaySrvAddressRowStatus':fsMIDhcpRelaySrvAddressRowStatus,'fsMIDhcpRelayIfTable':fsMIDhcpRelayIfTable,'fsMIDhcpRelayIfEntry':fsMIDhcpRelayIfEntry,'fsMIDhcpRelayIfCircuitId':fsMIDhcpRelayIfCircuitId,'fsMIDhcpRelayIfRemoteId':fsMIDhcpRelayIfRemoteId,'fsMIDhcpRelayIfRowStatus':fsMIDhcpRelayIfRowStatus})