_J='dhcpRelaySrvIpAddress'
_I='SUPERMICRO-DHCP-RLY-MIB'
_H='ifIndex'
_G='IF-MIB'
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
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
futureDhcpRelay=ModuleIdentity((1,3,6,1,4,1,10876,101,1,24))
if mibBuilder.loadTexts:futureDhcpRelay.setRevisions(('2012-09-05 00:00',))
_DhcpRelay_ObjectIdentity=ObjectIdentity
dhcpRelay=_DhcpRelay_ObjectIdentity((1,3,6,1,4,1,10876,101,1,24,1))
class _DhcpRelaying_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelaying_Type.__name__=_C
_DhcpRelaying_Object=MibScalar
dhcpRelaying=_DhcpRelaying_Object((1,3,6,1,4,1,10876,101,1,24,1,1),_DhcpRelaying_Type())
dhcpRelaying.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelaying.setStatus(_A)
class _DhcpRelayServersOnly_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayServersOnly_Type.__name__=_C
_DhcpRelayServersOnly_Object=MibScalar
dhcpRelayServersOnly=_DhcpRelayServersOnly_Object((1,3,6,1,4,1,10876,101,1,24,1,2),_DhcpRelayServersOnly_Type())
dhcpRelayServersOnly.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayServersOnly.setStatus(_A)
class _DhcpRelaySecsThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DhcpRelaySecsThreshold_Type.__name__=_C
_DhcpRelaySecsThreshold_Object=MibScalar
dhcpRelaySecsThreshold=_DhcpRelaySecsThreshold_Object((1,3,6,1,4,1,10876,101,1,24,1,3),_DhcpRelaySecsThreshold_Type())
dhcpRelaySecsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelaySecsThreshold.setStatus(_A)
class _DhcpRelayHopsThreshold_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_DhcpRelayHopsThreshold_Type.__name__=_C
_DhcpRelayHopsThreshold_Object=MibScalar
dhcpRelayHopsThreshold=_DhcpRelayHopsThreshold_Object((1,3,6,1,4,1,10876,101,1,24,1,4),_DhcpRelayHopsThreshold_Type())
dhcpRelayHopsThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayHopsThreshold.setStatus(_A)
class _DhcpRelayRAIOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayRAIOptionControl_Type.__name__=_C
_DhcpRelayRAIOptionControl_Object=MibScalar
dhcpRelayRAIOptionControl=_DhcpRelayRAIOptionControl_Object((1,3,6,1,4,1,10876,101,1,24,1,5),_DhcpRelayRAIOptionControl_Type())
dhcpRelayRAIOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayRAIOptionControl.setStatus(_A)
class _DhcpRelayRAICircuitIDSubOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayRAICircuitIDSubOptionControl_Type.__name__=_C
_DhcpRelayRAICircuitIDSubOptionControl_Object=MibScalar
dhcpRelayRAICircuitIDSubOptionControl=_DhcpRelayRAICircuitIDSubOptionControl_Object((1,3,6,1,4,1,10876,101,1,24,1,6),_DhcpRelayRAICircuitIDSubOptionControl_Type())
dhcpRelayRAICircuitIDSubOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayRAICircuitIDSubOptionControl.setStatus(_A)
class _DhcpRelayRAIRemoteIDSubOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayRAIRemoteIDSubOptionControl_Type.__name__=_C
_DhcpRelayRAIRemoteIDSubOptionControl_Object=MibScalar
dhcpRelayRAIRemoteIDSubOptionControl=_DhcpRelayRAIRemoteIDSubOptionControl_Object((1,3,6,1,4,1,10876,101,1,24,1,7),_DhcpRelayRAIRemoteIDSubOptionControl_Type())
dhcpRelayRAIRemoteIDSubOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayRAIRemoteIDSubOptionControl.setStatus(_A)
class _DhcpRelayRAISubnetMaskSubOptionControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DhcpRelayRAISubnetMaskSubOptionControl_Type.__name__=_C
_DhcpRelayRAISubnetMaskSubOptionControl_Object=MibScalar
dhcpRelayRAISubnetMaskSubOptionControl=_DhcpRelayRAISubnetMaskSubOptionControl_Object((1,3,6,1,4,1,10876,101,1,24,1,8),_DhcpRelayRAISubnetMaskSubOptionControl_Type())
dhcpRelayRAISubnetMaskSubOptionControl.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayRAISubnetMaskSubOptionControl.setStatus(_A)
_DhcpRelayRAIOptionInserted_Type=Counter32
_DhcpRelayRAIOptionInserted_Object=MibScalar
dhcpRelayRAIOptionInserted=_DhcpRelayRAIOptionInserted_Object((1,3,6,1,4,1,10876,101,1,24,1,9),_DhcpRelayRAIOptionInserted_Type())
dhcpRelayRAIOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpRelayRAIOptionInserted.setStatus(_A)
_DhcpRelayRAICircuitIDSubOptionInserted_Type=Counter32
_DhcpRelayRAICircuitIDSubOptionInserted_Object=MibScalar
dhcpRelayRAICircuitIDSubOptionInserted=_DhcpRelayRAICircuitIDSubOptionInserted_Object((1,3,6,1,4,1,10876,101,1,24,1,10),_DhcpRelayRAICircuitIDSubOptionInserted_Type())
dhcpRelayRAICircuitIDSubOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpRelayRAICircuitIDSubOptionInserted.setStatus(_A)
_DhcpRelayRAIRemoteIDSubOptionInserted_Type=Counter32
_DhcpRelayRAIRemoteIDSubOptionInserted_Object=MibScalar
dhcpRelayRAIRemoteIDSubOptionInserted=_DhcpRelayRAIRemoteIDSubOptionInserted_Object((1,3,6,1,4,1,10876,101,1,24,1,11),_DhcpRelayRAIRemoteIDSubOptionInserted_Type())
dhcpRelayRAIRemoteIDSubOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpRelayRAIRemoteIDSubOptionInserted.setStatus(_A)
_DhcpRelayRAISubnetMaskSubOptionInserted_Type=Counter32
_DhcpRelayRAISubnetMaskSubOptionInserted_Object=MibScalar
dhcpRelayRAISubnetMaskSubOptionInserted=_DhcpRelayRAISubnetMaskSubOptionInserted_Object((1,3,6,1,4,1,10876,101,1,24,1,12),_DhcpRelayRAISubnetMaskSubOptionInserted_Type())
dhcpRelayRAISubnetMaskSubOptionInserted.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpRelayRAISubnetMaskSubOptionInserted.setStatus(_A)
_DhcpRelayRAIOptionWronglySet_Type=Counter32
_DhcpRelayRAIOptionWronglySet_Object=MibScalar
dhcpRelayRAIOptionWronglySet=_DhcpRelayRAIOptionWronglySet_Object((1,3,6,1,4,1,10876,101,1,24,1,13),_DhcpRelayRAIOptionWronglySet_Type())
dhcpRelayRAIOptionWronglySet.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpRelayRAIOptionWronglySet.setStatus(_A)
_DhcpRelayRAISpaceConstraint_Type=Counter32
_DhcpRelayRAISpaceConstraint_Object=MibScalar
dhcpRelayRAISpaceConstraint=_DhcpRelayRAISpaceConstraint_Object((1,3,6,1,4,1,10876,101,1,24,1,14),_DhcpRelayRAISpaceConstraint_Type())
dhcpRelayRAISpaceConstraint.setMaxAccess(_F)
if mibBuilder.loadTexts:dhcpRelayRAISpaceConstraint.setStatus(_A)
class _DhcpConfigTraceLevel_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DhcpConfigTraceLevel_Type.__name__=_C
_DhcpConfigTraceLevel_Object=MibScalar
dhcpConfigTraceLevel=_DhcpConfigTraceLevel_Object((1,3,6,1,4,1,10876,101,1,24,1,15),_DhcpConfigTraceLevel_Type())
dhcpConfigTraceLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpConfigTraceLevel.setStatus(_A)
class _DhcpConfigDhcpCircuitOption_Type(Bits):defaultHexValue='01';namedValues=NamedValues(*(('routerindex',0),('vlanid',1),('recvport',2)))
_DhcpConfigDhcpCircuitOption_Type.__name__='Bits'
_DhcpConfigDhcpCircuitOption_Object=MibScalar
dhcpConfigDhcpCircuitOption=_DhcpConfigDhcpCircuitOption_Object((1,3,6,1,4,1,10876,101,1,24,1,16),_DhcpConfigDhcpCircuitOption_Type())
dhcpConfigDhcpCircuitOption.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpConfigDhcpCircuitOption.setStatus(_A)
class _DhcpRelayCounterReset_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('set',1),('notset',2)))
_DhcpRelayCounterReset_Type.__name__=_C
_DhcpRelayCounterReset_Object=MibScalar
dhcpRelayCounterReset=_DhcpRelayCounterReset_Object((1,3,6,1,4,1,10876,101,1,24,1,17),_DhcpRelayCounterReset_Type())
dhcpRelayCounterReset.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayCounterReset.setStatus(_A)
_DhcpRelayTable_ObjectIdentity=ObjectIdentity
dhcpRelayTable=_DhcpRelayTable_ObjectIdentity((1,3,6,1,4,1,10876,101,1,24,2))
_DhcpRelaySrvAddressTable_Object=MibTable
dhcpRelaySrvAddressTable=_DhcpRelaySrvAddressTable_Object((1,3,6,1,4,1,10876,101,1,24,2,1))
if mibBuilder.loadTexts:dhcpRelaySrvAddressTable.setStatus(_A)
_DhcpRelaySrvAddressEntry_Object=MibTableRow
dhcpRelaySrvAddressEntry=_DhcpRelaySrvAddressEntry_Object((1,3,6,1,4,1,10876,101,1,24,2,1,1))
dhcpRelaySrvAddressEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:dhcpRelaySrvAddressEntry.setStatus(_A)
_DhcpRelaySrvIpAddress_Type=IpAddress
_DhcpRelaySrvIpAddress_Object=MibTableColumn
dhcpRelaySrvIpAddress=_DhcpRelaySrvIpAddress_Object((1,3,6,1,4,1,10876,101,1,24,2,1,1,1),_DhcpRelaySrvIpAddress_Type())
dhcpRelaySrvIpAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dhcpRelaySrvIpAddress.setStatus(_A)
_DhcpRelaySrvAddressRowStatus_Type=RowStatus
_DhcpRelaySrvAddressRowStatus_Object=MibTableColumn
dhcpRelaySrvAddressRowStatus=_DhcpRelaySrvAddressRowStatus_Object((1,3,6,1,4,1,10876,101,1,24,2,1,1,2),_DhcpRelaySrvAddressRowStatus_Type())
dhcpRelaySrvAddressRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelaySrvAddressRowStatus.setStatus(_A)
_DhcpRelayIfTable_Object=MibTable
dhcpRelayIfTable=_DhcpRelayIfTable_Object((1,3,6,1,4,1,10876,101,1,24,2,2))
if mibBuilder.loadTexts:dhcpRelayIfTable.setStatus(_A)
_DhcpRelayIfEntry_Object=MibTableRow
dhcpRelayIfEntry=_DhcpRelayIfEntry_Object((1,3,6,1,4,1,10876,101,1,24,2,2,1))
dhcpRelayIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:dhcpRelayIfEntry.setStatus(_A)
_DhcpRelayIfCircuitId_Type=Unsigned32
_DhcpRelayIfCircuitId_Object=MibTableColumn
dhcpRelayIfCircuitId=_DhcpRelayIfCircuitId_Object((1,3,6,1,4,1,10876,101,1,24,2,2,1,1),_DhcpRelayIfCircuitId_Type())
dhcpRelayIfCircuitId.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayIfCircuitId.setStatus(_A)
_DhcpRelayIfRemoteId_Type=DisplayString
_DhcpRelayIfRemoteId_Object=MibTableColumn
dhcpRelayIfRemoteId=_DhcpRelayIfRemoteId_Object((1,3,6,1,4,1,10876,101,1,24,2,2,1,2),_DhcpRelayIfRemoteId_Type())
dhcpRelayIfRemoteId.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayIfRemoteId.setStatus(_A)
_DhcpRelayIfRowStatus_Type=RowStatus
_DhcpRelayIfRowStatus_Object=MibTableColumn
dhcpRelayIfRowStatus=_DhcpRelayIfRowStatus_Object((1,3,6,1,4,1,10876,101,1,24,2,2,1,3),_DhcpRelayIfRowStatus_Type())
dhcpRelayIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpRelayIfRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'futureDhcpRelay':futureDhcpRelay,'dhcpRelay':dhcpRelay,'dhcpRelaying':dhcpRelaying,'dhcpRelayServersOnly':dhcpRelayServersOnly,'dhcpRelaySecsThreshold':dhcpRelaySecsThreshold,'dhcpRelayHopsThreshold':dhcpRelayHopsThreshold,'dhcpRelayRAIOptionControl':dhcpRelayRAIOptionControl,'dhcpRelayRAICircuitIDSubOptionControl':dhcpRelayRAICircuitIDSubOptionControl,'dhcpRelayRAIRemoteIDSubOptionControl':dhcpRelayRAIRemoteIDSubOptionControl,'dhcpRelayRAISubnetMaskSubOptionControl':dhcpRelayRAISubnetMaskSubOptionControl,'dhcpRelayRAIOptionInserted':dhcpRelayRAIOptionInserted,'dhcpRelayRAICircuitIDSubOptionInserted':dhcpRelayRAICircuitIDSubOptionInserted,'dhcpRelayRAIRemoteIDSubOptionInserted':dhcpRelayRAIRemoteIDSubOptionInserted,'dhcpRelayRAISubnetMaskSubOptionInserted':dhcpRelayRAISubnetMaskSubOptionInserted,'dhcpRelayRAIOptionWronglySet':dhcpRelayRAIOptionWronglySet,'dhcpRelayRAISpaceConstraint':dhcpRelayRAISpaceConstraint,'dhcpConfigTraceLevel':dhcpConfigTraceLevel,'dhcpConfigDhcpCircuitOption':dhcpConfigDhcpCircuitOption,'dhcpRelayCounterReset':dhcpRelayCounterReset,'dhcpRelayTable':dhcpRelayTable,'dhcpRelaySrvAddressTable':dhcpRelaySrvAddressTable,'dhcpRelaySrvAddressEntry':dhcpRelaySrvAddressEntry,_J:dhcpRelaySrvIpAddress,'dhcpRelaySrvAddressRowStatus':dhcpRelaySrvAddressRowStatus,'dhcpRelayIfTable':dhcpRelayIfTable,'dhcpRelayIfEntry':dhcpRelayIfEntry,'dhcpRelayIfCircuitId':dhcpRelayIfCircuitId,'dhcpRelayIfRemoteId':dhcpRelayIfRemoteId,'dhcpRelayIfRowStatus':dhcpRelayIfRowStatus})