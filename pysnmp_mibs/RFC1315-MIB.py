_J='frErrIfIndex'
_I='frCircuitDlci'
_H='frCircuitIfIndex'
_G='frDlcmiIfIndex'
_F='NotificationType'
_E='RFC1315-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Frpublic_ObjectIdentity=ObjectIdentity
frpublic=_Frpublic_ObjectIdentity((1,3,6,1,2,1,10,32))
_FrDlcmiTable_Object=MibTable
frDlcmiTable=_FrDlcmiTable_Object((1,3,6,1,2,1,10,32,1))
if mibBuilder.loadTexts:frDlcmiTable.setStatus(_A)
_FrDlcmiEntry_Object=MibTableRow
frDlcmiEntry=_FrDlcmiEntry_Object((1,3,6,1,2,1,10,32,1,1))
frDlcmiEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:frDlcmiEntry.setStatus(_A)
_FrDlcmiIfIndex_Type=Integer32
_FrDlcmiIfIndex_Object=MibTableColumn
frDlcmiIfIndex=_FrDlcmiIfIndex_Object((1,3,6,1,2,1,10,32,1,1,1),_FrDlcmiIfIndex_Type())
frDlcmiIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:frDlcmiIfIndex.setStatus(_A)
class _FrDlcmiState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noLmiConfigured',1),('lmiRev1',2),('ansiT1-617-D',3),('ansiT1-617-B',4),('q933a',5),('original-lmi',6)))
_FrDlcmiState_Type.__name__=_B
_FrDlcmiState_Object=MibTableColumn
frDlcmiState=_FrDlcmiState_Object((1,3,6,1,2,1,10,32,1,1,2),_FrDlcmiState_Type())
frDlcmiState.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiState.setStatus(_A)
class _FrDlcmiAddress_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('q921',1),('q922March90',2),('q922November90',3),('q922',4)))
_FrDlcmiAddress_Type.__name__=_B
_FrDlcmiAddress_Object=MibTableColumn
frDlcmiAddress=_FrDlcmiAddress_Object((1,3,6,1,2,1,10,32,1,1,3),_FrDlcmiAddress_Type())
frDlcmiAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiAddress.setStatus(_A)
class _FrDlcmiAddressLen_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*(('two-octets',2),('three-octets',3),('four-octets',4)))
_FrDlcmiAddressLen_Type.__name__=_B
_FrDlcmiAddressLen_Object=MibTableColumn
frDlcmiAddressLen=_FrDlcmiAddressLen_Object((1,3,6,1,2,1,10,32,1,1,4),_FrDlcmiAddressLen_Type())
frDlcmiAddressLen.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiAddressLen.setStatus(_A)
class _FrDlcmiPollingInterval_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,30))
_FrDlcmiPollingInterval_Type.__name__=_B
_FrDlcmiPollingInterval_Object=MibTableColumn
frDlcmiPollingInterval=_FrDlcmiPollingInterval_Object((1,3,6,1,2,1,10,32,1,1,5),_FrDlcmiPollingInterval_Type())
frDlcmiPollingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiPollingInterval.setStatus(_A)
class _FrDlcmiFullEnquiryInterval_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FrDlcmiFullEnquiryInterval_Type.__name__=_B
_FrDlcmiFullEnquiryInterval_Object=MibTableColumn
frDlcmiFullEnquiryInterval=_FrDlcmiFullEnquiryInterval_Object((1,3,6,1,2,1,10,32,1,1,6),_FrDlcmiFullEnquiryInterval_Type())
frDlcmiFullEnquiryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiFullEnquiryInterval.setStatus(_A)
class _FrDlcmiErrorThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrDlcmiErrorThreshold_Type.__name__=_B
_FrDlcmiErrorThreshold_Object=MibTableColumn
frDlcmiErrorThreshold=_FrDlcmiErrorThreshold_Object((1,3,6,1,2,1,10,32,1,1,7),_FrDlcmiErrorThreshold_Type())
frDlcmiErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiErrorThreshold.setStatus(_A)
class _FrDlcmiMonitoredEvents_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrDlcmiMonitoredEvents_Type.__name__=_B
_FrDlcmiMonitoredEvents_Object=MibTableColumn
frDlcmiMonitoredEvents=_FrDlcmiMonitoredEvents_Object((1,3,6,1,2,1,10,32,1,1,8),_FrDlcmiMonitoredEvents_Type())
frDlcmiMonitoredEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiMonitoredEvents.setStatus(_A)
class _FrDlcmiMaxSupportedVCs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_FrDlcmiMaxSupportedVCs_Type.__name__=_B
_FrDlcmiMaxSupportedVCs_Object=MibTableColumn
frDlcmiMaxSupportedVCs=_FrDlcmiMaxSupportedVCs_Object((1,3,6,1,2,1,10,32,1,1,9),_FrDlcmiMaxSupportedVCs_Type())
frDlcmiMaxSupportedVCs.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiMaxSupportedVCs.setStatus(_A)
class _FrDlcmiMulticast_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonBroadcast',1),('broadcast',2)))
_FrDlcmiMulticast_Type.__name__=_B
_FrDlcmiMulticast_Object=MibTableColumn
frDlcmiMulticast=_FrDlcmiMulticast_Object((1,3,6,1,2,1,10,32,1,1,10),_FrDlcmiMulticast_Type())
frDlcmiMulticast.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiMulticast.setStatus(_A)
class _FrDlcmiDceIdleInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,60))
_FrDlcmiDceIdleInterval_Type.__name__=_B
_FrDlcmiDceIdleInterval_Object=MibTableColumn
frDlcmiDceIdleInterval=_FrDlcmiDceIdleInterval_Object((1,3,6,1,2,1,10,32,1,1,42),_FrDlcmiDceIdleInterval_Type())
frDlcmiDceIdleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiDceIdleInterval.setStatus(_A)
class _FrDlcmiDceErrorThreshold_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrDlcmiDceErrorThreshold_Type.__name__=_B
_FrDlcmiDceErrorThreshold_Object=MibTableColumn
frDlcmiDceErrorThreshold=_FrDlcmiDceErrorThreshold_Object((1,3,6,1,2,1,10,32,1,1,43),_FrDlcmiDceErrorThreshold_Type())
frDlcmiDceErrorThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiDceErrorThreshold.setStatus(_A)
class _FrDlcmiDceMonitoredEvents_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FrDlcmiDceMonitoredEvents_Type.__name__=_B
_FrDlcmiDceMonitoredEvents_Object=MibTableColumn
frDlcmiDceMonitoredEvents=_FrDlcmiDceMonitoredEvents_Object((1,3,6,1,2,1,10,32,1,1,44),_FrDlcmiDceMonitoredEvents_Type())
frDlcmiDceMonitoredEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiDceMonitoredEvents.setStatus(_A)
class _FrDlcmiMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dte',1),('dce',2),('nni',3)))
_FrDlcmiMode_Type.__name__=_B
_FrDlcmiMode_Object=MibTableColumn
frDlcmiMode=_FrDlcmiMode_Object((1,3,6,1,2,1,10,32,1,1,45),_FrDlcmiMode_Type())
frDlcmiMode.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiMode.setStatus(_A)
class _FrDlcmiDefaultRouteIfIndex_Type(Integer32):defaultValue=0
_FrDlcmiDefaultRouteIfIndex_Type.__name__=_B
_FrDlcmiDefaultRouteIfIndex_Object=MibTableColumn
frDlcmiDefaultRouteIfIndex=_FrDlcmiDefaultRouteIfIndex_Object((1,3,6,1,2,1,10,32,1,1,46),_FrDlcmiDefaultRouteIfIndex_Type())
frDlcmiDefaultRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frDlcmiDefaultRouteIfIndex.setStatus(_A)
_FrCircuitTable_Object=MibTable
frCircuitTable=_FrCircuitTable_Object((1,3,6,1,2,1,10,32,2))
if mibBuilder.loadTexts:frCircuitTable.setStatus(_A)
_FrCircuitEntry_Object=MibTableRow
frCircuitEntry=_FrCircuitEntry_Object((1,3,6,1,2,1,10,32,2,1))
frCircuitEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:frCircuitEntry.setStatus(_A)
_FrCircuitIfIndex_Type=Integer32
_FrCircuitIfIndex_Object=MibTableColumn
frCircuitIfIndex=_FrCircuitIfIndex_Object((1,3,6,1,2,1,10,32,2,1,1),_FrCircuitIfIndex_Type())
frCircuitIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitIfIndex.setStatus(_A)
_FrCircuitDlci_Type=Integer32
_FrCircuitDlci_Object=MibTableColumn
frCircuitDlci=_FrCircuitDlci_Object((1,3,6,1,2,1,10,32,2,1,2),_FrCircuitDlci_Type())
frCircuitDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitDlci.setStatus(_A)
class _FrCircuitState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('invalid',1),('active',2),('inactive',3)))
_FrCircuitState_Type.__name__=_B
_FrCircuitState_Object=MibTableColumn
frCircuitState=_FrCircuitState_Object((1,3,6,1,2,1,10,32,2,1,3),_FrCircuitState_Type())
frCircuitState.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitState.setStatus(_A)
_FrCircuitReceivedFECNs_Type=Counter32
_FrCircuitReceivedFECNs_Object=MibTableColumn
frCircuitReceivedFECNs=_FrCircuitReceivedFECNs_Object((1,3,6,1,2,1,10,32,2,1,4),_FrCircuitReceivedFECNs_Type())
frCircuitReceivedFECNs.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitReceivedFECNs.setStatus(_A)
_FrCircuitReceivedBECNs_Type=Counter32
_FrCircuitReceivedBECNs_Object=MibTableColumn
frCircuitReceivedBECNs=_FrCircuitReceivedBECNs_Object((1,3,6,1,2,1,10,32,2,1,5),_FrCircuitReceivedBECNs_Type())
frCircuitReceivedBECNs.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitReceivedBECNs.setStatus(_A)
_FrCircuitSentFrames_Type=Counter32
_FrCircuitSentFrames_Object=MibTableColumn
frCircuitSentFrames=_FrCircuitSentFrames_Object((1,3,6,1,2,1,10,32,2,1,6),_FrCircuitSentFrames_Type())
frCircuitSentFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitSentFrames.setStatus(_A)
_FrCircuitSentOctets_Type=Counter32
_FrCircuitSentOctets_Object=MibTableColumn
frCircuitSentOctets=_FrCircuitSentOctets_Object((1,3,6,1,2,1,10,32,2,1,7),_FrCircuitSentOctets_Type())
frCircuitSentOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitSentOctets.setStatus(_A)
_FrCircuitReceivedFrames_Type=Counter32
_FrCircuitReceivedFrames_Object=MibTableColumn
frCircuitReceivedFrames=_FrCircuitReceivedFrames_Object((1,3,6,1,2,1,10,32,2,1,8),_FrCircuitReceivedFrames_Type())
frCircuitReceivedFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitReceivedFrames.setStatus(_A)
_FrCircuitReceivedOctets_Type=Counter32
_FrCircuitReceivedOctets_Object=MibTableColumn
frCircuitReceivedOctets=_FrCircuitReceivedOctets_Object((1,3,6,1,2,1,10,32,2,1,9),_FrCircuitReceivedOctets_Type())
frCircuitReceivedOctets.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitReceivedOctets.setStatus(_A)
_FrCircuitCreationTime_Type=TimeTicks
_FrCircuitCreationTime_Object=MibTableColumn
frCircuitCreationTime=_FrCircuitCreationTime_Object((1,3,6,1,2,1,10,32,2,1,10),_FrCircuitCreationTime_Type())
frCircuitCreationTime.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitCreationTime.setStatus(_A)
_FrCircuitLastTimeChange_Type=TimeTicks
_FrCircuitLastTimeChange_Object=MibTableColumn
frCircuitLastTimeChange=_FrCircuitLastTimeChange_Object((1,3,6,1,2,1,10,32,2,1,11),_FrCircuitLastTimeChange_Type())
frCircuitLastTimeChange.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitLastTimeChange.setStatus(_A)
class _FrCircuitCommittedBurst_Type(Integer32):defaultValue=0
_FrCircuitCommittedBurst_Type.__name__=_B
_FrCircuitCommittedBurst_Object=MibTableColumn
frCircuitCommittedBurst=_FrCircuitCommittedBurst_Object((1,3,6,1,2,1,10,32,2,1,12),_FrCircuitCommittedBurst_Type())
frCircuitCommittedBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitCommittedBurst.setStatus(_A)
_FrCircuitExcessBurst_Type=Integer32
_FrCircuitExcessBurst_Object=MibTableColumn
frCircuitExcessBurst=_FrCircuitExcessBurst_Object((1,3,6,1,2,1,10,32,2,1,13),_FrCircuitExcessBurst_Type())
frCircuitExcessBurst.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitExcessBurst.setStatus(_A)
class _FrCircuitThroughput_Type(Integer32):defaultValue=0
_FrCircuitThroughput_Type.__name__=_B
_FrCircuitThroughput_Object=MibTableColumn
frCircuitThroughput=_FrCircuitThroughput_Object((1,3,6,1,2,1,10,32,2,1,14),_FrCircuitThroughput_Type())
frCircuitThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitThroughput.setStatus(_A)
class _FrCircuitRouteType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('switch',2)))
_FrCircuitRouteType_Type.__name__=_B
_FrCircuitRouteType_Object=MibTableColumn
frCircuitRouteType=_FrCircuitRouteType_Object((1,3,6,1,2,1,10,32,2,1,42),_FrCircuitRouteType_Type())
frCircuitRouteType.setMaxAccess(_D)
if mibBuilder.loadTexts:frCircuitRouteType.setStatus(_A)
class _FrCircuitRouteIfIndex_Type(Integer32):defaultValue=0
_FrCircuitRouteIfIndex_Type.__name__=_B
_FrCircuitRouteIfIndex_Object=MibTableColumn
frCircuitRouteIfIndex=_FrCircuitRouteIfIndex_Object((1,3,6,1,2,1,10,32,2,1,43),_FrCircuitRouteIfIndex_Type())
frCircuitRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitRouteIfIndex.setStatus(_A)
class _FrCircuitRouteDlci_Type(Integer32):defaultValue=0
_FrCircuitRouteDlci_Type.__name__=_B
_FrCircuitRouteDlci_Object=MibTableColumn
frCircuitRouteDlci=_FrCircuitRouteDlci_Object((1,3,6,1,2,1,10,32,2,1,44),_FrCircuitRouteDlci_Type())
frCircuitRouteDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:frCircuitRouteDlci.setStatus(_A)
_FrErrTable_Object=MibTable
frErrTable=_FrErrTable_Object((1,3,6,1,2,1,10,32,3))
if mibBuilder.loadTexts:frErrTable.setStatus(_A)
_FrErrEntry_Object=MibTableRow
frErrEntry=_FrErrEntry_Object((1,3,6,1,2,1,10,32,3,1))
frErrEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:frErrEntry.setStatus(_A)
_FrErrIfIndex_Type=Integer32
_FrErrIfIndex_Object=MibTableColumn
frErrIfIndex=_FrErrIfIndex_Object((1,3,6,1,2,1,10,32,3,1,1),_FrErrIfIndex_Type())
frErrIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:frErrIfIndex.setStatus(_A)
class _FrErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('unknownError',1),('receiveShort',2),('receiveLong',3),('illegalDLCI',4),('unknownDLCI',5),('dlcmiProtoErr',6),('dlcmiUnknownIE',7),('dlcmiSequenceErr',8),('dlcmiUnknownRpt',9),('noErrorSinceReset',10)))
_FrErrType_Type.__name__=_B
_FrErrType_Object=MibTableColumn
frErrType=_FrErrType_Object((1,3,6,1,2,1,10,32,3,1,2),_FrErrType_Type())
frErrType.setMaxAccess(_D)
if mibBuilder.loadTexts:frErrType.setStatus(_A)
_FrErrData_Type=OctetString
_FrErrData_Object=MibTableColumn
frErrData=_FrErrData_Object((1,3,6,1,2,1,10,32,3,1,3),_FrErrData_Type())
frErrData.setMaxAccess(_D)
if mibBuilder.loadTexts:frErrData.setStatus(_A)
_FrErrTime_Type=TimeTicks
_FrErrTime_Object=MibTableColumn
frErrTime=_FrErrTime_Object((1,3,6,1,2,1,10,32,3,1,4),_FrErrTime_Type())
frErrTime.setMaxAccess(_D)
if mibBuilder.loadTexts:frErrTime.setStatus(_A)
_FrGlobals_ObjectIdentity=ObjectIdentity
frGlobals=_FrGlobals_ObjectIdentity((1,3,6,1,2,1,10,32,4))
class _FrTrapState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FrTrapState_Type.__name__=_B
_FrTrapState_Object=MibScalar
frTrapState=_FrTrapState_Object((1,3,6,1,2,1,10,32,4,1),_FrTrapState_Type())
frTrapState.setMaxAccess(_C)
if mibBuilder.loadTexts:frTrapState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'frpublic':frpublic,'frDlcmiTable':frDlcmiTable,'frDlcmiEntry':frDlcmiEntry,_G:frDlcmiIfIndex,'frDlcmiState':frDlcmiState,'frDlcmiAddress':frDlcmiAddress,'frDlcmiAddressLen':frDlcmiAddressLen,'frDlcmiPollingInterval':frDlcmiPollingInterval,'frDlcmiFullEnquiryInterval':frDlcmiFullEnquiryInterval,'frDlcmiErrorThreshold':frDlcmiErrorThreshold,'frDlcmiMonitoredEvents':frDlcmiMonitoredEvents,'frDlcmiMaxSupportedVCs':frDlcmiMaxSupportedVCs,'frDlcmiMulticast':frDlcmiMulticast,'frDlcmiDceIdleInterval':frDlcmiDceIdleInterval,'frDlcmiDceErrorThreshold':frDlcmiDceErrorThreshold,'frDlcmiDceMonitoredEvents':frDlcmiDceMonitoredEvents,'frDlcmiMode':frDlcmiMode,'frDlcmiDefaultRouteIfIndex':frDlcmiDefaultRouteIfIndex,'frCircuitTable':frCircuitTable,'frCircuitEntry':frCircuitEntry,_H:frCircuitIfIndex,_I:frCircuitDlci,'frCircuitState':frCircuitState,'frCircuitReceivedFECNs':frCircuitReceivedFECNs,'frCircuitReceivedBECNs':frCircuitReceivedBECNs,'frCircuitSentFrames':frCircuitSentFrames,'frCircuitSentOctets':frCircuitSentOctets,'frCircuitReceivedFrames':frCircuitReceivedFrames,'frCircuitReceivedOctets':frCircuitReceivedOctets,'frCircuitCreationTime':frCircuitCreationTime,'frCircuitLastTimeChange':frCircuitLastTimeChange,'frCircuitCommittedBurst':frCircuitCommittedBurst,'frCircuitExcessBurst':frCircuitExcessBurst,'frCircuitThroughput':frCircuitThroughput,'frCircuitRouteType':frCircuitRouteType,'frCircuitRouteIfIndex':frCircuitRouteIfIndex,'frCircuitRouteDlci':frCircuitRouteDlci,'frErrTable':frErrTable,'frErrEntry':frErrEntry,_J:frErrIfIndex,'frErrType':frErrType,'frErrData':frErrData,'frErrTime':frErrTime,'frGlobals':frGlobals,'frTrapState':frTrapState})