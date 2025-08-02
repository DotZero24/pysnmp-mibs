_Q='unimplemented'
_P='snmpFddiATTACHMENTIndex'
_O='snmpFddiATTACHMENTSMTIndex'
_N='snmpFddiPORTIndex'
_M='snmpFddiPORTSMTIndex'
_L='snmpFddiMACIndex'
_K='snmpFddiMACSMTIndex'
_J='snmpFddiSMTIndex'
_I='unknown'
_H='other'
_G='RFC1285-MIB'
_F='false'
_E='true'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class FddiTime(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class FddiResourceId(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class FddiSMTStationIdType(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class FddiMACLongAddressType(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_Fddi_ObjectIdentity=ObjectIdentity
fddi=_Fddi_ObjectIdentity((1,3,6,1,2,1,10,15))
_SnmpFddiSMT_ObjectIdentity=ObjectIdentity
snmpFddiSMT=_SnmpFddiSMT_ObjectIdentity((1,3,6,1,2,1,10,15,1))
class _SnmpFddiSMTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpFddiSMTNumber_Type.__name__=_C
_SnmpFddiSMTNumber_Object=MibScalar
snmpFddiSMTNumber=_SnmpFddiSMTNumber_Object((1,3,6,1,2,1,10,15,1,1),_SnmpFddiSMTNumber_Type())
snmpFddiSMTNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTNumber.setStatus(_A)
_SnmpFddiSMTTable_Object=MibTable
snmpFddiSMTTable=_SnmpFddiSMTTable_Object((1,3,6,1,2,1,10,15,1,2))
if mibBuilder.loadTexts:snmpFddiSMTTable.setStatus(_A)
_SnmpFddiSMTEntry_Object=MibTableRow
snmpFddiSMTEntry=_SnmpFddiSMTEntry_Object((1,3,6,1,2,1,10,15,1,2,1))
snmpFddiSMTEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:snmpFddiSMTEntry.setStatus(_A)
class _SnmpFddiSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiSMTIndex_Type.__name__=_C
_SnmpFddiSMTIndex_Object=MibTableColumn
snmpFddiSMTIndex=_SnmpFddiSMTIndex_Object((1,3,6,1,2,1,10,15,1,2,1,1),_SnmpFddiSMTIndex_Type())
snmpFddiSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTIndex.setStatus(_A)
_SnmpFddiSMTStationId_Type=FddiSMTStationIdType
_SnmpFddiSMTStationId_Object=MibTableColumn
snmpFddiSMTStationId=_SnmpFddiSMTStationId_Object((1,3,6,1,2,1,10,15,1,2,1,2),_SnmpFddiSMTStationId_Type())
snmpFddiSMTStationId.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTStationId.setStatus(_A)
class _SnmpFddiSMTOpVersionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiSMTOpVersionId_Type.__name__=_C
_SnmpFddiSMTOpVersionId_Object=MibTableColumn
snmpFddiSMTOpVersionId=_SnmpFddiSMTOpVersionId_Object((1,3,6,1,2,1,10,15,1,2,1,3),_SnmpFddiSMTOpVersionId_Type())
snmpFddiSMTOpVersionId.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiSMTOpVersionId.setStatus(_A)
class _SnmpFddiSMTHiVersionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiSMTHiVersionId_Type.__name__=_C
_SnmpFddiSMTHiVersionId_Object=MibTableColumn
snmpFddiSMTHiVersionId=_SnmpFddiSMTHiVersionId_Object((1,3,6,1,2,1,10,15,1,2,1,4),_SnmpFddiSMTHiVersionId_Type())
snmpFddiSMTHiVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTHiVersionId.setStatus(_A)
class _SnmpFddiSMTLoVersionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiSMTLoVersionId_Type.__name__=_C
_SnmpFddiSMTLoVersionId_Object=MibTableColumn
snmpFddiSMTLoVersionId=_SnmpFddiSMTLoVersionId_Object((1,3,6,1,2,1,10,15,1,2,1,5),_SnmpFddiSMTLoVersionId_Type())
snmpFddiSMTLoVersionId.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTLoVersionId.setStatus(_A)
class _SnmpFddiSMTMACCt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnmpFddiSMTMACCt_Type.__name__=_C
_SnmpFddiSMTMACCt_Object=MibTableColumn
snmpFddiSMTMACCt=_SnmpFddiSMTMACCt_Object((1,3,6,1,2,1,10,15,1,2,1,6),_SnmpFddiSMTMACCt_Type())
snmpFddiSMTMACCt.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTMACCt.setStatus(_A)
class _SnmpFddiSMTNonMasterCt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_SnmpFddiSMTNonMasterCt_Type.__name__=_C
_SnmpFddiSMTNonMasterCt_Object=MibTableColumn
snmpFddiSMTNonMasterCt=_SnmpFddiSMTNonMasterCt_Object((1,3,6,1,2,1,10,15,1,2,1,7),_SnmpFddiSMTNonMasterCt_Type())
snmpFddiSMTNonMasterCt.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTNonMasterCt.setStatus(_A)
class _SnmpFddiSMTMasterCt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_SnmpFddiSMTMasterCt_Type.__name__=_C
_SnmpFddiSMTMasterCt_Object=MibTableColumn
snmpFddiSMTMasterCt=_SnmpFddiSMTMasterCt_Object((1,3,6,1,2,1,10,15,1,2,1,8),_SnmpFddiSMTMasterCt_Type())
snmpFddiSMTMasterCt.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTMasterCt.setStatus(_A)
class _SnmpFddiSMTPathsAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnmpFddiSMTPathsAvailable_Type.__name__=_C
_SnmpFddiSMTPathsAvailable_Object=MibTableColumn
snmpFddiSMTPathsAvailable=_SnmpFddiSMTPathsAvailable_Object((1,3,6,1,2,1,10,15,1,2,1,9),_SnmpFddiSMTPathsAvailable_Type())
snmpFddiSMTPathsAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTPathsAvailable.setStatus(_A)
class _SnmpFddiSMTConfigCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SnmpFddiSMTConfigCapabilities_Type.__name__=_C
_SnmpFddiSMTConfigCapabilities_Object=MibTableColumn
snmpFddiSMTConfigCapabilities=_SnmpFddiSMTConfigCapabilities_Object((1,3,6,1,2,1,10,15,1,2,1,10),_SnmpFddiSMTConfigCapabilities_Type())
snmpFddiSMTConfigCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTConfigCapabilities.setStatus(_A)
class _SnmpFddiSMTConfigPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_SnmpFddiSMTConfigPolicy_Type.__name__=_C
_SnmpFddiSMTConfigPolicy_Object=MibTableColumn
snmpFddiSMTConfigPolicy=_SnmpFddiSMTConfigPolicy_Object((1,3,6,1,2,1,10,15,1,2,1,11),_SnmpFddiSMTConfigPolicy_Type())
snmpFddiSMTConfigPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiSMTConfigPolicy.setStatus(_A)
class _SnmpFddiSMTConnectionPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpFddiSMTConnectionPolicy_Type.__name__=_C
_SnmpFddiSMTConnectionPolicy_Object=MibTableColumn
snmpFddiSMTConnectionPolicy=_SnmpFddiSMTConnectionPolicy_Object((1,3,6,1,2,1,10,15,1,2,1,12),_SnmpFddiSMTConnectionPolicy_Type())
snmpFddiSMTConnectionPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiSMTConnectionPolicy.setStatus(_A)
class _SnmpFddiSMTTNotify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_SnmpFddiSMTTNotify_Type.__name__=_C
_SnmpFddiSMTTNotify_Object=MibTableColumn
snmpFddiSMTTNotify=_SnmpFddiSMTTNotify_Object((1,3,6,1,2,1,10,15,1,2,1,13),_SnmpFddiSMTTNotify_Type())
snmpFddiSMTTNotify.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiSMTTNotify.setStatus(_A)
class _SnmpFddiSMTStatusReporting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiSMTStatusReporting_Type.__name__=_C
_SnmpFddiSMTStatusReporting_Object=MibTableColumn
snmpFddiSMTStatusReporting=_SnmpFddiSMTStatusReporting_Object((1,3,6,1,2,1,10,15,1,2,1,14),_SnmpFddiSMTStatusReporting_Type())
snmpFddiSMTStatusReporting.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTStatusReporting.setStatus(_A)
class _SnmpFddiSMTECMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('ec0',1),('ec1',2),('ec2',3),('ec3',4),('ec4',5),('ec5',6),('ec6',7),('ec7',8)))
_SnmpFddiSMTECMState_Type.__name__=_C
_SnmpFddiSMTECMState_Object=MibTableColumn
snmpFddiSMTECMState=_SnmpFddiSMTECMState_Object((1,3,6,1,2,1,10,15,1,2,1,15),_SnmpFddiSMTECMState_Type())
snmpFddiSMTECMState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTECMState.setStatus(_A)
class _SnmpFddiSMTCFState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cf0',1),('cf1',2),('cf2',3),('cf3',4),('cf4',5),('cf5',6)))
_SnmpFddiSMTCFState_Type.__name__=_C
_SnmpFddiSMTCFState_Object=MibTableColumn
snmpFddiSMTCFState=_SnmpFddiSMTCFState_Object((1,3,6,1,2,1,10,15,1,2,1,16),_SnmpFddiSMTCFState_Type())
snmpFddiSMTCFState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTCFState.setStatus(_A)
class _SnmpFddiSMTHoldState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-implemented',1),('not-holding',2),('holding-prm',3),('holding-sec',4)))
_SnmpFddiSMTHoldState_Type.__name__=_C
_SnmpFddiSMTHoldState_Object=MibTableColumn
snmpFddiSMTHoldState=_SnmpFddiSMTHoldState_Object((1,3,6,1,2,1,10,15,1,2,1,17),_SnmpFddiSMTHoldState_Type())
snmpFddiSMTHoldState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTHoldState.setStatus(_A)
class _SnmpFddiSMTRemoteDisconnectFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiSMTRemoteDisconnectFlag_Type.__name__=_C
_SnmpFddiSMTRemoteDisconnectFlag_Object=MibTableColumn
snmpFddiSMTRemoteDisconnectFlag=_SnmpFddiSMTRemoteDisconnectFlag_Object((1,3,6,1,2,1,10,15,1,2,1,18),_SnmpFddiSMTRemoteDisconnectFlag_Type())
snmpFddiSMTRemoteDisconnectFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiSMTRemoteDisconnectFlag.setStatus(_A)
class _SnmpFddiSMTStationAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('connect',2),('disconnect',3),('path-Test',4),('self-Test',5)))
_SnmpFddiSMTStationAction_Type.__name__=_C
_SnmpFddiSMTStationAction_Object=MibTableColumn
snmpFddiSMTStationAction=_SnmpFddiSMTStationAction_Object((1,3,6,1,2,1,10,15,1,2,1,19),_SnmpFddiSMTStationAction_Type())
snmpFddiSMTStationAction.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiSMTStationAction.setStatus(_A)
_SnmpFddiMAC_ObjectIdentity=ObjectIdentity
snmpFddiMAC=_SnmpFddiMAC_ObjectIdentity((1,3,6,1,2,1,10,15,2))
class _SnmpFddiMACNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpFddiMACNumber_Type.__name__=_C
_SnmpFddiMACNumber_Object=MibScalar
snmpFddiMACNumber=_SnmpFddiMACNumber_Object((1,3,6,1,2,1,10,15,2,1),_SnmpFddiMACNumber_Type())
snmpFddiMACNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACNumber.setStatus(_A)
_SnmpFddiMACTable_Object=MibTable
snmpFddiMACTable=_SnmpFddiMACTable_Object((1,3,6,1,2,1,10,15,2,2))
if mibBuilder.loadTexts:snmpFddiMACTable.setStatus(_A)
_SnmpFddiMACEntry_Object=MibTableRow
snmpFddiMACEntry=_SnmpFddiMACEntry_Object((1,3,6,1,2,1,10,15,2,2,1))
snmpFddiMACEntry.setIndexNames((0,_G,_K),(0,_G,_L))
if mibBuilder.loadTexts:snmpFddiMACEntry.setStatus(_A)
class _SnmpFddiMACSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiMACSMTIndex_Type.__name__=_C
_SnmpFddiMACSMTIndex_Object=MibTableColumn
snmpFddiMACSMTIndex=_SnmpFddiMACSMTIndex_Object((1,3,6,1,2,1,10,15,2,2,1,1),_SnmpFddiMACSMTIndex_Type())
snmpFddiMACSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACSMTIndex.setStatus(_A)
class _SnmpFddiMACIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiMACIndex_Type.__name__=_C
_SnmpFddiMACIndex_Object=MibTableColumn
snmpFddiMACIndex=_SnmpFddiMACIndex_Object((1,3,6,1,2,1,10,15,2,2,1,2),_SnmpFddiMACIndex_Type())
snmpFddiMACIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACIndex.setStatus(_A)
class _SnmpFddiMACFrameStatusCapabilities_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1799))
_SnmpFddiMACFrameStatusCapabilities_Type.__name__=_C
_SnmpFddiMACFrameStatusCapabilities_Object=MibTableColumn
snmpFddiMACFrameStatusCapabilities=_SnmpFddiMACFrameStatusCapabilities_Object((1,3,6,1,2,1,10,15,2,2,1,3),_SnmpFddiMACFrameStatusCapabilities_Type())
snmpFddiMACFrameStatusCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACFrameStatusCapabilities.setStatus(_A)
_SnmpFddiMACTMaxGreatestLowerBound_Type=FddiTime
_SnmpFddiMACTMaxGreatestLowerBound_Object=MibTableColumn
snmpFddiMACTMaxGreatestLowerBound=_SnmpFddiMACTMaxGreatestLowerBound_Object((1,3,6,1,2,1,10,15,2,2,1,4),_SnmpFddiMACTMaxGreatestLowerBound_Type())
snmpFddiMACTMaxGreatestLowerBound.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiMACTMaxGreatestLowerBound.setStatus(_A)
_SnmpFddiMACTVXGreatestLowerBound_Type=FddiTime
_SnmpFddiMACTVXGreatestLowerBound_Object=MibTableColumn
snmpFddiMACTVXGreatestLowerBound=_SnmpFddiMACTVXGreatestLowerBound_Object((1,3,6,1,2,1,10,15,2,2,1,5),_SnmpFddiMACTVXGreatestLowerBound_Type())
snmpFddiMACTVXGreatestLowerBound.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACTVXGreatestLowerBound.setStatus(_A)
class _SnmpFddiMACPathsAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnmpFddiMACPathsAvailable_Type.__name__=_C
_SnmpFddiMACPathsAvailable_Object=MibTableColumn
snmpFddiMACPathsAvailable=_SnmpFddiMACPathsAvailable_Object((1,3,6,1,2,1,10,15,2,2,1,6),_SnmpFddiMACPathsAvailable_Type())
snmpFddiMACPathsAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACPathsAvailable.setStatus(_A)
class _SnmpFddiMACCurrentPath_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16)));namedValues=NamedValues(*((_I,1),('primary',2),('secondary',4),('local',8),('isolated',16)))
_SnmpFddiMACCurrentPath_Type.__name__=_C
_SnmpFddiMACCurrentPath_Object=MibTableColumn
snmpFddiMACCurrentPath=_SnmpFddiMACCurrentPath_Object((1,3,6,1,2,1,10,15,2,2,1,7),_SnmpFddiMACCurrentPath_Type())
snmpFddiMACCurrentPath.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACCurrentPath.setStatus(_A)
_SnmpFddiMACUpstreamNbr_Type=FddiMACLongAddressType
_SnmpFddiMACUpstreamNbr_Object=MibTableColumn
snmpFddiMACUpstreamNbr=_SnmpFddiMACUpstreamNbr_Object((1,3,6,1,2,1,10,15,2,2,1,8),_SnmpFddiMACUpstreamNbr_Type())
snmpFddiMACUpstreamNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACUpstreamNbr.setStatus(_A)
_SnmpFddiMACOldUpstreamNbr_Type=FddiMACLongAddressType
_SnmpFddiMACOldUpstreamNbr_Object=MibTableColumn
snmpFddiMACOldUpstreamNbr=_SnmpFddiMACOldUpstreamNbr_Object((1,3,6,1,2,1,10,15,2,2,1,9),_SnmpFddiMACOldUpstreamNbr_Type())
snmpFddiMACOldUpstreamNbr.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACOldUpstreamNbr.setStatus(_A)
class _SnmpFddiMACDupAddrTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('pass',2),('fail',3)))
_SnmpFddiMACDupAddrTest_Type.__name__=_C
_SnmpFddiMACDupAddrTest_Object=MibTableColumn
snmpFddiMACDupAddrTest=_SnmpFddiMACDupAddrTest_Object((1,3,6,1,2,1,10,15,2,2,1,10),_SnmpFddiMACDupAddrTest_Type())
snmpFddiMACDupAddrTest.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACDupAddrTest.setStatus(_A)
_SnmpFddiMACPathsRequested_Type=Integer32
_SnmpFddiMACPathsRequested_Object=MibTableColumn
snmpFddiMACPathsRequested=_SnmpFddiMACPathsRequested_Object((1,3,6,1,2,1,10,15,2,2,1,11),_SnmpFddiMACPathsRequested_Type())
snmpFddiMACPathsRequested.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiMACPathsRequested.setStatus(_A)
class _SnmpFddiMACDownstreamPORTType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('a',1),('b',2),('s',3),('m',4),(_I,5)))
_SnmpFddiMACDownstreamPORTType_Type.__name__=_C
_SnmpFddiMACDownstreamPORTType_Object=MibTableColumn
snmpFddiMACDownstreamPORTType=_SnmpFddiMACDownstreamPORTType_Object((1,3,6,1,2,1,10,15,2,2,1,12),_SnmpFddiMACDownstreamPORTType_Type())
snmpFddiMACDownstreamPORTType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACDownstreamPORTType.setStatus(_A)
_SnmpFddiMACSMTAddress_Type=FddiMACLongAddressType
_SnmpFddiMACSMTAddress_Object=MibTableColumn
snmpFddiMACSMTAddress=_SnmpFddiMACSMTAddress_Object((1,3,6,1,2,1,10,15,2,2,1,13),_SnmpFddiMACSMTAddress_Type())
snmpFddiMACSMTAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACSMTAddress.setStatus(_A)
_SnmpFddiMACTReq_Type=FddiTime
_SnmpFddiMACTReq_Object=MibTableColumn
snmpFddiMACTReq=_SnmpFddiMACTReq_Object((1,3,6,1,2,1,10,15,2,2,1,14),_SnmpFddiMACTReq_Type())
snmpFddiMACTReq.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiMACTReq.setStatus(_A)
_SnmpFddiMACTNeg_Type=FddiTime
_SnmpFddiMACTNeg_Object=MibTableColumn
snmpFddiMACTNeg=_SnmpFddiMACTNeg_Object((1,3,6,1,2,1,10,15,2,2,1,15),_SnmpFddiMACTNeg_Type())
snmpFddiMACTNeg.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACTNeg.setStatus(_A)
_SnmpFddiMACTMax_Type=FddiTime
_SnmpFddiMACTMax_Object=MibTableColumn
snmpFddiMACTMax=_SnmpFddiMACTMax_Object((1,3,6,1,2,1,10,15,2,2,1,16),_SnmpFddiMACTMax_Type())
snmpFddiMACTMax.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACTMax.setStatus(_A)
_SnmpFddiMACTvxValue_Type=FddiTime
_SnmpFddiMACTvxValue_Object=MibTableColumn
snmpFddiMACTvxValue=_SnmpFddiMACTvxValue_Object((1,3,6,1,2,1,10,15,2,2,1,17),_SnmpFddiMACTvxValue_Type())
snmpFddiMACTvxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACTvxValue.setStatus(_A)
_SnmpFddiMACTMin_Type=FddiTime
_SnmpFddiMACTMin_Object=MibTableColumn
snmpFddiMACTMin=_SnmpFddiMACTMin_Object((1,3,6,1,2,1,10,15,2,2,1,18),_SnmpFddiMACTMin_Type())
snmpFddiMACTMin.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACTMin.setStatus(_A)
class _SnmpFddiMACCurrentFrameStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnmpFddiMACCurrentFrameStatus_Type.__name__=_C
_SnmpFddiMACCurrentFrameStatus_Object=MibTableColumn
snmpFddiMACCurrentFrameStatus=_SnmpFddiMACCurrentFrameStatus_Object((1,3,6,1,2,1,10,15,2,2,1,19),_SnmpFddiMACCurrentFrameStatus_Type())
snmpFddiMACCurrentFrameStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiMACCurrentFrameStatus.setStatus(_A)
_SnmpFddiMACFrameCts_Type=Counter32
_SnmpFddiMACFrameCts_Object=MibTableColumn
snmpFddiMACFrameCts=_SnmpFddiMACFrameCts_Object((1,3,6,1,2,1,10,15,2,2,1,20),_SnmpFddiMACFrameCts_Type())
snmpFddiMACFrameCts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACFrameCts.setStatus(_A)
_SnmpFddiMACErrorCts_Type=Counter32
_SnmpFddiMACErrorCts_Object=MibTableColumn
snmpFddiMACErrorCts=_SnmpFddiMACErrorCts_Object((1,3,6,1,2,1,10,15,2,2,1,21),_SnmpFddiMACErrorCts_Type())
snmpFddiMACErrorCts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACErrorCts.setStatus(_A)
_SnmpFddiMACLostCts_Type=Counter32
_SnmpFddiMACLostCts_Object=MibTableColumn
snmpFddiMACLostCts=_SnmpFddiMACLostCts_Object((1,3,6,1,2,1,10,15,2,2,1,22),_SnmpFddiMACLostCts_Type())
snmpFddiMACLostCts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACLostCts.setStatus(_A)
class _SnmpFddiMACFrameErrorThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiMACFrameErrorThreshold_Type.__name__=_C
_SnmpFddiMACFrameErrorThreshold_Object=MibTableColumn
snmpFddiMACFrameErrorThreshold=_SnmpFddiMACFrameErrorThreshold_Object((1,3,6,1,2,1,10,15,2,2,1,23),_SnmpFddiMACFrameErrorThreshold_Type())
snmpFddiMACFrameErrorThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACFrameErrorThreshold.setStatus(_A)
class _SnmpFddiMACFrameErrorRatio_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiMACFrameErrorRatio_Type.__name__=_C
_SnmpFddiMACFrameErrorRatio_Object=MibTableColumn
snmpFddiMACFrameErrorRatio=_SnmpFddiMACFrameErrorRatio_Object((1,3,6,1,2,1,10,15,2,2,1,24),_SnmpFddiMACFrameErrorRatio_Type())
snmpFddiMACFrameErrorRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACFrameErrorRatio.setStatus(_A)
class _SnmpFddiMACRMTState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('rm0',1),('rm1',2),('rm2',3),('rm3',4),('rm4',5),('rm5',6),('rm6',7),('rm7',8)))
_SnmpFddiMACRMTState_Type.__name__=_C
_SnmpFddiMACRMTState_Object=MibTableColumn
snmpFddiMACRMTState=_SnmpFddiMACRMTState_Object((1,3,6,1,2,1,10,15,2,2,1,25),_SnmpFddiMACRMTState_Type())
snmpFddiMACRMTState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACRMTState.setStatus(_A)
class _SnmpFddiMACDaFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiMACDaFlag_Type.__name__=_C
_SnmpFddiMACDaFlag_Object=MibTableColumn
snmpFddiMACDaFlag=_SnmpFddiMACDaFlag_Object((1,3,6,1,2,1,10,15,2,2,1,26),_SnmpFddiMACDaFlag_Type())
snmpFddiMACDaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACDaFlag.setStatus(_A)
class _SnmpFddiMACUnaDaFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiMACUnaDaFlag_Type.__name__=_C
_SnmpFddiMACUnaDaFlag_Object=MibTableColumn
snmpFddiMACUnaDaFlag=_SnmpFddiMACUnaDaFlag_Object((1,3,6,1,2,1,10,15,2,2,1,27),_SnmpFddiMACUnaDaFlag_Type())
snmpFddiMACUnaDaFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACUnaDaFlag.setStatus(_A)
class _SnmpFddiMACFrameCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiMACFrameCondition_Type.__name__=_C
_SnmpFddiMACFrameCondition_Object=MibTableColumn
snmpFddiMACFrameCondition=_SnmpFddiMACFrameCondition_Object((1,3,6,1,2,1,10,15,2,2,1,28),_SnmpFddiMACFrameCondition_Type())
snmpFddiMACFrameCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACFrameCondition.setStatus(_A)
_SnmpFddiMACChipSet_Type=ObjectIdentifier
_SnmpFddiMACChipSet_Object=MibTableColumn
snmpFddiMACChipSet=_SnmpFddiMACChipSet_Object((1,3,6,1,2,1,10,15,2,2,1,29),_SnmpFddiMACChipSet_Type())
snmpFddiMACChipSet.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiMACChipSet.setStatus(_A)
class _SnmpFddiMACAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),('enableLLCService',2),('disableLLCService',3),('connectMAC',4),('disconnectMAC',5)))
_SnmpFddiMACAction_Type.__name__=_C
_SnmpFddiMACAction_Object=MibTableColumn
snmpFddiMACAction=_SnmpFddiMACAction_Object((1,3,6,1,2,1,10,15,2,2,1,30),_SnmpFddiMACAction_Type())
snmpFddiMACAction.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiMACAction.setStatus(_A)
_SnmpFddiPATH_ObjectIdentity=ObjectIdentity
snmpFddiPATH=_SnmpFddiPATH_ObjectIdentity((1,3,6,1,2,1,10,15,3))
_SnmpFddiPORT_ObjectIdentity=ObjectIdentity
snmpFddiPORT=_SnmpFddiPORT_ObjectIdentity((1,3,6,1,2,1,10,15,4))
class _SnmpFddiPORTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpFddiPORTNumber_Type.__name__=_C
_SnmpFddiPORTNumber_Object=MibScalar
snmpFddiPORTNumber=_SnmpFddiPORTNumber_Object((1,3,6,1,2,1,10,15,4,1),_SnmpFddiPORTNumber_Type())
snmpFddiPORTNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTNumber.setStatus(_A)
_SnmpFddiPORTTable_Object=MibTable
snmpFddiPORTTable=_SnmpFddiPORTTable_Object((1,3,6,1,2,1,10,15,4,2))
if mibBuilder.loadTexts:snmpFddiPORTTable.setStatus(_A)
_SnmpFddiPORTEntry_Object=MibTableRow
snmpFddiPORTEntry=_SnmpFddiPORTEntry_Object((1,3,6,1,2,1,10,15,4,2,1))
snmpFddiPORTEntry.setIndexNames((0,_G,_M),(0,_G,_N))
if mibBuilder.loadTexts:snmpFddiPORTEntry.setStatus(_A)
class _SnmpFddiPORTSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiPORTSMTIndex_Type.__name__=_C
_SnmpFddiPORTSMTIndex_Object=MibTableColumn
snmpFddiPORTSMTIndex=_SnmpFddiPORTSMTIndex_Object((1,3,6,1,2,1,10,15,4,2,1,1),_SnmpFddiPORTSMTIndex_Type())
snmpFddiPORTSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTSMTIndex.setStatus(_A)
class _SnmpFddiPORTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiPORTIndex_Type.__name__=_C
_SnmpFddiPORTIndex_Object=MibTableColumn
snmpFddiPORTIndex=_SnmpFddiPORTIndex_Object((1,3,6,1,2,1,10,15,4,2,1,2),_SnmpFddiPORTIndex_Type())
snmpFddiPORTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTIndex.setStatus(_A)
class _SnmpFddiPORTPCType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('a',1),('b',2),('s',3),('m',4)))
_SnmpFddiPORTPCType_Type.__name__=_C
_SnmpFddiPORTPCType_Object=MibTableColumn
snmpFddiPORTPCType=_SnmpFddiPORTPCType_Object((1,3,6,1,2,1,10,15,4,2,1,3),_SnmpFddiPORTPCType_Type())
snmpFddiPORTPCType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTPCType.setStatus(_A)
class _SnmpFddiPORTPCNeighbor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('a',1),('b',2),('s',3),('m',4),(_I,5)))
_SnmpFddiPORTPCNeighbor_Type.__name__=_C
_SnmpFddiPORTPCNeighbor_Object=MibTableColumn
snmpFddiPORTPCNeighbor=_SnmpFddiPORTPCNeighbor_Object((1,3,6,1,2,1,10,15,4,2,1,4),_SnmpFddiPORTPCNeighbor_Type())
snmpFddiPORTPCNeighbor.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTPCNeighbor.setStatus(_A)
class _SnmpFddiPORTConnectionPolicies_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnmpFddiPORTConnectionPolicies_Type.__name__=_C
_SnmpFddiPORTConnectionPolicies_Object=MibTableColumn
snmpFddiPORTConnectionPolicies=_SnmpFddiPORTConnectionPolicies_Object((1,3,6,1,2,1,10,15,4,2,1,5),_SnmpFddiPORTConnectionPolicies_Type())
snmpFddiPORTConnectionPolicies.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiPORTConnectionPolicies.setStatus(_A)
class _SnmpFddiPORTRemoteMACIndicated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiPORTRemoteMACIndicated_Type.__name__=_C
_SnmpFddiPORTRemoteMACIndicated_Object=MibTableColumn
snmpFddiPORTRemoteMACIndicated=_SnmpFddiPORTRemoteMACIndicated_Object((1,3,6,1,2,1,10,15,4,2,1,6),_SnmpFddiPORTRemoteMACIndicated_Type())
snmpFddiPORTRemoteMACIndicated.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTRemoteMACIndicated.setStatus(_A)
class _SnmpFddiPORTCEState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ce0',1),('ce1',2),('ce2',3),('ce3',4),('ce4',5)))
_SnmpFddiPORTCEState_Type.__name__=_C
_SnmpFddiPORTCEState_Object=MibTableColumn
snmpFddiPORTCEState=_SnmpFddiPORTCEState_Object((1,3,6,1,2,1,10,15,4,2,1,7),_SnmpFddiPORTCEState_Type())
snmpFddiPORTCEState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTCEState.setStatus(_A)
class _SnmpFddiPORTPathsRequested_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_SnmpFddiPORTPathsRequested_Type.__name__=_C
_SnmpFddiPORTPathsRequested_Object=MibTableColumn
snmpFddiPORTPathsRequested=_SnmpFddiPORTPathsRequested_Object((1,3,6,1,2,1,10,15,4,2,1,8),_SnmpFddiPORTPathsRequested_Type())
snmpFddiPORTPathsRequested.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiPORTPathsRequested.setStatus(_A)
_SnmpFddiPORTMACPlacement_Type=FddiResourceId
_SnmpFddiPORTMACPlacement_Object=MibTableColumn
snmpFddiPORTMACPlacement=_SnmpFddiPORTMACPlacement_Object((1,3,6,1,2,1,10,15,4,2,1,9),_SnmpFddiPORTMACPlacement_Type())
snmpFddiPORTMACPlacement.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTMACPlacement.setStatus(_A)
class _SnmpFddiPORTAvailablePaths_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SnmpFddiPORTAvailablePaths_Type.__name__=_C
_SnmpFddiPORTAvailablePaths_Object=MibTableColumn
snmpFddiPORTAvailablePaths=_SnmpFddiPORTAvailablePaths_Object((1,3,6,1,2,1,10,15,4,2,1,10),_SnmpFddiPORTAvailablePaths_Type())
snmpFddiPORTAvailablePaths.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTAvailablePaths.setStatus(_A)
_SnmpFddiPORTMACLoopTime_Type=FddiTime
_SnmpFddiPORTMACLoopTime_Object=MibTableColumn
snmpFddiPORTMACLoopTime=_SnmpFddiPORTMACLoopTime_Object((1,3,6,1,2,1,10,15,4,2,1,11),_SnmpFddiPORTMACLoopTime_Type())
snmpFddiPORTMACLoopTime.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiPORTMACLoopTime.setStatus(_A)
_SnmpFddiPORTTBMax_Type=FddiTime
_SnmpFddiPORTTBMax_Object=MibTableColumn
snmpFddiPORTTBMax=_SnmpFddiPORTTBMax_Object((1,3,6,1,2,1,10,15,4,2,1,12),_SnmpFddiPORTTBMax_Type())
snmpFddiPORTTBMax.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiPORTTBMax.setStatus(_A)
class _SnmpFddiPORTBSFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiPORTBSFlag_Type.__name__=_C
_SnmpFddiPORTBSFlag_Object=MibTableColumn
snmpFddiPORTBSFlag=_SnmpFddiPORTBSFlag_Object((1,3,6,1,2,1,10,15,4,2,1,13),_SnmpFddiPORTBSFlag_Type())
snmpFddiPORTBSFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTBSFlag.setStatus(_A)
_SnmpFddiPORTLCTFailCts_Type=Counter32
_SnmpFddiPORTLCTFailCts_Object=MibTableColumn
snmpFddiPORTLCTFailCts=_SnmpFddiPORTLCTFailCts_Object((1,3,6,1,2,1,10,15,4,2,1,14),_SnmpFddiPORTLCTFailCts_Type())
snmpFddiPORTLCTFailCts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTLCTFailCts.setStatus(_A)
class _SnmpFddiPORTLerEstimate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_SnmpFddiPORTLerEstimate_Type.__name__=_C
_SnmpFddiPORTLerEstimate_Object=MibTableColumn
snmpFddiPORTLerEstimate=_SnmpFddiPORTLerEstimate_Object((1,3,6,1,2,1,10,15,4,2,1,15),_SnmpFddiPORTLerEstimate_Type())
snmpFddiPORTLerEstimate.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTLerEstimate.setStatus(_A)
_SnmpFddiPORTLemRejectCts_Type=Counter32
_SnmpFddiPORTLemRejectCts_Object=MibTableColumn
snmpFddiPORTLemRejectCts=_SnmpFddiPORTLemRejectCts_Object((1,3,6,1,2,1,10,15,4,2,1,16),_SnmpFddiPORTLemRejectCts_Type())
snmpFddiPORTLemRejectCts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTLemRejectCts.setStatus(_A)
_SnmpFddiPORTLemCts_Type=Counter32
_SnmpFddiPORTLemCts_Object=MibTableColumn
snmpFddiPORTLemCts=_SnmpFddiPORTLemCts_Object((1,3,6,1,2,1,10,15,4,2,1,17),_SnmpFddiPORTLemCts_Type())
snmpFddiPORTLemCts.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTLemCts.setStatus(_A)
class _SnmpFddiPORTLerCutoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_SnmpFddiPORTLerCutoff_Type.__name__=_C
_SnmpFddiPORTLerCutoff_Object=MibTableColumn
snmpFddiPORTLerCutoff=_SnmpFddiPORTLerCutoff_Object((1,3,6,1,2,1,10,15,4,2,1,18),_SnmpFddiPORTLerCutoff_Type())
snmpFddiPORTLerCutoff.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiPORTLerCutoff.setStatus(_A)
class _SnmpFddiPORTLerAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,15))
_SnmpFddiPORTLerAlarm_Type.__name__=_C
_SnmpFddiPORTLerAlarm_Object=MibTableColumn
snmpFddiPORTLerAlarm=_SnmpFddiPORTLerAlarm_Object((1,3,6,1,2,1,10,15,4,2,1,19),_SnmpFddiPORTLerAlarm_Type())
snmpFddiPORTLerAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiPORTLerAlarm.setStatus(_A)
class _SnmpFddiPORTConnectState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('disabled',1),('connecting',2),('standby',3),('active',4)))
_SnmpFddiPORTConnectState_Type.__name__=_C
_SnmpFddiPORTConnectState_Object=MibTableColumn
snmpFddiPORTConnectState=_SnmpFddiPORTConnectState_Object((1,3,6,1,2,1,10,15,4,2,1,20),_SnmpFddiPORTConnectState_Type())
snmpFddiPORTConnectState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTConnectState.setStatus(_A)
class _SnmpFddiPORTPCMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('pc0',1),('pc1',2),('pc2',3),('pc3',4),('pc4',5),('pc5',6),('pc6',7),('pc7',8),('pc8',9),('pc9',10)))
_SnmpFddiPORTPCMState_Type.__name__=_C
_SnmpFddiPORTPCMState_Object=MibTableColumn
snmpFddiPORTPCMState=_SnmpFddiPORTPCMState_Object((1,3,6,1,2,1,10,15,4,2,1,21),_SnmpFddiPORTPCMState_Type())
snmpFddiPORTPCMState.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTPCMState.setStatus(_A)
class _SnmpFddiPORTPCWithhold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('m-m',2),(_H,3)))
_SnmpFddiPORTPCWithhold_Type.__name__=_C
_SnmpFddiPORTPCWithhold_Object=MibTableColumn
snmpFddiPORTPCWithhold=_SnmpFddiPORTPCWithhold_Object((1,3,6,1,2,1,10,15,4,2,1,22),_SnmpFddiPORTPCWithhold_Type())
snmpFddiPORTPCWithhold.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTPCWithhold.setStatus(_A)
class _SnmpFddiPORTLerCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiPORTLerCondition_Type.__name__=_C
_SnmpFddiPORTLerCondition_Object=MibTableColumn
snmpFddiPORTLerCondition=_SnmpFddiPORTLerCondition_Object((1,3,6,1,2,1,10,15,4,2,1,23),_SnmpFddiPORTLerCondition_Type())
snmpFddiPORTLerCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTLerCondition.setStatus(_A)
_SnmpFddiPORTChipSet_Type=ObjectIdentifier
_SnmpFddiPORTChipSet_Object=MibTableColumn
snmpFddiPORTChipSet=_SnmpFddiPORTChipSet_Object((1,3,6,1,2,1,10,15,4,2,1,24),_SnmpFddiPORTChipSet_Type())
snmpFddiPORTChipSet.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiPORTChipSet.setStatus(_A)
class _SnmpFddiPORTAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),('maintPORT',2),('enablePORT',3),('disablePORT',4),('startPORT',5),('stopPORT',6)))
_SnmpFddiPORTAction_Type.__name__=_C
_SnmpFddiPORTAction_Object=MibTableColumn
snmpFddiPORTAction=_SnmpFddiPORTAction_Object((1,3,6,1,2,1,10,15,4,2,1,25),_SnmpFddiPORTAction_Type())
snmpFddiPORTAction.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiPORTAction.setStatus(_A)
_SnmpFddiATTACHMENT_ObjectIdentity=ObjectIdentity
snmpFddiATTACHMENT=_SnmpFddiATTACHMENT_ObjectIdentity((1,3,6,1,2,1,10,15,5))
class _SnmpFddiATTACHMENTNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SnmpFddiATTACHMENTNumber_Type.__name__=_C
_SnmpFddiATTACHMENTNumber_Object=MibScalar
snmpFddiATTACHMENTNumber=_SnmpFddiATTACHMENTNumber_Object((1,3,6,1,2,1,10,15,5,1),_SnmpFddiATTACHMENTNumber_Type())
snmpFddiATTACHMENTNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiATTACHMENTNumber.setStatus(_A)
_SnmpFddiATTACHMENTTable_Object=MibTable
snmpFddiATTACHMENTTable=_SnmpFddiATTACHMENTTable_Object((1,3,6,1,2,1,10,15,5,2))
if mibBuilder.loadTexts:snmpFddiATTACHMENTTable.setStatus(_A)
_SnmpFddiATTACHMENTEntry_Object=MibTableRow
snmpFddiATTACHMENTEntry=_SnmpFddiATTACHMENTEntry_Object((1,3,6,1,2,1,10,15,5,2,1))
snmpFddiATTACHMENTEntry.setIndexNames((0,_G,_O),(0,_G,_P))
if mibBuilder.loadTexts:snmpFddiATTACHMENTEntry.setStatus(_A)
class _SnmpFddiATTACHMENTSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiATTACHMENTSMTIndex_Type.__name__=_C
_SnmpFddiATTACHMENTSMTIndex_Object=MibTableColumn
snmpFddiATTACHMENTSMTIndex=_SnmpFddiATTACHMENTSMTIndex_Object((1,3,6,1,2,1,10,15,5,2,1,1),_SnmpFddiATTACHMENTSMTIndex_Type())
snmpFddiATTACHMENTSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiATTACHMENTSMTIndex.setStatus(_A)
class _SnmpFddiATTACHMENTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SnmpFddiATTACHMENTIndex_Type.__name__=_C
_SnmpFddiATTACHMENTIndex_Object=MibTableColumn
snmpFddiATTACHMENTIndex=_SnmpFddiATTACHMENTIndex_Object((1,3,6,1,2,1,10,15,5,2,1,2),_SnmpFddiATTACHMENTIndex_Type())
snmpFddiATTACHMENTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiATTACHMENTIndex.setStatus(_A)
class _SnmpFddiATTACHMENTClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('single-attachment',1),('dual-attachment',2),('concentrator',3)))
_SnmpFddiATTACHMENTClass_Type.__name__=_C
_SnmpFddiATTACHMENTClass_Object=MibTableColumn
snmpFddiATTACHMENTClass=_SnmpFddiATTACHMENTClass_Object((1,3,6,1,2,1,10,15,5,2,1,3),_SnmpFddiATTACHMENTClass_Type())
snmpFddiATTACHMENTClass.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiATTACHMENTClass.setStatus(_A)
class _SnmpFddiATTACHMENTOpticalBypassPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SnmpFddiATTACHMENTOpticalBypassPresent_Type.__name__=_C
_SnmpFddiATTACHMENTOpticalBypassPresent_Object=MibTableColumn
snmpFddiATTACHMENTOpticalBypassPresent=_SnmpFddiATTACHMENTOpticalBypassPresent_Object((1,3,6,1,2,1,10,15,5,2,1,4),_SnmpFddiATTACHMENTOpticalBypassPresent_Type())
snmpFddiATTACHMENTOpticalBypassPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiATTACHMENTOpticalBypassPresent.setStatus(_A)
_SnmpFddiATTACHMENTIMaxExpiration_Type=FddiTime
_SnmpFddiATTACHMENTIMaxExpiration_Object=MibTableColumn
snmpFddiATTACHMENTIMaxExpiration=_SnmpFddiATTACHMENTIMaxExpiration_Object((1,3,6,1,2,1,10,15,5,2,1,5),_SnmpFddiATTACHMENTIMaxExpiration_Type())
snmpFddiATTACHMENTIMaxExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiATTACHMENTIMaxExpiration.setStatus(_A)
class _SnmpFddiATTACHMENTInsertedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_Q,3)))
_SnmpFddiATTACHMENTInsertedStatus_Type.__name__=_C
_SnmpFddiATTACHMENTInsertedStatus_Object=MibTableColumn
snmpFddiATTACHMENTInsertedStatus=_SnmpFddiATTACHMENTInsertedStatus_Object((1,3,6,1,2,1,10,15,5,2,1,6),_SnmpFddiATTACHMENTInsertedStatus_Type())
snmpFddiATTACHMENTInsertedStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpFddiATTACHMENTInsertedStatus.setStatus(_A)
class _SnmpFddiATTACHMENTInsertPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_Q,3)))
_SnmpFddiATTACHMENTInsertPolicy_Type.__name__=_C
_SnmpFddiATTACHMENTInsertPolicy_Object=MibTableColumn
snmpFddiATTACHMENTInsertPolicy=_SnmpFddiATTACHMENTInsertPolicy_Object((1,3,6,1,2,1,10,15,5,2,1,7),_SnmpFddiATTACHMENTInsertPolicy_Type())
snmpFddiATTACHMENTInsertPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:snmpFddiATTACHMENTInsertPolicy.setStatus(_A)
_SnmpFddiChipSets_ObjectIdentity=ObjectIdentity
snmpFddiChipSets=_SnmpFddiChipSets_ObjectIdentity((1,3,6,1,2,1,10,15,6))
_SnmpFddiPHYChipSets_ObjectIdentity=ObjectIdentity
snmpFddiPHYChipSets=_SnmpFddiPHYChipSets_ObjectIdentity((1,3,6,1,2,1,10,15,6,1))
_SnmpFddiMACChipSets_ObjectIdentity=ObjectIdentity
snmpFddiMACChipSets=_SnmpFddiMACChipSets_ObjectIdentity((1,3,6,1,2,1,10,15,6,2))
_SnmpFddiPHYMACChipSets_ObjectIdentity=ObjectIdentity
snmpFddiPHYMACChipSets=_SnmpFddiPHYMACChipSets_ObjectIdentity((1,3,6,1,2,1,10,15,6,3))
mibBuilder.exportSymbols(_G,**{'FddiTime':FddiTime,'FddiResourceId':FddiResourceId,'FddiSMTStationIdType':FddiSMTStationIdType,'FddiMACLongAddressType':FddiMACLongAddressType,'fddi':fddi,'snmpFddiSMT':snmpFddiSMT,'snmpFddiSMTNumber':snmpFddiSMTNumber,'snmpFddiSMTTable':snmpFddiSMTTable,'snmpFddiSMTEntry':snmpFddiSMTEntry,_J:snmpFddiSMTIndex,'snmpFddiSMTStationId':snmpFddiSMTStationId,'snmpFddiSMTOpVersionId':snmpFddiSMTOpVersionId,'snmpFddiSMTHiVersionId':snmpFddiSMTHiVersionId,'snmpFddiSMTLoVersionId':snmpFddiSMTLoVersionId,'snmpFddiSMTMACCt':snmpFddiSMTMACCt,'snmpFddiSMTNonMasterCt':snmpFddiSMTNonMasterCt,'snmpFddiSMTMasterCt':snmpFddiSMTMasterCt,'snmpFddiSMTPathsAvailable':snmpFddiSMTPathsAvailable,'snmpFddiSMTConfigCapabilities':snmpFddiSMTConfigCapabilities,'snmpFddiSMTConfigPolicy':snmpFddiSMTConfigPolicy,'snmpFddiSMTConnectionPolicy':snmpFddiSMTConnectionPolicy,'snmpFddiSMTTNotify':snmpFddiSMTTNotify,'snmpFddiSMTStatusReporting':snmpFddiSMTStatusReporting,'snmpFddiSMTECMState':snmpFddiSMTECMState,'snmpFddiSMTCFState':snmpFddiSMTCFState,'snmpFddiSMTHoldState':snmpFddiSMTHoldState,'snmpFddiSMTRemoteDisconnectFlag':snmpFddiSMTRemoteDisconnectFlag,'snmpFddiSMTStationAction':snmpFddiSMTStationAction,'snmpFddiMAC':snmpFddiMAC,'snmpFddiMACNumber':snmpFddiMACNumber,'snmpFddiMACTable':snmpFddiMACTable,'snmpFddiMACEntry':snmpFddiMACEntry,_K:snmpFddiMACSMTIndex,_L:snmpFddiMACIndex,'snmpFddiMACFrameStatusCapabilities':snmpFddiMACFrameStatusCapabilities,'snmpFddiMACTMaxGreatestLowerBound':snmpFddiMACTMaxGreatestLowerBound,'snmpFddiMACTVXGreatestLowerBound':snmpFddiMACTVXGreatestLowerBound,'snmpFddiMACPathsAvailable':snmpFddiMACPathsAvailable,'snmpFddiMACCurrentPath':snmpFddiMACCurrentPath,'snmpFddiMACUpstreamNbr':snmpFddiMACUpstreamNbr,'snmpFddiMACOldUpstreamNbr':snmpFddiMACOldUpstreamNbr,'snmpFddiMACDupAddrTest':snmpFddiMACDupAddrTest,'snmpFddiMACPathsRequested':snmpFddiMACPathsRequested,'snmpFddiMACDownstreamPORTType':snmpFddiMACDownstreamPORTType,'snmpFddiMACSMTAddress':snmpFddiMACSMTAddress,'snmpFddiMACTReq':snmpFddiMACTReq,'snmpFddiMACTNeg':snmpFddiMACTNeg,'snmpFddiMACTMax':snmpFddiMACTMax,'snmpFddiMACTvxValue':snmpFddiMACTvxValue,'snmpFddiMACTMin':snmpFddiMACTMin,'snmpFddiMACCurrentFrameStatus':snmpFddiMACCurrentFrameStatus,'snmpFddiMACFrameCts':snmpFddiMACFrameCts,'snmpFddiMACErrorCts':snmpFddiMACErrorCts,'snmpFddiMACLostCts':snmpFddiMACLostCts,'snmpFddiMACFrameErrorThreshold':snmpFddiMACFrameErrorThreshold,'snmpFddiMACFrameErrorRatio':snmpFddiMACFrameErrorRatio,'snmpFddiMACRMTState':snmpFddiMACRMTState,'snmpFddiMACDaFlag':snmpFddiMACDaFlag,'snmpFddiMACUnaDaFlag':snmpFddiMACUnaDaFlag,'snmpFddiMACFrameCondition':snmpFddiMACFrameCondition,'snmpFddiMACChipSet':snmpFddiMACChipSet,'snmpFddiMACAction':snmpFddiMACAction,'snmpFddiPATH':snmpFddiPATH,'snmpFddiPORT':snmpFddiPORT,'snmpFddiPORTNumber':snmpFddiPORTNumber,'snmpFddiPORTTable':snmpFddiPORTTable,'snmpFddiPORTEntry':snmpFddiPORTEntry,_M:snmpFddiPORTSMTIndex,_N:snmpFddiPORTIndex,'snmpFddiPORTPCType':snmpFddiPORTPCType,'snmpFddiPORTPCNeighbor':snmpFddiPORTPCNeighbor,'snmpFddiPORTConnectionPolicies':snmpFddiPORTConnectionPolicies,'snmpFddiPORTRemoteMACIndicated':snmpFddiPORTRemoteMACIndicated,'snmpFddiPORTCEState':snmpFddiPORTCEState,'snmpFddiPORTPathsRequested':snmpFddiPORTPathsRequested,'snmpFddiPORTMACPlacement':snmpFddiPORTMACPlacement,'snmpFddiPORTAvailablePaths':snmpFddiPORTAvailablePaths,'snmpFddiPORTMACLoopTime':snmpFddiPORTMACLoopTime,'snmpFddiPORTTBMax':snmpFddiPORTTBMax,'snmpFddiPORTBSFlag':snmpFddiPORTBSFlag,'snmpFddiPORTLCTFailCts':snmpFddiPORTLCTFailCts,'snmpFddiPORTLerEstimate':snmpFddiPORTLerEstimate,'snmpFddiPORTLemRejectCts':snmpFddiPORTLemRejectCts,'snmpFddiPORTLemCts':snmpFddiPORTLemCts,'snmpFddiPORTLerCutoff':snmpFddiPORTLerCutoff,'snmpFddiPORTLerAlarm':snmpFddiPORTLerAlarm,'snmpFddiPORTConnectState':snmpFddiPORTConnectState,'snmpFddiPORTPCMState':snmpFddiPORTPCMState,'snmpFddiPORTPCWithhold':snmpFddiPORTPCWithhold,'snmpFddiPORTLerCondition':snmpFddiPORTLerCondition,'snmpFddiPORTChipSet':snmpFddiPORTChipSet,'snmpFddiPORTAction':snmpFddiPORTAction,'snmpFddiATTACHMENT':snmpFddiATTACHMENT,'snmpFddiATTACHMENTNumber':snmpFddiATTACHMENTNumber,'snmpFddiATTACHMENTTable':snmpFddiATTACHMENTTable,'snmpFddiATTACHMENTEntry':snmpFddiATTACHMENTEntry,_O:snmpFddiATTACHMENTSMTIndex,_P:snmpFddiATTACHMENTIndex,'snmpFddiATTACHMENTClass':snmpFddiATTACHMENTClass,'snmpFddiATTACHMENTOpticalBypassPresent':snmpFddiATTACHMENTOpticalBypassPresent,'snmpFddiATTACHMENTIMaxExpiration':snmpFddiATTACHMENTIMaxExpiration,'snmpFddiATTACHMENTInsertedStatus':snmpFddiATTACHMENTInsertedStatus,'snmpFddiATTACHMENTInsertPolicy':snmpFddiATTACHMENTInsertPolicy,'snmpFddiChipSets':snmpFddiChipSets,'snmpFddiPHYChipSets':snmpFddiPHYChipSets,'snmpFddiMACChipSets':snmpFddiMACChipSets,'snmpFddiPHYMACChipSets':snmpFddiPHYMACChipSets})