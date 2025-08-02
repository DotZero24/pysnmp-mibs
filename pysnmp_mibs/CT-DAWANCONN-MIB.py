_F='daWanConnectionIndex'
_E='CT-DAWANCONN-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cabletron,=mibBuilder.importSymbols('CTRON-OIDS','cabletron')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TimeStamp')
class DisplayString(OctetString):0
_CtSSA_ObjectIdentity=ObjectIdentity
ctSSA=_CtSSA_ObjectIdentity((1,3,6,1,4,1,52,4497))
_DaWanConnection_ObjectIdentity=ObjectIdentity
daWanConnection=_DaWanConnection_ObjectIdentity((1,3,6,1,4,1,52,4497,17))
class _DaWanNumConnections_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DaWanNumConnections_Type.__name__=_C
_DaWanNumConnections_Object=MibScalar
daWanNumConnections=_DaWanNumConnections_Object((1,3,6,1,4,1,52,4497,17,1),_DaWanNumConnections_Type())
daWanNumConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanNumConnections.setStatus(_A)
_DaWanConnectionTable_Object=MibTable
daWanConnectionTable=_DaWanConnectionTable_Object((1,3,6,1,4,1,52,4497,17,2))
if mibBuilder.loadTexts:daWanConnectionTable.setStatus(_A)
_DaWanConnectionEntry_Object=MibTableRow
daWanConnectionEntry=_DaWanConnectionEntry_Object((1,3,6,1,4,1,52,4497,17,2,1))
daWanConnectionEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:daWanConnectionEntry.setStatus(_A)
class _DaWanConnectionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DaWanConnectionIndex_Type.__name__=_C
_DaWanConnectionIndex_Object=MibTableColumn
daWanConnectionIndex=_DaWanConnectionIndex_Object((1,3,6,1,4,1,52,4497,17,2,1,1),_DaWanConnectionIndex_Type())
daWanConnectionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionIndex.setStatus(_A)
_DaWanConnectionIfIndex_Type=Integer32
_DaWanConnectionIfIndex_Object=MibTableColumn
daWanConnectionIfIndex=_DaWanConnectionIfIndex_Object((1,3,6,1,4,1,52,4497,17,2,1,2),_DaWanConnectionIfIndex_Type())
daWanConnectionIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionIfIndex.setStatus(_A)
class _DaWanConnectionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',1),('connecting',2),('connected',3),('active',4),('disconnecting',5),('disconnected',6)))
_DaWanConnectionState_Type.__name__=_C
_DaWanConnectionState_Object=MibTableColumn
daWanConnectionState=_DaWanConnectionState_Object((1,3,6,1,4,1,52,4497,17,2,1,3),_DaWanConnectionState_Type())
daWanConnectionState.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionState.setStatus(_A)
class _DaWanConnectionConnectControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('connect',1),('disconnect',2),('unknown',3)))
_DaWanConnectionConnectControl_Type.__name__=_C
_DaWanConnectionConnectControl_Object=MibTableColumn
daWanConnectionConnectControl=_DaWanConnectionConnectControl_Object((1,3,6,1,4,1,52,4497,17,2,1,4),_DaWanConnectionConnectControl_Type())
daWanConnectionConnectControl.setMaxAccess('read-write')
if mibBuilder.loadTexts:daWanConnectionConnectControl.setStatus(_A)
class _DaWanConnectionConnectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('digitalCircuit',1),('analogCircuit',2)))
_DaWanConnectionConnectType_Type.__name__=_C
_DaWanConnectionConnectType_Object=MibTableColumn
daWanConnectionConnectType=_DaWanConnectionConnectType_Object((1,3,6,1,4,1,52,4497,17,2,1,5),_DaWanConnectionConnectType_Type())
daWanConnectionConnectType.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionConnectType.setStatus(_A)
_DaWanConnectionDeviceIndex_Type=Integer32
_DaWanConnectionDeviceIndex_Object=MibTableColumn
daWanConnectionDeviceIndex=_DaWanConnectionDeviceIndex_Object((1,3,6,1,4,1,52,4497,17,2,1,6),_DaWanConnectionDeviceIndex_Type())
daWanConnectionDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionDeviceIndex.setStatus(_A)
_DaWanConnectionConnectSpeed_Type=Gauge32
_DaWanConnectionConnectSpeed_Object=MibTableColumn
daWanConnectionConnectSpeed=_DaWanConnectionConnectSpeed_Object((1,3,6,1,4,1,52,4497,17,2,1,7),_DaWanConnectionConnectSpeed_Type())
daWanConnectionConnectSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionConnectSpeed.setStatus(_A)
class _DaWanConnectionLocalAddress_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DaWanConnectionLocalAddress_Type.__name__=_D
_DaWanConnectionLocalAddress_Object=MibTableColumn
daWanConnectionLocalAddress=_DaWanConnectionLocalAddress_Object((1,3,6,1,4,1,52,4497,17,2,1,8),_DaWanConnectionLocalAddress_Type())
daWanConnectionLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionLocalAddress.setStatus(_A)
class _DaWanConnectionPeerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DaWanConnectionPeerAddress_Type.__name__=_D
_DaWanConnectionPeerAddress_Object=MibTableColumn
daWanConnectionPeerAddress=_DaWanConnectionPeerAddress_Object((1,3,6,1,4,1,52,4497,17,2,1,9),_DaWanConnectionPeerAddress_Type())
daWanConnectionPeerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionPeerAddress.setStatus(_A)
class _DaWanConnectionSubAddress_Type(DisplayString):defaultHexValue='';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DaWanConnectionSubAddress_Type.__name__=_D
_DaWanConnectionSubAddress_Object=MibTableColumn
daWanConnectionSubAddress=_DaWanConnectionSubAddress_Object((1,3,6,1,4,1,52,4497,17,2,1,10),_DaWanConnectionSubAddress_Type())
daWanConnectionSubAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionSubAddress.setStatus(_A)
class _DaWanConnectionInfoType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('speech',2),('unrestrictedDigital',3),('unrestrictedDigital56',4),('restrictedDigital',5),('audio31',6),('audio7',7),('video',8),('packetSwitched',9),('fax',10)))
_DaWanConnectionInfoType_Type.__name__=_C
_DaWanConnectionInfoType_Object=MibTableColumn
daWanConnectionInfoType=_DaWanConnectionInfoType_Object((1,3,6,1,4,1,52,4497,17,2,1,11),_DaWanConnectionInfoType_Type())
daWanConnectionInfoType.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionInfoType.setStatus(_A)
_DaWanConnectionChargedUnits_Type=Integer32
_DaWanConnectionChargedUnits_Object=MibTableColumn
daWanConnectionChargedUnits=_DaWanConnectionChargedUnits_Object((1,3,6,1,4,1,52,4497,17,2,1,12),_DaWanConnectionChargedUnits_Type())
daWanConnectionChargedUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionChargedUnits.setStatus(_A)
_DaWanConnectionConnectTime_Type=TimeStamp
_DaWanConnectionConnectTime_Object=MibTableColumn
daWanConnectionConnectTime=_DaWanConnectionConnectTime_Object((1,3,6,1,4,1,52,4497,17,2,1,13),_DaWanConnectionConnectTime_Type())
daWanConnectionConnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionConnectTime.setStatus(_A)
class _DaWanConnectionConnectDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_DaWanConnectionConnectDirection_Type.__name__=_C
_DaWanConnectionConnectDirection_Object=MibTableColumn
daWanConnectionConnectDirection=_DaWanConnectionConnectDirection_Object((1,3,6,1,4,1,52,4497,17,2,1,14),_DaWanConnectionConnectDirection_Type())
daWanConnectionConnectDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionConnectDirection.setStatus(_A)
_DaWanConnectionDisconnectTime_Type=TimeStamp
_DaWanConnectionDisconnectTime_Object=MibTableColumn
daWanConnectionDisconnectTime=_DaWanConnectionDisconnectTime_Object((1,3,6,1,4,1,52,4497,17,2,1,15),_DaWanConnectionDisconnectTime_Type())
daWanConnectionDisconnectTime.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionDisconnectTime.setStatus(_A)
class _DaWanConnectionDisconnectDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_DaWanConnectionDisconnectDirection_Type.__name__=_C
_DaWanConnectionDisconnectDirection_Object=MibTableColumn
daWanConnectionDisconnectDirection=_DaWanConnectionDisconnectDirection_Object((1,3,6,1,4,1,52,4497,17,2,1,16),_DaWanConnectionDisconnectDirection_Type())
daWanConnectionDisconnectDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionDisconnectDirection.setStatus(_A)
_DaWanConnectionDisconnectCause_Type=Integer32
_DaWanConnectionDisconnectCause_Object=MibTableColumn
daWanConnectionDisconnectCause=_DaWanConnectionDisconnectCause_Object((1,3,6,1,4,1,52,4497,17,2,1,17),_DaWanConnectionDisconnectCause_Type())
daWanConnectionDisconnectCause.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionDisconnectCause.setStatus(_A)
class _DaWanConnectionDisconnectText_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DaWanConnectionDisconnectText_Type.__name__=_D
_DaWanConnectionDisconnectText_Object=MibTableColumn
daWanConnectionDisconnectText=_DaWanConnectionDisconnectText_Object((1,3,6,1,4,1,52,4497,17,2,1,18),_DaWanConnectionDisconnectText_Type())
daWanConnectionDisconnectText.setMaxAccess(_B)
if mibBuilder.loadTexts:daWanConnectionDisconnectText.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_D:DisplayString,'ctSSA':ctSSA,'daWanConnection':daWanConnection,'daWanNumConnections':daWanNumConnections,'daWanConnectionTable':daWanConnectionTable,'daWanConnectionEntry':daWanConnectionEntry,_F:daWanConnectionIndex,'daWanConnectionIfIndex':daWanConnectionIfIndex,'daWanConnectionState':daWanConnectionState,'daWanConnectionConnectControl':daWanConnectionConnectControl,'daWanConnectionConnectType':daWanConnectionConnectType,'daWanConnectionDeviceIndex':daWanConnectionDeviceIndex,'daWanConnectionConnectSpeed':daWanConnectionConnectSpeed,'daWanConnectionLocalAddress':daWanConnectionLocalAddress,'daWanConnectionPeerAddress':daWanConnectionPeerAddress,'daWanConnectionSubAddress':daWanConnectionSubAddress,'daWanConnectionInfoType':daWanConnectionInfoType,'daWanConnectionChargedUnits':daWanConnectionChargedUnits,'daWanConnectionConnectTime':daWanConnectionConnectTime,'daWanConnectionConnectDirection':daWanConnectionConnectDirection,'daWanConnectionDisconnectTime':daWanConnectionDisconnectTime,'daWanConnectionDisconnectDirection':daWanConnectionDisconnectDirection,'daWanConnectionDisconnectCause':daWanConnectionDisconnectCause,'daWanConnectionDisconnectText':daWanConnectionDisconnectText})