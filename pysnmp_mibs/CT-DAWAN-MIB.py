_I='ctDAWanTNListIndex'
_H='unknown'
_G='OctetString'
_F='ctDAWanDeviceIndex'
_E='CT-DAWAN-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
class TimeStamp(TimeTicks):0
_CtSSA_ObjectIdentity=ObjectIdentity
ctSSA=_CtSSA_ObjectIdentity((1,3,6,1,4,1,52,4497))
_CtDAWanDevices_ObjectIdentity=ObjectIdentity
ctDAWanDevices=_CtDAWanDevices_ObjectIdentity((1,3,6,1,4,1,52,4497,16))
_CtDAWanDeviceNumDevices_Type=Integer32
_CtDAWanDeviceNumDevices_Object=MibScalar
ctDAWanDeviceNumDevices=_CtDAWanDeviceNumDevices_Object((1,3,6,1,4,1,52,4497,16,1),_CtDAWanDeviceNumDevices_Type())
ctDAWanDeviceNumDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceNumDevices.setStatus(_A)
_CtDAWanDevicesTable_Object=MibTable
ctDAWanDevicesTable=_CtDAWanDevicesTable_Object((1,3,6,1,4,1,52,4497,16,2))
if mibBuilder.loadTexts:ctDAWanDevicesTable.setStatus(_A)
_CtDAWanDeviceEntry_Object=MibTableRow
ctDAWanDeviceEntry=_CtDAWanDeviceEntry_Object((1,3,6,1,4,1,52,4497,16,2,1))
ctDAWanDeviceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ctDAWanDeviceEntry.setStatus(_A)
class _CtDAWanDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtDAWanDeviceIndex_Type.__name__=_C
_CtDAWanDeviceIndex_Object=MibTableColumn
ctDAWanDeviceIndex=_CtDAWanDeviceIndex_Object((1,3,6,1,4,1,52,4497,16,2,1,1),_CtDAWanDeviceIndex_Type())
ctDAWanDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceIndex.setStatus(_A)
_CtDAWanDeviceIfIndex_Type=Integer32
_CtDAWanDeviceIfIndex_Object=MibTableColumn
ctDAWanDeviceIfIndex=_CtDAWanDeviceIfIndex_Object((1,3,6,1,4,1,52,4497,16,2,1,2),_CtDAWanDeviceIfIndex_Type())
ctDAWanDeviceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceIfIndex.setStatus(_A)
_CtDAWanDeviceSessionID_Type=Gauge32
_CtDAWanDeviceSessionID_Object=MibTableColumn
ctDAWanDeviceSessionID=_CtDAWanDeviceSessionID_Object((1,3,6,1,4,1,52,4497,16,2,1,3),_CtDAWanDeviceSessionID_Type())
ctDAWanDeviceSessionID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceSessionID.setStatus(_A)
class _CtDAWanDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('inactive',1),('connecting',2),('active',3),('disconnecting',4)))
_CtDAWanDeviceState_Type.__name__=_C
_CtDAWanDeviceState_Object=MibTableColumn
ctDAWanDeviceState=_CtDAWanDeviceState_Object((1,3,6,1,4,1,52,4497,16,2,1,4),_CtDAWanDeviceState_Type())
ctDAWanDeviceState.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceState.setStatus(_A)
class _CtDAWanDeviceDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtDAWanDeviceDescr_Type.__name__=_D
_CtDAWanDeviceDescr_Object=MibTableColumn
ctDAWanDeviceDescr=_CtDAWanDeviceDescr_Object((1,3,6,1,4,1,52,4497,16,2,1,5),_CtDAWanDeviceDescr_Type())
ctDAWanDeviceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceDescr.setStatus(_A)
class _CtDAWanDeviceConnectControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connect',1),('disconnect',2),(_H,3)))
_CtDAWanDeviceConnectControl_Type.__name__=_C
_CtDAWanDeviceConnectControl_Object=MibTableColumn
ctDAWanDeviceConnectControl=_CtDAWanDeviceConnectControl_Object((1,3,6,1,4,1,52,4497,16,2,1,6),_CtDAWanDeviceConnectControl_Type())
ctDAWanDeviceConnectControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctDAWanDeviceConnectControl.setStatus(_A)
class _CtDAWanDeviceConnectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('digitalCircuit',1),('analogCircuit',2)))
_CtDAWanDeviceConnectType_Type.__name__=_C
_CtDAWanDeviceConnectType_Object=MibTableColumn
ctDAWanDeviceConnectType=_CtDAWanDeviceConnectType_Object((1,3,6,1,4,1,52,4497,16,2,1,7),_CtDAWanDeviceConnectType_Type())
ctDAWanDeviceConnectType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceConnectType.setStatus(_A)
class _CtDAWanDeviceL2Encapsulation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('ppp',2)))
_CtDAWanDeviceL2Encapsulation_Type.__name__=_C
_CtDAWanDeviceL2Encapsulation_Object=MibTableColumn
ctDAWanDeviceL2Encapsulation=_CtDAWanDeviceL2Encapsulation_Object((1,3,6,1,4,1,52,4497,16,2,1,8),_CtDAWanDeviceL2Encapsulation_Type())
ctDAWanDeviceL2Encapsulation.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceL2Encapsulation.setStatus(_A)
class _CtDAWanDeviceNumConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtDAWanDeviceNumConnections_Type.__name__=_C
_CtDAWanDeviceNumConnections_Object=MibTableColumn
ctDAWanDeviceNumConnections=_CtDAWanDeviceNumConnections_Object((1,3,6,1,4,1,52,4497,16,2,1,9),_CtDAWanDeviceNumConnections_Type())
ctDAWanDeviceNumConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceNumConnections.setStatus(_A)
_CtDAWanDeviceCurrentBandwidth_Type=Gauge32
_CtDAWanDeviceCurrentBandwidth_Object=MibTableColumn
ctDAWanDeviceCurrentBandwidth=_CtDAWanDeviceCurrentBandwidth_Object((1,3,6,1,4,1,52,4497,16,2,1,10),_CtDAWanDeviceCurrentBandwidth_Type())
ctDAWanDeviceCurrentBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceCurrentBandwidth.setStatus(_A)
_CtDAWanDeviceInitialBandwidth_Type=Gauge32
_CtDAWanDeviceInitialBandwidth_Object=MibTableColumn
ctDAWanDeviceInitialBandwidth=_CtDAWanDeviceInitialBandwidth_Object((1,3,6,1,4,1,52,4497,16,2,1,11),_CtDAWanDeviceInitialBandwidth_Type())
ctDAWanDeviceInitialBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceInitialBandwidth.setStatus(_A)
_CtDAWanDeviceMaxBandwidth_Type=Gauge32
_CtDAWanDeviceMaxBandwidth_Object=MibTableColumn
ctDAWanDeviceMaxBandwidth=_CtDAWanDeviceMaxBandwidth_Object((1,3,6,1,4,1,52,4497,16,2,1,12),_CtDAWanDeviceMaxBandwidth_Type())
ctDAWanDeviceMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceMaxBandwidth.setStatus(_A)
class _CtDAWanDeviceH0Support_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_CtDAWanDeviceH0Support_Type.__name__=_C
_CtDAWanDeviceH0Support_Object=MibTableColumn
ctDAWanDeviceH0Support=_CtDAWanDeviceH0Support_Object((1,3,6,1,4,1,52,4497,16,2,1,13),_CtDAWanDeviceH0Support_Type())
ctDAWanDeviceH0Support.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceH0Support.setStatus(_A)
_CtDAWanDeviceChargedUnits_Type=Gauge32
_CtDAWanDeviceChargedUnits_Object=MibTableColumn
ctDAWanDeviceChargedUnits=_CtDAWanDeviceChargedUnits_Object((1,3,6,1,4,1,52,4497,16,2,1,14),_CtDAWanDeviceChargedUnits_Type())
ctDAWanDeviceChargedUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceChargedUnits.setStatus(_A)
_CtDAWanDeviceSuccessCalls_Type=Gauge32
_CtDAWanDeviceSuccessCalls_Object=MibTableColumn
ctDAWanDeviceSuccessCalls=_CtDAWanDeviceSuccessCalls_Object((1,3,6,1,4,1,52,4497,16,2,1,15),_CtDAWanDeviceSuccessCalls_Type())
ctDAWanDeviceSuccessCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceSuccessCalls.setStatus(_A)
_CtDAWanDeviceFailCalls_Type=Gauge32
_CtDAWanDeviceFailCalls_Object=MibTableColumn
ctDAWanDeviceFailCalls=_CtDAWanDeviceFailCalls_Object((1,3,6,1,4,1,52,4497,16,2,1,16),_CtDAWanDeviceFailCalls_Type())
ctDAWanDeviceFailCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceFailCalls.setStatus(_A)
_CtDAWanDeviceAcceptCalls_Type=Gauge32
_CtDAWanDeviceAcceptCalls_Object=MibTableColumn
ctDAWanDeviceAcceptCalls=_CtDAWanDeviceAcceptCalls_Object((1,3,6,1,4,1,52,4497,16,2,1,17),_CtDAWanDeviceAcceptCalls_Type())
ctDAWanDeviceAcceptCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceAcceptCalls.setStatus(_A)
_CtDAWanDeviceRefuseCalls_Type=Gauge32
_CtDAWanDeviceRefuseCalls_Object=MibTableColumn
ctDAWanDeviceRefuseCalls=_CtDAWanDeviceRefuseCalls_Object((1,3,6,1,4,1,52,4497,16,2,1,18),_CtDAWanDeviceRefuseCalls_Type())
ctDAWanDeviceRefuseCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceRefuseCalls.setStatus(_A)
_CtDAWanDeviceConnectTime_Type=TimeStamp
_CtDAWanDeviceConnectTime_Object=MibTableColumn
ctDAWanDeviceConnectTime=_CtDAWanDeviceConnectTime_Object((1,3,6,1,4,1,52,4497,16,2,1,19),_CtDAWanDeviceConnectTime_Type())
ctDAWanDeviceConnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceConnectTime.setStatus(_A)
class _CtDAWanDeviceConnectDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_CtDAWanDeviceConnectDirection_Type.__name__=_C
_CtDAWanDeviceConnectDirection_Object=MibTableColumn
ctDAWanDeviceConnectDirection=_CtDAWanDeviceConnectDirection_Object((1,3,6,1,4,1,52,4497,16,2,1,20),_CtDAWanDeviceConnectDirection_Type())
ctDAWanDeviceConnectDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceConnectDirection.setStatus(_A)
_CtDAWanDeviceLastDisconnectTime_Type=TimeStamp
_CtDAWanDeviceLastDisconnectTime_Object=MibTableColumn
ctDAWanDeviceLastDisconnectTime=_CtDAWanDeviceLastDisconnectTime_Object((1,3,6,1,4,1,52,4497,16,2,1,21),_CtDAWanDeviceLastDisconnectTime_Type())
ctDAWanDeviceLastDisconnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceLastDisconnectTime.setStatus(_A)
class _CtDAWanDeviceLastDisconnectDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_CtDAWanDeviceLastDisconnectDirection_Type.__name__=_C
_CtDAWanDeviceLastDisconnectDirection_Object=MibTableColumn
ctDAWanDeviceLastDisconnectDirection=_CtDAWanDeviceLastDisconnectDirection_Object((1,3,6,1,4,1,52,4497,16,2,1,22),_CtDAWanDeviceLastDisconnectDirection_Type())
ctDAWanDeviceLastDisconnectDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceLastDisconnectDirection.setStatus(_A)
class _CtDAWanDeviceLastDisconnectCause_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_CtDAWanDeviceLastDisconnectCause_Type.__name__=_G
_CtDAWanDeviceLastDisconnectCause_Object=MibTableColumn
ctDAWanDeviceLastDisconnectCause=_CtDAWanDeviceLastDisconnectCause_Object((1,3,6,1,4,1,52,4497,16,2,1,23),_CtDAWanDeviceLastDisconnectCause_Type())
ctDAWanDeviceLastDisconnectCause.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceLastDisconnectCause.setStatus(_A)
class _CtDAWanDeviceLastDisconnectText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtDAWanDeviceLastDisconnectText_Type.__name__=_D
_CtDAWanDeviceLastDisconnectText_Object=MibTableColumn
ctDAWanDeviceLastDisconnectText=_CtDAWanDeviceLastDisconnectText_Object((1,3,6,1,4,1,52,4497,16,2,1,24),_CtDAWanDeviceLastDisconnectText_Type())
ctDAWanDeviceLastDisconnectText.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanDeviceLastDisconnectText.setStatus(_A)
_CtDAWanTNListTable_Object=MibTable
ctDAWanTNListTable=_CtDAWanTNListTable_Object((1,3,6,1,4,1,52,4497,16,3))
if mibBuilder.loadTexts:ctDAWanTNListTable.setStatus(_A)
_CtDAWanTNListEntry_Object=MibTableRow
ctDAWanTNListEntry=_CtDAWanTNListEntry_Object((1,3,6,1,4,1,52,4497,16,3,1))
ctDAWanTNListEntry.setIndexNames((0,_E,_F),(0,_E,_I))
if mibBuilder.loadTexts:ctDAWanTNListEntry.setStatus(_A)
class _CtDAWanTNListIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CtDAWanTNListIndex_Type.__name__=_C
_CtDAWanTNListIndex_Object=MibTableColumn
ctDAWanTNListIndex=_CtDAWanTNListIndex_Object((1,3,6,1,4,1,52,4497,16,3,1,1),_CtDAWanTNListIndex_Type())
ctDAWanTNListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanTNListIndex.setStatus(_A)
class _CtDAWanTN_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CtDAWanTN_Type.__name__=_D
_CtDAWanTN_Object=MibTableColumn
ctDAWanTN=_CtDAWanTN_Object((1,3,6,1,4,1,52,4497,16,3,1,2),_CtDAWanTN_Type())
ctDAWanTN.setMaxAccess(_B)
if mibBuilder.loadTexts:ctDAWanTN.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_D:DisplayString,'TimeStamp':TimeStamp,'ctSSA':ctSSA,'ctDAWanDevices':ctDAWanDevices,'ctDAWanDeviceNumDevices':ctDAWanDeviceNumDevices,'ctDAWanDevicesTable':ctDAWanDevicesTable,'ctDAWanDeviceEntry':ctDAWanDeviceEntry,_F:ctDAWanDeviceIndex,'ctDAWanDeviceIfIndex':ctDAWanDeviceIfIndex,'ctDAWanDeviceSessionID':ctDAWanDeviceSessionID,'ctDAWanDeviceState':ctDAWanDeviceState,'ctDAWanDeviceDescr':ctDAWanDeviceDescr,'ctDAWanDeviceConnectControl':ctDAWanDeviceConnectControl,'ctDAWanDeviceConnectType':ctDAWanDeviceConnectType,'ctDAWanDeviceL2Encapsulation':ctDAWanDeviceL2Encapsulation,'ctDAWanDeviceNumConnections':ctDAWanDeviceNumConnections,'ctDAWanDeviceCurrentBandwidth':ctDAWanDeviceCurrentBandwidth,'ctDAWanDeviceInitialBandwidth':ctDAWanDeviceInitialBandwidth,'ctDAWanDeviceMaxBandwidth':ctDAWanDeviceMaxBandwidth,'ctDAWanDeviceH0Support':ctDAWanDeviceH0Support,'ctDAWanDeviceChargedUnits':ctDAWanDeviceChargedUnits,'ctDAWanDeviceSuccessCalls':ctDAWanDeviceSuccessCalls,'ctDAWanDeviceFailCalls':ctDAWanDeviceFailCalls,'ctDAWanDeviceAcceptCalls':ctDAWanDeviceAcceptCalls,'ctDAWanDeviceRefuseCalls':ctDAWanDeviceRefuseCalls,'ctDAWanDeviceConnectTime':ctDAWanDeviceConnectTime,'ctDAWanDeviceConnectDirection':ctDAWanDeviceConnectDirection,'ctDAWanDeviceLastDisconnectTime':ctDAWanDeviceLastDisconnectTime,'ctDAWanDeviceLastDisconnectDirection':ctDAWanDeviceLastDisconnectDirection,'ctDAWanDeviceLastDisconnectCause':ctDAWanDeviceLastDisconnectCause,'ctDAWanDeviceLastDisconnectText':ctDAWanDeviceLastDisconnectText,'ctDAWanTNListTable':ctDAWanTNListTable,'ctDAWanTNListEntry':ctDAWanTNListEntry,_I:ctDAWanTNListIndex,'ctDAWanTN':ctDAWanTN})